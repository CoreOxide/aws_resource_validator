# Voiceid Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:voiceid.+:[0-9]{12}:domain/[a-zA-Z0-9]{22}$`
- **Min Length**: 1
- **Max Length**: 1011

### Arn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:voiceid.+:[0-9]{12}:domain/[a-zA-Z0-9]{22}$`

### ClientTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### CustomerSpeakerId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
- **Min Length**: 1
- **Max Length**: 256

### Description
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### DomainId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{22}$`
- **Min Length**: 22
- **Max Length**: 22

### DomainName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
- **Min Length**: 1
- **Max Length**: 256

### FraudsterId
- **Type**: string
- **Pattern**: `^id#[a-zA-Z0-9]{22}$`
- **Min Length**: 25
- **Max Length**: 25

### GeneratedFraudsterId
- **Type**: string
- **Pattern**: `^id#[a-zA-Z0-9]{22}$`
- **Min Length**: 25
- **Max Length**: 25

### GeneratedSpeakerId
- **Type**: string
- **Pattern**: `^id#[a-zA-Z0-9]{22}$`
- **Min Length**: 25
- **Max Length**: 25

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
- **Min Length**: 20
- **Max Length**: 2048

### JobId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{22}$`
- **Min Length**: 22
- **Max Length**: 22

### JobName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
- **Min Length**: 1
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `^\p{ASCII}{0,8192}$`
- **Min Length**: 0
- **Max Length**: 8192

### S3Uri
- **Type**: string
- **Pattern**: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
- **Min Length**: 0
- **Max Length**: 1024

### SessionId
- **Type**: string
- **Pattern**: `^id#[a-zA-Z0-9]{22}$`
- **Min Length**: 25
- **Max Length**: 25

### SessionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
- **Min Length**: 1
- **Max Length**: 36

### SessionNameOrId
- **Type**: string
- **Pattern**: `^(id#[a-zA-Z0-9]{22}|[a-zA-Z0-9][a-zA-Z0-9_-]*)$`
- **Min Length**: 1
- **Max Length**: 36

### SpeakerId
- **Type**: string
- **Pattern**: `^(id#[a-zA-Z0-9]{22}|[a-zA-Z0-9][a-zA-Z0-9_-]*)$`
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

### UniqueIdLarge
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{22}$`
- **Min Length**: 22
- **Max Length**: 22

### WatchlistDescription
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 1024

### WatchlistId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{22}$`
- **Min Length**: 22
- **Max Length**: 22

### WatchlistName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
- **Min Length**: 1
- **Max Length**: 256


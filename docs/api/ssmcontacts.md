# Ssmcontacts Service

### AcceptCode
- **Type**: string
- **Pattern**: `^[0-9]*$`
- **Min Length**: 6
- **Max Length**: 10

### ActivationCode
- **Type**: string
- **Pattern**: `^[0-9]*$`
- **Min Length**: 6
- **Max Length**: 10

### ChannelName
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.\-]*$`
- **Min Length**: 1
- **Max Length**: 255

### ContactAlias
- **Type**: string
- **Pattern**: `^[a-z0-9_\-]*$`
- **Min Length**: 1
- **Max Length**: 255

### ContactName
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.\-]*$`
- **Min Length**: 0
- **Max Length**: 255

### Content
- **Type**: string
- **Pattern**: `^[.\s\S]*$`
- **Min Length**: 1
- **Max Length**: 8192

### IdempotencyToken
- **Type**: string
- **Pattern**: `^[\\\/a-zA-Z0-9_+=\-]*$`
- **Max Length**: 2048

### IncidentId
- **Type**: string
- **Pattern**: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
- **Max Length**: 1024

### Member
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 512

### PaginationToken
- **Type**: string
- **Pattern**: `^[\\\/a-zA-Z0-9_+=\-]*$`
- **Max Length**: 2048

### Policy
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 395000

### PublicContent
- **Type**: string
- **Pattern**: `^[.\s\S]*$`
- **Min Length**: 1
- **Max Length**: 8192

### PublicSubject
- **Type**: string
- **Pattern**: `^[.\s\S]*$`
- **Min Length**: 1
- **Max Length**: 2048

### ReceiptInfo
- **Type**: string
- **Pattern**: `^[.\s\S]*$`
- **Min Length**: 1
- **Max Length**: 2048

### RotationName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-\s\.]*$`
- **Min Length**: 1
- **Max Length**: 255

### Sender
- **Type**: string
- **Pattern**: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
- **Max Length**: 255

### SsmContactsArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-]+)*`
- **Min Length**: 1
- **Max Length**: 2048

### StopReason
- **Type**: string
- **Pattern**: `^[.\s\S]*$`
- **Max Length**: 255

### Subject
- **Type**: string
- **Pattern**: `^[.\s\S]*$`
- **Min Length**: 1
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `^[\\\/a-zA-Z0-9_+=\-]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.:\/=+\-@]*$`
- **Min Length**: 1
- **Max Length**: 256

### TimeZoneId
- **Type**: string
- **Pattern**: `^[:a-zA-Z0-9_\-\s\.\\/]*$`
- **Min Length**: 1
- **Max Length**: 255

### Uuid
- **Type**: string
- **Pattern**: `([a-fA-Z0-9]{8,11}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}){1}`
- **Min Length**: 36
- **Max Length**: 39


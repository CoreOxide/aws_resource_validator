# Securityir Service

### AWSAccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`
- **Min Length**: 12
- **Max Length**: 12

### Arn
- **Type**: string
- **Pattern**: `arn:aws:security-ir:\w+?-\w+?-\d+:[0-9]{12}:(membership/m-[a-z0-9]{10,32}|case/[0-9]{10})`
- **Min Length**: 12
- **Max Length**: 1010

### AttachmentId
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}`

### AwsService
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 -.():]+`
- **Min Length**: 3
- **Max Length**: 50

### CaseArn
- **Type**: string
- **Pattern**: `arn:aws:security-ir:\w+?-\w+?-\d+:[0-9]{12}:case/[0-9]{10}`
- **Min Length**: 12
- **Max Length**: 80

### CaseId
- **Type**: string
- **Pattern**: `\d{10,32}.*`
- **Min Length**: 10
- **Max Length**: 32

### CommentId
- **Type**: string
- **Pattern**: `\d{6}`
- **Min Length**: 6
- **Max Length**: 6

### EmailAddress
- **Type**: string
- **Pattern**: `[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*`
- **Min Length**: 6
- **Max Length**: 254

### FileName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._-]+`
- **Min Length**: 1
- **Max Length**: 255

### IPAddress
- **Type**: string
- **Pattern**: `(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|(?:(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4})|(?:(?:[A-F0-9]{1,4}:){6}(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))`

### MembershipArn
- **Type**: string
- **Pattern**: `arn:aws:security-ir:\w+?-\w+?-\d+:[0-9]{12}:membership/m-[a-z0-9]{10,32}`
- **Min Length**: 12
- **Max Length**: 80

### MembershipId
- **Type**: string
- **Pattern**: `m-[a-z0-9]{10,32}`
- **Min Length**: 12
- **Max Length**: 34

### PrincipalId
- **Type**: string
- **Pattern**: `.*(^internal:midway:([a-z]{3,8}|svc-mw-[0-9]{12}[a-zA-Z0-9-]{5,20})$)|(^external:aws:\d{12}$).*`

### Url
- **Type**: string
- **Pattern**: `https?://(?:www.)?[a-zA-Z0-9@:._+~#=-]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_+.~#?&/=]{0,2048})`


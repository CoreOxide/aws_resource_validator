# Supportapp Service

### awsAccountAlias
- **Type**: string
- **Pattern**: `^[\w\- ]+$`
- **Min Length**: 1
- **Max Length**: 30

### channelId
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 256

### channelName
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 256

### paginationToken
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 256

### roleArn
- **Type**: string
- **Pattern**: `^arn:aws:iam::[0-9]{12}:role/(.+)$`
- **Min Length**: 31
- **Max Length**: 2048

### teamId
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 256

### teamName
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 256


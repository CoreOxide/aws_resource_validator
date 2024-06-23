# Codestarnotifications Service

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[\w:/-]+$`
- **Min Length**: 1
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `^[\w/+=]+$`

### NotificationRuleArn
- **Type**: string
- **Pattern**: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`

### NotificationRuleName
- **Type**: string
- **Pattern**: `[A-Za-z0-9\-_ ]+$`
- **Min Length**: 1
- **Max Length**: 64

### NotificationRuleResource
- **Type**: string
- **Pattern**: `^arn:aws[^:\s]*:[^:\s]*:[^:\s]*:[0-9]{12}:[^\s]+$`

### ResourceType
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9-])+$`
- **Min Length**: 1

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Max Length**: 256

### TargetType
- **Type**: string
- **Pattern**: `^[A-Za-z]+$`


# Notificationscontacts Service

### EmailContactAddress
- **Type**: string
- **Pattern**: `(.+)@(.+)`
- **Min Length**: 6
- **Max Length**: 254

### EmailContactArn
- **Type**: string
- **Pattern**: `arn:aws:notifications-contacts::[0-9]{12}:emailcontact/[a-z0-9]{27}`

### EmailContactName
- **Type**: string
- **Pattern**: `.*[\w-.~]+.*`
- **Min Length**: 1
- **Max Length**: 64

### SensitiveEmailContactAddress
- **Type**: string
- **Pattern**: `(.+)@(.+)`
- **Min Length**: 6
- **Max Length**: 254

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:).{1,128}`

### Token
- **Type**: string
- **Pattern**: `[a-z0-9]{7}`
- **Min Length**: 7
- **Max Length**: 7


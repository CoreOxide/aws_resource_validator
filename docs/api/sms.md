# Sms Service

### AppIdWithValidation
- **Type**: string
- **Pattern**: `^app-[0-9a-f]{17}$`

### InstanceId
- **Type**: string
- **Pattern**: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`

### NonEmptyStringWithMaxLen255
- **Type**: string
- **Pattern**: `^[\S]+$`
- **Min Length**: 1
- **Max Length**: 255

### ValidationId
- **Type**: string
- **Pattern**: `^val-[0-9a-f]{17}$`


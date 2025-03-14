# Budgets Service

### AccountId
- **Type**: string
- **Pattern**: `\d{12}`
- **Min Length**: 12
- **Max Length**: 12

### ActionId
- **Type**: string
- **Pattern**: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### BudgetName
- **Type**: string
- **Pattern**: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
- **Min Length**: 1
- **Max Length**: 100

### DimensionValue
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 2147483647

### GenericString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2147483647

### Group
- **Type**: string
- **Pattern**: `^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 640

### InstanceId
- **Type**: string
- **Pattern**: `^i-(\w{8}|\w{17})$|^[a-zA-Z]([\w-]{0,61}\w)?$`
- **Min Length**: 1
- **Max Length**: 63

### NumericValue
- **Type**: string
- **Pattern**: `([0-9]*\.)?[0-9]+`
- **Min Length**: 1
- **Max Length**: 2147483647

### PolicyArn
- **Type**: string
- **Pattern**: `^arn:aws(-cn|-us-gov|-iso|-iso-[a-z]{1})?:iam::(\d{12}|aws):policy(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$`
- **Min Length**: 25
- **Max Length**: 684

### PolicyId
- **Type**: string
- **Pattern**: `^p-[0-9a-zA-Z_]{8,128}$`
- **Min Length**: 10
- **Max Length**: 130

### Region
- **Type**: string
- **Pattern**: `^\w{2}-\w+(-\w+)?-\d$`
- **Min Length**: 9
- **Max Length**: 20

### Role
- **Type**: string
- **Pattern**: `^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 576

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-cn|-us-gov|-iso|-iso-[a-z]{1})?:iam::\d{12}:role(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$`
- **Min Length**: 32
- **Max Length**: 618

### SubscriberAddress
- **Type**: string
- **Pattern**: `(.*[\n\r\t\f\ ]?)*`
- **Min Length**: 1
- **Max Length**: 2147483647

### TargetId
- **Type**: string
- **Pattern**: `^(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)|(\d{12})`
- **Min Length**: 12
- **Max Length**: 68

### UnitValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 2147483647

### User
- **Type**: string
- **Pattern**: `^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 576


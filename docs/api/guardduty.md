# Guardduty Service

### GuardDutyArn
- **Type**: string
- **Pattern**: `^arn:[A-Za-z_.-]{1,20}:guardduty:[A-Za-z0-9_/.-]{0,63}:\d+:detector/[A-Za-z0-9_/.-]{32,264}$`

### InstanceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):[a-z]+:[a-z]+(-[0-9]+|-[a-z]+)+:([0-9]{12}):[a-z\-]+\/[a-zA-Z0-9]*$`

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:[A-Za-z-]+:[A-Za-z0-9]+:[A-Za-z0-9-]+:\d+:(([A-Za-z0-9-]+)[:\/])?[A-Za-z0-9-]*$`

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128


# Dlm Service

### ActionName
- **Type**: string
- **Pattern**: `[0-9A-Za-z _-]+`
- **Min Length**: 0
- **Max Length**: 120

### AvailabilityZone
- **Type**: string
- **Pattern**: `([a-z]+-){2,3}\d[a-z]`
- **Min Length**: 0
- **Max Length**: 16

### AwsAccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 12
- **Max Length**: 12

### CmkArn
- **Type**: string
- **Pattern**: `arn:aws(-[a-z]{1,3}){0,2}:kms:([a-z]+-){2,3}\d:\d+:key/.*`
- **Min Length**: 0
- **Max Length**: 2048

### CronExpression
- **Type**: string
- **Pattern**: `cron\([^\n]{11,100}\)`
- **Min Length**: 17
- **Max Length**: 106

### DescriptionRegex
- **Type**: string
- **Pattern**: `[\p{all}]*`
- **Min Length**: 0
- **Max Length**: 1000

### ExecutionHandler
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_\-.]{3,128}|[a-zA-Z0-9_\-.:/]{3,200}|[A-Z0-9_]+)$`
- **Min Length**: 0
- **Max Length**: 200

### ExecutionRoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[a-z]{1,3}){0,2}:iam::\d+:role/.*`
- **Min Length**: 0
- **Max Length**: 2048

### PolicyArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]{1,3}){0,2}:dlm:[A-Za-z0-9_/.-]{0,63}:\d+:policy/[0-9A-Za-z_-]{1,128}$`
- **Min Length**: 0
- **Max Length**: 2048

### PolicyDescription
- **Type**: string
- **Pattern**: `[0-9A-Za-z _-]+`
- **Min Length**: 0
- **Max Length**: 500

### PolicyId
- **Type**: string
- **Pattern**: `policy-[a-f0-9]+`
- **Min Length**: 0
- **Max Length**: 64

### ScheduleName
- **Type**: string
- **Pattern**: `[0-9A-Za-z _-]+`
- **Min Length**: 0
- **Max Length**: 120

### StatusMessage
- **Type**: string
- **Pattern**: `[\p{all}]*`
- **Min Length**: 0
- **Max Length**: 500

### String
- **Type**: string
- **Pattern**: `[\p{all}]*`
- **Min Length**: 0
- **Max Length**: 500

### TagFilter
- **Type**: string
- **Pattern**: `[\p{all}]*`
- **Min Length**: 0
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\p{all}]*`
- **Max Length**: 256

### Target
- **Type**: string
- **Pattern**: `^[\w:\-\/\*]+$`
- **Min Length**: 0
- **Max Length**: 2048

### TargetRegion
- **Type**: string
- **Pattern**: `([a-z]+-){2,3}\d`
- **Min Length**: 0
- **Max Length**: 16

### Time
- **Type**: string
- **Pattern**: `^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
- **Min Length**: 5
- **Max Length**: 5


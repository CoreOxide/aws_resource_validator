# Customerprofiles Service

### name
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 64

### BucketName
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 3
- **Max Length**: 63

### BucketPrefix
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 512

### ConnectorProfileName
- **Type**: string
- **Pattern**: `[\w/!@#+=.-]+`
- **Max Length**: 256

### DatetimeTypeFieldName
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### DestinationField
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### FlowDescription
- **Type**: string
- **Pattern**: `[\w!@#\-.?,\s]*`
- **Max Length**: 2048

### FlowName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][\w!@#.-]+`
- **Max Length**: 256

### JobScheduleTime
- **Type**: string
- **Pattern**: `^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
- **Min Length**: 3
- **Max Length**: 5

### KmsArn
- **Type**: string
- **Pattern**: `arn:aws:kms:.*:[0-9]+:.*`
- **Min Length**: 20
- **Max Length**: 2048

### Object
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 512

### Property
- **Type**: string
- **Pattern**: `.+`
- **Max Length**: 2048

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam:.*:[0-9]+:.*`
- **Max Length**: 512

### ScheduleExpression
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### TagArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9]{1,10}:profile`
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### Timezone
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256

### attributeName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 64

### displayName
- **Type**: string
- **Pattern**: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`
- **Min Length**: 1
- **Max Length**: 255

### s3BucketName
- **Type**: string
- **Pattern**: `^[a-z0-9.-]+$`
- **Min Length**: 3
- **Max Length**: 63

### s3KeyName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### s3KeyNameCustomerOutputConfig
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 800

### stringTo2048
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 2048

### typeName
- **Type**: string
- **Pattern**: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
- **Min Length**: 1
- **Max Length**: 255

### uuid
- **Type**: string
- **Pattern**: `[a-f0-9]{32}`


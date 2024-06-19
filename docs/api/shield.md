# Shield Service

### AttackId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\\-]*`
- **Min Length**: 1
- **Max Length**: 128

### ContactNotes
- **Type**: string
- **Pattern**: `^[\w\s\.\-,:/()+@]*$`
- **Min Length**: 1
- **Max Length**: 1024

### EmailAddress
- **Type**: string
- **Pattern**: `^\S+@\S+\.\S+$`
- **Min Length**: 1
- **Max Length**: 150

### HealthCheckArn
- **Type**: string
- **Pattern**: `^arn:aws:route53:::healthcheck/\S{36}$`
- **Min Length**: 1
- **Max Length**: 2048

### LogBucket
- **Type**: string
- **Pattern**: `^([a-z]|(\d(?!\d{0,2}\.\d{1,3}\.\d{1,3}\.\d{1,3})))([a-z\d]|(\.(?!(\.|-)))|(-(?!\.))){1,61}[a-z\d]$`
- **Min Length**: 3
- **Max Length**: 63

### PhoneNumber
- **Type**: string
- **Pattern**: `^\+[1-9]\d{1,14}$`
- **Min Length**: 1
- **Max Length**: 16

### ProtectionGroupId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\\-]*`
- **Min Length**: 1
- **Max Length**: 36

### ProtectionId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\\-]*`
- **Min Length**: 36
- **Max Length**: 36

### ProtectionName
- **Type**: string
- **Pattern**: `[ a-zA-Z0-9_\\.\\-]*`
- **Min Length**: 1
- **Max Length**: 128

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:aws.*`
- **Min Length**: 1
- **Max Length**: 2048

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
- **Min Length**: 1
- **Max Length**: 2048

### Token
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 4096


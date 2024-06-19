# Ec2instanceconnect Service

### AvailabilityZone
- **Type**: string
- **Pattern**: `^(\w+-){2,3}\d+\w+$`
- **Min Length**: 6
- **Max Length**: 32

### InstanceId
- **Type**: string
- **Pattern**: `^i-[a-f0-9]+$`
- **Min Length**: 10
- **Max Length**: 32

### InstanceOSUser
- **Type**: string
- **Pattern**: `(^[A-Za-z_][A-Za-z0-9\@\._-]{0,30}[A-Za-z0-9\$_-]?$)|(^(?=.{2,32}$)[0-9]{1,32}[A-Za-z\@\._-][A-Za-z0-9\@\._-]*[A-Za-z0-9\$_-]?$)`
- **Min Length**: 1
- **Max Length**: 32


# Devicefarm Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `^arn:aws:devicefarm:.+`
- **Min Length**: 32
- **Max Length**: 1011

### DeviceFarmArn
- **Type**: string
- **Pattern**: `^arn:aws:devicefarm:.+`
- **Min Length**: 32
- **Max Length**: 1011

### DeviceProxyHost
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9])([a-zA-Z0-9-.]+)([a-zA-Z0-9])$`
- **Min Length**: 1
- **Max Length**: 255

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 4096

### ResourceDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2048

### ResourceId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### ResourceName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 64

### SecurityGroupId
- **Type**: string
- **Pattern**: `^sg-[0-9a-fA-F]{8,}$`
- **Min Length**: 1
- **Max Length**: 4096

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-[0-9a-fA-F]{8,}$`
- **Min Length**: 1
- **Max Length**: 4096


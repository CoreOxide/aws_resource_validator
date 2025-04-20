# Networkflowmonitor Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`
- **Min Length**: 1
- **Max Length**: 12

### Arn
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 20
- **Max Length**: 2048

### InstanceId
- **Type**: string
- **Pattern**: `i-[a-zA-Z0-9]{8,32}`

### MonitorArn
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 20
- **Max Length**: 512

### ResourceName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 255

### SubnetId
- **Type**: string
- **Pattern**: `subnet-[a-zA-Z0-9]{8,32}`

### UuidString
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### VpcId
- **Type**: string
- **Pattern**: `vpc-[a-zA-Z0-9]{8,32}`


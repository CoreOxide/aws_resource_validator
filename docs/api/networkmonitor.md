# Networkmonitor Service

### Arn
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 20
- **Max Length**: 2048

### MonitorArn
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 20
- **Max Length**: 512

### ProbeId
- **Type**: string
- **Pattern**: `probe-[a-z0-9A-Z-]{21,64}`

### ResourceName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 200

### VpcId
- **Type**: string
- **Pattern**: `vpc-[a-zA-Z0-9]{8,32}`


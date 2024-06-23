# Ivschat Service

### BucketName
- **Type**: string
- **Pattern**: `^[a-z0-9-.]+$`
- **Min Length**: 3
- **Max Length**: 63

### DeliveryStreamName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 64

### ID
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 12
- **Max Length**: 12

### LambdaArn
- **Type**: string
- **Pattern**: `^$|^arn:aws:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
- **Min Length**: 0
- **Max Length**: 170

### LogGroupName
- **Type**: string
- **Pattern**: `^[\.\-_/#A-Za-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 512

### LoggingConfigurationArn
- **Type**: string
- **Pattern**: `^arn:aws:ivschat:[a-z0-9-]+:[0-9]+:logging-configuration/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### LoggingConfigurationID
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 12
- **Max Length**: 12

### LoggingConfigurationIdentifier
- **Type**: string
- **Pattern**: `^arn:aws:ivschat:[a-z0-9-]+:[0-9]+:logging-configuration/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### LoggingConfigurationName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 128

### MessageID
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 12
- **Max Length**: 12

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:aws:ivschat:[a-z0-9-]+:[0-9]+:[a-z-]/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### ResourceId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`

### RoomArn
- **Type**: string
- **Pattern**: `^arn:aws:ivschat:[a-z0-9-]+:[0-9]+:room/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### RoomID
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 12
- **Max Length**: 12

### RoomIdentifier
- **Type**: string
- **Pattern**: `^arn:aws:ivschat:[a-z0-9-]+:[0-9]+:room/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### RoomName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 128


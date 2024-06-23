# Greengrassv2 Service

### ClientTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 64

### ComponentARN
- **Type**: string
- **Pattern**: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):components:[^:]+`

### ComponentVersionARN
- **Type**: string
- **Pattern**: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):components:[^:]+:versions:[^:]+`

### GenericV2ARN
- **Type**: string
- **Pattern**: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):(components|deployments|coreDevices):.*`

### IoTJobARN
- **Type**: string
- **Pattern**: `arn:[^:]*:iot:[^:]+:[0-9]+:job/.+`

### TargetARN
- **Type**: string
- **Pattern**: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`

### ThingGroupARN
- **Type**: string
- **Pattern**: `arn:[^:]*:iot:[^:]*:[0-9]+:thinggroup/.+`


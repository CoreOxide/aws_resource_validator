# Scheduler Service

### ClientToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### DeadLetterConfigArnString
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:sqs:[a-z0-9\-]+:\d{12}:[a-zA-Z0-9\-_]+$`
- **Min Length**: 1
- **Max Length**: 1600

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:kms:[a-z0-9\-]+:\d{12}:(key|alias)\/[0-9a-zA-Z-_]*$`
- **Min Length**: 1
- **Max Length**: 2048

### Name
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z-_.]+$`
- **Min Length**: 1
- **Max Length**: 64

### NamePrefix
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z-_.]+$`
- **Min Length**: 1
- **Max Length**: 64

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:iam::\d{12}:role\/[\w+=,.@\/-]+$`
- **Min Length**: 1
- **Max Length**: 1600

### SageMakerPipelineParameterName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9\-_]*$`
- **Min Length**: 1
- **Max Length**: 256

### ScheduleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule\/[0-9a-zA-Z-_.]+\/[0-9a-zA-Z-_.]+$`
- **Min Length**: 1
- **Max Length**: 1224

### ScheduleGroupArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule-group\/[0-9a-zA-Z-_.]+$`
- **Min Length**: 1
- **Max Length**: 1224

### ScheduleGroupName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z-_.]+$`
- **Min Length**: 1
- **Max Length**: 64

### ScheduleGroupNamePrefix
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z-_.]+$`
- **Min Length**: 1
- **Max Length**: 64

### Source
- **Type**: string
- **Pattern**: `^(?=[/\.\-_A-Za-z0-9]+)((?!aws\.).*)|(\$(\.[\w_-]+(\[(\d+|\*)\])*)*)$`
- **Min Length**: 1
- **Max Length**: 256

### TagResourceArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule-group\/[0-9a-zA-Z-_.]+$`
- **Min Length**: 1
- **Max Length**: 1011


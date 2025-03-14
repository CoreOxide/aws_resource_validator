# Secretsmanager Service

### DurationType
- **Type**: string
- **Pattern**: `[0-9h]+`
- **Min Length**: 2
- **Max Length**: 3

### FilterValueStringType
- **Type**: string
- **Pattern**: `^\!?[a-zA-Z0-9 :_@\/\+\=\.\-\!]*$`
- **Max Length**: 512

### RegionType
- **Type**: string
- **Pattern**: `^([a-z]+-)+\d+$`
- **Min Length**: 1
- **Max Length**: 128

### RotationTokenType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+$`
- **Min Length**: 36
- **Max Length**: 256

### ScheduleExpressionType
- **Type**: string
- **Pattern**: `[0-9A-Za-z\(\)#\?\*\-\/, ]+`
- **Min Length**: 1
- **Max Length**: 256


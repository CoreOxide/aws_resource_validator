# Iotevents Service

### AlarmModelName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 128

### AttributeJsonPath
- **Type**: string
- **Pattern**: `^((`[\w\- ]+`)|([\w\-]+))(\.((`[\w- ]+`)|([\w\-]+)))*$`
- **Min Length**: 1
- **Max Length**: 128

### DetectorModelName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 128

### FirehoseSeparator
- **Type**: string
- **Pattern**: `([\n\t])|(\r\n)|(,)`

### InputName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 128

### KeyValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-_:]+$`
- **Min Length**: 1
- **Max Length**: 128

### VariableName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 128


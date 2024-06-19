# Iot1clickprojects Service

### DeviceTemplateName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 128

### PlacementName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 128

### ProjectArn
- **Type**: string
- **Pattern**: `^arn:aws:iot1click:[A-Za-z0-9_/.-]{0,63}:\d+:projects/[0-9A-Za-z_-]{1,128}$`

### ProjectName
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_-]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128


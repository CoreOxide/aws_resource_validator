# Privatenetworks Service

### Arn
- **Type**: string
- **Pattern**: `^arn:aws:private-networks:[a-z0-9-]+:[^:]*:.*$`

### DeviceIdentifierImsiString
- **Type**: string
- **Pattern**: `^[0-9]{15}$`

### Name
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z-]*$`
- **Min Length**: 1
- **Max Length**: 64

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[^\x00-\x1f\x22]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[^\x00-\x1f\x22]*$`
- **Min Length**: 0
- **Max Length**: 256


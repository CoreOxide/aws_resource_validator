# Observabilityadmin Service

### AccountIdentifier
- **Type**: string
- **Pattern**: `[0-9]{12}`
- **Min Length**: 12
- **Max Length**: 12

### TagKey
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
- **Min Length**: 0
- **Max Length**: 256


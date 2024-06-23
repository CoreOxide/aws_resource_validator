# Migrationhubconfig Service

### ControlId
- **Type**: string
- **Pattern**: `^hrc-[a-z0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 50

### HomeRegion
- **Type**: string
- **Pattern**: `^([a-z]+)-([a-z]+)-([0-9]+)$`
- **Min Length**: 1
- **Max Length**: 50

### TargetId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### Token
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\+\=]{0,2048}$`
- **Min Length**: 0
- **Max Length**: 2048


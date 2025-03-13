# Codebuild Service

### FleetName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9\-_]{1,127}`
- **Min Length**: 2
- **Max Length**: 128

### KeyInput
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=@+\-]*)$`
- **Min Length**: 1
- **Max Length**: 127

### ProjectName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9\-_]{1,149}`
- **Min Length**: 2
- **Max Length**: 150

### ValueInput
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=@+\-]*)$`
- **Min Length**: 0
- **Max Length**: 255


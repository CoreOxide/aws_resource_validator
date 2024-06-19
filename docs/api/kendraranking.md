# Kendraranking Service

### ClientTokenName
- **Type**: string
- **Pattern**: `^$|[\x00-\x7F]+`
- **Min Length**: 1
- **Max Length**: 64

### Description
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 0
- **Max Length**: 1000

### DocumentBody
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 2048

### ErrorMessage
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 2048

### NextToken
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 800

### RescoreExecutionPlanArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### RescoreExecutionPlanId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]*`
- **Min Length**: 36
- **Max Length**: 36

### RescoreExecutionPlanName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### RescoreId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]`
- **Min Length**: 1
- **Max Length**: 36


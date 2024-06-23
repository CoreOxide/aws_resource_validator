# Backup Service

### AccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`

### BackupOptionKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\.]{1,50}$`

### BackupOptionValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\.]{1,50}$`

### BackupRuleName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\.]{1,50}$`

### BackupSelectionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\.]{1,50}$`

### BackupVaultName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]{2,50}$`

### FrameworkDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 1024

### FrameworkName
- **Type**: string
- **Pattern**: `[a-zA-Z][_a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 256

### ReportPlanDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 1024

### ReportPlanName
- **Type**: string
- **Pattern**: `[a-zA-Z][_a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 256

### ResourceType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\.]{1,50}$`


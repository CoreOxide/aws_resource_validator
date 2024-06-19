# Discovery Service

### AgentId
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 10
- **Max Length**: 20

### ApplicationDescription
- **Type**: string
- **Pattern**: `(^$|[\s\S]*\S[\s\S]*)`
- **Max Length**: 1000

### ApplicationId
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 200

### ApplicationName
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Max Length**: 127

### Condition
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 200

### ConfigurationId
- **Type**: string
- **Pattern**: `\S*`
- **Max Length**: 200

### ConfigurationsExportId
- **Type**: string
- **Pattern**: `\S*`
- **Max Length**: 200

### EC2InstanceType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\d\.\-]+`
- **Min Length**: 1
- **Max Length**: 25

### FilterName
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Max Length**: 1000

### FilterValue
- **Type**: string
- **Pattern**: `(^$|[\s\S]*\S[\s\S]*)`
- **Max Length**: 1000

### ImportTaskIdentifier
- **Type**: string
- **Pattern**: `^import-task-[a-fA-F0-9]{32}$`
- **Max Length**: 200

### ImportTaskName
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 255

### ImportURL
- **Type**: string
- **Pattern**: `\S+://\S+/[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 4000

### OrderByElementFieldName
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Max Length**: 1000

### String
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 10000

### StringMax255
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 255

### UUID
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

### UsageMetricBasisName
- **Type**: string
- **Pattern**: `^(p(\d{1,2}|100)|AVG|SPEC|MAX)$`

### UserPreferredRegion
- **Type**: string
- **Pattern**: `[a-z]{2}-[a-z\-]+-[0-9]+`
- **Min Length**: 1
- **Max Length**: 30


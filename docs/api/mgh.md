# Mgh Service

### ApplicationId
- **Type**: string
- **Pattern**: `^.{1,1600}$`
- **Min Length**: 1
- **Max Length**: 1600

### ConfigurationId
- **Type**: string
- **Pattern**: `^.{1,1600}$`
- **Min Length**: 1
- **Max Length**: 1600

### CreatedArtifactDescription
- **Type**: string
- **Pattern**: `^.{0,500}$`
- **Min Length**: 0
- **Max Length**: 500

### CreatedArtifactName
- **Type**: string
- **Pattern**: `arn:[a-z-]+:[a-z0-9-]+:(?:[a-z0-9-]+|):(?:[0-9]{12}|):.*`
- **Min Length**: 1
- **Max Length**: 1600

### DiscoveredResourceDescription
- **Type**: string
- **Pattern**: `^.{0,500}$`
- **Min Length**: 0
- **Max Length**: 500

### MigrationTaskName
- **Type**: string
- **Pattern**: `[^:|]+`
- **Min Length**: 1
- **Max Length**: 256

### ProgressUpdateStream
- **Type**: string
- **Pattern**: `[^/:|\000-\037]+`
- **Min Length**: 1
- **Max Length**: 50

### ResourceAttributeValue
- **Type**: string
- **Pattern**: `^.{1,256}$`
- **Min Length**: 1
- **Max Length**: 256

### ResourceName
- **Type**: string
- **Pattern**: `^.{1,1600}$`
- **Min Length**: 1
- **Max Length**: 1600

### SourceResourceDescription
- **Type**: string
- **Pattern**: `^.{0,500}$`
- **Min Length**: 0
- **Max Length**: 500

### StatusDetail
- **Type**: string
- **Pattern**: `^.{0,2500}$`
- **Min Length**: 0
- **Max Length**: 2500

### Token
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\+\=]{0,2048}$`
- **Min Length**: 0
- **Max Length**: 2048


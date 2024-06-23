# Marketplacedeployment Service

### Catalog
- **Type**: string
- **Pattern**: `^[a-zA-Z_-]+$`
- **Min Length**: 1
- **Max Length**: 64

### ClientToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/_+=.:@-]+$`
- **Min Length**: 32
- **Max Length**: 64

### DeploymentParameterName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/_+=.@-]+$`
- **Min Length**: 1
- **Max Length**: 400

### DeploymentParameterResourceIdentifier
- **Type**: string
- **Pattern**: `^dp-[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 32

### ResourceArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:*/-]+$`
- **Min Length**: 1
- **Max Length**: 2048

### ResourceId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_/-]+$`
- **Min Length**: 1
- **Max Length**: 64

### TagKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/_+=.:@-]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/_+=.:@-]+$`
- **Min Length**: 1
- **Max Length**: 256


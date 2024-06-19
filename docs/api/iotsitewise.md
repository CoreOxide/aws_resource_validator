# Iotsitewise Service

### ARN
- **Type**: string
- **Pattern**: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
- **Min Length**: 1
- **Max Length**: 1600

### ActionPayloadString
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`

### AssetPropertyAlias
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1
- **Max Length**: 2048

### CapabilityNamespace
- **Type**: string
- **Pattern**: `^[a-zA-Z]+:[a-zA-Z]+:[0-9]+$`
- **Min Length**: 1
- **Max Length**: 512

### ClientToken
- **Type**: string
- **Pattern**: `\S{36,64}`
- **Min Length**: 36
- **Max Length**: 64

### CustomID
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
- **Min Length**: 13
- **Max Length**: 139

### DashboardDefinition
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 0
- **Max Length**: 204800

### DefaultValue
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`

### Description
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1
- **Max Length**: 2048

### Email
- **Type**: string
- **Pattern**: `[^@]+@[^@]+`
- **Min Length**: 1
- **Max Length**: 255

### EntryId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 64

### ExternalId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
- **Min Length**: 2
- **Max Length**: 128

### ID
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### IdentityId
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 256

### Macro
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1
- **Max Length**: 256

### Name
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `[A-Za-z0-9+/=]+`
- **Min Length**: 1
- **Max Length**: 4096

### PortalClientId
- **Type**: string
- **Pattern**: `^[!-~]*`
- **Min Length**: 1
- **Max Length**: 256

### PropertyAlias
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1

### PropertyUnit
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1
- **Max Length**: 256

### QueryStatement
- **Type**: string
- **Pattern**: `^[\s\S]+$`
- **Min Length**: 1

### Resolution
- **Type**: string
- **Pattern**: `1m|15m|1h|1d`
- **Min Length**: 2
- **Max Length**: 3

### SSOApplicationId
- **Type**: string
- **Pattern**: `^[!-~]*`
- **Min Length**: 1
- **Max Length**: 64

### Url
- **Type**: string
- **Pattern**: `^(http|https)\://\S+`
- **Min Length**: 1
- **Max Length**: 256

### VariableName
- **Type**: string
- **Pattern**: `^[a-z][a-z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 64


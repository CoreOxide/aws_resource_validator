# Appfabric Service

### Arn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 1011

### Email
- **Type**: string
- **Pattern**: `[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*`
- **Min Length**: 0
- **Max Length**: 320

### Identifier
- **Type**: string
- **Pattern**: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 1
- **Max Length**: 1011

### RedirectUri
- **Type**: string
- **Pattern**: `https://[-a-zA-Z0-9-._~:/?#@!$&\'()*+,;=]+`
- **Min Length**: 0
- **Max Length**: 1024

### UUID
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`


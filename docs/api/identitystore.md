# Identitystore Service

### AttributePath
- **Type**: string
- **Pattern**: `\p{L}+(?:\.\p{L}+){0,2}`
- **Min Length**: 1
- **Max Length**: 255

### ExternalIdIdentifier
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 256

### ExternalIdIssuer
- **Type**: string
- **Pattern**: `(?!(?i)(arn|aws):)[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 100

### GroupDisplayName
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  ]+`
- **Min Length**: 1
- **Max Length**: 1024

### IdentityStoreId
- **Type**: string
- **Pattern**: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 1
- **Max Length**: 36

### NextToken
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9+=/:_]*`
- **Min Length**: 1
- **Max Length**: 65535

### RequestId
- **Type**: string
- **Pattern**: `[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
- **Min Length**: 1
- **Max Length**: 36

### ResourceId
- **Type**: string
- **Pattern**: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
- **Min Length**: 1
- **Max Length**: 47

### SensitiveStringType
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
- **Min Length**: 1
- **Max Length**: 1024

### UserName
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128


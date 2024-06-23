# Stepfunctions Service

### CharacterRestrictedName
- **Type**: string
- **Pattern**: `^(?=.*[a-zA-Z_\-\.])[a-zA-Z0-9_\-\.]+$`
- **Min Length**: 1
- **Max Length**: 80

### ClientToken
- **Type**: string
- **Pattern**: `[!-~]+`
- **Min Length**: 1
- **Max Length**: 64

### TraceHeader
- **Type**: string
- **Pattern**: `\p{ASCII}*`
- **Min Length**: 0
- **Max Length**: 256


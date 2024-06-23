# Managedblockchain Service

### ArnString
- **Type**: string
- **Pattern**: `^arn:.+:.+:.+:.+:.+`
- **Min Length**: 1
- **Max Length**: 1011

### NameString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 64

### NetworkMemberNameString
- **Type**: string
- **Pattern**: `^(?!-|[0-9])(?!.*-$)(?!.*?--)[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 64

### PasswordString
- **Type**: string
- **Pattern**: `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?!.*[@\'\\"/])[a-zA-Z0-9\S]*$`
- **Min Length**: 8
- **Max Length**: 32

### UsernameString
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9]*$`
- **Min Length**: 1
- **Max Length**: 16


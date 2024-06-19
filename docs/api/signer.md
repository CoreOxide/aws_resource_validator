# Signer Service

### AccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ProfileName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]{2,}`
- **Min Length**: 2
- **Max Length**: 64

### ProfileVersion
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{10}$`
- **Min Length**: 10
- **Max Length**: 10

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128


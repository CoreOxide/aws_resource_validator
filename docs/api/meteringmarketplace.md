# Meteringmarketplace Service

### CustomerAWSAccountId
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 255

### CustomerIdentifier
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 255

### NonEmptyString
- **Type**: string
- **Pattern**: `[\s\S]+`

### Nonce
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 255

### ProductCode
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9/=:_.@]*$`
- **Min Length**: 1
- **Max Length**: 255

### TagKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+ -=._:\/@]+$`
- **Min Length**: 1
- **Max Length**: 100

### TagValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+ -=._:\/@]+$`
- **Min Length**: 1
- **Max Length**: 256

### UsageDimension
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 255


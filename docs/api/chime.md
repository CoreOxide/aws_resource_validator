# Chime Service

### AccountName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 100

### Alpha2CountryCode
- **Type**: string
- **Pattern**: `[A-Z]{2}`

### CallingName
- **Type**: string
- **Pattern**: `^$|^[a-zA-Z0-9 ]{2,15}$`

### ClientRequestToken
- **Type**: string
- **Pattern**: `[-_a-zA-Z0-9]*`
- **Min Length**: 2
- **Max Length**: 64

### E164PhoneNumber
- **Type**: string
- **Pattern**: `^\+?[1-9]\d{1,14}$`

### EmailAddress
- **Type**: string
- **Pattern**: `.+@.+\..+`

### GuidString
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`

### JoinTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+/]+$`
- **Min Length**: 2
- **Max Length**: 2048

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`

### TollFreePrefix
- **Type**: string
- **Pattern**: `^8(00|33|44|55|66|77|88)$`
- **Min Length**: 3
- **Max Length**: 3


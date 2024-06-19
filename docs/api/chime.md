# Chime Service

### AccountName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 100

### Alpha2CountryCode
- **Type**: string
- **Pattern**: `[A-Z]{2}`

### AreaCode
- **Type**: string
- **Pattern**: `^$|^[0-9]{3,3}$`

### Arn
- **Type**: string
- **Pattern**: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 1024

### CallingName
- **Type**: string
- **Pattern**: `^$|^[a-zA-Z0-9 ]{2,15}$`

### ChimeArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 5
- **Max Length**: 1600

### ClientRequestToken
- **Type**: string
- **Pattern**: `[-_a-zA-Z0-9]*`
- **Min Length**: 2
- **Max Length**: 64

### Content
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 4096

### Country
- **Type**: string
- **Pattern**: `^$|^[A-Z]{2,2}$`

### E164PhoneNumber
- **Type**: string
- **Pattern**: `^\+?[1-9]\d{1,14}$`

### EmailAddress
- **Type**: string
- **Pattern**: `.+@.+\..+`

### FunctionArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
- **Max Length**: 10000

### GuidString
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`

### JoinTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+/]+$`
- **Min Length**: 2
- **Max Length**: 2048

### MessageId
- **Type**: string
- **Pattern**: `[-_a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### Metadata
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### NextToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2048

### NonEmptyContent
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1

### NonEmptyResourceName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 256

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`

### NonEmptyString128
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### ProxySessionNameString
- **Type**: string
- **Pattern**: `^$|^[a-zA-Z0-9 ]{0,30}$`

### ResourceName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 0
- **Max Length**: 256

### SensitiveNonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`

### TollFreePrefix
- **Type**: string
- **Pattern**: `^8(00|33|44|55|66|77|88)$`
- **Min Length**: 3
- **Max Length**: 3

### TranscribeLanguageModelName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### TranscribeLanguageOptions
- **Type**: string
- **Pattern**: `^[a-zA-Z-,]+`
- **Min Length**: 1
- **Max Length**: 200

### TranscribePiiEntityTypes
- **Type**: string
- **Pattern**: `^[A-Z_, ]+`
- **Min Length**: 1
- **Max Length**: 300

### TranscribeVocabularyNamesOrFilterNamesString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9,-._]+`
- **Min Length**: 1
- **Max Length**: 3000

### UserId
- **Type**: string
- **Pattern**: `[A-Za-z0-9]([A-Za-z0-9\:\-\_\.\@]{0,62}[A-Za-z0-9])?`
- **Min Length**: 1
- **Max Length**: 64

### UserName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 100


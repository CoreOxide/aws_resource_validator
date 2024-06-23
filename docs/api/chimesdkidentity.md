# Chimesdkidentity Service

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

### LexBotAliasArn
- **Type**: string
- **Pattern**: `arn:aws:lex:[a-z]{2}-[a-z]+-\d{1}:\d{12}:bot-alias/[A-Z0-9]{10}/[A-Z0-9]{10}`
- **Min Length**: 15
- **Max Length**: 2048

### LexIntentName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

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

### NonEmptyResourceName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 256

### NonEmptySensitiveString1600
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1600

### ResourceName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 0
- **Max Length**: 256

### SensitiveChimeArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 5
- **Max Length**: 1600

### SensitiveString1600
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1600

### String1600
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1600

### String64
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 64

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


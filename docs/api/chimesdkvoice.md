# Chimesdkvoice Service

### AlexaSkillId
- **Type**: string
- **Pattern**: `amzn1\.application-oa2-client\.[0-9a-fA-F]{32}`
- **Max Length**: 64

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

### ClientRequestId
- **Type**: string
- **Pattern**: `^[-_a-zA-Z0-9]*${2,64}$`

### Country
- **Type**: string
- **Pattern**: `^$|^[A-Z]{2,2}$`

### E164PhoneNumber
- **Type**: string
- **Pattern**: `^\+?[1-9]\d{1,14}$`

### FunctionArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
- **Max Length**: 10000

### GuidString
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`

### NonEmptyString128
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### NonEmptyString256
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### PhoneNumberName
- **Type**: string
- **Pattern**: `^$|^[a-zA-Z0-9\,\.\_\-]+(\s+[a-zA-Z0-9\,\.\_\-]+)*$`
- **Min Length**: 0
- **Max Length**: 256

### ProxySessionNameString
- **Type**: string
- **Pattern**: `^$|^[a-zA-Z0-9 ]{0,30}$`

### SensitiveNonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`

### SipMediaApplicationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 _.-]+`
- **Min Length**: 1
- **Max Length**: 256

### SipRuleName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 _.-]+`
- **Min Length**: 1
- **Max Length**: 256

### TollFreePrefix
- **Type**: string
- **Pattern**: `^8(00|33|44|55|66|77|88)$`
- **Min Length**: 3
- **Max Length**: 3

### VoiceConnectorGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 _.-]+`
- **Min Length**: 1
- **Max Length**: 256

### VoiceConnectorName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 _.-]+`
- **Min Length**: 1
- **Max Length**: 256

### VoiceProfileDomainName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9 _.-]+`
- **Min Length**: 1
- **Max Length**: 256


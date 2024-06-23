# Chimesdkmeetings Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `^arn:.*`
- **Min Length**: 1
- **Max Length**: 1011

### Arn
- **Type**: string
- **Pattern**: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 1024

### ClientRequestToken
- **Type**: string
- **Pattern**: `[-_a-zA-Z0-9]*`
- **Min Length**: 2
- **Max Length**: 64

### GuidString
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`

### TagKey
- **Type**: string
- **Pattern**: `^[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\s\w+-=\.:/@]*`
- **Min Length**: 0
- **Max Length**: 256

### TenantId
- **Type**: string
- **Pattern**: `^(?!.*?(.)\1{3})[-_!@#$a-zA-Z0-9]*$`
- **Min Length**: 2
- **Max Length**: 256

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


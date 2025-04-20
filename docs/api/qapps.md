# Qapps Service

### BatchCreateCategoryInputCategoryColorString
- **Type**: string
- **Pattern**: `#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})`
- **Min Length**: 4
- **Max Length**: 7

### BatchCreateCategoryInputCategoryTitleString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*`
- **Min Length**: 1
- **Max Length**: 30

### CategoryInputColorString
- **Type**: string
- **Pattern**: `#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})`
- **Min Length**: 4
- **Max Length**: 7

### CategoryInputTitleString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*`
- **Min Length**: 1
- **Max Length**: 30

### CreatePresignedUrlInputFileContentsSha256String
- **Type**: string
- **Pattern**: `[A-Za-z0-9+/]{43}=$|^[A-Za-z0-9+/]{42}==$|^[A-Za-z0-9+/]{44}`

### DocumentAttributeKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 200

### Title
- **Type**: string
- **Pattern**: `[^{}\\"<>]+`
- **Min Length**: 0
- **Max Length**: 100

### UUID
- **Type**: string
- **Pattern**: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`


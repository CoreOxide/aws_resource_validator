# Workdocs Service

### ActivityNamesFilterType
- **Type**: string
- **Pattern**: `[\w,]+`
- **Min Length**: 1
- **Max Length**: 1024

### CommentIdType
- **Type**: string
- **Pattern**: `[\w+-.@]+`
- **Min Length**: 1
- **Max Length**: 128

### CustomMetadataKeyType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._+-/=][a-zA-Z0-9 ._+-/=]*`
- **Min Length**: 1
- **Max Length**: 56

### CustomMetadataValueType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._+-/=][a-zA-Z0-9 ._+-/=]*`
- **Min Length**: 1
- **Max Length**: 256

### DocumentVersionIdType
- **Type**: string
- **Pattern**: `[\w+-.@]+`
- **Min Length**: 1
- **Max Length**: 128

### EmailAddressType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
- **Min Length**: 1
- **Max Length**: 256

### FieldNamesType
- **Type**: string
- **Pattern**: `[\w,]+`
- **Min Length**: 1
- **Max Length**: 256

### HashType
- **Type**: string
- **Pattern**: `[&\w+-.@]+`
- **Min Length**: 0
- **Max Length**: 128

### HeaderNameType
- **Type**: string
- **Pattern**: `[\w-]+`
- **Min Length**: 1
- **Max Length**: 256

### IdType
- **Type**: string
- **Pattern**: `[&\w+-.@]+`
- **Min Length**: 1
- **Max Length**: 256

### MarkerType
- **Type**: string
- **Pattern**: `[\u0000-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 2048

### NextMarkerType
- **Type**: string
- **Pattern**: `[\d]+`
- **Min Length**: 1
- **Max Length**: 2048

### PasswordType
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 4
- **Max Length**: 32

### ResourceIdType
- **Type**: string
- **Pattern**: `[\w+-.@]+`
- **Min Length**: 1
- **Max Length**: 128

### ResourceNameType
- **Type**: string
- **Pattern**: `[\u0020-\u202D\u202F-\uFFFF]+`
- **Min Length**: 1
- **Max Length**: 255

### ResponseItemWebUrl
- **Type**: string
- **Pattern**: `[\u0020-\uFFFF]+`
- **Min Length**: 1
- **Max Length**: 512

### SearchMarkerType
- **Type**: string
- **Pattern**: `[\u0000-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 12288

### SearchQueryType
- **Type**: string
- **Pattern**: `[\u0020-\uFFFF]+`
- **Min Length**: 1
- **Max Length**: 512

### SharedLabel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._+-/=][a-zA-Z0-9 ._+-/=]*`
- **Min Length**: 1
- **Max Length**: 32

### UserIdsType
- **Type**: string
- **Pattern**: `[&\w+-.@, ]+`
- **Min Length**: 1
- **Max Length**: 2000

### UsernameType
- **Type**: string
- **Pattern**: `[\w\-+.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z]+)?`
- **Min Length**: 1
- **Max Length**: 256


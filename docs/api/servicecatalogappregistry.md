# Servicecatalogappregistry Service

### ApplicationArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

### ApplicationId
- **Type**: string
- **Pattern**: `[a-z0-9]+`
- **Min Length**: 26
- **Max Length**: 26

### ApplicationSpecifier
- **Type**: string
- **Pattern**: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
- **Min Length**: 1
- **Max Length**: 256

### Arn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
- **Min Length**: 1
- **Max Length**: 1600

### AttributeGroupArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`

### AttributeGroupId
- **Type**: string
- **Pattern**: `[-.\w]+`
- **Min Length**: 1
- **Max Length**: 256

### AttributeGroupSpecifier
- **Type**: string
- **Pattern**: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+)`
- **Min Length**: 1
- **Max Length**: 512

### Attributes
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 8000

### ClientToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 128

### CreatedBy
- **Type**: string
- **Pattern**: `^(?!-)([a-z0-9-]+\.)+(aws\.internal|amazonaws\.com(\.cn)?)$`
- **Min Length**: 1
- **Max Length**: 128

### Name
- **Type**: string
- **Pattern**: `[-.\w]+`
- **Min Length**: 1
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `[A-Za-z0-9+/=]+`
- **Min Length**: 1
- **Max Length**: 2024

### ResourceItemType
- **Type**: string
- **Pattern**: `AWS::[a-zA-Z0-9]+::\w+`

### ResourceSpecifier
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagKeyConfig
- **Type**: string
- **Pattern**: `^(?!\s+$)[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Min Length**: 0
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Max Length**: 256


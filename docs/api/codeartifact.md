# Codeartifact Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`
- **Min Length**: 12
- **Max Length**: 12

### Arn
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 1011

### AssetName
- **Type**: string
- **Pattern**: `\P{C}+`
- **Min Length**: 1
- **Max Length**: 255

### Description
- **Type**: string
- **Pattern**: `\P{C}*`
- **Max Length**: 1000

### DomainName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
- **Min Length**: 2
- **Max Length**: 50

### ExternalConnectionName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9._\-:]{1,99}`
- **Min Length**: 2
- **Max Length**: 100

### HashValue
- **Type**: string
- **Pattern**: `[0-9a-f]+`
- **Min Length**: 32
- **Max Length**: 512

### PackageGroupContactInfo
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 1000

### PackageGroupPattern
- **Type**: string
- **Pattern**: `[^\p{C}\p{IsWhitespace}]+`
- **Min Length**: 2
- **Max Length**: 520

### PackageGroupPatternPrefix
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 520

### PackageName
- **Type**: string
- **Pattern**: `[^#/\s]+`
- **Min Length**: 1
- **Max Length**: 255

### PackageNamespace
- **Type**: string
- **Pattern**: `[^#/\s]+`
- **Min Length**: 1
- **Max Length**: 255

### PackageVersion
- **Type**: string
- **Pattern**: `[^#/\s]+`
- **Min Length**: 1
- **Max Length**: 255

### PackageVersionRevision
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 50

### PaginationToken
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 2000

### PolicyDocument
- **Type**: string
- **Pattern**: `[\P{C}\s]+`
- **Min Length**: 1
- **Max Length**: 7168

### PolicyRevision
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 100

### RepositoryName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
- **Min Length**: 2
- **Max Length**: 100

### SHA256
- **Type**: string
- **Pattern**: `[0-9a-f]+`
- **Min Length**: 64
- **Max Length**: 64

### TagKey
- **Type**: string
- **Pattern**: `\P{C}+`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 256


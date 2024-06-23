# Ecrpublic Service

### Base64
- **Type**: string
- **Pattern**: `^\S+$`

### LayerDigest
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_+.]+:[a-fA-F0-9]+`

### RegistryAliasName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9]+(?:[._-][a-z0-9]+)*`
- **Min Length**: 2
- **Max Length**: 50

### RegistryId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### RepositoryName
- **Type**: string
- **Pattern**: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
- **Min Length**: 2
- **Max Length**: 205

### UploadId
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`


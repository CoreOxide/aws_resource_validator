# Ecr Service

### Base64
- **Type**: string
- **Pattern**: `^\S+$`

### CredentialArn
- **Type**: string
- **Pattern**: `^arn:aws:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`
- **Min Length**: 50
- **Max Length**: 612

### LayerDigest
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_+.]+:[a-fA-F0-9]+`

### PullThroughCacheRuleRepositoryPrefix
- **Type**: string
- **Pattern**: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
- **Min Length**: 2
- **Max Length**: 30

### Region
- **Type**: string
- **Pattern**: `[0-9a-z-]{2,25}`
- **Min Length**: 2
- **Max Length**: 25

### RegistryId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### RepositoryFilterValue
- **Type**: string
- **Pattern**: `^(?:[a-z0-9]+(?:[._-][a-z0-9]*)*/)*[a-z0-9]*(?:[._-][a-z0-9]*)*$`
- **Min Length**: 2
- **Max Length**: 256

### RepositoryName
- **Type**: string
- **Pattern**: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
- **Min Length**: 2
- **Max Length**: 256

### ScanningRepositoryFilterValue
- **Type**: string
- **Pattern**: `^[a-z0-9*](?:[._\-/a-z0-9*]?[a-z0-9*]+)*$`
- **Min Length**: 1
- **Max Length**: 255

### UploadId
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`


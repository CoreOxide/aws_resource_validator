# Marketplaceagreement Service

### AWSAccountId
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 32

### AgreementResourceType
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Min Length**: 1
- **Max Length**: 64

### AgreementType
- **Type**: string
- **Pattern**: `^[A-Za-z]+$`
- **Min Length**: 1
- **Max Length**: 64

### BoundedString
- **Type**: string
- **Pattern**: `^(.)+$`
- **Min Length**: 1
- **Max Length**: 4096

### Catalog
- **Type**: string
- **Pattern**: `^[a-zA-Z]+$`
- **Min Length**: 1
- **Max Length**: 64

### CurrencyCode
- **Type**: string
- **Pattern**: `^[A-Z]+$`
- **Min Length**: 3
- **Max Length**: 3

### FilterName
- **Type**: string
- **Pattern**: `^[A-Za-z_]+$`
- **Min Length**: 1
- **Max Length**: 32

### FilterValue
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+:_-]+$`
- **Min Length**: 1
- **Max Length**: 64

### NextToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+/=]+$`
- **Min Length**: 0
- **Max Length**: 8192

### OfferId
- **Type**: string
- **Pattern**: `^\S{1,64}$`
- **Min Length**: 1
- **Max Length**: 64

### RequestId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### ResourceId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_/-]+$`
- **Min Length**: 1
- **Max Length**: 64

### SortBy
- **Type**: string
- **Pattern**: `^[A-Za-z_]+$`
- **Min Length**: 1
- **Max Length**: 255

### UnversionedTermType
- **Type**: string
- **Pattern**: `^[A-Za-z]+$`
- **Min Length**: 1
- **Max Length**: 4096


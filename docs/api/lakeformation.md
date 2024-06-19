# Lakeformation Service

### AuditContextString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### CatalogIdString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### DescriptionString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### ETagString
- **Type**: string
- **Pattern**: `[\p{L}\p{N}\p{P}]*`
- **Min Length**: 1
- **Max Length**: 255

### HashString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### IAMRoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::[0-9]*:role/.*`

### IAMSAMLProviderArn
- **Type**: string
- **Pattern**: `arn:aws:iam::[0-9]*:saml-provider/.*`

### KeyString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### LFTagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@%]*)$`
- **Min Length**: 1
- **Max Length**: 128

### LFTagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:\*\/=+\-@%]*)$`
- **Min Length**: 0
- **Max Length**: 256

### NameString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### PredicateString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### QueryPlanningContextDatabaseNameString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1

### TransactionIdString
- **Type**: string
- **Pattern**: `[\p{L}\p{N}\p{P}]*`
- **Min Length**: 1
- **Max Length**: 255

### TrueFalseString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 5

### URI
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 1024

### VersionString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255


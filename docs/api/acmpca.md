# Acmpca Service

### ASN1PrintableString64
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\'()+-.?:/= ]*`
- **Min Length**: 0
- **Max Length**: 64

### AWSPolicy
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 81920

### AccountId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 12
- **Max Length**: 12

### Arn
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
- **Min Length**: 5
- **Max Length**: 200

### AuditReportId
- **Type**: string
- **Pattern**: `[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### Base64String1To4096
- **Type**: string
- **Pattern**: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
- **Min Length**: 1
- **Max Length**: 4096

### CnameString
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9;/?:@&=+$,%_.!~*()\']*`
- **Min Length**: 0
- **Max Length**: 253

### CountryCodeString
- **Type**: string
- **Pattern**: `[A-Za-z]{2}`
- **Min Length**: 2
- **Max Length**: 2

### CrlPathString
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9;?:@&=+$,%_.!~*()\']+(/[-a-zA-Z0-9;?:@&=+$,%_.!~*()\']+)*`
- **Min Length**: 0
- **Max Length**: 253

### CustomObjectIdentifier
- **Type**: string
- **Pattern**: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
- **Min Length**: 0
- **Max Length**: 64

### IdempotencyToken
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]*`
- **Min Length**: 1
- **Max Length**: 36

### Principal
- **Type**: string
- **Pattern**: `[^*]+`
- **Min Length**: 0
- **Max Length**: 128

### S3BucketName3To255
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9._/]+`
- **Min Length**: 3
- **Max Length**: 255

### TagKey
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
- **Min Length**: 0
- **Max Length**: 256


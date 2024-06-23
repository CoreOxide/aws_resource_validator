# Sts Service

### accessKeyIdType
- **Type**: string
- **Pattern**: `[\w]*`
- **Min Length**: 16
- **Max Length**: 128

### arnType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]+`
- **Min Length**: 20
- **Max Length**: 2048

### assumedRoleIdType
- **Type**: string
- **Pattern**: `[\w+=,.@:-]*`
- **Min Length**: 2
- **Max Length**: 193

### externalIdType
- **Type**: string
- **Pattern**: `[\w+=,.@:\/-]*`
- **Min Length**: 2
- **Max Length**: 1224

### federatedIdType
- **Type**: string
- **Pattern**: `[\w+=,.@\:-]*`
- **Min Length**: 2
- **Max Length**: 193

### roleSessionNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]*`
- **Min Length**: 2
- **Max Length**: 64

### serialNumberType
- **Type**: string
- **Pattern**: `[\w+=/:,.@-]*`
- **Min Length**: 9
- **Max Length**: 256

### sessionPolicyDocumentType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 2048

### sourceIdentityType
- **Type**: string
- **Pattern**: `[\w+=,.@-]*`
- **Min Length**: 2
- **Max Length**: 64

### tagKeyType
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`
- **Min Length**: 1
- **Max Length**: 128

### tagValueType
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Min Length**: 0
- **Max Length**: 256

### tokenCodeType
- **Type**: string
- **Pattern**: `[\d]*`
- **Min Length**: 6
- **Max Length**: 6

### unrestrictedSessionPolicyDocumentType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1

### userNameType
- **Type**: string
- **Pattern**: `[\w+=,.@-]*`
- **Min Length**: 2
- **Max Length**: 32


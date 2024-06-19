# Redshift Service

### AuthenticationProfileNameString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+$`
- **Max Length**: 63

### CustomDomainCertificateArnString
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`
- **Min Length**: 20
- **Max Length**: 2048

### CustomDomainNameString
- **Type**: string
- **Pattern**: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`
- **Min Length**: 1
- **Max Length**: 253

### IdcDisplayNameString
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 127

### IdentityNamespaceString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_+.#@$-]+$`
- **Min Length**: 1
- **Max Length**: 127

### PartnerIntegrationAccountId
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 12
- **Max Length**: 12

### PartnerIntegrationClusterIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+$`
- **Max Length**: 63

### PartnerIntegrationDatabaseName
- **Type**: string
- **Pattern**: `^[\p{L}_][\p{L}\p{N}@$#_]+$`
- **Max Length**: 127

### PartnerIntegrationPartnerName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-_]+$`
- **Max Length**: 255

### PartnerIntegrationStatusMessage
- **Type**: string
- **Pattern**: `^[\x20-\x7E]+$`
- **Max Length**: 262144

### RedshiftIdcApplicationName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9]*(-[a-z0-9]+)*`
- **Min Length**: 1
- **Max Length**: 63


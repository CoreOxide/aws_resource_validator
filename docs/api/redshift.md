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

### Description
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 1000

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

### InboundIntegrationArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:.+:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
- **Min Length**: 1
- **Max Length**: 255

### IntegrationArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:redshift:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
- **Min Length**: 1
- **Max Length**: 255

### IntegrationDescription
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 1000

### IntegrationName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`
- **Min Length**: 1
- **Max Length**: 63

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

### S3KeyPrefixValue
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Max Length**: 256

### SourceArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:(s3|dynamodb):.*:.*:[a-zA-Z0-9._\-\/]+$`
- **Min Length**: 1
- **Max Length**: 255

### TargetArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:redshift(-serverless)?:[a-z0-9\-]+:[0-9]{12}:(namespace\/|namespace:)[a-z0-9\-]+$`
- **Min Length**: 20
- **Max Length**: 2048


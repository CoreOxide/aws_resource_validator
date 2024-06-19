# Opsworkscm Service

### AWSOpsWorksCMResourceArn
- **Type**: string
- **Pattern**: `arn:aws.*:opsworks-cm:.*:[0-9]{12}:.*`

### AttributeName
- **Type**: string
- **Pattern**: `[A-Z][A-Z0-9_]*`
- **Min Length**: 1
- **Max Length**: 64

### AttributeValue
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 10000

### BackupId
- **Type**: string
- **Pattern**: `[a-zA-Z][a-zA-Z0-9\-\.\:]*`
- **Max Length**: 79

### CustomCertificate
- **Type**: string
- **Pattern**: `(?s)\s*-----BEGIN CERTIFICATE-----.+-----END CERTIFICATE-----\s*`
- **Max Length**: 2097152

### CustomDomain
- **Type**: string
- **Pattern**: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`
- **Max Length**: 253

### CustomPrivateKey
- **Type**: string
- **Pattern**: `(?ms)\s*^-----BEGIN (?-s:.*)PRIVATE KEY-----$.*?^-----END (?-s:.*)PRIVATE KEY-----$\s*`
- **Max Length**: 4096

### EngineAttributeName
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 10000

### EngineAttributeValue
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 10000

### InstanceProfileArn
- **Type**: string
- **Pattern**: `arn:aws:iam::[0-9]{12}:instance-profile/.*`
- **Max Length**: 10000

### KeyPair
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 10000

### NextToken
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 10000

### NodeAssociationStatusToken
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 10000

### NodeName
- **Type**: string
- **Pattern**: `^[\-\p{Alnum}_:.]+$`
- **Max Length**: 10000

### ServerName
- **Type**: string
- **Pattern**: `[a-zA-Z][a-zA-Z0-9\-]*`
- **Min Length**: 1
- **Max Length**: 40

### ServiceRoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::[0-9]{12}:role/.*`
- **Max Length**: 10000

### String
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 10000

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### TimeWindowDefinition
- **Type**: string
- **Pattern**: `^((Mon|Tue|Wed|Thu|Fri|Sat|Sun):)?([0-1][0-9]|2[0-3]):[0-5][0-9]$`
- **Max Length**: 10000


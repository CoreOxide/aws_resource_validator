# Redshiftserverless Service

### CustomDomainCertificateArnString
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`
- **Min Length**: 20
- **Max Length**: 2048

### CustomDomainName
- **Type**: string
- **Pattern**: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`
- **Min Length**: 1
- **Max Length**: 253

### IpAddressType
- **Type**: string
- **Pattern**: `^(ipv4|dualstack)$`

### ManagedWorkgroupName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_:\-]+$`
- **Min Length**: 3
- **Max Length**: 255

### NamespaceName
- **Type**: string
- **Pattern**: `^[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 64

### OwnerAccount
- **Type**: string
- **Pattern**: `(\d{12})`
- **Min Length**: 1
- **Max Length**: 12

### ScheduledActionName
- **Type**: string
- **Pattern**: `^[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 60

### SourceArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z-]*:glue:[a-z0-9-]+:\d+:(database|catalog)[a-z0-9-:]*(?:/[A-Za-z0-9-_]{1,255})*$`

### TrackName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]+$`
- **Min Length**: 1
- **Max Length**: 256

### WorkgroupName
- **Type**: string
- **Pattern**: `^[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 64


# Workspacesweb Service

### ARN
- **Type**: string
- **Pattern**: `^arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+$`
- **Min Length**: 20
- **Max Length**: 2048

### BrowserPolicy
- **Type**: string
- **Pattern**: `\{[\S\s]*\}\s*`
- **Min Length**: 2
- **Max Length**: 131072

### CertificatePrincipal
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 256

### CertificateThumbprint
- **Type**: string
- **Pattern**: `^[A-Fa-f0-9]{64}$`
- **Min Length**: 64
- **Max Length**: 64

### CookieDomain
- **Type**: string
- **Pattern**: `^(\.?)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)*[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$`
- **Min Length**: 0
- **Max Length**: 253

### CookiePath
- **Type**: string
- **Pattern**: `^/(\S)*$`
- **Min Length**: 0
- **Max Length**: 2000

### Description
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 256

### DisplayName
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 64

### IdentityProviderName
- **Type**: string
- **Pattern**: `^[^_][\p{L}\p{M}\p{S}\p{N}\p{P}][^_]+$`
- **Min Length**: 1
- **Max Length**: 32

### IpRange
- **Type**: string
- **Pattern**: `^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/([0-9]|[12][0-9]|3[0-2])|)$`

### KinesisStreamArn
- **Type**: string
- **Pattern**: `arn:[\w+=/,.@-]+:kinesis:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:stream/.+`
- **Min Length**: 20
- **Max Length**: 2048

### PaginationToken
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 2048

### PortalEndpoint
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]?((?!-)([A-Za-z0-9-]*[A-Za-z0-9])\.)+[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 253

### SamlMetadata
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 204800

### SecurityGroupId
- **Type**: string
- **Pattern**: `^[\w+\-]+$`
- **Min Length**: 1
- **Max Length**: 128

### StatusReason
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### StringType
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 0
- **Max Length**: 131072

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-([0-9a-f]{8}|[0-9a-f]{17})$`
- **Min Length**: 1
- **Max Length**: 32

### SubresourceARN
- **Type**: string
- **Pattern**: `^arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36}){2,}$`
- **Min Length**: 20
- **Max Length**: 2048

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

### VpcId
- **Type**: string
- **Pattern**: `^vpc-[0-9a-z]*$`
- **Min Length**: 1
- **Max Length**: 255

### keyArn
- **Type**: string
- **Pattern**: `^arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+$`
- **Min Length**: 20
- **Max Length**: 2048


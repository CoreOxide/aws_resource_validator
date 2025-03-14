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

### BuiltInPatternId
- **Type**: string
- **Pattern**: `^[_\-\d\w]+$`
- **Min Length**: 1
- **Max Length**: 50

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

### DescriptionSafe
- **Type**: string
- **Pattern**: `^[ _\-\d\w]+$`
- **Min Length**: 1
- **Max Length**: 256

### DisplayName
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 64

### DisplayNameSafe
- **Type**: string
- **Pattern**: `^[ _\-\d\w]+$`
- **Min Length**: 1
- **Max Length**: 64

### IdentityProviderName
- **Type**: string
- **Pattern**: `^[^_][\p{L}\p{M}\p{S}\p{N}\p{P}][^_]+$`
- **Min Length**: 1
- **Max Length**: 32

### InlineRedactionUrl
- **Type**: string
- **Pattern**: `^((([a-zA-Z][a-zA-Z0-9+.-]*):\/\/(\*|[\w%._\-\+~#=@]+)?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?)|(\*|[\w%._\-\+~#=@]+\.[\w%._\-\+~#=@]+)(?::(\d{1,5}))?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?|(([a-zA-Z][a-zA-Z0-9+.-]*):(\/\/)?\*))$`

### IpAddress
- **Type**: string
- **Pattern**: `^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`
- **Min Length**: 1
- **Max Length**: 15

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

### PatternName
- **Type**: string
- **Pattern**: `^[_\-\d\w]+$`
- **Min Length**: 1
- **Max Length**: 20

### PortalEndpoint
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]?((?!-)([A-Za-z0-9-]*[A-Za-z0-9])\.)+[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 253

### PortalId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+$`
- **Min Length**: 36
- **Max Length**: 36

### RedactionPlaceHolderText
- **Type**: string
- **Pattern**: `^[*_\-\d\w]+$`
- **Min Length**: 1
- **Max Length**: 20

### Regex
- **Type**: string
- **Pattern**: `^\/((?:[^\n])+)\/([gimsuyvd]{0,8})$`
- **Min Length**: 0
- **Max Length**: 300

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

### SessionId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+$`
- **Min Length**: 36
- **Max Length**: 36

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

### Username
- **Type**: string
- **Pattern**: `^[\s\S]*$`
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


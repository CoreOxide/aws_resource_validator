# Route53 Service

### ARN
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 20
- **Max Length**: 2048

### Cidr
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 50

### CidrLocationNameDefaultAllowed
- **Type**: string
- **Pattern**: `[0-9A-Za-z_\-\*]+`
- **Min Length**: 1
- **Max Length**: 16

### CidrLocationNameDefaultNotAllowed
- **Type**: string
- **Pattern**: `[0-9A-Za-z_\-]+`
- **Min Length**: 1
- **Max Length**: 16

### CidrNonce
- **Type**: string
- **Pattern**: `\p{ASCII}+`
- **Min Length**: 1
- **Max Length**: 64

### CollectionName
- **Type**: string
- **Pattern**: `[0-9A-Za-z_\-]+`
- **Min Length**: 1
- **Max Length**: 64

### IPAddress
- **Type**: string
- **Pattern**: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`
- **Max Length**: 45

### Latitude
- **Type**: string
- **Pattern**: `[-+]?[0-9]{1,2}(\.[0-9]{0,2})?`
- **Min Length**: 1
- **Max Length**: 6

### Longitude
- **Type**: string
- **Pattern**: `[-+]?[0-9]{1,3}(\.[0-9]{0,2})?`
- **Min Length**: 1
- **Max Length**: 7

### UUID
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`


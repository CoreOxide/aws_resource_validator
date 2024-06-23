# Lightsail Service

### AutoSnapshotDate
- **Type**: string
- **Pattern**: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`

### BucketAccessLogPrefix
- **Type**: string
- **Pattern**: `^[\w/!.*\')(-]+$`
- **Min Length**: 1
- **Max Length**: 100

### BucketName
- **Type**: string
- **Pattern**: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 54

### ContainerLabel
- **Type**: string
- **Pattern**: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
- **Min Length**: 1
- **Max Length**: 53

### ContainerName
- **Type**: string
- **Pattern**: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
- **Min Length**: 1
- **Max Length**: 53

### ContainerServiceName
- **Type**: string
- **Pattern**: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
- **Min Length**: 1
- **Max Length**: 63

### EmailAddress
- **Type**: string
- **Pattern**: `^[\w!#$%&.\'*+\/=?^_\x60{|}~\-]{1,64}@[a-zA-Z0-9\-]{1,63}(\.[a-zA-Z0-9\-]{1,63}){0,8}(\.[a-zA-Z]{2,63})$`
- **Min Length**: 6
- **Max Length**: 254

### IAMAccessKeyId
- **Type**: string
- **Pattern**: `^[A-Z0-9]{20}$`
- **Min Length**: 20
- **Max Length**: 20

### IpAddress
- **Type**: string
- **Pattern**: `([0-9]{1,3}\.){3}[0-9]{1,3}`

### Ipv6Address
- **Type**: string
- **Pattern**: `([A-F0-9]{1,4}:){7}[A-F0-9]{1,4}`

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:(aws[^:]*):([a-zA-Z0-9-]+):([a-z0-9-]+):([0-9]+):([a-zA-Z]+)/([a-zA-Z0-9-]+)$`

### ResourceName
- **Type**: string
- **Pattern**: `\w[\w\-]*\w`

### SensitiveNonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`

### SetupDomainName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]{1,63}(\.[a-zA-Z0-9\-]{1,63}){0,8}(\.[a-zA-Z]{2,63})$`
- **Min Length**: 4
- **Max Length**: 253

### SetupHistoryPageToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+/=]+$`
- **Min Length**: 24
- **Max Length**: 40

### TimeOfDay
- **Type**: string
- **Pattern**: `^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`


# Storagegateway Service

### DNSHostName
- **Type**: string
- **Pattern**: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`
- **Min Length**: 1
- **Max Length**: 255

### DomainName
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`
- **Min Length**: 1
- **Max Length**: 1024

### DomainUserName
- **Type**: string
- **Pattern**: `^\w[\w\.\- ]*$`
- **Min Length**: 1
- **Max Length**: 1024

### DomainUserPassword
- **Type**: string
- **Pattern**: `^[ -~]+$`
- **Min Length**: 1
- **Max Length**: 1024

### GatewayName
- **Type**: string
- **Pattern**: `^[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*$`
- **Min Length**: 2
- **Max Length**: 255

### Host
- **Type**: string
- **Pattern**: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])(:(\d+))?$`
- **Min Length**: 6
- **Max Length**: 1024

### IPV4Address
- **Type**: string
- **Pattern**: `^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}`
- **Min Length**: 7
- **Max Length**: 15

### IPV4AddressCIDR
- **Type**: string
- **Pattern**: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))?$`

### IqnName
- **Type**: string
- **Pattern**: `[0-9a-z:.-]+`
- **Min Length**: 1
- **Max Length**: 255

### KMSKey
- **Type**: string
- **Pattern**: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`
- **Min Length**: 7
- **Max Length**: 2048

### LocalConsolePassword
- **Type**: string
- **Pattern**: `^[ -~]+$`
- **Min Length**: 6
- **Max Length**: 512

### NetworkInterfaceId
- **Type**: string
- **Pattern**: `\A(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\z`

### NotificationPolicy
- **Type**: string
- **Pattern**: `^\{[\w\s:\{\}\[\]"]*}$`
- **Min Length**: 2
- **Max Length**: 100

### PermissionMode
- **Type**: string
- **Pattern**: `^[0-7]{4}$`
- **Min Length**: 1
- **Max Length**: 4

### PoolName
- **Type**: string
- **Pattern**: `^[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*$`
- **Min Length**: 1
- **Max Length**: 100

### Role
- **Type**: string
- **Pattern**: `^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):iam::([0-9]+):role/(\S+)$`
- **Min Length**: 20
- **Max Length**: 2048

### SMBGuestPassword
- **Type**: string
- **Pattern**: `^[ -~]+$`
- **Min Length**: 6
- **Max Length**: 512

### SnapshotId
- **Type**: string
- **Pattern**: `\Asnap-([0-9A-Fa-f]{8}|[0-9A-Fa-f]{17})\z`

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TapeARN
- **Type**: string
- **Pattern**: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`
- **Min Length**: 50
- **Max Length**: 500

### TapeBarcode
- **Type**: string
- **Pattern**: `^[A-Z0-9]*$`
- **Min Length**: 5
- **Max Length**: 16

### TapeBarcodePrefix
- **Type**: string
- **Pattern**: `^[A-Z]*$`
- **Min Length**: 1
- **Max Length**: 4

### TargetName
- **Type**: string
- **Pattern**: `^[-\.;a-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 200

### VolumeARN
- **Type**: string
- **Pattern**: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`
- **Min Length**: 50
- **Max Length**: 500


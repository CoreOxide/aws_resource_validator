# Panorama Service

### ApplicationInstanceId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 255

### ApplicationInstanceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 255

### BucketName
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### ClientToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 64

### DefaultGateway
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### DefaultRuntimeContextDevice
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 255

### Description
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 255

### DeviceId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 255

### DeviceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 255

### DeviceSerialNumber
- **Type**: string
- **Pattern**: `^[0-9]{1,20}$`

### Dns
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### ImageVersion
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### IpAddress
- **Type**: string
- **Pattern**: `^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))(:(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}))?$`
- **Min Length**: 1
- **Max Length**: 255

### IpAddressOrServerName
- **Type**: string
- **Pattern**: `(^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$)|(^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))(:(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}))?$)`
- **Min Length**: 1
- **Max Length**: 255

### JobId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 255

### ManifestOverridesPayloadData
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 51200

### ManifestPayloadData
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 51200

### Mask
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### NextToken
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 4096

### NodeAssetName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 255

### NodeId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\.]+$`
- **Min Length**: 1
- **Max Length**: 255

### NodeInstanceId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 128

### NodeName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 128

### NodePackageId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\/]+$`
- **Min Length**: 1
- **Max Length**: 255

### NodePackageName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_]+$`
- **Min Length**: 1
- **Max Length**: 128

### NodePackagePatchVersion
- **Type**: string
- **Pattern**: `^[a-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 255

### NodePackageVersion
- **Type**: string
- **Pattern**: `^([0-9]+)\.([0-9]+)$`
- **Min Length**: 1
- **Max Length**: 255

### ObjectKey
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### PackageOwnerAccount
- **Type**: string
- **Pattern**: `^[0-9a-z\_]+$`
- **Min Length**: 1
- **Max Length**: 12

### PortName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_]+$`
- **Min Length**: 1
- **Max Length**: 50

### PrincipalArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9][-.a-z0-9]{0,62}:iam::[0-9]{12}:[a-zA-Z0-9+=,.@\-_/]+$`
- **Min Length**: 1
- **Max Length**: 255

### Region
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### ResourceArn
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 2048

### RuntimeContextName
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### RuntimeRoleArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9][-.a-z0-9]{0,62}:iam::[0-9]{12}:role/.+$`
- **Min Length**: 1
- **Max Length**: 255

### TagKey
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 256

### TemplateKey
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### TemplateValue
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 255

### Token
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 4096


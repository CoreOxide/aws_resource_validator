# Ds Service

### AliasName
- **Type**: string
- **Pattern**: `^(?!D-|d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*`
- **Min Length**: 1
- **Max Length**: 62

### CertificateId
- **Type**: string
- **Pattern**: `^c-[0-9a-f]{10}$`

### CidrIp
- **Type**: string
- **Pattern**: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([1-9]|[1-2][0-9]|3[0-2]))$`

### ComputerPassword
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]+`
- **Min Length**: 8
- **Max Length**: 64

### CustomerId
- **Type**: string
- **Pattern**: `^(\d{12})$`

### CustomerUserName
- **Type**: string
- **Pattern**: `^(?!.*\\|.*"|.*\/|.*\[|.*\]|.*:|.*;|.*\||.*=|.*,|.*\+|.*\*|.*\?|.*<|.*>|.*@).*$`
- **Min Length**: 1
- **Max Length**: 64

### Description
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
- **Min Length**: 0
- **Max Length**: 128

### DirectoryConfigurationSettingName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-/. _]*$`
- **Min Length**: 1
- **Max Length**: 255

### DirectoryConfigurationSettingValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 255

### DirectoryId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{10}$`

### DirectoryName
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`

### DirectoryShortName
- **Type**: string
- **Pattern**: `^[^\\/:*?"<>|.]+[^\\/:*?"<>|]*$`

### DomainControllerId
- **Type**: string
- **Pattern**: `^dc-[0-9a-f]{10}$`

### IpAddr
- **Type**: string
- **Pattern**: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

### LogGroupName
- **Type**: string
- **Pattern**: `[-._/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### OCSPUrl
- **Type**: string
- **Pattern**: `^(https?|ftp|file|ldaps?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;()]*[-a-zA-Z0-9+&@#/%=~_|()]`
- **Min Length**: 1
- **Max Length**: 1024

### Password
- **Type**: string
- **Pattern**: `(?=^.{8,64}$)((?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9\s])(?=.*[a-z])|(?=.*[^A-Za-z0-9\s])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s]))^.*`

### RadiusSharedSecret
- **Type**: string
- **Pattern**: `^(\p{LD}|\p{Punct}| )+$`
- **Min Length**: 8
- **Max Length**: 512

### RemoteDomainName
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`
- **Max Length**: 1024

### RequestId
- **Type**: string
- **Pattern**: `^([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12})$`

### ResourceId
- **Type**: string
- **Pattern**: `^[d]-[0-9a-f]{10}$`

### SID
- **Type**: string
- **Pattern**: `[&\w+-.@]+`
- **Min Length**: 1
- **Max Length**: 256

### SchemaExtensionId
- **Type**: string
- **Pattern**: `^e-[0-9a-f]{10}$`

### SecurityGroupId
- **Type**: string
- **Pattern**: `^(sg-[0-9a-f]{8}|sg-[0-9a-f]{17})$`

### SnapshotId
- **Type**: string
- **Pattern**: `^s-[0-9a-f]{10}$`

### SnapshotName
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
- **Min Length**: 0
- **Max Length**: 128

### SubnetId
- **Type**: string
- **Pattern**: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`

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

### TopicName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 256

### TrustId
- **Type**: string
- **Pattern**: `^t-[0-9a-f]{10}$`

### TrustPassword
- **Type**: string
- **Pattern**: `^(\p{LD}|\p{Punct}| )+$`
- **Min Length**: 1
- **Max Length**: 128

### UserName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._-]+`
- **Min Length**: 1

### VpcId
- **Type**: string
- **Pattern**: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`


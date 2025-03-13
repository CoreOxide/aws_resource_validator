# Efs Service

### AccessPointArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}$`
- **Max Length**: 128

### AccessPointId
- **Type**: string
- **Pattern**: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}|fsap-[0-9a-f]{8,40})$`
- **Max Length**: 128

### AvailabilityZoneName
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 64

### AwsAccountId
- **Type**: string
- **Pattern**: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`
- **Max Length**: 14

### ClientToken
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 64

### CreationToken
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 64

### FileSystemId
- **Type**: string
- **Pattern**: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
- **Max Length**: 128

### IpAddress
- **Type**: string
- **Pattern**: `^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$`
- **Min Length**: 7
- **Max Length**: 15

### KmsKeyId
- **Type**: string
- **Pattern**: `^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))$`
- **Max Length**: 2048

### Marker
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 128

### MountTargetId
- **Type**: string
- **Pattern**: `^fsmt-[0-9a-f]{8,40}$`
- **Min Length**: 13
- **Max Length**: 45

### Path
- **Type**: string
- **Pattern**: `^(\/|(\/(?!\.)+[^$#<>;`|&?{}^*/\n]+){1,4})$`
- **Min Length**: 1
- **Max Length**: 100

### Permissions
- **Type**: string
- **Pattern**: `^[0-7]{3,4}$`
- **Min Length**: 3
- **Max Length**: 4

### Policy
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 20000

### RegionName
- **Type**: string
- **Pattern**: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
- **Min Length**: 1
- **Max Length**: 64

### ResourceId
- **Type**: string
- **Pattern**: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:(access-point/fsap|file-system/fs)-[0-9a-f]{8,40}|fs(ap)?-[0-9a-f]{8,40})$`
- **Max Length**: 128

### RoleArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
- **Max Length**: 2048

### SecurityGroup
- **Type**: string
- **Pattern**: `^sg-[0-9a-f]{8,40}`
- **Min Length**: 11
- **Max Length**: 43

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-[0-9a-f]{8,40}$`
- **Min Length**: 15
- **Max Length**: 47

### TagKey
- **Type**: string
- **Pattern**: `^(?![aA]{1}[wW]{1}[sS]{1}:)([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Max Length**: 256

### Token
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 128


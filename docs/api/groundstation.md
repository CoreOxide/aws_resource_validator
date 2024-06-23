# Groundstation Service

### AWSRegion
- **Type**: string
- **Pattern**: `^[\w-]+$`
- **Min Length**: 1
- **Max Length**: 128

### AnyArn
- **Type**: string
- **Pattern**: `^(arn:aws:)[\s\S]{0,1024}$`
- **Min Length**: 5
- **Max Length**: 1024

### ComponentTypeString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]{1,64}$`

### GroundStationName
- **Type**: string
- **Pattern**: `^[ a-zA-Z0-9-._:=]{4,256}$`
- **Min Length**: 4
- **Max Length**: 500

### InstanceId
- **Type**: string
- **Pattern**: `^[a-z0-9-]{10,64}$`
- **Min Length**: 10
- **Max Length**: 64

### InstanceType
- **Type**: string
- **Pattern**: `^[a-z0-9.-]{1,64}$`
- **Min Length**: 1
- **Max Length**: 64

### IpV4Address
- **Type**: string
- **Pattern**: `^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$`
- **Min Length**: 7
- **Max Length**: 16

### JsonString
- **Type**: string
- **Pattern**: `^[{}\[\]:.,"0-9A-z\-_\s]{2,8192}$`
- **Min Length**: 2
- **Max Length**: 8192

### KeyAliasArn
- **Type**: string
- **Pattern**: `^arn:aws[a-zA-Z-]{0,16}:kms:[a-z]{2}(-[a-z]{1,16}){1,3}-\d{1}:\d{12}:((alias/[a-zA-Z0-9:/_-]{1,256}))$`
- **Min Length**: 1
- **Max Length**: 512

### KeyAliasName
- **Type**: string
- **Pattern**: `^alias/[a-zA-Z0-9:/_-]+$`
- **Min Length**: 1
- **Max Length**: 256

### PaginationToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-/+_.=]+$`
- **Min Length**: 3
- **Max Length**: 1000

### S3BucketName
- **Type**: string
- **Pattern**: `^[a-z0-9.-]{3,63}$`
- **Min Length**: 3
- **Max Length**: 63

### S3KeyPrefix
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_\-=/]|\{satellite_id\}|\{config\-name}|\{s3\-config-id}|\{year\}|\{month\}|\{day\}){1,900}$`
- **Min Length**: 1
- **Max Length**: 900

### S3ObjectKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9!*\'\)\(./_-]{1,1024}$`
- **Min Length**: 1
- **Max Length**: 1024

### S3VersionId
- **Type**: string
- **Pattern**: `^[\s\S]{1,1024}$`
- **Min Length**: 1
- **Max Length**: 1024

### SafeName
- **Type**: string
- **Pattern**: `^[ a-zA-Z0-9_:-]{1,256}$`
- **Min Length**: 1
- **Max Length**: 256

### TleLineOne
- **Type**: string
- **Pattern**: `^1 [ 0-9]{5}[A-Z] [ 0-9]{5}[ A-Z]{3} [ 0-9]{5}[.][ 0-9]{8} (?:(?:[ 0+-][.][ 0-9]{8})|(?: [ +-][.][ 0-9]{7})) [ +-][ 0-9]{5}[+-][ 0-9] [ +-][ 0-9]{5}[+-][ 0-9] [ 0-9] [ 0-9]{4}[ 0-9]$`
- **Min Length**: 69
- **Max Length**: 69

### TleLineTwo
- **Type**: string
- **Pattern**: `^2 [ 0-9]{5} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{7} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{2}[.][ 0-9]{13}[ 0-9]$`
- **Min Length**: 69
- **Max Length**: 69

### UnboundedString
- **Type**: string
- **Pattern**: `^[\s\S]+$`
- **Min Length**: 1

### Uuid
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 128

### VersionString
- **Type**: string
- **Pattern**: `^(0|[1-9]\d*)(\.(0|[1-9]\d*))*$`
- **Min Length**: 1
- **Max Length**: 64


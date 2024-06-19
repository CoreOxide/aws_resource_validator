# Frauddetector Service

### Elements
- **Type**: string
- **Pattern**: `^\S+( +\S+)*$`
- **Min Length**: 1
- **Max Length**: 320

### KmsEncryptionKeyArn
- **Type**: string
- **Pattern**: `^DEFAULT|arn:[a-zA-Z0-9-]+:kms:[a-zA-Z0-9-]+:\d{12}:key\/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$`
- **Min Length**: 7
- **Max Length**: 90

### entityRestrictedString
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_.@+-]+$`
- **Min Length**: 1
- **Max Length**: 256

### filterString
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_-]+$`
- **Min Length**: 1
- **Max Length**: 256

### floatVersionString
- **Type**: string
- **Pattern**: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`
- **Min Length**: 3
- **Max Length**: 7

### fraudDetectorArn
- **Type**: string
- **Pattern**: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
- **Min Length**: 1
- **Max Length**: 256

### iamRoleArn
- **Type**: string
- **Pattern**: `^arn\:aws[a-z-]{0,15}\:iam\:\:[0-9]{12}\:role\/[^\s]{2,64}$`
- **Min Length**: 1
- **Max Length**: 256

### identifier
- **Type**: string
- **Pattern**: `^[0-9a-z_-]+$`
- **Min Length**: 1
- **Max Length**: 64

### modelIdentifier
- **Type**: string
- **Pattern**: `^[0-9a-z_]+$`
- **Min Length**: 1
- **Max Length**: 64

### nextToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 8192

### noDashIdentifier
- **Type**: string
- **Pattern**: `^[0-9a-z_]+$`
- **Min Length**: 1
- **Max Length**: 64

### s3BucketLocation
- **Type**: string
- **Pattern**: `^s3:\/\/(.+)$`
- **Min Length**: 1
- **Max Length**: 512

### sageMakerEndpointIdentifier
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_-]+$`
- **Min Length**: 1
- **Max Length**: 63

### tagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### variableType
- **Type**: string
- **Pattern**: `^[A-Z_]{1,64}$`
- **Min Length**: 1
- **Max Length**: 64

### wholeNumberVersionString
- **Type**: string
- **Pattern**: `^([1-9][0-9]*)$`
- **Min Length**: 1
- **Max Length**: 5


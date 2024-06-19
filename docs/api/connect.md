# Connect Service

### AwsRegion
- **Type**: string
- **Pattern**: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
- **Min Length**: 8
- **Max Length**: 31

### ContactFlowModuleDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 500

### ContactFlowModuleName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 127

### ContactTagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### CreateSecurityProfileName
- **Type**: string
- **Pattern**: `^[ a-zA-Z0-9_@-]+$`
- **Min Length**: 1
- **Max Length**: 127

### Description250
- **Type**: string
- **Pattern**: `(^[\S].*[\S]$)|(^[\S]$)`
- **Min Length**: 1
- **Max Length**: 250

### DirectoryAlias
- **Type**: string
- **Pattern**: `^(?!d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*$`
- **Min Length**: 1
- **Max Length**: 45

### DirectoryId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{10}$`
- **Min Length**: 12
- **Max Length**: 12

### FileName
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 256

### InstanceArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9-]{1}:[0-9]{1,20}:instance/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

### InstanceIdOrArn
- **Type**: string
- **Pattern**: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 250

### Name128
- **Type**: string
- **Pattern**: `(^[\S].*[\S]$)|(^[\S]$)`
- **Min Length**: 1
- **Max Length**: 128

### Password
- **Type**: string
- **Pattern**: `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\S]{8,64}$/`

### PhoneNumber
- **Type**: string
- **Pattern**: `\\+[1-9]\\d{1,14}$`

### PhoneNumberDescription
- **Type**: string
- **Pattern**: `^[\W\S_]*`
- **Min Length**: 0
- **Max Length**: 500

### PhoneNumberPrefix
- **Type**: string
- **Pattern**: `\\+?[0-9]{1,11}`

### PhoneNumberWorkflowMessage
- **Type**: string
- **Pattern**: `^[\W\S_]*`
- **Min Length**: 0
- **Max Length**: 255

### RegionName
- **Type**: string
- **Pattern**: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

### RuleName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### S3Uri
- **Type**: string
- **Pattern**: `s3://\S+/.+|https://\\S+\\.s3\\.\\S+\\.amazonaws\\.com/\\S+`
- **Min Length**: 1
- **Max Length**: 2000

### SourceApplicationName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_ -]+$`
- **Min Length**: 1
- **Max Length**: 100

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TrafficDistributionGroupArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### TrafficDistributionGroupId
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### TrafficDistributionGroupIdOrArn
- **Type**: string
- **Pattern**: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z-]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### ViewAction
- **Type**: string
- **Pattern**: `^([\p{L}\p{N}_.:\/=+\-@()\']+[\p{L}\p{Z}\p{N}_.:\/=+\-@()\']*)$`
- **Min Length**: 1
- **Max Length**: 255

### ViewContentSha256
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 64

### ViewDescription
- **Type**: string
- **Pattern**: `^([\p{L}\p{N}_.:\/=+\-@,()\']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()\']*)$`
- **Min Length**: 1
- **Max Length**: 4096

### ViewId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_\-:\/$]+$`
- **Min Length**: 1
- **Max Length**: 500

### ViewName
- **Type**: string
- **Pattern**: `^([\p{L}\p{N}_.:\/=+\-@()\']+[\p{L}\p{Z}\p{N}_.:\/=+\-@()\']*)$`
- **Min Length**: 1
- **Max Length**: 255

### ViewsClientToken
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
- **Max Length**: 500

### ViewsInstanceId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_\-:\/]+$`
- **Min Length**: 1
- **Max Length**: 100

### ViewsNextToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9=\/+_.-]+$`
- **Min Length**: 1
- **Max Length**: 4096

### VocabularyName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 140

### VocabularyNextToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 131070


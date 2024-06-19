# Comprehend Service

### AttributeNamesListItem
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Min Length**: 1
- **Max Length**: 63

### ClientRequestTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 64

### ComprehendArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-]{1,64}/[a-zA-Z0-9](-*[a-zA-Z0-9])*((/dataset/[a-zA-Z0-9](-*[a-zA-Z0-9])*)|(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*))?`
- **Max Length**: 256

### ComprehendArnName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
- **Max Length**: 63

### ComprehendDatasetArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*/dataset/[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Max Length**: 256

### ComprehendEndpointArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier-endpoint|entity-recognizer-endpoint)/[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Max Length**: 256

### ComprehendEndpointName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
- **Max Length**: 40

### ComprehendFlywheelArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Max Length**: 256

### ComprehendModelArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`
- **Max Length**: 256

### Description
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
- **Max Length**: 2048

### DocumentClassifierArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:document-classifier/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`
- **Max Length**: 256

### DocumentClassifierEndpointArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:([0-9]{12}|aws):document-classifier-endpoint/[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Max Length**: 256

### EntityRecognizerArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:entity-recognizer/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`
- **Max Length**: 256

### EntityRecognizerEndpointArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:entity-recognizer-endpoint/[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Max Length**: 256

### EntityTypeName
- **Type**: string
- **Pattern**: `^(?![^\n\r\t,]*\\n|\\r|\\t)[^\n\r\t,]+$`
- **Max Length**: 64

### EventTypeString
- **Type**: string
- **Pattern**: `[A-Z_]*`
- **Min Length**: 1
- **Max Length**: 40

### FlywheelIterationId
- **Type**: string
- **Pattern**: `[0-9]{8}T[0-9]{6}Z`
- **Max Length**: 63

### FlywheelS3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
- **Max Length**: 512

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
- **Min Length**: 20
- **Max Length**: 2048

### JobId
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 32

### JobName
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 256

### KmsKeyId
- **Type**: string
- **Pattern**: `^\p{ASCII}+$`
- **Max Length**: 2048

### LabelDelimiter
- **Type**: string
- **Pattern**: `^[ ~!@#$%^*\-_+=|\\:;\t>?/]$`
- **Min Length**: 1
- **Max Length**: 1

### LabelListItem
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Max Length**: 5000

### MaskCharacter
- **Type**: string
- **Pattern**: `[!@#$%&*]`
- **Min Length**: 1
- **Max Length**: 1

### Policy
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 20000

### PolicyRevisionId
- **Type**: string
- **Pattern**: `[0-9A-Fa-f]+`
- **Max Length**: 64

### S3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
- **Max Length**: 1024

### SecurityGroupId
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 32

### SubnetId
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 32

### VersionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
- **Max Length**: 63


# Lookoutequipment Service

### BoundedLengthString
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{1,5000}`
- **Min Length**: 1
- **Max Length**: 5000

### Comments
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{1,2560}`
- **Min Length**: 1
- **Max Length**: 2560

### ComponentName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._\-]{1,200}$`
- **Min Length**: 1
- **Max Length**: 200

### ComponentTimestampDelimiter
- **Type**: string
- **Pattern**: `^(\-|\_|\s)?$`
- **Min Length**: 0
- **Max Length**: 1

### DatasetArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+`
- **Min Length**: 20
- **Max Length**: 2048

### DatasetIdentifier
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_-]{1,200}$`
- **Min Length**: 1
- **Max Length**: 200

### DatasetName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_-]{1,200}$`
- **Min Length**: 1
- **Max Length**: 200

### Equipment
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{1,200}`
- **Min Length**: 1
- **Max Length**: 200

### FaultCode
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{1,100}`
- **Min Length**: 1
- **Max Length**: 100

### FileNameTimestampFormat
- **Type**: string
- **Pattern**: `^EPOCH|yyyy-MM-dd-HH-mm-ss|yyyyMMddHHmmss$`

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
- **Min Length**: 20
- **Max Length**: 2048

### IdempotenceToken
- **Type**: string
- **Pattern**: `\p{ASCII}{1,256}`
- **Min Length**: 1
- **Max Length**: 256

### InferenceSchedulerArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:inference-scheduler\/.+`
- **Min Length**: 20
- **Max Length**: 2048

### InferenceSchedulerIdentifier
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_-]{1,200}$`
- **Min Length**: 1
- **Max Length**: 200

### InferenceSchedulerName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_-]{1,200}$`
- **Min Length**: 1
- **Max Length**: 200

### IngestionJobId
- **Type**: string
- **Pattern**: `[A-Fa-f0-9]{0,32}`
- **Max Length**: 32

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws[a-z\-]*:kms:[a-z0-9\-]*:\d{12}:[\w\-\/]+`
- **Min Length**: 1
- **Max Length**: 1024

### LabelGroupArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:label-group\/.+`
- **Min Length**: 20
- **Max Length**: 2048

### LabelGroupName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_-]{1,200}$`
- **Min Length**: 1
- **Max Length**: 200

### LabelId
- **Type**: string
- **Pattern**: `[A-Fa-f0-9]{0,32}`
- **Max Length**: 32

### LookbackWindow
- **Type**: string
- **Pattern**: `^P180D$|^P360D$|^P540D$|^P720D$`

### ModelArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`
- **Min Length**: 20
- **Max Length**: 2048

### ModelName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_-]{1,200}$`
- **Min Length**: 1
- **Max Length**: 200

### ModelVersionArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`
- **Min Length**: 20
- **Max Length**: 2048

### NameOrArn
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
- **Min Length**: 1
- **Max Length**: 2048

### NextToken
- **Type**: string
- **Pattern**: `\p{ASCII}{0,8192}`
- **Max Length**: 8192

### Policy
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 20000

### PolicyRevisionId
- **Type**: string
- **Pattern**: `[0-9A-Fa-f]+`
- **Max Length**: 50

### ResourceArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:.+`
- **Min Length**: 20
- **Max Length**: 2048

### RetrainingFrequency
- **Type**: string
- **Pattern**: `^P(\dY)?(\d{1,2}M)?(\d{1,3}D)?$`
- **Min Length**: 1
- **Max Length**: 10

### S3Bucket
- **Type**: string
- **Pattern**: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### S3Key
- **Type**: string
- **Pattern**: `[\P{M}\p{M}]{1,1024}[^/]$`
- **Min Length**: 1
- **Max Length**: 1024

### S3Prefix
- **Type**: string
- **Pattern**: `(^$)|([\u0009\u000A\u000D\u0020-\u00FF]{1,1023}/$)`
- **Min Length**: 0
- **Max Length**: 1024

### SensorName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z:#$.\-_]{1,200}$`
- **Min Length**: 1
- **Max Length**: 200

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\s\w+-=\.:/@]*`
- **Min Length**: 0
- **Max Length**: 256

### TimeZoneOffset
- **Type**: string
- **Pattern**: `^(\+|\-)[0-9]{2}\:[0-9]{2}$`


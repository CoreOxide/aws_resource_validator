# Rekognition Service

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### CollectionId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-]+`
- **Min Length**: 1
- **Max Length**: 255

### DatasetArn
- **Type**: string
- **Pattern**: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`
- **Min Length**: 20
- **Max Length**: 2048

### DatasetEntry
- **Type**: string
- **Pattern**: `^\{.*\}$`
- **Min Length**: 1
- **Max Length**: 100000

### DatasetLabel
- **Type**: string
- **Pattern**: `.{1,}`
- **Min Length**: 1
- **Max Length**: 255

### ExternalImageId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-:]+`
- **Min Length**: 1
- **Max Length**: 255

### FaceId
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

### GeneralLabelsFilterValue
- **Type**: string
- **Pattern**: `[A-Za-z0-9àâèçñó\'-_(). ]*`
- **Min Length**: 0
- **Max Length**: 50

### HumanLoopName
- **Type**: string
- **Pattern**: `^[a-z0-9](-*[a-z0-9])*`
- **Min Length**: 1
- **Max Length**: 63

### ImageId
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

### IndexFacesModelVersion
- **Type**: string
- **Pattern**: `[0-9\.]+`

### JobId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### JobTag
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-:+=\/]+`
- **Min Length**: 1
- **Max Length**: 1024

### KinesisDataArn
- **Type**: string
- **Pattern**: `(^arn:([a-z\d-]+):kinesis:([a-z\d-]+):\d{12}:.+$)`

### KinesisVideoArn
- **Type**: string
- **Pattern**: `(^arn:([a-z\d-]+):kinesisvideo:([a-z\d-]+):\d{12}:.+$)`

### KinesisVideoStreamFragmentNumber
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 128

### KmsKeyId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
- **Min Length**: 1
- **Max Length**: 2048

### LivenessS3KeyPrefix
- **Type**: string
- **Pattern**: `\S*`
- **Max Length**: 950

### LivenessSessionId
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### MediaAnalysisJobId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### MediaAnalysisJobName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-]+`
- **Min Length**: 1
- **Max Length**: 64

### MediaAnalysisS3KeyPrefix
- **Type**: string
- **Pattern**: `\S*`
- **Max Length**: 800

### ProjectArn
- **Type**: string
- **Pattern**: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
- **Min Length**: 20
- **Max Length**: 2048

### ProjectName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-]+`
- **Min Length**: 1
- **Max Length**: 255

### ProjectPolicyDocument
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 2000

### ProjectPolicyName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-]+`
- **Min Length**: 1
- **Max Length**: 128

### ProjectPolicyRevisionId
- **Type**: string
- **Pattern**: `[0-9A-Fa-f]+`
- **Max Length**: 64

### ProjectVersionArn
- **Type**: string
- **Pattern**: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
- **Min Length**: 20
- **Max Length**: 2048

### ProjectVersionId
- **Type**: string
- **Pattern**: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
- **Min Length**: 20
- **Max Length**: 2048

### QueryString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2048

### RekognitionUniqueId
- **Type**: string
- **Pattern**: `[0-9A-Za-z]*`

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

### S3Bucket
- **Type**: string
- **Pattern**: `[0-9A-Za-z\.\-_]*`
- **Min Length**: 3
- **Max Length**: 255

### SNSTopicArn
- **Type**: string
- **Pattern**: `(^arn:aws:sns:.*:\w{12}:.+$)`

### StreamProcessorArn
- **Type**: string
- **Pattern**: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:streamprocessor\/.+$)`

### StreamProcessorName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-]+`
- **Min Length**: 1
- **Max Length**: 128

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### UserId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-:]+`
- **Min Length**: 1
- **Max Length**: 128

### VersionDescription
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_. ()\':,;?]+`
- **Min Length**: 1
- **Max Length**: 255

### VersionName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-]+`
- **Min Length**: 1
- **Max Length**: 255


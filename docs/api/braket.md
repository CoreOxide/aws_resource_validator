# Braket Service

### BraketResourceArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:braket:[a-z0-9\-]*:[0-9]{12}:.*$`

### CreateJobRequestJobNameString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,50}$`
- **Min Length**: 1
- **Max Length**: 50

### GetJobResponseJobNameString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,50}$`
- **Min Length**: 1
- **Max Length**: 50

### HyperParametersValueString
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 2500

### InputFileConfigChannelNameString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9\.\-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### JobArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:job/.*$`

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`

### S3Path
- **Type**: string
- **Pattern**: `^(https|s3)://([^/]+)/?(.*)$`
- **Min Length**: 0
- **Max Length**: 1024

### Uri
- **Type**: string
- **Pattern**: `\d{10,14}\.dkr\.ecr.[a-z0-9-]+\.amazonaws\.com\/.+(@sha256)?:.+`
- **Min Length**: 1
- **Max Length**: 255


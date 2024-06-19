# Kinesisvideo Service

### ChannelName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256

### DestinationRegion
- **Type**: string
- **Pattern**: `^[a-z]+(-[a-z]+)?-[a-z]+-[0-9]$`
- **Min Length**: 9
- **Max Length**: 14

### DestinationUri
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9]+:(//)?([^/]+)/?([^*]*)$`
- **Min Length**: 1
- **Max Length**: 255

### DeviceName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 128

### FormatConfigValue
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9]+`
- **Min Length**: 0
- **Max Length**: 256

### HubDeviceArn
- **Type**: string
- **Pattern**: `arn:[a-z\d-]+:iot:[a-z0-9-]+:[0-9]+:thing/[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 1024

### KmsKeyId
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 2048

### MediaType
- **Type**: string
- **Pattern**: `[\w\-\.\+]+/[\w\-\.\+]+(,[\w\-\.\+]+/[\w\-\.\+]+)*`
- **Min Length**: 1
- **Max Length**: 128

### MediaUriSecretArn
- **Type**: string
- **Pattern**: `arn:[a-z\d-]+:secretsmanager:[a-z0-9-]+:[0-9]+:secret:[a-zA-Z0-9_.-]+`
- **Min Length**: 20
- **Max Length**: 2048

### NextToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+/=]*`
- **Min Length**: 0
- **Max Length**: 1024

### ResourceARN
- **Type**: string
- **Pattern**: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
- **Min Length**: 1
- **Max Length**: 1024

### ScheduleExpression
- **Type**: string
- **Pattern**: `[^\n]{11,100}`
- **Min Length**: 11
- **Max Length**: 100

### StreamName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Min Length**: 0
- **Max Length**: 256

### Version
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 64


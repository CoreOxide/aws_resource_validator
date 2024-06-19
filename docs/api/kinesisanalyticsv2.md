# Kinesisanalyticsv2 Service

### ApplicationMaintenanceWindowEndTime
- **Type**: string
- **Pattern**: `([01][0-9]|2[0-3]):[0-5][0-9]`
- **Min Length**: 5
- **Max Length**: 5

### ApplicationMaintenanceWindowStartTime
- **Type**: string
- **Pattern**: `([01][0-9]|2[0-3]):[0-5][0-9]`
- **Min Length**: 5
- **Max Length**: 5

### ApplicationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 128

### BasePath
- **Type**: string
- **Pattern**: `[a-zA-Z0-9/!-_.*\'()]+`
- **Min Length**: 1
- **Max Length**: 1024

### BucketARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### ConditionalToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_+/=]+`
- **Min Length**: 1
- **Max Length**: 512

### DatabaseARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### Id
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 50

### InAppStreamName
- **Type**: string
- **Pattern**: `[^-\s<>&]*`
- **Min Length**: 1
- **Max Length**: 32

### KinesisAnalyticsARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### LogStreamARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### MavenArtifactId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256

### MavenGroupId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256

### MavenVersion
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256

### RecordColumnName
- **Type**: string
- **Pattern**: `[^-\s<>&]*`
- **Min Length**: 1
- **Max Length**: 256

### RecordEncoding
- **Type**: string
- **Pattern**: `UTF-8`
- **Min Length**: 5
- **Max Length**: 5

### RecordRowPath
- **Type**: string
- **Pattern**: `^(?=^\$)(?=^\S+$).*$`
- **Min Length**: 1
- **Max Length**: 65535

### ResourceARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### RoleARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### SnapshotName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256


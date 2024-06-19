# Kinesisanalytics Service

### ApplicationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 128

### BucketARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### Id
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 50

### KinesisAnalyticsARN
- **Type**: string
- **Pattern**: `arn:aws:kinesisanalytics:[a-z]{2}-[a-z]+-\d{1}+:\d{12}+:application/[a-zA-Z0-9_.-]{1,128}`
- **Min Length**: 1
- **Max Length**: 2048

### LogStreamARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### RecordEncoding
- **Type**: string
- **Pattern**: `UTF-8`

### ResourceARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 2048

### RoleARN
- **Type**: string
- **Pattern**: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
- **Min Length**: 1
- **Max Length**: 2048


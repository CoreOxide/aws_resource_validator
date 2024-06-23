# Machinelearning Service

### AwsUserArn
- **Type**: string
- **Pattern**: `arn:aws:iam::[0-9]+:((user/.+)|(root))`

### ComparatorValue
- **Type**: string
- **Pattern**: `.*\S.*|^$`
- **Max Length**: 1024

### EntityId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 64

### EntityName
- **Type**: string
- **Pattern**: `.*\S.*|^$`
- **Max Length**: 1024

### RDSInstanceIdentifier
- **Type**: string
- **Pattern**: `[a-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 63

### RedshiftClusterIdentifier
- **Type**: string
- **Pattern**: `[a-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 63

### RedshiftDatabaseName
- **Type**: string
- **Pattern**: `[a-z0-9]+`
- **Min Length**: 1
- **Max Length**: 64

### S3Url
- **Type**: string
- **Pattern**: `s3://([^/]+)(/.*)?`
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### VipURL
- **Type**: string
- **Pattern**: `https://[a-zA-Z0-9-.]*\.amazon(aws)?\.com[/]?`
- **Max Length**: 2048


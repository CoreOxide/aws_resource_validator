# Mwaa Service

### AirflowVersion
- **Type**: string
- **Pattern**: `^[0-9a-z.]+$`
- **Min Length**: 1
- **Max Length**: 32

### CeleryExecutorQueue
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:sqs:[a-z0-9\-]+:\d{12}:[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 1
- **Max Length**: 1224

### CloudWatchLogGroupArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:logs:[a-z0-9\-]+:\d{12}:log-group:\w+`
- **Min Length**: 1
- **Max Length**: 1224

### ConfigKey
- **Type**: string
- **Pattern**: `^[a-z]+([a-z0-9._]*[a-z0-9_]+)?$`
- **Min Length**: 1
- **Max Length**: 64

### ConfigValue
- **Type**: string
- **Pattern**: `^[ -~]+$`
- **Min Length**: 1
- **Max Length**: 65536

### EnvironmentArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:airflow:[a-z0-9\-]+:\d{12}:environment/\w+`
- **Min Length**: 1
- **Max Length**: 1224

### EnvironmentName
- **Type**: string
- **Pattern**: `^[a-zA-Z][0-9a-zA-Z-_]*$`
- **Min Length**: 1
- **Max Length**: 80

### ErrorMessage
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 1024

### Hostname
- **Type**: string
- **Pattern**: `^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$`
- **Min Length**: 1
- **Max Length**: 255

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 1
- **Max Length**: 1224

### KmsKey
- **Type**: string
- **Pattern**: `^(((arn:aws(-[a-z]+)?:kms:[a-z]{2}-[a-z]+-\d:\d+:)?key\/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}|(arn:aws(-[a-z]+)?:kms:[a-z]{2}-[a-z]+-\d:\d+:)?alias/.+)$`
- **Min Length**: 1
- **Max Length**: 1224

### RelativePath
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### S3BucketArn
- **Type**: string
- **Pattern**: `^arn:aws(-[a-z]+)?:s3:::[a-z0-9.\-]+$`
- **Min Length**: 1
- **Max Length**: 1224

### SecurityGroupId
- **Type**: string
- **Pattern**: `^sg-[a-zA-Z0-9\-._]+$`
- **Min Length**: 1
- **Max Length**: 1024

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-[a-zA-Z0-9\-._]+$`
- **Min Length**: 1
- **Max Length**: 1024

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 256

### UpdateSource
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 256

### VpcEndpointServiceName
- **Type**: string
- **Pattern**: `^([a-z.-]+)?com\.amazonaws\.vpce\.[a-z0-9\-]+\.[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 1
- **Max Length**: 1224

### WebserverUrl
- **Type**: string
- **Pattern**: `^https://.+$`
- **Min Length**: 1
- **Max Length**: 256

### WeeklyMaintenanceWindowStart
- **Type**: string
- **Pattern**: `(MON|TUE|WED|THU|FRI|SAT|SUN):([01]\d|2[0-3]):(00|30)`
- **Min Length**: 1
- **Max Length**: 9


# Iotfleetwise Service

### CloudWatchLogGroupName
- **Type**: string
- **Pattern**: `[\.\-_\/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### IAMRoleArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
- **Min Length**: 20
- **Max Length**: 2048

### NodePath
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.]+`
- **Min Length**: 1
- **Max Length**: 150

### Prefix
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_:./!*\'()]+`
- **Min Length**: 1
- **Max Length**: 512

### S3BucketArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):s3:::.+`
- **Min Length**: 16
- **Max Length**: 100

### TimestreamDatabaseName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 3
- **Max Length**: 255

### TimestreamTableArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):timestream:[a-zA-Z0-9-]+:[0-9]{12}:database/[a-zA-Z0-9_.-]+/table/[a-zA-Z0-9_.-]+`
- **Min Length**: 20
- **Max Length**: 2048

### TimestreamTableName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 3
- **Max Length**: 255

### TopicName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-#:./]+`
- **Min Length**: 1
- **Max Length**: 150

### attributeName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 150

### campaignName
- **Type**: string
- **Pattern**: `[a-zA-Z\d\-_:]+`
- **Min Length**: 1
- **Max Length**: 100

### description
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1
- **Max Length**: 2048

### fleetId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 100

### message
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1
- **Max Length**: 2048

### resourceName
- **Type**: string
- **Pattern**: `[a-zA-Z\d\-_:]+`
- **Min Length**: 1
- **Max Length**: 100

### vehicleName
- **Type**: string
- **Pattern**: `[a-zA-Z\d\-_:]+`
- **Min Length**: 1
- **Max Length**: 100

### wildcardSignalName
- **Type**: string
- **Pattern**: `[\w|*|-]+(\.[\w|*|-]+)*`
- **Min Length**: 1
- **Max Length**: 150


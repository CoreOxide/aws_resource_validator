# Iotanalytics Service

### BucketKeyExpression
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9!_.*\'()/{}:-]*$`
- **Min Length**: 1
- **Max Length**: 255

### BucketName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9.\-_]*$`
- **Min Length**: 3
- **Max Length**: 255

### ChannelName
- **Type**: string
- **Pattern**: `(^(?!_{2}))(^[a-zA-Z0-9_]+$)`
- **Min Length**: 1
- **Max Length**: 128

### ColumnDataType
- **Type**: string
- **Pattern**: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
- **Min Length**: 1
- **Max Length**: 131072

### ColumnName
- **Type**: string
- **Pattern**: `^[A-Za-z_]([A-Za-z0-9]*|[A-Za-z0-9][A-Za-z0-9_]*)$`
- **Min Length**: 1
- **Max Length**: 255

### DatasetActionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]+$`
- **Min Length**: 1
- **Max Length**: 128

### DatasetName
- **Type**: string
- **Pattern**: `(^(?!_{2}))(^[a-zA-Z0-9_]+$)`
- **Min Length**: 1
- **Max Length**: 128

### DatastoreName
- **Type**: string
- **Pattern**: `(^(?!_{2}))(^[a-zA-Z0-9_]+$)`
- **Min Length**: 1
- **Max Length**: 128

### GlueDatabaseName
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 150

### GlueTableName
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 150

### IotEventsInputName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 128

### LambdaName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 64

### LateDataRuleName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]+$`
- **Min Length**: 1
- **Max Length**: 128

### MessageId
- **Type**: string
- **Pattern**: `\p{ASCII}*`
- **Min Length**: 1
- **Max Length**: 128

### OutputFileName
- **Type**: string
- **Pattern**: `[\w\.-]{1,255}`

### PartitionAttributeName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]+$`
- **Min Length**: 1
- **Max Length**: 128

### PipelineName
- **Type**: string
- **Pattern**: `(^(?!_{2}))(^[a-zA-Z0-9_]+$)`
- **Min Length**: 1
- **Max Length**: 128

### S3KeyPrefix
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9!_.*\'()/{}:-]*/$`
- **Min Length**: 1
- **Max Length**: 255

### S3PathChannelMessage
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/_!\'(){}\*\s\.\-\=\:]+$`
- **Min Length**: 1
- **Max Length**: 1024

### TimestampFormat
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s\[\]_,.\'/:-]*$`
- **Min Length**: 1
- **Max Length**: 50


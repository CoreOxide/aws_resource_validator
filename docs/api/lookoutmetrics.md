# Lookoutmetrics Service

### AlertDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Max Length**: 256

### AlertName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
- **Min Length**: 1
- **Max Length**: 63

### AnomalyDetectionTaskStatusMessage
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### AnomalyDetectorDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### AnomalyDetectorName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
- **Min Length**: 1
- **Max Length**: 63

### Arn
- **Type**: string
- **Pattern**: `arn:([a-z\d-]+):.*:.*:.*:.+`
- **Max Length**: 256

### AthenaDataCatalog
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 256

### AthenaDatabaseName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_]+`
- **Min Length**: 1
- **Max Length**: 255

### AthenaS3ResultsPath
- **Type**: string
- **Pattern**: `^s3://[a-z0-9].+$`
- **Max Length**: 1024

### AthenaTableName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_]+`
- **Min Length**: 1
- **Max Length**: 128

### AthenaWorkGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._-]{1,128}`
- **Min Length**: 1
- **Max Length**: 128

### Charset
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
- **Max Length**: 63

### ColumnName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
- **Min Length**: 1
- **Max Length**: 63

### DataQualityMetricDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### DatabaseHost
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 253

### DateTimeFormat
- **Type**: string
- **Pattern**: `.*\S.*`
- **Max Length**: 63

### Delimiter
- **Type**: string
- **Pattern**: `[^\r\n]`
- **Max Length**: 1

### FlowName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][\w!@#.-]+`
- **Max Length**: 256

### HistoricalDataPath
- **Type**: string
- **Pattern**: `^s3://[a-z0-9].+$`
- **Max Length**: 1024

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws.*:kms:.*:[0-9]{12}:key/[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}`
- **Min Length**: 20
- **Max Length**: 2048

### MetricName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
- **Max Length**: 256

### MetricSetDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### MetricSetName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
- **Min Length**: 1
- **Max Length**: 63

### Namespace
- **Type**: string
- **Pattern**: `[^:].*`
- **Min Length**: 1
- **Max Length**: 255

### NextToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 3000

### PoirotSecretManagerArn
- **Type**: string
- **Pattern**: `arn:([a-z\d-]+):.*:.*:secret:AmazonLookoutMetrics-.+`
- **Max Length**: 256

### QuoteSymbol
- **Type**: string
- **Pattern**: `[^\r\n]|^$`
- **Max Length**: 1

### RDSDatabaseIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z](?!.*--)(?!.*-$)[0-9a-zA-Z\-]*$`
- **Min Length**: 1
- **Max Length**: 63

### RDSDatabaseName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.]+`
- **Min Length**: 1
- **Max Length**: 64

### RedshiftClusterIdentifier
- **Type**: string
- **Pattern**: `^[a-z](?!.*--)(?!.*-$)[0-9a-z\-]*$`
- **Min Length**: 1
- **Max Length**: 63

### RedshiftDatabaseName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.]+`
- **Min Length**: 1
- **Max Length**: 100

### RelatedColumnName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### SecurityGroupId
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 255

### SubnetId
- **Type**: string
- **Pattern**: `[\-0-9a-zA-Z]+`
- **Max Length**: 255

### TableName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_.]*$`
- **Min Length**: 1
- **Max Length**: 100

### TemplatedPath
- **Type**: string
- **Pattern**: `^s3://[a-zA-Z0-9_\-\/ {}=]+$`
- **Max Length**: 1024

### TimeSeriesId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Max Length**: 520

### TimestampString
- **Type**: string
- **Pattern**: `^([12]\d{3})-(1[0-2]|0[1-9])-(0[1-9]|[12]\d|3[01])T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)(Z|(\+|\-)(0\d|1[0-2]):([0-5]\d)(\[[[:alnum:]\/\_]+\])?)$`
- **Max Length**: 60

### Timezone
- **Type**: string
- **Pattern**: `.*\S.*`
- **Max Length**: 60

### UUID
- **Type**: string
- **Pattern**: `[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}`
- **Max Length**: 63


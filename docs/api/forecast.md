# Forecast Service

### Arn
- **Type**: string
- **Pattern**: `arn:([a-z\d-]+):forecast:.*:.*:.+`
- **Max Length**: 256

### AttributeValue
- **Type**: string
- **Pattern**: `.+`
- **Max Length**: 256

### ForecastType
- **Type**: string
- **Pattern**: `(^0?\.\d\d?$|^mean$)`
- **Min Length**: 2
- **Max Length**: 4

### Format
- **Type**: string
- **Pattern**: `^CSV|PARQUET$`
- **Max Length**: 7

### Frequency
- **Type**: string
- **Pattern**: `^Y|M|W|D|H|30min|15min|10min|5min|1min$`
- **Min Length**: 1
- **Max Length**: 5

### GeolocationFormat
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]+$`
- **Max Length**: 256

### KMSKeyArn
- **Type**: string
- **Pattern**: `arn:aws:kms:.*:key/.*`
- **Max Length**: 256

### LocalDateTime
- **Type**: string
- **Pattern**: `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$`
- **Max Length**: 19

### LongArn
- **Type**: string
- **Pattern**: `arn:([a-z\d-]+):forecast:.*:.*:.+`
- **Max Length**: 300

### Name
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*`
- **Min Length**: 1
- **Max Length**: 63

### NextToken
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 3000

### ParameterKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\.\/\[\]\,\\]+$`
- **Max Length**: 256

### ParameterValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\_\.\/\[\]\,\"\\\s]+$`
- **Max Length**: 256

### S3Path
- **Type**: string
- **Pattern**: `^s3://[a-z0-9].+$`
- **Min Length**: 7
- **Max Length**: 4096

### String
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_]+$`
- **Max Length**: 256

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

### TimeZone
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\+\-\_]+$`
- **Max Length**: 256

### TimestampFormat
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-\:\.\,\\'\s]+$`
- **Max Length**: 256

### Value
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_\-]+$`
- **Max Length**: 256


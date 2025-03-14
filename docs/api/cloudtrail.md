# Cloudtrail Service

### AccountId
- **Type**: string
- **Pattern**: `\d+`
- **Min Length**: 12
- **Max Length**: 16

### ChannelArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:]+$`
- **Min Length**: 3
- **Max Length**: 256

### ChannelName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._\-]+$`
- **Min Length**: 3
- **Max Length**: 128

### DashboardArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:]+$`

### DashboardName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-]+$`
- **Min Length**: 3
- **Max Length**: 128

### DeliveryS3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
- **Max Length**: 1024

### ErrorCode
- **Type**: string
- **Pattern**: `^[\w\d\s_.,\-:\[\]]+$`
- **Max Length**: 128

### ErrorMessage
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 4
- **Max Length**: 1000

### EventDataStoreArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:]+$`
- **Min Length**: 3
- **Max Length**: 256

### EventDataStoreKmsKeyId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:]+$`
- **Min Length**: 1
- **Max Length**: 350

### EventDataStoreName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._\-]+$`
- **Min Length**: 3
- **Max Length**: 128

### EventName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_]+$`
- **Max Length**: 128

### EventSource
- **Type**: string
- **Pattern**: `^[a-z0-9_-]+\.amazonaws\.com$`
- **Max Length**: 256

### FederationRoleArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:@=\+,\.]+$`
- **Min Length**: 3
- **Max Length**: 125

### Location
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:]+$`
- **Min Length**: 3
- **Max Length**: 1024

### OperatorValue
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 2048

### PaginationToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 4
- **Max Length**: 1000

### PartitionKeyName
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### PartitionKeyType
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 255

### Prompt
- **Type**: string
- **Pattern**: `^[ -~\n]*$`
- **Min Length**: 3
- **Max Length**: 500

### QueryAlias
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9._\-]*$`
- **Min Length**: 1
- **Max Length**: 256

### QueryParameter
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### QueryParameterKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:$]+$`
- **Min Length**: 3
- **Max Length**: 128

### QueryParameterValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:]+$`
- **Min Length**: 1
- **Max Length**: 128

### QueryStatement
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 1
- **Max Length**: 10000

### RefreshId
- **Type**: string
- **Pattern**: `\d+`
- **Min Length**: 10
- **Max Length**: 20

### ResourceArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:]+$`
- **Min Length**: 3
- **Max Length**: 256

### SearchSampleQueriesSearchPhrase
- **Type**: string
- **Pattern**: `^[ -~\n]*$`
- **Min Length**: 2
- **Max Length**: 1000

### SelectorField
- **Type**: string
- **Pattern**: `[\w|\d|\.|_]+`
- **Min Length**: 1
- **Max Length**: 1000

### SelectorName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1000

### Source
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### TimeOfDay
- **Type**: string
- **Pattern**: `^[0-9]{2}:[0-9]{2}`

### UUID
- **Type**: string
- **Pattern**: `^[a-f0-9\-]+$`
- **Min Length**: 36
- **Max Length**: 36

### ViewPropertiesKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._\-]+$`
- **Min Length**: 3
- **Max Length**: 128

### ViewPropertiesValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._\- ]+$`
- **Min Length**: 1
- **Max Length**: 128


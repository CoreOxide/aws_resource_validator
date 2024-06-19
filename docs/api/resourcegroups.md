# Resourcegroups Service

### Description
- **Type**: string
- **Pattern**: `[\sa-zA-Z0-9_\.-]*`
- **Max Length**: 1024

### GroupArn
- **Type**: string
- **Pattern**: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\.-]{1,300}`
- **Min Length**: 12
- **Max Length**: 1600

### GroupConfigurationParameterName
- **Type**: string
- **Pattern**: `[a-z-]+`
- **Min Length**: 1
- **Max Length**: 80

### GroupConfigurationParameterValue
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:\/\._-]+`
- **Min Length**: 1
- **Max Length**: 256

### GroupConfigurationType
- **Type**: string
- **Pattern**: `AWS::[a-zA-Z0-9]+::[a-zA-Z0-9]+`
- **Max Length**: 40

### GroupFilterValue
- **Type**: string
- **Pattern**: `AWS::(AllSupported|[a-zA-Z0-9]+::[a-zA-Z0-9]+)`
- **Min Length**: 1
- **Max Length**: 128

### GroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\.-]+`
- **Min Length**: 1
- **Max Length**: 300

### GroupString
- **Type**: string
- **Pattern**: `(arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/)?[a-zA-Z0-9_\.-]{1,300}`
- **Min Length**: 1
- **Max Length**: 1600

### NextToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+/]*={0,2}$`
- **Min Length**: 0
- **Max Length**: 8192

### Query
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 4096

### QueryType
- **Type**: string
- **Pattern**: `^\w+$`
- **Min Length**: 1
- **Max Length**: 128

### ResourceArn
- **Type**: string
- **Pattern**: `arn:aws(-[a-z]+)*:[a-z0-9\-]*:([a-z]{2}(-[a-z]+)+-\d{1})?:([0-9]{12})?:.+`

### ResourceFilterValue
- **Type**: string
- **Pattern**: `AWS::[a-zA-Z0-9]+::[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 128

### ResourceType
- **Type**: string
- **Pattern**: `AWS::[a-zA-Z0-9]+::\w+`

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


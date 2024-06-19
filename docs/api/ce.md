# Ce Service

### Arn
- **Type**: string
- **Pattern**: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
- **Min Length**: 20
- **Max Length**: 2048

### CostCategoryName
- **Type**: string
- **Pattern**: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
- **Min Length**: 1
- **Max Length**: 50

### CostCategoryValue
- **Type**: string
- **Pattern**: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
- **Min Length**: 1
- **Max Length**: 50

### GenericString
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

### GroupDefinitionKey
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

### MetricName
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

### NextPageToken
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 8192

### RecommendationDetailId
- **Type**: string
- **Pattern**: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### RecommendationId
- **Type**: string
- **Pattern**: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### ResourceTagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### ResourceTagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### SearchString
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

### SortDefinitionKey
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

### SubscriberAddress
- **Type**: string
- **Pattern**: `(^[a-zA-Z0-9.!#$%&\'*+=?^_‘{|}~-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$)|(^arn:(aws[a-zA-Z-]*):sns:[a-zA-Z0-9-]+:[0-9]{12}:[a-zA-Z0-9_-]+(\.fifo)?$)`
- **Min Length**: 6
- **Max Length**: 302

### TagKey
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

### Value
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 1024

### YearMonthDay
- **Type**: string
- **Pattern**: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
- **Min Length**: 0
- **Max Length**: 40

### ZonedDateTime
- **Type**: string
- **Pattern**: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
- **Min Length**: 20
- **Max Length**: 25


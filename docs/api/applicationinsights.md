# Applicationinsights Service

### AccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### AmazonResourceName
- **Type**: string
- **Pattern**: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
- **Min Length**: 1
- **Max Length**: 1011

### ComponentConfiguration
- **Type**: string
- **Pattern**: `[\S\s]+`
- **Min Length**: 1
- **Max Length**: 10000

### ComponentName
- **Type**: string
- **Pattern**: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
- **Min Length**: 1
- **Max Length**: 1011

### CustomComponentName
- **Type**: string
- **Pattern**: `^[\d\w\-_\.+]*$`
- **Min Length**: 1
- **Max Length**: 128

### LogPatternName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\.\-_]*`
- **Min Length**: 1
- **Max Length**: 50

### LogPatternRegex
- **Type**: string
- **Pattern**: `[\S\s]+`
- **Min Length**: 1
- **Max Length**: 50

### LogPatternSetName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\.\-_]*`
- **Min Length**: 1
- **Max Length**: 30

### ObservationId
- **Type**: string
- **Pattern**: `o-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
- **Min Length**: 38
- **Max Length**: 38

### OpsItemSNSTopicArn
- **Type**: string
- **Pattern**: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
- **Min Length**: 20
- **Max Length**: 300

### PaginationToken
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 1024

### ProblemId
- **Type**: string
- **Pattern**: `p-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
- **Min Length**: 38
- **Max Length**: 38

### ResourceARN
- **Type**: string
- **Pattern**: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
- **Min Length**: 1
- **Max Length**: 1011

### ResourceGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\.\-_]*`
- **Min Length**: 1
- **Max Length**: 256

### ResourceType
- **Type**: string
- **Pattern**: `[0-9a-zA-Z:_]*`
- **Min Length**: 1
- **Max Length**: 50

### SNSNotificationArn
- **Type**: string
- **Pattern**: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
- **Min Length**: 20
- **Max Length**: 300

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

### WorkloadId
- **Type**: string
- **Pattern**: `w-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
- **Min Length**: 38
- **Max Length**: 38

### WorkloadName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\.\-_]*`
- **Min Length**: 1
- **Max Length**: 12


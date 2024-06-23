# Logs Service

### AccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### AmazonResourceName
- **Type**: string
- **Pattern**: `[\w+=/:,.@-]*`
- **Min Length**: 1
- **Max Length**: 1011

### AnomalyDetectorArn
- **Type**: string
- **Pattern**: `[\w#+=/:,.@-]*`
- **Min Length**: 1

### ClientToken
- **Type**: string
- **Pattern**: `\S{36,128}`
- **Min Length**: 36
- **Max Length**: 128

### DeliveryDestinationName
- **Type**: string
- **Pattern**: `[\w-]*`
- **Min Length**: 1
- **Max Length**: 60

### DeliveryId
- **Type**: string
- **Pattern**: `^[0-9A-Za-z]+$`
- **Min Length**: 1
- **Max Length**: 64

### DeliverySourceName
- **Type**: string
- **Pattern**: `[\w-]*`
- **Min Length**: 1
- **Max Length**: 60

### DestinationName
- **Type**: string
- **Pattern**: `[^:*]*`
- **Min Length**: 1
- **Max Length**: 512

### FilterName
- **Type**: string
- **Pattern**: `[^:*]*`
- **Min Length**: 1
- **Max Length**: 512

### LogGroupArn
- **Type**: string
- **Pattern**: `[\w#+=/:,.@-]*`
- **Min Length**: 1
- **Max Length**: 2048

### LogGroupIdentifier
- **Type**: string
- **Pattern**: `[\w#+=/:,.@-]*`
- **Min Length**: 1
- **Max Length**: 2048

### LogGroupName
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### LogGroupNamePattern
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]*`
- **Min Length**: 0
- **Max Length**: 512

### LogStreamName
- **Type**: string
- **Pattern**: `[^:*]*`
- **Min Length**: 1
- **Max Length**: 512

### LogType
- **Type**: string
- **Pattern**: `[\w]*`
- **Min Length**: 1
- **Max Length**: 255

### MetricName
- **Type**: string
- **Pattern**: `[^:*$]*`
- **Max Length**: 255

### MetricNamespace
- **Type**: string
- **Pattern**: `[^:*$]*`
- **Max Length**: 255

### ResourceIdentifier
- **Type**: string
- **Pattern**: `[\w+=/:,.@\-\*]*`
- **Min Length**: 1
- **Max Length**: 2048

### Service
- **Type**: string
- **Pattern**: `[\w]*`
- **Min Length**: 1
- **Max Length**: 255

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Max Length**: 256


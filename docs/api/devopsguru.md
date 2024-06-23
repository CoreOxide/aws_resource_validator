# Devopsguru Service

### AnomalyId
- **Type**: string
- **Pattern**: `^[\w~.-]*$`
- **Min Length**: 1
- **Max Length**: 100

### AppBoundaryKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### AwsAccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ClientToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+[a-zA-Z0-9-]*$`
- **Min Length**: 1
- **Max Length**: 100

### EventResourceArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:[a-z0-9-]*:[a-z0-9-]*:\d{12}:.*$`
- **Min Length**: 36
- **Max Length**: 2048

### EventResourceName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### EventResourceType
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### EventSource
- **Type**: string
- **Pattern**: `^[a-z]+[a-z0-9]*\.amazonaws\.com|aws\.events$`
- **Min Length**: 10
- **Max Length**: 50

### InsightId
- **Type**: string
- **Pattern**: `^[\w-]*$`
- **Min Length**: 1
- **Max Length**: 100

### InsightName
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 1
- **Max Length**: 530

### KMSKeyId
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 2048

### MonitoredResourceName
- **Type**: string
- **Pattern**: `[\.\-_\/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### NotificationChannelId
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### OrganizationalUnitId
- **Type**: string
- **Pattern**: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
- **Max Length**: 68

### ResourceType
- **Type**: string
- **Pattern**: `^[a-zA-Z]+[a-zA-Z0-9-_:]*$`
- **Min Length**: 1
- **Max Length**: 256

### SsmOpsItemId
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 100

### StackName
- **Type**: string
- **Pattern**: `^[a-zA-Z*]+[a-zA-Z0-9-]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*|\*)$`
- **Min Length**: 0
- **Max Length**: 256

### TopicArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z0-9-]*:sns:[a-z0-9-]+:\d{12}:[^:]+$`
- **Min Length**: 36
- **Max Length**: 1024

### UuidNextToken
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36


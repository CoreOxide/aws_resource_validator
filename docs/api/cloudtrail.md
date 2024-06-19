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

### QueryStatement
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 1
- **Max Length**: 10000

### ResourceArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._/\-:]+$`
- **Min Length**: 3
- **Max Length**: 256

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

### UUID
- **Type**: string
- **Pattern**: `^[a-f0-9\-]+$`
- **Min Length**: 36
- **Max Length**: 36


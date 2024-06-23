# Chimesdkmessaging Service

### ChannelId
- **Type**: string
- **Pattern**: `[A-Za-z0-9]([A-Za-z0-9\:\-\_\.\@]{0,62}[A-Za-z0-9])?`
- **Min Length**: 1
- **Max Length**: 64

### ChimeArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 5
- **Max Length**: 1600

### ClientRequestToken
- **Type**: string
- **Pattern**: `[-_a-zA-Z0-9]*`
- **Min Length**: 2
- **Max Length**: 64

### Content
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 4096

### ContentType
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 45

### FilterRule
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1

### LambdaFunctionArn
- **Type**: string
- **Pattern**: `arn:aws:lambda:[a-z]{2}-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9\-_\.]+(:(\$LATEST|[a-zA-Z0-9\-_]+))?`
- **Min Length**: 15
- **Max Length**: 2048

### MessageAttributeName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 64

### MessageAttributeStringValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 512

### MessageId
- **Type**: string
- **Pattern**: `[-_a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### Metadata
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### NextToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2048

### NonEmptyContent
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1

### NonEmptyResourceName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 1
- **Max Length**: 256

### PushNotificationBody
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 150

### PushNotificationTitle
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 50

### ResourceName
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
- **Min Length**: 0
- **Max Length**: 256

### SearchFieldValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 512

### StatusDetail
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 256

### SubChannelId
- **Type**: string
- **Pattern**: `[-_a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128


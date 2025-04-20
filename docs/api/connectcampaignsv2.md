# Connectcampaignsv2 Service

### Arn
- **Type**: string
- **Pattern**: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-z]{2}-[a-z]+-\d{1,2}:[a-zA-Z0-9-]+:[^:]+(?:/[^:]+)*(?:/[^:]+)?(?:\:[^:]+)?`
- **Min Length**: 20
- **Max Length**: 500

### AttributeName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-_]+`
- **Min Length**: 0
- **Max Length**: 32767

### AttributeValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 32767

### CampaignId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-:/]*`
- **Min Length**: 0
- **Max Length**: 256

### ClientToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-.]*`
- **Min Length**: 0
- **Max Length**: 200

### DestinationPhoneNumber
- **Type**: string
- **Pattern**: `[\d\-+]*`
- **Min Length**: 0
- **Max Length**: 20

### DialRequestId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-.]*`
- **Min Length**: 0
- **Max Length**: 256

### EmailAddress
- **Type**: string
- **Pattern**: `.*[^\s@]+@[^\s@]+\.[^\s@]+.*`
- **Min Length**: 1
- **Max Length**: 255

### InstanceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-.]*`
- **Min Length**: 0
- **Max Length**: 256

### Iso8601Date
- **Type**: string
- **Pattern**: `\d{4}-\d{2}-\d{2}`

### Iso8601Duration
- **Type**: string
- **Pattern**: `P(?:([-+]?[0-9]+)D)?(T(?:([-+]?[0-9]+)H)?(?:([-+]?[0-9]+)M)?(?:([-+]?[0-9]+)(?:[.,]([0-9]{0,9}))?S)?)?`
- **Min Length**: 0
- **Max Length**: 50

### Iso8601Time
- **Type**: string
- **Pattern**: `T\d{2}:\d{2}`

### ProfileId
- **Type**: string
- **Pattern**: `[a-f0-9]{32}`

### ProfileOutboundRequestId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-.]*`
- **Min Length**: 0
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:)[a-zA-Z+-=._:/]+`
- **Min Length**: 1
- **Max Length**: 128

### TimeZone
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-/]*`
- **Min Length**: 0
- **Max Length**: 50


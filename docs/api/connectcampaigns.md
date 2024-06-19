# Connectcampaigns Service

### Arn
- **Type**: string
- **Pattern**: `arn:.*`
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
- **Pattern**: `[\S]*`
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

### InstanceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-.]*`
- **Min Length**: 0
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:)[a-zA-Z+-=._:/]+`
- **Min Length**: 1
- **Max Length**: 128


# Health Service

### accountId
- **Type**: string
- **Pattern**: `^\S+$`
- **Max Length**: 12

### availabilityZone
- **Type**: string
- **Pattern**: `[a-z]{2}\-[0-9a-z\-]{4,16}`
- **Min Length**: 6
- **Max Length**: 18

### entityArn
- **Type**: string
- **Pattern**: `.{0,1600}`
- **Max Length**: 1600

### entityValue
- **Type**: string
- **Pattern**: `.{0,1224}`
- **Max Length**: 1224

### eventArn
- **Type**: string
- **Pattern**: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
- **Max Length**: 1600

### eventType
- **Type**: string
- **Pattern**: `[^:/]{3,100}`
- **Min Length**: 3
- **Max Length**: 100

### eventTypeCode
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\_\-]{3,100}`
- **Min Length**: 3
- **Max Length**: 100

### locale
- **Type**: string
- **Pattern**: `.{2,256}`
- **Min Length**: 2
- **Max Length**: 256

### nextToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=/+_.-]{4,10000}`
- **Min Length**: 4
- **Max Length**: 10000

### region
- **Type**: string
- **Pattern**: `[^:/]{2,25}`
- **Min Length**: 2
- **Max Length**: 25

### service
- **Type**: string
- **Pattern**: `[^:/]{2,30}`
- **Min Length**: 2
- **Max Length**: 30

### tagKey
- **Type**: string
- **Pattern**: `.{0,127}`
- **Max Length**: 127

### tagValue
- **Type**: string
- **Pattern**: `.{0,255}`
- **Max Length**: 255


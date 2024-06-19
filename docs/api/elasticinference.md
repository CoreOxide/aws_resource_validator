# Elasticinference Service

### AcceleratorId
- **Type**: string
- **Pattern**: `^eia-[0-9a-f]+$`
- **Min Length**: 1
- **Max Length**: 256

### AcceleratorTypeName
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 256

### FilterName
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 128

### Key
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+/]+={0,2}$`
- **Min Length**: 1
- **Max Length**: 2048

### ResourceARN
- **Type**: string
- **Pattern**: `^arn:aws[^\s:]*:elastic-inference:[^\s:]+:\d{12}:elastic-inference-accelerator/eia-[0-9a-f]+$`
- **Min Length**: 1
- **Max Length**: 1011

### String
- **Type**: string
- **Pattern**: `^.*$`
- **Max Length**: 500000

### TagKey
- **Type**: string
- **Pattern**: `^\S$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 256


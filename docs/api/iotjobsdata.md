# Iotjobsdata Service

### ClientRequestTokenV2
- **Type**: string
- **Pattern**: `^[\x21-\x7E]+$`
- **Min Length**: 1
- **Max Length**: 64

### CommandExecutionId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### CommandParameterName
- **Type**: string
- **Pattern**: `^[.$a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 192

### DescribeJobExecutionJobId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+|^\$next`

### DetailsKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### DetailsValue
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Min Length**: 1

### JobId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### ThingName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### UnsignedLongParameterValue
- **Type**: string
- **Pattern**: `^[0-9]*$`
- **Min Length**: 1
- **Max Length**: 20


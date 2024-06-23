# Iotjobsdata Service

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
- **Pattern**: `[^\p{C}]*+`
- **Min Length**: 1
- **Max Length**: 1024

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


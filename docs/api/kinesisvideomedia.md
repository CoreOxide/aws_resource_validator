# Kinesisvideomedia Service

### ContentType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\.\-]+$`
- **Min Length**: 1
- **Max Length**: 128

### ContinuationToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\.\-]+$`
- **Min Length**: 1
- **Max Length**: 128

### FragmentNumberString
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 128

### ResourceARN
- **Type**: string
- **Pattern**: `arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
- **Min Length**: 1
- **Max Length**: 1024

### StreamName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256


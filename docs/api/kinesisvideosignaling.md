# Kinesisvideosignaling Service

### ClientId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256

### MessagePayload
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+/=]+`
- **Min Length**: 1
- **Max Length**: 10000

### Password
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256

### ResourceARN
- **Type**: string
- **Pattern**: `arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
- **Min Length**: 1
- **Max Length**: 1024

### Username
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256


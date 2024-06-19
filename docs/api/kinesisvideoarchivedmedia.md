# Kinesisvideoarchivedmedia Service

### ContentType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\.\-]+$`
- **Min Length**: 1
- **Max Length**: 128

### FormatConfigValue
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9]+`
- **Min Length**: 0
- **Max Length**: 256

### FragmentNumberString
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 128

### NextToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+/]+={0,2}`
- **Min Length**: 1
- **Max Length**: 4096

### ResourceARN
- **Type**: string
- **Pattern**: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
- **Min Length**: 1
- **Max Length**: 1024

### StreamName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 256


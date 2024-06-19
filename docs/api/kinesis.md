# Kinesis Service

### ConsumerARN
- **Type**: string
- **Pattern**: `^(arn):aws.*:kinesis:.*:\d{12}:.*stream\/[a-zA-Z0-9_.-]+\/consumer\/[a-zA-Z0-9_.-]+:[0-9]+`
- **Min Length**: 1
- **Max Length**: 2048

### ConsumerName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 128

### HashKey
- **Type**: string
- **Pattern**: `0|([1-9]\d{0,38})`

### ResourceARN
- **Type**: string
- **Pattern**: `arn:aws.*:kinesis:.*:\d{12}:.*stream/\S+`
- **Min Length**: 1
- **Max Length**: 2048

### SequenceNumber
- **Type**: string
- **Pattern**: `0|([1-9]\d{0,128})`

### ShardId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 128

### StreamARN
- **Type**: string
- **Pattern**: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
- **Min Length**: 1
- **Max Length**: 2048

### StreamName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 128


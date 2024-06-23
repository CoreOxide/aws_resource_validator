# Ebs Service

### BlockToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+/=]+$`
- **Max Length**: 256

### Checksum
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+/=]+$`
- **Max Length**: 64

### ChecksumAggregationMethod
- **Type**: string
- **Pattern**: `^[A-Za-z0-9]+$`
- **Max Length**: 32

### ChecksumAlgorithm
- **Type**: string
- **Pattern**: `^[A-Za-z0-9]+$`
- **Max Length**: 32

### Description
- **Type**: string
- **Pattern**: `^[\S\s]+$`
- **Max Length**: 255

### IdempotencyToken
- **Type**: string
- **Pattern**: `^[\S]+$`
- **Max Length**: 255

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws[a-z\-]*:kms:.*:[0-9]{12}:key/.*`
- **Min Length**: 1
- **Max Length**: 2048

### OwnerId
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 24

### PageToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+/=]+$`
- **Max Length**: 256

### SnapshotId
- **Type**: string
- **Pattern**: `^snap-[0-9a-f]+$`
- **Min Length**: 1
- **Max Length**: 64

### TagKey
- **Type**: string
- **Pattern**: `^[\S\s]+$`
- **Max Length**: 127

### TagValue
- **Type**: string
- **Pattern**: `^[\S\s]*$`
- **Max Length**: 255


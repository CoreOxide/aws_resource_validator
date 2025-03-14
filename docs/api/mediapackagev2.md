# Mediapackagev2 Service

### EncryptionConstantInitializationVectorString
- **Type**: string
- **Pattern**: `[0-9a-fA-F]+`
- **Min Length**: 32
- **Max Length**: 32

### EntityTag
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 256

### IdempotencyToken
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 256

### ListHarvestJobsRequestChannelNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 256

### ListHarvestJobsRequestOriginEndpointNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 256

### ManifestName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 256

### ResourceName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 256

### S3DestinationPath
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 1024

### SegmentSegmentNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 256

### SpekeKeyProviderResourceIdString
- **Type**: string
- **Pattern**: `[0-9a-zA-Z_-]+`
- **Min Length**: 1
- **Max Length**: 256


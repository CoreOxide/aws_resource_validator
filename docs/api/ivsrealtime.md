# Ivsrealtime Service

### AttributeKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 0
- **Max Length**: 128

### AutoParticipantRecordingStorageConfigurationArn
- **Type**: string
- **Pattern**: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+$`
- **Min Length**: 0
- **Max Length**: 128

### ChannelArn
- **Type**: string
- **Pattern**: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### CompositionArn
- **Type**: string
- **Pattern**: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:composition/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### CompositionClientToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 1
- **Max Length**: 64

### DestinationConfigurationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 0
- **Max Length**: 128

### EncoderConfigurationArn
- **Type**: string
- **Pattern**: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:encoder-configuration/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### EncoderConfigurationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 0
- **Max Length**: 128

### IngestConfigurationArn
- **Type**: string
- **Pattern**: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ingest-configuration/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### IngestConfigurationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 0
- **Max Length**: 128

### IngestConfigurationStageArn
- **Type**: string
- **Pattern**: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+$`
- **Min Length**: 0
- **Max Length**: 128

### PaginationToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+/=_-]*`
- **Min Length**: 0
- **Max Length**: 1024

### ParticipantClientAttribute
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_.,:;\s]*`
- **Min Length**: 0
- **Max Length**: 128

### ParticipantId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]*`
- **Min Length**: 0
- **Max Length**: 64

### ParticipantRecordingS3BucketName
- **Type**: string
- **Pattern**: `[a-z0-9-.]*`
- **Min Length**: 0
- **Max Length**: 63

### ParticipantRecordingS3Prefix
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]*`
- **Min Length**: 0
- **Max Length**: 256

### PublicKeyArn
- **Type**: string
- **Pattern**: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:public-key/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### PublicKeyMaterial
- **Type**: string
- **Pattern**: `.*-----BEGIN PUBLIC KEY-----\r?\n([a-zA-Z0-9+/=\r\n]+)\r?\n-----END PUBLIC KEY-----(\r?\n)?.*`

### PublicKeyName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 0
- **Max Length**: 128

### ResourceArn
- **Type**: string
- **Pattern**: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:[a-z-]/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### S3BucketName
- **Type**: string
- **Pattern**: `[a-z0-9-.]+`
- **Min Length**: 3
- **Max Length**: 63

### StageArn
- **Type**: string
- **Pattern**: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### StageName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 0
- **Max Length**: 128

### StageSessionId
- **Type**: string
- **Pattern**: `st-[a-zA-Z0-9]+`
- **Min Length**: 16
- **Max Length**: 16

### StorageConfigurationArn
- **Type**: string
- **Pattern**: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### StorageConfigurationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]*`
- **Min Length**: 0
- **Max Length**: 128

### StreamKey
- **Type**: string
- **Pattern**: `rt_[0-9]+_[a-z0-9-]+_[a-zA-Z0-9-]+_.+`


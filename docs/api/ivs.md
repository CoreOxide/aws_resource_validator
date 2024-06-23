# Ivs Service

### ChannelArn
- **Type**: string
- **Pattern**: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### ChannelName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 128

### ChannelPlaybackRestrictionPolicyArn
- **Type**: string
- **Pattern**: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-restriction-policy/[a-zA-Z0-9-]+$`
- **Min Length**: 0
- **Max Length**: 128

### ChannelRecordingConfigurationArn
- **Type**: string
- **Pattern**: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$`
- **Min Length**: 0
- **Max Length**: 128

### PaginationToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+/=_-]*$`
- **Min Length**: 0
- **Max Length**: 1024

### PlaybackKeyPairArn
- **Type**: string
- **Pattern**: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-key/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### PlaybackKeyPairName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 128

### PlaybackRestrictionPolicyArn
- **Type**: string
- **Pattern**: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-restriction-policy/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### PlaybackRestrictionPolicyName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 128

### RecordingConfigurationArn
- **Type**: string
- **Pattern**: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$`
- **Min Length**: 0
- **Max Length**: 128

### RecordingConfigurationName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]*$`
- **Min Length**: 0
- **Max Length**: 128

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:[a-z-]/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### S3DestinationBucketName
- **Type**: string
- **Pattern**: `^[a-z0-9-.]+$`
- **Min Length**: 3
- **Max Length**: 63

### StreamId
- **Type**: string
- **Pattern**: `^st-[a-zA-Z0-9]+$`
- **Min Length**: 26
- **Max Length**: 26

### StreamKeyArn
- **Type**: string
- **Pattern**: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:stream-key/[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128


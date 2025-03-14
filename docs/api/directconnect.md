# Directconnect Service

### CoreNetworkAttachmentId
- **Type**: string
- **Pattern**: `^attachment-([0-9a-f]{1,17})$`
- **Min Length**: 12
- **Max Length**: 28

### CoreNetworkIdentifier
- **Type**: string
- **Pattern**: `^core-network-([0-9a-f]{1,17})$`
- **Min Length**: 14
- **Max Length**: 30

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256


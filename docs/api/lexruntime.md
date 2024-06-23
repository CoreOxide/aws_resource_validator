# Lexruntime Service

### ActiveContextName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### BotVersion
- **Type**: string
- **Pattern**: `[0-9]+|\$LATEST`
- **Min Length**: 1
- **Max Length**: 64

### IntentSummaryCheckpointLabel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 255

### UserId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z._:-]+`
- **Min Length**: 2
- **Max Length**: 100


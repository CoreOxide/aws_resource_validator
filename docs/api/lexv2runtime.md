# Lexv2runtime Service

### ActiveContextName
- **Type**: string
- **Pattern**: `^([A-Za-z0-9]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### BotIdentifier
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 10
- **Max Length**: 10

### DTMFRegex
- **Type**: string
- **Pattern**: `^[A-D0-9#*]{1}$`
- **Min Length**: 1
- **Max Length**: 1

### EventId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z._:-]+`
- **Min Length**: 2
- **Max Length**: 100

### Name
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?)+$`
- **Min Length**: 1
- **Max Length**: 100

### SessionId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z._:-]+`
- **Min Length**: 2
- **Max Length**: 100


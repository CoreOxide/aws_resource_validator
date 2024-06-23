# Controltower Service

### Arn
- **Type**: string
- **Pattern**: `^arn:aws[0-9a-zA-Z_\-:\/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### BaselineArn
- **Type**: string
- **Pattern**: `^arn:[a-z-]+:controltower:[a-z0-9-]*:[0-9]{0,12}:baseline/[A-Z0-9]{16}$`

### BaselineVersion
- **Type**: string
- **Pattern**: `^\d+(?:\.\d+){0,2}$`
- **Min Length**: 1
- **Max Length**: 10

### ControlIdentifier
- **Type**: string
- **Pattern**: `^arn:aws[0-9a-zA-Z_\-:\/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### LandingZoneVersion
- **Type**: string
- **Pattern**: `^\d+.\d+$`
- **Min Length**: 3
- **Max Length**: 10

### ListEnabledBaselinesNextToken
- **Type**: string
- **Pattern**: `\S+`

### OperationIdentifier
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### TargetIdentifier
- **Type**: string
- **Pattern**: `^arn:aws[0-9a-zA-Z_\-:\/]+$`
- **Min Length**: 20
- **Max Length**: 2048


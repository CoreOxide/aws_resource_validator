# Gameliftstreams Service

### ApplicationLogOutputUri
- **Type**: string
- **Pattern**: `^$|^s3://([a-zA-Z0-9][a-zA-Z0-9._-]{1,61}[a-zA-Z0-9])(/[a-zA-Z0-9._-]+)*/?$`
- **Min Length**: 0
- **Max Length**: 1024

### Arn
- **Type**: string
- **Pattern**: `^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$`
- **Min Length**: 1
- **Max Length**: 128

### ClientToken
- **Type**: string
- **Pattern**: `^[\x21-\x7E]+$`
- **Min Length**: 32
- **Max Length**: 128

### Description
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*$`
- **Min Length**: 1
- **Max Length**: 80

### EnvironmentVariablesKeyString
- **Type**: string
- **Pattern**: `^[_a-zA-Z][_a-zA-Z0-9]*$`
- **Min Length**: 1
- **Max Length**: 256

### Id
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 32

### Identifier
- **Type**: string
- **Pattern**: `^(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)$`
- **Min Length**: 1
- **Max Length**: 128

### LocationName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 20

### OutputUri
- **Type**: string
- **Pattern**: `^s3://.*(/|\.zip|\.ZIP)$`
- **Min Length**: 0
- **Max Length**: 1024

### UserId
- **Type**: string
- **Pattern**: `^[-_a-zA-Z0-9/=+]*$`
- **Min Length**: 0
- **Max Length**: 1024


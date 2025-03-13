# Appintegrations Service

### ApplicationName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._ \-]+$`
- **Min Length**: 1
- **Max Length**: 255

### ApplicationNamespace
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._\-]+$`
- **Min Length**: 1
- **Max Length**: 32

### ApplicationTrustedSource
- **Type**: string
- **Pattern**: `^\w+\:\/\/.*$`
- **Min Length**: 1
- **Max Length**: 128

### Arn
- **Type**: string
- **Pattern**: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
- **Min Length**: 1
- **Max Length**: 2048

### ArnOrUUID
- **Type**: string
- **Pattern**: `^(arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})(:[\w\$]+)?$`
- **Min Length**: 1
- **Max Length**: 2048

### ClientId
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 255

### Description
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1000

### DestinationURI
- **Type**: string
- **Pattern**: `^(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+$)|(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+[\w/!@#+=.-]+[\w/!@#+=.,-]+$)`
- **Min Length**: 1
- **Max Length**: 1000

### EventBridgeBus
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._\-]+$`
- **Min Length**: 1
- **Max Length**: 255

### EventBridgeRuleName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._\-]+$`
- **Min Length**: 1
- **Max Length**: 2048

### EventDefinitionSchema
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 10240

### EventName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._\-]+::[a-zA-Z0-9\/\._\-]+(?:\*)?$`
- **Min Length**: 1
- **Max Length**: 255

### Fields
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._\-]+$`
- **Min Length**: 1
- **Max Length**: 255

### IdempotencyToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 2048

### Identifier
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 255

### Name
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._\-]+$`
- **Min Length**: 1
- **Max Length**: 255

### NextToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1000

### NonBlankLongString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 200

### NonBlankString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 255

### Object
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._\-]+$`
- **Min Length**: 1
- **Max Length**: 255

### Permission
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\._\-\*]+$`
- **Min Length**: 1
- **Max Length**: 255

### Source
- **Type**: string
- **Pattern**: `^aws\.partner\/.*$`
- **Min Length**: 1
- **Max Length**: 256

### SourceURI
- **Type**: string
- **Pattern**: `^(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+$)|(\w+\:\/\/[\w.-]+[\w/!@#+=.-]+[\w/!@#+=.-]+[\w/!@#+=.,-]+$)`
- **Min Length**: 1
- **Max Length**: 1000

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### URL
- **Type**: string
- **Pattern**: `^\w+\:\/\/.*$`
- **Min Length**: 1
- **Max Length**: 1000

### UUID
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`


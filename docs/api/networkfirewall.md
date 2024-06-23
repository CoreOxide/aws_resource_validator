# Networkfirewall Service

### ActionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 128

### AddressDefinition
- **Type**: string
- **Pattern**: `^([a-fA-F\d:\.]+($|/\d{1,3}))$`
- **Min Length**: 1
- **Max Length**: 255

### AzSubnet
- **Type**: string
- **Pattern**: `^subnet-[0-9a-f]+$`
- **Min Length**: 1
- **Max Length**: 128

### Description
- **Type**: string
- **Pattern**: `^.*$`
- **Max Length**: 512

### Destination
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 1024

### DimensionValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_ ]+$`
- **Min Length**: 1
- **Max Length**: 128

### HashMapKey
- **Type**: string
- **Pattern**: `^[0-9A-Za-z.\-_@\/]+$`
- **Min Length**: 3
- **Max Length**: 50

### HashMapValue
- **Type**: string
- **Pattern**: `[\s\S]*$`
- **Min Length**: 1
- **Max Length**: 1024

### IPSetReferenceName
- **Type**: string
- **Pattern**: `^[A-Za-z][A-Za-z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 32

### KeyId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2048

### Keyword
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 128

### LogDestinationType
- **Type**: string
- **Pattern**: `[0-9A-Za-z]+`
- **Min Length**: 2
- **Max Length**: 30

### PaginationToken
- **Type**: string
- **Pattern**: `[0-9A-Za-z:\/+=]+$`
- **Min Length**: 1
- **Max Length**: 4096

### PolicyString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 395000

### Port
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 1024

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:aws.*`
- **Min Length**: 1
- **Max Length**: 256

### ResourceId
- **Type**: string
- **Pattern**: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`
- **Min Length**: 36
- **Max Length**: 36

### ResourceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### RuleVariableName
- **Type**: string
- **Pattern**: `^[A-Za-z][A-Za-z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 32

### Setting
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 8192

### Source
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 1024

### StatusReason
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9- ]+$`
- **Min Length**: 1
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 256

### UpdateToken
- **Type**: string
- **Pattern**: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`
- **Min Length**: 1
- **Max Length**: 1024

### VariableDefinition
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1

### VpcId
- **Type**: string
- **Pattern**: `^vpc-[0-9a-f]+$`
- **Min Length**: 1
- **Max Length**: 128


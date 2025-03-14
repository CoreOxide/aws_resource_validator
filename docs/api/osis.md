# Osis Service

### BlueprintFormat
- **Type**: string
- **Pattern**: `(YAML|JSON)`

### CidrBlock
- **Type**: string
- **Pattern**: `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/(3[0-2]|[12]?[0-9])$`

### LogGroup
- **Type**: string
- **Pattern**: `\/aws\/vendedlogs\/[\.\-_/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### NextToken
- **Type**: string
- **Pattern**: `^([\s\S]*)$`
- **Min Length**: 0
- **Max Length**: 3000

### PipelineArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`
- **Min Length**: 46
- **Max Length**: 76

### PipelineName
- **Type**: string
- **Pattern**: `[a-z][a-z0-9\-]+`
- **Min Length**: 3
- **Max Length**: 28

### SecurityGroupId
- **Type**: string
- **Pattern**: `sg-\w{8}(\w{9})?`
- **Min Length**: 11
- **Max Length**: 20

### SubnetId
- **Type**: string
- **Pattern**: `subnet-\w{8}(\w{9})?`
- **Min Length**: 15
- **Max Length**: 24

### TagKey
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 256


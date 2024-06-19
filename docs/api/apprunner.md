# Apprunner Service

### AppRunnerResourceArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
- **Min Length**: 1
- **Max Length**: 1011

### AutoScalingConfigurationName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
- **Min Length**: 4
- **Max Length**: 32

### BuildCommand
- **Type**: string
- **Pattern**: `[^\x0a\x0d]+`

### ConnectionName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
- **Min Length**: 4
- **Max Length**: 32

### Cpu
- **Type**: string
- **Pattern**: `256|512|1024|2048|4096|(0.25|0.5|1|2|4) vCPU`
- **Min Length**: 3
- **Max Length**: 9

### CustomerAccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`
- **Min Length**: 12
- **Max Length**: 12

### DomainName
- **Type**: string
- **Pattern**: `[A-Za-z0-9*.-]{1,255}`
- **Min Length**: 1
- **Max Length**: 255

### ImageIdentifier
- **Type**: string
- **Pattern**: `([0-9]{12}.dkr.ecr.[a-z\-]+-[0-9]{1}.amazonaws.com\/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*\/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(:([\w\d+\-=._:\/@])+|@([\w\d\:]+))?)|(^public\.ecr\.aws\/.+\/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*\/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(:([\w\d+\-=._:\/@])+|@([\w\d\:]+))?)`
- **Min Length**: 1
- **Max Length**: 1024

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:kms:[a-z\-]+-[0-9]{1}:[0-9]{12}:key\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 0
- **Max Length**: 256

### Memory
- **Type**: string
- **Pattern**: `512|1024|2048|3072|4096|6144|8192|10240|12288|(0.5|1|2|3|4|6|8|10|12) GB`
- **Min Length**: 3
- **Max Length**: 6

### NextToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

### ObservabilityConfigurationName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
- **Min Length**: 4
- **Max Length**: 32

### RoleArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::[0-9]{12}:(role|role\/service-role)\/[\w+=,.@\-/]{1,1000}`
- **Min Length**: 29
- **Max Length**: 1024

### RuntimeEnvironmentVariablesKey
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 51200

### RuntimeEnvironmentVariablesValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 51200

### ServiceId
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
- **Min Length**: 32
- **Max Length**: 32

### ServiceName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9-_]{3,39}`
- **Min Length**: 4
- **Max Length**: 40

### SourceDirectory
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 1
- **Max Length**: 4096

### StartCommand
- **Type**: string
- **Pattern**: `[^\x0a\x0d]+`

### String
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 51200

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:).+`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 256

### UUID
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
- **Min Length**: 36
- **Max Length**: 36

### VpcConnectorName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9\-_]{3,39}`
- **Min Length**: 4
- **Max Length**: 40

### VpcIngressConnectionName
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9\-_]{3,39}`
- **Min Length**: 4
- **Max Length**: 40


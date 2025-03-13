# Emrserverless Service

### ApplicationArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+`
- **Min Length**: 60
- **Max Length**: 1024

### ApplicationId
- **Type**: string
- **Pattern**: `[0-9a-z]+`
- **Min Length**: 1
- **Max Length**: 64

### ApplicationName
- **Type**: string
- **Pattern**: `[A-Za-z0-9._/#-]+`
- **Min Length**: 1
- **Max Length**: 64

### ClientToken
- **Type**: string
- **Pattern**: `[A-Za-z0-9._-]+`
- **Min Length**: 1
- **Max Length**: 64

### ConfigurationPropertyKey
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### ConfigurationPropertyValue
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 1024

### CpuSize
- **Type**: string
- **Pattern**: `[1-9][0-9]*(\s)?(vCPU|vcpu|VCPU)?`
- **Min Length**: 1
- **Max Length**: 15

### DiskSize
- **Type**: string
- **Pattern**: `[1-9][0-9]*(\s)?(GB|gb|gB|Gb)`
- **Min Length**: 1
- **Max Length**: 15

### DiskType
- **Type**: string
- **Pattern**: `(SHUFFLE_OPTIMIZED|[Ss]huffle_[Oo]ptimized|STANDARD|[Ss]tandard)`

### EncryptionKeyArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):kms:[a-zA-Z0-9\-]*:([0-9]{12}):key\/[a-zA-Z0-9-]+`
- **Min Length**: 20
- **Max Length**: 2048

### EntryPointArgument
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 10280

### EntryPointPath
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 4096

### HiveCliParameters
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 102400

### IAMRoleArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
- **Min Length**: 20
- **Max Length**: 2048

### ImageDigest
- **Type**: string
- **Pattern**: `sha256:[0-9a-f]{64}`

### ImageUri
- **Type**: string
- **Pattern**: `([0-9]{12})\.dkr\.ecr\.([a-z0-9-]+).([a-z0-9._-]+)\/((?:[a-z0-9]+(?:[-._][a-z0-9]+)*/)*[a-z0-9]+(?:[-._][a-z0-9]+)*)(?::([a-zA-Z0-9_]+[a-zA-Z0-9-._]*)|@(sha256:[0-9a-f]{64}))`
- **Min Length**: 1
- **Max Length**: 1024

### InitScriptPath
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### JobArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+\/jobruns\/[0-9a-zA-Z]+`
- **Min Length**: 60
- **Max Length**: 1024

### JobRunId
- **Type**: string
- **Pattern**: `[0-9a-z]+`
- **Min Length**: 1
- **Max Length**: 64

### LogGroupName
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### LogStreamNamePrefix
- **Type**: string
- **Pattern**: `[^:*]*`
- **Min Length**: 1
- **Max Length**: 512

### LogTypeString
- **Type**: string
- **Pattern**: `[a-zA-Z]+[-_]*[a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 50

### MemorySize
- **Type**: string
- **Pattern**: `[1-9][0-9]*(\s)?(GB|gb|gB|Gb)?`
- **Min Length**: 1
- **Max Length**: 15

### NextToken
- **Type**: string
- **Pattern**: `[A-Za-z0-9_=-]+`
- **Min Length**: 1
- **Max Length**: 1024

### PrometheusUrlString
- **Type**: string
- **Pattern**: `https://aps-workspaces.([a-z]{2}-[a-z-]{1,20}-[1-9]).amazonaws(.[0-9A-Za-z]{2,4})+/workspaces/[-_.0-9A-Za-z]{1,100}/api/v1/remote_write`
- **Min Length**: 1
- **Max Length**: 10280

### Query
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 10280

### ReleaseLabel
- **Type**: string
- **Pattern**: `[A-Za-z0-9._/-]+`
- **Min Length**: 1
- **Max Length**: 64

### RequestIdentityUserArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+`
- **Min Length**: 20
- **Max Length**: 2048

### ResourceArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+(\/jobruns\/[0-9a-zA-Z]+)?`
- **Min Length**: 60
- **Max Length**: 1024

### SecurityGroupString
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+.*`
- **Min Length**: 1
- **Max Length**: 32

### SparkSubmitParameters
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 102400

### String1024
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### String256
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### SubnetString
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+.*`
- **Min Length**: 1
- **Max Length**: 32

### TagKey
- **Type**: string
- **Pattern**: `[A-Za-z0-9 /_.:=+@-]+`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[A-Za-z0-9 /_.:=+@-]*`
- **Min Length**: 0
- **Max Length**: 256

### UriString
- **Type**: string
- **Pattern**: `.*[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*.*`
- **Min Length**: 1
- **Max Length**: 10280

### WorkerTypeString
- **Type**: string
- **Pattern**: `[a-zA-Z]+[-_]*[a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 50


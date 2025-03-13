# Pipes Service

### Arn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`
- **Min Length**: 1
- **Max Length**: 1600

### ArnOrJsonPath
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 1
- **Max Length**: 1600

### ArnOrUrl
- **Type**: string
- **Pattern**: `smk://(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]):[0-9]{1,5}|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`
- **Min Length**: 1
- **Max Length**: 1600

### CloudwatchLogGroupArn
- **Type**: string
- **Pattern**: `(^arn:aws([a-z]|\-)*:logs:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):log-group:[\.\-_/#A-Za-z0-9]{1,512}(:\*)?)`
- **Min Length**: 1
- **Max Length**: 1600

### EndpointString
- **Type**: string
- **Pattern**: `(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]):[0-9]{1,5}`
- **Min Length**: 1
- **Max Length**: 300

### EventBridgeEndpointId
- **Type**: string
- **Pattern**: `[A-Za-z0-9\-]+[\.][A-Za-z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 50

### EventBridgeEventSource
- **Type**: string
- **Pattern**: `.*(?=[/\.\-_A-Za-z0-9]+)((?!aws\.).*)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*).*`
- **Min Length**: 1
- **Max Length**: 256

### FirehoseArn
- **Type**: string
- **Pattern**: `(^arn:aws([a-z]|\-)*:firehose:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):deliverystream/[a-zA-Z0-9_.-]{1,64})`
- **Min Length**: 1
- **Max Length**: 1600

### HeaderKey
- **Type**: string
- **Pattern**: `[!#$%&\'*+-.^_`|~0-9a-zA-Z]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 0
- **Max Length**: 512

### HeaderValue
- **Type**: string
- **Pattern**: `[ \t]*[\x20-\x7E]+([ \t]+[\x20-\x7E]+)*[ \t]*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 0
- **Max Length**: 512

### JsonPath
- **Type**: string
- **Pattern**: `\$(\.[\w/_-]+(\[(\d+|\*)\])*)*`
- **Min Length**: 1
- **Max Length**: 256

### KafkaTopicName
- **Type**: string
- **Pattern**: `[^.]([a-zA-Z0-9\-_.]+)`
- **Min Length**: 1
- **Max Length**: 249

### KmsKeyIdentifier
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-/:]*`
- **Min Length**: 0
- **Max Length**: 2048

### MQBrokerQueueName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 1000

### OptionalArn
- **Type**: string
- **Pattern**: `$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`
- **Min Length**: 0
- **Max Length**: 1600

### PathParameter
- **Type**: string
- **Pattern**: `(?!\s*$).+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

### PipeArn
- **Type**: string
- **Pattern**: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)`
- **Min Length**: 1
- **Max Length**: 1600

### PipeDescription
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 512

### PipeName
- **Type**: string
- **Pattern**: `[\.\-_A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 64

### PipeStateReason
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 512

### QueryStringKey
- **Type**: string
- **Pattern**: `[^\x00-\x1F\x7F]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 0
- **Max Length**: 512

### QueryStringValue
- **Type**: string
- **Pattern**: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 0
- **Max Length**: 512

### RoleArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z0-9+=,.@\-_/]+`
- **Min Length**: 1
- **Max Length**: 1600

### S3LogDestinationParametersBucketOwnerString
- **Type**: string
- **Pattern**: `\d{12}`

### SageMakerPipelineParameterName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9](-*[a-zA-Z0-9])*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 1
- **Max Length**: 256

### SecretManagerArn
- **Type**: string
- **Pattern**: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`
- **Min Length**: 1
- **Max Length**: 1600

### SecretManagerArnOrJsonPath
- **Type**: string
- **Pattern**: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 1
- **Max Length**: 1600

### SecurityGroup
- **Type**: string
- **Pattern**: `sg-[0-9a-zA-Z]*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 1
- **Max Length**: 1024

### SecurityGroupId
- **Type**: string
- **Pattern**: `sg-[0-9a-zA-Z]*`
- **Min Length**: 1
- **Max Length**: 1024

### Subnet
- **Type**: string
- **Pattern**: `subnet-[0-9a-z]*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`
- **Min Length**: 1
- **Max Length**: 1024

### SubnetId
- **Type**: string
- **Pattern**: `subnet-[0-9a-z]*`
- **Min Length**: 1
- **Max Length**: 1024

### URI
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-\/*:_+=.@-]*`
- **Min Length**: 1
- **Max Length**: 200


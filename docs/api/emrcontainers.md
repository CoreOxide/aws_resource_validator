# Emrcontainers Service

### ACMCertArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):acm:.+:(\d{12}):certificate/.+$`
- **Min Length**: 44
- **Max Length**: 2048

### Base64Encoded
- **Type**: string
- **Pattern**: `^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$`
- **Max Length**: 5000

### ClientToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 64

### ClusterId
- **Type**: string
- **Pattern**: `^[0-9A-Za-z][A-Za-z0-9\-_]*`
- **Min Length**: 1
- **Max Length**: 100

### CredentialType
- **Type**: string
- **Pattern**: `^.*\S.*$`
- **Min Length**: 1
- **Max Length**: 64

### EndpointArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/virtualclusters\/[0-9a-zA-Z]+\/endpoints\/[0-9a-zA-Z]+$`
- **Min Length**: 60
- **Max Length**: 1024

### EndpointType
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 64

### EntryPointArgument
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 10280

### EntryPointPath
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### IAMRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
- **Min Length**: 20
- **Max Length**: 2048

### JobArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/virtualclusters\/[0-9a-zA-Z]+\/jobruns\/[0-9a-zA-Z]+$`
- **Min Length**: 60
- **Max Length**: 1024

### JobTemplateArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/jobtemplates\/[0-9a-zA-Z]+$`
- **Min Length**: 60
- **Max Length**: 1024

### KmsKeyArn
- **Type**: string
- **Pattern**: `^(arn:(aws[a-zA-Z0-9-]*):kms:.+:(\d{12})?:key\/[(0-9a-zA-Z)-?]+|\$\{[a-zA-Z]\w*\})$`
- **Min Length**: 3
- **Max Length**: 2048

### KubernetesNamespace
- **Type**: string
- **Pattern**: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`
- **Min Length**: 1
- **Max Length**: 63

### LogContext
- **Type**: string
- **Pattern**: `^((?!.*-s3alias)(?!xn--.*)[a-z0-9][-a-z0-9.]*)?[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### LogGroupName
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### NextToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### ParametricIAMRoleArn
- **Type**: string
- **Pattern**: `(^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$)|([\.\-_\#A-Za-z0-9\$\{\}]+)`
- **Min Length**: 4
- **Max Length**: 2048

### ParametricReleaseLabel
- **Type**: string
- **Pattern**: `([\.\-_/A-Za-z0-9]+|\$\{[a-zA-Z]\w*\})`
- **Min Length**: 1
- **Max Length**: 64

### ReleaseLabel
- **Type**: string
- **Pattern**: `[\.\-_/A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 64

### RequestIdentityUserArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+$`
- **Min Length**: 20
- **Max Length**: 2048

### ResourceIdString
- **Type**: string
- **Pattern**: `[0-9a-z]+`
- **Min Length**: 1
- **Max Length**: 64

### ResourceNameString
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 64

### RotationSize
- **Type**: string
- **Pattern**: `^\d+(\.\d+)?[KMG][Bb]?$`
- **Min Length**: 3
- **Max Length**: 12

### RsiArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):/virtualclusters/.+$`
- **Min Length**: 60
- **Max Length**: 500

### SecretsManagerArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):secretsmanager:.+:(\d{12}):secret:[0-9a-zA-Z/_+=.@-]+$`
- **Min Length**: 3
- **Max Length**: 2048

### SecurityConfigurationArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/securityconfigurations\/[0-9a-zA-Z]+$`
- **Min Length**: 60
- **Max Length**: 1024

### SessionTagValue
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9 ]+`
- **Min Length**: 1
- **Max Length**: 512

### SparkSqlParameters
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 102400

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

### String128
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### String2048
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2048

### String256
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 256

### StringEmpty256
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 256

### TemplateParameter
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9\$\{\}]+`
- **Min Length**: 1
- **Max Length**: 512

### TemplateParameterName
- **Type**: string
- **Pattern**: `[\.\-_\#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### Token
- **Type**: string
- **Pattern**: `^.*\S.*$`
- **Min Length**: 1

### UriString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 10280

### VirtualClusterArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/virtualclusters\/[0-9a-zA-Z]+$`
- **Min Length**: 60
- **Max Length**: 1024


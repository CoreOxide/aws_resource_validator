# Codeconnections Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`
- **Min Length**: 12
- **Max Length**: 12

### AmazonResourceName
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
- **Min Length**: 1
- **Max Length**: 1011

### BranchName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 255

### ConnectionArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
- **Min Length**: 0
- **Max Length**: 256

### ConnectionName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 32

### HostArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
- **Min Length**: 0
- **Max Length**: 256

### HostName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 64

### HostStatus
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 64

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
- **Min Length**: 1
- **Max Length**: 1024

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:kms:[a-z\-0-9]+:\d{12}:key/[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 1024

### NextToken
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 1024

### OwnerId
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 255

### RepositoryLinkArn
- **Type**: string
- **Pattern**: `^arn:aws(?:-[a-z]+)*:(codestar-connections|codeconnections):[a-z\-0-9]+:\d{12}:repository-link\/[a-zA-Z0-9\-:/]+`

### RepositoryLinkId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`

### RepositoryName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 128

### ResourceName
- **Type**: string
- **Pattern**: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
- **Min Length**: 1
- **Max Length**: 100

### SecurityGroupId
- **Type**: string
- **Pattern**: `sg-\w{8}(\w{9})?`
- **Min Length**: 11
- **Max Length**: 20

### SharpNextToken
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 2048

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

### TlsCertificate
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 16384

### Url
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 512

### VpcId
- **Type**: string
- **Pattern**: `vpc-\w{8}(\w{9})?`
- **Min Length**: 12
- **Max Length**: 21


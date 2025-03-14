# Amplify Service

### AccessToken
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 255

### AppId
- **Type**: string
- **Pattern**: `d[a-z0-9]+`
- **Min Length**: 1
- **Max Length**: 20

### ArtifactId
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255

### AutoBranchCreationPattern
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 2048

### AutoSubDomainCreationPattern
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 2048

### AutoSubDomainIAMRole
- **Type**: string
- **Pattern**: `^$|^arn:aws:iam::\d{12}:role.+`
- **Max Length**: 1000

### BackendEnvironmentArn
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 0
- **Max Length**: 1000

### BasicAuthCredentials
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 2000

### BranchArn
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 1000

### BranchName
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 255

### BuildSpec
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 25000

### CertificateArn
- **Type**: string
- **Pattern**: `^arn:aws:acm:[a-z0-9-]+:\d{12}:certificate\/.+$`
- **Min Length**: 0
- **Max Length**: 1000

### CommitId
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255

### CommitMessage
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 10000

### ComputeRoleArn
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 0
- **Max Length**: 1000

### Condition
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 0
- **Max Length**: 2048

### CustomHeaders
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 0
- **Max Length**: 25000

### DeploymentArtifacts
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 1000

### Description
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 1000

### DisplayName
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255

### DomainName
- **Type**: string
- **Pattern**: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(\.)?$`
- **Max Length**: 64

### DomainPrefix
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255

### EnvKey
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255

### EnvValue
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 5500

### EnvironmentName
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 255

### FileName
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255

### Framework
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255

### JobId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Max Length**: 255

### JobReason
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255

### MD5Hash
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 32

### Name
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 255

### NextToken
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 2000

### OauthToken
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 1000

### PullRequestEnvironmentName
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 20

### Repository
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 1000

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:aws:amplify:.*`
- **Min Length**: 0
- **Max Length**: 2048

### ServiceRoleArn
- **Type**: string
- **Pattern**: `(?s).*`
- **Min Length**: 0
- **Max Length**: 1000

### Source
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 2048

### SourceUrl
- **Type**: string
- **Pattern**: `^(s3|https|http)://.*`
- **Max Length**: 3000

### StackArn
- **Type**: string
- **Pattern**: `^arn:aws:cloudformation:[a-z0-9-]+:\d{12}:stack/.+/.+$`
- **Min Length**: 20
- **Max Length**: 2048

### StackName
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 255

### Status
- **Type**: string
- **Pattern**: `.{3,7}`
- **Min Length**: 3
- **Max Length**: 7

### TTL
- **Type**: string
- **Pattern**: `\d*`
- **Min Length**: 0
- **Max Length**: 32

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Max Length**: 256

### Target
- **Type**: string
- **Pattern**: `(?s).+`
- **Min Length**: 1
- **Max Length**: 2048

### WebAclArn
- **Type**: string
- **Pattern**: `^arn:aws:wafv2:.*`
- **Min Length**: 0
- **Max Length**: 512

### WebhookId
- **Type**: string
- **Pattern**: `(?s).*`
- **Max Length**: 255


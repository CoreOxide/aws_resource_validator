# Codestar Service

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[\w:/-]+$`
- **Min Length**: 1
- **Max Length**: 256

### Email
- **Type**: string
- **Pattern**: `^[\w-.+]+@[\w-.+]+$`
- **Min Length**: 3
- **Max Length**: 128

### PaginationToken
- **Type**: string
- **Pattern**: `^[\w/+=]+$`
- **Min Length**: 1
- **Max Length**: 512

### ProjectArn
- **Type**: string
- **Pattern**: `^arn:aws[^:\s]*:codestar:[^:\s]+:[0-9]{12}:project\/[a-z]([a-z0-9|-])+$`

### ProjectDescription
- **Type**: string
- **Pattern**: `^$|^\S(.*\S)?$`
- **Max Length**: 1024

### ProjectId
- **Type**: string
- **Pattern**: `^[a-z][a-z0-9-]+$`
- **Min Length**: 2
- **Max Length**: 15

### ProjectName
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 100

### ProjectTemplateId
- **Type**: string
- **Pattern**: `^arn:aws[^:\s]{0,5}:codestar:[^:\s]+::project-template(\/(github|codecommit))?\/[a-z0-9-]+$`
- **Min Length**: 1

### Reason
- **Type**: string
- **Pattern**: `^$|^\S(.*\S)?$`
- **Max Length**: 1024

### RepositoryDescription
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 1000

### RepositoryName
- **Type**: string
- **Pattern**: `^\S[\w.-]*$`
- **Min Length**: 1
- **Max Length**: 100

### RepositoryOwner
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 100

### RepositoryType
- **Type**: string
- **Pattern**: `^(user|organization|User|Organization)$`

### ResourceId
- **Type**: string
- **Pattern**: `^arn\:aws\:\S.*\:.*`
- **Min Length**: 11

### Role
- **Type**: string
- **Pattern**: `^(Owner|Viewer|Contributor)$`

### SshPublicKey
- **Type**: string
- **Pattern**: `^[\t\r\n\u0020-\u00FF]*$`
- **Max Length**: 16384

### StackId
- **Type**: string
- **Pattern**: `^arn:aws[^:\s]*:cloudformation:[^:\s]+:[0-9]{12}:stack\/[^:\s]+\/[^:\s]+$`

### State
- **Type**: string
- **Pattern**: `^(CreateInProgress|CreateComplete|CreateFailed|DeleteComplete|DeleteFailed|DeleteInProgress|UpdateComplete|UpdateInProgress|UpdateFailed|Unknown)$`

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Max Length**: 256

### TemplateParameterKey
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 30

### TemplateParameterValue
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 100

### UserArn
- **Type**: string
- **Pattern**: `^arn:aws:iam::\d{12}:user(?:(\u002F)|(\u002F[\u0021-\u007E]+\u002F))[\w+=,.@-]+$`
- **Min Length**: 32
- **Max Length**: 95

### UserProfileDisplayName
- **Type**: string
- **Pattern**: `^\S(.*\S)?$`
- **Min Length**: 1
- **Max Length**: 64


# Cloudformation Service

### Account
- **Type**: string
- **Pattern**: `^[0-9]{12}$`

### AccountsUrl
- **Type**: string
- **Pattern**: `(s3://|http(s?)://).+`
- **Min Length**: 1
- **Max Length**: 5120

### ChangeSetId
- **Type**: string
- **Pattern**: `arn:[-a-zA-Z0-9:/]*`
- **Min Length**: 1

### ChangeSetName
- **Type**: string
- **Pattern**: `[a-zA-Z][-a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### ChangeSetNameOrId
- **Type**: string
- **Pattern**: `[a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/]*`
- **Min Length**: 1
- **Max Length**: 1600

### ClientRequestToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][-a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### ConfigurationSchema
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 60000

### ConnectionArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
- **Min Length**: 1
- **Max Length**: 256

### ExecutionRoleName
- **Type**: string
- **Pattern**: `[a-zA-Z_0-9+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 64

### HookResultId
- **Type**: string
- **Pattern**: `[a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/]*|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 1600

### HookTargetTypeName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}$`
- **Min Length**: 1
- **Max Length**: 256

### HookTypeConfigurationVersionId
- **Type**: string
- **Pattern**: `[A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### HookTypeVersionId
- **Type**: string
- **Pattern**: `[A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### LogGroupName
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### OperationResultFilterValues
- **Type**: string
- **Pattern**: `^\S{6,9}$`
- **Min Length**: 6
- **Max Length**: 9

### OrganizationalUnitId
- **Type**: string
- **Pattern**: `^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$`

### PrivateTypeArn
- **Type**: string
- **Pattern**: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:[0-9]{12}:type/.+`
- **Max Length**: 1024

### PublicVersionNumber
- **Type**: string
- **Pattern**: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(.*)$`
- **Min Length**: 5

### PublisherId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z]{12,40}`
- **Min Length**: 1
- **Max Length**: 40

### PublisherName
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 100

### PublisherProfile
- **Type**: string
- **Pattern**: `(http:|https:)+[^\s]+[\w]`
- **Max Length**: 1024

### Region
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]{1,128}$`

### RegistrationToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][-a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### RequestToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][-a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### ResourceToSkip
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+|[a-zA-Z][-a-zA-Z0-9]*\.[a-zA-Z0-9]+`

### RoleArn
- **Type**: string
- **Pattern**: `arn:.+:iam::[0-9]{12}:role/.+`
- **Min Length**: 1
- **Max Length**: 256

### S3Bucket
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 3
- **Max Length**: 63

### StackIdsUrl
- **Type**: string
- **Pattern**: `(s3://|http(s?)://).+`
- **Min Length**: 1
- **Max Length**: 5120

### StackInstanceFilterValues
- **Type**: string
- **Pattern**: `^\S{1,128}$`
- **Min Length**: 1
- **Max Length**: 128

### StackNameOrId
- **Type**: string
- **Pattern**: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`
- **Min Length**: 1

### StackSetNameOrId
- **Type**: string
- **Pattern**: `[a-zA-Z][-a-zA-Z0-9]*(?::[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12})?`

### ThirdPartyTypeArn
- **Type**: string
- **Pattern**: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}::type/.+/[0-9a-zA-Z]{12,40}/.+`
- **Max Length**: 1024

### TypeArn
- **Type**: string
- **Pattern**: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`
- **Max Length**: 1024

### TypeConfiguration
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 204800

### TypeConfigurationAlias
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{1,256}$`
- **Min Length**: 1
- **Max Length**: 256

### TypeConfigurationArn
- **Type**: string
- **Pattern**: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type-configuration/.+`
- **Max Length**: 1024

### TypeName
- **Type**: string
- **Pattern**: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`
- **Min Length**: 10
- **Max Length**: 204

### TypeNamePrefix
- **Type**: string
- **Pattern**: `([A-Za-z0-9]{2,64}::){0,2}([A-Za-z0-9]{2,64}:?){0,1}`
- **Min Length**: 1
- **Max Length**: 204

### TypeTestsStatusDescription
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 1024

### TypeVersionId
- **Type**: string
- **Pattern**: `[A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128


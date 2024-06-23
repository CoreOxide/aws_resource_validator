# Codepipeline Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### ActionConfigurationQueryableValue
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 50

### ActionName
- **Type**: string
- **Pattern**: `[A-Za-z0-9.@\-_]+`
- **Min Length**: 1
- **Max Length**: 100

### ActionNamespace
- **Type**: string
- **Pattern**: `[A-Za-z0-9@\-_]+`
- **Min Length**: 1
- **Max Length**: 100

### ActionProvider
- **Type**: string
- **Pattern**: `[0-9A-Za-z_-]+`
- **Min Length**: 1
- **Max Length**: 35

### ActionTypeOwner
- **Type**: string
- **Pattern**: `AWS|ThirdParty`

### AllowedAccount
- **Type**: string
- **Pattern**: `[0-9]{12}|\*`

### ApprovalToken
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

### ArtifactName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-]+`
- **Min Length**: 1
- **Max Length**: 100

### ArtifactStoreLocation
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-\.]+`
- **Min Length**: 3
- **Max Length**: 63

### ClientId
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### DisabledReason
- **Type**: string
- **Pattern**: `[a-zA-Z0-9!@ \(\)\.\*\?\-]+`
- **Min Length**: 1
- **Max Length**: 300

### GitBranchNamePattern
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 255

### GitFilePathPattern
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 255

### JobId
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

### LambdaFunctionArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:lambda:.+:[0-9]{12}:function:.+`
- **Min Length**: 1
- **Max Length**: 140

### OutputVariablesKey
- **Type**: string
- **Pattern**: `[A-Za-z0-9@\-_]+`

### PipelineArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:codepipeline:.+:[0-9]{12}:.+`

### PipelineExecutionId
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

### PipelineName
- **Type**: string
- **Pattern**: `[A-Za-z0-9.@\-_]+`
- **Min Length**: 1
- **Max Length**: 100

### PipelineVariableDescription
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 200

### PipelineVariableName
- **Type**: string
- **Pattern**: `[A-Za-z0-9@\-_]+`
- **Min Length**: 1
- **Max Length**: 128

### PipelineVariableValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1000

### ResourceArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:codepipeline:.+:[0-9]{12}:.+`

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`
- **Max Length**: 1024

### StageName
- **Type**: string
- **Pattern**: `[A-Za-z0-9.@\-_]+`
- **Min Length**: 1
- **Max Length**: 100

### Version
- **Type**: string
- **Pattern**: `[0-9A-Za-z_-]+`
- **Min Length**: 1
- **Max Length**: 9

### WebhookName
- **Type**: string
- **Pattern**: `[A-Za-z0-9.@\-_]+`
- **Min Length**: 1
- **Max Length**: 100


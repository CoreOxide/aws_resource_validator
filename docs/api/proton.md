# Proton Service

### Arn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 200

### AwsAccountId
- **Type**: string
- **Pattern**: `^\d{12}$`

### ClientToken
- **Type**: string
- **Pattern**: `^[!-~]*$`
- **Min Length**: 0
- **Max Length**: 64

### DeploymentId
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### EnvironmentAccountConnectionId
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### FullTemplateVersionNumber
- **Type**: string
- **Pattern**: `^(0|([1-9]{1}\d*)).(0|([1-9]{1}\d*))$`
- **Min Length**: 1
- **Max Length**: 10

### NextToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+=/]+$`

### RepositoryName
- **Type**: string
- **Pattern**: `[A-Za-z0-9_.-].*/[A-Za-z0-9_.-].*`
- **Min Length**: 1
- **Max Length**: 100

### ResourceName
- **Type**: string
- **Pattern**: `^[0-9A-Za-z]+[0-9A-Za-z_\-]*$`
- **Min Length**: 1
- **Max Length**: 100

### ResourceNameOrEmpty
- **Type**: string
- **Pattern**: `(^$)|^[0-9A-Za-z]+[0-9A-Za-z_\-]*$`
- **Min Length**: 0
- **Max Length**: 100

### RoleArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})$`
- **Min Length**: 1
- **Max Length**: 2048

### RoleArnOrEmptyString
- **Type**: string
- **Pattern**: `(^$)|(^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})$)`
- **Min Length**: 0
- **Max Length**: 2048

### S3Bucket
- **Type**: string
- **Pattern**: `^[a-z0-9]+[a-z0-9-\.]+[a-z0-9]+$`
- **Min Length**: 3
- **Max Length**: 63

### TemplateVersionPart
- **Type**: string
- **Pattern**: `^(0|([1-9]{1}\d*))$`
- **Min Length**: 1
- **Max Length**: 20


# Iottwinmaker Service

### BundleName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### ColumnName
- **Type**: string
- **Pattern**: `.*`

### ComponentPath
- **Type**: string
- **Pattern**: `[a-zA-Z_\-0-9/]+`
- **Min Length**: 1
- **Max Length**: 2048

### ComponentTypeId
- **Type**: string
- **Pattern**: `[a-zA-Z_\.\-0-9:]+`
- **Min Length**: 1
- **Max Length**: 256

### ComponentTypeName
- **Type**: string
- **Pattern**: `.*[^\u0000-\u001F\u007F]*.*`
- **Min Length**: 0
- **Max Length**: 256

### Description
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2048

### EntityId
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 128

### EntityName
- **Type**: string
- **Pattern**: `[^\u0000-\u001F\u007F]+`
- **Min Length**: 1
- **Max Length**: 256

### Expression
- **Type**: string
- **Pattern**: `(^\$\{Parameters\.[a-zA-z]+([a-zA-z_0-9]*)}$)`
- **Min Length**: 1
- **Max Length**: 316

### Id
- **Type**: string
- **Pattern**: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 128

### IdOrArn
- **Type**: string
- **Pattern**: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+$|^arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 2048

### LambdaArn
- **Type**: string
- **Pattern**: `arn:((aws)|(aws-cn)|(aws-us-gov)):lambda:[a-z0-9-]+:[0-9]{12}:function:[\/a-zA-Z0-9_-]+`
- **Min Length**: 20
- **Max Length**: 2048

### LinkedService
- **Type**: string
- **Pattern**: `[a-zA-Z_0-9]+`

### Name
- **Type**: string
- **Pattern**: `[a-zA-Z_\-0-9]+`
- **Min Length**: 1
- **Max Length**: 256

### NextToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 17880

### ParentEntityId
- **Type**: string
- **Pattern**: `\$ROOT|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 128

### PropertyDisplayName
- **Type**: string
- **Pattern**: `.*[^\u0000-\u001F\u007F]*.*`
- **Min Length**: 0
- **Max Length**: 256

### QueryStatement
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 1000

### RoleArn
- **Type**: string
- **Pattern**: `arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*`
- **Min Length**: 20
- **Max Length**: 2048

### S3DestinationLocation
- **Type**: string
- **Pattern**: `.*(^arn:((aws)|(aws-cn)|(aws-us-gov)):s3:::)([/a-zA-Z0-9_-]+$).*`

### S3Location
- **Type**: string
- **Pattern**: `.*(^arn:((aws)|(aws-cn)|(aws-us-gov)):s3:::)([a-zA-Z0-9_-]+$).*`
- **Min Length**: 0
- **Max Length**: 1024

### S3SourceLocation
- **Type**: string
- **Pattern**: `.*(^arn:((aws)|(aws-cn)|(aws-us-gov)):s3:::)([a-zA-Z0-9_-]+)\/([/.a-zA-Z0-9_-]+$).*`

### S3Url
- **Type**: string
- **Pattern**: `[sS]3://[A-Za-z0-9._/-]+`
- **Min Length**: 0
- **Max Length**: 256

### SceneCapability
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 256

### SceneMetadataValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2048

### SiteWiseExternalId
- **Type**: string
- **Pattern**: `.*[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+.*`
- **Min Length**: 2
- **Max Length**: 128

### String
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### SyncSource
- **Type**: string
- **Pattern**: `[a-zA-Z_0-9]+`

### TagKey
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### TwinMakerArn
- **Type**: string
- **Pattern**: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`
- **Min Length**: 20
- **Max Length**: 2048

### Uuid
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### Value
- **Type**: string
- **Pattern**: `.*`

### WorkspaceDeleteMessage
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2048


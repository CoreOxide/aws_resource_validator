# Neptunegraph Service

### Arn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 1011

### ExportFilterOutputDataType
- **Type**: string
- **Pattern**: `(Any|Byte|Short|Int|Long|Float|Double|String|Bool|Boolean|Float\[\]|Double\[\])`

### ExportFilterOutputPropertyName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_]+`
- **Min Length**: 1
- **Max Length**: 128

### ExportTaskId
- **Type**: string
- **Pattern**: `t-[a-z0-9]{10}`

### GraphId
- **Type**: string
- **Pattern**: `g-[a-z0-9]{10}`

### GraphIdentifier
- **Type**: string
- **Pattern**: `g-[a-z0-9]{10}`

### GraphName
- **Type**: string
- **Pattern**: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`
- **Min Length**: 1
- **Max Length**: 63

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
- **Min Length**: 1
- **Max Length**: 1024

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`

### SecurityGroupId
- **Type**: string
- **Pattern**: `sg-[a-z0-9]+`

### SnapshotId
- **Type**: string
- **Pattern**: `gs-[a-z0-9]{10}`

### SnapshotIdentifier
- **Type**: string
- **Pattern**: `gs-[a-z0-9]{10}`

### SnapshotName
- **Type**: string
- **Pattern**: `(?!gs-)[a-z][a-z0-9]*(-[a-z0-9]+)*`
- **Min Length**: 1
- **Max Length**: 63

### SubnetId
- **Type**: string
- **Pattern**: `subnet-[a-z0-9]+`

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:)[a-zA-Z+-=._:/]+`
- **Min Length**: 1
- **Max Length**: 128

### TaskId
- **Type**: string
- **Pattern**: `t-[a-z0-9]{10}`

### VpcEndpointId
- **Type**: string
- **Pattern**: `vpce-[0-9a-f]{17}`

### VpcId
- **Type**: string
- **Pattern**: `vpc-[a-z0-9]+`


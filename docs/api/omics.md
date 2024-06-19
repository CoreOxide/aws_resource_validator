# Omics Service

### ActivationJobId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 10
- **Max Length**: 36

### Arn
- **Type**: string
- **Pattern**: `arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*)`
- **Min Length**: 20
- **Max Length**: 2048

### ClientToken
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### CompleteReadSetUploadPartListItemChecksumString
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 100

### EngineLogStream
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

### ExportJobId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 10
- **Max Length**: 36

### GeneratedFrom
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### ImportJobId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 10
- **Max Length**: 36

### JobStatusMessage
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### Md5
- **Type**: string
- **Pattern**: `[\p{L}||\p{N}]+`
- **Min Length**: 1
- **Max Length**: 255

### NextToken
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 6144

### Range
- **Type**: string
- **Pattern**: `[\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### ReadSetArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 127

### ReadSetDescription
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 255

### ReadSetId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 10
- **Max Length**: 36

### ReadSetName
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### ReadSetStatusMessage
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 255

### ReferenceArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 127

### ReferenceArnFilter
- **Type**: string
- **Pattern**: `$|^arn:.+`
- **Min Length**: 0
- **Max Length**: 127

### ReferenceDescription
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 255

### ReferenceId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 10
- **Max Length**: 36

### ReferenceName
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 3
- **Max Length**: 255

### ReferenceStoreArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 127

### ReferenceStoreDescription
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 255

### ReferenceStoreId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 10
- **Max Length**: 36

### ReferenceStoreName
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### ResourceId
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

### RoleArn
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 20
- **Max Length**: 2048

### RunArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 128

### RunFailureReason
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 64

### RunGroupArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 128

### RunGroupId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 1
- **Max Length**: 18

### RunGroupListToken
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### RunGroupName
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### RunGroupRequestId
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### RunId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 1
- **Max Length**: 18

### RunListToken
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### RunLogStream
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

### RunName
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### RunOutputUri
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 750

### RunRequestId
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### RunResourceDigest
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 0
- **Max Length**: 64

### RunResourceDigestKey
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 256

### RunRoleArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 128

### RunStatusMessage
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

### RunUuid
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### S3AccessPointArn
- **Type**: string
- **Pattern**: `arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*`
- **Min Length**: 1
- **Max Length**: 1024

### S3Destination
- **Type**: string
- **Pattern**: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`

### S3Uri
- **Type**: string
- **Pattern**: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/(.{1,1024})`

### SampleId
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### SchemaItemKeyString
- **Type**: string
- **Pattern**: `[a-z0-9_]{1,255}`

### SequenceStoreArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 127

### SequenceStoreDescription
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 255

### SequenceStoreId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 10
- **Max Length**: 36

### SequenceStoreName
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### ShareName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 256

### SseConfigKeyArnString
- **Type**: string
- **Pattern**: `.*arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*).*`
- **Min Length**: 20
- **Max Length**: 2048

### StoreName
- **Type**: string
- **Pattern**: `([a-z]){1}([a-z0-9_]){2,254}`
- **Min Length**: 3
- **Max Length**: 255

### SubjectId
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 127

### TagArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 128

### TaskFailureReason
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 64

### TaskId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 1
- **Max Length**: 18

### TaskInstanceType
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

### TaskListToken
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### TaskLogStream
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

### TaskStatusMessage
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

### UploadId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 10
- **Max Length**: 36

### VersionName
- **Type**: string
- **Pattern**: `([a-z]){1}([a-z0-9_]){2,254}`
- **Min Length**: 3
- **Max Length**: 255

### WorkflowArn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 128

### WorkflowDefinition
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 256

### WorkflowDescription
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 256

### WorkflowId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 1
- **Max Length**: 18

### WorkflowListToken
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### WorkflowMain
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### WorkflowName
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### WorkflowOwnerId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### WorkflowParameterDescription
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 0
- **Max Length**: 256

### WorkflowParameterName
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### WorkflowRequestId
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
- **Min Length**: 1
- **Max Length**: 128

### WorkflowStatusMessage
- **Type**: string
- **Pattern**: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`


# Ssm Service

### AccountId
- **Type**: string
- **Pattern**: `(?i)all|[0-9]{12}`

### ActivationId
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### AlarmName
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 255

### AssociationExecutionId
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

### AssociationId
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

### AssociationName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{3,128}$`

### AssociationVersion
- **Type**: string
- **Pattern**: `([$]LATEST)|([1-9][0-9]*)`

### AttachmentIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{3,128}$`

### AttachmentName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{3,128}$`

### AutomationActionName
- **Type**: string
- **Pattern**: `^aws:[a-zA-Z]{3,25}$`

### BaselineId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-:/]{20,128}$`
- **Min Length**: 20
- **Max Length**: 128

### BaselineName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{3,128}$`
- **Min Length**: 3
- **Max Length**: 128

### ComplianceTypeName
- **Type**: string
- **Pattern**: `[A-Za-z0-9_\-]\w+|Custom:[a-zA-Z0-9_\-]\w+`
- **Min Length**: 1
- **Max Length**: 100

### DefaultInstanceName
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### DocumentARN
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.:/]{3,128}$`

### DocumentDisplayName
- **Type**: string
- **Pattern**: `^[\w\.\-\:\/ ]*$`
- **Max Length**: 1024

### DocumentName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{3,128}$`

### DocumentReviewComment
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 1024

### DocumentSchemaVersion
- **Type**: string
- **Pattern**: `([0-9]+)\.([0-9]+)`

### DocumentVersion
- **Type**: string
- **Pattern**: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`

### DocumentVersionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{1,128}$`

### DocumentVersionNumber
- **Type**: string
- **Pattern**: `(^[1-9][0-9]*$)`

### ExecutionRoleName
- **Type**: string
- **Pattern**: `[\w+=,.@/-]+`
- **Min Length**: 1
- **Max Length**: 64

### IdempotencyToken
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### InstallOverrideList
- **Type**: string
- **Pattern**: `^https://.+$|^s3://([^/]+)/(.*?([^/]+))$`
- **Min Length**: 1
- **Max Length**: 256

### InstanceId
- **Type**: string
- **Pattern**: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`

### InstancePropertyFilterValue
- **Type**: string
- **Pattern**: `^.{1,100000}$`
- **Min Length**: 1
- **Max Length**: 100000

### InstancePropertyStringFilterKey
- **Type**: string
- **Pattern**: `^.{1,100000}$`
- **Min Length**: 1
- **Max Length**: 100000

### InventoryItemCaptureTime
- **Type**: string
- **Pattern**: `^(20)[0-9][0-9]-(0[1-9]|1[012])-([12][0-9]|3[01]|0[1-9])(T)(2[0-3]|[0-1][0-9])(:[0-5][0-9])(:[0-5][0-9])(Z)$`

### InventoryItemSchemaVersion
- **Type**: string
- **Pattern**: `^([0-9]{1,6})(\.[0-9]{1,6})$`

### InventoryItemTypeName
- **Type**: string
- **Pattern**: `^(AWS|Custom):.*$`
- **Min Length**: 1
- **Max Length**: 100

### MaintenanceWindowExecutionId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### MaintenanceWindowExecutionTaskId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### MaintenanceWindowExecutionTaskInvocationId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### MaintenanceWindowId
- **Type**: string
- **Pattern**: `^mw-[0-9a-f]{17}$`
- **Min Length**: 20
- **Max Length**: 20

### MaintenanceWindowName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{3,128}$`
- **Min Length**: 3
- **Max Length**: 128

### MaintenanceWindowTargetId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### MaintenanceWindowTaskId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### ManagedInstanceId
- **Type**: string
- **Pattern**: `(^mi-[0-9a-f]{17}$)|(^eks_c:[0-9A-Za-z][A-Za-z0-9\-_]{0,99}_\w{17}$)`
- **Min Length**: 20
- **Max Length**: 124

### MaxConcurrency
- **Type**: string
- **Pattern**: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
- **Min Length**: 1
- **Max Length**: 7

### MaxErrors
- **Type**: string
- **Pattern**: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
- **Min Length**: 1
- **Max Length**: 7

### MaxSessionDuration
- **Type**: string
- **Pattern**: `^([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|1[0-4][0-3][0-9]|1440)$`
- **Min Length**: 1
- **Max Length**: 4

### MetadataKey
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 256

### OpsAggregatorType
- **Type**: string
- **Pattern**: `^(range|count|sum)`
- **Min Length**: 1
- **Max Length**: 20

### OpsDataTypeName
- **Type**: string
- **Pattern**: `^(AWS|Custom):.*$`
- **Min Length**: 1
- **Max Length**: 100

### OpsEntityItemCaptureTime
- **Type**: string
- **Pattern**: `^(20)[0-9][0-9]-(0[1-9]|1[012])-([12][0-9]|3[01]|0[1-9])(T)(2[0-3]|[0-1][0-9])(:[0-5][0-9])(:[0-5][0-9])(Z)$`

### OpsItemAccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`

### OpsItemArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[0-9]{12}:opsitem.*`
- **Min Length**: 20
- **Max Length**: 2048

### OpsItemCategory
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 64

### OpsItemDataKey
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 128

### OpsItemDataValueString
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`

### OpsItemDescription
- **Type**: string
- **Pattern**: `[\s\S]*\S[\s\S]*`
- **Min Length**: 1
- **Max Length**: 2048

### OpsItemEventFilterValue
- **Type**: string
- **Pattern**: `^(oi)-[0-9a-f]{12}$`
- **Min Length**: 1
- **Max Length**: 15

### OpsItemId
- **Type**: string
- **Pattern**: `^(oi)-[0-9a-f]{12}$`

### OpsItemSeverity
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 64

### OpsItemSource
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 128

### OpsItemTitle
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 1024

### OpsMetadataArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:opsmetadata\/([a-zA-Z0-9-_\.\/]*)`
- **Min Length**: 1
- **Max Length**: 1011

### OpsMetadataFilterKey
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 128

### OpsMetadataResourceId
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 1024

### ParameterKeyId
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9:/_-]+)$`
- **Min Length**: 1
- **Max Length**: 256

### ParameterStringFilterKey
- **Type**: string
- **Pattern**: `tag:.+|Name|Type|KeyId|Path|Label|Tier|DataType`
- **Min Length**: 1
- **Max Length**: 132

### PatchGroup
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 256

### PatchSourceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{3,50}$`

### Policy
- **Type**: string
- **Pattern**: `^(?!\s*$).+`

### RegistrationMetadataKey
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 128

### RegistrationMetadataValue
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 2048

### RequireType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{1,128}$`
- **Max Length**: 128

### ResourceDataSyncAWSKMSKeyARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 512

### ResourceDataSyncOrganizationalUnitId
- **Type**: string
- **Pattern**: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
- **Min Length**: 1
- **Max Length**: 128

### Reviewer
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]{1,128}$`
- **Max Length**: 50

### SessionReason
- **Type**: string
- **Pattern**: `^.{1,256}$`
- **Min Length**: 1
- **Max Length**: 256

### SharedDocumentVersion
- **Type**: string
- **Pattern**: `([$]LATEST|[$]DEFAULT|[$]ALL)`
- **Max Length**: 8

### SnapshotId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### SourceId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:_-]*$`
- **Min Length**: 0
- **Max Length**: 128

### StringDateTime
- **Type**: string
- **Pattern**: `^([\-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d(?!:))?)?(\17[0-5]\d([\.,]\d)?)?([zZ]|([\-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### TargetKey
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.:/=\-@]*$|resource-groups:ResourceTypeFilters|resource-groups:Name`
- **Min Length**: 1
- **Max Length**: 163

### TargetType
- **Type**: string
- **Pattern**: `^\/[\w\.\-\:\/]*$`
- **Max Length**: 200

### UUID
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

### Version
- **Type**: string
- **Pattern**: `^[0-9]{1,6}(\.[0-9]{1,6}){2,3}$`


# Servicecatalog Service

### AccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`

### CodeStarConnectionArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9][-.a-z0-9]{0,62}:codestar-connections:([a-z0-9][-.a-z0-9]{0,62})?:([a-z0-9][-.a-z0-9]{0,62})?:[^/].{0,1023}$`
- **Min Length**: 1
- **Max Length**: 1224

### EngineWorkflowFailureReason
- **Type**: string
- **Pattern**: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
- **Min Length**: 1
- **Max Length**: 2048

### EngineWorkflowToken
- **Type**: string
- **Pattern**: `[0-9A-Za-z+\/=]+`
- **Min Length**: 1
- **Max Length**: 20000

### Id
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-]*`
- **Min Length**: 1
- **Max Length**: 100

### IdempotencyToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 128

### NotificationArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 1
- **Max Length**: 1224

### OrganizationNodeValue
- **Type**: string
- **Pattern**: `(^[0-9]{12}$)|(^arn:aws:organizations::\d{12}:organization\/o-[a-z0-9]{10,32})|(^o-[a-z0-9]{10,32}$)|(^arn:aws:organizations::\d{12}:ou\/o-[a-z0-9]{10,32}\/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}$)|(^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)`

### PageToken
- **Type**: string
- **Pattern**: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
- **Max Length**: 2024

### ProductArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 1
- **Max Length**: 1224

### ProvisionedProductName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9._-]*`
- **Min Length**: 1
- **Max Length**: 128

### ProvisionedProductNameOrArn
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}|arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 1
- **Max Length**: 1224

### ProvisioningArtifactOutputKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 255

### RecordTagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### RecordTagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 256

### RoleArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:iam::[a-z0-9-\.]{0,63}:role\/.{0,1023}`
- **Min Length**: 1
- **Max Length**: 1224

### ServiceActionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.]*`
- **Min Length**: 1
- **Max Length**: 256

### StatusMessage
- **Type**: string
- **Pattern**: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagOptionKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagOptionValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 256

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 256

### UniqueTagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### UniqueTagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 256


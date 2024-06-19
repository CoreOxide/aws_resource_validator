# Qbusiness Service

### ApplicationArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### ApplicationId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### ApplicationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### AttachmentName
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 1
- **Max Length**: 1000

### BlockedPhrase
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 36

### ConversationId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### DataSourceArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### DataSourceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### DataSourceName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### DataSourceUserId
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 1
- **Max Length**: 1024

### Description
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 1000

### DocumentAttributeKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 200

### DocumentId
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 1
- **Max Length**: 1825

### DocumentMetadataConfigurationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 30

### ErrorMessage
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 1
- **Max Length**: 2048

### ExampleChatMessage
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 350

### ExecutionId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### GroupName
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 1
- **Max Length**: 1024

### IdcApplicationArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
- **Min Length**: 10
- **Max Length**: 1224

### IndexArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### IndexId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### IndexName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### InstanceArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
- **Min Length**: 10
- **Max Length**: 1224

### KendraIndexId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### LambdaArn
- **Type**: string
- **Pattern**: `arn:aws[a-zA-Z-]*:lambda:[a-z-]*-[0-9]:[0-9]{12}:function:[a-zA-Z0-9-_]+(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?(:[a-zA-Z0-9-_]+)?`
- **Min Length**: 1
- **Max Length**: 2048

### MessageBody
- **Type**: string
- **Pattern**: `\P{C}*$}`
- **Min Length**: 0
- **Max Length**: 1000

### MessageId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### MessageUsefulnessComment
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 1000

### MetricValue
- **Type**: string
- **Pattern**: `(([1-9][0-9]*)|0)`

### PluginArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### PluginId
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### PluginName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 100

### RetrieverArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### RetrieverId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### RetrieverName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### RoleArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### S3BucketName
- **Type**: string
- **Pattern**: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
- **Min Length**: 1
- **Max Length**: 63

### SamlMetadataXML
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1000
- **Max Length**: 10000000

### SecretArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### SecurityGroupId
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 200

### SubnetId
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 200

### SyncSchedule
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 998

### SystemMessageId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
- **Min Length**: 36
- **Max Length**: 36

### SystemMessageOverride
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 350

### TopicConfigurationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]{0,35}`
- **Min Length**: 1
- **Max Length**: 36

### TopicDescription
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 350

### Url
- **Type**: string
- **Pattern**: `(https?|ftp|file)://([^\s]*)`
- **Min Length**: 1
- **Max Length**: 2048

### UserId
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 1
- **Max Length**: 1024

### WebExperienceArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### WebExperienceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]*`
- **Min Length**: 36
- **Max Length**: 36

### WebExperienceSubtitle
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 500

### WebExperienceTitle
- **Type**: string
- **Pattern**: `\P{C}*`
- **Min Length**: 0
- **Max Length**: 500


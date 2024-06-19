# Lexv2models Service

### ActiveContextName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### AnalyticsSessionId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z._:-]`

### AudioFileS3Location
- **Type**: string
- **Pattern**: `^s3://([a-z0-9\\.-]+)/(.+)$`
- **Min Length**: 1
- **Max Length**: 1024

### BedrockKnowledgeBaseArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,40}:[0-9]{12}:knowledge-base\/[A-Za-z0-9]{10}$|^[A-Za-z0-9]{10}$`
- **Min Length**: 1
- **Max Length**: 200

### BedrockModelArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model\/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}$`

### BotAliasId
- **Type**: string
- **Pattern**: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
- **Min Length**: 10
- **Max Length**: 10

### BotAliasName
- **Type**: string
- **Pattern**: `^(\bAmazonLexTestAlias\b|[0-9a-zA-Z][_-]?)+$`
- **Min Length**: 1
- **Max Length**: 100

### BotVersion
- **Type**: string
- **Pattern**: `^(DRAFT|[0-9]+)$`
- **Min Length**: 1
- **Max Length**: 5

### BuiltInOrCustomSlotTypeId
- **Type**: string
- **Pattern**: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`
- **Min Length**: 1
- **Max Length**: 25

### CloudWatchLogGroupArn
- **Type**: string
- **Pattern**: `^arn:[\w\-]+:logs:[\w\-]+:[\d]{12}:log-group:[\.\-_/#A-Za-z0-9]{1,512}(?::\*)?$`
- **Min Length**: 1
- **Max Length**: 2048

### DTMFCharacter
- **Type**: string
- **Pattern**: `^[A-D0-9#*]{1}$`

### DomainEndpoint
- **Type**: string
- **Pattern**: `^(http|https):\/\/+[^\s]+[\w]`

### DraftBotVersion
- **Type**: string
- **Pattern**: `^DRAFT$`
- **Min Length**: 5
- **Max Length**: 5

### FilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_()\s-]+$`
- **Min Length**: 1
- **Max Length**: 100

### Id
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 10
- **Max Length**: 10

### ImportedResourceId
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z_])+$`
- **Min Length**: 5
- **Max Length**: 10

### KendraIndexArn
- **Type**: string
- **Pattern**: `^arn:aws:kendra:[a-z]+-[a-z]+-[0-9]:[0-9]{12}:index\/[a-zA-Z0-9][a-zA-Z0-9_-]*$`
- **Min Length**: 32
- **Max Length**: 2048

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:[\w\-]+:kms:[\w\-]+:[\d]{12}:(?:key\/[\w\-]+|alias\/[a-zA-Z0-9:\/_\-]{1,256})$`
- **Min Length**: 20
- **Max Length**: 2048

### LambdaARN
- **Type**: string
- **Pattern**: `arn:aws:lambda:[a-z]+-[a-z]+-[0-9]:[0-9]{12}:function:[a-zA-Z0-9-_]+(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?(:[a-zA-Z0-9-_]+)?`
- **Min Length**: 20
- **Max Length**: 2048

### Name
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`
- **Min Length**: 1
- **Max Length**: 100

### NumericalBotVersion
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 5

### OSIndexName
- **Type**: string
- **Pattern**: `^(?![_-])[a-z0-9][a-z0-9_\-]{0,254}$`
- **Min Length**: 1
- **Max Length**: 255

### ObjectPrefix
- **Type**: string
- **Pattern**: `^[\/]?+[a-zA-Z0-9!_.*\'()-]+(\/[a-zA-Z0-9!_.*\'()-]+)*$`
- **Min Length**: 1

### Operation
- **Type**: string
- **Pattern**: `lex:[a-zA-Z*]+$`
- **Min Length**: 5
- **Max Length**: 50

### PrincipalArn
- **Type**: string
- **Pattern**: `^arn:aws:iam::[0-9]{12}:(root|(user|role)/.*)$`
- **Min Length**: 30
- **Max Length**: 1024

### RevisionId
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 5

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws:iam::[0-9]{12}:role/.*$`
- **Min Length**: 32
- **Max Length**: 2048

### S3BucketArn
- **Type**: string
- **Pattern**: `^arn:[\w\-]+:s3:::[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
- **Min Length**: 1
- **Max Length**: 2048

### S3BucketName
- **Type**: string
- **Pattern**: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### S3ObjectPath
- **Type**: string
- **Pattern**: `[\.\-\!\*\_\\'\(\)a-zA-Z0-9][\.\-\!\*\_\\'\(\)\/a-zA-Z0-9]*$`
- **Min Length**: 1
- **Max Length**: 1024

### ServicePrincipal
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_.]+$`
- **Min Length**: 15
- **Max Length**: 1024

### SessionId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z._:-]+`
- **Min Length**: 2
- **Max Length**: 100

### SubSlotExpression
- **Type**: string
- **Pattern**: `[0-9A-Za-z_\-\s\(\)]+`
- **Min Length**: 0
- **Max Length**: 640

### TestResultSlotName
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_.-]?)+$`
- **Min Length**: 1
- **Max Length**: 100

### TestSetConversationId
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?)+$`
- **Min Length**: 1
- **Max Length**: 50

### Transcript
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 6000000


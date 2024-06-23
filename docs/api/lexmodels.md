# Lexmodels Service

### AliasName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### AliasNameOrListAll
- **Type**: string
- **Pattern**: `^(-|^([A-Za-z]_?)+$)$`
- **Min Length**: 1
- **Max Length**: 100

### BotChannelName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### BotName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 2
- **Max Length**: 50

### CustomOrBuiltinSlotTypeName
- **Type**: string
- **Pattern**: `^((AMAZON\.)_?|[A-Za-z]_?)+`
- **Min Length**: 1
- **Max Length**: 100

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:[\w\-]+:iam::[\d]{12}:role/.+$`
- **Min Length**: 20
- **Max Length**: 2048

### InputContextName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### IntentName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### KendraIndexArn
- **Type**: string
- **Pattern**: `arn:aws:kendra:[a-z]+-[a-z]+-[0-9]:[0-9]{12}:index\/[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 20
- **Max Length**: 2048

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:[\w\-]+:kms:[\w\-]+:[\d]{12}:(?:key\/[\w\-]+|alias\/[a-zA-Z0-9:\/_\-]{1,256})$`
- **Min Length**: 20
- **Max Length**: 2048

### LambdaARN
- **Type**: string
- **Pattern**: `arn:aws[a-zA-Z-]*:lambda:[a-z]+-[a-z]+(-[a-z]+)*-[0-9]:[0-9]{12}:function:[a-zA-Z0-9-_]+(\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?(:[a-zA-Z0-9-_]+)?`
- **Min Length**: 20
- **Max Length**: 2048

### MigrationId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 10
- **Max Length**: 10

### Name
- **Type**: string
- **Pattern**: `[a-zA-Z_]+`
- **Min Length**: 1
- **Max Length**: 100

### NumericalVersion
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 1
- **Max Length**: 64

### OutputContextName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:[\w\-]+:(?:logs:[\w\-]+:[\d]{12}:log-group:[\.\-_/#A-Za-z0-9]{1,512}(?::\*)?|s3:::[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9])$`
- **Min Length**: 1
- **Max Length**: 2048

### SlotName
- **Type**: string
- **Pattern**: `^([A-Za-z](-|_|.)?)+$`
- **Min Length**: 1
- **Max Length**: 100

### SlotTypeName
- **Type**: string
- **Pattern**: `^([A-Za-z]_?)+$`
- **Min Length**: 1
- **Max Length**: 100

### V2BotId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 10
- **Max Length**: 10

### V2BotName
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?)+$`
- **Min Length**: 1
- **Max Length**: 100

### Version
- **Type**: string
- **Pattern**: `\$LATEST|[0-9]+`
- **Min Length**: 1
- **Max Length**: 64

### roleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::[0-9]{12}:role/.*`
- **Min Length**: 20
- **Max Length**: 2048


# Athena Service

### AwsAccountId
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 12
- **Max Length**: 12

### CalculationResultType
- **Type**: string
- **Pattern**: `\w+\/[-+.\w]+`
- **Min Length**: 1
- **Max Length**: 256

### CapacityReservationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._-]+`
- **Min Length**: 1
- **Max Length**: 128

### CatalogNameString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 256

### ClientRequestToken
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 1
- **Max Length**: 36

### CommentString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 255

### ExecutorId
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 100000

### IdentityCenterApplicationArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$`
- **Min Length**: 0
- **Max Length**: 255

### IdentityCenterInstanceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
- **Min Length**: 0
- **Max Length**: 255

### KeyString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### KmsKey
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:key/?[a-zA-Z_0-9+=,.@\-_/]+$|^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:alias/?[a-zA-Z_0-9+=,.@\-_/]+$|^alias/[a-zA-Z0-9/_-]+$|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 1
- **Max Length**: 2048

### NamedQueryId
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 128

### NotebookId
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 1
- **Max Length**: 36

### NotebookName
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]+`
- **Min Length**: 1
- **Max Length**: 255

### QueryExecutionId
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 1
- **Max Length**: 128

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### S3Uri
- **Type**: string
- **Pattern**: `^(https|s3|S3)://([^/]+)/?(.*)$`
- **Max Length**: 1024

### StatementName
- **Type**: string
- **Pattern**: `[a-zA-Z_][a-zA-Z0-9_@:]{1,256}`
- **Min Length**: 1
- **Max Length**: 256

### TypeString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 4096

### WorkGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._-]{1,128}`


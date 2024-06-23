# Glue Service

### AuthTokenString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### CatalogIdString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### CodeGenIdentifier
- **Type**: string
- **Pattern**: `[A-Za-z_][A-Za-z0-9_]*`
- **Min Length**: 1
- **Max Length**: 255

### ColumnNameString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 1024

### ColumnTypeString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 131072

### CommentString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 255

### CommitIdString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 40

### CsvColumnDelimiter
- **Type**: string
- **Pattern**: `[^\r\n]`
- **Min Length**: 1
- **Max Length**: 1

### CsvQuoteSymbol
- **Type**: string
- **Pattern**: `[^\r\n]`
- **Min Length**: 1
- **Max Length**: 1

### CustomPatterns
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 16000

### DQDLString
- **Type**: string
- **Pattern**: `([\u0020-\u007E\r\s\n])*`
- **Min Length**: 1
- **Max Length**: 65536

### DataQualityObservationDescription
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### DataQualityRuleResultDescription
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### DescriptionString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### DescriptionStringRemovable
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### EnclosedInStringProperty
- **Type**: string
- **Pattern**: `([\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF]|[^\S\r\n"\'])*`

### EnclosedInStringPropertyWithQuote
- **Type**: string
- **Pattern**: `([\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF]|[^\S\r\n])*`

### ExtendedString
- **Type**: string
- **Pattern**: `[\s\S]*`

### FederationIdentifier
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 512

### FilterString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### FormatString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Max Length**: 128

### GenericLimitedString
- **Type**: string
- **Pattern**: `[A-Za-z0-9_-]*`

### GlueResourceArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov|aws-cn):glue:.*`
- **Min Length**: 1
- **Max Length**: 10240

### GlueStudioColumnNameString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 1024

### GlueVersionString
- **Type**: string
- **Pattern**: `^\w+\.\w+$`
- **Min Length**: 1
- **Max Length**: 255

### GrokPattern
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\t]*`
- **Min Length**: 1
- **Max Length**: 2048

### HashString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### IAMRoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::[0-9]{12}:role/.+`

### IdString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### KeyString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws:kms:.*`

### LocationString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Max Length**: 2056

### LogGroup
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 512

### LogStream
- **Type**: string
- **Pattern**: `[^:*]*`
- **Min Length**: 1
- **Max Length**: 512

### MaskValue
- **Type**: string
- **Pattern**: `[*A-Za-z0-9_-]*`
- **Min Length**: 0
- **Max Length**: 256

### MessagePrefix
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### MetadataKeyString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+-=._./@]+`
- **Min Length**: 1
- **Max Length**: 128

### MetadataValueString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+-=._./@]+`
- **Min Length**: 1
- **Max Length**: 256

### NameString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### NodeId
- **Type**: string
- **Pattern**: `[A-Za-z0-9_-]*`

### NodeName
- **Type**: string
- **Pattern**: `([\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF]|[^\r\n])*`

### OrchestrationArgumentsValue
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 4096

### OrchestrationIAMRoleArn
- **Type**: string
- **Pattern**: `arn:aws[^:]*:iam::[0-9]*:role/.+`
- **Min Length**: 1
- **Max Length**: 1024

### OrchestrationNameString
- **Type**: string
- **Pattern**: `[\.\-_A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 128

### OrchestrationRoleArn
- **Type**: string
- **Pattern**: `arn:aws[^:]*:iam::[0-9]*:role/.+`
- **Min Length**: 20
- **Max Length**: 2048

### OrchestrationS3Location
- **Type**: string
- **Pattern**: `^s3://([^/]+)/([^/]+/)*([^/]+)$`
- **Min Length**: 1
- **Max Length**: 8192

### PredicateString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 2048

### PythonVersionString
- **Type**: string
- **Pattern**: `^([2-3]|3[.]9)$`

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::\d{12}:role/.*`

### RuntimeNameString
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 64

### SchemaDefinitionDiff
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 340000

### SchemaDefinitionString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 170000

### SchemaRegistryNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_$#.]+`
- **Min Length**: 1
- **Max Length**: 255

### SchemaVersionIdString
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### SqlQuery
- **Type**: string
- **Pattern**: `([\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\s])*`

### TransactionIdString
- **Type**: string
- **Pattern**: `[\p{L}\p{N}\p{P}]*`
- **Min Length**: 1
- **Max Length**: 255

### TypeString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 20000

### URI
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 1
- **Max Length**: 1024

### VersionString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 255

### VersionsString
- **Type**: string
- **Pattern**: `[1-9][0-9]*|[1-9][0-9]*-[1-9][0-9]*`
- **Min Length**: 1
- **Max Length**: 100000


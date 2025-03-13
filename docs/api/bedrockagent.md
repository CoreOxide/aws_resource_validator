# Bedrockagent Service

### AgentAliasArn
- **Type**: string
- **Pattern**: `^arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}$`
- **Min Length**: 0
- **Max Length**: 2048

### AgentAliasId
- **Type**: string
- **Pattern**: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
- **Min Length**: 10
- **Max Length**: 10

### AgentArn
- **Type**: string
- **Pattern**: `^arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent/[0-9a-zA-Z]{10}$`
- **Min Length**: 0
- **Max Length**: 2048

### AgentRoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+$`
- **Min Length**: 0
- **Max Length**: 2048

### AwsDataCatalogTableName
- **Type**: string
- **Pattern**: `^.*\.*$`
- **Min Length**: 1
- **Max Length**: 200

### BedrockEmbeddingModelArn
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
- **Min Length**: 20
- **Max Length**: 2048

### BedrockModelArn
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]{1,12})?:(bedrock):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
- **Min Length**: 1
- **Max Length**: 2048

### BucketOwnerAccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ByteContentDocMimeTypeString
- **Type**: string
- **Pattern**: `[a-z]{1,20}/.{1,20}`

### ClientToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}$`
- **Min Length**: 33
- **Max Length**: 256

### ColumnName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-]+$`
- **Min Length**: 0
- **Max Length**: 63

### DraftVersion
- **Type**: string
- **Pattern**: `^DRAFT$`
- **Min Length**: 5
- **Max Length**: 5

### FieldName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### FlowAliasArn
- **Type**: string
- **Pattern**: `^arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/(TSTALIASID|[0-9a-zA-Z]{10})$`

### FlowAliasId
- **Type**: string
- **Pattern**: `^(TSTALIASID|[0-9a-zA-Z]{10})$`

### FlowAliasIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(TSTALIASID|[0-9a-zA-Z]{10})$`

### FlowArn
- **Type**: string
- **Pattern**: `^arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}$`

### FlowConditionName
- **Type**: string
- **Pattern**: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`

### FlowConnectionName
- **Type**: string
- **Pattern**: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,100}$`

### FlowExecutionRoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+$`
- **Min Length**: 0
- **Max Length**: 2048

### FlowId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]{10}$`

### FlowIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})$`

### FlowName
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`

### FlowNodeInputName
- **Type**: string
- **Pattern**: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`

### FlowNodeName
- **Type**: string
- **Pattern**: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`

### FlowNodeOutputName
- **Type**: string
- **Pattern**: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`

### GraphArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):neptune-graph:[a-zA-Z0-9-]*:[0-9]{12}:graph/g-[a-zA-Z0-9]{10}$`
- **Min Length**: 1
- **Max Length**: 255

### GuardrailIdentifier
- **Type**: string
- **Pattern**: `^(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))$`
- **Min Length**: 0
- **Max Length**: 2048

### GuardrailVersion
- **Type**: string
- **Pattern**: `^(([0-9]{1,8})|(DRAFT))$`

### HttpsUrl
- **Type**: string
- **Pattern**: `^https://[A-Za-z0-9][^\s]*$`

### Id
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]{10}$`

### IngestionJobFilterValue
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 100

### KendraIndexArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):kendra:[a-z0-9-]{1,20}:([0-9]{12}|):index/([a-zA-Z0-9][a-zA-Z0-9-]{35}|[a-zA-Z0-9][a-zA-Z0-9-]{35}-[a-zA-Z0-9][a-zA-Z0-9-]{35})$`

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
- **Min Length**: 1
- **Max Length**: 2048

### KnowledgeBaseArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+$`
- **Min Length**: 0
- **Max Length**: 128

### KnowledgeBaseId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 0
- **Max Length**: 10

### KnowledgeBaseModelIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
- **Min Length**: 1
- **Max Length**: 2048

### KnowledgeBaseRoleArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+$`
- **Min Length**: 0
- **Max Length**: 2048

### LambdaArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
- **Min Length**: 0
- **Max Length**: 2048

### LexBotAliasArn
- **Type**: string
- **Pattern**: `^arn:aws(|-us-gov):lex:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:bot-alias/[0-9a-zA-Z]+/[0-9a-zA-Z]+$`
- **Min Length**: 0
- **Max Length**: 78

### Microsoft365TenantId
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### ModelIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
- **Min Length**: 1
- **Max Length**: 2048

### MongoDbAtlasCollectionName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 63

### MongoDbAtlasDatabaseName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 63

### MongoDbAtlasEndpoint
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### MongoDbAtlasEndpointServiceName
- **Type**: string
- **Pattern**: `^(?:arn:aws(?:-us-gov|-cn|-iso|-iso-[a-z])*:.+:.*:\d+:.+/.+$|[a-zA-Z0-9*]+[a-zA-Z0-9._-]*)$`
- **Min Length**: 1
- **Max Length**: 255

### MongoDbAtlasIndexName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### Name
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`

### NextToken
- **Type**: string
- **Pattern**: `^\S*$`
- **Min Length**: 1
- **Max Length**: 2048

### NonBlankString
- **Type**: string
- **Pattern**: `^[\s\S]+$`

### NumericalVersion
- **Type**: string
- **Pattern**: `^[0-9]{1,5}$`

### OpenSearchServerlessCollectionArn
- **Type**: string
- **Pattern**: `^arn:aws:aoss:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:collection/[a-z0-9-]{3,32}$`
- **Min Length**: 0
- **Max Length**: 2048

### OpenSearchServerlessIndexName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### PineconeConnectionString
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### PineconeNamespace
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### PromptArn
- **Type**: string
- **Pattern**: `^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?)$`

### PromptId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]{10}$`

### PromptIdentifier
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z]{10})|(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10})(?::[0-9]{1,5})?$`

### PromptInputVariableName
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`

### PromptMetadataKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s._:/=+@-]*$`
- **Min Length**: 1
- **Max Length**: 128

### PromptMetadataValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s._:/=+@-]*$`
- **Min Length**: 0
- **Max Length**: 1024

### PromptModelIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
- **Min Length**: 1
- **Max Length**: 2048

### PromptName
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`

### PromptVariantName
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`

### ProvisionedModelIdentifier
- **Type**: string
- **Pattern**: `^((([0-9a-zA-Z][_-]?){1,63})|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}))$`
- **Min Length**: 1
- **Max Length**: 2048

### QueryGenerationTableName
- **Type**: string
- **Pattern**: `^.*\..*\..*$`

### RdsArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):rds:[a-zA-Z0-9-]*:[0-9]{12}:cluster:[a-zA-Z0-9-]{1,63}$`

### RdsDatabaseName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-]+$`
- **Min Length**: 0
- **Max Length**: 63

### RdsTableName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\.\-]+$`
- **Min Length**: 0
- **Max Length**: 63

### RedisEnterpriseCloudEndpoint
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### RedisEnterpriseCloudIndexName
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 2048

### S3BucketArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):s3:::[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$`
- **Min Length**: 1
- **Max Length**: 2048

### S3BucketName
- **Type**: string
- **Pattern**: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### S3BucketUri
- **Type**: string
- **Pattern**: `^s3://.{1,128}$`
- **Min Length**: 1
- **Max Length**: 2048

### S3ObjectKey
- **Type**: string
- **Pattern**: `^[.!*\'()_\-a-zA-Z0-9][.!*\'()_\-\/a-zA-Z0-9]*$`
- **Min Length**: 1
- **Max Length**: 1024

### S3ObjectUri
- **Type**: string
- **Pattern**: `^s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.{1,1024}$`
- **Min Length**: 1
- **Max Length**: 1024

### SecretArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`

### TagKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s._:/=+@-]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s._:/=+@-]*$`
- **Min Length**: 0
- **Max Length**: 256

### TaggableResourcesArn
- **Type**: string
- **Pattern**: `(^arn:aws:bedrock:[a-zA-Z0-9-]+:/d{12}:(agent|agent-alias|knowledge-base|flow|prompt)/[A-Z0-9]{10}(?:/[A-Z0-9]{10})?$|^arn:aws:bedrock:[a-zA-Z0-9-]+:/d{12}:flow/([A-Z0-9]{10})/alias/([A-Z0-9]{10})$|^arn:aws:bedrock:[a-zA-Z0-9-]+:/d{12}:prompt/([A-Z0-9]{10})?(?::/d+)?$)`
- **Min Length**: 20
- **Max Length**: 1011

### ToolName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 64

### Url
- **Type**: string
- **Pattern**: `^https?://[A-Za-z0-9][^\s]*$`

### Version
- **Type**: string
- **Pattern**: `^(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})$`
- **Min Length**: 1
- **Max Length**: 5

### WorkgroupArn
- **Type**: string
- **Pattern**: `^(arn:(aws(-[a-z]+)*):redshift-serverless:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$`


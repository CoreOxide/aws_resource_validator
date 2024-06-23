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
- **Pattern**: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?AmazonBedrockExecutionRoleForAgents_.+$`
- **Min Length**: 0
- **Max Length**: 2048

### BedrockEmbeddingModelArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))$`
- **Min Length**: 20
- **Max Length**: 1011

### BucketOwnerAccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ClientToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
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

### Id
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]{10}$`

### IngestionJobFilterValue
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 100

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

### ModelIdentifier
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+)$`
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

### ProvisionedModelIdentifier
- **Type**: string
- **Pattern**: `^((([0-9a-zA-Z][_-]?){1,63})|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}))$`
- **Min Length**: 1
- **Max Length**: 2048

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

### S3ObjectKey
- **Type**: string
- **Pattern**: `^[\.\-\!\*\_\\'\(\)a-zA-Z0-9][\.\-\!\*\_\\'\(\)\/a-zA-Z0-9]*$`
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
- **Pattern**: `(^arn:aws:bedrock:[a-zA-Z0-9-]+:/d{12}:(agent|agent-alias|knowledge-base)/[A-Z0-9]{10}(?:/[A-Z0-9]{10})?$)`
- **Min Length**: 20
- **Max Length**: 1011

### Version
- **Type**: string
- **Pattern**: `^(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})$`
- **Min Length**: 1
- **Max Length**: 5


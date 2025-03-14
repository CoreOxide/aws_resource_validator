# Firehose Service

### AWSKMSKeyARN
- **Type**: string
- **Pattern**: `arn:.*:kms:[a-zA-Z0-9\-]+:\d{12}:(key|alias)/[a-zA-Z_0-9+=,.@\-_/]+`
- **Min Length**: 1
- **Max Length**: 512

### AmazonOpenSearchServerlessCollectionEndpoint
- **Type**: string
- **Pattern**: `https:.*`
- **Min Length**: 1
- **Max Length**: 512

### AmazonOpenSearchServerlessIndexName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 80

### AmazonopensearchserviceClusterEndpoint
- **Type**: string
- **Pattern**: `https:.*`
- **Min Length**: 1
- **Max Length**: 512

### AmazonopensearchserviceDomainARN
- **Type**: string
- **Pattern**: `arn:.*:es:[a-zA-Z0-9\-]+:\d{12}:domain/[a-z][-0-9a-z]{2,27}`
- **Min Length**: 1
- **Max Length**: 512

### AmazonopensearchserviceIndexName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 80

### AmazonopensearchserviceTypeName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 100

### BucketARN
- **Type**: string
- **Pattern**: `arn:.*:s3:::[\w\.\-]{1,255}`
- **Min Length**: 1
- **Max Length**: 2048

### ClusterJDBCURL
- **Type**: string
- **Pattern**: `jdbc:(redshift|postgresql)://((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+(redshift(-serverless)?)\.([a-zA-Z0-9\.\-]+):\d{1,5}/[a-zA-Z0-9_$-]+`
- **Min Length**: 1
- **Max Length**: 512

### CopyOptions
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 10240

### CustomTimeZone
- **Type**: string
- **Pattern**: `^$|[a-zA-Z/_]+`
- **Min Length**: 0
- **Max Length**: 50

### DataTableColumns
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 10240

### DataTableName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 512

### DatabaseColumnName
- **Type**: string
- **Pattern**: `[\u0001-\uFFFF]*`
- **Min Length**: 1
- **Max Length**: 194

### DatabaseEndpoint
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 255

### DatabaseName
- **Type**: string
- **Pattern**: `[\u0001-\uFFFF]*`
- **Min Length**: 1
- **Max Length**: 64

### DatabaseTableName
- **Type**: string
- **Pattern**: `[\u0001-\uFFFF]*`
- **Min Length**: 1
- **Max Length**: 129

### DeliveryStreamARN
- **Type**: string
- **Pattern**: `arn:.*:firehose:[a-zA-Z0-9\-]+:\d{12}:deliverystream/[a-zA-Z0-9._-]+`
- **Min Length**: 1
- **Max Length**: 512

### DeliveryStreamName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 64

### DeliveryStreamVersionId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 1
- **Max Length**: 50

### DestinationId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 100

### ElasticsearchClusterEndpoint
- **Type**: string
- **Pattern**: `https:.*`
- **Min Length**: 1
- **Max Length**: 512

### ElasticsearchDomainARN
- **Type**: string
- **Pattern**: `arn:.*:es:[a-zA-Z0-9\-]+:\d{12}:domain/[a-z][-0-9a-z]{2,27}`
- **Min Length**: 1
- **Max Length**: 512

### ElasticsearchIndexName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 80

### ElasticsearchTypeName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 100

### ErrorOutputPrefix
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### FileExtension
- **Type**: string
- **Pattern**: `^$|\.[0-9a-z!\-_.*\'()]+`
- **Min Length**: 0
- **Max Length**: 128

### GlueDataCatalogARN
- **Type**: string
- **Pattern**: `arn:.*:glue:.*:\d{12}:catalog`
- **Min Length**: 1
- **Max Length**: 512

### HECEndpoint
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2048

### HECToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 2048

### HttpEndpointAccessKey
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 4096

### HttpEndpointAttributeName
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 256

### HttpEndpointAttributeValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### HttpEndpointName
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 256

### HttpEndpointUrl
- **Type**: string
- **Pattern**: `https://.*`
- **Min Length**: 1
- **Max Length**: 1000

### KinesisStreamARN
- **Type**: string
- **Pattern**: `arn:.*:kinesis:[a-zA-Z0-9\-]+:\d{12}:stream/[a-zA-Z0-9_.-]+`
- **Min Length**: 1
- **Max Length**: 512

### LogGroupName
- **Type**: string
- **Pattern**: `[\.\-_/#A-Za-z0-9]*`
- **Min Length**: 0
- **Max Length**: 512

### LogStreamName
- **Type**: string
- **Pattern**: `[^:*]*`
- **Min Length**: 0
- **Max Length**: 512

### MSKClusterARN
- **Type**: string
- **Pattern**: `arn:.*`
- **Min Length**: 1
- **Max Length**: 512

### NonEmptyString
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 1024

### NonEmptyStringWithoutWhitespace
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 1024

### Password
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 6
- **Max Length**: 512

### Prefix
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### ProcessorParameterValue
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 5120

### RoleARN
- **Type**: string
- **Pattern**: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
- **Min Length**: 1
- **Max Length**: 512

### SecretARN
- **Type**: string
- **Pattern**: `arn:.*:secretsmanager:[a-zA-Z0-9\-]+:\d{12}:secret:[a-zA-Z0-9\-/_+=.@]+`
- **Min Length**: 1
- **Max Length**: 2048

### SnowflakeAccountUrl
- **Type**: string
- **Pattern**: `.+?\.snowflakecomputing\.com`
- **Min Length**: 24
- **Max Length**: 2048

### SnowflakePrivateKey
- **Type**: string
- **Pattern**: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`
- **Min Length**: 256
- **Max Length**: 4096

### SnowflakePrivateLinkVpceId
- **Type**: string
- **Pattern**: `([a-zA-Z0-9\-\_]+\.){2,3}vpce\.[a-zA-Z0-9\-]*\.vpce-svc\-[a-zA-Z0-9\-]{17}$`
- **Min Length**: 47
- **Max Length**: 255

### StringWithLettersDigitsUnderscoresDots
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\.\_]+`
- **Min Length**: 1
- **Max Length**: 255

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:\/=+\-@%]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.:\/=+\-@%]*$`
- **Min Length**: 0
- **Max Length**: 256

### TopicName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\\._\\-]+`
- **Min Length**: 1
- **Max Length**: 255

### Username
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 512

### VpcEndpointServiceName
- **Type**: string
- **Pattern**: `([a-zA-Z0-9\-\_]+\.){2,3}vpce\.[a-zA-Z0-9\-]*\.vpce-svc\-[a-zA-Z0-9\-]{17}$`
- **Min Length**: 47
- **Max Length**: 255

### WarehouseLocation
- **Type**: string
- **Pattern**: `s3:\/\/.*`
- **Min Length**: 1
- **Max Length**: 2048


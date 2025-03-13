# Supplychain Service

### AscResourceArn
- **Type**: string
- **Pattern**: `arn:aws:scn(?::([a-z0-9-]+):([0-9]+):instance)?/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})[-_./A-Za-z0-9]*`
- **Min Length**: 20
- **Max Length**: 1011

### AwsAccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### ConfigurationS3Uri
- **Type**: string
- **Pattern**: `[sS]3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+`
- **Min Length**: 10

### DataIntegrationFlowName
- **Type**: string
- **Pattern**: `[A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 256

### DataIntegrationFlowS3Prefix
- **Type**: string
- **Pattern**: `[/A-Za-z0-9._-]+`
- **Min Length**: 0
- **Max Length**: 700

### DataIntegrationFlowSourceName
- **Type**: string
- **Pattern**: `[A-Za-z0-9_]+`
- **Min Length**: 1
- **Max Length**: 256

### DataLakeDatasetName
- **Type**: string
- **Pattern**: `[a-z0-9_]+`
- **Min Length**: 1
- **Max Length**: 75

### DataLakeDatasetNamespace
- **Type**: string
- **Pattern**: `[a-z]+`
- **Min Length**: 1
- **Max Length**: 50

### DataLakeDatasetSchemaFieldName
- **Type**: string
- **Pattern**: `[a-z0-9_]+`
- **Min Length**: 1
- **Max Length**: 100

### DataLakeDatasetSchemaName
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 100

### DatasetIdentifier
- **Type**: string
- **Pattern**: `[-_/A-Za-z0-9:]+`
- **Min Length**: 1
- **Max Length**: 1011

### InstanceDescription
- **Type**: string
- **Pattern**: `([a-zA-Z0-9., _ʼ\'%-]){0,500}`
- **Min Length**: 0
- **Max Length**: 501

### InstanceName
- **Type**: string
- **Pattern**: `(?![ _ʼ\'%-])[a-zA-Z0-9 _ʼ\'%-]{0,62}[a-zA-Z0-9]`
- **Min Length**: 0
- **Max Length**: 63

### InstanceWebAppDnsDomain
- **Type**: string
- **Pattern**: `(?![-])[a-zA-Z0-9-]{1,62}[a-zA-Z0-9]`

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9][-.a-z0-9]{0,62}:kms:([a-z0-9][-.a-z0-9]{0,62})?:([a-z0-9][-.a-z0-9]{0,62})?:key/.{0,1019}`
- **Min Length**: 0
- **Max Length**: 2048

### S3BucketName
- **Type**: string
- **Pattern**: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
- **Min Length**: 3
- **Max Length**: 63

### UUID
- **Type**: string
- **Pattern**: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36


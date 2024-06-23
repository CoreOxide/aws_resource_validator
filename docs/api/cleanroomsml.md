# Cleanroomsml Service

### AccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 12
- **Max Length**: 12

### AudienceGenerationJobArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+$`
- **Min Length**: 20
- **Max Length**: 2048

### AudienceModelArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+$`
- **Min Length**: 20
- **Max Length**: 2048

### ColumnName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
- **Min Length**: 1
- **Max Length**: 128

### ConfiguredAudienceModelArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+$`
- **Min Length**: 20
- **Max Length**: 2048

### GlueDatabaseName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_](([a-zA-Z0-9_]+-)*([a-zA-Z0-9_]+))?$`
- **Min Length**: 1
- **Max Length**: 128

### GlueTableName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
- **Min Length**: 1
- **Max Length**: 128

### Hash
- **Type**: string
- **Pattern**: `^[0-9a-f]+$`
- **Min Length**: 64
- **Max Length**: 128

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:iam::[0-9]{12}:role/.+$`
- **Min Length**: 20
- **Max Length**: 2048

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+$`
- **Min Length**: 20
- **Max Length**: 2048

### NameString
- **Type**: string
- **Pattern**: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
- **Min Length**: 1
- **Max Length**: 63

### ResourceDescription
- **Type**: string
- **Pattern**: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
- **Min Length**: 0
- **Max Length**: 255

### S3Path
- **Type**: string
- **Pattern**: `^s3://.+$`
- **Min Length**: 1
- **Max Length**: 1285

### TaggableArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:(training-dataset|audience-model|configured-audience-model|audience-generation-job)/[-a-zA-Z0-9_/.]+$`
- **Min Length**: 20
- **Max Length**: 2048

### TrainingDatasetArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+$`
- **Min Length**: 20
- **Max Length**: 2048

### UUID
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
- **Min Length**: 36
- **Max Length**: 36


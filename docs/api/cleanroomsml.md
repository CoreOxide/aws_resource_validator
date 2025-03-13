# Cleanroomsml Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`
- **Min Length**: 12
- **Max Length**: 12

### AlgorithmImage
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 255

### AnalysisTemplateArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 200

### AudienceGenerationJobArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### AudienceModelArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### ColumnName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
- **Min Length**: 1
- **Max Length**: 128

### ConfiguredAudienceModelArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### ConfiguredModelAlgorithmArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### ConfiguredModelAlgorithmAssociationArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:(membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/)?configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### ContainerArgument
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### ContainerEntrypointString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### EnvironmentKeyString
- **Type**: string
- **Pattern**: `[a-zA-Z_][a-zA-Z0-9_]*`
- **Min Length**: 1
- **Max Length**: 512

### EnvironmentValueString
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 1
- **Max Length**: 512

### GlueDatabaseName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_]+-)*([a-zA-Z0-9_]+))?`
- **Min Length**: 1
- **Max Length**: 128

### GlueTableName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
- **Min Length**: 1
- **Max Length**: 128

### Hash
- **Type**: string
- **Pattern**: `[0-9a-f]+`
- **Min Length**: 64
- **Max Length**: 128

### HyperParametersKeyString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 256

### HyperParametersValueString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 2500

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`
- **Min Length**: 20
- **Max Length**: 2048

### InferenceEnvironmentMapKeyString
- **Type**: string
- **Pattern**: `[a-zA-Z_][a-zA-Z0-9_]*`
- **Min Length**: 1
- **Max Length**: 1024

### InferenceEnvironmentMapValueString
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 1
- **Max Length**: 10240

### InferenceOutputConfigurationAcceptString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 256

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+`
- **Min Length**: 20
- **Max Length**: 2048

### MLInputChannelArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ml-input-channel/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### MetricName
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 255

### MetricRegex
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 500

### ModelTrainingDataChannelName
- **Type**: string
- **Pattern**: `[A-Za-z0-9\.\-_]+`
- **Min Length**: 1
- **Max Length**: 64

### NameString
- **Type**: string
- **Pattern**: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 63

### ParameterKey
- **Type**: string
- **Pattern**: `[0-9a-zA-Z_]+`
- **Min Length**: 1
- **Max Length**: 100

### ResourceDescription
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
- **Min Length**: 0
- **Max Length**: 255

### S3Path
- **Type**: string
- **Pattern**: `s3://.+`
- **Min Length**: 1
- **Max Length**: 1285

### TaggableArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:(membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/(configured-model-algorithm-association|trained-model|trained-model-inference-job|ml-input-channel)|training-dataset|audience-model|configured-audience-model|audience-generation-job|configured-model-algorithm|configured-model-algorithm-association|trained-model|trained-model-inference-job)/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### TrainedModelArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:(membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/)?trained-model/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### TrainedModelInferenceJobArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:(membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/)?trained-model-inference-job/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### TrainingDatasetArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### UUID
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36


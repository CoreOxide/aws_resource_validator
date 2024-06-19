# Chimesdkmediapipelines Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 1011

### Arn
- **Type**: string
- **Pattern**: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 1024

### AudioSampleRateOption
- **Type**: string
- **Pattern**: `44100|48000`

### AwsRegion
- **Type**: string
- **Pattern**: `^([a-z]+-){2,}\d+$`
- **Min Length**: 1
- **Max Length**: 32

### CategoryName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### ClientRequestToken
- **Type**: string
- **Pattern**: `[-_a-zA-Z0-9]*`
- **Min Length**: 2
- **Max Length**: 64

### FragmentNumberString
- **Type**: string
- **Pattern**: `^[0-9]+$`
- **Min Length**: 1
- **Max Length**: 128

### GuidString
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
- **Min Length**: 36
- **Max Length**: 36

### Keyword
- **Type**: string
- **Pattern**: `^[\s0-9a-zA-Z\'-]+`
- **Min Length**: 1
- **Max Length**: 100

### KinesisVideoStreamArn
- **Type**: string
- **Pattern**: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
- **Min Length**: 1
- **Max Length**: 1024

### KinesisVideoStreamPoolId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 256

### KinesisVideoStreamPoolName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 128

### LanguageOptions
- **Type**: string
- **Pattern**: `^[a-zA-Z-,]+`
- **Min Length**: 1
- **Max Length**: 200

### MediaInsightsPipelineConfigurationNameString
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 2
- **Max Length**: 64

### ModelName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Max Length**: 1024

### PiiEntityTypes
- **Type**: string
- **Pattern**: `^[A-Z_, ]+`
- **Min Length**: 1
- **Max Length**: 300

### RuleName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 2
- **Max Length**: 64

### String
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 4096

### TileAspectRatio
- **Type**: string
- **Pattern**: `^\d{1,2}\/\d{1,2}$`

### VocabularyFilterName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### VocabularyFilterNames
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9,-._]+`
- **Min Length**: 1
- **Max Length**: 3000

### VocabularyName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### VocabularyNames
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9,-._]+`
- **Min Length**: 1
- **Max Length**: 3000


# Fis Service

### ActionDescription
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### ActionId
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 128

### ActionParameterDescription
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### ActionParameterName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ActionTargetName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ClientToken
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 1024

### CloudWatchLogGroupArn
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 20
- **Max Length**: 2048

### ExceptionMessage
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 1024

### ExperimentActionDescription
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### ExperimentActionName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentActionParameter
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 1024

### ExperimentActionParameterName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentActionStartAfter
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentActionStatusReason
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### ExperimentActionTargetName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentErrorCode
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 128

### ExperimentId
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentReportErrorCode
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 128

### ExperimentReportReason
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### ExperimentReportS3ReportArn
- **Type**: string
- **Pattern**: `[\s\S]+`

### ExperimentReportS3ReportType
- **Type**: string
- **Pattern**: `[\s\S]+`

### ExperimentStatusReason
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### ExperimentTargetFilterPath
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 256

### ExperimentTargetFilterValue
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 128

### ExperimentTargetName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTargetParameterName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTargetSelectionMode
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTemplateActionDescription
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### ExperimentTemplateActionName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTemplateActionParameter
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 1024

### ExperimentTemplateActionParameterName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTemplateActionStartAfter
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTemplateActionTargetName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTemplateDescription
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### ExperimentTemplateId
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTemplateTargetFilterPath
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 256

### ExperimentTemplateTargetFilterValue
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 128

### ExperimentTemplateTargetName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTemplateTargetParameterName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### ExperimentTemplateTargetParameterValue
- **Type**: string
- **Pattern**: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]+$`
- **Min Length**: 1
- **Max Length**: 1024

### ExperimentTemplateTargetSelectionMode
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### NextToken
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 1024

### ReportConfigurationCloudWatchDashboardIdentifier
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 512

### ReportConfigurationDuration
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 32

### ReportConfigurationS3OutputPrefix
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 256

### ResourceArn
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 20
- **Max Length**: 2048

### RoleArn
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 20
- **Max Length**: 2048

### S3BucketName
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 3
- **Max Length**: 63

### S3ObjectKey
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 1
- **Max Length**: 700

### SafetyLeverId
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### StopConditionSource
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### StopConditionValue
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Min Length**: 20
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 256

### TargetAccountConfigurationDescription
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 512

### TargetAccountId
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 12
- **Max Length**: 48

### TargetInformationKey
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### TargetInformationValue
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 2048

### TargetName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64

### TargetResourceTypeDescription
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### TargetResourceTypeId
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 128

### TargetResourceTypeParameterDescription
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 512

### TargetResourceTypeParameterName
- **Type**: string
- **Pattern**: `[\S]+`
- **Max Length**: 64


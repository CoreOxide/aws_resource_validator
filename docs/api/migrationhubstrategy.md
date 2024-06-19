# Migrationhubstrategy Service

### ApplicationComponentId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z-]+`
- **Min Length**: 0
- **Max Length**: 44

### AssessmentStatusMessage
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 512

### AsyncTaskId
- **Type**: string
- **Pattern**: `[0-9a-z-:]+`
- **Min Length**: 0
- **Max Length**: 52

### IPAddress
- **Type**: string
- **Pattern**: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`
- **Min Length**: 0
- **Max Length**: 15

### InterfaceName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### ListApplicationComponentsRequestFilterValueString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 256

### Location
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### MacAddress
- **Type**: string
- **Pattern**: `^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|([0-9a-fA-F]{4}\\.[0-9a-fA-F]{4}\\.[0-9a-fA-F]{4})$”$`
- **Min Length**: 0
- **Max Length**: 17

### NetMask
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### NextToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 2048

### OSVersion
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 64

### ProjectName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### RecommendationReportStatusMessage
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 512

### RecommendationTaskId
- **Type**: string
- **Pattern**: `[0-9a-z-:]+`
- **Min Length**: 0
- **Max Length**: 52

### ResourceId
- **Type**: string
- **Pattern**: `^[0-9a-b]+`
- **Min Length**: 0
- **Max Length**: 44

### S3Bucket
- **Type**: string
- **Pattern**: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
- **Min Length**: 0
- **Max Length**: 63

### S3Key
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 1024

### SecretsManagerKey
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 512

### ServerId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 27

### SourceVersion
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 40

### StartAssessmentRequestS3bucketForAnalysisDataString
- **Type**: string
- **Pattern**: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
- **Min Length**: 0
- **Max Length**: 63

### StartAssessmentRequestS3bucketForReportDataString
- **Type**: string
- **Pattern**: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
- **Min Length**: 0
- **Max Length**: 63

### StartImportFileTaskRequestNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 50

### StartImportFileTaskRequestS3bucketForReportDataString
- **Type**: string
- **Pattern**: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
- **Min Length**: 0
- **Max Length**: 63

### StatusMessage
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 1024

### String
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 1024

### TranformationToolDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### TranformationToolInstallationLink
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### importS3Bucket
- **Type**: string
- **Pattern**: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
- **Min Length**: 0
- **Max Length**: 63

### importS3Key
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 1024


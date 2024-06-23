# Applicationcostprofiler Service

### ImportId
- **Type**: string
- **Pattern**: `[0-9A-Za-z\.\-_]*`
- **Min Length**: 1
- **Max Length**: 255

### ReportDescription
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### ReportId
- **Type**: string
- **Pattern**: `^[0-9A-Za-z\.\-_]+$`
- **Min Length**: 1
- **Max Length**: 255

### S3Bucket
- **Type**: string
- **Pattern**: `(?=^.{3,63}$)(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$)`
- **Min Length**: 3
- **Max Length**: 63

### S3Key
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 512

### S3Prefix
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 512

### Token
- **Type**: string
- **Pattern**: `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
- **Min Length**: 1
- **Max Length**: 102400


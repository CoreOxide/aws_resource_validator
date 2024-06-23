# Sagemakeredge Service

### ChecksumString
- **Type**: string
- **Pattern**: `^[a-z0-9](-*[a-z0-9])*$`
- **Min Length**: 1
- **Max Length**: 63

### DeviceFleetName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
- **Min Length**: 1
- **Max Length**: 63

### DeviceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
- **Min Length**: 1
- **Max Length**: 63

### Dimension
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9\/])*$`
- **Min Length**: 1
- **Max Length**: 1000

### EntityName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
- **Min Length**: 1
- **Max Length**: 63

### Metric
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
- **Min Length**: 4
- **Max Length**: 100

### ModelName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
- **Min Length**: 4
- **Max Length**: 255

### S3Uri
- **Type**: string
- **Pattern**: `^s3://([^/]+)/?(.*)$`
- **Max Length**: 1024

### Version
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\ \_\.]+`
- **Min Length**: 1
- **Max Length**: 64


# Simspaceweaver Service

### ClientToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 32
- **Max Length**: 128

### LogGroupArn
- **Type**: string
- **Pattern**: `^arn:(?:aws|aws-cn|aws-us-gov):log-group:([a-z]{2}-[a-z]+-\d{1}):(\d{12})?:role\/(.+)$`
- **Min Length**: 0
- **Max Length**: 1600

### RoleArn
- **Type**: string
- **Pattern**: `^arn:(?:aws|aws-cn|aws-us-gov):iam::(\d{12})?:role\/(.+)$`
- **Min Length**: 0
- **Max Length**: 1600

### SimSpaceWeaverArn
- **Type**: string
- **Pattern**: `^arn:(?:aws|aws-cn|aws-us-gov):simspaceweaver:([a-z]{2}-[a-z]+-\d{1}):(\d{12})?:([a-z]+)\/(.+)$`
- **Min Length**: 0
- **Max Length**: 1600

### SimSpaceWeaverLongResourceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 256

### SimSpaceWeaverResourceName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 64

### TimeToLiveString
- **Type**: string
- **Pattern**: `^\d{1,5}[mhdMHD]$`
- **Min Length**: 2
- **Max Length**: 6

### UUID
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
- **Min Length**: 36


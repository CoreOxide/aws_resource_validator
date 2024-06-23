# Codegurusecurity Service

### ClientToken
- **Type**: string
- **Pattern**: `^[\S]+$`
- **Min Length**: 1
- **Max Length**: 64

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws:kms:[\S]+:[\d]{12}:key\/(([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})|(mrk-[0-9a-zA-Z]{32}))$`
- **Min Length**: 1
- **Max Length**: 2048

### NextToken
- **Type**: string
- **Pattern**: `^[\S]+$`
- **Min Length**: 1
- **Max Length**: 2048

### ScanName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_$:.]*$`
- **Min Length**: 1
- **Max Length**: 140

### ScanNameArn
- **Type**: string
- **Pattern**: `^arn:aws:codeguru-security:[\S]+:[\d]{12}:scans\/[a-zA-Z0-9-_$:.]*$`
- **Min Length**: 1
- **Max Length**: 300

### Uuid
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`


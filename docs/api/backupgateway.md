# Backupgateway Service

### ActivationKey
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\-]+$`
- **Min Length**: 1
- **Max Length**: 50

### GatewayArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+$`
- **Min Length**: 50
- **Max Length**: 500

### Host
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 3
- **Max Length**: 128

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):iam::([0-9]+):role/(\S+)$`
- **Min Length**: 20
- **Max Length**: 2048

### KmsKeyArn
- **Type**: string
- **Pattern**: `^(^arn:(aws|aws-cn|aws-us-gov):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)$`
- **Min Length**: 50
- **Max Length**: 500

### LogGroupArn
- **Type**: string
- **Pattern**: `^$|^arn:(aws|aws-cn|aws-us-gov):logs:([a-zA-Z0-9-]+):([0-9]+):log-group:[a-zA-Z0-9_\-\/\.]+:\*$`
- **Min Length**: 0
- **Max Length**: 2048

### Name
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]*$`
- **Min Length**: 1
- **Max Length**: 100

### NextToken
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 1000

### Password
- **Type**: string
- **Pattern**: `^[ -~]+$`
- **Min Length**: 1
- **Max Length**: 100

### Path
- **Type**: string
- **Pattern**: `^[^\x00]+$`
- **Min Length**: 1
- **Max Length**: 4096

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+$`
- **Min Length**: 50
- **Max Length**: 500

### ServerArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+$`
- **Min Length**: 50
- **Max Length**: 500

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[^\x00]*$`
- **Min Length**: 0
- **Max Length**: 256

### Username
- **Type**: string
- **Pattern**: `^[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*$`
- **Min Length**: 1
- **Max Length**: 100


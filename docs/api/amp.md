# Amp Service

### ClusterArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:eks:[-a-z0-9]+:[0-9]{12}:cluster/.+$`

### IdempotencyToken
- **Type**: string
- **Pattern**: `^[!-~]+$`
- **Min Length**: 1
- **Max Length**: 64

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws:kms:[a-z0-9\-]+:\d+:key/[a-f0-9\-]+$`
- **Min Length**: 20
- **Max Length**: 2048

### LogGroupArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z0-9-]*:logs:[a-z0-9-]+:\d{12}:log-group:[A-Za-z0-9\.\-\_\#/]{1,512}\:\*$`

### RuleGroupsNamespaceName
- **Type**: string
- **Pattern**: `[0-9A-Za-z][-.0-9A-Z_a-z]*`
- **Min Length**: 1
- **Max Length**: 64

### ScraperAlias
- **Type**: string
- **Pattern**: `^[0-9A-Za-z][-.0-9A-Z_a-z]*$`
- **Min Length**: 1
- **Max Length**: 100

### ScraperId
- **Type**: string
- **Pattern**: `^[0-9A-Za-z][-.0-9A-Z_a-z]*$`
- **Min Length**: 1
- **Max Length**: 64

### SecurityGroupId
- **Type**: string
- **Pattern**: `^sg-[0-9a-z]+$`
- **Min Length**: 0
- **Max Length**: 255

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-[0-9a-z]+$`
- **Min Length**: 0
- **Max Length**: 255

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### WorkspaceArn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:workspace/.+$`

### WorkspaceId
- **Type**: string
- **Pattern**: `[0-9A-Za-z][-.0-9A-Z_a-z]*`
- **Min Length**: 1
- **Max Length**: 64


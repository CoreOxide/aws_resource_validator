# Cloud9 Service

### ClientRequestToken
- **Type**: string
- **Pattern**: `[\x20-\x7E]{10,128}`

### EnvironmentArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):cloud9:([a-z]{2}-[a-z]+-\d{1}):[0-9]{12}:environment:[a-zA-Z0-9]{8,32}`

### EnvironmentId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{8,32}$`

### InstanceType
- **Type**: string
- **Pattern**: `^[a-z]+[1-9][.][a-z0-9]+$`
- **Min Length**: 5
- **Max Length**: 20

### SubnetId
- **Type**: string
- **Pattern**: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`
- **Min Length**: 15
- **Max Length**: 24

### UserArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):(iam|sts)::\d+:(root|(user\/[\w+=/:,.@-]{1,64}|federated-user\/[\w+=/:,.@-]{2,32}|assumed-role\/[\w+=:,.@-]{1,64}\/[\w+=,.@-]{1,64}))$`


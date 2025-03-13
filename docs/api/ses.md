# Ses Service

### ConnectInstanceArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9-]{1}:[0-9]{1,20}:instance/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

### IAMRoleARN
- **Type**: string
- **Pattern**: `arn:[\w-]+:iam::[0-9]+:role(\u002F)([\u0021-\u007E]+\u002F)?([\w+=,.@-]+)`
- **Min Length**: 20
- **Max Length**: 2048


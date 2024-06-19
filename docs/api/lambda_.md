# Lambda Service

### FunctionArn
- **Type**: string
- **Pattern**: `arn:aws:lambda:[a-z]{2}-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?`

### FunctionName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]+`
- **Min Length**: 1
- **Max Length**: 64

### Handler
- **Type**: string
- **Pattern**: `[a-zA-Z0-9./\-_]+`

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`


# Synthetics Service

### BaseScreenshotConfigIgnoreCoordinate
- **Type**: string
- **Pattern**: `^(-?\d{1,5}\.?\d{0,2},){3}(-?\d{1,5}\.?\d{0,2}){1}$`

### CanaryArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:canary:[0-9a-z_\-]{1,21}`
- **Min Length**: 1
- **Max Length**: 2048

### CanaryName
- **Type**: string
- **Pattern**: `^[0-9a-z_\-]+$`
- **Min Length**: 1
- **Max Length**: 21

### CodeHandler
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z_-]+\/)*[0-9A-Za-z_\\-]+\.[A-Za-z_][A-Za-z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 128

### EnvironmentVariableName
- **Type**: string
- **Pattern**: `[a-zA-Z]([a-zA-Z0-9_])+`

### FunctionArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
- **Min Length**: 1
- **Max Length**: 2048

### GroupArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:group:[0-9a-z]+`
- **Min Length**: 1
- **Max Length**: 128

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:kms:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:key/[\w\-\/]+`
- **Min Length**: 1
- **Max Length**: 2048

### PaginationToken
- **Type**: string
- **Pattern**: `^.+$`
- **Min Length**: 1
- **Max Length**: 512

### ResourceArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:(canary|group):[0-9a-z_\-]+`
- **Min Length**: 1
- **Max Length**: 2048

### RoleArn
- **Type**: string
- **Pattern**: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
- **Min Length**: 1
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### UUID
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`


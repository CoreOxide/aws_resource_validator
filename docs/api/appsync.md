# Appsync Service

### CertificateArn
- **Type**: string
- **Pattern**: `^arn:[a-z-]*:(acm|iam):[a-z0-9-]*:\d{12}:(certificate|server-certificate)/[0-9A-Za-z_/-]*$`
- **Min Length**: 20
- **Max Length**: 2048

### Context
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 2
- **Max Length**: 28000

### Description
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 255

### DomainName
- **Type**: string
- **Pattern**: `^(\*[\w\d-]*\.)?([\w\d-]+\.)+[\w\d-]+$`
- **Min Length**: 1
- **Max Length**: 253

### EnvironmentVariableKey
- **Type**: string
- **Pattern**: `^[A-Za-z]+\w*$`
- **Min Length**: 2
- **Max Length**: 64

### EvaluationResult
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 0
- **Max Length**: 65536

### MappingTemplate
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 65536

### PaginationToken
- **Type**: string
- **Pattern**: `[\\S]+`
- **Min Length**: 1
- **Max Length**: 65536

### RdsDataApiConfigResourceArn
- **Type**: string
- **Pattern**: `^arn:[a-z-]*:rds:[a-z0-9-]*:\d{12}:cluster:[0-9A-Za-z_/-]*$`
- **Min Length**: 20
- **Max Length**: 2048

### RdsDataApiConfigSecretArn
- **Type**: string
- **Pattern**: `^arn:[a-z-]*:secretsmanager:[a-z0-9-]*:\d{12}:secret:[0-9A-Za-z_/+=.@!-]*$`
- **Min Length**: 20
- **Max Length**: 2048

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:aws:appsync:[A-Za-z0-9_/.-]{0,63}:\d{12}:apis/[0-9A-Za-z_-]{26}$`
- **Min Length**: 70
- **Max Length**: 75

### ResourceName
- **Type**: string
- **Pattern**: `[_A-Za-z][_0-9A-Za-z]*`
- **Min Length**: 1
- **Max Length**: 65536

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[ a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[\s\w+-=\.:/@]*$`
- **Max Length**: 256

### Template
- **Type**: string
- **Pattern**: `^[\s\S]*$`
- **Min Length**: 2
- **Max Length**: 65536


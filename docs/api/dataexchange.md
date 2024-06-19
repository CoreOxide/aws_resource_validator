# Dataexchange Service

### AwsAccountId
- **Type**: string
- **Pattern**: `.*/^[\d]{12}$/.*`
- **Min Length**: 12
- **Max Length**: 12

### ClientToken
- **Type**: string
- **Pattern**: `[\x21-\x7E]{1,64}`
- **Min Length**: 1
- **Max Length**: 64

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::(\d{12}):role\/.+`

### stringMin24Max24PatternAZaZ094AZaZ092AZaZ093
- **Type**: string
- **Pattern**: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
- **Min Length**: 24
- **Max Length**: 24


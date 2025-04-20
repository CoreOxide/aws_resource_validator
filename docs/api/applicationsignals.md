# Applicationsignals Service

### AwsAccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### KeyAttributeName
- **Type**: string
- **Pattern**: `[a-zA-Z]{1,50}`

### KeyAttributeValue
- **Type**: string
- **Pattern**: `[ -~]*[!-~]+[ -~]*`
- **Min Length**: 1
- **Max Length**: 1024

### MetricType
- **Type**: string
- **Pattern**: `[A-Za-z0-9 -]+`

### Namespace
- **Type**: string
- **Pattern**: `.*[^:].*`
- **Min Length**: 1
- **Max Length**: 255

### ServiceLevelIndicatorStatistic
- **Type**: string
- **Pattern**: `[a-zA-Z0-9.]+`
- **Min Length**: 1
- **Max Length**: 20

### ServiceLevelObjectiveArn
- **Type**: string
- **Pattern**: `arn:aws:application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
- **Min Length**: 1
- **Max Length**: 2048

### ServiceLevelObjectiveId
- **Type**: string
- **Pattern**: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]$|^arn:aws:application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`

### ServiceLevelObjectiveName
- **Type**: string
- **Pattern**: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`


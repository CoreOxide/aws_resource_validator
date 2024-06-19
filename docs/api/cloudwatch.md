# Cloudwatch Service

### AnomalyDetectorMetricStat
- **Type**: string
- **Pattern**: `(SampleCount|Average|Sum|Minimum|Maximum|IQM|(p|tc|tm|ts|wm)(\d{1,2}(\.\d{0,10})?|100)|[ou]\d+(\.\d*)?)(_E|_L|_H)?|(TM|TC|TS|WM)\(((((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?:((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%|((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%:(((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?)\)|(TM|TC|TS|WM|PR)\(((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)):((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?|((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?:(\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))\)`
- **Max Length**: 50

### AnomalyDetectorMetricTimezone
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 50

### InsightRuleDefinition
- **Type**: string
- **Pattern**: `[\x00-\x7F]+`
- **Min Length**: 1
- **Max Length**: 8192

### InsightRuleMetricName
- **Type**: string
- **Pattern**: `[\x20-\x7E]+`
- **Min Length**: 1
- **Max Length**: 32

### InsightRuleName
- **Type**: string
- **Pattern**: `[\x20-\x7E]+`
- **Min Length**: 1
- **Max Length**: 128

### InsightRuleOrderBy
- **Type**: string
- **Pattern**: `[\x20-\x7E]+`
- **Min Length**: 1
- **Max Length**: 32

### InsightRuleState
- **Type**: string
- **Pattern**: `[\x20-\x7E]+`
- **Min Length**: 1
- **Max Length**: 32

### Namespace
- **Type**: string
- **Pattern**: `[^:].*`
- **Min Length**: 1
- **Max Length**: 255

### TemplateName
- **Type**: string
- **Pattern**: `[0-9A-Za-z][\-\.\_0-9A-Za-z]{0,126}[0-9A-Za-z]`
- **Min Length**: 1
- **Max Length**: 128


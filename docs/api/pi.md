# Pi Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `^arn:.*:pi:.*$`
- **Min Length**: 1
- **Max Length**: 1011

### AnalysisReportId
- **Type**: string
- **Pattern**: `report-[0-9a-f]{17}`
- **Min Length**: 1
- **Max Length**: 100

### DescriptiveString
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 2000

### IdentifierString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 0
- **Max Length**: 256

### MarkdownString
- **Type**: string
- **Pattern**: `(.|\n)*`
- **Min Length**: 0
- **Max Length**: 8000

### NextToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_=-]+$`
- **Min Length**: 1
- **Max Length**: 8192

### RequestString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 256

### String
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 256

### TagKey
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 256


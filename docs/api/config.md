# Config Service

### AccountId
- **Type**: string
- **Pattern**: `\d{12}`

### ConfigRuleName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 128

### ConfigurationAggregatorArn
- **Type**: string
- **Pattern**: `arn:aws[a-z\-]*:config:[a-z\-\d]+:\d+:config-aggregator/config-aggregator-[a-z\d]+`

### ConfigurationAggregatorName
- **Type**: string
- **Pattern**: `[\w\-]+`
- **Min Length**: 1
- **Max Length**: 256

### ConformancePackName
- **Type**: string
- **Pattern**: `[a-zA-Z][-a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 256

### OrganizationConfigRuleName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 64

### OrganizationConformancePackName
- **Type**: string
- **Pattern**: `[a-zA-Z][-a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### PolicyRuntime
- **Type**: string
- **Pattern**: `guard\-2\.x\.x`
- **Min Length**: 1
- **Max Length**: 64

### QueryArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:config:[a-z\-\d]+:\d+:stored-query/[a-zA-Z0-9-_]+/query-[a-zA-Z\d-_/]+$`
- **Min Length**: 1
- **Max Length**: 500

### QueryDescription
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 256

### QueryExpression
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 4096

### QueryId
- **Type**: string
- **Pattern**: `^\S+$`
- **Min Length**: 1
- **Max Length**: 36

### QueryName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### RetentionConfigurationName
- **Type**: string
- **Pattern**: `[\w\-]+`
- **Min Length**: 1
- **Max Length**: 256

### SSMDocumentName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.:/]{3,200}$`

### SSMDocumentVersion
- **Type**: string
- **Pattern**: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`

### SchemaVersionId
- **Type**: string
- **Pattern**: `[A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### TemplateS3Uri
- **Type**: string
- **Pattern**: `s3://.*`
- **Min Length**: 1
- **Max Length**: 1024


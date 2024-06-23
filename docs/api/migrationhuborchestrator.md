# Migrationhuborchestrator Service

### ApplicationConfigurationName
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### ClientToken
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 256

### CreateMigrationWorkflowRequestApplicationConfigurationIdString
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]*`
- **Min Length**: 0
- **Max Length**: 100

### CreateMigrationWorkflowRequestDescriptionString
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+, ]*`
- **Min Length**: 0
- **Max Length**: 500

### CreateMigrationWorkflowRequestNameString
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### CreateMigrationWorkflowRequestTemplateIdString
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### CreateTemplateRequestTemplateDescriptionString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 250

### CreateTemplateRequestTemplateNameString
- **Type**: string
- **Pattern**: `[ a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### IPAddress
- **Type**: string
- **Pattern**: `(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])`
- **Min Length**: 0
- **Max Length**: 15

### MigrationWorkflowDescription
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+, ]*`
- **Min Length**: 0
- **Max Length**: 500

### MigrationWorkflowId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 100

### MigrationWorkflowName
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### NextToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 0
- **Max Length**: 2048

### PluginId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 60

### PluginVersion
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 1024

### ResourceArn
- **Type**: string
- **Pattern**: `arn:aws:migrationhub-orchestrator:[a-z0-9-]+:[0-9]+:(template|workflow)/[.]*`

### S3Bucket
- **Type**: string
- **Pattern**: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
- **Min Length**: 0
- **Max Length**: 63

### StepDescription
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+, ]*`
- **Min Length**: 0
- **Max Length**: 500

### StepGroupDescription
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+, ]*`
- **Min Length**: 0
- **Max Length**: 500

### StepGroupId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 100

### StepGroupName
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### StepId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 100

### StepInputParametersKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_ ()]+`
- **Min Length**: 1
- **Max Length**: 100

### StepName
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### StringMapKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_ ()]+`
- **Min Length**: 1
- **Max Length**: 100

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:)[a-zA-Z+-=._:/]+`
- **Min Length**: 1
- **Max Length**: 128

### TemplateId
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### TemplateInputName
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### TemplateName
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### UpdateMigrationWorkflowRequestDescriptionString
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+, ]*`
- **Min Length**: 0
- **Max Length**: 500

### UpdateMigrationWorkflowRequestNameString
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100

### UpdateTemplateRequestTemplateDescriptionString
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 0
- **Max Length**: 250

### UpdateTemplateRequestTemplateNameString
- **Type**: string
- **Pattern**: `[ a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### WorkflowStepOutputName
- **Type**: string
- **Pattern**: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
- **Min Length**: 1
- **Max Length**: 100


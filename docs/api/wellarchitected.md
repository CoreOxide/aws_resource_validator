# Wellarchitected Service

### ApplicationArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`
- **Max Length**: 2084

### AwsAccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`
- **Min Length**: 12
- **Max Length**: 12

### JiraProjectKey
- **Type**: string
- **Pattern**: `^[A-Z][A-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 100

### ProfileArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
- **Max Length**: 2084

### ProfileVersion
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 32

### ResourceArn
- **Type**: string
- **Pattern**: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
- **Min Length**: 50
- **Max Length**: 250

### ShareId
- **Type**: string
- **Pattern**: `[0-9a-f]{32}`

### ShareInvitationId
- **Type**: string
- **Pattern**: `[0-9a-f]{32}`

### TemplateArn
- **Type**: string
- **Pattern**: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
- **Min Length**: 50
- **Max Length**: 250

### TemplateDescription
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-_.,:/()@!&?#+\'’\s]+$`
- **Min Length**: 3
- **Max Length**: 250

### TemplateName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-_.,:/()@!&?#+\'’\s]+$`
- **Min Length**: 3
- **Max Length**: 100

### TemplateNamePrefix
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-_.,:/()@!&?#+\'’\s]+$`
- **Max Length**: 100

### WorkloadArchitecturalDesign
- **Type**: string
- **Pattern**: `^(|(https?|ftp):\/\/[^\s/$.?#].[^\s]*)$`
- **Max Length**: 2048

### WorkloadId
- **Type**: string
- **Pattern**: `[0-9a-f]{32}`
- **Min Length**: 32
- **Max Length**: 32


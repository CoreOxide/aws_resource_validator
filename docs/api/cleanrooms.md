# Cleanrooms Service

### AccountId
- **Type**: string
- **Pattern**: `\d+`
- **Min Length**: 12
- **Max Length**: 12

### AnalysisRuleColumnName
- **Type**: string
- **Pattern**: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
- **Min Length**: 1
- **Max Length**: 127

### AnalysisTemplateArn
- **Type**: string
- **Pattern**: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 200

### AnalysisTemplateArnOrQueryWildcard
- **Type**: string
- **Pattern**: `(ANY_QUERY|arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+)`
- **Min Length**: 0
- **Max Length**: 200

### AnalysisTemplateIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### CleanroomsArn
- **Type**: string
- **Pattern**: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:[\d\w/-]+`
- **Min Length**: 0
- **Max Length**: 100

### CollaborationArn
- **Type**: string
- **Pattern**: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 100

### CollaborationDescription
- **Type**: string
- **Pattern**: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
- **Min Length**: 1
- **Max Length**: 255

### CollaborationIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### CollaborationName
- **Type**: string
- **Pattern**: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 100

### ColumnName
- **Type**: string
- **Pattern**: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
- **Min Length**: 0
- **Max Length**: 128

### ColumnTypeString
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
- **Min Length**: 0
- **Max Length**: 255

### ConfiguredAudienceModelArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
- **Min Length**: 20
- **Max Length**: 2048

### ConfiguredAudienceModelAssociationArn
- **Type**: string
- **Pattern**: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/configuredaudiencemodelassociation/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 256

### ConfiguredAudienceModelAssociationIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### ConfiguredAudienceModelAssociationName
- **Type**: string
- **Pattern**: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 100

### ConfiguredTableArn
- **Type**: string
- **Pattern**: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtable/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 100

### ConfiguredTableAssociationArn
- **Type**: string
- **Pattern**: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtableassociation/[\d\w-]+/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 100

### ConfiguredTableAssociationIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### ConfiguredTableIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### DisplayName
- **Type**: string
- **Pattern**: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
- **Min Length**: 1
- **Max Length**: 100

### GlueDatabaseName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_]+-)*([a-zA-Z0-9_]+))?`
- **Min Length**: 0
- **Max Length**: 128

### GlueTableName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
- **Min Length**: 0
- **Max Length**: 128

### KeyPrefix
- **Type**: string
- **Pattern**: `[\w!.=*/-]*`
- **Min Length**: 0
- **Max Length**: 512

### MembershipArn
- **Type**: string
- **Pattern**: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 100

### MembershipIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### ParameterName
- **Type**: string
- **Pattern**: `[0-9a-zA-Z_]+`
- **Min Length**: 1
- **Max Length**: 100

### PrivacyBudgetTemplateArn
- **Type**: string
- **Pattern**: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:privacybudgettemplate/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 100

### PrivacyBudgetTemplateIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### ProtectedQueryIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### ProtectedQueryS3OutputConfigurationBucketString
- **Type**: string
- **Pattern**: `.*(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$).*`
- **Min Length**: 3
- **Max Length**: 63

### ResourceAlias
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
- **Min Length**: 0
- **Max Length**: 128

### ResourceDescription
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
- **Min Length**: 0
- **Max Length**: 255

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::[\w]+:role/[\w+=./@-]+`
- **Min Length**: 32
- **Max Length**: 512

### TableAlias
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
- **Min Length**: 0
- **Max Length**: 128

### TableDescription
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
- **Min Length**: 0
- **Max Length**: 255

### UUID
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36


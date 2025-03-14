# Cleanrooms Service

### AccountId
- **Type**: string
- **Pattern**: `\d+`
- **Min Length**: 12
- **Max Length**: 12

### AdditionalAnalysesResourceArn
- **Type**: string
- **Pattern**: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
- **Min Length**: 0
- **Max Length**: 256

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
- **Pattern**: `(ANY_QUERY|ANY_JOB|arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+)`
- **Min Length**: 0
- **Max Length**: 200

### AnalysisTemplateIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### AthenaDatabaseName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_]+-)*([a-zA-Z0-9_]+))?`
- **Min Length**: 0
- **Max Length**: 128

### AthenaOutputLocation
- **Type**: string
- **Pattern**: `s3://[a-z0-9.-]{3,63}(.*)`
- **Min Length**: 8
- **Max Length**: 1024

### AthenaTableName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
- **Min Length**: 0
- **Max Length**: 128

### AthenaWorkGroup
- **Type**: string
- **Pattern**: `([a-zA-Z0-9._-])*`
- **Min Length**: 1
- **Max Length**: 128

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

### GenericResourceName
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

### IdMappingTableArn
- **Type**: string
- **Pattern**: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/idmappingtable/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 200

### IdMappingTableInputReferenceArn
- **Type**: string
- **Pattern**: `arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(idmappingworkflow/.*)`
- **Min Length**: 20
- **Max Length**: 2048

### IdNamespaceAssociationArn
- **Type**: string
- **Pattern**: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/idnamespaceassociation/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 256

### IdNamespaceAssociationIdentifier
- **Type**: string
- **Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- **Min Length**: 36
- **Max Length**: 36

### IdNamespaceAssociationInputReferenceArn
- **Type**: string
- **Pattern**: `arn:aws:entityresolution:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:idnamespace/[\d\w-]+`
- **Min Length**: 0
- **Max Length**: 256

### KMSKeyArn
- **Type**: string
- **Pattern**: `arn:aws:kms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:key/[a-zA-Z0-9-]+`
- **Min Length**: 20
- **Max Length**: 2048

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

### SecretsManagerArn
- **Type**: string
- **Pattern**: `arn:aws:secretsmanager:[a-z]{2}-[a-z]+-[0-9]:\d{12}:secret:.*`
- **Min Length**: 0
- **Max Length**: 256

### SnowflakeAccountIdentifier
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}\p{Zs}.]+`
- **Min Length**: 3
- **Max Length**: 256

### SnowflakeDatabaseName
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}\p{Zs}]+`
- **Min Length**: 1
- **Max Length**: 256

### SnowflakeSchemaName
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}\p{Zs}]+`
- **Min Length**: 1
- **Max Length**: 256

### SnowflakeTableName
- **Type**: string
- **Pattern**: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}\p{Zs}]+`
- **Min Length**: 1
- **Max Length**: 256

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


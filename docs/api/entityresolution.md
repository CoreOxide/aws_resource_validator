# Entityresolution Service

### AttributeName
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9- \t]*$`
- **Min Length**: 0
- **Max Length**: 255

### AwsAccountId
- **Type**: string
- **Pattern**: `^\d{12}$`

### BatchDeleteUniqueIdInputInputSourceString
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})$`

### EntityName
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9-]*$`
- **Min Length**: 1
- **Max Length**: 255

### EntityNameOrIdMappingWorkflowArn
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9-=+/]*$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})$`

### EntityNameOrIdNamespaceArn
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9-=+/]*$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$`

### IdMappingWorkflowArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})$`

### IdMappingWorkflowInputSourceInputSourceARNString
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})$`

### IdNamespaceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$`

### IdNamespaceInputSourceInputSourceARNString
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})$`

### InputSourceInputSourceARNString
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})$`

### JobId
- **Type**: string
- **Pattern**: `^[a-f0-9]{32}$`

### KMSArn
- **Type**: string
- **Pattern**: `^arn:aws:kms:.*:[0-9]+:.*$`

### MatchingWorkflowArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$`

### NextToken
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9-=+/]*$`
- **Min Length**: 1
- **Max Length**: 1024

### PolicyToken
- **Type**: string
- **Pattern**: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### ProviderServiceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})$`
- **Min Length**: 20
- **Max Length**: 255

### RecordAttributeMapKeyString
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9- \t]*$`
- **Min Length**: 0
- **Max Length**: 255

### RecordAttributeMapValueString
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9-./@ ()+\t]*$`
- **Min Length**: 0
- **Max Length**: 255

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 32
- **Max Length**: 512

### RuleRuleNameString
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9- \t]*$`
- **Min Length**: 0
- **Max Length**: 255

### S3Path
- **Type**: string
- **Pattern**: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
- **Min Length**: 1
- **Max Length**: 1024

### SchemaMappingArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(schemamapping/[a-zA-Z_0-9-]{1,255})$`

### StatementAction
- **Type**: string
- **Pattern**: `^(entityresolution:[a-zA-Z0-9]+)$`
- **Min Length**: 3
- **Max Length**: 64

### StatementId
- **Type**: string
- **Pattern**: `^[0-9A-Za-z]+$`
- **Min Length**: 1
- **Max Length**: 64

### StatementPrincipal
- **Type**: string
- **Pattern**: `^(\d{12})|([a-z0-9\.]+)$`
- **Min Length**: 12
- **Max Length**: 64

### UniqueId
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9-,]*$`
- **Min Length**: 1
- **Max Length**: 760

### VeniceGlobalArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:((schemamapping|matchingworkflow|idmappingworkflow|idnamespace)/[a-zA-Z_0-9-]{1,255})$`


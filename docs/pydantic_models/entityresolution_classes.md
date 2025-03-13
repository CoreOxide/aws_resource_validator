# Entityresolution Classes

# AddPolicyStatementInputTypeDef

### action
- **Type**: typing.Sequence[str]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Allow', 'Deny']
- **Required**: Yes

### principal
- **Type**: typing.Sequence[str]
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Optional[str]


# AddPolicyStatementOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteUniqueIdInputTypeDef

### uniqueIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### inputSource
- **Type**: typing.Optional[str]


# BatchDeleteUniqueIdOutputTypeDef

### deleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.DeletedUniqueIdTypeDef]
- **Required**: Yes

### disconnectedUniqueIds
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.DeleteUniqueIdErrorTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACCEPTED', 'COMPLETED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIdMappingWorkflowInputTypeDef

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesUnionTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowInputSourceTypeDef]
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### outputSourceConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowOutputSourceTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateIdMappingWorkflowOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesOutputTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowInputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowOutputSourceTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMatchingWorkflowInputTypeDef

### inputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.InputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceUnionTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesUnionTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### incrementalRunConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.IncrementalRunConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMatchingWorkflowOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### incrementalRunConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IncrementalRunConfigTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.InputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceOutputTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesOutputTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSchemaMappingInputTypeDef

### mappedInputFields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.SchemaInputAttributeTypeDef]
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSchemaMappingOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### mappedInputFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.SchemaInputAttributeTypeDef]
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIdMappingWorkflowInputTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdMappingWorkflowOutputTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIdNamespaceInputTypeDef

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdNamespaceOutputTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMatchingWorkflowInputTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMatchingWorkflowOutputTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePolicyStatementInputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyStatementOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSchemaMappingInputTypeDef

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaMappingOutputTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUniqueIdErrorTypeDef

### errorType
- **Type**: typing.Literal['SERVICE_ERROR', 'VALIDATION_ERROR']
- **Required**: Yes

### uniqueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletedUniqueIdTypeDef

### uniqueId
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorDetailsTypeDef

### errorMessage
- **Type**: typing.Optional[str]


# GetIdMappingJobInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdMappingJobOutputTypeDef

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### errorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ErrorDetailsTypeDef'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingJobMetricsTypeDef'>
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingJobOutputSourceTypeDef]
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdMappingWorkflowInputTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdMappingWorkflowOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesOutputTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowInputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowOutputSourceTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdNamespaceInputTypeDef

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMatchIdInputTypeDef

### record
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### applyNormalization
- **Type**: typing.Optional[bool]


# GetMatchIdOutputTypeDef

### matchId
- **Type**: <class 'str'>
- **Required**: Yes

### matchRule
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMatchingJobInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMatchingJobOutputTypeDef

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### errorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ErrorDetailsTypeDef'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.JobMetricsTypeDef'>
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.JobOutputSourceTypeDef]
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMatchingWorkflowInputTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMatchingWorkflowOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### incrementalRunConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IncrementalRunConfigTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.InputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceOutputTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesOutputTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyInputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProviderServiceInputTypeDef

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetProviderServiceOutputTypeDef

### anonymizedOutput
- **Type**: <class 'bool'>
- **Required**: Yes

### providerComponentSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ProviderComponentSchemaTypeDef'>
- **Required**: Yes

### providerConfigurationDefinition
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### providerEndpointConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ProviderEndpointConfigurationTypeDef'>
- **Required**: Yes

### providerEntityOutputDefinition
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### providerIdNameSpaceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ProviderIdNameSpaceConfigurationTypeDef'>
- **Required**: Yes

### providerIntermediateDataAccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ProviderIntermediateDataAccessConfigurationTypeDef'>
- **Required**: Yes

### providerJobConfiguration
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceType
- **Type**: typing.Literal['ASSIGNMENT', 'ID_MAPPING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaMappingInputTypeDef

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaMappingOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### hasWorkflows
- **Type**: <class 'bool'>
- **Required**: Yes

### mappedInputFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.SchemaInputAttributeTypeDef]
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdMappingJobMetricsTypeDef

### inputRecords
- **Type**: typing.Optional[int]

### recordsNotProcessed
- **Type**: typing.Optional[int]

### totalMappedRecords
- **Type**: typing.Optional[int]

### totalMappedSourceRecords
- **Type**: typing.Optional[int]

### totalMappedTargetRecords
- **Type**: typing.Optional[int]

### totalRecordsProcessed
- **Type**: typing.Optional[int]


# IdMappingJobOutputSourceTypeDef

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]


# IdMappingRuleBasedPropertiesOutputTypeDef

### attributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### recordMatchingModel
- **Type**: typing.Literal['MANY_SOURCE_TO_ONE_TARGET', 'ONE_SOURCE_TO_ONE_TARGET']
- **Required**: Yes

### ruleDefinitionType
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.RuleOutputTypeDef]]


# IdMappingRuleBasedPropertiesTypeDef

### attributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### recordMatchingModel
- **Type**: typing.Literal['MANY_SOURCE_TO_ONE_TARGET', 'ONE_SOURCE_TO_ONE_TARGET']
- **Required**: Yes

### ruleDefinitionType
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.RuleTypeDef]]


# IdMappingTechniquesOutputTypeDef

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderPropertiesOutputTypeDef]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingRuleBasedPropertiesOutputTypeDef]


# IdMappingTechniquesTypeDef

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderPropertiesTypeDef]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingRuleBasedPropertiesTypeDef]


# IdMappingTechniquesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdMappingWorkflowInputSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdMappingWorkflowOutputSourceTypeDef

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]


# IdMappingWorkflowSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# IdNamespaceIdMappingWorkflowMetadataTypeDef

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes


# IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.NamespaceProviderPropertiesOutputTypeDef]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.NamespaceRuleBasedPropertiesOutputTypeDef]


# IdNamespaceIdMappingWorkflowPropertiesTypeDef

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.NamespaceProviderPropertiesUnionTypeDef]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.NamespaceRuleBasedPropertiesUnionTypeDef]


# IdNamespaceIdMappingWorkflowPropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdNamespaceInputSourceTypeDef

### inputSourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: typing.Optional[str]


# IdNamespaceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IncrementalRunConfigTypeDef

### incrementalRunType
- **Type**: typing.Optional[typing.Literal['IMMEDIATE']]


# InputSourceTypeDef

### inputSourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### applyNormalization
- **Type**: typing.Optional[bool]


# IntermediateSourceConfigurationTypeDef

### intermediateS3Path
- **Type**: <class 'str'>
- **Required**: Yes


# JobMetricsTypeDef

### inputRecords
- **Type**: typing.Optional[int]

### matchIDs
- **Type**: typing.Optional[int]

### recordsNotProcessed
- **Type**: typing.Optional[int]

### totalRecordsProcessed
- **Type**: typing.Optional[int]


# JobOutputSourceTypeDef

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]


# JobSummaryTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### endTime
- **Type**: typing.Optional[datetime.datetime]


# ListIdMappingJobsInputPaginateTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListIdMappingJobsInputTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingJobsOutputTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.JobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingWorkflowsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListIdMappingWorkflowsInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingWorkflowsOutputTypeDef

### workflowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdNamespacesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListIdNamespacesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdNamespacesOutputTypeDef

### idNamespaceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingJobsInputPaginateTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListMatchingJobsInputTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingJobsOutputTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.JobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingWorkflowsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListMatchingWorkflowsInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingWorkflowsOutputTypeDef

### workflowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.MatchingWorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProviderServicesInputPaginateTypeDef

### providerName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListProviderServicesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### providerName
- **Type**: typing.Optional[str]


# ListProviderServicesOutputTypeDef

### providerServiceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSchemaMappingsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListSchemaMappingsInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSchemaMappingsOutputTypeDef

### schemaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.SchemaMappingSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MatchingWorkflowSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### resolutionType
- **Type**: typing.Literal['ML_MATCHING', 'PROVIDER', 'RULE_MATCHING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# NamespaceProviderPropertiesOutputTypeDef

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### providerConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# NamespaceProviderPropertiesTypeDef

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### providerConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# NamespaceProviderPropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NamespaceRuleBasedPropertiesOutputTypeDef

### attributeMatchingModel
- **Type**: typing.Optional[typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']]

### recordMatchingModels
- **Type**: typing.Optional[typing.List[typing.Literal['MANY_SOURCE_TO_ONE_TARGET', 'ONE_SOURCE_TO_ONE_TARGET']]]

### ruleDefinitionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['SOURCE', 'TARGET']]]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.RuleOutputTypeDef]]


# NamespaceRuleBasedPropertiesTypeDef

### attributeMatchingModel
- **Type**: typing.Optional[typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']]

### recordMatchingModels
- **Type**: typing.Optional[typing.Sequence[typing.Literal['MANY_SOURCE_TO_ONE_TARGET', 'ONE_SOURCE_TO_ONE_TARGET']]]

### ruleDefinitionTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['SOURCE', 'TARGET']]]

### rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.RuleUnionTypeDef]]


# NamespaceRuleBasedPropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OutputAttributeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### hashed
- **Type**: typing.Optional[bool]


# OutputSourceOutputTypeDef

### output
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.OutputAttributeTypeDef]
- **Required**: Yes

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]

### applyNormalization
- **Type**: typing.Optional[bool]


# OutputSourceTypeDef

### output
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.OutputAttributeTypeDef]
- **Required**: Yes

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]

### applyNormalization
- **Type**: typing.Optional[bool]


# OutputSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProviderComponentSchemaTypeDef

### providerSchemaAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderSchemaAttributeTypeDef]]

### schemas
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# ProviderEndpointConfigurationTypeDef

### marketplaceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderMarketplaceConfigurationTypeDef]


# ProviderIdNameSpaceConfigurationTypeDef

### description
- **Type**: typing.Optional[str]

### providerSourceConfigurationDefinition
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### providerTargetConfigurationDefinition
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ProviderIntermediateDataAccessConfigurationTypeDef

### awsAccountIds
- **Type**: typing.Optional[typing.List[str]]

### requiredBucketActions
- **Type**: typing.Optional[typing.List[str]]


# ProviderMarketplaceConfigurationTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### listingId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ProviderPropertiesOutputTypeDef

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.IntermediateSourceConfigurationTypeDef]

### providerConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ProviderPropertiesTypeDef

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.IntermediateSourceConfigurationTypeDef]

### providerConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ProviderSchemaAttributeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProviderServiceSummaryTypeDef

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceType
- **Type**: typing.Literal['ASSIGNMENT', 'ID_MAPPING']
- **Required**: Yes


# PutPolicyInputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: typing.Optional[str]


# PutPolicyOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResolutionTechniquesOutputTypeDef

### resolutionType
- **Type**: typing.Literal['ML_MATCHING', 'PROVIDER', 'RULE_MATCHING']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderPropertiesOutputTypeDef]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.RuleBasedPropertiesOutputTypeDef]


# ResolutionTechniquesTypeDef

### resolutionType
- **Type**: typing.Literal['ML_MATCHING', 'PROVIDER', 'RULE_MATCHING']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderPropertiesTypeDef]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.RuleBasedPropertiesTypeDef]


# ResolutionTechniquesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# RuleBasedPropertiesOutputTypeDef

### attributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.RuleOutputTypeDef]
- **Required**: Yes

### matchPurpose
- **Type**: typing.Optional[typing.Literal['IDENTIFIER_GENERATION', 'INDEXING']]


# RuleBasedPropertiesTypeDef

### attributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.RuleTypeDef]
- **Required**: Yes

### matchPurpose
- **Type**: typing.Optional[typing.Literal['IDENTIFIER_GENERATION', 'INDEXING']]


# RuleOutputTypeDef

### matchingKeys
- **Type**: typing.List[str]
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# RuleTypeDef

### matchingKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# RuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaInputAttributeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaMappingSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### hasWorkflows
- **Type**: <class 'bool'>
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# StartIdMappingJobInputTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingJobOutputSourceTypeDef]]


# StartIdMappingJobOutputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingJobOutputSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMatchingJobInputTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# StartMatchingJobOutputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateIdMappingWorkflowInputTypeDef

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesUnionTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowInputSourceTypeDef]
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### outputSourceConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowOutputSourceTypeDef]]

### roleArn
- **Type**: typing.Optional[str]


# UpdateIdMappingWorkflowOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesOutputTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowInputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowOutputSourceTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIdNamespaceInputTypeDef

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### idMappingWorkflowProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesUnionTypeDef]]

### inputSourceConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceInputSourceTypeDef]]

### roleArn
- **Type**: typing.Optional[str]


# UpdateMatchingWorkflowInputTypeDef

### inputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.InputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceUnionTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesUnionTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### incrementalRunConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.IncrementalRunConfigTypeDef]


# UpdateMatchingWorkflowOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### incrementalRunConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IncrementalRunConfigTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.InputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceOutputTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesOutputTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSchemaMappingInputTypeDef

### mappedInputFields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.SchemaInputAttributeTypeDef]
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateSchemaMappingOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### mappedInputFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.SchemaInputAttributeTypeDef]
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



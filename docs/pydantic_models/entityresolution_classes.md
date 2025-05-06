# Entityresolution Classes

# AddPolicyStatementInput

### action
- **Type**: typing.List[str]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Allow', 'Deny']
- **Required**: Yes

### principal
- **Type**: typing.List[str]
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Optional[str]


# AddPolicyStatementOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteUniqueIdInput

### uniqueIds
- **Type**: typing.List[str]
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### inputSource
- **Type**: typing.Optional[str]


# BatchDeleteUniqueIdOutput

### deleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.DeletedUniqueId]
- **Required**: Yes

### disconnectedUniqueIds
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.DeleteUniqueIdError]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACCEPTED', 'COMPLETED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdMappingWorkflowInput

### idMappingTechniques
- **Type**: typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingTechniques, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingTechniquesOutput]
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowInputSource]
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### outputSourceConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowOutputSource]]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateIdMappingWorkflowOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingTechniquesOutput'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowInputSource]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowOutputSource]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdNamespaceInput

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### idMappingWorkflowProperties
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceIdMappingWorkflowProperties, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesOutput]]]

### inputSourceConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceInputSource]]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateIdNamespaceOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingWorkflowProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesOutput]
- **Required**: Yes

### idNamespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceInputSource]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### type
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMatchingWorkflowInput

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.InputSource]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputSource, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputSourceOutput]]
- **Required**: Yes

### resolutionTechniques
- **Type**: typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResolutionTechniques, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResolutionTechniquesOutput]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IncrementalRunConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMatchingWorkflowOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### incrementalRunConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IncrementalRunConfig'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.InputSource]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputSourceOutput]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResolutionTechniquesOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSchemaMappingInput

### mappedInputFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.SchemaInputAttribute]
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSchemaMappingOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### mappedInputFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.SchemaInputAttribute]
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIdMappingWorkflowInput

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdMappingWorkflowOutput

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIdNamespaceInput

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdNamespaceOutput

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMatchingWorkflowInput

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMatchingWorkflowOutput

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePolicyStatementInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### statementId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyStatementOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSchemaMappingInput

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaMappingOutput

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUniqueIdError

### errorType
- **Type**: typing.Literal['SERVICE_ERROR', 'VALIDATION_ERROR']
- **Required**: Yes

### uniqueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletedUniqueId

### uniqueId
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorDetails

### errorMessage
- **Type**: typing.Optional[str]


# GetIdMappingJobInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdMappingJobOutput

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### errorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ErrorDetails'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingJobMetrics'>
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingJobOutputSource]
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdMappingWorkflowInput

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdMappingWorkflowOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingTechniquesOutput'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowInputSource]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowOutputSource]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdNamespaceInput

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdNamespaceOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingWorkflowProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesOutput]
- **Required**: Yes

### idNamespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceInputSource]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### type
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# GetMatchIdInput

### record
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### applyNormalization
- **Type**: typing.Optional[bool]


# GetMatchIdOutput

### matchId
- **Type**: <class 'str'>
- **Required**: Yes

### matchRule
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# GetMatchingJobInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMatchingJobOutput

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### errorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ErrorDetails'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.JobMetrics'>
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.JobOutputSource]
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# GetMatchingWorkflowInput

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMatchingWorkflowOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### incrementalRunConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IncrementalRunConfig'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.InputSource]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputSourceOutput]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResolutionTechniquesOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# GetProviderServiceInput

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetProviderServiceOutput

### anonymizedOutput
- **Type**: <class 'bool'>
- **Required**: Yes

### providerComponentSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderComponentSchema'>
- **Required**: Yes

### providerConfigurationDefinition
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### providerEndpointConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderEndpointConfiguration'>
- **Required**: Yes

### providerEntityOutputDefinition
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### providerIdNameSpaceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderIdNameSpaceConfiguration'>
- **Required**: Yes

### providerIntermediateDataAccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderIntermediateDataAccessConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaMappingInput

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaMappingOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.SchemaInputAttribute]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# IdMappingJobMetrics

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


# IdMappingJobOutputSource

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]


# IdMappingRuleBasedProperties

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.Rule]]


# IdMappingRuleBasedPropertiesOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.RuleOutput]]


# IdMappingTechniques

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderProperties]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingRuleBasedProperties]


# IdMappingTechniquesOutput

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderPropertiesOutput]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingRuleBasedPropertiesOutput]


# IdMappingWorkflowInputSource

### inputSourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['SOURCE', 'TARGET']]


# IdMappingWorkflowOutputSource

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]


# IdMappingWorkflowSummary

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


# IdNamespaceIdMappingWorkflowMetadata

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes


# IdNamespaceIdMappingWorkflowProperties

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes

### providerProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.NamespaceProviderProperties, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.NamespaceProviderPropertiesOutput, NoneType]

### ruleBasedProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.NamespaceRuleBasedProperties, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.NamespaceRuleBasedPropertiesOutput, NoneType]


# IdNamespaceIdMappingWorkflowPropertiesOutput

### idMappingType
- **Type**: typing.Literal['PROVIDER', 'RULE_BASED']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.NamespaceProviderPropertiesOutput]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.NamespaceRuleBasedPropertiesOutput]


# IdNamespaceInputSource

### inputSourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: typing.Optional[str]


# IdNamespaceSummary

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### idNamespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### idMappingWorkflowProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceIdMappingWorkflowMetadata]]


# IncrementalRunConfig

### incrementalRunType
- **Type**: typing.Optional[typing.Literal['IMMEDIATE']]


# InputSource

### inputSourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### applyNormalization
- **Type**: typing.Optional[bool]


# IntermediateSourceConfiguration

### intermediateS3Path
- **Type**: <class 'str'>
- **Required**: Yes


# JobMetrics

### inputRecords
- **Type**: typing.Optional[int]

### matchIDs
- **Type**: typing.Optional[int]

### recordsNotProcessed
- **Type**: typing.Optional[int]

### totalRecordsProcessed
- **Type**: typing.Optional[int]


# JobOutputSource

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]


# JobSummary

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


# ListIdMappingJobsInput

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingJobsInputPaginate

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.PaginatorConfig]


# ListIdMappingJobsOutput

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingWorkflowsInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingWorkflowsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.PaginatorConfig]


# ListIdMappingWorkflowsOutput

### workflowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdNamespacesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdNamespacesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.PaginatorConfig]


# ListIdNamespacesOutput

### idNamespaceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingJobsInput

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingJobsInputPaginate

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.PaginatorConfig]


# ListMatchingJobsOutput

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingWorkflowsInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingWorkflowsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.PaginatorConfig]


# ListMatchingWorkflowsOutput

### workflowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.MatchingWorkflowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProviderServicesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### providerName
- **Type**: typing.Optional[str]


# ListProviderServicesInputPaginate

### providerName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.PaginatorConfig]


# ListProviderServicesOutput

### providerServiceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderServiceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSchemaMappingsInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSchemaMappingsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.PaginatorConfig]


# ListSchemaMappingsOutput

### schemaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.SchemaMappingSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# MatchingWorkflowSummary

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


# NamespaceProviderProperties

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### providerConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# NamespaceProviderPropertiesOutput

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### providerConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# NamespaceRuleBasedProperties

### attributeMatchingModel
- **Type**: typing.Optional[typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']]

### recordMatchingModels
- **Type**: typing.Optional[typing.List[typing.Literal['MANY_SOURCE_TO_ONE_TARGET', 'ONE_SOURCE_TO_ONE_TARGET']]]

### ruleDefinitionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['SOURCE', 'TARGET']]]

### rules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.Rule, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.RuleOutput]]]


# NamespaceRuleBasedPropertiesOutput

### attributeMatchingModel
- **Type**: typing.Optional[typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']]

### recordMatchingModels
- **Type**: typing.Optional[typing.List[typing.Literal['MANY_SOURCE_TO_ONE_TARGET', 'ONE_SOURCE_TO_ONE_TARGET']]]

### ruleDefinitionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['SOURCE', 'TARGET']]]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.RuleOutput]]


# OutputAttribute

### name
- **Type**: <class 'str'>
- **Required**: Yes

### hashed
- **Type**: typing.Optional[bool]


# OutputSource

### output
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputAttribute]
- **Required**: Yes

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]

### applyNormalization
- **Type**: typing.Optional[bool]


# OutputSourceOutput

### output
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputAttribute]
- **Required**: Yes

### outputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### KMSArn
- **Type**: typing.Optional[str]

### applyNormalization
- **Type**: typing.Optional[bool]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProviderComponentSchema

### providerSchemaAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderSchemaAttribute]]

### schemas
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# ProviderEndpointConfiguration

### marketplaceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderMarketplaceConfiguration]


# ProviderIdNameSpaceConfiguration

### description
- **Type**: typing.Optional[str]

### providerSourceConfigurationDefinition
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### providerTargetConfigurationDefinition
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ProviderIntermediateDataAccessConfiguration

### awsAccountIds
- **Type**: typing.Optional[typing.List[str]]

### requiredBucketActions
- **Type**: typing.Optional[typing.List[str]]


# ProviderMarketplaceConfiguration

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


# ProviderProperties

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IntermediateSourceConfiguration]

### providerConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ProviderPropertiesOutput

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IntermediateSourceConfiguration]

### providerConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ProviderSchemaAttribute

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ADDRESS', 'ADDRESS_CITY', 'ADDRESS_COUNTRY', 'ADDRESS_POSTALCODE', 'ADDRESS_STATE', 'ADDRESS_STREET1', 'ADDRESS_STREET2', 'ADDRESS_STREET3', 'DATE', 'EMAIL_ADDRESS', 'NAME', 'NAME_FIRST', 'NAME_LAST', 'NAME_MIDDLE', 'PHONE', 'PHONE_COUNTRYCODE', 'PHONE_NUMBER', 'PROVIDER_ID', 'STRING', 'UNIQUE_ID']
- **Required**: Yes

### hashing
- **Type**: typing.Optional[bool]

### subType
- **Type**: typing.Optional[str]


# ProviderServiceSummary

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


# PutPolicyInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: typing.Optional[str]


# PutPolicyOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# ResolutionTechniques

### resolutionType
- **Type**: typing.Literal['ML_MATCHING', 'PROVIDER', 'RULE_MATCHING']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderProperties]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.RuleBasedProperties]


# ResolutionTechniquesOutput

### resolutionType
- **Type**: typing.Literal['ML_MATCHING', 'PROVIDER', 'RULE_MATCHING']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ProviderPropertiesOutput]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.RuleBasedPropertiesOutput]


# ResponseMetadata

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


# Rule

### matchingKeys
- **Type**: typing.List[str]
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# RuleBasedProperties

### attributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.Rule]
- **Required**: Yes

### matchPurpose
- **Type**: typing.Optional[typing.Literal['IDENTIFIER_GENERATION', 'INDEXING']]


# RuleBasedPropertiesOutput

### attributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.RuleOutput]
- **Required**: Yes

### matchPurpose
- **Type**: typing.Optional[typing.Literal['IDENTIFIER_GENERATION', 'INDEXING']]


# RuleOutput

### matchingKeys
- **Type**: typing.List[str]
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaInputAttribute

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ADDRESS', 'ADDRESS_CITY', 'ADDRESS_COUNTRY', 'ADDRESS_POSTALCODE', 'ADDRESS_STATE', 'ADDRESS_STREET1', 'ADDRESS_STREET2', 'ADDRESS_STREET3', 'DATE', 'EMAIL_ADDRESS', 'NAME', 'NAME_FIRST', 'NAME_LAST', 'NAME_MIDDLE', 'PHONE', 'PHONE_COUNTRYCODE', 'PHONE_NUMBER', 'PROVIDER_ID', 'STRING', 'UNIQUE_ID']
- **Required**: Yes

### groupName
- **Type**: typing.Optional[str]

### hashed
- **Type**: typing.Optional[bool]

### matchKey
- **Type**: typing.Optional[str]

### subType
- **Type**: typing.Optional[str]


# SchemaMappingSummary

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


# StartIdMappingJobInput

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingJobOutputSource]]


# StartIdMappingJobOutput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingJobOutputSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# StartMatchingJobInput

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes


# StartMatchingJobOutput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateIdMappingWorkflowInput

### idMappingTechniques
- **Type**: typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingTechniques, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingTechniquesOutput]
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowInputSource]
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### outputSourceConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowOutputSource]]

### roleArn
- **Type**: typing.Optional[str]


# UpdateIdMappingWorkflowOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingTechniquesOutput'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowInputSource]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdMappingWorkflowOutputSource]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIdNamespaceInput

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### idMappingWorkflowProperties
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceIdMappingWorkflowProperties, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesOutput]]]

### inputSourceConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceInputSource]]

### roleArn
- **Type**: typing.Optional[str]


# UpdateIdNamespaceOutput

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingWorkflowProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesOutput]
- **Required**: Yes

### idNamespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IdNamespaceInputSource]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMatchingWorkflowInput

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.InputSource]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputSource, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputSourceOutput]]
- **Required**: Yes

### resolutionTechniques
- **Type**: typing.Union[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResolutionTechniques, aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResolutionTechniquesOutput]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IncrementalRunConfig]


# UpdateMatchingWorkflowOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### incrementalRunConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.IncrementalRunConfig'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.InputSource]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.OutputSourceOutput]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResolutionTechniquesOutput'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSchemaMappingInput

### mappedInputFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.SchemaInputAttribute]
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateSchemaMappingOutput

### description
- **Type**: <class 'str'>
- **Required**: Yes

### mappedInputFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.SchemaInputAttribute]
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution.entityresolution_classes.ResponseMetadata'>
- **Required**: Yes



# entityresolution_classes

# AddPolicyStatementInputRequestTypeDef

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

# BatchDeleteUniqueIdInputRequestTypeDef

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


# CreateIdMappingWorkflowInputRequestTypeDef

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowInputSourceTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### outputSourceConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowOutputSourceTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateIdMappingWorkflowOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesTypeDef'>
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


# CreateIdNamespaceInputRequestTypeDef

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### idMappingWorkflowProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesTypeDef]]

### inputSourceConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceInputSourceTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateIdNamespaceOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingWorkflowProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesTypeDef]
- **Required**: Yes

### idNamespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceInputSourceTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMatchingWorkflowInputRequestTypeDef

### inputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.InputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesTypeDef'>
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


# CreateSchemaMappingInputRequestTypeDef

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


# DeleteIdMappingWorkflowInputRequestTypeDef

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


# DeleteIdNamespaceInputRequestTypeDef

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


# DeleteMatchingWorkflowInputRequestTypeDef

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


# DeletePolicyStatementInputRequestTypeDef

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


# DeleteSchemaMappingInputRequestTypeDef

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


# GetIdMappingJobInputRequestTypeDef

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


# GetIdMappingWorkflowInputRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesTypeDef'>
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


# GetIdNamespaceInputRequestTypeDef

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdNamespaceOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingWorkflowProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesTypeDef]
- **Required**: Yes

### idNamespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceInputSourceTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMatchIdInputRequestTypeDef

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


# GetMatchingJobInputRequestTypeDef

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


# GetMatchingWorkflowInputRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesTypeDef'>
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


# GetPolicyInputRequestTypeDef

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


# GetProviderServiceInputRequestTypeDef

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


# GetSchemaMappingInputRequestTypeDef

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


# IdMappingTechniquesTypeDef

### idMappingType
- **Type**: typing.Literal['PROVIDER']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderPropertiesTypeDef]


# IdMappingWorkflowInputSourceTypeDef

### inputSourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['SOURCE', 'TARGET']]


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


# IdNamespaceIdMappingWorkflowPropertiesTypeDef

### idMappingType
- **Type**: typing.Literal['PROVIDER']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.NamespaceProviderPropertiesTypeDef]


# IdNamespaceInputSourceTypeDef

### inputSourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### schemaName
- **Type**: typing.Optional[str]


# IdNamespaceSummaryTypeDef

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


# ListIdMappingJobsInputListIdMappingJobsPaginateTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListIdMappingJobsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIdMappingWorkflowsInputListIdMappingWorkflowsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListIdMappingWorkflowsInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdMappingWorkflowsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workflowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIdNamespacesInputListIdNamespacesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListIdNamespacesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdNamespacesOutputTypeDef

### idNamespaceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMatchingJobsInputListMatchingJobsPaginateTypeDef

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListMatchingJobsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListMatchingWorkflowsInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMatchingWorkflowsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workflowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.MatchingWorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProviderServicesInputListProviderServicesPaginateTypeDef

### providerName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListProviderServicesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### providerName
- **Type**: typing.Optional[str]


# ListProviderServicesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### providerServiceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.PaginatorConfigTypeDef]


# ListSchemaMappingsInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSchemaMappingsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### schemaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.SchemaMappingSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

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


# NamespaceProviderPropertiesTypeDef

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### providerConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# OutputAttributeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### hashed
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


# ProviderPropertiesTypeDef

### providerServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.IntermediateSourceConfigurationTypeDef]

### providerConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ProviderSchemaAttributeTypeDef

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


# PutPolicyInputRequestTypeDef

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


# ResolutionTechniquesTypeDef

### resolutionType
- **Type**: typing.Literal['ML_MATCHING', 'PROVIDER', 'RULE_MATCHING']
- **Required**: Yes

### providerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.ProviderPropertiesTypeDef]

### ruleBasedProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.entityresolution_classes.RuleBasedPropertiesTypeDef]


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


# RuleBasedPropertiesTypeDef

### attributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.RuleTypeDef]
- **Required**: Yes


# RuleTypeDef

### matchingKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ruleName
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaInputAttributeTypeDef

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ADDRESS', 'ADDRESS_CITY', 'ADDRESS_COUNTRY', 'ADDRESS_POSTALCODE', 'ADDRESS_STATE', 'ADDRESS_STREET1', 'ADDRESS_STREET2', 'ADDRESS_STREET3', 'DATE', 'EMAIL_ADDRESS', 'NAME', 'NAME_FIRST', 'NAME_LAST', 'NAME_MIDDLE', 'PHONE', 'PHONE_COUNTRYCODE', 'PHONE_NUMBER', 'PROVIDER_ID', 'STRING', 'UNIQUE_ID']
- **Required**: Yes

### groupName
- **Type**: typing.Optional[str]

### matchKey
- **Type**: typing.Optional[str]

### subType
- **Type**: typing.Optional[str]


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


# StartIdMappingJobInputRequestTypeDef

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


# StartMatchingJobInputRequestTypeDef

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


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateIdMappingWorkflowInputRequestTypeDef

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesTypeDef'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowInputSourceTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### outputSourceConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingWorkflowOutputSourceTypeDef]]


# UpdateIdMappingWorkflowOutputTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.IdMappingTechniquesTypeDef'>
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


# UpdateIdNamespaceInputRequestTypeDef

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### idMappingWorkflowProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesTypeDef]]

### inputSourceConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceInputSourceTypeDef]]

### roleArn
- **Type**: typing.Optional[str]


# UpdateIdNamespaceOutputTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### idMappingWorkflowProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceIdMappingWorkflowPropertiesTypeDef]
- **Required**: Yes

### idNamespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### idNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### inputSourceConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.IdNamespaceInputSourceTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMatchingWorkflowInputRequestTypeDef

### inputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.InputSourceTypeDef]
- **Required**: Yes

### outputSourceConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.entityresolution_classes.OutputSourceTypeDef]
- **Required**: Yes

### resolutionTechniques
- **Type**: <class 'aws_resource_validator.pydantic_models.entityresolution_classes.ResolutionTechniquesTypeDef'>
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


# UpdateSchemaMappingInputRequestTypeDef

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



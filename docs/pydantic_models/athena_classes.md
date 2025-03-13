# Athena Classes

# AclConfigurationTypeDef

### S3AclOption
- **Type**: typing.Literal['BUCKET_OWNER_FULL_CONTROL']
- **Required**: Yes


# ApplicationDPUSizesTypeDef

### ApplicationRuntimeId
- **Type**: typing.Optional[str]

### SupportedDPUSizes
- **Type**: typing.Optional[typing.List[int]]


# AthenaErrorTypeDef

### ErrorCategory
- **Type**: typing.Optional[int]

### ErrorType
- **Type**: typing.Optional[int]

### Retryable
- **Type**: typing.Optional[bool]

### ErrorMessage
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetNamedQueryInputTypeDef

### NamedQueryIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetNamedQueryOutputTypeDef

### NamedQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.NamedQueryTypeDef]
- **Required**: Yes

### UnprocessedNamedQueryIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.UnprocessedNamedQueryIdTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetPreparedStatementInputTypeDef

### PreparedStatementNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetPreparedStatementOutputTypeDef

### PreparedStatements
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.PreparedStatementTypeDef]
- **Required**: Yes

### UnprocessedPreparedStatementNames
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.UnprocessedPreparedStatementNameTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetQueryExecutionInputTypeDef

### QueryExecutionIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetQueryExecutionOutputTypeDef

### QueryExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.QueryExecutionTypeDef]
- **Required**: Yes

### UnprocessedQueryExecutionIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.UnprocessedQueryExecutionIdTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CalculationConfigurationTypeDef

### CodeBlock
- **Type**: typing.Optional[str]


# CalculationResultTypeDef

### StdOutS3Uri
- **Type**: typing.Optional[str]

### StdErrorS3Uri
- **Type**: typing.Optional[str]

### ResultS3Uri
- **Type**: typing.Optional[str]

### ResultType
- **Type**: typing.Optional[str]


# CalculationStatisticsTypeDef

### DpuExecutionInMillis
- **Type**: typing.Optional[int]

### Progress
- **Type**: typing.Optional[str]


# CalculationStatusTypeDef

### SubmissionDateTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionDateTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'CREATING', 'FAILED', 'QUEUED', 'RUNNING']]

### StateChangeReason
- **Type**: typing.Optional[str]


# CalculationSummaryTypeDef

### CalculationExecutionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.CalculationStatusTypeDef]


# CancelCapacityReservationInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CapacityAllocationTypeDef

### Status
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### RequestTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StatusMessage
- **Type**: typing.Optional[str]

### RequestCompletionTime
- **Type**: typing.Optional[datetime.datetime]


# CapacityAssignmentConfigurationTypeDef

### CapacityReservationName
- **Type**: typing.Optional[str]

### CapacityAssignments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.CapacityAssignmentOutputTypeDef]]


# CapacityAssignmentOutputTypeDef

### WorkGroupNames
- **Type**: typing.Optional[typing.List[str]]


# CapacityAssignmentTypeDef

### WorkGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]


# CapacityAssignmentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityReservationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'UPDATE_PENDING']
- **Required**: Yes

### TargetDpus
- **Type**: <class 'int'>
- **Required**: Yes

### AllocatedDpus
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastAllocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.CapacityAllocationTypeDef]

### LastSuccessfulAllocationTime
- **Type**: typing.Optional[datetime.datetime]


# ColumnInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCapacityReservationInputTypeDef

### TargetDpus
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.TagTypeDef]]


# CreateDataCatalogOutputTypeDef

### DataCatalog
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.DataCatalogTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNamedQueryInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### WorkGroup
- **Type**: typing.Optional[str]


# CreateNamedQueryOutputTypeDef

### NamedQueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNotebookInputTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateNotebookOutputTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePreparedStatementInputTypeDef

### StatementName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreatePresignedNotebookUrlRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePresignedNotebookUrlResponseTypeDef

### NotebookUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AuthToken
- **Type**: <class 'str'>
- **Required**: Yes

### AuthTokenExpirationTime
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkGroupInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.WorkGroupConfigurationTypeDef]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.TagTypeDef]]


# CustomerContentEncryptionConfigurationTypeDef

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes


# DataCatalogSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataCatalogTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatabaseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# DatumTypeDef

### VarCharValue
- **Type**: typing.Optional[str]


# DeleteCapacityReservationInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataCatalogInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteCatalogOnly
- **Type**: typing.Optional[bool]


# DeleteDataCatalogOutputTypeDef

### DataCatalog
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.DataCatalogTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNamedQueryInputTypeDef

### NamedQueryId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotebookInputTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePreparedStatementInputTypeDef

### StatementName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkGroupInputTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### RecursiveDeleteOption
- **Type**: typing.Optional[bool]


# EncryptionConfigurationTypeDef

### EncryptionOption
- **Type**: typing.Literal['CSE_KMS', 'SSE_KMS', 'SSE_S3']
- **Required**: Yes

### KmsKey
- **Type**: typing.Optional[str]


# EngineConfigurationOutputTypeDef

### MaxConcurrentDpus
- **Type**: <class 'int'>
- **Required**: Yes

### CoordinatorDpuSize
- **Type**: typing.Optional[int]

### DefaultExecutorDpuSize
- **Type**: typing.Optional[int]

### AdditionalConfigs
- **Type**: typing.Optional[typing.Dict[str, str]]

### SparkProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# EngineConfigurationTypeDef

### MaxConcurrentDpus
- **Type**: <class 'int'>
- **Required**: Yes

### CoordinatorDpuSize
- **Type**: typing.Optional[int]

### DefaultExecutorDpuSize
- **Type**: typing.Optional[int]

### AdditionalConfigs
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SparkProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# EngineConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EngineVersionTypeDef

### SelectedEngineVersion
- **Type**: typing.Optional[str]

### EffectiveEngineVersion
- **Type**: typing.Optional[str]


# ExecutorsSummaryTypeDef

### ExecutorId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutorType
- **Type**: typing.Optional[typing.Literal['COORDINATOR', 'GATEWAY', 'WORKER']]

### StartDateTime
- **Type**: typing.Optional[int]

### TerminationDateTime
- **Type**: typing.Optional[int]

### ExecutorState
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'FAILED', 'REGISTERED', 'TERMINATED', 'TERMINATING']]

### ExecutorSize
- **Type**: typing.Optional[int]


# ExportNotebookInputTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportNotebookOutputTypeDef

### NotebookMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.NotebookMetadataTypeDef'>
- **Required**: Yes

### Payload
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilterDefinitionTypeDef

### Name
- **Type**: typing.Optional[str]


# GetCalculationExecutionCodeRequestTypeDef

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculationExecutionCodeResponseTypeDef

### CodeBlock
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCalculationExecutionRequestTypeDef

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculationExecutionResponseTypeDef

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### WorkingDirectory
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationStatusTypeDef'>
- **Required**: Yes

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationStatisticsTypeDef'>
- **Required**: Yes

### Result
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCalculationExecutionStatusRequestTypeDef

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculationExecutionStatusResponseTypeDef

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationStatusTypeDef'>
- **Required**: Yes

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCapacityAssignmentConfigurationInputTypeDef

### CapacityReservationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCapacityAssignmentConfigurationOutputTypeDef

### CapacityAssignmentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CapacityAssignmentConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCapacityReservationInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCapacityReservationOutputTypeDef

### CapacityReservation
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CapacityReservationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataCatalogInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]


# GetDataCatalogOutputTypeDef

### DataCatalog
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.DataCatalogTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDatabaseInputTypeDef

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]


# GetDatabaseOutputTypeDef

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.DatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNamedQueryInputTypeDef

### NamedQueryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetNamedQueryOutputTypeDef

### NamedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.NamedQueryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNotebookMetadataInputTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes


# GetNotebookMetadataOutputTypeDef

### NotebookMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.NotebookMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPreparedStatementInputTypeDef

### StatementName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# GetPreparedStatementOutputTypeDef

### PreparedStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.PreparedStatementTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryExecutionInputTypeDef

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryExecutionOutputTypeDef

### QueryExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.QueryExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryResultsInputPaginateTypeDef

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# GetQueryResultsInputTypeDef

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetQueryResultsOutputTypeDef

### UpdateCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResultSet
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResultSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetQueryRuntimeStatisticsInputTypeDef

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryRuntimeStatisticsOutputTypeDef

### QueryRuntimeStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.QueryRuntimeStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### EngineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.EngineConfigurationOutputTypeDef'>
- **Required**: Yes

### NotebookVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SessionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.SessionConfigurationTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.SessionStatusTypeDef'>
- **Required**: Yes

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.SessionStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionStatusRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionStatusResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.SessionStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableMetadataInputTypeDef

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]


# GetTableMetadataOutputTypeDef

### TableMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.TableMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkGroupInputTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkGroupOutputTypeDef

### WorkGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.WorkGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityCenterConfigurationTypeDef

### EnableIdentityCenter
- **Type**: typing.Optional[bool]

### IdentityCenterInstanceArn
- **Type**: typing.Optional[str]


# ImportNotebookOutputTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationDPUSizesInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationDPUSizesOutputTypeDef

### ApplicationDPUSizes
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.ApplicationDPUSizesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCalculationExecutionsRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### StateFilter
- **Type**: typing.Optional[typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'CREATING', 'FAILED', 'QUEUED', 'RUNNING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCalculationExecutionsResponseTypeDef

### Calculations
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.CalculationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCapacityReservationsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCapacityReservationsOutputTypeDef

### CapacityReservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.CapacityReservationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataCatalogsInputPaginateTypeDef

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListDataCatalogsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListDataCatalogsOutputTypeDef

### DataCatalogsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.DataCatalogSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatabasesInputPaginateTypeDef

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListDatabasesInputTypeDef

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListDatabasesOutputTypeDef

### DatabaseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.DatabaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngineVersionsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEngineVersionsOutputTypeDef

### EngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.EngineVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExecutorsRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutorStateFilter
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'FAILED', 'REGISTERED', 'TERMINATED', 'TERMINATING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExecutorsResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutorsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.ExecutorsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNamedQueriesInputPaginateTypeDef

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListNamedQueriesInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListNamedQueriesOutputTypeDef

### NamedQueryIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookMetadataInputTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.FilterDefinitionTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNotebookMetadataOutputTypeDef

### NotebookMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.NotebookMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookSessionsRequestTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookSessionsResponseTypeDef

### NotebookSessionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.NotebookSessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPreparedStatementsInputTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPreparedStatementsOutputTypeDef

### PreparedStatements
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.PreparedStatementSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueryExecutionsInputPaginateTypeDef

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListQueryExecutionsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListQueryExecutionsOutputTypeDef

### QueryExecutionIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSessionsRequestTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### StateFilter
- **Type**: typing.Optional[typing.Literal['BUSY', 'CREATED', 'CREATING', 'DEGRADED', 'FAILED', 'IDLE', 'TERMINATED', 'TERMINATING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSessionsResponseTypeDef

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.SessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTableMetadataInputPaginateTypeDef

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListTableMetadataInputTypeDef

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListTableMetadataOutputTypeDef

### TableMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.TableMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputPaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkGroupsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkGroupsOutputTypeDef

### WorkGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.WorkGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NamedQueryTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### NamedQueryId
- **Type**: typing.Optional[str]

### WorkGroup
- **Type**: typing.Optional[str]


# NotebookMetadataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotebookSessionSummaryTypeDef

### SessionId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PreparedStatementSummaryTypeDef

### StatementName
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# PreparedStatementTypeDef

### StatementName
- **Type**: typing.Optional[str]

### QueryStatement
- **Type**: typing.Optional[str]

### WorkGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# PutCapacityAssignmentConfigurationInputTypeDef

### CapacityReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityAssignments
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.CapacityAssignmentUnionTypeDef]
- **Required**: Yes


# QueryExecutionContextTypeDef

### Database
- **Type**: typing.Optional[str]

### Catalog
- **Type**: typing.Optional[str]


# QueryExecutionStatisticsTypeDef

### EngineExecutionTimeInMillis
- **Type**: typing.Optional[int]

### DataScannedInBytes
- **Type**: typing.Optional[int]

### DataManifestLocation
- **Type**: typing.Optional[str]

### TotalExecutionTimeInMillis
- **Type**: typing.Optional[int]

### QueryQueueTimeInMillis
- **Type**: typing.Optional[int]

### ServicePreProcessingTimeInMillis
- **Type**: typing.Optional[int]

### QueryPlanningTimeInMillis
- **Type**: typing.Optional[int]

### ServiceProcessingTimeInMillis
- **Type**: typing.Optional[int]

### ResultReuseInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultReuseInformationTypeDef]


# QueryExecutionStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']]

### StateChangeReason
- **Type**: typing.Optional[str]

### SubmissionDateTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionDateTime
- **Type**: typing.Optional[datetime.datetime]

### AthenaError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.AthenaErrorTypeDef]


# QueryExecutionTypeDef

### QueryExecutionId
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]

### StatementType
- **Type**: typing.Optional[typing.Literal['DDL', 'DML', 'UTILITY']]

### ResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultConfigurationTypeDef]

### ResultReuseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultReuseConfigurationTypeDef]

### QueryExecutionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryExecutionContextTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryExecutionStatusTypeDef]

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryExecutionStatisticsTypeDef]

### WorkGroup
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.EngineVersionTypeDef]

### ExecutionParameters
- **Type**: typing.Optional[typing.List[str]]

### SubstatementType
- **Type**: typing.Optional[str]

### QueryResultsS3AccessGrantsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryResultsS3AccessGrantsConfigurationTypeDef]


# QueryResultsS3AccessGrantsConfigurationTypeDef

### EnableS3AccessGrants
- **Type**: <class 'bool'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['DIRECTORY_IDENTITY']
- **Required**: Yes

### CreateUserLevelPrefix
- **Type**: typing.Optional[bool]


# QueryRuntimeStatisticsRowsTypeDef

### InputRows
- **Type**: typing.Optional[int]

### InputBytes
- **Type**: typing.Optional[int]

### OutputBytes
- **Type**: typing.Optional[int]

### OutputRows
- **Type**: typing.Optional[int]


# QueryRuntimeStatisticsTimelineTypeDef

### QueryQueueTimeInMillis
- **Type**: typing.Optional[int]

### ServicePreProcessingTimeInMillis
- **Type**: typing.Optional[int]

### QueryPlanningTimeInMillis
- **Type**: typing.Optional[int]

### EngineExecutionTimeInMillis
- **Type**: typing.Optional[int]

### ServiceProcessingTimeInMillis
- **Type**: typing.Optional[int]

### TotalExecutionTimeInMillis
- **Type**: typing.Optional[int]


# QueryRuntimeStatisticsTypeDef

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryRuntimeStatisticsTimelineTypeDef]

### Rows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryRuntimeStatisticsRowsTypeDef]

### OutputStage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryStageTypeDef]


# QueryStagePlanNodeTypeDef

### Name
- **Type**: typing.Optional[str]

### Identifier
- **Type**: typing.Optional[str]

### Children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### RemoteSources
- **Type**: typing.Optional[typing.List[str]]


# QueryStageTypeDef

### StageId
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[str]

### OutputBytes
- **Type**: typing.Optional[int]

### OutputRows
- **Type**: typing.Optional[int]

### InputBytes
- **Type**: typing.Optional[int]

### InputRows
- **Type**: typing.Optional[int]

### ExecutionTime
- **Type**: typing.Optional[int]

### QueryStagePlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryStagePlanNodeTypeDef]

### SubStages
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


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


# ResultConfigurationTypeDef

### OutputLocation
- **Type**: typing.Optional[str]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.EncryptionConfigurationTypeDef]

### ExpectedBucketOwner
- **Type**: typing.Optional[str]

### AclConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.AclConfigurationTypeDef]


# ResultConfigurationUpdatesTypeDef

### OutputLocation
- **Type**: typing.Optional[str]

### RemoveOutputLocation
- **Type**: typing.Optional[bool]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.EncryptionConfigurationTypeDef]

### RemoveEncryptionConfiguration
- **Type**: typing.Optional[bool]

### ExpectedBucketOwner
- **Type**: typing.Optional[str]

### RemoveExpectedBucketOwner
- **Type**: typing.Optional[bool]

### AclConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.AclConfigurationTypeDef]

### RemoveAclConfiguration
- **Type**: typing.Optional[bool]


# ResultReuseByAgeConfigurationTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxAgeInMinutes
- **Type**: typing.Optional[int]


# ResultReuseConfigurationTypeDef

### ResultReuseByAgeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultReuseByAgeConfigurationTypeDef]


# ResultReuseInformationTypeDef

### ReusedPreviousResult
- **Type**: <class 'bool'>
- **Required**: Yes


# ResultSetMetadataTypeDef

### ColumnInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.ColumnInfoTypeDef]]


# ResultSetTypeDef

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.RowTypeDef]]

### ResultSetMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultSetMetadataTypeDef]


# RowTypeDef

### Data
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.DatumTypeDef]]


# SessionConfigurationTypeDef

### ExecutionRole
- **Type**: typing.Optional[str]

### WorkingDirectory
- **Type**: typing.Optional[str]

### IdleTimeoutSeconds
- **Type**: typing.Optional[int]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.EncryptionConfigurationTypeDef]


# SessionStatisticsTypeDef

### DpuExecutionInMillis
- **Type**: typing.Optional[int]


# SessionStatusTypeDef

### StartDateTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]

### IdleSinceDateTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['BUSY', 'CREATED', 'CREATING', 'DEGRADED', 'FAILED', 'IDLE', 'TERMINATED', 'TERMINATING']]

### StateChangeReason
- **Type**: typing.Optional[str]


# SessionSummaryTypeDef

### SessionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.EngineVersionTypeDef]

### NotebookVersion
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.SessionStatusTypeDef]


# StartCalculationExecutionRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CalculationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.CalculationConfigurationTypeDef]

### CodeBlock
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartCalculationExecutionResponseTypeDef

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'CREATING', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartQueryExecutionInputTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### QueryExecutionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryExecutionContextTypeDef]

### ResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultConfigurationTypeDef]

### WorkGroup
- **Type**: typing.Optional[str]

### ExecutionParameters
- **Type**: typing.Optional[typing.Sequence[str]]

### ResultReuseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultReuseConfigurationTypeDef]


# StartQueryExecutionOutputTypeDef

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSessionRequestTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### EngineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.EngineConfigurationUnionTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### NotebookVersion
- **Type**: typing.Optional[str]

### SessionIdleTimeoutInMinutes
- **Type**: typing.Optional[int]

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartSessionResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['BUSY', 'CREATED', 'CREATING', 'DEGRADED', 'FAILED', 'IDLE', 'TERMINATED', 'TERMINATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopCalculationExecutionRequestTypeDef

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# StopCalculationExecutionResponseTypeDef

### State
- **Type**: typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'CREATING', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopQueryExecutionInputTypeDef

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# TableMetadataTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### LastAccessTime
- **Type**: typing.Optional[datetime.datetime]

### TableType
- **Type**: typing.Optional[str]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.ColumnTypeDef]]

### PartitionKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.ColumnTypeDef]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# TagResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TerminateSessionRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateSessionResponseTypeDef

### State
- **Type**: typing.Literal['BUSY', 'CREATED', 'CREATING', 'DEGRADED', 'FAILED', 'IDLE', 'TERMINATED', 'TERMINATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UnprocessedNamedQueryIdTypeDef

### NamedQueryId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UnprocessedPreparedStatementNameTypeDef

### StatementName
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UnprocessedQueryExecutionIdTypeDef

### QueryExecutionId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UntagResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCapacityReservationInputTypeDef

### TargetDpus
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateNamedQueryInputTypeDef

### NamedQueryId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateNotebookMetadataInputTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpdatePreparedStatementInputTypeDef

### StatementName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateWorkGroupInputTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ConfigurationUpdates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.WorkGroupConfigurationUpdatesTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# WorkGroupConfigurationTypeDef

### ResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultConfigurationTypeDef]

### EnforceWorkGroupConfiguration
- **Type**: typing.Optional[bool]

### PublishCloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### BytesScannedCutoffPerQuery
- **Type**: typing.Optional[int]

### RequesterPaysEnabled
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.EngineVersionTypeDef]

### AdditionalConfiguration
- **Type**: typing.Optional[str]

### ExecutionRole
- **Type**: typing.Optional[str]

### CustomerContentEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.CustomerContentEncryptionConfigurationTypeDef]

### EnableMinimumEncryptionConfiguration
- **Type**: typing.Optional[bool]

### IdentityCenterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.IdentityCenterConfigurationTypeDef]

### QueryResultsS3AccessGrantsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryResultsS3AccessGrantsConfigurationTypeDef]


# WorkGroupConfigurationUpdatesTypeDef

### EnforceWorkGroupConfiguration
- **Type**: typing.Optional[bool]

### ResultConfigurationUpdates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.ResultConfigurationUpdatesTypeDef]

### PublishCloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### BytesScannedCutoffPerQuery
- **Type**: typing.Optional[int]

### RemoveBytesScannedCutoffPerQuery
- **Type**: typing.Optional[bool]

### RequesterPaysEnabled
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.EngineVersionTypeDef]

### RemoveCustomerContentEncryptionConfiguration
- **Type**: typing.Optional[bool]

### AdditionalConfiguration
- **Type**: typing.Optional[str]

### ExecutionRole
- **Type**: typing.Optional[str]

### CustomerContentEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.CustomerContentEncryptionConfigurationTypeDef]

### EnableMinimumEncryptionConfiguration
- **Type**: typing.Optional[bool]

### QueryResultsS3AccessGrantsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryResultsS3AccessGrantsConfigurationTypeDef]


# WorkGroupSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Description
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### EngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.EngineVersionTypeDef]

### IdentityCenterApplicationArn
- **Type**: typing.Optional[str]


# WorkGroupTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.WorkGroupConfigurationTypeDef]

### Description
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### IdentityCenterApplicationArn
- **Type**: typing.Optional[str]



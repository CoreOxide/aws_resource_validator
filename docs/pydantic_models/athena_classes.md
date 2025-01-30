# athena_classes

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

# BatchGetNamedQueryInputRequestTypeDef

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


# BatchGetPreparedStatementInputRequestTypeDef

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


# BatchGetQueryExecutionInputRequestTypeDef

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


# CancelCapacityReservationInputRequestTypeDef

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

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogName
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### Precision
- **Type**: typing.Optional[int]

### Scale
- **Type**: typing.Optional[int]

### Nullable
- **Type**: typing.Optional[typing.Literal['NOT_NULL', 'NULLABLE', 'UNKNOWN']]

### CaseSensitive
- **Type**: typing.Optional[bool]


# ColumnTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[str]

### Comment
- **Type**: typing.Optional[str]


# CreateCapacityReservationInputRequestTypeDef

### TargetDpus
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.TagTypeDef]]


# CreateDataCatalogInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['GLUE', 'HIVE', 'LAMBDA']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.TagTypeDef]]


# CreateNamedQueryInputRequestTypeDef

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


# CreateNotebookInputRequestTypeDef

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


# CreatePreparedStatementInputRequestTypeDef

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


# CreatePresignedNotebookUrlRequestRequestTypeDef

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


# CreateWorkGroupInputRequestTypeDef

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

### CatalogName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['GLUE', 'HIVE', 'LAMBDA']]


# DataCatalogTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['GLUE', 'HIVE', 'LAMBDA']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# DeleteCapacityReservationInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataCatalogInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNamedQueryInputRequestTypeDef

### NamedQueryId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotebookInputRequestTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePreparedStatementInputRequestTypeDef

### StatementName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkGroupInputRequestTypeDef

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


# ExportNotebookInputRequestTypeDef

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


# GetCalculationExecutionCodeRequestRequestTypeDef

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


# GetCalculationExecutionRequestRequestTypeDef

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


# GetCalculationExecutionStatusRequestRequestTypeDef

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


# GetCapacityAssignmentConfigurationInputRequestTypeDef

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


# GetCapacityReservationInputRequestTypeDef

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


# GetDataCatalogInputRequestTypeDef

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


# GetDatabaseInputRequestTypeDef

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


# GetNamedQueryInputRequestTypeDef

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


# GetNotebookMetadataInputRequestTypeDef

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


# GetPreparedStatementInputRequestTypeDef

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


# GetQueryExecutionInputRequestTypeDef

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


# GetQueryResultsInputGetQueryResultsPaginateTypeDef

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# GetQueryResultsInputRequestTypeDef

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


# GetQueryRuntimeStatisticsInputRequestTypeDef

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


# GetSessionRequestRequestTypeDef

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


# GetSessionStatusRequestRequestTypeDef

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


# GetTableMetadataInputRequestTypeDef

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


# GetWorkGroupInputRequestTypeDef

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


# ImportNotebookInputRequestTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['IPYNB']
- **Required**: Yes

### Payload
- **Type**: typing.Optional[str]

### NotebookS3LocationUri
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# ImportNotebookOutputTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationDPUSizesInputRequestTypeDef

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


# ListCalculationExecutionsRequestRequestTypeDef

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


# ListCapacityReservationsInputRequestTypeDef

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


# ListDataCatalogsInputListDataCatalogsPaginateTypeDef

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListDataCatalogsInputRequestTypeDef

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


# ListDatabasesInputListDatabasesPaginateTypeDef

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListDatabasesInputRequestTypeDef

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


# ListEngineVersionsInputRequestTypeDef

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


# ListExecutorsRequestRequestTypeDef

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


# ListNamedQueriesInputListNamedQueriesPaginateTypeDef

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListNamedQueriesInputRequestTypeDef

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


# ListNotebookMetadataInputRequestTypeDef

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


# ListNotebookSessionsRequestRequestTypeDef

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


# ListPreparedStatementsInputRequestTypeDef

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


# ListQueryExecutionsInputListQueryExecutionsPaginateTypeDef

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListQueryExecutionsInputRequestTypeDef

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


# ListSessionsRequestRequestTypeDef

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


# ListTableMetadataInputListTableMetadataPaginateTypeDef

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


# ListTableMetadataInputRequestTypeDef

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


# ListTagsForResourceInputListTagsForResourcePaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputRequestTypeDef

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


# ListWorkGroupsInputRequestTypeDef

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

### NotebookId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### WorkGroup
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['IPYNB']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


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


# PutCapacityAssignmentConfigurationInputRequestTypeDef

### CapacityReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityAssignments
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.athena_classes.CapacityAssignmentTypeDef, aws_resource_validator.pydantic_models.athena_classes.CapacityAssignmentOutputTypeDef]]
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


# StartCalculationExecutionRequestRequestTypeDef

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


# StartQueryExecutionInputRequestTypeDef

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


# StartSessionRequestRequestTypeDef

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### EngineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.EngineConfigurationTypeDef'>
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


# StopCalculationExecutionRequestRequestTypeDef

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


# StopQueryExecutionInputRequestTypeDef

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


# TagResourceInputRequestTypeDef

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


# TerminateSessionRequestRequestTypeDef

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


# UntagResourceInputRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCapacityReservationInputRequestTypeDef

### TargetDpus
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDataCatalogInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['GLUE', 'HIVE', 'LAMBDA']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateNamedQueryInputRequestTypeDef

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


# UpdateNotebookInputRequestTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['IPYNB']
- **Required**: Yes

### SessionId
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpdateNotebookMetadataInputRequestTypeDef

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpdatePreparedStatementInputRequestTypeDef

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


# UpdateWorkGroupInputRequestTypeDef

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



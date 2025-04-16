# Athena Classes

# AclConfiguration

### S3AclOption
- **Type**: typing.Literal['BUCKET_OWNER_FULL_CONTROL']
- **Required**: Yes


# ApplicationDPUSizes

### ApplicationRuntimeId
- **Type**: typing.Optional[str]

### SupportedDPUSizes
- **Type**: typing.Optional[typing.List[int]]


# AthenaError

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

# BatchGetNamedQueryInput

### NamedQueryIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetNamedQueryOutput

### NamedQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.NamedQuery]
- **Required**: Yes

### UnprocessedNamedQueryIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.UnprocessedNamedQueryId]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetPreparedStatementInput

### PreparedStatementNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetPreparedStatementOutput

### PreparedStatements
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.PreparedStatement]
- **Required**: Yes

### UnprocessedPreparedStatementNames
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.UnprocessedPreparedStatementName]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetQueryExecutionInput

### QueryExecutionIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetQueryExecutionOutput

### QueryExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.QueryExecution]
- **Required**: Yes

### UnprocessedQueryExecutionIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.UnprocessedQueryExecutionId]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# CalculationConfiguration

### CodeBlock
- **Type**: typing.Optional[str]


# CalculationResult

### StdOutS3Uri
- **Type**: typing.Optional[str]

### StdErrorS3Uri
- **Type**: typing.Optional[str]

### ResultS3Uri
- **Type**: typing.Optional[str]

### ResultType
- **Type**: typing.Optional[str]


# CalculationStatistics

### DpuExecutionInMillis
- **Type**: typing.Optional[int]

### Progress
- **Type**: typing.Optional[str]


# CalculationStatus

### SubmissionDateTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionDateTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'CREATING', 'FAILED', 'QUEUED', 'RUNNING']]

### StateChangeReason
- **Type**: typing.Optional[str]


# CalculationSummary

### CalculationExecutionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.CalculationStatus]


# CancelCapacityReservationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CapacityAllocation

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


# CapacityAssignment

### WorkGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]


# CapacityAssignmentConfiguration

### CapacityReservationName
- **Type**: typing.Optional[str]

### CapacityAssignments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.CapacityAssignmentOutput]]


# CapacityAssignmentOutput

### WorkGroupNames
- **Type**: typing.Optional[typing.List[str]]


# CapacityAssignmentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityReservation

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.CapacityAllocation]

### LastSuccessfulAllocationTime
- **Type**: typing.Optional[datetime.datetime]


# Column

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCapacityReservationInput

### TargetDpus
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.Tag]]


# CreateDataCatalogOutput

### DataCatalog
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.DataCatalog'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNamedQueryInput

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


# CreateNamedQueryOutput

### NamedQueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNotebookInput

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateNotebookOutput

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePreparedStatementInput

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


# CreatePresignedNotebookUrlRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePresignedNotebookUrlResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkGroupInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.WorkGroupConfiguration]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.Tag]]


# CustomerContentEncryptionConfiguration

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes


# DataCatalog

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataCatalogSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Database

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# Datum

### VarCharValue
- **Type**: typing.Optional[str]


# DeleteCapacityReservationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataCatalogInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteCatalogOnly
- **Type**: typing.Optional[bool]


# DeleteDataCatalogOutput

### DataCatalog
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.DataCatalog'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNamedQueryInput

### NamedQueryId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotebookInput

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePreparedStatementInput

### StatementName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkGroupInput

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### RecursiveDeleteOption
- **Type**: typing.Optional[bool]


# EncryptionConfiguration

### EncryptionOption
- **Type**: typing.Literal['CSE_KMS', 'SSE_KMS', 'SSE_S3']
- **Required**: Yes

### KmsKey
- **Type**: typing.Optional[str]


# EngineConfiguration

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


# EngineConfigurationOutput

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


# EngineConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EngineVersion

### SelectedEngineVersion
- **Type**: typing.Optional[str]

### EffectiveEngineVersion
- **Type**: typing.Optional[str]


# ExecutorsSummary

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


# ExportNotebookInput

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportNotebookOutput

### NotebookMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.NotebookMetadata'>
- **Required**: Yes

### Payload
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# FilterDefinition

### Name
- **Type**: typing.Optional[str]


# GetCalculationExecutionCodeRequest

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculationExecutionCodeResponse

### CodeBlock
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetCalculationExecutionRequest

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculationExecutionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationStatus'>
- **Required**: Yes

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationStatistics'>
- **Required**: Yes

### Result
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetCalculationExecutionStatusRequest

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculationExecutionStatusResponse

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationStatus'>
- **Required**: Yes

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CalculationStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetCapacityAssignmentConfigurationInput

### CapacityReservationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCapacityAssignmentConfigurationOutput

### CapacityAssignmentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CapacityAssignmentConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetCapacityReservationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCapacityReservationOutput

### CapacityReservation
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.CapacityReservation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataCatalogInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]


# GetDataCatalogOutput

### DataCatalog
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.DataCatalog'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetDatabaseInput

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]


# GetDatabaseOutput

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.Database'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetNamedQueryInput

### NamedQueryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetNamedQueryOutput

### NamedQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.NamedQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetNotebookMetadataInput

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes


# GetNotebookMetadataOutput

### NotebookMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.NotebookMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetPreparedStatementInput

### StatementName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# GetPreparedStatementOutput

### PreparedStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.PreparedStatement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryExecutionInput

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryExecutionOutput

### QueryExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.QueryExecution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryResultsInput

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetQueryResultsInputPaginate

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfig]


# GetQueryResultsOutput

### UpdateCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResultSet
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResultSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetQueryRuntimeStatisticsInput

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryRuntimeStatisticsOutput

### QueryRuntimeStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.QueryRuntimeStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.EngineConfigurationOutput'>
- **Required**: Yes

### NotebookVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SessionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.SessionConfiguration'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.SessionStatus'>
- **Required**: Yes

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.SessionStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionStatusRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionStatusResponse

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.SessionStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableMetadataInput

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


# GetTableMetadataOutput

### TableMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.TableMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkGroupInput

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkGroupOutput

### WorkGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.WorkGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# IdentityCenterConfiguration

### EnableIdentityCenter
- **Type**: typing.Optional[bool]

### IdentityCenterInstanceArn
- **Type**: typing.Optional[str]


# ImportNotebookOutput

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# ListApplicationDPUSizesInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationDPUSizesOutput

### ApplicationDPUSizes
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.ApplicationDPUSizes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCalculationExecutionsRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### StateFilter
- **Type**: typing.Optional[typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'CREATING', 'FAILED', 'QUEUED', 'RUNNING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCalculationExecutionsResponse

### Calculations
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.CalculationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCapacityReservationsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCapacityReservationsOutput

### CapacityReservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.CapacityReservation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataCatalogsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListDataCatalogsInputPaginate

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfig]


# ListDataCatalogsOutput

### DataCatalogsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.DataCatalogSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatabasesInput

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListDatabasesInputPaginate

### CatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfig]


# ListDatabasesOutput

### DatabaseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.Database]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngineVersionsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEngineVersionsOutput

### EngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.EngineVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExecutorsRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutorStateFilter
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'FAILED', 'REGISTERED', 'TERMINATED', 'TERMINATING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExecutorsResponse

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutorsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.ExecutorsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNamedQueriesInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListNamedQueriesInputPaginate

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfig]


# ListNamedQueriesOutput

### NamedQueryIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookMetadataInput

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.FilterDefinition]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNotebookMetadataOutput

### NotebookMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.NotebookMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookSessionsRequest

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookSessionsResponse

### NotebookSessionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.NotebookSessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPreparedStatementsInput

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPreparedStatementsOutput

### PreparedStatements
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.PreparedStatementSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueryExecutionsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WorkGroup
- **Type**: typing.Optional[str]


# ListQueryExecutionsInputPaginate

### WorkGroup
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfig]


# ListQueryExecutionsOutput

### QueryExecutionIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSessionsRequest

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### StateFilter
- **Type**: typing.Optional[typing.Literal['BUSY', 'CREATED', 'CREATING', 'DEGRADED', 'FAILED', 'IDLE', 'TERMINATED', 'TERMINATING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSessionsResponse

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.SessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTableMetadataInput

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


# ListTableMetadataInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfig]


# ListTableMetadataOutput

### TableMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.TableMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceInputPaginate

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.PaginatorConfig]


# ListTagsForResourceOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkGroupsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkGroupsOutput

### WorkGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.athena_classes.WorkGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NamedQuery

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


# NotebookMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotebookSessionSummary

### SessionId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PreparedStatement

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


# PreparedStatementSummary

### StatementName
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# PutCapacityAssignmentConfigurationInput

### CapacityReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityAssignments
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.CapacityAssignmentUnion]
- **Required**: Yes


# QueryExecution

### QueryExecutionId
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]

### StatementType
- **Type**: typing.Optional[typing.Literal['DDL', 'DML', 'UTILITY']]

### ResultConfiguration
- **Type**: <class 'NoneType'>

### ResultReuseConfiguration
- **Type**: <class 'NoneType'>

### QueryExecutionContext
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryExecutionStatus]

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryExecutionStatistics]

### WorkGroup
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: <class 'NoneType'>

### ExecutionParameters
- **Type**: typing.Optional[typing.List[str]]

### SubstatementType
- **Type**: typing.Optional[str]

### QueryResultsS3AccessGrantsConfiguration
- **Type**: <class 'NoneType'>


# QueryExecutionContext

### Database
- **Type**: typing.Optional[str]

### Catalog
- **Type**: typing.Optional[str]


# QueryExecutionStatistics

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
- **Type**: <class 'NoneType'>


# QueryExecutionStatus

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']]

### StateChangeReason
- **Type**: typing.Optional[str]

### SubmissionDateTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionDateTime
- **Type**: typing.Optional[datetime.datetime]

### AthenaError
- **Type**: <class 'NoneType'>


# QueryResultsS3AccessGrantsConfiguration

### EnableS3AccessGrants
- **Type**: <class 'bool'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['DIRECTORY_IDENTITY']
- **Required**: Yes

### CreateUserLevelPrefix
- **Type**: typing.Optional[bool]


# QueryRuntimeStatistics

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryRuntimeStatisticsTimeline]

### Rows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryRuntimeStatisticsRows]

### OutputStage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryStage]


# QueryRuntimeStatisticsRows

### InputRows
- **Type**: typing.Optional[int]

### InputBytes
- **Type**: typing.Optional[int]

### OutputBytes
- **Type**: typing.Optional[int]

### OutputRows
- **Type**: typing.Optional[int]


# QueryRuntimeStatisticsTimeline

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


# QueryStage

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.QueryStagePlanNode]

### SubStages
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# QueryStagePlanNode

### Name
- **Type**: typing.Optional[str]

### Identifier
- **Type**: typing.Optional[str]

### Children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### RemoteSources
- **Type**: typing.Optional[typing.List[str]]


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


# ResultConfiguration

### OutputLocation
- **Type**: typing.Optional[str]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### ExpectedBucketOwner
- **Type**: typing.Optional[str]

### AclConfiguration
- **Type**: <class 'NoneType'>


# ResultConfigurationUpdates

### OutputLocation
- **Type**: typing.Optional[str]

### RemoveOutputLocation
- **Type**: typing.Optional[bool]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### RemoveEncryptionConfiguration
- **Type**: typing.Optional[bool]

### ExpectedBucketOwner
- **Type**: typing.Optional[str]

### RemoveExpectedBucketOwner
- **Type**: typing.Optional[bool]

### AclConfiguration
- **Type**: <class 'NoneType'>

### RemoveAclConfiguration
- **Type**: typing.Optional[bool]


# ResultReuseByAgeConfiguration

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxAgeInMinutes
- **Type**: typing.Optional[int]


# ResultReuseConfiguration

### ResultReuseByAgeConfiguration
- **Type**: <class 'NoneType'>


# ResultReuseInformation

### ReusedPreviousResult
- **Type**: <class 'bool'>
- **Required**: Yes


# ResultSet

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.Row]]

### ResultSetMetadata
- **Type**: <class 'NoneType'>


# ResultSetMetadata

### ColumnInfo
- **Type**: typing.Optional[typing.List[NoneType]]


# Row

### Data
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.Datum]]


# SessionConfiguration

### ExecutionRole
- **Type**: typing.Optional[str]

### WorkingDirectory
- **Type**: typing.Optional[str]

### IdleTimeoutSeconds
- **Type**: typing.Optional[int]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>


# SessionStatistics

### DpuExecutionInMillis
- **Type**: typing.Optional[int]


# SessionStatus

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


# SessionSummary

### SessionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: <class 'NoneType'>

### NotebookVersion
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.SessionStatus]


# StartCalculationExecutionRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CalculationConfiguration
- **Type**: <class 'NoneType'>

### CodeBlock
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartCalculationExecutionResponse

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'CREATING', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# StartQueryExecutionInput

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### QueryExecutionContext
- **Type**: <class 'NoneType'>

### ResultConfiguration
- **Type**: <class 'NoneType'>

### WorkGroup
- **Type**: typing.Optional[str]

### ExecutionParameters
- **Type**: typing.Optional[typing.Sequence[str]]

### ResultReuseConfiguration
- **Type**: <class 'NoneType'>


# StartQueryExecutionOutput

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# StartSessionRequest

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### EngineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.EngineConfigurationUnion'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### NotebookVersion
- **Type**: typing.Optional[str]

### SessionIdleTimeoutInMinutes
- **Type**: typing.Optional[int]

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartSessionResponse

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['BUSY', 'CREATED', 'CREATING', 'DEGRADED', 'FAILED', 'IDLE', 'TERMINATED', 'TERMINATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# StopCalculationExecutionRequest

### CalculationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# StopCalculationExecutionResponse

### State
- **Type**: typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'CREATING', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# StopQueryExecutionInput

### QueryExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# TableMetadata

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.Column]]

### PartitionKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.athena_classes.Column]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.athena_classes.Tag]
- **Required**: Yes


# TerminateSessionRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateSessionResponse

### State
- **Type**: typing.Literal['BUSY', 'CREATED', 'CREATING', 'DEGRADED', 'FAILED', 'IDLE', 'TERMINATED', 'TERMINATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.athena_classes.ResponseMetadata'>
- **Required**: Yes


# UnprocessedNamedQueryId

### NamedQueryId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UnprocessedPreparedStatementName

### StatementName
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UnprocessedQueryExecutionId

### QueryExecutionId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UntagResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCapacityReservationInput

### TargetDpus
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateNamedQueryInput

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


# UpdateNotebookMetadataInput

### NotebookId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpdatePreparedStatementInput

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


# UpdateWorkGroupInput

### WorkGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ConfigurationUpdates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.WorkGroupConfigurationUpdates]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# WorkGroup

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.athena_classes.WorkGroupConfiguration]

### Description
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### IdentityCenterApplicationArn
- **Type**: typing.Optional[str]


# WorkGroupConfiguration

### ResultConfiguration
- **Type**: <class 'NoneType'>

### EnforceWorkGroupConfiguration
- **Type**: typing.Optional[bool]

### PublishCloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### BytesScannedCutoffPerQuery
- **Type**: typing.Optional[int]

### RequesterPaysEnabled
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: <class 'NoneType'>

### AdditionalConfiguration
- **Type**: typing.Optional[str]

### ExecutionRole
- **Type**: typing.Optional[str]

### CustomerContentEncryptionConfiguration
- **Type**: <class 'NoneType'>

### EnableMinimumEncryptionConfiguration
- **Type**: typing.Optional[bool]

### IdentityCenterConfiguration
- **Type**: <class 'NoneType'>

### QueryResultsS3AccessGrantsConfiguration
- **Type**: <class 'NoneType'>


# WorkGroupConfigurationUpdates

### EnforceWorkGroupConfiguration
- **Type**: typing.Optional[bool]

### ResultConfigurationUpdates
- **Type**: <class 'NoneType'>

### PublishCloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### BytesScannedCutoffPerQuery
- **Type**: typing.Optional[int]

### RemoveBytesScannedCutoffPerQuery
- **Type**: typing.Optional[bool]

### RequesterPaysEnabled
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: <class 'NoneType'>

### RemoveCustomerContentEncryptionConfiguration
- **Type**: typing.Optional[bool]

### AdditionalConfiguration
- **Type**: typing.Optional[str]

### ExecutionRole
- **Type**: typing.Optional[str]

### CustomerContentEncryptionConfiguration
- **Type**: <class 'NoneType'>

### EnableMinimumEncryptionConfiguration
- **Type**: typing.Optional[bool]

### QueryResultsS3AccessGrantsConfiguration
- **Type**: <class 'NoneType'>


# WorkGroupSummary

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Description
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### EngineVersion
- **Type**: <class 'NoneType'>

### IdentityCenterApplicationArn
- **Type**: typing.Optional[str]



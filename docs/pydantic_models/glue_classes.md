# Glue Classes

# Action

### JobName
- **Type**: typing.Optional[str]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Timeout
- **Type**: typing.Optional[int]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: <class 'NoneType'>

### CrawlerName
- **Type**: typing.Optional[str]


# ActionOutput

### JobName
- **Type**: typing.Optional[str]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Timeout
- **Type**: typing.Optional[int]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: <class 'NoneType'>

### CrawlerName
- **Type**: typing.Optional[str]


# Aggregate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Groups
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### Aggs
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.AggregateOperation, aws_resource_validator.pydantic_models.glue.glue_classes.AggregateOperationOutput]]
- **Required**: Yes


# AggregateOperation

### Column
- **Type**: typing.List[str]
- **Required**: Yes

### AggFunc
- **Type**: typing.Literal['avg', 'count', 'countDistinct', 'first', 'kurtosis', 'last', 'max', 'min', 'skewness', 'stddev_pop', 'stddev_samp', 'sum', 'sumDistinct', 'var_pop', 'var_samp']
- **Required**: Yes


# AggregateOperationOutput

### Column
- **Type**: typing.List[str]
- **Required**: Yes

### AggFunc
- **Type**: typing.Literal['avg', 'count', 'countDistinct', 'first', 'kurtosis', 'last', 'max', 'min', 'skewness', 'stddev_pop', 'stddev_samp', 'sum', 'sumDistinct', 'var_pop', 'var_samp']
- **Required**: Yes


# AggregateOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Groups
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### Aggs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.AggregateOperationOutput]
- **Required**: Yes


# AllowedValue

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# AmazonRedshiftAdvancedOption

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AmazonRedshiftNodeData

### AccessType
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### CatalogDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### CatalogTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### CatalogRedshiftSchema
- **Type**: typing.Optional[str]

### CatalogRedshiftTable
- **Type**: typing.Optional[str]

### TempDir
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### AdvancedOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftAdvancedOption]]

### SampleQuery
- **Type**: typing.Optional[str]

### PreAction
- **Type**: typing.Optional[str]

### PostAction
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[str]

### TablePrefix
- **Type**: typing.Optional[str]

### Upsert
- **Type**: typing.Optional[bool]

### MergeAction
- **Type**: typing.Optional[str]

### MergeWhenMatched
- **Type**: typing.Optional[str]

### MergeWhenNotMatched
- **Type**: typing.Optional[str]

### MergeClause
- **Type**: typing.Optional[str]

### CrawlerConnection
- **Type**: typing.Optional[str]

### TableSchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Option]]

### StagingTable
- **Type**: typing.Optional[str]

### SelectedColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Option]]


# AmazonRedshiftNodeDataOutput

### AccessType
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### CatalogDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### CatalogTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### CatalogRedshiftSchema
- **Type**: typing.Optional[str]

### CatalogRedshiftTable
- **Type**: typing.Optional[str]

### TempDir
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### AdvancedOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftAdvancedOption]]

### SampleQuery
- **Type**: typing.Optional[str]

### PreAction
- **Type**: typing.Optional[str]

### PostAction
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[str]

### TablePrefix
- **Type**: typing.Optional[str]

### Upsert
- **Type**: typing.Optional[bool]

### MergeAction
- **Type**: typing.Optional[str]

### MergeWhenMatched
- **Type**: typing.Optional[str]

### MergeWhenNotMatched
- **Type**: typing.Optional[str]

### MergeClause
- **Type**: typing.Optional[str]

### CrawlerConnection
- **Type**: typing.Optional[str]

### TableSchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Option]]

### StagingTable
- **Type**: typing.Optional[str]

### SelectedColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Option]]


# AmazonRedshiftSource

### Name
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftNodeData, aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftNodeDataOutput, NoneType]


# AmazonRedshiftSourceOutput

### Name
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftNodeDataOutput]


# AmazonRedshiftTarget

### Name
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftNodeData, aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftNodeDataOutput, NoneType]

### Inputs
- **Type**: typing.Optional[typing.List[str]]


# AmazonRedshiftTargetOutput

### Name
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftNodeDataOutput]

### Inputs
- **Type**: typing.Optional[typing.List[str]]


# AnnotationError

### ProfileId
- **Type**: typing.Optional[str]

### StatisticId
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# ApplyMapping

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Mapping
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Mapping, aws_resource_validator.pydantic_models.glue.glue_classes.MappingOutput]]
- **Required**: Yes


# ApplyMappingOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Mapping
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.MappingOutput]
- **Required**: Yes


# ApplyMappingPaginator

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Mapping
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.MappingPaginator]
- **Required**: Yes


# AthenaConnectorSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionTable
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# AthenaConnectorSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionTable
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# AuditContext

### AdditionalAuditContext
- **Type**: typing.Optional[str]

### RequestedColumns
- **Type**: typing.Optional[typing.List[str]]

### AllColumnsRequested
- **Type**: typing.Optional[bool]


# AuthConfiguration

### AuthenticationType
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Property'>
- **Required**: Yes

### SecretArn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Property]

### OAuth2Properties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]]

### BasicAuthenticationProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]]

### CustomAuthenticationProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]]


# AuthenticationConfiguration

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['BASIC', 'CUSTOM', 'IAM', 'OAUTH2']]

### SecretArn
- **Type**: typing.Optional[str]

### OAuth2Properties
- **Type**: <class 'NoneType'>


# AuthenticationConfigurationInput

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['BASIC', 'CUSTOM', 'IAM', 'OAUTH2']]

### OAuth2Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.OAuth2PropertiesInput]

### SecretArn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### BasicAuthenticationCredentials
- **Type**: <class 'NoneType'>

### CustomAuthenticationCredentials
- **Type**: typing.Optional[typing.Dict[str, str]]


# AuthorizationCodeProperties

### AuthorizationCode
- **Type**: typing.Optional[str]

### RedirectUri
- **Type**: typing.Optional[str]


# BackfillError

### Code
- **Type**: typing.Optional[typing.Literal['ENCRYPTED_PARTITION_ERROR', 'INTERNAL_ERROR', 'INVALID_PARTITION_TYPE_DATA_ERROR', 'MISSING_PARTITION_VALUE_ERROR', 'UNSUPPORTED_PARTITION_CHARACTER_ERROR']]

### Partitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionValueListOutput]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthenticationCredentials

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# BasicCatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# BasicCatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# BatchCreatePartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionInputList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionInput]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchCreatePartitionResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteConnectionRequest

### ConnectionNameList
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchDeleteConnectionResponse

### Succeeded
- **Type**: typing.List[str]
- **Required**: Yes

### Errors
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.ErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeletePartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionsToDelete
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionValueList, aws_resource_validator.pydantic_models.glue.glue_classes.PartitionValueListOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchDeletePartitionResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TablesToDelete
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]


# BatchDeleteTableResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.TableError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteTableVersionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionIds
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchDeleteTableVersionResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.TableVersionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetBlueprintsRequest

### Names
- **Type**: typing.List[str]
- **Required**: Yes

### IncludeBlueprint
- **Type**: typing.Optional[bool]

### IncludeParameterSpec
- **Type**: typing.Optional[bool]


# BatchGetBlueprintsResponse

### Blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Blueprint]
- **Required**: Yes

### MissingBlueprints
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetCrawlersRequest

### CrawlerNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetCrawlersResponse

### Crawlers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Crawler]
- **Required**: Yes

### CrawlersNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetCustomEntityTypesRequest

### Names
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetCustomEntityTypesResponse

### CustomEntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CustomEntityType]
- **Required**: Yes

### CustomEntityTypesNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDataQualityResultRequest

### ResultIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetDataQualityResultResponse

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityResult]
- **Required**: Yes

### ResultsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDevEndpointsRequest

### DevEndpointNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetDevEndpointsResponse

### DevEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DevEndpoint]
- **Required**: Yes

### DevEndpointsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetJobsRequest

### JobNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Job]
- **Required**: Yes

### JobsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetPartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionsToGet
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionValueList, aws_resource_validator.pydantic_models.glue.glue_classes.PartitionValueListOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchGetPartitionResponse

### Partitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Partition]
- **Required**: Yes

### UnprocessedKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionValueListOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetTableOptimizerEntry

### catalogId
- **Type**: typing.Optional[str]

### databaseName
- **Type**: typing.Optional[str]

### tableName
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['compaction', 'orphan_file_deletion', 'retention']]


# BatchGetTableOptimizerError

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ErrorDetail]

### catalogId
- **Type**: typing.Optional[str]

### databaseName
- **Type**: typing.Optional[str]

### tableName
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['compaction', 'orphan_file_deletion', 'retention']]


# BatchGetTableOptimizerRequest

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BatchGetTableOptimizerEntry]
- **Required**: Yes


# BatchGetTableOptimizerResponse

### TableOptimizers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BatchTableOptimizer]
- **Required**: Yes

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BatchGetTableOptimizerError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetTriggersRequest

### TriggerNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetTriggersResponse

### Triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Trigger]
- **Required**: Yes

### TriggersNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetWorkflowsRequest

### Names
- **Type**: typing.List[str]
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]


# BatchGetWorkflowsResponse

### Workflows
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Workflow]
- **Required**: Yes

### MissingWorkflows
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutDataQualityStatisticAnnotationRequest

### InclusionAnnotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DatapointInclusionAnnotation]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# BatchPutDataQualityStatisticAnnotationResponse

### FailedInclusionAnnotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.AnnotationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchStopJobRunError

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: <class 'NoneType'>


# BatchStopJobRunRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobRunIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchStopJobRunResponse

### SuccessfulSubmissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BatchStopJobRunSuccessfulSubmission]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BatchStopJobRunError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BatchStopJobRunSuccessfulSubmission

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]


# BatchTableOptimizer

### catalogId
- **Type**: typing.Optional[str]

### databaseName
- **Type**: typing.Optional[str]

### tableName
- **Type**: typing.Optional[str]

### tableOptimizer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableOptimizer]


# BatchUpdatePartitionFailureEntry

### PartitionValueList
- **Type**: typing.Optional[typing.List[str]]

### ErrorDetail
- **Type**: <class 'NoneType'>


# BatchUpdatePartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BatchUpdatePartitionRequestEntry]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchUpdatePartitionRequestEntry

### PartitionValueList
- **Type**: typing.List[str]
- **Required**: Yes

### PartitionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.PartitionInput'>
- **Required**: Yes


# BatchUpdatePartitionResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BatchUpdatePartitionFailureEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# BinaryColumnStatisticsData

### MaximumLength
- **Type**: <class 'int'>
- **Required**: Yes

### AverageLength
- **Type**: <class 'float'>
- **Required**: Yes

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes


# Blueprint

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### ParameterSpec
- **Type**: typing.Optional[str]

### BlueprintLocation
- **Type**: typing.Optional[str]

### BlueprintServiceLocation
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'FAILED', 'UPDATING']]

### ErrorMessage
- **Type**: typing.Optional[str]

### LastActiveDefinition
- **Type**: <class 'NoneType'>


# BlueprintDetails

### BlueprintName
- **Type**: typing.Optional[str]

### RunId
- **Type**: typing.Optional[str]


# BlueprintRun

### BlueprintName
- **Type**: typing.Optional[str]

### RunId
- **Type**: typing.Optional[str]

### WorkflowName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'ROLLING_BACK', 'RUNNING', 'SUCCEEDED']]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### CompletedOn
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]

### RollbackErrorMessage
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# BooleanColumnStatisticsData

### NumberOfTrues
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfFalses
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes


# CancelDataQualityRuleRecommendationRunRequest

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDataQualityRulesetEvaluationRunRequest

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMLTaskRunRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMLTaskRunResponse

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CancelStatementRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'int'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# Capabilities

### SupportedAuthenticationTypes
- **Type**: typing.List[typing.Literal['BASIC', 'CUSTOM', 'IAM', 'OAUTH2']]
- **Required**: Yes

### SupportedDataOperations
- **Type**: typing.List[typing.Literal['READ', 'WRITE']]
- **Required**: Yes

### SupportedComputeEnvironments
- **Type**: typing.List[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]
- **Required**: Yes


# Catalog

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### TargetRedshiftCatalog
- **Type**: <class 'NoneType'>

### FederatedCatalog
- **Type**: <class 'NoneType'>

### CatalogProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogPropertiesOutput]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissionsOutput]]

### CreateDatabaseDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissionsOutput]]


# CatalogDeltaSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalDeltaOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# CatalogDeltaSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalDeltaOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# CatalogEntry

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# CatalogHudiSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalHudiOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# CatalogHudiSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalHudiOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# CatalogImportStatus

### ImportCompleted
- **Type**: typing.Optional[bool]

### ImportTime
- **Type**: typing.Optional[datetime.datetime]

### ImportedBy
- **Type**: typing.Optional[str]


# CatalogInput

### Description
- **Type**: typing.Optional[str]

### FederatedCatalog
- **Type**: <class 'NoneType'>

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TargetRedshiftCatalog
- **Type**: <class 'NoneType'>

### CatalogProperties
- **Type**: <class 'NoneType'>

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissions, aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissionsOutput]]]

### CreateDatabaseDefaultPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissions, aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissionsOutput]]]


# CatalogKafkaSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### StreamingOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.KafkaStreamingSourceOptions, aws_resource_validator.pydantic_models.glue.glue_classes.KafkaStreamingSourceOptionsOutput, NoneType]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StreamingDataPreviewOptions]


# CatalogKafkaSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### StreamingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.KafkaStreamingSourceOptionsOutput]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StreamingDataPreviewOptions]


# CatalogKinesisSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### StreamingOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.KinesisStreamingSourceOptions, aws_resource_validator.pydantic_models.glue.glue_classes.KinesisStreamingSourceOptionsOutput, NoneType]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StreamingDataPreviewOptions]


# CatalogKinesisSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### StreamingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.KinesisStreamingSourceOptionsOutput]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StreamingDataPreviewOptions]


# CatalogProperties

### DataLakeAccessProperties
- **Type**: <class 'NoneType'>

### CustomProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# CatalogPropertiesOutput

### DataLakeAccessProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataLakeAccessPropertiesOutput]

### CustomProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# CatalogSchemaChangePolicy

### EnableUpdateCatalog
- **Type**: typing.Optional[bool]

### UpdateBehavior
- **Type**: typing.Optional[typing.Literal['LOG', 'UPDATE_IN_DATABASE']]


# CatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# CatalogTarget

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Tables
- **Type**: typing.List[str]
- **Required**: Yes

### ConnectionName
- **Type**: typing.Optional[str]

### EventQueueArn
- **Type**: typing.Optional[str]

### DlqEventQueueArn
- **Type**: typing.Optional[str]


# CatalogTargetOutput

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Tables
- **Type**: typing.List[str]
- **Required**: Yes

### ConnectionName
- **Type**: typing.Optional[str]

### EventQueueArn
- **Type**: typing.Optional[str]

### DlqEventQueueArn
- **Type**: typing.Optional[str]


# CheckSchemaVersionValidityInput

### DataFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'PROTOBUF']
- **Required**: Yes

### SchemaDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# CheckSchemaVersionValidityResponse

### Valid
- **Type**: <class 'bool'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# Classifier

### GrokClassifier
- **Type**: <class 'NoneType'>

### XMLClassifier
- **Type**: <class 'NoneType'>

### JsonClassifier
- **Type**: <class 'NoneType'>

### CsvClassifier
- **Type**: <class 'NoneType'>


# CloudWatchEncryption

### CloudWatchEncryptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SSE-KMS']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# CodeGenConfigurationNode

### AthenaConnectorSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.AthenaConnectorSource, aws_resource_validator.pydantic_models.glue.glue_classes.AthenaConnectorSourceOutput, NoneType]

### JDBCConnectorSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorSource, aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorSourceOutput, NoneType]

### SparkConnectorSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SparkConnectorSource, aws_resource_validator.pydantic_models.glue.glue_classes.SparkConnectorSourceOutput, NoneType]

### CatalogSource
- **Type**: <class 'NoneType'>

### RedshiftSource
- **Type**: <class 'NoneType'>

### S3CatalogSource
- **Type**: <class 'NoneType'>

### S3CsvSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3CsvSource, aws_resource_validator.pydantic_models.glue.glue_classes.S3CsvSourceOutput, NoneType]

### S3JsonSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3JsonSource, aws_resource_validator.pydantic_models.glue.glue_classes.S3JsonSourceOutput, NoneType]

### S3ParquetSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3ParquetSource, aws_resource_validator.pydantic_models.glue.glue_classes.S3ParquetSourceOutput, NoneType]

### RelationalCatalogSource
- **Type**: <class 'NoneType'>

### DynamoDBCatalogSource
- **Type**: <class 'NoneType'>

### JDBCConnectorTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorTarget, aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorTargetOutput, NoneType]

### SparkConnectorTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SparkConnectorTarget, aws_resource_validator.pydantic_models.glue.glue_classes.SparkConnectorTargetOutput, NoneType]

### CatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.BasicCatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.BasicCatalogTargetOutput, NoneType]

### RedshiftTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.RedshiftTarget, aws_resource_validator.pydantic_models.glue.glue_classes.RedshiftTargetOutput, NoneType]

### S3CatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogTargetOutput, NoneType]

### S3GlueParquetTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3GlueParquetTarget, aws_resource_validator.pydantic_models.glue.glue_classes.S3GlueParquetTargetOutput, NoneType]

### S3DirectTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectTarget, aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectTargetOutput, NoneType]

### ApplyMapping
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ApplyMapping, aws_resource_validator.pydantic_models.glue.glue_classes.ApplyMappingOutput, NoneType]

### SelectFields
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SelectFields, aws_resource_validator.pydantic_models.glue.glue_classes.SelectFieldsOutput, NoneType]

### DropFields
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DropFields, aws_resource_validator.pydantic_models.glue.glue_classes.DropFieldsOutput, NoneType]

### RenameField
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.RenameField, aws_resource_validator.pydantic_models.glue.glue_classes.RenameFieldOutput, NoneType]

### Spigot
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Spigot, aws_resource_validator.pydantic_models.glue.glue_classes.SpigotOutput, NoneType]

### Join
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Join, aws_resource_validator.pydantic_models.glue.glue_classes.JoinOutput, NoneType]

### SplitFields
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SplitFields, aws_resource_validator.pydantic_models.glue.glue_classes.SplitFieldsOutput, NoneType]

### SelectFromCollection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SelectFromCollection, aws_resource_validator.pydantic_models.glue.glue_classes.SelectFromCollectionOutput, NoneType]

### FillMissingValues
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.FillMissingValues, aws_resource_validator.pydantic_models.glue.glue_classes.FillMissingValuesOutput, NoneType]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Filter, aws_resource_validator.pydantic_models.glue.glue_classes.FilterOutput, NoneType]

### CustomCode
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CustomCode, aws_resource_validator.pydantic_models.glue.glue_classes.CustomCodeOutput, NoneType]

### SparkSQL
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SparkSQL, aws_resource_validator.pydantic_models.glue.glue_classes.SparkSQLOutput, NoneType]

### DirectKinesisSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DirectKinesisSource, aws_resource_validator.pydantic_models.glue.glue_classes.DirectKinesisSourceOutput, NoneType]

### DirectKafkaSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DirectKafkaSource, aws_resource_validator.pydantic_models.glue.glue_classes.DirectKafkaSourceOutput, NoneType]

### CatalogKinesisSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogKinesisSource, aws_resource_validator.pydantic_models.glue.glue_classes.CatalogKinesisSourceOutput, NoneType]

### CatalogKafkaSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogKafkaSource, aws_resource_validator.pydantic_models.glue.glue_classes.CatalogKafkaSourceOutput, NoneType]

### DropNullFields
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DropNullFields, aws_resource_validator.pydantic_models.glue.glue_classes.DropNullFieldsOutput, NoneType]

### Merge
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Merge, aws_resource_validator.pydantic_models.glue.glue_classes.MergeOutput, NoneType]

### Union
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.UnionType, aws_resource_validator.pydantic_models.glue.glue_classes.UnionOutput, NoneType]

### PIIDetection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.PIIDetection, aws_resource_validator.pydantic_models.glue.glue_classes.PIIDetectionOutput, NoneType]

### Aggregate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Aggregate, aws_resource_validator.pydantic_models.glue.glue_classes.AggregateOutput, NoneType]

### DropDuplicates
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DropDuplicates, aws_resource_validator.pydantic_models.glue.glue_classes.DropDuplicatesOutput, NoneType]

### GovernedCatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.GovernedCatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.GovernedCatalogTargetOutput, NoneType]

### GovernedCatalogSource
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerCatalogSource
- **Type**: <class 'NoneType'>

### MySQLCatalogSource
- **Type**: <class 'NoneType'>

### OracleSQLCatalogSource
- **Type**: <class 'NoneType'>

### PostgreSQLCatalogSource
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerCatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.MicrosoftSQLServerCatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.MicrosoftSQLServerCatalogTargetOutput, NoneType]

### MySQLCatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.MySQLCatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.MySQLCatalogTargetOutput, NoneType]

### OracleSQLCatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.OracleSQLCatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.OracleSQLCatalogTargetOutput, NoneType]

### PostgreSQLCatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.PostgreSQLCatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.PostgreSQLCatalogTargetOutput, NoneType]

### DynamicTransform
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DynamicTransform, aws_resource_validator.pydantic_models.glue.glue_classes.DynamicTransformOutput, NoneType]

### EvaluateDataQuality
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.EvaluateDataQuality, aws_resource_validator.pydantic_models.glue.glue_classes.EvaluateDataQualityOutput, NoneType]

### S3CatalogHudiSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogHudiSource, aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogHudiSourceOutput, NoneType]

### CatalogHudiSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogHudiSource, aws_resource_validator.pydantic_models.glue.glue_classes.CatalogHudiSourceOutput, NoneType]

### S3HudiSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiSource, aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiSourceOutput, NoneType]

### S3HudiCatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiCatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiCatalogTargetOutput, NoneType]

### S3HudiDirectTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiDirectTarget, aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiDirectTargetOutput, NoneType]

### DirectJDBCSource
- **Type**: <class 'NoneType'>

### S3CatalogDeltaSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogDeltaSource, aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogDeltaSourceOutput, NoneType]

### CatalogDeltaSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogDeltaSource, aws_resource_validator.pydantic_models.glue.glue_classes.CatalogDeltaSourceOutput, NoneType]

### S3DeltaSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaSource, aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaSourceOutput, NoneType]

### S3DeltaCatalogTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaCatalogTarget, aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaCatalogTargetOutput, NoneType]

### S3DeltaDirectTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaDirectTarget, aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaDirectTargetOutput, NoneType]

### AmazonRedshiftSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftSource, aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftSourceOutput, NoneType]

### AmazonRedshiftTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftTarget, aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftTargetOutput, NoneType]

### EvaluateDataQualityMultiFrame
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.EvaluateDataQualityMultiFrame, aws_resource_validator.pydantic_models.glue.glue_classes.EvaluateDataQualityMultiFrameOutput, NoneType]

### Recipe
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Recipe, aws_resource_validator.pydantic_models.glue.glue_classes.RecipeOutput, NoneType]

### SnowflakeSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeSource, aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeSourceOutput, NoneType]

### SnowflakeTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeTarget, aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeTargetOutput, NoneType]

### ConnectorDataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectorDataSource, aws_resource_validator.pydantic_models.glue.glue_classes.ConnectorDataSourceOutput, NoneType]

### ConnectorDataTarget
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectorDataTarget, aws_resource_validator.pydantic_models.glue.glue_classes.ConnectorDataTargetOutput, NoneType]


# CodeGenConfigurationNodeOutput

### AthenaConnectorSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AthenaConnectorSourceOutput]

### JDBCConnectorSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorSourceOutput]

### SparkConnectorSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SparkConnectorSourceOutput]

### CatalogSource
- **Type**: <class 'NoneType'>

### RedshiftSource
- **Type**: <class 'NoneType'>

### S3CatalogSource
- **Type**: <class 'NoneType'>

### S3CsvSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3CsvSourceOutput]

### S3JsonSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3JsonSourceOutput]

### S3ParquetSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3ParquetSourceOutput]

### RelationalCatalogSource
- **Type**: <class 'NoneType'>

### DynamoDBCatalogSource
- **Type**: <class 'NoneType'>

### JDBCConnectorTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorTargetOutput]

### SparkConnectorTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SparkConnectorTargetOutput]

### CatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.BasicCatalogTargetOutput]

### RedshiftTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RedshiftTargetOutput]

### S3CatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogTargetOutput]

### S3GlueParquetTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3GlueParquetTargetOutput]

### S3DirectTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectTargetOutput]

### ApplyMapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ApplyMappingOutput]

### SelectFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SelectFieldsOutput]

### DropFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DropFieldsOutput]

### RenameField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RenameFieldOutput]

### Spigot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SpigotOutput]

### Join
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JoinOutput]

### SplitFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SplitFieldsOutput]

### SelectFromCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SelectFromCollectionOutput]

### FillMissingValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.FillMissingValuesOutput]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.FilterOutput]

### CustomCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CustomCodeOutput]

### SparkSQL
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SparkSQLOutput]

### DirectKinesisSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectKinesisSourceOutput]

### DirectKafkaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectKafkaSourceOutput]

### CatalogKinesisSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogKinesisSourceOutput]

### CatalogKafkaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogKafkaSourceOutput]

### DropNullFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DropNullFieldsOutput]

### Merge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.MergeOutput]

### Union
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.UnionOutput]

### PIIDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PIIDetectionOutput]

### Aggregate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AggregateOutput]

### DropDuplicates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DropDuplicatesOutput]

### GovernedCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.GovernedCatalogTargetOutput]

### GovernedCatalogSource
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerCatalogSource
- **Type**: <class 'NoneType'>

### MySQLCatalogSource
- **Type**: <class 'NoneType'>

### OracleSQLCatalogSource
- **Type**: <class 'NoneType'>

### PostgreSQLCatalogSource
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.MicrosoftSQLServerCatalogTargetOutput]

### MySQLCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.MySQLCatalogTargetOutput]

### OracleSQLCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.OracleSQLCatalogTargetOutput]

### PostgreSQLCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PostgreSQLCatalogTargetOutput]

### DynamicTransform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DynamicTransformOutput]

### EvaluateDataQuality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.EvaluateDataQualityOutput]

### S3CatalogHudiSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogHudiSourceOutput]

### CatalogHudiSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogHudiSourceOutput]

### S3HudiSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiSourceOutput]

### S3HudiCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiCatalogTargetOutput]

### S3HudiDirectTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiDirectTargetOutput]

### DirectJDBCSource
- **Type**: <class 'NoneType'>

### S3CatalogDeltaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogDeltaSourceOutput]

### CatalogDeltaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogDeltaSourceOutput]

### S3DeltaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaSourceOutput]

### S3DeltaCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaCatalogTargetOutput]

### S3DeltaDirectTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaDirectTargetOutput]

### AmazonRedshiftSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftSourceOutput]

### AmazonRedshiftTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftTargetOutput]

### EvaluateDataQualityMultiFrame
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.EvaluateDataQualityMultiFrameOutput]

### Recipe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RecipeOutput]

### SnowflakeSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeSourceOutput]

### SnowflakeTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeTargetOutput]

### ConnectorDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectorDataSourceOutput]

### ConnectorDataTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectorDataTargetOutput]


# CodeGenConfigurationNodePaginator

### AthenaConnectorSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AthenaConnectorSourceOutput]

### JDBCConnectorSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorSourceOutput]

### SparkConnectorSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SparkConnectorSourceOutput]

### CatalogSource
- **Type**: <class 'NoneType'>

### RedshiftSource
- **Type**: <class 'NoneType'>

### S3CatalogSource
- **Type**: <class 'NoneType'>

### S3CsvSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3CsvSourceOutput]

### S3JsonSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3JsonSourceOutput]

### S3ParquetSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3ParquetSourceOutput]

### RelationalCatalogSource
- **Type**: <class 'NoneType'>

### DynamoDBCatalogSource
- **Type**: <class 'NoneType'>

### JDBCConnectorTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorTargetOutput]

### SparkConnectorTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SparkConnectorTargetOutput]

### CatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.BasicCatalogTargetOutput]

### RedshiftTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RedshiftTargetOutput]

### S3CatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogTargetOutput]

### S3GlueParquetTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3GlueParquetTargetOutput]

### S3DirectTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectTargetOutput]

### ApplyMapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ApplyMappingPaginator]

### SelectFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SelectFieldsOutput]

### DropFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DropFieldsOutput]

### RenameField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RenameFieldOutput]

### Spigot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SpigotOutput]

### Join
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JoinOutput]

### SplitFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SplitFieldsOutput]

### SelectFromCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SelectFromCollectionOutput]

### FillMissingValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.FillMissingValuesOutput]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.FilterOutput]

### CustomCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CustomCodeOutput]

### SparkSQL
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SparkSQLOutput]

### DirectKinesisSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectKinesisSourceOutput]

### DirectKafkaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectKafkaSourceOutput]

### CatalogKinesisSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogKinesisSourceOutput]

### CatalogKafkaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogKafkaSourceOutput]

### DropNullFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DropNullFieldsOutput]

### Merge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.MergeOutput]

### Union
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.UnionOutput]

### PIIDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PIIDetectionOutput]

### Aggregate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AggregateOutput]

### DropDuplicates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DropDuplicatesOutput]

### GovernedCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.GovernedCatalogTargetOutput]

### GovernedCatalogSource
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerCatalogSource
- **Type**: <class 'NoneType'>

### MySQLCatalogSource
- **Type**: <class 'NoneType'>

### OracleSQLCatalogSource
- **Type**: <class 'NoneType'>

### PostgreSQLCatalogSource
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.MicrosoftSQLServerCatalogTargetOutput]

### MySQLCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.MySQLCatalogTargetOutput]

### OracleSQLCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.OracleSQLCatalogTargetOutput]

### PostgreSQLCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PostgreSQLCatalogTargetOutput]

### DynamicTransform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DynamicTransformOutput]

### EvaluateDataQuality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.EvaluateDataQualityOutput]

### S3CatalogHudiSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogHudiSourceOutput]

### CatalogHudiSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogHudiSourceOutput]

### S3HudiSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiSourceOutput]

### S3HudiCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiCatalogTargetOutput]

### S3HudiDirectTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3HudiDirectTargetOutput]

### DirectJDBCSource
- **Type**: <class 'NoneType'>

### S3CatalogDeltaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3CatalogDeltaSourceOutput]

### CatalogDeltaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogDeltaSourceOutput]

### S3DeltaSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaSourceOutput]

### S3DeltaCatalogTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaCatalogTargetOutput]

### S3DeltaDirectTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DeltaDirectTargetOutput]

### AmazonRedshiftSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftSourceOutput]

### AmazonRedshiftTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AmazonRedshiftTargetOutput]

### EvaluateDataQualityMultiFrame
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.EvaluateDataQualityMultiFrameOutput]

### Recipe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RecipeOutput]

### SnowflakeSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeSourceOutput]

### SnowflakeTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeTargetOutput]

### ConnectorDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectorDataSourceOutput]

### ConnectorDataTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectorDataTargetOutput]


# CodeGenEdge

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### TargetParameter
- **Type**: typing.Optional[str]


# CodeGenNode

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### Args
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenNodeArg]
- **Required**: Yes

### LineNumber
- **Type**: typing.Optional[int]


# CodeGenNodeArg

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Param
- **Type**: typing.Optional[bool]


# CodeGenNodeOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### Args
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenNodeArg]
- **Required**: Yes

### LineNumber
- **Type**: typing.Optional[int]


# Column

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[str]

### Comment
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ColumnError

### ColumnName
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ErrorDetail]


# ColumnImportance

### ColumnName
- **Type**: typing.Optional[str]

### Importance
- **Type**: typing.Optional[float]


# ColumnOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[str]

### Comment
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ColumnRowFilter

### ColumnName
- **Type**: typing.Optional[str]

### RowFilterExpression
- **Type**: typing.Optional[str]


# ColumnStatistics

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnType
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzedTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### StatisticsData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsData, aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsDataOutput]
- **Required**: Yes


# ColumnStatisticsData

### Type
- **Type**: typing.Literal['BINARY', 'BOOLEAN', 'DATE', 'DECIMAL', 'DOUBLE', 'LONG', 'STRING']
- **Required**: Yes

### BooleanColumnStatisticsData
- **Type**: <class 'NoneType'>

### DateColumnStatisticsData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DateColumnStatisticsData, aws_resource_validator.pydantic_models.glue.glue_classes.DateColumnStatisticsDataOutput, NoneType]

### DecimalColumnStatisticsData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DecimalColumnStatisticsData, aws_resource_validator.pydantic_models.glue.glue_classes.DecimalColumnStatisticsDataOutput, NoneType]

### DoubleColumnStatisticsData
- **Type**: <class 'NoneType'>

### LongColumnStatisticsData
- **Type**: <class 'NoneType'>

### StringColumnStatisticsData
- **Type**: <class 'NoneType'>

### BinaryColumnStatisticsData
- **Type**: <class 'NoneType'>


# ColumnStatisticsDataOutput

### Type
- **Type**: typing.Literal['BINARY', 'BOOLEAN', 'DATE', 'DECIMAL', 'DOUBLE', 'LONG', 'STRING']
- **Required**: Yes

### BooleanColumnStatisticsData
- **Type**: <class 'NoneType'>

### DateColumnStatisticsData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DateColumnStatisticsDataOutput]

### DecimalColumnStatisticsData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DecimalColumnStatisticsDataOutput]

### DoubleColumnStatisticsData
- **Type**: <class 'NoneType'>

### LongColumnStatisticsData
- **Type**: <class 'NoneType'>

### StringColumnStatisticsData
- **Type**: <class 'NoneType'>

### BinaryColumnStatisticsData
- **Type**: <class 'NoneType'>


# ColumnStatisticsError

### ColumnStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsOutput]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ErrorDetail]


# ColumnStatisticsOutput

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnType
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StatisticsData
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsDataOutput'>
- **Required**: Yes


# ColumnStatisticsTaskRun

### CustomerId
- **Type**: typing.Optional[str]

### ColumnStatisticsTaskRunId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### ColumnNameList
- **Type**: typing.Optional[typing.List[str]]

### CatalogID
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### SampleSize
- **Type**: typing.Optional[float]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### WorkerType
- **Type**: typing.Optional[str]

### ComputationType
- **Type**: typing.Optional[typing.Literal['FULL', 'INCREMENTAL']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'SUCCEEDED']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]

### DPUSeconds
- **Type**: typing.Optional[float]


# ColumnStatisticsTaskSettings

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Schedule
- **Type**: <class 'NoneType'>

### ColumnNameList
- **Type**: typing.Optional[typing.List[str]]

### CatalogID
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### SampleSize
- **Type**: typing.Optional[float]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### ScheduleType
- **Type**: typing.Optional[typing.Literal['AUTO', 'CRON']]

### SettingSource
- **Type**: typing.Optional[typing.Literal['CATALOG', 'TABLE']]

### LastExecutionAttempt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ExecutionAttempt]


# CompactionMetrics

### IcebergMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.IcebergCompactionMetrics]


# ComputeEnvironmentConfiguration

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeEnvironment
- **Type**: typing.Literal['ATHENA', 'PYTHON', 'SPARK']
- **Required**: Yes

### SupportedAuthenticationTypes
- **Type**: typing.List[typing.Literal['BASIC', 'CUSTOM', 'IAM', 'OAUTH2']]
- **Required**: Yes

### ConnectionOptions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]
- **Required**: Yes

### ConnectionPropertyNameOverrides
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ConnectionOptionNameOverrides
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ConnectionPropertiesRequiredOverrides
- **Type**: typing.List[str]
- **Required**: Yes

### PhysicalConnectionPropertiesRequired
- **Type**: typing.Optional[bool]


# Condition

### LogicalOperator
- **Type**: typing.Optional[typing.Literal['EQUALS']]

### JobName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ERROR', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT', 'WAITING']]

### CrawlerName
- **Type**: typing.Optional[str]

### CrawlState
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'ERROR', 'FAILED', 'RUNNING', 'SUCCEEDED']]


# ConditionExpression

### Condition
- **Type**: <class 'str'>
- **Required**: Yes

### TargetColumn
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# ConfigurationObject

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]

### MinValue
- **Type**: typing.Optional[str]

### MaxValue
- **Type**: typing.Optional[str]


# ConfigurationObjectOutput

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]

### MinValue
- **Type**: typing.Optional[str]

### MaxValue
- **Type**: typing.Optional[str]


# ConfusionMatrix

### NumTruePositives
- **Type**: typing.Optional[int]

### NumFalsePositives
- **Type**: typing.Optional[int]

### NumTrueNegatives
- **Type**: typing.Optional[int]

### NumFalseNegatives
- **Type**: typing.Optional[int]


# Connection

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ConnectionType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']]

### MatchCriteria
- **Type**: typing.Optional[typing.List[str]]

### ConnectionProperties
- **Type**: typing.Optional[typing.Dict[typing.Literal['CLUSTER_IDENTIFIER', 'CONFIG_FILES', 'CONNECTION_URL', 'CONNECTOR_CLASS_NAME', 'CONNECTOR_TYPE', 'CONNECTOR_URL', 'CUSTOM_JDBC_CERT', 'CUSTOM_JDBC_CERT_STRING', 'DATABASE', 'ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD', 'ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD', 'ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD', 'ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD', 'ENCRYPTED_PASSWORD', 'ENDPOINT', 'ENDPOINT_TYPE', 'HOST', 'INSTANCE_ID', 'JDBC_CONNECTION_URL', 'JDBC_DRIVER_CLASS_NAME', 'JDBC_DRIVER_JAR_URI', 'JDBC_ENFORCE_SSL', 'JDBC_ENGINE', 'JDBC_ENGINE_VERSION', 'KAFKA_BOOTSTRAP_SERVERS', 'KAFKA_CLIENT_KEYSTORE', 'KAFKA_CLIENT_KEYSTORE_PASSWORD', 'KAFKA_CLIENT_KEY_PASSWORD', 'KAFKA_CUSTOM_CERT', 'KAFKA_SASL_GSSAPI_KEYTAB', 'KAFKA_SASL_GSSAPI_KRB5_CONF', 'KAFKA_SASL_GSSAPI_PRINCIPAL', 'KAFKA_SASL_GSSAPI_SERVICE', 'KAFKA_SASL_MECHANISM', 'KAFKA_SASL_PLAIN_PASSWORD', 'KAFKA_SASL_PLAIN_USERNAME', 'KAFKA_SASL_SCRAM_PASSWORD', 'KAFKA_SASL_SCRAM_SECRETS_ARN', 'KAFKA_SASL_SCRAM_USERNAME', 'KAFKA_SKIP_CUSTOM_CERT_VALIDATION', 'KAFKA_SSL_ENABLED', 'PASSWORD', 'PORT', 'REGION', 'ROLE_ARN', 'SECRET_ID', 'SKIP_CUSTOM_JDBC_CERT_VALIDATION', 'USERNAME', 'WORKGROUP_NAME'], str]]

### SparkProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### AthenaProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### PythonProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### PhysicalConnectionRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PhysicalConnectionRequirementsOutput]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedBy
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'READY']]

### StatusReason
- **Type**: typing.Optional[str]

### LastConnectionValidationTime
- **Type**: typing.Optional[datetime.datetime]

### AuthenticationConfiguration
- **Type**: <class 'NoneType'>

### ConnectionSchemaVersion
- **Type**: typing.Optional[int]

### CompatibleComputeEnvironments
- **Type**: typing.Optional[typing.List[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]]


# ConnectionInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']
- **Required**: Yes

### ConnectionProperties
- **Type**: typing.Dict[typing.Literal['CLUSTER_IDENTIFIER', 'CONFIG_FILES', 'CONNECTION_URL', 'CONNECTOR_CLASS_NAME', 'CONNECTOR_TYPE', 'CONNECTOR_URL', 'CUSTOM_JDBC_CERT', 'CUSTOM_JDBC_CERT_STRING', 'DATABASE', 'ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD', 'ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD', 'ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD', 'ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD', 'ENCRYPTED_PASSWORD', 'ENDPOINT', 'ENDPOINT_TYPE', 'HOST', 'INSTANCE_ID', 'JDBC_CONNECTION_URL', 'JDBC_DRIVER_CLASS_NAME', 'JDBC_DRIVER_JAR_URI', 'JDBC_ENFORCE_SSL', 'JDBC_ENGINE', 'JDBC_ENGINE_VERSION', 'KAFKA_BOOTSTRAP_SERVERS', 'KAFKA_CLIENT_KEYSTORE', 'KAFKA_CLIENT_KEYSTORE_PASSWORD', 'KAFKA_CLIENT_KEY_PASSWORD', 'KAFKA_CUSTOM_CERT', 'KAFKA_SASL_GSSAPI_KEYTAB', 'KAFKA_SASL_GSSAPI_KRB5_CONF', 'KAFKA_SASL_GSSAPI_PRINCIPAL', 'KAFKA_SASL_GSSAPI_SERVICE', 'KAFKA_SASL_MECHANISM', 'KAFKA_SASL_PLAIN_PASSWORD', 'KAFKA_SASL_PLAIN_USERNAME', 'KAFKA_SASL_SCRAM_PASSWORD', 'KAFKA_SASL_SCRAM_SECRETS_ARN', 'KAFKA_SASL_SCRAM_USERNAME', 'KAFKA_SKIP_CUSTOM_CERT_VALIDATION', 'KAFKA_SSL_ENABLED', 'PASSWORD', 'PORT', 'REGION', 'ROLE_ARN', 'SECRET_ID', 'SKIP_CUSTOM_JDBC_CERT_VALIDATION', 'USERNAME', 'WORKGROUP_NAME'], str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### MatchCriteria
- **Type**: typing.Optional[typing.List[str]]

### SparkProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### AthenaProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### PythonProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### PhysicalConnectionRequirements
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.PhysicalConnectionRequirements, aws_resource_validator.pydantic_models.glue.glue_classes.PhysicalConnectionRequirementsOutput, NoneType]

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AuthenticationConfigurationInput]

### ValidateCredentials
- **Type**: typing.Optional[bool]

### ValidateForComputeEnvironments
- **Type**: typing.Optional[typing.List[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]]


# ConnectionPasswordEncryption

### ReturnConnectionPasswordEncrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### AwsKmsKeyId
- **Type**: typing.Optional[str]


# ConnectionTypeBrief

### ConnectionType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']]

### Description
- **Type**: typing.Optional[str]

### Capabilities
- **Type**: <class 'NoneType'>


# ConnectionsList

### Connections
- **Type**: typing.Optional[typing.List[str]]


# ConnectionsListOutput

### Connections
- **Type**: typing.Optional[typing.List[str]]


# ConnectorDataSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema, aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]]


# ConnectorDataSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# ConnectorDataTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Inputs
- **Type**: typing.Optional[typing.List[str]]


# ConnectorDataTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Inputs
- **Type**: typing.Optional[typing.List[str]]


# Crawl

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'ERROR', 'FAILED', 'RUNNING', 'SUCCEEDED']]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### CompletedOn
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]

### LogGroup
- **Type**: typing.Optional[str]

### LogStream
- **Type**: typing.Optional[str]


# Crawler

### Name
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CrawlerTargetsOutput]

### DatabaseName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Classifiers
- **Type**: typing.Optional[typing.List[str]]

### RecrawlPolicy
- **Type**: <class 'NoneType'>

### SchemaChangePolicy
- **Type**: <class 'NoneType'>

### LineageConfiguration
- **Type**: <class 'NoneType'>

### State
- **Type**: typing.Optional[typing.Literal['READY', 'RUNNING', 'STOPPING']]

### TablePrefix
- **Type**: typing.Optional[str]

### Schedule
- **Type**: <class 'NoneType'>

### CrawlElapsedTime
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### LastCrawl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.LastCrawlInfo]

### Version
- **Type**: typing.Optional[int]

### Configuration
- **Type**: typing.Optional[str]

### CrawlerSecurityConfiguration
- **Type**: typing.Optional[str]

### LakeFormationConfiguration
- **Type**: <class 'NoneType'>


# CrawlerHistory

### CrawlId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'STOPPED']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Summary
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### LogGroup
- **Type**: typing.Optional[str]

### LogStream
- **Type**: typing.Optional[str]

### MessagePrefix
- **Type**: typing.Optional[str]

### DPUHour
- **Type**: typing.Optional[float]


# CrawlerMetrics

### CrawlerName
- **Type**: typing.Optional[str]

### TimeLeftSeconds
- **Type**: typing.Optional[float]

### StillEstimating
- **Type**: typing.Optional[bool]

### LastRuntimeSeconds
- **Type**: typing.Optional[float]

### MedianRuntimeSeconds
- **Type**: typing.Optional[float]

### TablesCreated
- **Type**: typing.Optional[int]

### TablesUpdated
- **Type**: typing.Optional[int]

### TablesDeleted
- **Type**: typing.Optional[int]


# CrawlerNodeDetails

### Crawls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Crawl]]


# CrawlerTargets

### S3Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.S3Target]]

### JdbcTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.JdbcTarget]]

### MongoDBTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.MongoDBTarget]]

### DynamoDBTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DynamoDBTarget]]

### CatalogTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogTarget]]

### DeltaTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DeltaTarget]]

### IcebergTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IcebergTarget]]

### HudiTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.HudiTarget]]


# CrawlerTargetsOutput

### S3Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.S3TargetOutput]]

### JdbcTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.JdbcTargetOutput]]

### MongoDBTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.MongoDBTarget]]

### DynamoDBTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DynamoDBTarget]]

### CatalogTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogTargetOutput]]

### DeltaTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DeltaTargetOutput]]

### IcebergTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IcebergTargetOutput]]

### HudiTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.HudiTargetOutput]]


# CrawlsFilter

### FieldName
- **Type**: typing.Optional[typing.Literal['CRAWL_ID', 'DPU_HOUR', 'END_TIME', 'START_TIME', 'STATE']]

### FilterOperator
- **Type**: typing.Optional[typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']]

### FieldValue
- **Type**: typing.Optional[str]


# CreateBlueprintRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BlueprintLocation
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateBlueprintResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCatalogRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.CatalogInput'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateClassifierRequest

### GrokClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CreateGrokClassifierRequest]

### XMLClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CreateXMLClassifierRequest]

### JsonClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CreateJsonClassifierRequest]

### CsvClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CreateCsvClassifierRequest]


# CreateColumnStatisticsTaskSettingsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Optional[str]

### ColumnNameList
- **Type**: typing.Optional[typing.List[str]]

### SampleSize
- **Type**: typing.Optional[float]

### CatalogID
- **Type**: typing.Optional[str]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConnectionRequest

### ConnectionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConnectionResponse

### CreateConnectionStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'READY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCrawlerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CrawlerTargets, aws_resource_validator.pydantic_models.glue.glue_classes.CrawlerTargetsOutput]
- **Required**: Yes

### DatabaseName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### Classifiers
- **Type**: typing.Optional[typing.List[str]]

### TablePrefix
- **Type**: typing.Optional[str]

### SchemaChangePolicy
- **Type**: <class 'NoneType'>

### RecrawlPolicy
- **Type**: <class 'NoneType'>

### LineageConfiguration
- **Type**: <class 'NoneType'>

### LakeFormationConfiguration
- **Type**: <class 'NoneType'>

### Configuration
- **Type**: typing.Optional[str]

### CrawlerSecurityConfiguration
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCsvClassifierRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Delimiter
- **Type**: typing.Optional[str]

### QuoteSymbol
- **Type**: typing.Optional[str]

### ContainsHeader
- **Type**: typing.Optional[typing.Literal['ABSENT', 'PRESENT', 'UNKNOWN']]

### Header
- **Type**: typing.Optional[typing.List[str]]

### DisableValueTrimming
- **Type**: typing.Optional[bool]

### AllowSingleColumn
- **Type**: typing.Optional[bool]

### CustomDatatypeConfigured
- **Type**: typing.Optional[bool]

### CustomDatatypes
- **Type**: typing.Optional[typing.List[str]]

### Serde
- **Type**: typing.Optional[typing.Literal['LazySimpleSerDe', 'None', 'OpenCSVSerDe']]


# CreateCustomEntityTypeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### ContextWords
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCustomEntityTypeResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataQualityRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityTargetTable]

### DataQualitySecurityConfiguration
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# CreateDataQualityRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatabaseRequest

### DatabaseInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DatabaseInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDevEndpointRequest

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetId
- **Type**: typing.Optional[str]

### PublicKey
- **Type**: typing.Optional[str]

### PublicKeys
- **Type**: typing.Optional[typing.List[str]]

### NumberOfNodes
- **Type**: typing.Optional[int]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### GlueVersion
- **Type**: typing.Optional[str]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### ExtraPythonLibsS3Path
- **Type**: typing.Optional[str]

### ExtraJarsS3Path
- **Type**: typing.Optional[str]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDevEndpointResponse

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### YarnEndpointAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ZeppelinRemoteSparkInterpreterPort
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfNodes
- **Type**: <class 'int'>
- **Required**: Yes

### WorkerType
- **Type**: typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']
- **Required**: Yes

### GlueVersion
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfWorkers
- **Type**: <class 'int'>
- **Required**: Yes

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ExtraPythonLibsS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### ExtraJarsS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Arguments
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGrokClassifierRequest

### Classification
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GrokPattern
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPatterns
- **Type**: typing.Optional[str]


# CreateIntegrationRequest

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DataFilter
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### AdditionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Tag]]


# CreateIntegrationResourcePropertyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: <class 'NoneType'>

### TargetProcessingProperties
- **Type**: <class 'NoneType'>


# CreateIntegrationResourcePropertyResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SourceProcessingProperties'>
- **Required**: Yes

### TargetProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TargetProcessingProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntegrationResponse

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalEncryptionContext
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Tag]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING', 'NEEDS_ATTENTION', 'SYNCING']
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IntegrationError]
- **Required**: Yes

### DataFilter
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntegrationTablePropertiesRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTableConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SourceTableConfig, aws_resource_validator.pydantic_models.glue.glue_classes.SourceTableConfigOutput, NoneType]

### TargetTableConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.TargetTableConfig, aws_resource_validator.pydantic_models.glue.glue_classes.TargetTableConfigOutput, NoneType]


# CreateJobRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Command
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.JobCommand'>
- **Required**: Yes

### JobMode
- **Type**: typing.Optional[typing.Literal['NOTEBOOK', 'SCRIPT', 'VISUAL']]

### JobRunQueuingEnabled
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### LogUri
- **Type**: typing.Optional[str]

### ExecutionProperty
- **Type**: <class 'NoneType'>

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### NonOverridableArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsList, aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsListOutput, NoneType]

### MaxRetries
- **Type**: typing.Optional[int]

### AllocatedCapacity
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[float]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### NotificationProperty
- **Type**: <class 'NoneType'>

### GlueVersion
- **Type**: typing.Optional[str]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### CodeGenConfigurationNodes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenConfigurationNode, aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenConfigurationNodeOutput]]]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### SourceControlDetails
- **Type**: <class 'NoneType'>

### MaintenanceWindow
- **Type**: typing.Optional[str]


# CreateJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJsonClassifierRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JsonPath
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMLTransformRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InputRecordTables
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.GlueTable, aws_resource_validator.pydantic_models.glue.glue_classes.GlueTableOutput]]
- **Required**: Yes

### Parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TransformParameters'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### GlueVersion
- **Type**: typing.Optional[str]

### MaxCapacity
- **Type**: typing.Optional[float]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxRetries
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TransformEncryption
- **Type**: <class 'NoneType'>


# CreateMLTransformResponse

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePartitionIndexRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionIndex
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.PartitionIndex'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreatePartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.PartitionInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreateRegistryInput

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRegistryResponse

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSchemaInput

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'PROTOBUF']
- **Required**: Yes

### RegistryId
- **Type**: <class 'NoneType'>

### Compatibility
- **Type**: typing.Optional[typing.Literal['BACKWARD', 'BACKWARD_ALL', 'DISABLED', 'FORWARD', 'FORWARD_ALL', 'FULL', 'FULL_ALL', 'NONE']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### SchemaDefinition
- **Type**: typing.Optional[str]


# CreateSchemaResponse

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'PROTOBUF']
- **Required**: Yes

### Compatibility
- **Type**: typing.Literal['BACKWARD', 'BACKWARD_ALL', 'DISABLED', 'FORWARD', 'FORWARD_ALL', 'FULL', 'FULL_ALL', 'NONE']
- **Required**: Yes

### SchemaCheckpoint
- **Type**: <class 'int'>
- **Required**: Yes

### LatestSchemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### NextSchemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### SchemaStatus
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'PENDING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersionStatus
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'FAILURE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScriptRequest

### DagNodes
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenNode, aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenNodeOutput]]]

### DagEdges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenEdge]]

### Language
- **Type**: typing.Optional[typing.Literal['PYTHON', 'SCALA']]


# CreateScriptResponse

### PythonScript
- **Type**: <class 'str'>
- **Required**: Yes

### ScalaCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecurityConfigurationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.EncryptionConfiguration, aws_resource_validator.pydantic_models.glue.glue_classes.EncryptionConfigurationOutput]
- **Required**: Yes


# CreateSecurityConfigurationResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSessionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Command
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SessionCommand'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### IdleTimeout
- **Type**: typing.Optional[int]

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsList, aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsListOutput, NoneType]

### MaxCapacity
- **Type**: typing.Optional[float]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### GlueVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestOrigin
- **Type**: typing.Optional[str]


# CreateSessionResponse

### Session
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Session'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTableOptimizerRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['compaction', 'orphan_file_deletion', 'retention']
- **Required**: Yes

### TableOptimizerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TableOptimizerConfiguration'>
- **Required**: Yes


# CreateTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TableInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PartitionIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionIndex]]

### TransactionId
- **Type**: typing.Optional[str]

### OpenTableFormatInput
- **Type**: <class 'NoneType'>


# CreateTriggerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['CONDITIONAL', 'EVENT', 'ON_DEMAND', 'SCHEDULED']
- **Required**: Yes

### Actions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Action, aws_resource_validator.pydantic_models.glue.glue_classes.ActionOutput]]
- **Required**: Yes

### WorkflowName
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### Predicate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Predicate, aws_resource_validator.pydantic_models.glue.glue_classes.PredicateOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### StartOnCreation
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### EventBatchingCondition
- **Type**: <class 'NoneType'>


# CreateTriggerResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUsageProfileRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ProfileConfiguration, aws_resource_validator.pydantic_models.glue.glue_classes.ProfileConfigurationOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateUsageProfileResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserDefinedFunctionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.UserDefinedFunctionInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreateWorkflowRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DefaultRunProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### MaxConcurrentRuns
- **Type**: typing.Optional[int]


# CreateWorkflowResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# CreateXMLClassifierRequest

### Classification
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RowTag
- **Type**: typing.Optional[str]


# CsvClassifier

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[int]

### Delimiter
- **Type**: typing.Optional[str]

### QuoteSymbol
- **Type**: typing.Optional[str]

### ContainsHeader
- **Type**: typing.Optional[typing.Literal['ABSENT', 'PRESENT', 'UNKNOWN']]

### Header
- **Type**: typing.Optional[typing.List[str]]

### DisableValueTrimming
- **Type**: typing.Optional[bool]

### AllowSingleColumn
- **Type**: typing.Optional[bool]

### CustomDatatypeConfigured
- **Type**: typing.Optional[bool]

### CustomDatatypes
- **Type**: typing.Optional[typing.List[str]]

### Serde
- **Type**: typing.Optional[typing.Literal['LazySimpleSerDe', 'None', 'OpenCSVSerDe']]


# CustomCode

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### ClassName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# CustomCodeOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### ClassName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# CustomEntityType

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### ContextWords
- **Type**: typing.Optional[typing.List[str]]


# DQResultsPublishingOptions

### EvaluationContext
- **Type**: typing.Optional[str]

### ResultsS3Prefix
- **Type**: typing.Optional[str]

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### ResultsPublishingEnabled
- **Type**: typing.Optional[bool]


# DQStopJobOnFailureOptions

### StopJobOnFailureTiming
- **Type**: typing.Optional[typing.Literal['AfterDataLoad', 'Immediate']]


# DataCatalogEncryptionSettings

### EncryptionAtRest
- **Type**: <class 'NoneType'>

### ConnectionPasswordEncryption
- **Type**: <class 'NoneType'>


# DataLakeAccessProperties

### DataLakeAccess
- **Type**: typing.Optional[bool]

### DataTransferRole
- **Type**: typing.Optional[str]

### KmsKey
- **Type**: typing.Optional[str]

### CatalogType
- **Type**: typing.Optional[str]


# DataLakeAccessPropertiesOutput

### DataLakeAccess
- **Type**: typing.Optional[bool]

### DataTransferRole
- **Type**: typing.Optional[str]

### KmsKey
- **Type**: typing.Optional[str]

### ManagedWorkgroupName
- **Type**: typing.Optional[str]

### ManagedWorkgroupStatus
- **Type**: typing.Optional[str]

### RedshiftDatabaseName
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### CatalogType
- **Type**: typing.Optional[str]


# DataLakePrincipal

### DataLakePrincipalIdentifier
- **Type**: typing.Optional[str]


# DataQualityAnalyzerResult

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EvaluationMessage
- **Type**: typing.Optional[str]

### EvaluatedMetrics
- **Type**: typing.Optional[typing.Dict[str, float]]


# DataQualityEncryption

### DataQualityEncryptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SSE-KMS']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# DataQualityEvaluationRunAdditionalRunOptions

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### ResultsS3Prefix
- **Type**: typing.Optional[str]

### CompositeRuleEvaluationMethod
- **Type**: typing.Optional[typing.Literal['COLUMN', 'ROW']]


# DataQualityMetricValues

### ActualValue
- **Type**: typing.Optional[float]

### ExpectedValue
- **Type**: typing.Optional[float]

### LowerLimit
- **Type**: typing.Optional[float]

### UpperLimit
- **Type**: typing.Optional[float]


# DataQualityObservation

### Description
- **Type**: typing.Optional[str]

### MetricBasedObservation
- **Type**: <class 'NoneType'>


# DataQualityResult

### ResultId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]

### RulesetName
- **Type**: typing.Optional[str]

### EvaluationContext
- **Type**: typing.Optional[str]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### CompletedOn
- **Type**: typing.Optional[datetime.datetime]

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]

### RulesetEvaluationRunId
- **Type**: typing.Optional[str]

### RuleResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityRuleResult]]

### AnalyzerResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityAnalyzerResult]]

### Observations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityObservation]]


# DataQualityResultDescription

### ResultId
- **Type**: typing.Optional[str]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]


# DataQualityResultFilterCriteria

### DataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DataSource, aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput, NoneType]

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]

### StartedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DataQualityRuleRecommendationRunDescription

### RunId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]


# DataQualityRuleRecommendationRunFilter

### DataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DataSource, aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]
- **Required**: Yes

### StartedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DataQualityRuleResult

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EvaluationMessage
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[typing.Literal['ERROR', 'FAIL', 'PASS']]

### EvaluatedMetrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### EvaluatedRule
- **Type**: typing.Optional[str]


# DataQualityRulesetEvaluationRunDescription

### RunId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]


# DataQualityRulesetEvaluationRunFilter

### DataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DataSource, aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]
- **Required**: Yes

### StartedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DataQualityRulesetFilterCriteria

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityTargetTable]


# DataQualityRulesetListDetails

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityTargetTable]

### RecommendationRunId
- **Type**: typing.Optional[str]

### RuleCount
- **Type**: typing.Optional[int]


# DataQualityTargetTable

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DataSource

### GlueTable
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.GlueTable, aws_resource_validator.pydantic_models.glue.glue_classes.GlueTableOutput]
- **Required**: Yes


# DataSourceOutput

### GlueTable
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.GlueTableOutput'>
- **Required**: Yes


# Database

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LocationUri
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissionsOutput]]

### TargetDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DatabaseIdentifier]

### CatalogId
- **Type**: typing.Optional[str]

### FederatedDatabase
- **Type**: <class 'NoneType'>


# DatabaseIdentifier

### CatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# DatabaseInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LocationUri
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissions, aws_resource_validator.pydantic_models.glue.glue_classes.PrincipalPermissionsOutput]]]

### TargetDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DatabaseIdentifier]

### FederatedDatabase
- **Type**: <class 'NoneType'>


# DatapointInclusionAnnotation

### ProfileId
- **Type**: typing.Optional[str]

### StatisticId
- **Type**: typing.Optional[str]

### InclusionAnnotation
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# Datatype

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes


# DateColumnStatisticsData

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaximumValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DateColumnStatisticsDataOutput

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Optional[datetime.datetime]

### MaximumValue
- **Type**: typing.Optional[datetime.datetime]


# DecimalColumnStatisticsData

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DecimalNumber, aws_resource_validator.pydantic_models.glue.glue_classes.DecimalNumberOutput, NoneType]

### MaximumValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DecimalNumber, aws_resource_validator.pydantic_models.glue.glue_classes.DecimalNumberOutput, NoneType]


# DecimalColumnStatisticsDataOutput

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DecimalNumberOutput]

### MaximumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DecimalNumberOutput]


# DecimalNumber

### UnscaledValue
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### Scale
- **Type**: <class 'int'>
- **Required**: Yes


# DecimalNumberOutput

### UnscaledValue
- **Type**: <class 'bytes'>
- **Required**: Yes

### Scale
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteBlueprintRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBlueprintResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCatalogRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClassifierRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteColumnStatisticsForPartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.List[str]
- **Required**: Yes

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteColumnStatisticsForTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteColumnStatisticsTaskSettingsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionRequest

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteCrawlerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomEntityTypeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomEntityTypeResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataQualityRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatabaseRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteDevEndpointRequest

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationRequest

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponse

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalEncryptionContext
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Tag]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING', 'NEEDS_ATTENTION', 'SYNCING']
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IntegrationError]
- **Required**: Yes

### DataFilter
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIntegrationTablePropertiesRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobResponse

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMLTransformRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMLTransformResponse

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePartitionIndexRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeletePartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteRegistryInput

### RegistryId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.RegistryId'>
- **Required**: Yes


# DeleteRegistryResponse

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### PolicyHashCondition
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# DeleteSchemaInput

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes


# DeleteSchemaResponse

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSchemaVersionsInput

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes

### Versions
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaVersionsResponse

### SchemaVersionErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SchemaVersionErrorItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSecurityConfigurationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSessionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# DeleteSessionResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTableOptimizerRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['compaction', 'orphan_file_deletion', 'retention']
- **Required**: Yes


# DeleteTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]


# DeleteTableVersionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteTriggerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTriggerResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUsageProfileRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserDefinedFunctionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteWorkflowRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DeltaTarget

### DeltaTables
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### WriteManifest
- **Type**: typing.Optional[bool]

### CreateNativeDeltaTable
- **Type**: typing.Optional[bool]


# DeltaTargetOutput

### DeltaTables
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### WriteManifest
- **Type**: typing.Optional[bool]

### CreateNativeDeltaTable
- **Type**: typing.Optional[bool]


# DescribeConnectionTypeRequest

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectionTypeResponse

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Capabilities'>
- **Required**: Yes

### ConnectionProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]
- **Required**: Yes

### ConnectionOptions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]
- **Required**: Yes

### AuthenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.AuthConfiguration'>
- **Required**: Yes

### ComputeEnvironmentConfigurations
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.ComputeEnvironmentConfiguration]
- **Required**: Yes

### PhysicalConnectionRequirements
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]
- **Required**: Yes

### AthenaConnectionProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]
- **Required**: Yes

### PythonConnectionProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]
- **Required**: Yes

### SparkConnectionProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.Property]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEntityRequest

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### EntityName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### DataStoreApiVersion
- **Type**: typing.Optional[str]


# DescribeEntityRequestPaginate

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### EntityName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### DataStoreApiVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# DescribeEntityResponse

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Field]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInboundIntegrationsRequest

### IntegrationArn
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### TargetArn
- **Type**: typing.Optional[str]


# DescribeInboundIntegrationsResponse

### InboundIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.InboundIntegration]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIntegrationsRequest

### IntegrationIdentifier
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IntegrationFilter]]


# DescribeIntegrationsResponse

### Integrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Integration]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# DevEndpoint

### EndpointName
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetId
- **Type**: typing.Optional[str]

### YarnEndpointAddress
- **Type**: typing.Optional[str]

### PrivateAddress
- **Type**: typing.Optional[str]

### ZeppelinRemoteSparkInterpreterPort
- **Type**: typing.Optional[int]

### PublicAddress
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### GlueVersion
- **Type**: typing.Optional[str]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### NumberOfNodes
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### ExtraPythonLibsS3Path
- **Type**: typing.Optional[str]

### ExtraJarsS3Path
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### LastUpdateStatus
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### PublicKey
- **Type**: typing.Optional[str]

### PublicKeys
- **Type**: typing.Optional[typing.List[str]]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]


# DevEndpointCustomLibraries

### ExtraPythonLibsS3Path
- **Type**: typing.Optional[str]

### ExtraJarsS3Path
- **Type**: typing.Optional[str]


# DirectJDBCSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: typing.Literal['mysql', 'oracle', 'postgresql', 'redshift', 'sqlserver']
- **Required**: Yes

### RedshiftTmpDir
- **Type**: typing.Optional[str]


# DirectKafkaSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.KafkaStreamingSourceOptions, aws_resource_validator.pydantic_models.glue.glue_classes.KafkaStreamingSourceOptionsOutput, NoneType]

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StreamingDataPreviewOptions]


# DirectKafkaSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.KafkaStreamingSourceOptionsOutput]

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StreamingDataPreviewOptions]


# DirectKinesisSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### StreamingOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.KinesisStreamingSourceOptions, aws_resource_validator.pydantic_models.glue.glue_classes.KinesisStreamingSourceOptionsOutput, NoneType]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StreamingDataPreviewOptions]


# DirectKinesisSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### StreamingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.KinesisStreamingSourceOptionsOutput]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StreamingDataPreviewOptions]


# DirectSchemaChangePolicy

### EnableUpdateCatalog
- **Type**: typing.Optional[bool]

### UpdateBehavior
- **Type**: typing.Optional[typing.Literal['LOG', 'UPDATE_IN_DATABASE']]

### Table
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]


# DoubleColumnStatisticsData

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Optional[float]

### MaximumValue
- **Type**: typing.Optional[float]


# DropDuplicates

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Columns
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# DropDuplicatesOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Columns
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# DropFields

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# DropFieldsOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# DropNullFields

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### NullCheckBoxList
- **Type**: <class 'NoneType'>

### NullTextList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.NullValueField]]


# DropNullFieldsOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### NullCheckBoxList
- **Type**: <class 'NoneType'>

### NullTextList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.NullValueField]]


# DynamicTransform

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TransformName
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.TransformConfigParameter, aws_resource_validator.pydantic_models.glue.glue_classes.TransformConfigParameterOutput]]]

### Version
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# DynamicTransformOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TransformName
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.TransformConfigParameterOutput]]

### Version
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# DynamoDBCatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# DynamoDBTarget

### Path
- **Type**: typing.Optional[str]

### scanAll
- **Type**: typing.Optional[bool]

### scanRate
- **Type**: typing.Optional[float]


# Edge

### SourceId
- **Type**: typing.Optional[str]

### DestinationId
- **Type**: typing.Optional[str]


# EncryptionAtRest

### CatalogEncryptionMode
- **Type**: typing.Literal['DISABLED', 'SSE-KMS', 'SSE-KMS-WITH-SERVICE-ROLE']
- **Required**: Yes

### SseAwsKmsKeyId
- **Type**: typing.Optional[str]

### CatalogEncryptionServiceRole
- **Type**: typing.Optional[str]


# EncryptionConfiguration

### S3Encryption
- **Type**: typing.Optional[typing.List[NoneType]]

### CloudWatchEncryption
- **Type**: <class 'NoneType'>

### JobBookmarksEncryption
- **Type**: <class 'NoneType'>

### DataQualityEncryption
- **Type**: <class 'NoneType'>


# EncryptionConfigurationOutput

### S3Encryption
- **Type**: typing.Optional[typing.List[NoneType]]

### CloudWatchEncryption
- **Type**: <class 'NoneType'>

### JobBookmarksEncryption
- **Type**: <class 'NoneType'>

### DataQualityEncryption
- **Type**: <class 'NoneType'>


# Entity

### EntityName
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### IsParentEntity
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### CustomProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ErrorDetail

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# ErrorDetails

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# EvaluateDataQuality

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### Output
- **Type**: typing.Optional[typing.Literal['EvaluationResults', 'PrimaryInput']]

### PublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DQResultsPublishingOptions]

### StopJobOnFailureOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DQStopJobOnFailureOptions]


# EvaluateDataQualityMultiFrame

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalDataSources
- **Type**: typing.Optional[typing.Dict[str, str]]

### PublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DQResultsPublishingOptions]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['observations.scope', 'performanceTuning.caching'], str]]

### StopJobOnFailureOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DQStopJobOnFailureOptions]


# EvaluateDataQualityMultiFrameOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalDataSources
- **Type**: typing.Optional[typing.Dict[str, str]]

### PublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DQResultsPublishingOptions]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['observations.scope', 'performanceTuning.caching'], str]]

### StopJobOnFailureOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DQStopJobOnFailureOptions]


# EvaluateDataQualityOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### Output
- **Type**: typing.Optional[typing.Literal['EvaluationResults', 'PrimaryInput']]

### PublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DQResultsPublishingOptions]

### StopJobOnFailureOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DQStopJobOnFailureOptions]


# EvaluationMetrics

### TransformType
- **Type**: typing.Literal['FIND_MATCHES']
- **Required**: Yes

### FindMatchesMetrics
- **Type**: <class 'NoneType'>


# EventBatchingCondition

### BatchSize
- **Type**: <class 'int'>
- **Required**: Yes

### BatchWindow
- **Type**: typing.Optional[int]


# ExecutionAttempt

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'STARTED']]

### ColumnStatisticsTaskRunId
- **Type**: typing.Optional[str]

### ExecutionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]


# ExecutionProperty

### MaxConcurrentRuns
- **Type**: typing.Optional[int]


# ExportLabelsTaskRunProperties

### OutputS3Path
- **Type**: typing.Optional[str]


# FederatedCatalog

### Identifier
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]


# FederatedDatabase

### Identifier
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]


# FederatedTable

### Identifier
- **Type**: typing.Optional[str]

### DatabaseIdentifier
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]


# Field

### FieldName
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### FieldType
- **Type**: typing.Optional[typing.Literal['ARRAY', 'BIGINT', 'BOOLEAN', 'BYTE', 'DATE', 'DECIMAL', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'MAP', 'SHORT', 'SMALLINT', 'STRING', 'STRUCT', 'TIMESTAMP']]

### IsPrimaryKey
- **Type**: typing.Optional[bool]

### IsNullable
- **Type**: typing.Optional[bool]

### IsRetrievable
- **Type**: typing.Optional[bool]

### IsFilterable
- **Type**: typing.Optional[bool]

### IsPartitionable
- **Type**: typing.Optional[bool]

### IsCreateable
- **Type**: typing.Optional[bool]

### IsUpdateable
- **Type**: typing.Optional[bool]

### IsUpsertable
- **Type**: typing.Optional[bool]

### IsDefaultOnCreate
- **Type**: typing.Optional[bool]

### SupportedValues
- **Type**: typing.Optional[typing.List[str]]

### SupportedFilterOperators
- **Type**: typing.Optional[typing.List[typing.Literal['BETWEEN', 'CONTAINS', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'NOT_EQUAL_TO', 'ORDER_BY']]]

### ParentField
- **Type**: typing.Optional[str]

### NativeDataType
- **Type**: typing.Optional[str]

### CustomProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# FillMissingValues

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### ImputedPath
- **Type**: <class 'str'>
- **Required**: Yes

### FilledPath
- **Type**: typing.Optional[str]


# FillMissingValuesOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### ImputedPath
- **Type**: <class 'str'>
- **Required**: Yes

### FilledPath
- **Type**: typing.Optional[str]


# Filter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### LogicalOperator
- **Type**: typing.Literal['AND', 'OR']
- **Required**: Yes

### Filters
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.FilterExpression, aws_resource_validator.pydantic_models.glue.glue_classes.FilterExpressionOutput]]
- **Required**: Yes


# FilterExpression

### Operation
- **Type**: typing.Literal['EQ', 'GT', 'GTE', 'ISNULL', 'LT', 'LTE', 'REGEX']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.FilterValue, aws_resource_validator.pydantic_models.glue.glue_classes.FilterValueOutput]]
- **Required**: Yes

### Negated
- **Type**: typing.Optional[bool]


# FilterExpressionOutput

### Operation
- **Type**: typing.Literal['EQ', 'GT', 'GTE', 'ISNULL', 'LT', 'LTE', 'REGEX']
- **Required**: Yes

### Values
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.FilterValueOutput]
- **Required**: Yes

### Negated
- **Type**: typing.Optional[bool]


# FilterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### LogicalOperator
- **Type**: typing.Literal['AND', 'OR']
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.FilterExpressionOutput]
- **Required**: Yes


# FilterValue

### Type
- **Type**: typing.Literal['COLUMNEXTRACTED', 'CONSTANT']
- **Required**: Yes

### Value
- **Type**: typing.List[str]
- **Required**: Yes


# FilterValueOutput

### Type
- **Type**: typing.Literal['COLUMNEXTRACTED', 'CONSTANT']
- **Required**: Yes

### Value
- **Type**: typing.List[str]
- **Required**: Yes


# FindMatchesMetrics

### AreaUnderPRCurve
- **Type**: typing.Optional[float]

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### F1
- **Type**: typing.Optional[float]

### ConfusionMatrix
- **Type**: <class 'NoneType'>

### ColumnImportances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnImportance]]


# FindMatchesParameters

### PrimaryKeyColumnName
- **Type**: typing.Optional[str]

### PrecisionRecallTradeoff
- **Type**: typing.Optional[float]

### AccuracyCostTradeoff
- **Type**: typing.Optional[float]

### EnforceProvidedLabels
- **Type**: typing.Optional[bool]


# FindMatchesTaskRunProperties

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]


# GetBlueprintRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeBlueprint
- **Type**: typing.Optional[bool]

### IncludeParameterSpec
- **Type**: typing.Optional[bool]


# GetBlueprintResponse

### Blueprint
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Blueprint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetBlueprintRunRequest

### BlueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBlueprintRunResponse

### BlueprintRun
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.BlueprintRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetBlueprintRunsRequest

### BlueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetBlueprintRunsResponse

### BlueprintRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BlueprintRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCatalogImportStatusRequest

### CatalogId
- **Type**: typing.Optional[str]


# GetCatalogImportStatusResponse

### ImportStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.CatalogImportStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetCatalogRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCatalogResponse

### Catalog
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Catalog'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetCatalogsRequest

### ParentCatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Recursive
- **Type**: typing.Optional[bool]

### IncludeRoot
- **Type**: typing.Optional[bool]


# GetCatalogsResponse

### CatalogList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Catalog]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetClassifierRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetClassifierResponse

### Classifier
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Classifier'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetClassifiersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetClassifiersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetClassifiersResponse

### Classifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Classifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetColumnStatisticsForPartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.List[str]
- **Required**: Yes

### ColumnNames
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetColumnStatisticsForPartitionResponse

### ColumnStatisticsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsOutput]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetColumnStatisticsForTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnNames
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetColumnStatisticsForTableResponse

### ColumnStatisticsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsOutput]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetColumnStatisticsTaskRunRequest

### ColumnStatisticsTaskRunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetColumnStatisticsTaskRunResponse

### ColumnStatisticsTaskRun
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsTaskRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetColumnStatisticsTaskRunsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetColumnStatisticsTaskRunsResponse

### ColumnStatisticsTaskRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsTaskRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetColumnStatisticsTaskSettingsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# GetColumnStatisticsTaskSettingsResponse

### ColumnStatisticsTaskSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsTaskSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### HidePassword
- **Type**: typing.Optional[bool]

### ApplyOverrideForComputeEnvironment
- **Type**: typing.Optional[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]


# GetConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectionsFilter

### MatchCriteria
- **Type**: typing.Optional[typing.List[str]]

### ConnectionType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']]

### ConnectionSchemaVersion
- **Type**: typing.Optional[int]


# GetConnectionsRequest

### CatalogId
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.GetConnectionsFilter]

### HidePassword
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetConnectionsRequestPaginate

### CatalogId
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.GetConnectionsFilter]

### HidePassword
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetConnectionsResponse

### ConnectionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Connection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCrawlerMetricsRequest

### CrawlerNameList
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCrawlerMetricsRequestPaginate

### CrawlerNameList
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetCrawlerMetricsResponse

### CrawlerMetricsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CrawlerMetrics]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCrawlerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCrawlerResponse

### Crawler
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Crawler'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetCrawlersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCrawlersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetCrawlersResponse

### Crawlers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Crawler]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCustomEntityTypeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomEntityTypeResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### ContextWords
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataCatalogEncryptionSettingsRequest

### CatalogId
- **Type**: typing.Optional[str]


# GetDataCatalogEncryptionSettingsResponse

### DataCatalogEncryptionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DataCatalogEncryptionSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataQualityModelRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### StatisticId
- **Type**: typing.Optional[str]


# GetDataQualityModelResponse

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### StartedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataQualityModelResultRequest

### StatisticId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityModelResultResponse

### CompletedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Model
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.StatisticModelResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataQualityResultRequest

### ResultId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityResultResponse

### ResultId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Score
- **Type**: <class 'float'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput'>
- **Required**: Yes

### RulesetName
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationContext
- **Type**: <class 'str'>
- **Required**: Yes

### StartedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### RulesetEvaluationRunId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityRuleResult]
- **Required**: Yes

### AnalyzerResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityAnalyzerResult]
- **Required**: Yes

### Observations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityObservation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataQualityRuleRecommendationRunRequest

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityRuleRecommendationRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfWorkers
- **Type**: <class 'int'>
- **Required**: Yes

### Timeout
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']
- **Required**: Yes

### ErrorString
- **Type**: <class 'str'>
- **Required**: Yes

### StartedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionTime
- **Type**: <class 'int'>
- **Required**: Yes

### RecommendedRuleset
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedRulesetName
- **Type**: <class 'str'>
- **Required**: Yes

### DataQualitySecurityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataQualityRulesetEvaluationRunRequest

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityRulesetEvaluationRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfWorkers
- **Type**: <class 'int'>
- **Required**: Yes

### Timeout
- **Type**: <class 'int'>
- **Required**: Yes

### AdditionalRunOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityEvaluationRunAdditionalRunOptions'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']
- **Required**: Yes

### ErrorString
- **Type**: <class 'str'>
- **Required**: Yes

### StartedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionTime
- **Type**: <class 'int'>
- **Required**: Yes

### RulesetNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResultIds
- **Type**: typing.List[str]
- **Required**: Yes

### AdditionalDataSources
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataQualityRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### TargetTable
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityTargetTable'>
- **Required**: Yes

### CreatedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RecommendationRunId
- **Type**: <class 'str'>
- **Required**: Yes

### DataQualitySecurityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDatabaseRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetDatabaseResponse

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Database'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDatabasesRequest

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FEDERATED', 'FOREIGN']]

### AttributesToGet
- **Type**: typing.Optional[typing.List[typing.Literal['NAME']]]


# GetDatabasesRequestPaginate

### CatalogId
- **Type**: typing.Optional[str]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FEDERATED', 'FOREIGN']]

### AttributesToGet
- **Type**: typing.Optional[typing.List[typing.Literal['NAME']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetDatabasesResponse

### DatabaseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Database]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDataflowGraphRequest

### PythonScript
- **Type**: typing.Optional[str]


# GetDataflowGraphResponse

### DagNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenNodeOutput]
- **Required**: Yes

### DagEdges
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenEdge]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDevEndpointRequest

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevEndpointResponse

### DevEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DevEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetDevEndpointsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetDevEndpointsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetDevEndpointsResponse

### DevEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DevEndpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetEntityRecordsRequest

### EntityName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: <class 'int'>
- **Required**: Yes

### ConnectionName
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### DataStoreApiVersion
- **Type**: typing.Optional[str]

### ConnectionOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### FilterPredicate
- **Type**: typing.Optional[str]

### OrderBy
- **Type**: typing.Optional[str]

### SelectedFields
- **Type**: typing.Optional[typing.List[str]]


# GetEntityRecordsResponse

### Records
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetIntegrationResourcePropertyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResourcePropertyResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SourceProcessingProperties'>
- **Required**: Yes

### TargetProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TargetProcessingProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetIntegrationTablePropertiesRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationTablePropertiesResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTableConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SourceTableConfigOutput'>
- **Required**: Yes

### TargetTableConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TargetTableConfigOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobBookmarkRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: typing.Optional[str]


# GetJobBookmarkResponse

### JobBookmarkEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.JobBookmarkEntry'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRunRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### PredecessorsIncluded
- **Type**: typing.Optional[bool]


# GetJobRunResponse

### JobRun
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.JobRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRunsRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetJobRunsRequestPaginate

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetJobRunsResponse

### JobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.JobRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetJobsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetJobsResponsePaginator

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.JobPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMLTaskRunRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMLTaskRunResponse

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']
- **Required**: Yes

### LogGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TaskRunProperties'>
- **Required**: Yes

### ErrorString
- **Type**: <class 'str'>
- **Required**: Yes

### StartedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionTime
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLTaskRunsRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TaskRunFilterCriteria]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TaskRunSortCriteria]


# GetMLTaskRunsResponse

### TaskRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.TaskRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMLTransformRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMLTransformResponse

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DELETING', 'NOT_READY', 'READY']
- **Required**: Yes

### CreatedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InputRecordTables
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueTableOutput]
- **Required**: Yes

### Parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TransformParameters'>
- **Required**: Yes

### EvaluationMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.EvaluationMetrics'>
- **Required**: Yes

### LabelCount
- **Type**: <class 'int'>
- **Required**: Yes

### Schema
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SchemaColumn]
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### GlueVersion
- **Type**: <class 'str'>
- **Required**: Yes

### MaxCapacity
- **Type**: <class 'float'>
- **Required**: Yes

### WorkerType
- **Type**: typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']
- **Required**: Yes

### NumberOfWorkers
- **Type**: <class 'int'>
- **Required**: Yes

### Timeout
- **Type**: <class 'int'>
- **Required**: Yes

### MaxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### TransformEncryption
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TransformEncryption'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLTransformsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TransformFilterCriteria]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TransformSortCriteria]


# GetMLTransformsResponse

### Transforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.MLTransform]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMappingRequest

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.CatalogEntry'>
- **Required**: Yes

### Sinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogEntry]]

### Location
- **Type**: <class 'NoneType'>


# GetMappingResponse

### Mapping
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.MappingEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetPartitionIndexesRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetPartitionIndexesRequestPaginate

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetPartitionIndexesResponse

### PartitionIndexDescriptorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PartitionIndexDescriptor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetPartitionResponse

### Partition
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Partition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetPartitionsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Segment
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### ExcludeColumnSchema
- **Type**: typing.Optional[bool]

### TransactionId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetPartitionsRequestPaginate

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[str]

### Segment
- **Type**: <class 'NoneType'>

### ExcludeColumnSchema
- **Type**: typing.Optional[bool]

### TransactionId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetPartitionsResponse

### Partitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Partition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPlanRequest

### Mapping
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.MappingEntry]
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.CatalogEntry'>
- **Required**: Yes

### Sinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogEntry]]

### Location
- **Type**: <class 'NoneType'>

### Language
- **Type**: typing.Optional[typing.Literal['PYTHON', 'SCALA']]

### AdditionalPlanOptionsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetPlanResponse

### PythonScript
- **Type**: <class 'str'>
- **Required**: Yes

### ScalaCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegistryInput

### RegistryId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.RegistryId'>
- **Required**: Yes


# GetRegistryResponse

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DELETING']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePoliciesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetResourcePoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetResourcePoliciesResponse

### GetResourcePoliciesResponseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GluePolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourcePolicyRequest

### ResourceArn
- **Type**: typing.Optional[str]


# GetResourcePolicyResponse

### PolicyInJson
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyHash
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaByDefinitionInput

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes

### SchemaDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaByDefinitionResponse

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'PROTOBUF']
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'FAILURE', 'PENDING']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaInput

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes


# GetSchemaResponse

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'PROTOBUF']
- **Required**: Yes

### Compatibility
- **Type**: typing.Literal['BACKWARD', 'BACKWARD_ALL', 'DISABLED', 'FORWARD', 'FORWARD_ALL', 'FULL', 'FULL_ALL', 'NONE']
- **Required**: Yes

### SchemaCheckpoint
- **Type**: <class 'int'>
- **Required**: Yes

### LatestSchemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### NextSchemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### SchemaStatus
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'PENDING']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaVersionInput

### SchemaId
- **Type**: <class 'NoneType'>

### SchemaVersionId
- **Type**: typing.Optional[str]

### SchemaVersionNumber
- **Type**: <class 'NoneType'>


# GetSchemaVersionResponse

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'PROTOBUF']
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'FAILURE', 'PENDING']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaVersionsDiffInput

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes

### FirstSchemaVersionNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaVersionNumber'>
- **Required**: Yes

### SecondSchemaVersionNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaVersionNumber'>
- **Required**: Yes

### SchemaDiffType
- **Type**: typing.Literal['SYNTAX_DIFF']
- **Required**: Yes


# GetSchemaVersionsDiffResponse

### Diff
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetSecurityConfigurationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSecurityConfigurationResponse

### SecurityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SecurityConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetSecurityConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetSecurityConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetSecurityConfigurationsResponse

### SecurityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SecurityConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSessionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# GetSessionResponse

### Session
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Session'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetStatementRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'int'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# GetStatementResponse

### Statement
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Statement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableOptimizerRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['compaction', 'orphan_file_deletion', 'retention']
- **Required**: Yes


# GetTableOptimizerResponse

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TableOptimizer
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TableOptimizer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### IncludeStatusDetails
- **Type**: typing.Optional[bool]


# GetTableResponse

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Table'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableVersionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# GetTableVersionResponse

### TableVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TableVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableVersionsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetTableVersionsRequestPaginate

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetTableVersionsResponse

### TableVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.TableVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTableVersionsResponsePaginator

### TableVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.TableVersionPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTablesRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### TransactionId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### IncludeStatusDetails
- **Type**: typing.Optional[bool]

### AttributesToGet
- **Type**: typing.Optional[typing.List[typing.Literal['NAME', 'TABLE_TYPE']]]


# GetTablesRequestPaginate

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### IncludeStatusDetails
- **Type**: typing.Optional[bool]

### AttributesToGet
- **Type**: typing.Optional[typing.List[typing.Literal['NAME', 'TABLE_TYPE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetTablesResponse

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Table]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTablesResponsePaginator

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.TablePaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTagsResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetTriggerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTriggerResponse

### Trigger
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Trigger'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetTriggersRequest

### NextToken
- **Type**: typing.Optional[str]

### DependentJobName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetTriggersRequestPaginate

### DependentJobName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetTriggersResponse

### Triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Trigger]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUnfilteredPartitionMetadataRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.List[str]
- **Required**: Yes

### SupportedPermissionTypes
- **Type**: typing.List[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]

### AuditContext
- **Type**: <class 'NoneType'>

### QuerySessionContext
- **Type**: <class 'NoneType'>


# GetUnfilteredPartitionMetadataResponse

### Partition
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Partition'>
- **Required**: Yes

### AuthorizedColumns
- **Type**: typing.List[str]
- **Required**: Yes

### IsRegisteredWithLakeFormation
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetUnfilteredPartitionsMetadataRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedPermissionTypes
- **Type**: typing.List[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[str]

### AuditContext
- **Type**: <class 'NoneType'>

### NextToken
- **Type**: typing.Optional[str]

### Segment
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### QuerySessionContext
- **Type**: <class 'NoneType'>


# GetUnfilteredPartitionsMetadataResponse

### UnfilteredPartitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.UnfilteredPartition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUnfilteredTableMetadataRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedPermissionTypes
- **Type**: typing.List[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]

### AuditContext
- **Type**: <class 'NoneType'>

### ParentResourceArn
- **Type**: typing.Optional[str]

### RootResourceArn
- **Type**: typing.Optional[str]

### SupportedDialect
- **Type**: <class 'NoneType'>

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DROP', 'INSERT', 'SELECT']]]

### QuerySessionContext
- **Type**: <class 'NoneType'>


# GetUnfilteredTableMetadataResponse

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Table'>
- **Required**: Yes

### AuthorizedColumns
- **Type**: typing.List[str]
- **Required**: Yes

### IsRegisteredWithLakeFormation
- **Type**: <class 'bool'>
- **Required**: Yes

### CellFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnRowFilter]
- **Required**: Yes

### QueryAuthorizationId
- **Type**: <class 'str'>
- **Required**: Yes

### IsMultiDialectView
- **Type**: <class 'bool'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### IsProtected
- **Type**: <class 'bool'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['ALL', 'ALTER', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DROP', 'INSERT', 'SELECT']]
- **Required**: Yes

### RowFilter
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetUsageProfileRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsageProfileResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ProfileConfigurationOutput'>
- **Required**: Yes

### CreatedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserDefinedFunctionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetUserDefinedFunctionResponse

### UserDefinedFunction
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.UserDefinedFunction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserDefinedFunctionsRequest

### Pattern
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetUserDefinedFunctionsRequestPaginate

### Pattern
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetUserDefinedFunctionsResponse

### UserDefinedFunctions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.UserDefinedFunction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetWorkflowRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]


# GetWorkflowResponse

### Workflow
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Workflow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowRunPropertiesRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowRunPropertiesResponse

### RunProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowRunRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]


# GetWorkflowRunResponse

### Run
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.WorkflowRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowRunsRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetWorkflowRunsRequestPaginate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# GetWorkflowRunsResponse

### Runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.WorkflowRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GluePolicy

### PolicyInJson
- **Type**: typing.Optional[str]

### PolicyHash
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]


# GlueSchema

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueStudioSchemaColumn]]


# GlueSchemaOutput

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueStudioSchemaColumn]]


# GlueStudioSchemaColumn

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[str]


# GlueTable

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# GlueTableOutput

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# GovernedCatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionPredicate
- **Type**: typing.Optional[str]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3SourceAdditionalOptions]


# GovernedCatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogSchemaChangePolicy]


# GovernedCatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogSchemaChangePolicy]


# GrokClassifier

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Classification
- **Type**: <class 'str'>
- **Required**: Yes

### GrokPattern
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[int]

### CustomPatterns
- **Type**: typing.Optional[str]


# HudiTarget

### Paths
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### MaximumTraversalDepth
- **Type**: typing.Optional[int]


# HudiTargetOutput

### Paths
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### MaximumTraversalDepth
- **Type**: typing.Optional[int]


# IcebergCompactionMetrics

### NumberOfBytesCompacted
- **Type**: typing.Optional[int]

### NumberOfFilesCompacted
- **Type**: typing.Optional[int]

### NumberOfDpus
- **Type**: typing.Optional[int]

### JobDurationInHour
- **Type**: typing.Optional[float]


# IcebergInput

### MetadataOperation
- **Type**: typing.Literal['CREATE']
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# IcebergOrphanFileDeletionConfiguration

### orphanFileRetentionPeriodInDays
- **Type**: typing.Optional[int]

### location
- **Type**: typing.Optional[str]


# IcebergOrphanFileDeletionMetrics

### NumberOfOrphanFilesDeleted
- **Type**: typing.Optional[int]

### NumberOfDpus
- **Type**: typing.Optional[int]

### JobDurationInHour
- **Type**: typing.Optional[float]


# IcebergRetentionConfiguration

### snapshotRetentionPeriodInDays
- **Type**: typing.Optional[int]

### numberOfSnapshotsToRetain
- **Type**: typing.Optional[int]

### cleanExpiredFiles
- **Type**: typing.Optional[bool]


# IcebergRetentionMetrics

### NumberOfDataFilesDeleted
- **Type**: typing.Optional[int]

### NumberOfManifestFilesDeleted
- **Type**: typing.Optional[int]

### NumberOfManifestListsDeleted
- **Type**: typing.Optional[int]

### NumberOfDpus
- **Type**: typing.Optional[int]

### JobDurationInHour
- **Type**: typing.Optional[float]


# IcebergTarget

### Paths
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### MaximumTraversalDepth
- **Type**: typing.Optional[int]


# IcebergTargetOutput

### Paths
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### MaximumTraversalDepth
- **Type**: typing.Optional[int]


# ImportCatalogToGlueRequest

### CatalogId
- **Type**: typing.Optional[str]


# ImportLabelsTaskRunProperties

### InputS3Path
- **Type**: typing.Optional[str]

### Replace
- **Type**: typing.Optional[bool]


# InboundIntegration

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING', 'NEEDS_ATTENTION', 'SYNCING']
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IntegrationError]]


# Integration

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING', 'NEEDS_ATTENTION', 'SYNCING']
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### AdditionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Tag]]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IntegrationError]]

### DataFilter
- **Type**: typing.Optional[str]


# IntegrationError

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# IntegrationFilter

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# IntegrationPartition

### FieldName
- **Type**: typing.Optional[str]

### FunctionSpec
- **Type**: typing.Optional[str]


# JDBCConnectorOptions

### FilterPredicate
- **Type**: typing.Optional[str]

### PartitionColumn
- **Type**: typing.Optional[str]

### LowerBound
- **Type**: typing.Optional[int]

### UpperBound
- **Type**: typing.Optional[int]

### NumPartitions
- **Type**: typing.Optional[int]

### JobBookmarkKeys
- **Type**: typing.Optional[typing.List[str]]

### JobBookmarkKeysSortOrder
- **Type**: typing.Optional[str]

### DataTypeMapping
- **Type**: typing.Optional[typing.Dict[typing.Literal['ARRAY', 'BIGINT', 'BINARY', 'BIT', 'BLOB', 'BOOLEAN', 'CHAR', 'CLOB', 'DATALINK', 'DATE', 'DECIMAL', 'DISTINCT', 'DOUBLE', 'FLOAT', 'INTEGER', 'JAVA_OBJECT', 'LONGNVARCHAR', 'LONGVARBINARY', 'LONGVARCHAR', 'NCHAR', 'NCLOB', 'NULL', 'NUMERIC', 'NVARCHAR', 'OTHER', 'REAL', 'REF', 'REF_CURSOR', 'ROWID', 'SMALLINT', 'SQLXML', 'STRUCT', 'TIME', 'TIMESTAMP', 'TIMESTAMP_WITH_TIMEZONE', 'TIME_WITH_TIMEZONE', 'TINYINT', 'VARBINARY', 'VARCHAR'], typing.Literal['BIGDECIMAL', 'BYTE', 'DATE', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'SHORT', 'STRING', 'TIMESTAMP']]]


# JDBCConnectorOptionsOutput

### FilterPredicate
- **Type**: typing.Optional[str]

### PartitionColumn
- **Type**: typing.Optional[str]

### LowerBound
- **Type**: typing.Optional[int]

### UpperBound
- **Type**: typing.Optional[int]

### NumPartitions
- **Type**: typing.Optional[int]

### JobBookmarkKeys
- **Type**: typing.Optional[typing.List[str]]

### JobBookmarkKeysSortOrder
- **Type**: typing.Optional[str]

### DataTypeMapping
- **Type**: typing.Optional[typing.Dict[typing.Literal['ARRAY', 'BIGINT', 'BINARY', 'BIT', 'BLOB', 'BOOLEAN', 'CHAR', 'CLOB', 'DATALINK', 'DATE', 'DECIMAL', 'DISTINCT', 'DOUBLE', 'FLOAT', 'INTEGER', 'JAVA_OBJECT', 'LONGNVARCHAR', 'LONGVARBINARY', 'LONGVARCHAR', 'NCHAR', 'NCLOB', 'NULL', 'NUMERIC', 'NVARCHAR', 'OTHER', 'REAL', 'REF', 'REF_CURSOR', 'ROWID', 'SMALLINT', 'SQLXML', 'STRUCT', 'TIME', 'TIMESTAMP', 'TIMESTAMP_WITH_TIMEZONE', 'TIME_WITH_TIMEZONE', 'TINYINT', 'VARBINARY', 'VARCHAR'], typing.Literal['BIGDECIMAL', 'BYTE', 'DATE', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'SHORT', 'STRING', 'TIMESTAMP']]]


# JDBCConnectorSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorOptions, aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorOptionsOutput, NoneType]

### ConnectionTable
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# JDBCConnectorSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JDBCConnectorOptionsOutput]

### ConnectionTable
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# JDBCConnectorTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionTable
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# JDBCConnectorTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionTable
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# JdbcTarget

### ConnectionName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### EnableAdditionalMetadata
- **Type**: typing.Optional[typing.List[typing.Literal['COMMENTS', 'RAWTYPES']]]


# JdbcTargetOutput

### ConnectionName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### EnableAdditionalMetadata
- **Type**: typing.Optional[typing.List[typing.Literal['COMMENTS', 'RAWTYPES']]]


# Job

### Name
- **Type**: typing.Optional[str]

### JobMode
- **Type**: typing.Optional[typing.Literal['NOTEBOOK', 'SCRIPT', 'VISUAL']]

### JobRunQueuingEnabled
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### LogUri
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### ExecutionProperty
- **Type**: <class 'NoneType'>

### Command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JobCommand]

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### NonOverridableArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsListOutput]

### MaxRetries
- **Type**: typing.Optional[int]

### AllocatedCapacity
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[float]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: <class 'NoneType'>

### GlueVersion
- **Type**: typing.Optional[str]

### CodeGenConfigurationNodes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenConfigurationNodeOutput]]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### SourceControlDetails
- **Type**: <class 'NoneType'>

### MaintenanceWindow
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]


# JobBookmarkEntry

### JobName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Run
- **Type**: typing.Optional[int]

### Attempt
- **Type**: typing.Optional[int]

### PreviousRunId
- **Type**: typing.Optional[str]

### RunId
- **Type**: typing.Optional[str]

### JobBookmark
- **Type**: typing.Optional[str]


# JobBookmarksEncryption

### JobBookmarksEncryptionMode
- **Type**: typing.Optional[typing.Literal['CSE-KMS', 'DISABLED']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# JobCommand

### Name
- **Type**: typing.Optional[str]

### ScriptLocation
- **Type**: typing.Optional[str]

### PythonVersion
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[str]


# JobNodeDetails

### JobRuns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.JobRun]]


# JobPaginator

### Name
- **Type**: typing.Optional[str]

### JobMode
- **Type**: typing.Optional[typing.Literal['NOTEBOOK', 'SCRIPT', 'VISUAL']]

### JobRunQueuingEnabled
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### LogUri
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### ExecutionProperty
- **Type**: <class 'NoneType'>

### Command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JobCommand]

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### NonOverridableArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsListOutput]

### MaxRetries
- **Type**: typing.Optional[int]

### AllocatedCapacity
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[float]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: <class 'NoneType'>

### GlueVersion
- **Type**: typing.Optional[str]

### CodeGenConfigurationNodes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenConfigurationNodePaginator]]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### SourceControlDetails
- **Type**: <class 'NoneType'>

### MaintenanceWindow
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]


# JobRun

### Id
- **Type**: typing.Optional[str]

### Attempt
- **Type**: typing.Optional[int]

### PreviousRunId
- **Type**: typing.Optional[str]

### TriggerName
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobMode
- **Type**: typing.Optional[typing.Literal['NOTEBOOK', 'SCRIPT', 'VISUAL']]

### JobRunQueuingEnabled
- **Type**: typing.Optional[bool]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### CompletedOn
- **Type**: typing.Optional[datetime.datetime]

### JobRunState
- **Type**: typing.Optional[typing.Literal['ERROR', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT', 'WAITING']]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### ErrorMessage
- **Type**: typing.Optional[str]

### PredecessorRuns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Predecessor]]

### AllocatedCapacity
- **Type**: typing.Optional[int]

### ExecutionTime
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[float]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### LogGroupName
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: <class 'NoneType'>

### GlueVersion
- **Type**: typing.Optional[str]

### DPUSeconds
- **Type**: typing.Optional[float]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### MaintenanceWindow
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]

### StateDetail
- **Type**: typing.Optional[str]


# JobUpdate

### JobMode
- **Type**: typing.Optional[typing.Literal['NOTEBOOK', 'SCRIPT', 'VISUAL']]

### JobRunQueuingEnabled
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### LogUri
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### ExecutionProperty
- **Type**: <class 'NoneType'>

### Command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JobCommand]

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### NonOverridableArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsList, aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsListOutput, NoneType]

### MaxRetries
- **Type**: typing.Optional[int]

### AllocatedCapacity
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[float]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: <class 'NoneType'>

### GlueVersion
- **Type**: typing.Optional[str]

### CodeGenConfigurationNodes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenConfigurationNode, aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenConfigurationNodeOutput]]]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### SourceControlDetails
- **Type**: <class 'NoneType'>

### MaintenanceWindow
- **Type**: typing.Optional[str]


# Join

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### JoinType
- **Type**: typing.Literal['equijoin', 'left', 'leftanti', 'leftsemi', 'outer', 'right']
- **Required**: Yes

### Columns
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.JoinColumn, aws_resource_validator.pydantic_models.glue.glue_classes.JoinColumnOutput]]
- **Required**: Yes


# JoinColumn

### From
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# JoinColumnOutput

### From
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# JoinOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### JoinType
- **Type**: typing.Literal['equijoin', 'left', 'leftanti', 'leftsemi', 'outer', 'right']
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.JoinColumnOutput]
- **Required**: Yes


# JsonClassifier

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JsonPath
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[int]


# KafkaStreamingSourceOptions

### BootstrapServers
- **Type**: typing.Optional[str]

### SecurityProtocol
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### TopicName
- **Type**: typing.Optional[str]

### Assign
- **Type**: typing.Optional[str]

### SubscribePattern
- **Type**: typing.Optional[str]

### Classification
- **Type**: typing.Optional[str]

### Delimiter
- **Type**: typing.Optional[str]

### StartingOffsets
- **Type**: typing.Optional[str]

### EndingOffsets
- **Type**: typing.Optional[str]

### PollTimeoutMs
- **Type**: typing.Optional[int]

### NumRetries
- **Type**: typing.Optional[int]

### RetryIntervalMs
- **Type**: typing.Optional[int]

### MaxOffsetsPerTrigger
- **Type**: typing.Optional[int]

### MinPartitions
- **Type**: typing.Optional[int]

### IncludeHeaders
- **Type**: typing.Optional[bool]

### AddRecordTimestamp
- **Type**: typing.Optional[str]

### EmitConsumerLagMetrics
- **Type**: typing.Optional[str]

### StartingTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# KafkaStreamingSourceOptionsOutput

### BootstrapServers
- **Type**: typing.Optional[str]

### SecurityProtocol
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### TopicName
- **Type**: typing.Optional[str]

### Assign
- **Type**: typing.Optional[str]

### SubscribePattern
- **Type**: typing.Optional[str]

### Classification
- **Type**: typing.Optional[str]

### Delimiter
- **Type**: typing.Optional[str]

### StartingOffsets
- **Type**: typing.Optional[str]

### EndingOffsets
- **Type**: typing.Optional[str]

### PollTimeoutMs
- **Type**: typing.Optional[int]

### NumRetries
- **Type**: typing.Optional[int]

### RetryIntervalMs
- **Type**: typing.Optional[int]

### MaxOffsetsPerTrigger
- **Type**: typing.Optional[int]

### MinPartitions
- **Type**: typing.Optional[int]

### IncludeHeaders
- **Type**: typing.Optional[bool]

### AddRecordTimestamp
- **Type**: typing.Optional[str]

### EmitConsumerLagMetrics
- **Type**: typing.Optional[str]

### StartingTimestamp
- **Type**: typing.Optional[datetime.datetime]


# KeySchemaElement

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamingSourceOptions

### EndpointUrl
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]

### Classification
- **Type**: typing.Optional[str]

### Delimiter
- **Type**: typing.Optional[str]

### StartingPosition
- **Type**: typing.Optional[typing.Literal['earliest', 'latest', 'timestamp', 'trim_horizon']]

### MaxFetchTimeInMs
- **Type**: typing.Optional[int]

### MaxFetchRecordsPerShard
- **Type**: typing.Optional[int]

### MaxRecordPerRead
- **Type**: typing.Optional[int]

### AddIdleTimeBetweenReads
- **Type**: typing.Optional[bool]

### IdleTimeBetweenReadsInMs
- **Type**: typing.Optional[int]

### DescribeShardInterval
- **Type**: typing.Optional[int]

### NumRetries
- **Type**: typing.Optional[int]

### RetryIntervalMs
- **Type**: typing.Optional[int]

### MaxRetryIntervalMs
- **Type**: typing.Optional[int]

### AvoidEmptyBatches
- **Type**: typing.Optional[bool]

### StreamArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### RoleSessionName
- **Type**: typing.Optional[str]

### AddRecordTimestamp
- **Type**: typing.Optional[str]

### EmitConsumerLagMetrics
- **Type**: typing.Optional[str]

### StartingTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# KinesisStreamingSourceOptionsOutput

### EndpointUrl
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]

### Classification
- **Type**: typing.Optional[str]

### Delimiter
- **Type**: typing.Optional[str]

### StartingPosition
- **Type**: typing.Optional[typing.Literal['earliest', 'latest', 'timestamp', 'trim_horizon']]

### MaxFetchTimeInMs
- **Type**: typing.Optional[int]

### MaxFetchRecordsPerShard
- **Type**: typing.Optional[int]

### MaxRecordPerRead
- **Type**: typing.Optional[int]

### AddIdleTimeBetweenReads
- **Type**: typing.Optional[bool]

### IdleTimeBetweenReadsInMs
- **Type**: typing.Optional[int]

### DescribeShardInterval
- **Type**: typing.Optional[int]

### NumRetries
- **Type**: typing.Optional[int]

### RetryIntervalMs
- **Type**: typing.Optional[int]

### MaxRetryIntervalMs
- **Type**: typing.Optional[int]

### AvoidEmptyBatches
- **Type**: typing.Optional[bool]

### StreamArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### RoleSessionName
- **Type**: typing.Optional[str]

### AddRecordTimestamp
- **Type**: typing.Optional[str]

### EmitConsumerLagMetrics
- **Type**: typing.Optional[str]

### StartingTimestamp
- **Type**: typing.Optional[datetime.datetime]


# LabelingSetGenerationTaskRunProperties

### OutputS3Path
- **Type**: typing.Optional[str]


# LakeFormationConfiguration

### UseLakeFormationCredentials
- **Type**: typing.Optional[bool]

### AccountId
- **Type**: typing.Optional[str]


# LastActiveDefinition

### Description
- **Type**: typing.Optional[str]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### ParameterSpec
- **Type**: typing.Optional[str]

### BlueprintLocation
- **Type**: typing.Optional[str]

### BlueprintServiceLocation
- **Type**: typing.Optional[str]


# LastCrawlInfo

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'SUCCEEDED']]

### ErrorMessage
- **Type**: typing.Optional[str]

### LogGroup
- **Type**: typing.Optional[str]

### LogStream
- **Type**: typing.Optional[str]

### MessagePrefix
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# LineageConfiguration

### CrawlerLineageSettings
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]


# ListBlueprintsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListBlueprintsRequestPaginate

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListBlueprintsResponse

### Blueprints
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListColumnStatisticsTaskRunsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListColumnStatisticsTaskRunsResponse

### ColumnStatisticsTaskRunIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionTypesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionTypesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListConnectionTypesResponse

### ConnectionTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionTypeBrief]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrawlersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListCrawlersResponse

### CrawlerNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrawlsRequest

### CrawlerName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CrawlsFilter]]

### NextToken
- **Type**: typing.Optional[str]


# ListCrawlsResponse

### Crawls
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CrawlerHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomEntityTypesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListCustomEntityTypesResponse

### CustomEntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CustomEntityType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityResultsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityResultFilterCriteria]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataQualityResultsResponse

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityResultDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityRuleRecommendationRunsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityRuleRecommendationRunFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataQualityRuleRecommendationRunsResponse

### Runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityRuleRecommendationRunDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityRulesetEvaluationRunsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityRulesetEvaluationRunFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataQualityRulesetEvaluationRunsResponse

### Runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityRulesetEvaluationRunDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityRulesetsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityRulesetFilterCriteria]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListDataQualityRulesetsResponse

### Rulesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityRulesetListDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityStatisticAnnotationsRequest

### StatisticId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### TimestampFilter
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityStatisticAnnotationsResponse

### Annotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.StatisticAnnotation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityStatisticsRequest

### StatisticId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### TimestampFilter
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityStatisticsResponse

### Statistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.StatisticSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevEndpointsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListDevEndpointsResponse

### DevEndpointNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitiesRequest

### ConnectionName
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### ParentEntityName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### DataStoreApiVersion
- **Type**: typing.Optional[str]


# ListEntitiesRequestPaginate

### ConnectionName
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### ParentEntityName
- **Type**: typing.Optional[str]

### DataStoreApiVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListEntitiesResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Entity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListJobsRequestPaginate

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListJobsResponse

### JobNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMLTransformsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TransformFilterCriteria]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TransformSortCriteria]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListMLTransformsResponse

### TransformIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegistriesInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRegistriesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListRegistriesResponse

### Registries
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.RegistryListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaVersionsInput

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaVersionsInputPaginate

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListSchemaVersionsResponse

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SchemaVersionListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemasInput

### RegistryId
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSchemasInputPaginate

### RegistryId
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListSchemasResponse

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SchemaListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSessionsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestOrigin
- **Type**: typing.Optional[str]


# ListSessionsResponse

### Ids
- **Type**: typing.List[str]
- **Required**: Yes

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Session]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStatementsRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListStatementsResponse

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Statement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTableOptimizerRunsRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['compaction', 'orphan_file_deletion', 'retention']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTableOptimizerRunsRequestPaginate

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['compaction', 'orphan_file_deletion', 'retention']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListTableOptimizerRunsResponse

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TableOptimizerRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.TableOptimizerRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTriggersRequest

### NextToken
- **Type**: typing.Optional[str]

### DependentJobName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListTriggersRequestPaginate

### DependentJobName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListTriggersResponse

### TriggerNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsageProfilesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUsageProfilesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListUsageProfilesResponse

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.UsageProfileDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkflowsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PaginatorConfig]


# ListWorkflowsResponse

### Workflows
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Location

### Jdbc
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenNodeArg]]

### S3
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenNodeArg]]

### DynamoDB
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.CodeGenNodeArg]]


# LongColumnStatisticsData

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Optional[int]

### MaximumValue
- **Type**: typing.Optional[int]


# MLTransform

### TransformId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'NOT_READY', 'READY']]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### InputRecordTables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueTableOutput]]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TransformParameters]

### EvaluationMetrics
- **Type**: <class 'NoneType'>

### LabelCount
- **Type**: typing.Optional[int]

### Schema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SchemaColumn]]

### Role
- **Type**: typing.Optional[str]

### GlueVersion
- **Type**: typing.Optional[str]

### MaxCapacity
- **Type**: typing.Optional[float]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxRetries
- **Type**: typing.Optional[int]

### TransformEncryption
- **Type**: <class 'NoneType'>


# MLUserDataEncryption

### MlUserDataEncryptionMode
- **Type**: typing.Literal['DISABLED', 'SSE-KMS']
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# Mapping

### ToKey
- **Type**: typing.Optional[str]

### FromPath
- **Type**: typing.Optional[typing.List[str]]

### FromType
- **Type**: typing.Optional[str]

### ToType
- **Type**: typing.Optional[str]

### Dropped
- **Type**: typing.Optional[bool]

### Children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# MappingEntry

### SourceTable
- **Type**: typing.Optional[str]

### SourcePath
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### TargetTable
- **Type**: typing.Optional[str]

### TargetPath
- **Type**: typing.Optional[str]

### TargetType
- **Type**: typing.Optional[str]


# MappingOutput

### ToKey
- **Type**: typing.Optional[str]

### FromPath
- **Type**: typing.Optional[typing.List[str]]

### FromType
- **Type**: typing.Optional[str]

### ToType
- **Type**: typing.Optional[str]

### Dropped
- **Type**: typing.Optional[bool]

### Children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# MappingPaginator

### ToKey
- **Type**: typing.Optional[str]

### FromPath
- **Type**: typing.Optional[typing.List[str]]

### FromType
- **Type**: typing.Optional[str]

### ToType
- **Type**: typing.Optional[str]

### Dropped
- **Type**: typing.Optional[bool]

### Children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# Merge

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryKeys
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# MergeOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryKeys
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# MetadataInfo

### MetadataValue
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### OtherMetadataValueList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.OtherMetadataValueListItem]]


# MetadataKeyValuePair

### MetadataKey
- **Type**: typing.Optional[str]

### MetadataValue
- **Type**: typing.Optional[str]


# MetricBasedObservation

### MetricName
- **Type**: typing.Optional[str]

### StatisticId
- **Type**: typing.Optional[str]

### MetricValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityMetricValues]

### NewRules
- **Type**: typing.Optional[typing.List[str]]


# MicrosoftSQLServerCatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# MicrosoftSQLServerCatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# MicrosoftSQLServerCatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyIntegrationRequest

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DataFilter
- **Type**: typing.Optional[str]

### IntegrationName
- **Type**: typing.Optional[str]


# ModifyIntegrationResponse

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalEncryptionContext
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Tag]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING', 'NEEDS_ATTENTION', 'SYNCING']
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IntegrationError]
- **Required**: Yes

### DataFilter
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# MongoDBTarget

### ConnectionName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### ScanAll
- **Type**: typing.Optional[bool]


# MySQLCatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# MySQLCatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# MySQLCatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# Node

### Type
- **Type**: typing.Optional[typing.Literal['CRAWLER', 'JOB', 'TRIGGER']]

### Name
- **Type**: typing.Optional[str]

### UniqueId
- **Type**: typing.Optional[str]

### TriggerDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TriggerNodeDetails]

### JobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.JobNodeDetails]

### CrawlerDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CrawlerNodeDetails]


# NotificationProperty

### NotifyDelayAfter
- **Type**: typing.Optional[int]


# NullCheckBoxList

### IsEmpty
- **Type**: typing.Optional[bool]

### IsNullString
- **Type**: typing.Optional[bool]

### IsNegOne
- **Type**: typing.Optional[bool]


# NullValueField

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Datatype
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Datatype'>
- **Required**: Yes


# OAuth2ClientApplication

### UserManagedClientApplicationClientId
- **Type**: typing.Optional[str]

### AWSManagedClientApplicationReference
- **Type**: typing.Optional[str]


# OAuth2Credentials

### UserManagedClientApplicationClientSecret
- **Type**: typing.Optional[str]

### AccessToken
- **Type**: typing.Optional[str]

### RefreshToken
- **Type**: typing.Optional[str]

### JwtToken
- **Type**: typing.Optional[str]


# OAuth2Properties

### OAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### OAuth2ClientApplication
- **Type**: <class 'NoneType'>

### TokenUrl
- **Type**: typing.Optional[str]

### TokenUrlParametersMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# OAuth2PropertiesInput

### OAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### OAuth2ClientApplication
- **Type**: <class 'NoneType'>

### TokenUrl
- **Type**: typing.Optional[str]

### TokenUrlParametersMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### AuthorizationCodeProperties
- **Type**: <class 'NoneType'>

### OAuth2Credentials
- **Type**: <class 'NoneType'>


# OpenTableFormatInput

### IcebergInput
- **Type**: <class 'NoneType'>


# Option

### Value
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# OracleSQLCatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# OracleSQLCatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# OracleSQLCatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# Order

### Column
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: <class 'int'>
- **Required**: Yes


# OrphanFileDeletionConfiguration

### icebergConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.IcebergOrphanFileDeletionConfiguration]


# OrphanFileDeletionMetrics

### IcebergMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.IcebergOrphanFileDeletionMetrics]


# OtherMetadataValueListItem

### MetadataValue
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]


# PIIDetection

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### PiiType
- **Type**: typing.Literal['ColumnAudit', 'ColumnMasking', 'RowAudit', 'RowMasking']
- **Required**: Yes

### EntityTypesToDetect
- **Type**: typing.List[str]
- **Required**: Yes

### OutputColumnName
- **Type**: typing.Optional[str]

### SampleFraction
- **Type**: typing.Optional[float]

### ThresholdFraction
- **Type**: typing.Optional[float]

### MaskValue
- **Type**: typing.Optional[str]


# PIIDetectionOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### PiiType
- **Type**: typing.Literal['ColumnAudit', 'ColumnMasking', 'RowAudit', 'RowMasking']
- **Required**: Yes

### EntityTypesToDetect
- **Type**: typing.List[str]
- **Required**: Yes

### OutputColumnName
- **Type**: typing.Optional[str]

### SampleFraction
- **Type**: typing.Optional[float]

### ThresholdFraction
- **Type**: typing.Optional[float]

### MaskValue
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Partition

### Values
- **Type**: typing.Optional[typing.List[str]]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastAccessTime
- **Type**: typing.Optional[datetime.datetime]

### StorageDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StorageDescriptorOutput]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastAnalyzedTime
- **Type**: typing.Optional[datetime.datetime]

### CatalogId
- **Type**: typing.Optional[str]


# PartitionError

### PartitionValues
- **Type**: typing.Optional[typing.List[str]]

### ErrorDetail
- **Type**: <class 'NoneType'>


# PartitionIndex

### Keys
- **Type**: typing.List[str]
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes


# PartitionIndexDescriptor

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.KeySchemaElement]
- **Required**: Yes

### IndexStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### BackfillErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.BackfillError]]


# PartitionInput

### Values
- **Type**: typing.Optional[typing.List[str]]

### LastAccessTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StorageDescriptor
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.StorageDescriptor, aws_resource_validator.pydantic_models.glue.glue_classes.StorageDescriptorOutput, NoneType]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastAnalyzedTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PartitionValueList

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# PartitionValueListOutput

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# PhysicalConnectionRequirements

### SubnetId
- **Type**: typing.Optional[str]

### SecurityGroupIdList
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZone
- **Type**: typing.Optional[str]


# PhysicalConnectionRequirementsOutput

### SubnetId
- **Type**: typing.Optional[str]

### SecurityGroupIdList
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZone
- **Type**: typing.Optional[str]


# PostgreSQLCatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# PostgreSQLCatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# PostgreSQLCatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# Predecessor

### JobName
- **Type**: typing.Optional[str]

### RunId
- **Type**: typing.Optional[str]


# Predicate

### Logical
- **Type**: typing.Optional[typing.Literal['AND', 'ANY']]

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Condition]]


# PredicateOutput

### Logical
- **Type**: typing.Optional[typing.Literal['AND', 'ANY']]

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Condition]]


# PrincipalPermissions

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataLakePrincipal]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DROP', 'INSERT', 'SELECT']]]


# PrincipalPermissionsOutput

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataLakePrincipal]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DROP', 'INSERT', 'SELECT']]]


# ProfileConfiguration

### SessionConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.ConfigurationObject]]

### JobConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.ConfigurationObject]]


# ProfileConfigurationOutput

### SessionConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.ConfigurationObjectOutput]]

### JobConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.ConfigurationObjectOutput]]


# Property

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Required
- **Type**: <class 'bool'>
- **Required**: Yes

### PropertyTypes
- **Type**: typing.List[typing.Literal['READ_ONLY', 'SECRET', 'SECRET_OR_USER_INPUT', 'UNUSED', 'USER_INPUT']]
- **Required**: Yes

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.AllowedValue]]

### DataOperationScopes
- **Type**: typing.Optional[typing.List[typing.Literal['READ', 'WRITE']]]


# PropertyPredicate

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Comparator
- **Type**: typing.Optional[typing.Literal['EQUALS', 'GREATER_THAN', 'GREATER_THAN_EQUALS', 'LESS_THAN', 'LESS_THAN_EQUALS']]


# PutDataCatalogEncryptionSettingsRequest

### DataCatalogEncryptionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DataCatalogEncryptionSettings'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# PutDataQualityProfileAnnotationRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InclusionAnnotation
- **Type**: typing.Literal['EXCLUDE', 'INCLUDE']
- **Required**: Yes


# PutResourcePolicyRequest

### PolicyInJson
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: typing.Optional[str]

### PolicyHashCondition
- **Type**: typing.Optional[str]

### PolicyExistsCondition
- **Type**: typing.Optional[typing.Literal['MUST_EXIST', 'NONE', 'NOT_EXIST']]

### EnableHybrid
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]


# PutResourcePolicyResponse

### PolicyHash
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# PutSchemaVersionMetadataInput

### MetadataKeyValue
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.MetadataKeyValuePair'>
- **Required**: Yes

### SchemaId
- **Type**: <class 'NoneType'>

### SchemaVersionNumber
- **Type**: <class 'NoneType'>

### SchemaVersionId
- **Type**: typing.Optional[str]


# PutSchemaVersionMetadataResponse

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### MetadataKey
- **Type**: <class 'str'>
- **Required**: Yes

### MetadataValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# PutWorkflowRunPropertiesRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### RunProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# QuerySchemaVersionMetadataInput

### SchemaId
- **Type**: <class 'NoneType'>

### SchemaVersionNumber
- **Type**: <class 'NoneType'>

### SchemaVersionId
- **Type**: typing.Optional[str]

### MetadataList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.MetadataKeyValuePair]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# QuerySchemaVersionMetadataResponse

### MetadataInfoMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue.glue_classes.MetadataInfo]
- **Required**: Yes

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# QuerySessionContext

### QueryId
- **Type**: typing.Optional[str]

### QueryStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ClusterId
- **Type**: typing.Optional[str]

### QueryAuthorizationId
- **Type**: typing.Optional[str]

### AdditionalContext
- **Type**: typing.Optional[typing.Dict[str, str]]


# Recipe

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### RecipeReference
- **Type**: <class 'NoneType'>

### RecipeSteps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.RecipeStep, aws_resource_validator.pydantic_models.glue.glue_classes.RecipeStepOutput]]]


# RecipeAction

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecipeActionOutput

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecipeOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### RecipeReference
- **Type**: <class 'NoneType'>

### RecipeSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.RecipeStepOutput]]


# RecipeReference

### RecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: <class 'str'>
- **Required**: Yes


# RecipeStep

### Action
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.RecipeAction, aws_resource_validator.pydantic_models.glue.glue_classes.RecipeActionOutput]
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ConditionExpression]]


# RecipeStepOutput

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.RecipeActionOutput'>
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ConditionExpression]]


# RecrawlPolicy

### RecrawlBehavior
- **Type**: typing.Optional[typing.Literal['CRAWL_EVENT_MODE', 'CRAWL_EVERYTHING', 'CRAWL_NEW_FOLDERS_ONLY']]


# RedshiftSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### RedshiftTmpDir
- **Type**: typing.Optional[str]

### TmpDirIAMRole
- **Type**: typing.Optional[str]


# RedshiftTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### RedshiftTmpDir
- **Type**: typing.Optional[str]

### TmpDirIAMRole
- **Type**: typing.Optional[str]

### UpsertRedshiftOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.UpsertRedshiftTargetOptions, aws_resource_validator.pydantic_models.glue.glue_classes.UpsertRedshiftTargetOptionsOutput, NoneType]


# RedshiftTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### RedshiftTmpDir
- **Type**: typing.Optional[str]

### TmpDirIAMRole
- **Type**: typing.Optional[str]

### UpsertRedshiftOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.UpsertRedshiftTargetOptionsOutput]


# RegisterSchemaVersionInput

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes

### SchemaDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterSchemaVersionResponse

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'FAILURE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# RegistryId

### RegistryName
- **Type**: typing.Optional[str]

### RegistryArn
- **Type**: typing.Optional[str]


# RegistryListItem

### RegistryName
- **Type**: typing.Optional[str]

### RegistryArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING']]

### CreatedTime
- **Type**: typing.Optional[str]

### UpdatedTime
- **Type**: typing.Optional[str]


# RelationalCatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveSchemaVersionMetadataInput

### MetadataKeyValue
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.MetadataKeyValuePair'>
- **Required**: Yes

### SchemaId
- **Type**: <class 'NoneType'>

### SchemaVersionNumber
- **Type**: <class 'NoneType'>

### SchemaVersionId
- **Type**: typing.Optional[str]


# RemoveSchemaVersionMetadataResponse

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### MetadataKey
- **Type**: <class 'str'>
- **Required**: Yes

### MetadataValue
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# RenameField

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### SourcePath
- **Type**: typing.List[str]
- **Required**: Yes

### TargetPath
- **Type**: typing.List[str]
- **Required**: Yes


# RenameFieldOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### SourcePath
- **Type**: typing.List[str]
- **Required**: Yes

### TargetPath
- **Type**: typing.List[str]
- **Required**: Yes


# ResetJobBookmarkRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: typing.Optional[str]


# ResetJobBookmarkResponse

### JobBookmarkEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.JobBookmarkEntry'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceUri

### ResourceType
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'FILE', 'JAR']]

### Uri
- **Type**: typing.Optional[str]


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


# ResumeWorkflowRunRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeIds
- **Type**: typing.List[str]
- **Required**: Yes


# ResumeWorkflowRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# RetentionConfiguration

### icebergConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.IcebergRetentionConfiguration]


# RetentionMetrics

### IcebergMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.IcebergRetentionMetrics]


# RunIdentifier

### RunId
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]


# RunMetrics

### NumberOfBytesCompacted
- **Type**: typing.Optional[str]

### NumberOfFilesCompacted
- **Type**: typing.Optional[str]

### NumberOfDpus
- **Type**: typing.Optional[str]

### JobDurationInHour
- **Type**: typing.Optional[str]


# RunStatementRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# RunStatementResponse

### Id
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# S3CatalogDeltaSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalDeltaOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# S3CatalogDeltaSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalDeltaOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# S3CatalogHudiSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalHudiOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# S3CatalogHudiSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalHudiOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# S3CatalogSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionPredicate
- **Type**: typing.Optional[str]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3SourceAdditionalOptions]


# S3CatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogSchemaChangePolicy]


# S3CatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogSchemaChangePolicy]


# S3CsvSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### Separator
- **Type**: typing.Literal['comma', 'ctrla', 'pipe', 'semicolon', 'tab']
- **Required**: Yes

### QuoteChar
- **Type**: typing.Literal['disabled', 'quillemet', 'quote', 'single_quote']
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['bzip2', 'gzip']]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### GroupSize
- **Type**: typing.Optional[str]

### GroupFiles
- **Type**: typing.Optional[str]

### Recurse
- **Type**: typing.Optional[bool]

### MaxBand
- **Type**: typing.Optional[int]

### MaxFilesInBand
- **Type**: typing.Optional[int]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### Escaper
- **Type**: typing.Optional[str]

### Multiline
- **Type**: typing.Optional[bool]

### WithHeader
- **Type**: typing.Optional[bool]

### WriteHeader
- **Type**: typing.Optional[bool]

### SkipFirst
- **Type**: typing.Optional[bool]

### OptimizePerformance
- **Type**: typing.Optional[bool]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# S3CsvSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### Separator
- **Type**: typing.Literal['comma', 'ctrla', 'pipe', 'semicolon', 'tab']
- **Required**: Yes

### QuoteChar
- **Type**: typing.Literal['disabled', 'quillemet', 'quote', 'single_quote']
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['bzip2', 'gzip']]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### GroupSize
- **Type**: typing.Optional[str]

### GroupFiles
- **Type**: typing.Optional[str]

### Recurse
- **Type**: typing.Optional[bool]

### MaxBand
- **Type**: typing.Optional[int]

### MaxFilesInBand
- **Type**: typing.Optional[int]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### Escaper
- **Type**: typing.Optional[str]

### Multiline
- **Type**: typing.Optional[bool]

### WithHeader
- **Type**: typing.Optional[bool]

### WriteHeader
- **Type**: typing.Optional[bool]

### SkipFirst
- **Type**: typing.Optional[bool]

### OptimizePerformance
- **Type**: typing.Optional[bool]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# S3DeltaCatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogSchemaChangePolicy]


# S3DeltaCatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogSchemaChangePolicy]


# S3DeltaDirectTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Compression
- **Type**: typing.Literal['snappy', 'uncompressed']
- **Required**: Yes

### Format
- **Type**: typing.Literal['avro', 'csv', 'delta', 'hudi', 'json', 'orc', 'parquet']
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectSchemaChangePolicy]


# S3DeltaDirectTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Compression
- **Type**: typing.Literal['snappy', 'uncompressed']
- **Required**: Yes

### Format
- **Type**: typing.Literal['avro', 'csv', 'delta', 'hudi', 'json', 'orc', 'parquet']
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectSchemaChangePolicy]


# S3DeltaSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### AdditionalDeltaOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# S3DeltaSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### AdditionalDeltaOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# S3DirectSourceAdditionalOptions

### BoundedSize
- **Type**: typing.Optional[int]

### BoundedFiles
- **Type**: typing.Optional[int]

### EnableSamplePath
- **Type**: typing.Optional[bool]

### SamplePath
- **Type**: typing.Optional[str]


# S3DirectTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['avro', 'csv', 'delta', 'hudi', 'json', 'orc', 'parquet']
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### Compression
- **Type**: typing.Optional[str]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectSchemaChangePolicy]


# S3DirectTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['avro', 'csv', 'delta', 'hudi', 'json', 'orc', 'parquet']
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### Compression
- **Type**: typing.Optional[str]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectSchemaChangePolicy]


# S3Encryption

### S3EncryptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SSE-KMS', 'SSE-S3']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# S3GlueParquetTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### Compression
- **Type**: typing.Optional[typing.Literal['gzip', 'lzo', 'none', 'snappy', 'uncompressed']]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectSchemaChangePolicy]


# S3GlueParquetTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### Compression
- **Type**: typing.Optional[typing.Literal['gzip', 'lzo', 'none', 'snappy', 'uncompressed']]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectSchemaChangePolicy]


# S3HudiCatalogTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogSchemaChangePolicy]


# S3HudiCatalogTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CatalogSchemaChangePolicy]


# S3HudiDirectTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Compression
- **Type**: typing.Literal['gzip', 'lzo', 'snappy', 'uncompressed']
- **Required**: Yes

### Format
- **Type**: typing.Literal['avro', 'csv', 'delta', 'hudi', 'json', 'orc', 'parquet']
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectSchemaChangePolicy]


# S3HudiDirectTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Compression
- **Type**: typing.Literal['gzip', 'lzo', 'snappy', 'uncompressed']
- **Required**: Yes

### Format
- **Type**: typing.Literal['avro', 'csv', 'delta', 'hudi', 'json', 'orc', 'parquet']
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DirectSchemaChangePolicy]


# S3HudiSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### AdditionalHudiOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# S3HudiSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### AdditionalHudiOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# S3JsonSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['bzip2', 'gzip']]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### GroupSize
- **Type**: typing.Optional[str]

### GroupFiles
- **Type**: typing.Optional[str]

### Recurse
- **Type**: typing.Optional[bool]

### MaxBand
- **Type**: typing.Optional[int]

### MaxFilesInBand
- **Type**: typing.Optional[int]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### JsonPath
- **Type**: typing.Optional[str]

### Multiline
- **Type**: typing.Optional[bool]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# S3JsonSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['bzip2', 'gzip']]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### GroupSize
- **Type**: typing.Optional[str]

### GroupFiles
- **Type**: typing.Optional[str]

### Recurse
- **Type**: typing.Optional[bool]

### MaxBand
- **Type**: typing.Optional[int]

### MaxFilesInBand
- **Type**: typing.Optional[int]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### JsonPath
- **Type**: typing.Optional[str]

### Multiline
- **Type**: typing.Optional[bool]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# S3ParquetSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['gzip', 'lzo', 'none', 'snappy', 'uncompressed']]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### GroupSize
- **Type**: typing.Optional[str]

### GroupFiles
- **Type**: typing.Optional[str]

### Recurse
- **Type**: typing.Optional[bool]

### MaxBand
- **Type**: typing.Optional[int]

### MaxFilesInBand
- **Type**: typing.Optional[int]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# S3ParquetSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['gzip', 'lzo', 'none', 'snappy', 'uncompressed']]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### GroupSize
- **Type**: typing.Optional[str]

### GroupFiles
- **Type**: typing.Optional[str]

### Recurse
- **Type**: typing.Optional[bool]

### MaxBand
- **Type**: typing.Optional[int]

### MaxFilesInBand
- **Type**: typing.Optional[int]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.S3DirectSourceAdditionalOptions]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# S3SourceAdditionalOptions

### BoundedSize
- **Type**: typing.Optional[int]

### BoundedFiles
- **Type**: typing.Optional[int]


# S3Target

### Path
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### SampleSize
- **Type**: typing.Optional[int]

### EventQueueArn
- **Type**: typing.Optional[str]

### DlqEventQueueArn
- **Type**: typing.Optional[str]


# S3TargetOutput

### Path
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### SampleSize
- **Type**: typing.Optional[int]

### EventQueueArn
- **Type**: typing.Optional[str]

### DlqEventQueueArn
- **Type**: typing.Optional[str]


# Schedule

### ScheduleExpression
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['NOT_SCHEDULED', 'SCHEDULED', 'TRANSITIONING']]


# SchemaChangePolicy

### UpdateBehavior
- **Type**: typing.Optional[typing.Literal['LOG', 'UPDATE_IN_DATABASE']]

### DeleteBehavior
- **Type**: typing.Optional[typing.Literal['DELETE_FROM_DATABASE', 'DEPRECATE_IN_DATABASE', 'LOG']]


# SchemaColumn

### Name
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]


# SchemaId

### SchemaArn
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### RegistryName
- **Type**: typing.Optional[str]


# SchemaListItem

### RegistryName
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### SchemaArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SchemaStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'PENDING']]

### CreatedTime
- **Type**: typing.Optional[str]

### UpdatedTime
- **Type**: typing.Optional[str]


# SchemaReference

### SchemaId
- **Type**: <class 'NoneType'>

### SchemaVersionId
- **Type**: typing.Optional[str]

### SchemaVersionNumber
- **Type**: typing.Optional[int]


# SchemaVersionErrorItem

### VersionNumber
- **Type**: typing.Optional[int]

### ErrorDetails
- **Type**: <class 'NoneType'>


# SchemaVersionListItem

### SchemaArn
- **Type**: typing.Optional[str]

### SchemaVersionId
- **Type**: typing.Optional[str]

### VersionNumber
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'FAILURE', 'PENDING']]

### CreatedTime
- **Type**: typing.Optional[str]


# SchemaVersionNumber

### LatestVersion
- **Type**: typing.Optional[bool]

### VersionNumber
- **Type**: typing.Optional[int]


# SearchTablesRequest

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.PropertyPredicate]]

### SearchText
- **Type**: typing.Optional[str]

### SortCriteria
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SortCriterion]]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FEDERATED', 'FOREIGN']]

### IncludeStatusDetails
- **Type**: typing.Optional[bool]


# SearchTablesResponse

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Table]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SecurityConfiguration

### Name
- **Type**: typing.Optional[str]

### CreatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.EncryptionConfigurationOutput]


# Segment

### SegmentNumber
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSegments
- **Type**: <class 'int'>
- **Required**: Yes


# SelectFields

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# SelectFieldsOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# SelectFromCollection

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Index
- **Type**: <class 'int'>
- **Required**: Yes


# SelectFromCollectionOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Index
- **Type**: <class 'int'>
- **Required**: Yes


# SerDeInfo

### Name
- **Type**: typing.Optional[str]

### SerializationLibrary
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# SerDeInfoOutput

### Name
- **Type**: typing.Optional[str]

### SerializationLibrary
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# Session

### Id
- **Type**: typing.Optional[str]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROVISIONING', 'READY', 'STOPPED', 'STOPPING', 'TIMEOUT']]

### ErrorMessage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### Command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SessionCommand]

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionsListOutput]

### Progress
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### GlueVersion
- **Type**: typing.Optional[str]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### CompletedOn
- **Type**: typing.Optional[datetime.datetime]

### ExecutionTime
- **Type**: typing.Optional[float]

### DPUSeconds
- **Type**: typing.Optional[float]

### IdleTimeout
- **Type**: typing.Optional[int]

### ProfileName
- **Type**: typing.Optional[str]


# SessionCommand

### Name
- **Type**: typing.Optional[str]

### PythonVersion
- **Type**: typing.Optional[str]


# SkewedInfo

### SkewedColumnNames
- **Type**: typing.Optional[typing.List[str]]

### SkewedColumnValues
- **Type**: typing.Optional[typing.List[str]]

### SkewedColumnValueLocationMaps
- **Type**: typing.Optional[typing.Dict[str, str]]


# SkewedInfoOutput

### SkewedColumnNames
- **Type**: typing.Optional[typing.List[str]]

### SkewedColumnValues
- **Type**: typing.Optional[typing.List[str]]

### SkewedColumnValueLocationMaps
- **Type**: typing.Optional[typing.Dict[str, str]]


# SnowflakeNodeData

### SourceType
- **Type**: typing.Optional[str]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### Schema
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### TempDir
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### SampleQuery
- **Type**: typing.Optional[str]

### PreAction
- **Type**: typing.Optional[str]

### PostAction
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[str]

### Upsert
- **Type**: typing.Optional[bool]

### MergeAction
- **Type**: typing.Optional[str]

### MergeWhenMatched
- **Type**: typing.Optional[str]

### MergeWhenNotMatched
- **Type**: typing.Optional[str]

### MergeClause
- **Type**: typing.Optional[str]

### StagingTable
- **Type**: typing.Optional[str]

### SelectedColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Option]]

### AutoPushdown
- **Type**: typing.Optional[bool]

### TableSchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Option]]


# SnowflakeNodeDataOutput

### SourceType
- **Type**: typing.Optional[str]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### Schema
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### TempDir
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.Option]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### SampleQuery
- **Type**: typing.Optional[str]

### PreAction
- **Type**: typing.Optional[str]

### PostAction
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[str]

### Upsert
- **Type**: typing.Optional[bool]

### MergeAction
- **Type**: typing.Optional[str]

### MergeWhenMatched
- **Type**: typing.Optional[str]

### MergeWhenNotMatched
- **Type**: typing.Optional[str]

### MergeClause
- **Type**: typing.Optional[str]

### StagingTable
- **Type**: typing.Optional[str]

### SelectedColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Option]]

### AutoPushdown
- **Type**: typing.Optional[bool]

### TableSchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Option]]


# SnowflakeSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeNodeData, aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeNodeDataOutput]
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema, aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]]


# SnowflakeSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeNodeDataOutput'>
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# SnowflakeTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeNodeData, aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeNodeDataOutput]
- **Required**: Yes

### Inputs
- **Type**: typing.Optional[typing.List[str]]


# SnowflakeTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SnowflakeNodeDataOutput'>
- **Required**: Yes

### Inputs
- **Type**: typing.Optional[typing.List[str]]


# SortCriterion

### FieldName
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# SourceControlDetails

### Provider
- **Type**: typing.Optional[typing.Literal['AWS_CODE_COMMIT', 'BITBUCKET', 'GITHUB', 'GITLAB']]

### Repository
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### Branch
- **Type**: typing.Optional[str]

### Folder
- **Type**: typing.Optional[str]

### LastCommitId
- **Type**: typing.Optional[str]

### AuthStrategy
- **Type**: typing.Optional[typing.Literal['AWS_SECRETS_MANAGER', 'PERSONAL_ACCESS_TOKEN']]

### AuthToken
- **Type**: typing.Optional[str]


# SourceProcessingProperties

### RoleArn
- **Type**: typing.Optional[str]


# SourceTableConfig

### Fields
- **Type**: typing.Optional[typing.List[str]]

### FilterPredicate
- **Type**: typing.Optional[str]

### PrimaryKey
- **Type**: typing.Optional[typing.List[str]]

### RecordUpdateField
- **Type**: typing.Optional[str]


# SourceTableConfigOutput

### Fields
- **Type**: typing.Optional[typing.List[str]]

### FilterPredicate
- **Type**: typing.Optional[str]

### PrimaryKey
- **Type**: typing.Optional[typing.List[str]]

### RecordUpdateField
- **Type**: typing.Optional[str]


# SparkConnectorSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# SparkConnectorSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# SparkConnectorTarget

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# SparkConnectorTargetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# SparkSQL

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### SqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### SqlAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SqlAlias]
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchema]]


# SparkSQLOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### SqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### SqlAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SqlAlias]
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.GlueSchemaOutput]]


# Spigot

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Topk
- **Type**: typing.Optional[int]

### Prob
- **Type**: typing.Optional[float]


# SpigotOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Topk
- **Type**: typing.Optional[int]

### Prob
- **Type**: typing.Optional[float]


# SplitFields

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# SplitFieldsOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# SqlAlias

### From
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# StartBlueprintRunRequest

### BlueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[str]


# StartBlueprintRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartColumnStatisticsTaskRunRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnNameList
- **Type**: typing.Optional[typing.List[str]]

### SampleSize
- **Type**: typing.Optional[float]

### CatalogID
- **Type**: typing.Optional[str]

### SecurityConfiguration
- **Type**: typing.Optional[str]


# StartColumnStatisticsTaskRunResponse

### ColumnStatisticsTaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartColumnStatisticsTaskRunScheduleRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# StartCrawlerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartCrawlerScheduleRequest

### CrawlerName
- **Type**: <class 'str'>
- **Required**: Yes


# StartDataQualityRuleRecommendationRunRequest

### DataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DataSource, aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfWorkers
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### CreatedRulesetName
- **Type**: typing.Optional[str]

### DataQualitySecurityConfiguration
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# StartDataQualityRuleRecommendationRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartDataQualityRulesetEvaluationRunRequest

### DataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DataSource, aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### RulesetNames
- **Type**: typing.List[str]
- **Required**: Yes

### NumberOfWorkers
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### ClientToken
- **Type**: typing.Optional[str]

### AdditionalRunOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DataQualityEvaluationRunAdditionalRunOptions]

### AdditionalDataSources
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.DataSource, aws_resource_validator.pydantic_models.glue.glue_classes.DataSourceOutput]]]


# StartDataQualityRulesetEvaluationRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartExportLabelsTaskRunRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputS3Path
- **Type**: <class 'str'>
- **Required**: Yes


# StartExportLabelsTaskRunResponse

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartImportLabelsTaskRunRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### InputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### ReplaceAllLabels
- **Type**: typing.Optional[bool]


# StartImportLabelsTaskRunResponse

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartJobRunRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobRunQueuingEnabled
- **Type**: typing.Optional[bool]

### JobRunId
- **Type**: typing.Optional[str]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### AllocatedCapacity
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[float]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: <class 'NoneType'>

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]


# StartJobRunResponse

### JobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartMLEvaluationTaskRunRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes


# StartMLEvaluationTaskRunResponse

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartMLLabelingSetGenerationTaskRunRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputS3Path
- **Type**: <class 'str'>
- **Required**: Yes


# StartMLLabelingSetGenerationTaskRunResponse

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartTriggerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartTriggerResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartWorkflowRunRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartWorkflowRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StartingEventBatchCondition

### BatchSize
- **Type**: typing.Optional[int]

### BatchWindow
- **Type**: typing.Optional[int]


# Statement

### Id
- **Type**: typing.Optional[int]

### Code
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CANCELLED', 'CANCELLING', 'ERROR', 'RUNNING', 'WAITING']]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StatementOutput]

### Progress
- **Type**: typing.Optional[float]

### StartedOn
- **Type**: typing.Optional[int]

### CompletedOn
- **Type**: typing.Optional[int]


# StatementOutput

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StatementOutputData]

### ExecutionCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CANCELLED', 'CANCELLING', 'ERROR', 'RUNNING', 'WAITING']]

### ErrorName
- **Type**: typing.Optional[str]

### ErrorValue
- **Type**: typing.Optional[str]

### Traceback
- **Type**: typing.Optional[typing.List[str]]


# StatementOutputData

### TextPlain
- **Type**: typing.Optional[str]


# StatisticAnnotation

### ProfileId
- **Type**: typing.Optional[str]

### StatisticId
- **Type**: typing.Optional[str]

### StatisticRecordedOn
- **Type**: typing.Optional[datetime.datetime]

### InclusionAnnotation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TimestampedInclusionAnnotation]


# StatisticModelResult

### LowerBound
- **Type**: typing.Optional[float]

### UpperBound
- **Type**: typing.Optional[float]

### PredictedValue
- **Type**: typing.Optional[float]

### ActualValue
- **Type**: typing.Optional[float]

### Date
- **Type**: typing.Optional[datetime.datetime]

### InclusionAnnotation
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# StatisticSummary

### StatisticId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### RunIdentifier
- **Type**: <class 'NoneType'>

### StatisticName
- **Type**: typing.Optional[str]

### DoubleValue
- **Type**: typing.Optional[float]

### EvaluationLevel
- **Type**: typing.Optional[typing.Literal['Column', 'Dataset', 'Multicolumn']]

### ColumnsReferenced
- **Type**: typing.Optional[typing.List[str]]

### ReferencedDatasets
- **Type**: typing.Optional[typing.List[str]]

### StatisticProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### RecordedOn
- **Type**: typing.Optional[datetime.datetime]

### InclusionAnnotation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TimestampedInclusionAnnotation]


# StatusDetails

### RequestedChange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ViewValidations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ViewValidation]]


# StatusDetailsPaginator

### RequestedChange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ViewValidations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ViewValidation]]


# StopColumnStatisticsTaskRunRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# StopColumnStatisticsTaskRunScheduleRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# StopCrawlerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopCrawlerScheduleRequest

### CrawlerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopSessionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# StopSessionResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StopTriggerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopTriggerResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# StopWorkflowRunRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# StorageDescriptor

### Columns
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Column, aws_resource_validator.pydantic_models.glue.glue_classes.ColumnOutput]]]

### Location
- **Type**: typing.Optional[str]

### AdditionalLocations
- **Type**: typing.Optional[typing.List[str]]

### InputFormat
- **Type**: typing.Optional[str]

### OutputFormat
- **Type**: typing.Optional[str]

### Compressed
- **Type**: typing.Optional[bool]

### NumberOfBuckets
- **Type**: typing.Optional[int]

### SerdeInfo
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SerDeInfo, aws_resource_validator.pydantic_models.glue.glue_classes.SerDeInfoOutput, NoneType]

### BucketColumns
- **Type**: typing.Optional[typing.List[str]]

### SortColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Order]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### SkewedInfo
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SkewedInfo, aws_resource_validator.pydantic_models.glue.glue_classes.SkewedInfoOutput, NoneType]

### StoredAsSubDirectories
- **Type**: typing.Optional[bool]

### SchemaReference
- **Type**: <class 'NoneType'>


# StorageDescriptorOutput

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnOutput]]

### Location
- **Type**: typing.Optional[str]

### AdditionalLocations
- **Type**: typing.Optional[typing.List[str]]

### InputFormat
- **Type**: typing.Optional[str]

### OutputFormat
- **Type**: typing.Optional[str]

### Compressed
- **Type**: typing.Optional[bool]

### NumberOfBuckets
- **Type**: typing.Optional[int]

### SerdeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SerDeInfoOutput]

### BucketColumns
- **Type**: typing.Optional[typing.List[str]]

### SortColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Order]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### SkewedInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.SkewedInfoOutput]

### StoredAsSubDirectories
- **Type**: typing.Optional[bool]

### SchemaReference
- **Type**: <class 'NoneType'>


# StreamingDataPreviewOptions

### PollingTime
- **Type**: typing.Optional[int]

### RecordPollingLimit
- **Type**: typing.Optional[int]


# StringColumnStatisticsData

### MaximumLength
- **Type**: <class 'int'>
- **Required**: Yes

### AverageLength
- **Type**: <class 'float'>
- **Required**: Yes

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes


# SupportedDialect

### Dialect
- **Type**: typing.Optional[typing.Literal['ATHENA', 'REDSHIFT', 'SPARK']]

### DialectVersion
- **Type**: typing.Optional[str]


# Table

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### LastAccessTime
- **Type**: typing.Optional[datetime.datetime]

### LastAnalyzedTime
- **Type**: typing.Optional[datetime.datetime]

### Retention
- **Type**: typing.Optional[int]

### StorageDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StorageDescriptorOutput]

### PartitionKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnOutput]]

### ViewOriginalText
- **Type**: typing.Optional[str]

### ViewExpandedText
- **Type**: typing.Optional[str]

### TableType
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreatedBy
- **Type**: typing.Optional[str]

### IsRegisteredWithLakeFormation
- **Type**: typing.Optional[bool]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableIdentifier]

### CatalogId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### FederatedTable
- **Type**: <class 'NoneType'>

### ViewDefinition
- **Type**: <class 'NoneType'>

### IsMultiDialectView
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableStatus]


# TableError

### TableName
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: <class 'NoneType'>


# TableIdentifier

### CatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# TableInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### LastAccessTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastAnalyzedTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Retention
- **Type**: typing.Optional[int]

### StorageDescriptor
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.StorageDescriptor, aws_resource_validator.pydantic_models.glue.glue_classes.StorageDescriptorOutput, NoneType]

### PartitionKeys
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Column, aws_resource_validator.pydantic_models.glue.glue_classes.ColumnOutput]]]

### ViewOriginalText
- **Type**: typing.Optional[str]

### ViewExpandedText
- **Type**: typing.Optional[str]

### TableType
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableIdentifier]

### ViewDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ViewDefinitionInput]


# TableOptimizer

### type
- **Type**: typing.Optional[typing.Literal['compaction', 'orphan_file_deletion', 'retention']]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableOptimizerConfiguration]

### lastRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableOptimizerRun]


# TableOptimizerConfiguration

### roleArn
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableOptimizerVpcConfiguration]

### retentionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RetentionConfiguration]

### orphanFileDeletionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.OrphanFileDeletionConfiguration]


# TableOptimizerRun

### eventType
- **Type**: typing.Optional[typing.Literal['completed', 'failed', 'in_progress', 'starting']]

### startTimestamp
- **Type**: typing.Optional[datetime.datetime]

### endTimestamp
- **Type**: typing.Optional[datetime.datetime]

### metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RunMetrics]

### error
- **Type**: typing.Optional[str]

### compactionMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.CompactionMetrics]

### retentionMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.RetentionMetrics]

### orphanFileDeletionMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.OrphanFileDeletionMetrics]


# TableOptimizerVpcConfiguration

### glueConnectionName
- **Type**: typing.Optional[str]


# TablePaginator

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### LastAccessTime
- **Type**: typing.Optional[datetime.datetime]

### LastAnalyzedTime
- **Type**: typing.Optional[datetime.datetime]

### Retention
- **Type**: typing.Optional[int]

### StorageDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StorageDescriptorOutput]

### PartitionKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnOutput]]

### ViewOriginalText
- **Type**: typing.Optional[str]

### ViewExpandedText
- **Type**: typing.Optional[str]

### TableType
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreatedBy
- **Type**: typing.Optional[str]

### IsRegisteredWithLakeFormation
- **Type**: typing.Optional[bool]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableIdentifier]

### CatalogId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### FederatedTable
- **Type**: <class 'NoneType'>

### ViewDefinition
- **Type**: <class 'NoneType'>

### IsMultiDialectView
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TableStatusPaginator]


# TableStatus

### RequestedBy
- **Type**: typing.Optional[str]

### UpdatedBy
- **Type**: typing.Optional[str]

### RequestTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### Action
- **Type**: typing.Optional[typing.Literal['CREATE', 'UPDATE']]

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'QUEUED', 'STOPPED', 'SUCCESS']]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ErrorDetail]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StatusDetails]


# TableStatusPaginator

### RequestedBy
- **Type**: typing.Optional[str]

### UpdatedBy
- **Type**: typing.Optional[str]

### RequestTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### Action
- **Type**: typing.Optional[typing.Literal['CREATE', 'UPDATE']]

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'QUEUED', 'STOPPED', 'SUCCESS']]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ErrorDetail]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.StatusDetailsPaginator]


# TableVersion

### Table
- **Type**: <class 'NoneType'>

### VersionId
- **Type**: typing.Optional[str]


# TableVersionError

### TableName
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: <class 'NoneType'>


# TableVersionPaginator

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TablePaginator]

### VersionId
- **Type**: typing.Optional[str]


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToAdd
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TargetProcessingProperties

### RoleArn
- **Type**: typing.Optional[str]

### KmsArn
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### EventBusArn
- **Type**: typing.Optional[str]


# TargetRedshiftCatalog

### CatalogArn
- **Type**: <class 'str'>
- **Required**: Yes


# TargetTableConfig

### UnnestSpec
- **Type**: typing.Optional[typing.Literal['FULL', 'NOUNNEST', 'TOPLEVEL']]

### PartitionSpec
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IntegrationPartition]]

### TargetTableName
- **Type**: typing.Optional[str]


# TargetTableConfigOutput

### UnnestSpec
- **Type**: typing.Optional[typing.Literal['FULL', 'NOUNNEST', 'TOPLEVEL']]

### PartitionSpec
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.IntegrationPartition]]

### TargetTableName
- **Type**: typing.Optional[str]


# TaskRun

### TransformId
- **Type**: typing.Optional[str]

### TaskRunId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### LogGroupName
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TaskRunProperties]

### ErrorString
- **Type**: typing.Optional[str]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### CompletedOn
- **Type**: typing.Optional[datetime.datetime]

### ExecutionTime
- **Type**: typing.Optional[int]


# TaskRunFilterCriteria

### TaskRunType
- **Type**: typing.Optional[typing.Literal['EVALUATION', 'EXPORT_LABELS', 'FIND_MATCHES', 'IMPORT_LABELS', 'LABELING_SET_GENERATION']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### StartedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TaskRunProperties

### TaskType
- **Type**: typing.Optional[typing.Literal['EVALUATION', 'EXPORT_LABELS', 'FIND_MATCHES', 'IMPORT_LABELS', 'LABELING_SET_GENERATION']]

### ImportLabelsTaskRunProperties
- **Type**: <class 'NoneType'>

### ExportLabelsTaskRunProperties
- **Type**: <class 'NoneType'>

### LabelingSetGenerationTaskRunProperties
- **Type**: <class 'NoneType'>

### FindMatchesTaskRunProperties
- **Type**: <class 'NoneType'>


# TaskRunSortCriteria

### Column
- **Type**: typing.Literal['STARTED', 'STATUS', 'TASK_RUN_TYPE']
- **Required**: Yes

### SortDirection
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# TestConnectionInput

### ConnectionType
- **Type**: typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']
- **Required**: Yes

### ConnectionProperties
- **Type**: typing.Dict[typing.Literal['CLUSTER_IDENTIFIER', 'CONFIG_FILES', 'CONNECTION_URL', 'CONNECTOR_CLASS_NAME', 'CONNECTOR_TYPE', 'CONNECTOR_URL', 'CUSTOM_JDBC_CERT', 'CUSTOM_JDBC_CERT_STRING', 'DATABASE', 'ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD', 'ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD', 'ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD', 'ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD', 'ENCRYPTED_PASSWORD', 'ENDPOINT', 'ENDPOINT_TYPE', 'HOST', 'INSTANCE_ID', 'JDBC_CONNECTION_URL', 'JDBC_DRIVER_CLASS_NAME', 'JDBC_DRIVER_JAR_URI', 'JDBC_ENFORCE_SSL', 'JDBC_ENGINE', 'JDBC_ENGINE_VERSION', 'KAFKA_BOOTSTRAP_SERVERS', 'KAFKA_CLIENT_KEYSTORE', 'KAFKA_CLIENT_KEYSTORE_PASSWORD', 'KAFKA_CLIENT_KEY_PASSWORD', 'KAFKA_CUSTOM_CERT', 'KAFKA_SASL_GSSAPI_KEYTAB', 'KAFKA_SASL_GSSAPI_KRB5_CONF', 'KAFKA_SASL_GSSAPI_PRINCIPAL', 'KAFKA_SASL_GSSAPI_SERVICE', 'KAFKA_SASL_MECHANISM', 'KAFKA_SASL_PLAIN_PASSWORD', 'KAFKA_SASL_PLAIN_USERNAME', 'KAFKA_SASL_SCRAM_PASSWORD', 'KAFKA_SASL_SCRAM_SECRETS_ARN', 'KAFKA_SASL_SCRAM_USERNAME', 'KAFKA_SKIP_CUSTOM_CERT_VALIDATION', 'KAFKA_SSL_ENABLED', 'PASSWORD', 'PORT', 'REGION', 'ROLE_ARN', 'SECRET_ID', 'SKIP_CUSTOM_JDBC_CERT_VALIDATION', 'USERNAME', 'WORKGROUP_NAME'], str]
- **Required**: Yes

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.AuthenticationConfigurationInput]


# TestConnectionRequest

### ConnectionName
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### TestConnectionInput
- **Type**: <class 'NoneType'>


# TimestampFilter

### RecordedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### RecordedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TimestampedInclusionAnnotation

### Value
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]


# TransformConfigParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['bool', 'complex', 'float', 'int', 'list', 'null', 'str']
- **Required**: Yes

### ValidationRule
- **Type**: typing.Optional[str]

### ValidationMessage
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[typing.List[str]]

### ListType
- **Type**: typing.Optional[typing.Literal['bool', 'complex', 'float', 'int', 'list', 'null', 'str']]

### IsOptional
- **Type**: typing.Optional[bool]


# TransformConfigParameterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['bool', 'complex', 'float', 'int', 'list', 'null', 'str']
- **Required**: Yes

### ValidationRule
- **Type**: typing.Optional[str]

### ValidationMessage
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[typing.List[str]]

### ListType
- **Type**: typing.Optional[typing.Literal['bool', 'complex', 'float', 'int', 'list', 'null', 'str']]

### IsOptional
- **Type**: typing.Optional[bool]


# TransformEncryption

### MlUserDataEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.MLUserDataEncryption]

### TaskRunSecurityConfigurationName
- **Type**: typing.Optional[str]


# TransformFilterCriteria

### Name
- **Type**: typing.Optional[str]

### TransformType
- **Type**: typing.Optional[typing.Literal['FIND_MATCHES']]

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'NOT_READY', 'READY']]

### GlueVersion
- **Type**: typing.Optional[str]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Schema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.SchemaColumn]]


# TransformParameters

### TransformType
- **Type**: typing.Literal['FIND_MATCHES']
- **Required**: Yes

### FindMatchesParameters
- **Type**: <class 'NoneType'>


# TransformSortCriteria

### Column
- **Type**: typing.Literal['CREATED', 'LAST_MODIFIED', 'NAME', 'STATUS', 'TRANSFORM_TYPE']
- **Required**: Yes

### SortDirection
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# Trigger

### Name
- **Type**: typing.Optional[str]

### WorkflowName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CONDITIONAL', 'EVENT', 'ON_DEMAND', 'SCHEDULED']]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'ACTIVATING', 'CREATED', 'CREATING', 'DEACTIVATED', 'DEACTIVATING', 'DELETING', 'UPDATING']]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ActionOutput]]

### Predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.PredicateOutput]

### EventBatchingCondition
- **Type**: <class 'NoneType'>


# TriggerNodeDetails

### Trigger
- **Type**: <class 'NoneType'>


# TriggerUpdate

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Action, aws_resource_validator.pydantic_models.glue.glue_classes.ActionOutput]]]

### Predicate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.Predicate, aws_resource_validator.pydantic_models.glue.glue_classes.PredicateOutput, NoneType]

### EventBatchingCondition
- **Type**: <class 'NoneType'>


# UnfilteredPartition

### Partition
- **Type**: <class 'NoneType'>

### AuthorizedColumns
- **Type**: typing.Optional[typing.List[str]]

### IsRegisteredWithLakeFormation
- **Type**: typing.Optional[bool]


# UnionOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### UnionType
- **Type**: typing.Literal['ALL', 'DISTINCT']
- **Required**: Yes


# UnionType

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### UnionType
- **Type**: typing.Literal['ALL', 'DISTINCT']
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToRemove
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateBlueprintRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BlueprintLocation
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateBlueprintResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCatalogRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.CatalogInput'>
- **Required**: Yes


# UpdateClassifierRequest

### GrokClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.UpdateGrokClassifierRequest]

### XMLClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.UpdateXMLClassifierRequest]

### JsonClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.UpdateJsonClassifierRequest]

### CsvClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.UpdateCsvClassifierRequest]


# UpdateColumnStatisticsForPartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.List[str]
- **Required**: Yes

### ColumnStatisticsList
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatistics, aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateColumnStatisticsForPartitionResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateColumnStatisticsForTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnStatisticsList
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatistics, aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateColumnStatisticsForTableResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ColumnStatisticsError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateColumnStatisticsTaskSettingsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### ColumnNameList
- **Type**: typing.Optional[typing.List[str]]

### SampleSize
- **Type**: typing.Optional[float]

### CatalogID
- **Type**: typing.Optional[str]

### SecurityConfiguration
- **Type**: typing.Optional[str]


# UpdateConnectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ConnectionInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateCrawlerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.CrawlerTargets, aws_resource_validator.pydantic_models.glue.glue_classes.CrawlerTargetsOutput, NoneType]

### Schedule
- **Type**: typing.Optional[str]

### Classifiers
- **Type**: typing.Optional[typing.List[str]]

### TablePrefix
- **Type**: typing.Optional[str]

### SchemaChangePolicy
- **Type**: <class 'NoneType'>

### RecrawlPolicy
- **Type**: <class 'NoneType'>

### LineageConfiguration
- **Type**: <class 'NoneType'>

### LakeFormationConfiguration
- **Type**: <class 'NoneType'>

### Configuration
- **Type**: typing.Optional[str]

### CrawlerSecurityConfiguration
- **Type**: typing.Optional[str]


# UpdateCrawlerScheduleRequest

### CrawlerName
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Optional[str]


# UpdateCsvClassifierRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Delimiter
- **Type**: typing.Optional[str]

### QuoteSymbol
- **Type**: typing.Optional[str]

### ContainsHeader
- **Type**: typing.Optional[typing.Literal['ABSENT', 'PRESENT', 'UNKNOWN']]

### Header
- **Type**: typing.Optional[typing.List[str]]

### DisableValueTrimming
- **Type**: typing.Optional[bool]

### AllowSingleColumn
- **Type**: typing.Optional[bool]

### CustomDatatypeConfigured
- **Type**: typing.Optional[bool]

### CustomDatatypes
- **Type**: typing.Optional[typing.List[str]]

### Serde
- **Type**: typing.Optional[typing.Literal['LazySimpleSerDe', 'None', 'OpenCSVSerDe']]


# UpdateDataQualityRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Ruleset
- **Type**: typing.Optional[str]


# UpdateDataQualityRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDatabaseRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.DatabaseInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateDevEndpointRequest

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### PublicKey
- **Type**: typing.Optional[str]

### AddPublicKeys
- **Type**: typing.Optional[typing.List[str]]

### DeletePublicKeys
- **Type**: typing.Optional[typing.List[str]]

### CustomLibraries
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.DevEndpointCustomLibraries]

### UpdateEtlLibraries
- **Type**: typing.Optional[bool]

### DeleteArguments
- **Type**: typing.Optional[typing.List[str]]

### AddArguments
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateGrokClassifierRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Classification
- **Type**: typing.Optional[str]

### GrokPattern
- **Type**: typing.Optional[str]

### CustomPatterns
- **Type**: typing.Optional[str]


# UpdateIntegrationResourcePropertyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: <class 'NoneType'>

### TargetProcessingProperties
- **Type**: <class 'NoneType'>


# UpdateIntegrationResourcePropertyResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SourceProcessingProperties'>
- **Required**: Yes

### TargetProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TargetProcessingProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIntegrationTablePropertiesRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTableConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.SourceTableConfig, aws_resource_validator.pydantic_models.glue.glue_classes.SourceTableConfigOutput, NoneType]

### TargetTableConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.TargetTableConfig, aws_resource_validator.pydantic_models.glue.glue_classes.TargetTableConfigOutput, NoneType]


# UpdateJobFromSourceControlRequest

### JobName
- **Type**: typing.Optional[str]

### Provider
- **Type**: typing.Optional[typing.Literal['AWS_CODE_COMMIT', 'BITBUCKET', 'GITHUB', 'GITLAB']]

### RepositoryName
- **Type**: typing.Optional[str]

### RepositoryOwner
- **Type**: typing.Optional[str]

### BranchName
- **Type**: typing.Optional[str]

### Folder
- **Type**: typing.Optional[str]

### CommitId
- **Type**: typing.Optional[str]

### AuthStrategy
- **Type**: typing.Optional[typing.Literal['AWS_SECRETS_MANAGER', 'PERSONAL_ACCESS_TOKEN']]

### AuthToken
- **Type**: typing.Optional[str]


# UpdateJobFromSourceControlResponse

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateJobRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.JobUpdate'>
- **Required**: Yes


# UpdateJobResponse

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateJsonClassifierRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JsonPath
- **Type**: typing.Optional[str]


# UpdateMLTransformRequest

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.TransformParameters]

### Role
- **Type**: typing.Optional[str]

### GlueVersion
- **Type**: typing.Optional[str]

### MaxCapacity
- **Type**: typing.Optional[float]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxRetries
- **Type**: typing.Optional[int]


# UpdateMLTransformResponse

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePartitionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValueList
- **Type**: typing.List[str]
- **Required**: Yes

### PartitionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.PartitionInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateRegistryInput

### RegistryId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.RegistryId'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRegistryResponse

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSchemaInput

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.SchemaId'>
- **Required**: Yes

### SchemaVersionNumber
- **Type**: <class 'NoneType'>

### Compatibility
- **Type**: typing.Optional[typing.Literal['BACKWARD', 'BACKWARD_ALL', 'DISABLED', 'FORWARD', 'FORWARD_ALL', 'FULL', 'FULL_ALL', 'NONE']]

### Description
- **Type**: typing.Optional[str]


# UpdateSchemaResponse

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSourceControlFromJobRequest

### JobName
- **Type**: typing.Optional[str]

### Provider
- **Type**: typing.Optional[typing.Literal['AWS_CODE_COMMIT', 'BITBUCKET', 'GITHUB', 'GITLAB']]

### RepositoryName
- **Type**: typing.Optional[str]

### RepositoryOwner
- **Type**: typing.Optional[str]

### BranchName
- **Type**: typing.Optional[str]

### Folder
- **Type**: typing.Optional[str]

### CommitId
- **Type**: typing.Optional[str]

### AuthStrategy
- **Type**: typing.Optional[typing.Literal['AWS_SECRETS_MANAGER', 'PERSONAL_ACCESS_TOKEN']]

### AuthToken
- **Type**: typing.Optional[str]


# UpdateSourceControlFromJobResponse

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTableOptimizerRequest

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['compaction', 'orphan_file_deletion', 'retention']
- **Required**: Yes

### TableOptimizerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TableOptimizerConfiguration'>
- **Required**: Yes


# UpdateTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TableInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### SkipArchive
- **Type**: typing.Optional[bool]

### TransactionId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### ViewUpdateAction
- **Type**: typing.Optional[typing.Literal['ADD', 'ADD_OR_REPLACE', 'DROP', 'REPLACE']]

### Force
- **Type**: typing.Optional[bool]


# UpdateTriggerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TriggerUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.TriggerUpdate'>
- **Required**: Yes


# UpdateTriggerResponse

### Trigger
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.Trigger'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUsageProfileRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glue.glue_classes.ProfileConfiguration, aws_resource_validator.pydantic_models.glue.glue_classes.ProfileConfigurationOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateUsageProfileResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserDefinedFunctionRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.UserDefinedFunctionInput'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateWorkflowRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DefaultRunProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### MaxConcurrentRuns
- **Type**: typing.Optional[int]


# UpdateWorkflowResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue.glue_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateXMLClassifierRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Classification
- **Type**: typing.Optional[str]

### RowTag
- **Type**: typing.Optional[str]


# UpsertRedshiftTargetOptions

### TableLocation
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### UpsertKeys
- **Type**: typing.Optional[typing.List[str]]


# UpsertRedshiftTargetOptionsOutput

### TableLocation
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### UpsertKeys
- **Type**: typing.Optional[typing.List[str]]


# UsageProfileDefinition

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]


# UserDefinedFunction

### FunctionName
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### ClassName
- **Type**: typing.Optional[str]

### OwnerName
- **Type**: typing.Optional[str]

### OwnerType
- **Type**: typing.Optional[typing.Literal['GROUP', 'ROLE', 'USER']]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceUris
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ResourceUri]]

### CatalogId
- **Type**: typing.Optional[str]


# UserDefinedFunctionInput

### FunctionName
- **Type**: typing.Optional[str]

### ClassName
- **Type**: typing.Optional[str]

### OwnerName
- **Type**: typing.Optional[str]

### OwnerType
- **Type**: typing.Optional[typing.Literal['GROUP', 'ROLE', 'USER']]

### ResourceUris
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ResourceUri]]


# ViewDefinition

### IsProtected
- **Type**: typing.Optional[bool]

### Definer
- **Type**: typing.Optional[str]

### SubObjects
- **Type**: typing.Optional[typing.List[str]]

### Representations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ViewRepresentation]]


# ViewDefinitionInput

### IsProtected
- **Type**: typing.Optional[bool]

### Definer
- **Type**: typing.Optional[str]

### Representations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.ViewRepresentationInput]]

### SubObjects
- **Type**: typing.Optional[typing.List[str]]


# ViewRepresentation

### Dialect
- **Type**: typing.Optional[typing.Literal['ATHENA', 'REDSHIFT', 'SPARK']]

### DialectVersion
- **Type**: typing.Optional[str]

### ViewOriginalText
- **Type**: typing.Optional[str]

### ViewExpandedText
- **Type**: typing.Optional[str]

### ValidationConnection
- **Type**: typing.Optional[str]

### IsStale
- **Type**: typing.Optional[bool]


# ViewRepresentationInput

### Dialect
- **Type**: typing.Optional[typing.Literal['ATHENA', 'REDSHIFT', 'SPARK']]

### DialectVersion
- **Type**: typing.Optional[str]

### ViewOriginalText
- **Type**: typing.Optional[str]

### ValidationConnection
- **Type**: typing.Optional[str]

### ViewExpandedText
- **Type**: typing.Optional[str]


# ViewValidation

### Dialect
- **Type**: typing.Optional[typing.Literal['ATHENA', 'REDSHIFT', 'SPARK']]

### DialectVersion
- **Type**: typing.Optional[str]

### ViewValidationText
- **Type**: typing.Optional[str]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'QUEUED', 'STOPPED', 'SUCCESS']]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.ErrorDetail]


# Workflow

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRunProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### LastRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.WorkflowRun]

### Graph
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.WorkflowGraph]

### MaxConcurrentRuns
- **Type**: typing.Optional[int]

### BlueprintDetails
- **Type**: <class 'NoneType'>


# WorkflowGraph

### Nodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Node]]

### Edges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue.glue_classes.Edge]]


# WorkflowRun

### Name
- **Type**: typing.Optional[str]

### WorkflowRunId
- **Type**: typing.Optional[str]

### PreviousRunId
- **Type**: typing.Optional[str]

### WorkflowRunProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### CompletedOn
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'ERROR', 'RUNNING', 'STOPPED', 'STOPPING']]

### ErrorMessage
- **Type**: typing.Optional[str]

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.WorkflowRunStatistics]

### Graph
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue.glue_classes.WorkflowGraph]

### StartingEventBatchCondition
- **Type**: <class 'NoneType'>


# WorkflowRunStatistics

### TotalActions
- **Type**: typing.Optional[int]

### TimeoutActions
- **Type**: typing.Optional[int]

### FailedActions
- **Type**: typing.Optional[int]

### StoppedActions
- **Type**: typing.Optional[int]

### SucceededActions
- **Type**: typing.Optional[int]

### RunningActions
- **Type**: typing.Optional[int]

### ErroredActions
- **Type**: typing.Optional[int]

### WaitingActions
- **Type**: typing.Optional[int]


# XMLClassifier

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Classification
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[int]

### RowTag
- **Type**: typing.Optional[str]



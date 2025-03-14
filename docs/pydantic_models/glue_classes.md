# Glue Classes

# ActionOutputTypeDef

### JobName
- **Type**: typing.Optional[str]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Timeout
- **Type**: typing.Optional[int]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NotificationPropertyTypeDef]

### CrawlerName
- **Type**: typing.Optional[str]


# ActionTypeDef

### JobName
- **Type**: typing.Optional[str]

### Arguments
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Timeout
- **Type**: typing.Optional[int]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NotificationPropertyTypeDef]

### CrawlerName
- **Type**: typing.Optional[str]


# ActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregateOperationOutputTypeDef

### Column
- **Type**: typing.List[str]
- **Required**: Yes

### AggFunc
- **Type**: typing.Literal['avg', 'count', 'countDistinct', 'first', 'kurtosis', 'last', 'max', 'min', 'skewness', 'stddev_pop', 'stddev_samp', 'sum', 'sumDistinct', 'var_pop', 'var_samp']
- **Required**: Yes


# AggregateOperationTypeDef

### Column
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AggFunc
- **Type**: typing.Literal['avg', 'count', 'countDistinct', 'first', 'kurtosis', 'last', 'max', 'min', 'skewness', 'stddev_pop', 'stddev_samp', 'sum', 'sumDistinct', 'var_pop', 'var_samp']
- **Required**: Yes


# AggregateOperationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregateOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.AggregateOperationOutputTypeDef]
- **Required**: Yes


# AggregateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Groups
- **Type**: typing.Sequence[typing.Sequence[str]]
- **Required**: Yes

### Aggs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.AggregateOperationUnionTypeDef]
- **Required**: Yes


# AllowedValueTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# AmazonRedshiftAdvancedOptionTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AmazonRedshiftNodeDataOutputTypeDef

### AccessType
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### CatalogDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### CatalogTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### CatalogRedshiftSchema
- **Type**: typing.Optional[str]

### CatalogRedshiftTable
- **Type**: typing.Optional[str]

### TempDir
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.AmazonRedshiftAdvancedOptionTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]]

### StagingTable
- **Type**: typing.Optional[str]

### SelectedColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]]


# AmazonRedshiftNodeDataTypeDef

### AccessType
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### CatalogDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### CatalogTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### CatalogRedshiftSchema
- **Type**: typing.Optional[str]

### CatalogRedshiftTable
- **Type**: typing.Optional[str]

### TempDir
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.AmazonRedshiftAdvancedOptionTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]]

### StagingTable
- **Type**: typing.Optional[str]

### SelectedColumns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]]


# AmazonRedshiftNodeDataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AmazonRedshiftSourceOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AmazonRedshiftNodeDataOutputTypeDef]


# AmazonRedshiftSourceTypeDef

### Name
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AmazonRedshiftNodeDataUnionTypeDef]


# AmazonRedshiftTargetOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AmazonRedshiftNodeDataOutputTypeDef]

### Inputs
- **Type**: typing.Optional[typing.List[str]]


# AmazonRedshiftTargetTypeDef

### Name
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AmazonRedshiftNodeDataUnionTypeDef]

### Inputs
- **Type**: typing.Optional[typing.Sequence[str]]


# AnnotationErrorTypeDef

### ProfileId
- **Type**: typing.Optional[str]

### StatisticId
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# AthenaConnectorSourceOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# AthenaConnectorSourceTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# AuditContextTypeDef

### AdditionalAuditContext
- **Type**: typing.Optional[str]

### RequestedColumns
- **Type**: typing.Optional[typing.Sequence[str]]

### AllColumnsRequested
- **Type**: typing.Optional[bool]


# AuthConfigurationTypeDef

### AuthenticationType
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef'>
- **Required**: Yes

### SecretArn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]

### OAuth2Properties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]]

### BasicAuthenticationProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]]

### CustomAuthenticationProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]]


# AuthenticationConfigurationInputTypeDef

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['BASIC', 'CUSTOM', 'IAM', 'OAUTH2']]

### OAuth2Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OAuth2PropertiesInputTypeDef]

### SecretArn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### BasicAuthenticationCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.BasicAuthenticationCredentialsTypeDef]

### CustomAuthenticationCredentials
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AuthenticationConfigurationTypeDef

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['BASIC', 'CUSTOM', 'IAM', 'OAUTH2']]

### SecretArn
- **Type**: typing.Optional[str]

### OAuth2Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OAuth2PropertiesTypeDef]


# AuthorizationCodePropertiesTypeDef

### AuthorizationCode
- **Type**: typing.Optional[str]

### RedirectUri
- **Type**: typing.Optional[str]


# BackfillErrorTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['ENCRYPTED_PARTITION_ERROR', 'INTERNAL_ERROR', 'INVALID_PARTITION_TYPE_DATA_ERROR', 'MISSING_PARTITION_VALUE_ERROR', 'UNSUPPORTED_PARTITION_CHARACTER_ERROR']]

### Partitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.PartitionValueListOutputTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthenticationCredentialsTypeDef

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# BasicCatalogTargetOutputTypeDef

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


# BasicCatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]


# BatchCreatePartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionInputList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.PartitionInputTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchCreatePartitionResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.PartitionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteConnectionRequestTypeDef

### ConnectionNameList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchDeleteConnectionResponseTypeDef

### Succeeded
- **Type**: typing.List[str]
- **Required**: Yes

### Errors
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeletePartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionsToDelete
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.PartitionValueListUnionTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchDeletePartitionResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.PartitionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteTableRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TablesToDelete
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]


# BatchDeleteTableResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TableErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteTableVersionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchDeleteTableVersionResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TableVersionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetBlueprintsRequestTypeDef

### Names
- **Type**: typing.Sequence[str]
- **Required**: Yes

### IncludeBlueprint
- **Type**: typing.Optional[bool]

### IncludeParameterSpec
- **Type**: typing.Optional[bool]


# BatchGetBlueprintsResponseTypeDef

### Blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.BlueprintTypeDef]
- **Required**: Yes

### MissingBlueprints
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetCrawlersRequestTypeDef

### CrawlerNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetCrawlersResponseTypeDef

### Crawlers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CrawlerTypeDef]
- **Required**: Yes

### CrawlersNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetCustomEntityTypesRequestTypeDef

### Names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetCustomEntityTypesResponseTypeDef

### CustomEntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CustomEntityTypeTypeDef]
- **Required**: Yes

### CustomEntityTypesNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetDataQualityResultRequestTypeDef

### ResultIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDataQualityResultResponseTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityResultTypeDef]
- **Required**: Yes

### ResultsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetDevEndpointsRequestTypeDef

### DevEndpointNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDevEndpointsResponseTypeDef

### DevEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DevEndpointTypeDef]
- **Required**: Yes

### DevEndpointsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetJobsRequestTypeDef

### JobNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.JobTypeDef]
- **Required**: Yes

### JobsNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetPartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionsToGet
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.PartitionValueListUnionTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchGetPartitionResponseTypeDef

### Partitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.PartitionTypeDef]
- **Required**: Yes

### UnprocessedKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.PartitionValueListOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetTableOptimizerEntryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetTableOptimizerErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetTableOptimizerRequestTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.BatchGetTableOptimizerEntryTypeDef]
- **Required**: Yes


# BatchGetTableOptimizerResponseTypeDef

### TableOptimizers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.BatchTableOptimizerTypeDef]
- **Required**: Yes

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.BatchGetTableOptimizerErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetTriggersRequestTypeDef

### TriggerNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetTriggersResponseTypeDef

### Triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TriggerTypeDef]
- **Required**: Yes

### TriggersNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetWorkflowsRequestTypeDef

### Names
- **Type**: typing.Sequence[str]
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]


# BatchGetWorkflowsResponseTypeDef

### Workflows
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.WorkflowTypeDef]
- **Required**: Yes

### MissingWorkflows
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutDataQualityStatisticAnnotationRequestTypeDef

### InclusionAnnotations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.DatapointInclusionAnnotationTypeDef]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# BatchPutDataQualityStatisticAnnotationResponseTypeDef

### FailedInclusionAnnotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.AnnotationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchStopJobRunErrorTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]


# BatchStopJobRunRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobRunIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchStopJobRunResponseTypeDef

### SuccessfulSubmissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.BatchStopJobRunSuccessfulSubmissionTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.BatchStopJobRunErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchStopJobRunSuccessfulSubmissionTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]


# BatchTableOptimizerTypeDef

### catalogId
- **Type**: typing.Optional[str]

### databaseName
- **Type**: typing.Optional[str]

### tableName
- **Type**: typing.Optional[str]

### tableOptimizer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TableOptimizerTypeDef]


# BatchUpdatePartitionFailureEntryTypeDef

### PartitionValueList
- **Type**: typing.Optional[typing.List[str]]

### ErrorDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]


# BatchUpdatePartitionRequestEntryTypeDef

### PartitionValueList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PartitionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.PartitionInputTypeDef'>
- **Required**: Yes


# BatchUpdatePartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.BatchUpdatePartitionRequestEntryTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchUpdatePartitionResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.BatchUpdatePartitionFailureEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BinaryColumnStatisticsDataTypeDef

### MaximumLength
- **Type**: <class 'int'>
- **Required**: Yes

### AverageLength
- **Type**: <class 'float'>
- **Required**: Yes

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlueprintDetailsTypeDef

### BlueprintName
- **Type**: typing.Optional[str]

### RunId
- **Type**: typing.Optional[str]


# BlueprintRunTypeDef

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


# BlueprintTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LastActiveDefinitionTypeDef]


# BooleanColumnStatisticsDataTypeDef

### NumberOfTrues
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfFalses
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes


# CancelDataQualityRuleRecommendationRunRequestTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDataQualityRulesetEvaluationRunRequestTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMLTaskRunRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMLTaskRunResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelStatementRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'int'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# CapabilitiesTypeDef

### SupportedAuthenticationTypes
- **Type**: typing.List[typing.Literal['BASIC', 'CUSTOM', 'IAM', 'OAUTH2']]
- **Required**: Yes

### SupportedDataOperations
- **Type**: typing.List[typing.Literal['READ', 'WRITE']]
- **Required**: Yes

### SupportedComputeEnvironments
- **Type**: typing.List[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]
- **Required**: Yes


# CatalogDeltaSourceOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# CatalogDeltaSourceTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# CatalogEntryTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# CatalogHudiSourceOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# CatalogHudiSourceTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# CatalogImportStatusTypeDef

### ImportCompleted
- **Type**: typing.Optional[bool]

### ImportTime
- **Type**: typing.Optional[datetime.datetime]

### ImportedBy
- **Type**: typing.Optional[str]


# CatalogInputTypeDef

### Description
- **Type**: typing.Optional[str]

### FederatedCatalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FederatedCatalogTypeDef]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TargetRedshiftCatalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TargetRedshiftCatalogTypeDef]

### CatalogProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogPropertiesTypeDef]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.PrincipalPermissionsUnionTypeDef]]

### CreateDatabaseDefaultPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.PrincipalPermissionsUnionTypeDef]]


# CatalogKafkaSourceOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.KafkaStreamingSourceOptionsOutputTypeDef]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StreamingDataPreviewOptionsTypeDef]


# CatalogKafkaSourceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.KafkaStreamingSourceOptionsUnionTypeDef]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StreamingDataPreviewOptionsTypeDef]


# CatalogKinesisSourceOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.KinesisStreamingSourceOptionsOutputTypeDef]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StreamingDataPreviewOptionsTypeDef]


# CatalogKinesisSourceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.KinesisStreamingSourceOptionsUnionTypeDef]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StreamingDataPreviewOptionsTypeDef]


# CatalogPropertiesOutputTypeDef

### DataLakeAccessProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataLakeAccessPropertiesOutputTypeDef]

### CustomProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# CatalogPropertiesTypeDef

### DataLakeAccessProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataLakeAccessPropertiesTypeDef]

### CustomProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CatalogSchemaChangePolicyTypeDef

### EnableUpdateCatalog
- **Type**: typing.Optional[bool]

### UpdateBehavior
- **Type**: typing.Optional[typing.Literal['LOG', 'UPDATE_IN_DATABASE']]


# CatalogSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# CatalogTargetOutputTypeDef

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


# CatalogTargetTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Tables
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ConnectionName
- **Type**: typing.Optional[str]

### EventQueueArn
- **Type**: typing.Optional[str]

### DlqEventQueueArn
- **Type**: typing.Optional[str]


# CatalogTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TargetRedshiftCatalogTypeDef]

### FederatedCatalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FederatedCatalogTypeDef]

### CatalogProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogPropertiesOutputTypeDef]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.PrincipalPermissionsOutputTypeDef]]

### CreateDatabaseDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.PrincipalPermissionsOutputTypeDef]]


# CheckSchemaVersionValidityInputTypeDef

### DataFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'PROTOBUF']
- **Required**: Yes

### SchemaDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# CheckSchemaVersionValidityResponseTypeDef

### Valid
- **Type**: <class 'bool'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClassifierTypeDef

### GrokClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.GrokClassifierTypeDef]

### XMLClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.XMLClassifierTypeDef]

### JsonClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.JsonClassifierTypeDef]

### CsvClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CsvClassifierTypeDef]


# CloudWatchEncryptionTypeDef

### CloudWatchEncryptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SSE-KMS']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# CodeGenConfigurationNodeOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeGenConfigurationNodePaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeGenConfigurationNodeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeGenEdgeTypeDef

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### TargetParameter
- **Type**: typing.Optional[str]


# CodeGenNodeArgTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Param
- **Type**: typing.Optional[bool]


# CodeGenNodeOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### Args
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CodeGenNodeArgTypeDef]
- **Required**: Yes

### LineNumber
- **Type**: typing.Optional[int]


# CodeGenNodeTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### Args
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CodeGenNodeArgTypeDef]
- **Required**: Yes

### LineNumber
- **Type**: typing.Optional[int]


# CodeGenNodeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnErrorTypeDef

### ColumnName
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]


# ColumnImportanceTypeDef

### ColumnName
- **Type**: typing.Optional[str]

### Importance
- **Type**: typing.Optional[float]


# ColumnOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnRowFilterTypeDef

### ColumnName
- **Type**: typing.Optional[str]

### RowFilterExpression
- **Type**: typing.Optional[str]


# ColumnStatisticsDataOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnStatisticsDataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnStatisticsErrorTypeDef

### ColumnStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsOutputTypeDef]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]


# ColumnStatisticsOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsDataOutputTypeDef'>
- **Required**: Yes


# ColumnStatisticsTaskRunTypeDef

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


# ColumnStatisticsTaskSettingsTypeDef

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ScheduleTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ExecutionAttemptTypeDef]


# ColumnStatisticsTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnType
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzedTime
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef'>
- **Required**: Yes

### StatisticsData
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsDataUnionTypeDef'>
- **Required**: Yes


# ColumnStatisticsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CompactionMetricsTypeDef

### IcebergMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.IcebergCompactionMetricsTypeDef]


# ComputeEnvironmentConfigurationTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]
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


# ConditionExpressionTypeDef

### Condition
- **Type**: <class 'str'>
- **Required**: Yes

### TargetColumn
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# ConditionTypeDef

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


# ConfigurationObjectOutputTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]

### MinValue
- **Type**: typing.Optional[str]

### MaxValue
- **Type**: typing.Optional[str]


# ConfigurationObjectTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[typing.Sequence[str]]

### MinValue
- **Type**: typing.Optional[str]

### MaxValue
- **Type**: typing.Optional[str]


# ConfusionMatrixTypeDef

### NumTruePositives
- **Type**: typing.Optional[int]

### NumFalsePositives
- **Type**: typing.Optional[int]

### NumTrueNegatives
- **Type**: typing.Optional[int]

### NumFalseNegatives
- **Type**: typing.Optional[int]


# ConnectionInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']
- **Required**: Yes

### ConnectionProperties
- **Type**: typing.Mapping[typing.Literal['CLUSTER_IDENTIFIER', 'CONFIG_FILES', 'CONNECTION_URL', 'CONNECTOR_CLASS_NAME', 'CONNECTOR_TYPE', 'CONNECTOR_URL', 'CUSTOM_JDBC_CERT', 'CUSTOM_JDBC_CERT_STRING', 'DATABASE', 'ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD', 'ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD', 'ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD', 'ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD', 'ENCRYPTED_PASSWORD', 'ENDPOINT', 'ENDPOINT_TYPE', 'HOST', 'INSTANCE_ID', 'JDBC_CONNECTION_URL', 'JDBC_DRIVER_CLASS_NAME', 'JDBC_DRIVER_JAR_URI', 'JDBC_ENFORCE_SSL', 'JDBC_ENGINE', 'JDBC_ENGINE_VERSION', 'KAFKA_BOOTSTRAP_SERVERS', 'KAFKA_CLIENT_KEYSTORE', 'KAFKA_CLIENT_KEYSTORE_PASSWORD', 'KAFKA_CLIENT_KEY_PASSWORD', 'KAFKA_CUSTOM_CERT', 'KAFKA_SASL_GSSAPI_KEYTAB', 'KAFKA_SASL_GSSAPI_KRB5_CONF', 'KAFKA_SASL_GSSAPI_PRINCIPAL', 'KAFKA_SASL_GSSAPI_SERVICE', 'KAFKA_SASL_MECHANISM', 'KAFKA_SASL_PLAIN_PASSWORD', 'KAFKA_SASL_PLAIN_USERNAME', 'KAFKA_SASL_SCRAM_PASSWORD', 'KAFKA_SASL_SCRAM_SECRETS_ARN', 'KAFKA_SASL_SCRAM_USERNAME', 'KAFKA_SKIP_CUSTOM_CERT_VALIDATION', 'KAFKA_SSL_ENABLED', 'PASSWORD', 'PORT', 'REGION', 'ROLE_ARN', 'SECRET_ID', 'SKIP_CUSTOM_JDBC_CERT_VALIDATION', 'USERNAME', 'WORKGROUP_NAME'], str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### MatchCriteria
- **Type**: typing.Optional[typing.Sequence[str]]

### SparkProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AthenaProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PythonProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PhysicalConnectionRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PhysicalConnectionRequirementsUnionTypeDef]

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AuthenticationConfigurationInputTypeDef]

### ValidateCredentials
- **Type**: typing.Optional[bool]

### ValidateForComputeEnvironments
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]]


# ConnectionPasswordEncryptionTypeDef

### ReturnConnectionPasswordEncrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### AwsKmsKeyId
- **Type**: typing.Optional[str]


# ConnectionTypeBriefTypeDef

### ConnectionType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']]

### Description
- **Type**: typing.Optional[str]

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CapabilitiesTypeDef]


# ConnectionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PhysicalConnectionRequirementsOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AuthenticationConfigurationTypeDef]

### ConnectionSchemaVersion
- **Type**: typing.Optional[int]

### CompatibleComputeEnvironments
- **Type**: typing.Optional[typing.List[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]]


# ConnectionsListOutputTypeDef

### Connections
- **Type**: typing.Optional[typing.List[str]]


# ConnectionsListTypeDef

### Connections
- **Type**: typing.Optional[typing.Sequence[str]]


# ConnectionsListUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectorDataSourceOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# ConnectorDataSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaUnionTypeDef]]


# ConnectorDataTargetOutputTypeDef

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


# ConnectorDataTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### Inputs
- **Type**: typing.Optional[typing.Sequence[str]]


# CrawlTypeDef

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


# CrawlerHistoryTypeDef

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


# CrawlerMetricsTypeDef

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


# CrawlerNodeDetailsTypeDef

### Crawls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.CrawlTypeDef]]


# CrawlerTargetsOutputTypeDef

### S3Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.S3TargetOutputTypeDef]]

### JdbcTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.JdbcTargetOutputTypeDef]]

### MongoDBTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.MongoDBTargetTypeDef]]

### DynamoDBTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.DynamoDBTargetTypeDef]]

### CatalogTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.CatalogTargetOutputTypeDef]]

### DeltaTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.DeltaTargetOutputTypeDef]]

### IcebergTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.IcebergTargetOutputTypeDef]]

### HudiTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.HudiTargetOutputTypeDef]]


# CrawlerTargetsTypeDef

### S3Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.S3TargetTypeDef]]

### JdbcTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.JdbcTargetTypeDef]]

### MongoDBTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.MongoDBTargetTypeDef]]

### DynamoDBTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.DynamoDBTargetTypeDef]]

### CatalogTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CatalogTargetTypeDef]]

### DeltaTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.DeltaTargetTypeDef]]

### IcebergTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.IcebergTargetTypeDef]]

### HudiTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.HudiTargetTypeDef]]


# CrawlerTargetsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CrawlerTypeDef

### Name
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CrawlerTargetsOutputTypeDef]

### DatabaseName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Classifiers
- **Type**: typing.Optional[typing.List[str]]

### RecrawlPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RecrawlPolicyTypeDef]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaChangePolicyTypeDef]

### LineageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LineageConfigurationTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['READY', 'RUNNING', 'STOPPING']]

### TablePrefix
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ScheduleTypeDef]

### CrawlElapsedTime
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### LastCrawl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LastCrawlInfoTypeDef]

### Version
- **Type**: typing.Optional[int]

### Configuration
- **Type**: typing.Optional[str]

### CrawlerSecurityConfiguration
- **Type**: typing.Optional[str]

### LakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LakeFormationConfigurationTypeDef]


# CrawlsFilterTypeDef

### FieldName
- **Type**: typing.Optional[typing.Literal['CRAWL_ID', 'DPU_HOUR', 'END_TIME', 'START_TIME', 'STATE']]

### FilterOperator
- **Type**: typing.Optional[typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']]

### FieldValue
- **Type**: typing.Optional[str]


# CreateBlueprintRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BlueprintLocation
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateBlueprintResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCatalogRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.CatalogInputTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateClassifierRequestTypeDef

### GrokClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CreateGrokClassifierRequestTypeDef]

### XMLClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CreateXMLClassifierRequestTypeDef]

### JsonClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CreateJsonClassifierRequestTypeDef]

### CsvClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CreateCsvClassifierRequestTypeDef]


# CreateColumnStatisticsTaskSettingsRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### SampleSize
- **Type**: typing.Optional[float]

### CatalogID
- **Type**: typing.Optional[str]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConnectionRequestTypeDef

### ConnectionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ConnectionInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConnectionResponseTypeDef

### CreateConnectionStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'READY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCrawlerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.CrawlerTargetsUnionTypeDef'>
- **Required**: Yes

### DatabaseName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### Classifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### TablePrefix
- **Type**: typing.Optional[str]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaChangePolicyTypeDef]

### RecrawlPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RecrawlPolicyTypeDef]

### LineageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LineageConfigurationTypeDef]

### LakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LakeFormationConfigurationTypeDef]

### Configuration
- **Type**: typing.Optional[str]

### CrawlerSecurityConfiguration
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCsvClassifierRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### DisableValueTrimming
- **Type**: typing.Optional[bool]

### AllowSingleColumn
- **Type**: typing.Optional[bool]

### CustomDatatypeConfigured
- **Type**: typing.Optional[bool]

### CustomDatatypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Serde
- **Type**: typing.Optional[typing.Literal['LazySimpleSerDe', 'None', 'OpenCSVSerDe']]


# CreateCustomEntityTypeRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### ContextWords
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCustomEntityTypeResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataQualityRulesetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityTargetTableTypeDef]

### DataQualitySecurityConfiguration
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# CreateDataQualityRulesetResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatabaseRequestTypeDef

### DatabaseInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DatabaseInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDevEndpointRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetId
- **Type**: typing.Optional[str]

### PublicKey
- **Type**: typing.Optional[str]

### PublicKeys
- **Type**: typing.Optional[typing.Sequence[str]]

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Arguments
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDevEndpointResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGrokClassifierRequestTypeDef

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


# CreateIntegrationRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.TagTypeDef]]


# CreateIntegrationResourcePropertyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SourceProcessingPropertiesTypeDef]

### TargetProcessingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TargetProcessingPropertiesTypeDef]


# CreateIntegrationResourcePropertyResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SourceProcessingPropertiesTypeDef'>
- **Required**: Yes

### TargetProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TargetProcessingPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TagTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING', 'NEEDS_ATTENTION', 'SYNCING']
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.IntegrationErrorTypeDef]
- **Required**: Yes

### DataFilter
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationTablePropertiesRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTableConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SourceTableConfigUnionTypeDef]

### TargetTableConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TargetTableConfigUnionTypeDef]


# CreateJobRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Command
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.JobCommandTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ExecutionPropertyTypeDef]

### DefaultArguments
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NonOverridableArguments
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ConnectionsListUnionTypeDef]

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NotificationProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NotificationPropertyTypeDef]

### GlueVersion
- **Type**: typing.Optional[str]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### CodeGenConfigurationNodes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.glue_classes.CodeGenConfigurationNodeUnionTypeDef]]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### SourceControlDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SourceControlDetailsTypeDef]

### MaintenanceWindow
- **Type**: typing.Optional[str]


# CreateJobResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJsonClassifierRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JsonPath
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMLTransformRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InputRecordTables
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueTableUnionTypeDef]
- **Required**: Yes

### Parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TransformParametersTypeDef'>
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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TransformEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TransformEncryptionTypeDef]


# CreateMLTransformResponseTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePartitionIndexRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionIndex
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.PartitionIndexTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreatePartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.PartitionInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreateRegistryInputTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRegistryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSchemaInputTypeDef

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'PROTOBUF']
- **Required**: Yes

### RegistryId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RegistryIdTypeDef]

### Compatibility
- **Type**: typing.Optional[typing.Literal['BACKWARD', 'BACKWARD_ALL', 'DISABLED', 'FORWARD', 'FORWARD_ALL', 'FULL', 'FULL_ALL', 'NONE']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SchemaDefinition
- **Type**: typing.Optional[str]


# CreateSchemaResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateScriptRequestTypeDef

### DagNodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CodeGenNodeUnionTypeDef]]

### DagEdges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CodeGenEdgeTypeDef]]

### Language
- **Type**: typing.Optional[typing.Literal['PYTHON', 'SCALA']]


# CreateScriptResponseTypeDef

### PythonScript
- **Type**: <class 'str'>
- **Required**: Yes

### ScalaCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecurityConfigurationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.EncryptionConfigurationUnionTypeDef'>
- **Required**: Yes


# CreateSecurityConfigurationResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSessionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Command
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SessionCommandTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### IdleTimeout
- **Type**: typing.Optional[int]

### DefaultArguments
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ConnectionsListUnionTypeDef]

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestOrigin
- **Type**: typing.Optional[str]


# CreateSessionResponseTypeDef

### Session
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTableRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TableInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PartitionIndexes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.PartitionIndexTypeDef]]

### TransactionId
- **Type**: typing.Optional[str]

### OpenTableFormatInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OpenTableFormatInputTypeDef]


# CreateTriggerResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUsageProfileRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ProfileConfigurationUnionTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateUsageProfileResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserDefinedFunctionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.UserDefinedFunctionInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreateWorkflowRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DefaultRunProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### MaxConcurrentRuns
- **Type**: typing.Optional[int]


# CreateWorkflowResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateXMLClassifierRequestTypeDef

### Classification
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RowTag
- **Type**: typing.Optional[str]


# CsvClassifierTypeDef

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


# CustomCodeOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# CustomCodeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### ClassName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# CustomEntityTypeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### ContextWords
- **Type**: typing.Optional[typing.List[str]]


# DQResultsPublishingOptionsTypeDef

### EvaluationContext
- **Type**: typing.Optional[str]

### ResultsS3Prefix
- **Type**: typing.Optional[str]

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### ResultsPublishingEnabled
- **Type**: typing.Optional[bool]


# DQStopJobOnFailureOptionsTypeDef

### StopJobOnFailureTiming
- **Type**: typing.Optional[typing.Literal['AfterDataLoad', 'Immediate']]


# DataCatalogEncryptionSettingsTypeDef

### EncryptionAtRest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.EncryptionAtRestTypeDef]

### ConnectionPasswordEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ConnectionPasswordEncryptionTypeDef]


# DataLakeAccessPropertiesOutputTypeDef

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


# DataLakeAccessPropertiesTypeDef

### DataLakeAccess
- **Type**: typing.Optional[bool]

### DataTransferRole
- **Type**: typing.Optional[str]

### KmsKey
- **Type**: typing.Optional[str]

### CatalogType
- **Type**: typing.Optional[str]


# DataLakePrincipalTypeDef

### DataLakePrincipalIdentifier
- **Type**: typing.Optional[str]


# DataQualityAnalyzerResultTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EvaluationMessage
- **Type**: typing.Optional[str]

### EvaluatedMetrics
- **Type**: typing.Optional[typing.Dict[str, float]]


# DataQualityEncryptionTypeDef

### DataQualityEncryptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SSE-KMS']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# DataQualityEvaluationRunAdditionalRunOptionsTypeDef

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### ResultsS3Prefix
- **Type**: typing.Optional[str]

### CompositeRuleEvaluationMethod
- **Type**: typing.Optional[typing.Literal['COLUMN', 'ROW']]


# DataQualityMetricValuesTypeDef

### ActualValue
- **Type**: typing.Optional[float]

### ExpectedValue
- **Type**: typing.Optional[float]

### LowerLimit
- **Type**: typing.Optional[float]

### UpperLimit
- **Type**: typing.Optional[float]


# DataQualityObservationTypeDef

### Description
- **Type**: typing.Optional[str]

### MetricBasedObservation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.MetricBasedObservationTypeDef]


# DataQualityResultDescriptionTypeDef

### ResultId
- **Type**: typing.Optional[str]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataSourceOutputTypeDef]

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]


# DataQualityResultFilterCriteriaTypeDef

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataSourceUnionTypeDef]

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]

### StartedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### StartedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# DataQualityResultTypeDef

### ResultId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataSourceOutputTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityRuleResultTypeDef]]

### AnalyzerResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityAnalyzerResultTypeDef]]

### Observations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityObservationTypeDef]]


# DataQualityRuleRecommendationRunDescriptionTypeDef

### RunId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataSourceOutputTypeDef]


# DataQualityRuleRecommendationRunFilterTypeDef

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataSourceUnionTypeDef'>
- **Required**: Yes

### StartedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### StartedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# DataQualityRuleResultTypeDef

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


# DataQualityRulesetEvaluationRunDescriptionTypeDef

### RunId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataSourceOutputTypeDef]


# DataQualityRulesetEvaluationRunFilterTypeDef

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataSourceUnionTypeDef'>
- **Required**: Yes

### StartedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### StartedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# DataQualityRulesetFilterCriteriaTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### LastModifiedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### LastModifiedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityTargetTableTypeDef]


# DataQualityRulesetListDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityTargetTableTypeDef]

### RecommendationRunId
- **Type**: typing.Optional[str]

### RuleCount
- **Type**: typing.Optional[int]


# DataQualityTargetTableTypeDef

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DataSourceOutputTypeDef

### GlueTable
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.GlueTableOutputTypeDef'>
- **Required**: Yes


# DataSourceTypeDef

### GlueTable
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.GlueTableUnionTypeDef'>
- **Required**: Yes


# DataSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatabaseIdentifierTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# DatabaseInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LocationUri
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.PrincipalPermissionsUnionTypeDef]]

### TargetDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DatabaseIdentifierTypeDef]

### FederatedDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FederatedDatabaseTypeDef]


# DatabaseTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.PrincipalPermissionsOutputTypeDef]]

### TargetDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DatabaseIdentifierTypeDef]

### CatalogId
- **Type**: typing.Optional[str]

### FederatedDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FederatedDatabaseTypeDef]


# DatapointInclusionAnnotationTypeDef

### ProfileId
- **Type**: typing.Optional[str]

### StatisticId
- **Type**: typing.Optional[str]

### InclusionAnnotation
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# DatatypeTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes


# DateColumnStatisticsDataOutputTypeDef

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


# DateColumnStatisticsDataTypeDef

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### MaximumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# DecimalColumnStatisticsDataOutputTypeDef

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DecimalNumberOutputTypeDef]

### MaximumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DecimalNumberOutputTypeDef]


# DecimalColumnStatisticsDataTypeDef

### NumberOfNulls
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfDistinctValues
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DecimalNumberUnionTypeDef]

### MaximumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DecimalNumberUnionTypeDef]


# DecimalNumberOutputTypeDef

### UnscaledValue
- **Type**: <class 'bytes'>
- **Required**: Yes

### Scale
- **Type**: <class 'int'>
- **Required**: Yes


# DecimalNumberTypeDef

### UnscaledValue
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.BlobTypeDef'>
- **Required**: Yes

### Scale
- **Type**: <class 'int'>
- **Required**: Yes


# DecimalNumberUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteBlueprintRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBlueprintResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCatalogRequestTypeDef

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClassifierRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteColumnStatisticsForPartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteColumnStatisticsForTableRequestTypeDef

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


# DeleteColumnStatisticsTaskSettingsRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionRequestTypeDef

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteCrawlerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomEntityTypeRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomEntityTypeResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataQualityRulesetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatabaseRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteDevEndpointRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationRequestTypeDef

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TagTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING', 'NEEDS_ATTENTION', 'SYNCING']
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.IntegrationErrorTypeDef]
- **Required**: Yes

### DataFilter
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIntegrationTablePropertiesRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobResponseTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMLTransformRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMLTransformResponseTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePartitionIndexRequestTypeDef

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


# DeletePartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteRegistryInputTypeDef

### RegistryId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.RegistryIdTypeDef'>
- **Required**: Yes


# DeleteRegistryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### PolicyHashCondition
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# DeleteSchemaInputTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes


# DeleteSchemaResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSchemaVersionsInputTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes

### Versions
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaVersionsResponseTypeDef

### SchemaVersionErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.SchemaVersionErrorItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSecurityConfigurationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSessionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# DeleteSessionResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTableRequestTypeDef

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


# DeleteTableVersionRequestTypeDef

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


# DeleteTriggerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTriggerResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUsageProfileRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserDefinedFunctionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteWorkflowRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeltaTargetOutputTypeDef

### DeltaTables
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### WriteManifest
- **Type**: typing.Optional[bool]

### CreateNativeDeltaTable
- **Type**: typing.Optional[bool]


# DeltaTargetTypeDef

### DeltaTables
- **Type**: typing.Optional[typing.Sequence[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### WriteManifest
- **Type**: typing.Optional[bool]

### CreateNativeDeltaTable
- **Type**: typing.Optional[bool]


# DescribeConnectionTypeRequestTypeDef

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectionTypeResponseTypeDef

### ConnectionType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.CapabilitiesTypeDef'>
- **Required**: Yes

### ConnectionProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]
- **Required**: Yes

### ConnectionOptions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]
- **Required**: Yes

### AuthenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.AuthConfigurationTypeDef'>
- **Required**: Yes

### ComputeEnvironmentConfigurations
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.ComputeEnvironmentConfigurationTypeDef]
- **Required**: Yes

### PhysicalConnectionRequirements
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]
- **Required**: Yes

### AthenaConnectionProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]
- **Required**: Yes

### PythonConnectionProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]
- **Required**: Yes

### SparkConnectionProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.PropertyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEntityRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# DescribeEntityRequestTypeDef

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


# DescribeEntityResponseTypeDef

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.FieldTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInboundIntegrationsRequestTypeDef

### IntegrationArn
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### TargetArn
- **Type**: typing.Optional[str]


# DescribeInboundIntegrationsResponseTypeDef

### InboundIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.InboundIntegrationTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIntegrationsRequestTypeDef

### IntegrationIdentifier
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.IntegrationFilterTypeDef]]


# DescribeIntegrationsResponseTypeDef

### Integrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.IntegrationTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DevEndpointCustomLibrariesTypeDef

### ExtraPythonLibsS3Path
- **Type**: typing.Optional[str]

### ExtraJarsS3Path
- **Type**: typing.Optional[str]


# DevEndpointTypeDef

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


# DirectJDBCSourceTypeDef

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


# DirectKafkaSourceOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.KafkaStreamingSourceOptionsOutputTypeDef]

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StreamingDataPreviewOptionsTypeDef]


# DirectKafkaSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.KafkaStreamingSourceOptionsUnionTypeDef]

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StreamingDataPreviewOptionsTypeDef]


# DirectKinesisSourceOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### StreamingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.KinesisStreamingSourceOptionsOutputTypeDef]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StreamingDataPreviewOptionsTypeDef]


# DirectKinesisSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WindowSize
- **Type**: typing.Optional[int]

### DetectSchema
- **Type**: typing.Optional[bool]

### StreamingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.KinesisStreamingSourceOptionsUnionTypeDef]

### DataPreviewOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StreamingDataPreviewOptionsTypeDef]


# DirectSchemaChangePolicyTypeDef

### EnableUpdateCatalog
- **Type**: typing.Optional[bool]

### UpdateBehavior
- **Type**: typing.Optional[typing.Literal['LOG', 'UPDATE_IN_DATABASE']]

### Table
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]


# DoubleColumnStatisticsDataTypeDef

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


# DropDuplicatesOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Columns
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# DropDuplicatesTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Columns
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]


# DropFieldsOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# DropFieldsTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Paths
- **Type**: typing.Sequence[typing.Sequence[str]]
- **Required**: Yes


# DropNullFieldsOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### NullCheckBoxList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NullCheckBoxListTypeDef]

### NullTextList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.NullValueFieldTypeDef]]


# DropNullFieldsTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NullCheckBoxList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NullCheckBoxListTypeDef]

### NullTextList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.NullValueFieldTypeDef]]


# DynamicTransformOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.TransformConfigParameterOutputTypeDef]]

### Version
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# DynamicTransformTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TransformName
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.TransformConfigParameterUnionTypeDef]]

### Version
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# DynamoDBCatalogSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# DynamoDBTargetTypeDef

### Path
- **Type**: typing.Optional[str]

### scanAll
- **Type**: typing.Optional[bool]

### scanRate
- **Type**: typing.Optional[float]


# EdgeTypeDef

### SourceId
- **Type**: typing.Optional[str]

### DestinationId
- **Type**: typing.Optional[str]


# EncryptionAtRestTypeDef

### CatalogEncryptionMode
- **Type**: typing.Literal['DISABLED', 'SSE-KMS', 'SSE-KMS-WITH-SERVICE-ROLE']
- **Required**: Yes

### SseAwsKmsKeyId
- **Type**: typing.Optional[str]

### CatalogEncryptionServiceRole
- **Type**: typing.Optional[str]


# EncryptionConfigurationOutputTypeDef

### S3Encryption
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.S3EncryptionTypeDef]]

### CloudWatchEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CloudWatchEncryptionTypeDef]

### JobBookmarksEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.JobBookmarksEncryptionTypeDef]

### DataQualityEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityEncryptionTypeDef]


# EncryptionConfigurationTypeDef

### S3Encryption
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.S3EncryptionTypeDef]]

### CloudWatchEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CloudWatchEncryptionTypeDef]

### JobBookmarksEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.JobBookmarksEncryptionTypeDef]

### DataQualityEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityEncryptionTypeDef]


# EncryptionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntityTypeDef

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


# ErrorDetailTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# ErrorDetailsTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# EvaluateDataQualityMultiFrameOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DQResultsPublishingOptionsTypeDef]

### AdditionalOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['observations.scope', 'performanceTuning.caching'], str]]

### StopJobOnFailureOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DQStopJobOnFailureOptionsTypeDef]


# EvaluateDataQualityMultiFrameTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalDataSources
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DQResultsPublishingOptionsTypeDef]

### AdditionalOptions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['observations.scope', 'performanceTuning.caching'], str]]

### StopJobOnFailureOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DQStopJobOnFailureOptionsTypeDef]


# EvaluateDataQualityOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DQResultsPublishingOptionsTypeDef]

### StopJobOnFailureOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DQStopJobOnFailureOptionsTypeDef]


# EvaluateDataQualityTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Ruleset
- **Type**: <class 'str'>
- **Required**: Yes

### Output
- **Type**: typing.Optional[typing.Literal['EvaluationResults', 'PrimaryInput']]

### PublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DQResultsPublishingOptionsTypeDef]

### StopJobOnFailureOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DQStopJobOnFailureOptionsTypeDef]


# EvaluationMetricsTypeDef

### TransformType
- **Type**: typing.Literal['FIND_MATCHES']
- **Required**: Yes

### FindMatchesMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FindMatchesMetricsTypeDef]


# EventBatchingConditionTypeDef

### BatchSize
- **Type**: <class 'int'>
- **Required**: Yes

### BatchWindow
- **Type**: typing.Optional[int]


# ExecutionAttemptTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'STARTED']]

### ColumnStatisticsTaskRunId
- **Type**: typing.Optional[str]

### ExecutionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]


# ExecutionPropertyTypeDef

### MaxConcurrentRuns
- **Type**: typing.Optional[int]


# ExportLabelsTaskRunPropertiesTypeDef

### OutputS3Path
- **Type**: typing.Optional[str]


# FederatedCatalogTypeDef

### Identifier
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]


# FederatedDatabaseTypeDef

### Identifier
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]


# FederatedTableTypeDef

### Identifier
- **Type**: typing.Optional[str]

### DatabaseIdentifier
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]


# FieldTypeDef

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


# FillMissingValuesOutputTypeDef

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


# FillMissingValuesTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ImputedPath
- **Type**: <class 'str'>
- **Required**: Yes

### FilledPath
- **Type**: typing.Optional[str]


# FilterExpressionOutputTypeDef

### Operation
- **Type**: typing.Literal['EQ', 'GT', 'GTE', 'ISNULL', 'LT', 'LTE', 'REGEX']
- **Required**: Yes

### Values
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.FilterValueOutputTypeDef]
- **Required**: Yes

### Negated
- **Type**: typing.Optional[bool]


# FilterExpressionTypeDef

### Operation
- **Type**: typing.Literal['EQ', 'GT', 'GTE', 'ISNULL', 'LT', 'LTE', 'REGEX']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.FilterValueUnionTypeDef]
- **Required**: Yes

### Negated
- **Type**: typing.Optional[bool]


# FilterExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.FilterExpressionOutputTypeDef]
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### LogicalOperator
- **Type**: typing.Literal['AND', 'OR']
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.FilterExpressionUnionTypeDef]
- **Required**: Yes


# FilterValueOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindMatchesMetricsTypeDef

### AreaUnderPRCurve
- **Type**: typing.Optional[float]

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### F1
- **Type**: typing.Optional[float]

### ConfusionMatrix
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ConfusionMatrixTypeDef]

### ColumnImportances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnImportanceTypeDef]]


# FindMatchesParametersTypeDef

### PrimaryKeyColumnName
- **Type**: typing.Optional[str]

### PrecisionRecallTradeoff
- **Type**: typing.Optional[float]

### AccuracyCostTradeoff
- **Type**: typing.Optional[float]

### EnforceProvidedLabels
- **Type**: typing.Optional[bool]


# FindMatchesTaskRunPropertiesTypeDef

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]


# GetBlueprintRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeBlueprint
- **Type**: typing.Optional[bool]

### IncludeParameterSpec
- **Type**: typing.Optional[bool]


# GetBlueprintResponseTypeDef

### Blueprint
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.BlueprintTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBlueprintRunRequestTypeDef

### BlueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBlueprintRunResponseTypeDef

### BlueprintRun
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.BlueprintRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBlueprintRunsRequestTypeDef

### BlueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetBlueprintRunsResponseTypeDef

### BlueprintRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.BlueprintRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCatalogImportStatusRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]


# GetCatalogImportStatusResponseTypeDef

### ImportStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.CatalogImportStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCatalogRequestTypeDef

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCatalogResponseTypeDef

### Catalog
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.CatalogTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCatalogsRequestTypeDef

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


# GetCatalogsResponseTypeDef

### CatalogList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CatalogTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetClassifierRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetClassifierResponseTypeDef

### Classifier
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ClassifierTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetClassifiersRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetClassifiersRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetClassifiersResponseTypeDef

### Classifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ClassifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetColumnStatisticsForPartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ColumnNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetColumnStatisticsForPartitionResponseTypeDef

### ColumnStatisticsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsOutputTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetColumnStatisticsForTableRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetColumnStatisticsForTableResponseTypeDef

### ColumnStatisticsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsOutputTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetColumnStatisticsTaskRunRequestTypeDef

### ColumnStatisticsTaskRunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetColumnStatisticsTaskRunResponseTypeDef

### ColumnStatisticsTaskRun
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsTaskRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetColumnStatisticsTaskRunsRequestTypeDef

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


# GetColumnStatisticsTaskRunsResponseTypeDef

### ColumnStatisticsTaskRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsTaskRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetColumnStatisticsTaskSettingsRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# GetColumnStatisticsTaskSettingsResponseTypeDef

### ColumnStatisticsTaskSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsTaskSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### HidePassword
- **Type**: typing.Optional[bool]

### ApplyOverrideForComputeEnvironment
- **Type**: typing.Optional[typing.Literal['ATHENA', 'PYTHON', 'SPARK']]


# GetConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectionsFilterTypeDef

### MatchCriteria
- **Type**: typing.Optional[typing.Sequence[str]]

### ConnectionType
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']]

### ConnectionSchemaVersion
- **Type**: typing.Optional[int]


# GetConnectionsRequestPaginateTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.GetConnectionsFilterTypeDef]

### HidePassword
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetConnectionsRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.GetConnectionsFilterTypeDef]

### HidePassword
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetConnectionsResponseTypeDef

### ConnectionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCrawlerMetricsRequestPaginateTypeDef

### CrawlerNameList
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetCrawlerMetricsRequestTypeDef

### CrawlerNameList
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCrawlerMetricsResponseTypeDef

### CrawlerMetricsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CrawlerMetricsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCrawlerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCrawlerResponseTypeDef

### Crawler
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.CrawlerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCrawlersRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetCrawlersRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCrawlersResponseTypeDef

### Crawlers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CrawlerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCustomEntityTypeRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomEntityTypeResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataCatalogEncryptionSettingsRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]


# GetDataCatalogEncryptionSettingsResponseTypeDef

### DataCatalogEncryptionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataCatalogEncryptionSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataQualityModelRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### StatisticId
- **Type**: typing.Optional[str]


# GetDataQualityModelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataQualityModelResultRequestTypeDef

### StatisticId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityModelResultResponseTypeDef

### CompletedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Model
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.StatisticModelResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataQualityResultRequestTypeDef

### ResultId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityResultResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataSourceOutputTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityRuleResultTypeDef]
- **Required**: Yes

### AnalyzerResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityAnalyzerResultTypeDef]
- **Required**: Yes

### Observations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityObservationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataQualityRuleRecommendationRunRequestTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityRuleRecommendationRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataSourceOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataQualityRulesetEvaluationRunRequestTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityRulesetEvaluationRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataSourceOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataQualityEvaluationRunAdditionalRunOptionsTypeDef'>
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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.DataSourceOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataQualityRulesetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataQualityRulesetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataQualityTargetTableTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDatabaseRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetDatabaseResponseTypeDef

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDatabasesRequestPaginateTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FEDERATED', 'FOREIGN']]

### AttributesToGet
- **Type**: typing.Optional[typing.Sequence[typing.Literal['NAME']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetDatabasesRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FEDERATED', 'FOREIGN']]

### AttributesToGet
- **Type**: typing.Optional[typing.Sequence[typing.Literal['NAME']]]


# GetDatabasesResponseTypeDef

### DatabaseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DatabaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDataflowGraphRequestTypeDef

### PythonScript
- **Type**: typing.Optional[str]


# GetDataflowGraphResponseTypeDef

### DagNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CodeGenNodeOutputTypeDef]
- **Required**: Yes

### DagEdges
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CodeGenEdgeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDevEndpointRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevEndpointResponseTypeDef

### DevEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DevEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDevEndpointsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetDevEndpointsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetDevEndpointsResponseTypeDef

### DevEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DevEndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetEntityRecordsRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### FilterPredicate
- **Type**: typing.Optional[str]

### OrderBy
- **Type**: typing.Optional[str]

### SelectedFields
- **Type**: typing.Optional[typing.Sequence[str]]


# GetEntityRecordsResponseTypeDef

### Records
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetIntegrationResourcePropertyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResourcePropertyResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SourceProcessingPropertiesTypeDef'>
- **Required**: Yes

### TargetProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TargetProcessingPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntegrationTablePropertiesRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationTablePropertiesResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTableConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SourceTableConfigOutputTypeDef'>
- **Required**: Yes

### TargetTableConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TargetTableConfigOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobBookmarkRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: typing.Optional[str]


# GetJobBookmarkResponseTypeDef

### JobBookmarkEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.JobBookmarkEntryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRunRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### PredecessorsIncluded
- **Type**: typing.Optional[bool]


# GetJobRunResponseTypeDef

### JobRun
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.JobRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRunsRequestPaginateTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetJobRunsRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetJobRunsResponseTypeDef

### JobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.JobRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetJobsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetJobsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetJobsResponsePaginatorTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.JobPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.JobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMLTaskRunRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMLTaskRunResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TaskRunPropertiesTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLTaskRunsRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TaskRunFilterCriteriaTypeDef]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TaskRunSortCriteriaTypeDef]


# GetMLTaskRunsResponseTypeDef

### TaskRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TaskRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMLTransformRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMLTransformResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueTableOutputTypeDef]
- **Required**: Yes

### Parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TransformParametersTypeDef'>
- **Required**: Yes

### EvaluationMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.EvaluationMetricsTypeDef'>
- **Required**: Yes

### LabelCount
- **Type**: <class 'int'>
- **Required**: Yes

### Schema
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.SchemaColumnTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TransformEncryptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLTransformsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TransformFilterCriteriaTypeDef]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TransformSortCriteriaTypeDef]


# GetMLTransformsResponseTypeDef

### Transforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.MLTransformTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMappingRequestTypeDef

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.CatalogEntryTypeDef'>
- **Required**: Yes

### Sinks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CatalogEntryTypeDef]]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LocationTypeDef]


# GetPartitionIndexesRequestPaginateTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetPartitionIndexesRequestTypeDef

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


# GetPartitionIndexesResponseTypeDef

### PartitionIndexDescriptorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.PartitionIndexDescriptorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetPartitionResponseTypeDef

### Partition
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.PartitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPartitionsRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SegmentTypeDef]

### ExcludeColumnSchema
- **Type**: typing.Optional[bool]

### TransactionId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetPartitionsRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SegmentTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### ExcludeColumnSchema
- **Type**: typing.Optional[bool]

### TransactionId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# GetPartitionsResponseTypeDef

### Partitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.PartitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPlanResponseTypeDef

### PythonScript
- **Type**: <class 'str'>
- **Required**: Yes

### ScalaCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegistryInputTypeDef

### RegistryId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.RegistryIdTypeDef'>
- **Required**: Yes


# GetRegistryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePoliciesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetResourcePoliciesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetResourcePoliciesResponseTypeDef

### GetResourcePoliciesResponseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.GluePolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: typing.Optional[str]


# GetResourcePolicyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaByDefinitionInputTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes

### SchemaDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaByDefinitionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaInputTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes


# GetSchemaResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaVersionInputTypeDef

### SchemaId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef]

### SchemaVersionId
- **Type**: typing.Optional[str]

### SchemaVersionNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaVersionNumberTypeDef]


# GetSchemaVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaVersionsDiffInputTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes

### FirstSchemaVersionNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaVersionNumberTypeDef'>
- **Required**: Yes

### SecondSchemaVersionNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaVersionNumberTypeDef'>
- **Required**: Yes

### SchemaDiffType
- **Type**: typing.Literal['SYNTAX_DIFF']
- **Required**: Yes


# GetSchemaVersionsDiffResponseTypeDef

### Diff
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSecurityConfigurationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSecurityConfigurationResponseTypeDef

### SecurityConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SecurityConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSecurityConfigurationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetSecurityConfigurationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetSecurityConfigurationsResponseTypeDef

### SecurityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.SecurityConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSessionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# GetSessionResponseTypeDef

### Session
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStatementRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'int'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# GetStatementResponseTypeDef

### Statement
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.StatementTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableOptimizerResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TableOptimizerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### IncludeStatusDetails
- **Type**: typing.Optional[bool]


# GetTableResponseTypeDef

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableVersionRequestTypeDef

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


# GetTableVersionResponseTypeDef

### TableVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TableVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableVersionsRequestPaginateTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetTableVersionsRequestTypeDef

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


# GetTableVersionsResponsePaginatorTypeDef

### TableVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TableVersionPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTableVersionsResponseTypeDef

### TableVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TableVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTablesRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### IncludeStatusDetails
- **Type**: typing.Optional[bool]

### AttributesToGet
- **Type**: typing.Optional[typing.Sequence[typing.Literal['NAME', 'TABLE_TYPE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetTablesRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### IncludeStatusDetails
- **Type**: typing.Optional[bool]

### AttributesToGet
- **Type**: typing.Optional[typing.Sequence[typing.Literal['NAME', 'TABLE_TYPE']]]


# GetTablesResponsePaginatorTypeDef

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TablePaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTablesResponseTypeDef

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TableTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTagsRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTagsResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTriggerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTriggerResponseTypeDef

### Trigger
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TriggerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTriggersRequestPaginateTypeDef

### DependentJobName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetTriggersRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### DependentJobName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetTriggersResponseTypeDef

### Triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TriggerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUnfilteredPartitionMetadataRequestTypeDef

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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SupportedPermissionTypes
- **Type**: typing.Sequence[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]

### AuditContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AuditContextTypeDef]

### QuerySessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.QuerySessionContextTypeDef]


# GetUnfilteredPartitionMetadataResponseTypeDef

### Partition
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.PartitionTypeDef'>
- **Required**: Yes

### AuthorizedColumns
- **Type**: typing.List[str]
- **Required**: Yes

### IsRegisteredWithLakeFormation
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUnfilteredPartitionsMetadataRequestTypeDef

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
- **Type**: typing.Sequence[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[str]

### AuditContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AuditContextTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### Segment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SegmentTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### QuerySessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.QuerySessionContextTypeDef]


# GetUnfilteredPartitionsMetadataResponseTypeDef

### UnfilteredPartitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.UnfilteredPartitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUnfilteredTableMetadataRequestTypeDef

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
- **Type**: typing.Sequence[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]

### AuditContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AuditContextTypeDef]

### ParentResourceArn
- **Type**: typing.Optional[str]

### RootResourceArn
- **Type**: typing.Optional[str]

### SupportedDialect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SupportedDialectTypeDef]

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DROP', 'INSERT', 'SELECT']]]

### QuerySessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.QuerySessionContextTypeDef]


# GetUnfilteredTableMetadataResponseTypeDef

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TableTypeDef'>
- **Required**: Yes

### AuthorizedColumns
- **Type**: typing.List[str]
- **Required**: Yes

### IsRegisteredWithLakeFormation
- **Type**: <class 'bool'>
- **Required**: Yes

### CellFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnRowFilterTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUsageProfileRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsageProfileResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ProfileConfigurationOutputTypeDef'>
- **Required**: Yes

### CreatedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserDefinedFunctionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetUserDefinedFunctionResponseTypeDef

### UserDefinedFunction
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.UserDefinedFunctionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserDefinedFunctionsResponseTypeDef

### UserDefinedFunctions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.UserDefinedFunctionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetWorkflowRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]


# GetWorkflowResponseTypeDef

### Workflow
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.WorkflowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowRunPropertiesRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowRunPropertiesResponseTypeDef

### RunProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowRunRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]


# GetWorkflowRunResponseTypeDef

### Run
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.WorkflowRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowRunsRequestPaginateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# GetWorkflowRunsRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGraph
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetWorkflowRunsResponseTypeDef

### Runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.WorkflowRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GluePolicyTypeDef

### PolicyInJson
- **Type**: typing.Optional[str]

### PolicyHash
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]


# GlueSchemaOutputTypeDef

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueStudioSchemaColumnTypeDef]]


# GlueSchemaTypeDef

### Columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueStudioSchemaColumnTypeDef]]


# GlueSchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GlueStudioSchemaColumnTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GlueTableOutputTypeDef

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


# GlueTableTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GlueTableUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GovernedCatalogSourceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3SourceAdditionalOptionsTypeDef]


# GovernedCatalogTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogSchemaChangePolicyTypeDef]


# GovernedCatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogSchemaChangePolicyTypeDef]


# GrokClassifierTypeDef

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


# HudiTargetOutputTypeDef

### Paths
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### MaximumTraversalDepth
- **Type**: typing.Optional[int]


# HudiTargetTypeDef

### Paths
- **Type**: typing.Optional[typing.Sequence[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.Sequence[str]]

### MaximumTraversalDepth
- **Type**: typing.Optional[int]


# IcebergCompactionMetricsTypeDef

### NumberOfBytesCompacted
- **Type**: typing.Optional[int]

### NumberOfFilesCompacted
- **Type**: typing.Optional[int]

### NumberOfDpus
- **Type**: typing.Optional[int]

### JobDurationInHour
- **Type**: typing.Optional[float]


# IcebergInputTypeDef

### MetadataOperation
- **Type**: typing.Literal['CREATE']
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# IcebergOrphanFileDeletionConfigurationTypeDef

### orphanFileRetentionPeriodInDays
- **Type**: typing.Optional[int]

### location
- **Type**: typing.Optional[str]


# IcebergOrphanFileDeletionMetricsTypeDef

### NumberOfOrphanFilesDeleted
- **Type**: typing.Optional[int]

### NumberOfDpus
- **Type**: typing.Optional[int]

### JobDurationInHour
- **Type**: typing.Optional[float]


# IcebergRetentionConfigurationTypeDef

### snapshotRetentionPeriodInDays
- **Type**: typing.Optional[int]

### numberOfSnapshotsToRetain
- **Type**: typing.Optional[int]

### cleanExpiredFiles
- **Type**: typing.Optional[bool]


# IcebergRetentionMetricsTypeDef

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


# IcebergTargetOutputTypeDef

### Paths
- **Type**: typing.Optional[typing.List[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### MaximumTraversalDepth
- **Type**: typing.Optional[int]


# IcebergTargetTypeDef

### Paths
- **Type**: typing.Optional[typing.Sequence[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.Sequence[str]]

### MaximumTraversalDepth
- **Type**: typing.Optional[int]


# ImportCatalogToGlueRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]


# ImportLabelsTaskRunPropertiesTypeDef

### InputS3Path
- **Type**: typing.Optional[str]

### Replace
- **Type**: typing.Optional[bool]


# InboundIntegrationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.IntegrationErrorTypeDef]]


# IntegrationErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# IntegrationFilterTypeDef

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# IntegrationPartitionTypeDef

### FieldName
- **Type**: typing.Optional[str]

### FunctionSpec
- **Type**: typing.Optional[str]


# IntegrationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.TagTypeDef]]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.IntegrationErrorTypeDef]]

### DataFilter
- **Type**: typing.Optional[str]


# JDBCConnectorOptionsOutputTypeDef

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


# JDBCConnectorOptionsTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### JobBookmarkKeysSortOrder
- **Type**: typing.Optional[str]

### DataTypeMapping
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ARRAY', 'BIGINT', 'BINARY', 'BIT', 'BLOB', 'BOOLEAN', 'CHAR', 'CLOB', 'DATALINK', 'DATE', 'DECIMAL', 'DISTINCT', 'DOUBLE', 'FLOAT', 'INTEGER', 'JAVA_OBJECT', 'LONGNVARCHAR', 'LONGVARBINARY', 'LONGVARCHAR', 'NCHAR', 'NCLOB', 'NULL', 'NUMERIC', 'NVARCHAR', 'OTHER', 'REAL', 'REF', 'REF_CURSOR', 'ROWID', 'SMALLINT', 'SQLXML', 'STRUCT', 'TIME', 'TIMESTAMP', 'TIMESTAMP_WITH_TIMEZONE', 'TIME_WITH_TIMEZONE', 'TINYINT', 'VARBINARY', 'VARCHAR'], typing.Literal['BIGDECIMAL', 'BYTE', 'DATE', 'DOUBLE', 'FLOAT', 'INT', 'LONG', 'SHORT', 'STRING', 'TIMESTAMP']]]


# JDBCConnectorOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JDBCConnectorSourceOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.JDBCConnectorOptionsOutputTypeDef]

### ConnectionTable
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# JDBCConnectorSourceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.JDBCConnectorOptionsUnionTypeDef]

### ConnectionTable
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# JDBCConnectorTargetOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# JDBCConnectorTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# JdbcTargetOutputTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.List[str]]

### EnableAdditionalMetadata
- **Type**: typing.Optional[typing.List[typing.Literal['COMMENTS', 'RAWTYPES']]]


# JdbcTargetTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.Sequence[str]]

### EnableAdditionalMetadata
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMMENTS', 'RAWTYPES']]]


# JobBookmarkEntryTypeDef

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


# JobBookmarksEncryptionTypeDef

### JobBookmarksEncryptionMode
- **Type**: typing.Optional[typing.Literal['CSE-KMS', 'DISABLED']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# JobCommandTypeDef

### Name
- **Type**: typing.Optional[str]

### ScriptLocation
- **Type**: typing.Optional[str]

### PythonVersion
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[str]


# JobNodeDetailsTypeDef

### JobRuns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.JobRunTypeDef]]


# JobPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ExecutionPropertyTypeDef]

### Command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.JobCommandTypeDef]

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### NonOverridableArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ConnectionsListOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NotificationPropertyTypeDef]

### GlueVersion
- **Type**: typing.Optional[str]

### CodeGenConfigurationNodes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.CodeGenConfigurationNodePaginatorTypeDef]]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### SourceControlDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SourceControlDetailsTypeDef]

### MaintenanceWindow
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]


# JobRunTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.PredecessorTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NotificationPropertyTypeDef]

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


# JobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ExecutionPropertyTypeDef]

### Command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.JobCommandTypeDef]

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### NonOverridableArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ConnectionsListOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NotificationPropertyTypeDef]

### GlueVersion
- **Type**: typing.Optional[str]

### CodeGenConfigurationNodes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.CodeGenConfigurationNodeOutputTypeDef]]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### SourceControlDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SourceControlDetailsTypeDef]

### MaintenanceWindow
- **Type**: typing.Optional[str]

### ProfileName
- **Type**: typing.Optional[str]


# JobUpdateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ExecutionPropertyTypeDef]

### Command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.JobCommandTypeDef]

### DefaultArguments
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NonOverridableArguments
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ConnectionsListUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NotificationPropertyTypeDef]

### GlueVersion
- **Type**: typing.Optional[str]

### CodeGenConfigurationNodes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.glue_classes.CodeGenConfigurationNodeUnionTypeDef]]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]

### SourceControlDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SourceControlDetailsTypeDef]

### MaintenanceWindow
- **Type**: typing.Optional[str]


# JoinColumnOutputTypeDef

### From
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# JoinColumnTypeDef

### From
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.Sequence[typing.Sequence[str]]
- **Required**: Yes


# JoinColumnUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JoinOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.JoinColumnOutputTypeDef]
- **Required**: Yes


# JoinTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### JoinType
- **Type**: typing.Literal['equijoin', 'left', 'leftanti', 'leftsemi', 'outer', 'right']
- **Required**: Yes

### Columns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.JoinColumnUnionTypeDef]
- **Required**: Yes


# JsonClassifierTypeDef

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


# KafkaStreamingSourceOptionsOutputTypeDef

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


# KafkaStreamingSourceOptionsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# KafkaStreamingSourceOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeySchemaElementTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KinesisStreamingSourceOptionsOutputTypeDef

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


# KinesisStreamingSourceOptionsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# KinesisStreamingSourceOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LabelingSetGenerationTaskRunPropertiesTypeDef

### OutputS3Path
- **Type**: typing.Optional[str]


# LakeFormationConfigurationTypeDef

### UseLakeFormationCredentials
- **Type**: typing.Optional[bool]

### AccountId
- **Type**: typing.Optional[str]


# LastActiveDefinitionTypeDef

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


# LastCrawlInfoTypeDef

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


# LineageConfigurationTypeDef

### CrawlerLineageSettings
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]


# ListBlueprintsRequestPaginateTypeDef

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListBlueprintsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ListBlueprintsResponseTypeDef

### Blueprints
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListColumnStatisticsTaskRunsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListColumnStatisticsTaskRunsResponseTypeDef

### ColumnStatisticsTaskRunIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionTypesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListConnectionTypesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionTypesResponseTypeDef

### ConnectionTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ConnectionTypeBriefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrawlersRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ListCrawlersResponseTypeDef

### CrawlerNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrawlsRequestTypeDef

### CrawlerName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CrawlsFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# ListCrawlsResponseTypeDef

### Crawls
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CrawlerHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomEntityTypesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ListCustomEntityTypesResponseTypeDef

### CustomEntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.CustomEntityTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityResultsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityResultFilterCriteriaTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataQualityResultsResponseTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityResultDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityRuleRecommendationRunsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityRuleRecommendationRunFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataQualityRuleRecommendationRunsResponseTypeDef

### Runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityRuleRecommendationRunDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityRulesetEvaluationRunsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityRulesetEvaluationRunFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataQualityRulesetEvaluationRunsResponseTypeDef

### Runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityRulesetEvaluationRunDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityRulesetsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityRulesetFilterCriteriaTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ListDataQualityRulesetsResponseTypeDef

### Rulesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.DataQualityRulesetListDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityStatisticAnnotationsRequestTypeDef

### StatisticId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### TimestampFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityStatisticAnnotationsResponseTypeDef

### Annotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.StatisticAnnotationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityStatisticsRequestTypeDef

### StatisticId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### TimestampFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityStatisticsResponseTypeDef

### Statistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.StatisticSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevEndpointsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ListDevEndpointsResponseTypeDef

### DevEndpointNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitiesRequestPaginateTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### ParentEntityName
- **Type**: typing.Optional[str]

### DataStoreApiVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListEntitiesRequestTypeDef

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


# ListEntitiesResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.EntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequestPaginateTypeDef

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListJobsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ListJobsResponseTypeDef

### JobNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMLTransformsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TransformFilterCriteriaTypeDef]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TransformSortCriteriaTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ListMLTransformsResponseTypeDef

### TransformIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegistriesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListRegistriesInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRegistriesResponseTypeDef

### Registries
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.RegistryListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaVersionsInputPaginateTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListSchemaVersionsInputTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaVersionsResponseTypeDef

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.SchemaVersionListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemasInputPaginateTypeDef

### RegistryId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RegistryIdTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListSchemasInputTypeDef

### RegistryId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RegistryIdTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSchemasResponseTypeDef

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.SchemaListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSessionsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestOrigin
- **Type**: typing.Optional[str]


# ListSessionsResponseTypeDef

### Ids
- **Type**: typing.List[str]
- **Required**: Yes

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.SessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStatementsRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListStatementsResponseTypeDef

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.StatementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTableOptimizerRunsResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TableOptimizerRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTriggersRequestPaginateTypeDef

### DependentJobName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListTriggersRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### DependentJobName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ListTriggersResponseTypeDef

### TriggerNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsageProfilesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListUsageProfilesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUsageProfilesResponseTypeDef

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.UsageProfileDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PaginatorConfigTypeDef]


# ListWorkflowsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkflowsResponseTypeDef

### Workflows
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocationTypeDef

### Jdbc
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CodeGenNodeArgTypeDef]]

### S3
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CodeGenNodeArgTypeDef]]

### DynamoDB
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.CodeGenNodeArgTypeDef]]


# LongColumnStatisticsDataTypeDef

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


# MLTransformTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueTableOutputTypeDef]]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TransformParametersTypeDef]

### EvaluationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.EvaluationMetricsTypeDef]

### LabelCount
- **Type**: typing.Optional[int]

### Schema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.SchemaColumnTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TransformEncryptionTypeDef]


# MLUserDataEncryptionTypeDef

### MlUserDataEncryptionMode
- **Type**: typing.Literal['DISABLED', 'SSE-KMS']
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# MappingEntryTypeDef

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


# MappingOutputTypeDef

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


# MappingPaginatorTypeDef

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


# MappingTypeDef

### ToKey
- **Type**: typing.Optional[str]

### FromPath
- **Type**: typing.Optional[typing.Sequence[str]]

### FromType
- **Type**: typing.Optional[str]

### ToType
- **Type**: typing.Optional[str]

### Dropped
- **Type**: typing.Optional[bool]

### Children
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# MergeOutputTypeDef

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


# MergeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryKeys
- **Type**: typing.Sequence[typing.Sequence[str]]
- **Required**: Yes


# MetadataInfoTypeDef

### MetadataValue
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### OtherMetadataValueList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.OtherMetadataValueListItemTypeDef]]


# MetadataKeyValuePairTypeDef

### MetadataKey
- **Type**: typing.Optional[str]

### MetadataValue
- **Type**: typing.Optional[str]


# MetricBasedObservationTypeDef

### MetricName
- **Type**: typing.Optional[str]

### StatisticId
- **Type**: typing.Optional[str]

### MetricValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityMetricValuesTypeDef]

### NewRules
- **Type**: typing.Optional[typing.List[str]]


# MicrosoftSQLServerCatalogSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# MicrosoftSQLServerCatalogTargetOutputTypeDef

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


# MicrosoftSQLServerCatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyIntegrationRequestTypeDef

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DataFilter
- **Type**: typing.Optional[str]

### IntegrationName
- **Type**: typing.Optional[str]


# ModifyIntegrationResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TagTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING', 'NEEDS_ATTENTION', 'SYNCING']
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.IntegrationErrorTypeDef]
- **Required**: Yes

### DataFilter
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MongoDBTargetTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### ScanAll
- **Type**: typing.Optional[bool]


# MySQLCatalogSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# MySQLCatalogTargetOutputTypeDef

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


# MySQLCatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# NodeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotificationPropertyTypeDef

### NotifyDelayAfter
- **Type**: typing.Optional[int]


# NullCheckBoxListTypeDef

### IsEmpty
- **Type**: typing.Optional[bool]

### IsNullString
- **Type**: typing.Optional[bool]

### IsNegOne
- **Type**: typing.Optional[bool]


# NullValueFieldTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Datatype
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DatatypeTypeDef'>
- **Required**: Yes


# OAuth2ClientApplicationTypeDef

### UserManagedClientApplicationClientId
- **Type**: typing.Optional[str]

### AWSManagedClientApplicationReference
- **Type**: typing.Optional[str]


# OAuth2CredentialsTypeDef

### UserManagedClientApplicationClientSecret
- **Type**: typing.Optional[str]

### AccessToken
- **Type**: typing.Optional[str]

### RefreshToken
- **Type**: typing.Optional[str]

### JwtToken
- **Type**: typing.Optional[str]


# OAuth2PropertiesInputTypeDef

### OAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### OAuth2ClientApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OAuth2ClientApplicationTypeDef]

### TokenUrl
- **Type**: typing.Optional[str]

### TokenUrlParametersMap
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AuthorizationCodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AuthorizationCodePropertiesTypeDef]

### OAuth2Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OAuth2CredentialsTypeDef]


# OAuth2PropertiesTypeDef

### OAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### OAuth2ClientApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OAuth2ClientApplicationTypeDef]

### TokenUrl
- **Type**: typing.Optional[str]

### TokenUrlParametersMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# OpenTableFormatInputTypeDef

### IcebergInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.IcebergInputTypeDef]


# OptionTypeDef

### Value
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# OracleSQLCatalogSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# OracleSQLCatalogTargetOutputTypeDef

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


# OracleSQLCatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# OrderTypeDef

### Column
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: <class 'int'>
- **Required**: Yes


# OrphanFileDeletionConfigurationTypeDef

### icebergConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.IcebergOrphanFileDeletionConfigurationTypeDef]


# OrphanFileDeletionMetricsTypeDef

### IcebergMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.IcebergOrphanFileDeletionMetricsTypeDef]


# OtherMetadataValueListItemTypeDef

### MetadataValue
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]


# PIIDetectionOutputTypeDef

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


# PIIDetectionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PiiType
- **Type**: typing.Literal['ColumnAudit', 'ColumnMasking', 'RowAudit', 'RowMasking']
- **Required**: Yes

### EntityTypesToDetect
- **Type**: typing.Sequence[str]
- **Required**: Yes

### OutputColumnName
- **Type**: typing.Optional[str]

### SampleFraction
- **Type**: typing.Optional[float]

### ThresholdFraction
- **Type**: typing.Optional[float]

### MaskValue
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartitionErrorTypeDef

### PartitionValues
- **Type**: typing.Optional[typing.List[str]]

### ErrorDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]


# PartitionIndexDescriptorTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.KeySchemaElementTypeDef]
- **Required**: Yes

### IndexStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### BackfillErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.BackfillErrorTypeDef]]


# PartitionIndexTypeDef

### Keys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes


# PartitionInputTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### LastAccessTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### StorageDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StorageDescriptorUnionTypeDef]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### LastAnalyzedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# PartitionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StorageDescriptorOutputTypeDef]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastAnalyzedTime
- **Type**: typing.Optional[datetime.datetime]

### CatalogId
- **Type**: typing.Optional[str]


# PartitionValueListOutputTypeDef

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# PartitionValueListTypeDef

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PartitionValueListUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PhysicalConnectionRequirementsOutputTypeDef

### SubnetId
- **Type**: typing.Optional[str]

### SecurityGroupIdList
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZone
- **Type**: typing.Optional[str]


# PhysicalConnectionRequirementsTypeDef

### SubnetId
- **Type**: typing.Optional[str]

### SecurityGroupIdList
- **Type**: typing.Optional[typing.Sequence[str]]

### AvailabilityZone
- **Type**: typing.Optional[str]


# PhysicalConnectionRequirementsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PostgreSQLCatalogSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# PostgreSQLCatalogTargetOutputTypeDef

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


# PostgreSQLCatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# PredecessorTypeDef

### JobName
- **Type**: typing.Optional[str]

### RunId
- **Type**: typing.Optional[str]


# PredicateOutputTypeDef

### Logical
- **Type**: typing.Optional[typing.Literal['AND', 'ANY']]

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ConditionTypeDef]]


# PredicateTypeDef

### Logical
- **Type**: typing.Optional[typing.Literal['AND', 'ANY']]

### Conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ConditionTypeDef]]


# PredicateUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrincipalPermissionsOutputTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataLakePrincipalTypeDef]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DROP', 'INSERT', 'SELECT']]]


# PrincipalPermissionsTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataLakePrincipalTypeDef]

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DROP', 'INSERT', 'SELECT']]]


# PrincipalPermissionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProfileConfigurationOutputTypeDef

### SessionConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.ConfigurationObjectOutputTypeDef]]

### JobConfiguration
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.ConfigurationObjectOutputTypeDef]]


# ProfileConfigurationTypeDef

### SessionConfiguration
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.glue_classes.ConfigurationObjectTypeDef]]

### JobConfiguration
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.glue_classes.ConfigurationObjectTypeDef]]


# ProfileConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PropertyPredicateTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Comparator
- **Type**: typing.Optional[typing.Literal['EQUALS', 'GREATER_THAN', 'GREATER_THAN_EQUALS', 'LESS_THAN', 'LESS_THAN_EQUALS']]


# PropertyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutDataCatalogEncryptionSettingsRequestTypeDef

### DataCatalogEncryptionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataCatalogEncryptionSettingsTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# PutDataQualityProfileAnnotationRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InclusionAnnotation
- **Type**: typing.Literal['EXCLUDE', 'INCLUDE']
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

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


# PutResourcePolicyResponseTypeDef

### PolicyHash
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutSchemaVersionMetadataInputTypeDef

### MetadataKeyValue
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.MetadataKeyValuePairTypeDef'>
- **Required**: Yes

### SchemaId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef]

### SchemaVersionNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaVersionNumberTypeDef]

### SchemaVersionId
- **Type**: typing.Optional[str]


# PutSchemaVersionMetadataResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutWorkflowRunPropertiesRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### RunProperties
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# QuerySchemaVersionMetadataInputTypeDef

### SchemaId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef]

### SchemaVersionNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaVersionNumberTypeDef]

### SchemaVersionId
- **Type**: typing.Optional[str]

### MetadataList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.MetadataKeyValuePairTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# QuerySchemaVersionMetadataResponseTypeDef

### MetadataInfoMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.glue_classes.MetadataInfoTypeDef]
- **Required**: Yes

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# QuerySessionContextTypeDef

### QueryId
- **Type**: typing.Optional[str]

### QueryStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### ClusterId
- **Type**: typing.Optional[str]

### QueryAuthorizationId
- **Type**: typing.Optional[str]

### AdditionalContext
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RecipeActionOutputTypeDef

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecipeActionTypeDef

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RecipeActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecipeOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### RecipeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RecipeReferenceTypeDef]

### RecipeSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.RecipeStepOutputTypeDef]]


# RecipeReferenceTypeDef

### RecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: <class 'str'>
- **Required**: Yes


# RecipeStepOutputTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.RecipeActionOutputTypeDef'>
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ConditionExpressionTypeDef]]


# RecipeStepTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.RecipeActionUnionTypeDef'>
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ConditionExpressionTypeDef]]


# RecipeStepUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecipeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RecipeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RecipeReferenceTypeDef]

### RecipeSteps
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.RecipeStepUnionTypeDef]]


# RecrawlPolicyTypeDef

### RecrawlBehavior
- **Type**: typing.Optional[typing.Literal['CRAWL_EVENT_MODE', 'CRAWL_EVERYTHING', 'CRAWL_NEW_FOLDERS_ONLY']]


# RedshiftSourceTypeDef

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


# RedshiftTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.UpsertRedshiftTargetOptionsOutputTypeDef]


# RedshiftTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.UpsertRedshiftTargetOptionsUnionTypeDef]


# RegisterSchemaVersionInputTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes

### SchemaDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterSchemaVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegistryIdTypeDef

### RegistryName
- **Type**: typing.Optional[str]

### RegistryArn
- **Type**: typing.Optional[str]


# RegistryListItemTypeDef

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


# RelationalCatalogSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveSchemaVersionMetadataInputTypeDef

### MetadataKeyValue
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.MetadataKeyValuePairTypeDef'>
- **Required**: Yes

### SchemaId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef]

### SchemaVersionNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaVersionNumberTypeDef]

### SchemaVersionId
- **Type**: typing.Optional[str]


# RemoveSchemaVersionMetadataResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RenameFieldOutputTypeDef

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


# RenameFieldTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SourcePath
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TargetPath
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResetJobBookmarkRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: typing.Optional[str]


# ResetJobBookmarkResponseTypeDef

### JobBookmarkEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.JobBookmarkEntryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceUriTypeDef

### ResourceType
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'FILE', 'JAR']]

### Uri
- **Type**: typing.Optional[str]


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


# ResumeWorkflowRunRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResumeWorkflowRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetentionConfigurationTypeDef

### icebergConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.IcebergRetentionConfigurationTypeDef]


# RetentionMetricsTypeDef

### IcebergMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.IcebergRetentionMetricsTypeDef]


# RunIdentifierTypeDef

### RunId
- **Type**: typing.Optional[str]

### JobRunId
- **Type**: typing.Optional[str]


# RunMetricsTypeDef

### NumberOfBytesCompacted
- **Type**: typing.Optional[str]

### NumberOfFilesCompacted
- **Type**: typing.Optional[str]

### NumberOfDpus
- **Type**: typing.Optional[str]

### JobDurationInHour
- **Type**: typing.Optional[str]


# RunStatementRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# RunStatementResponseTypeDef

### Id
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3CatalogDeltaSourceOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# S3CatalogDeltaSourceTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# S3CatalogHudiSourceOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# S3CatalogHudiSourceTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# S3CatalogSourceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3SourceAdditionalOptionsTypeDef]


# S3CatalogTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogSchemaChangePolicyTypeDef]


# S3CatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogSchemaChangePolicyTypeDef]


# S3CsvSourceOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# S3CsvSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Optional[typing.Sequence[str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# S3DeltaCatalogTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogSchemaChangePolicyTypeDef]


# S3DeltaCatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### AdditionalOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogSchemaChangePolicyTypeDef]


# S3DeltaDirectTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DirectSchemaChangePolicyTypeDef]


# S3DeltaDirectTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### AdditionalOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DirectSchemaChangePolicyTypeDef]


# S3DeltaSourceOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### AdditionalDeltaOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# S3DeltaSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AdditionalDeltaOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# S3DirectSourceAdditionalOptionsTypeDef

### BoundedSize
- **Type**: typing.Optional[int]

### BoundedFiles
- **Type**: typing.Optional[int]

### EnableSamplePath
- **Type**: typing.Optional[bool]

### SamplePath
- **Type**: typing.Optional[str]


# S3DirectTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DirectSchemaChangePolicyTypeDef]


# S3DirectTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['avro', 'csv', 'delta', 'hudi', 'json', 'orc', 'parquet']
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### Compression
- **Type**: typing.Optional[str]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DirectSchemaChangePolicyTypeDef]


# S3EncryptionTypeDef

### S3EncryptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SSE-KMS', 'SSE-S3']]

### KmsKeyArn
- **Type**: typing.Optional[str]


# S3GlueParquetTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DirectSchemaChangePolicyTypeDef]


# S3GlueParquetTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### Compression
- **Type**: typing.Optional[typing.Literal['gzip', 'lzo', 'none', 'snappy', 'uncompressed']]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DirectSchemaChangePolicyTypeDef]


# S3HudiCatalogTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogSchemaChangePolicyTypeDef]


# S3HudiCatalogTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalOptions
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CatalogSchemaChangePolicyTypeDef]


# S3HudiDirectTargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DirectSchemaChangePolicyTypeDef]


# S3HudiDirectTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DirectSchemaChangePolicyTypeDef]


# S3HudiSourceOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.List[str]
- **Required**: Yes

### AdditionalHudiOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# S3HudiSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AdditionalHudiOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AdditionalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# S3JsonSourceOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

### JsonPath
- **Type**: typing.Optional[str]

### Multiline
- **Type**: typing.Optional[bool]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# S3JsonSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['bzip2', 'gzip']]

### Exclusions
- **Type**: typing.Optional[typing.Sequence[str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

### JsonPath
- **Type**: typing.Optional[str]

### Multiline
- **Type**: typing.Optional[bool]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# S3ParquetSourceOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# S3ParquetSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Paths
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['gzip', 'lzo', 'none', 'snappy', 'uncompressed']]

### Exclusions
- **Type**: typing.Optional[typing.Sequence[str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.S3DirectSourceAdditionalOptionsTypeDef]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# S3SourceAdditionalOptionsTypeDef

### BoundedSize
- **Type**: typing.Optional[int]

### BoundedFiles
- **Type**: typing.Optional[int]


# S3TargetOutputTypeDef

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


# S3TargetTypeDef

### Path
- **Type**: typing.Optional[str]

### Exclusions
- **Type**: typing.Optional[typing.Sequence[str]]

### ConnectionName
- **Type**: typing.Optional[str]

### SampleSize
- **Type**: typing.Optional[int]

### EventQueueArn
- **Type**: typing.Optional[str]

### DlqEventQueueArn
- **Type**: typing.Optional[str]


# ScheduleTypeDef

### ScheduleExpression
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['NOT_SCHEDULED', 'SCHEDULED', 'TRANSITIONING']]


# SchemaChangePolicyTypeDef

### UpdateBehavior
- **Type**: typing.Optional[typing.Literal['LOG', 'UPDATE_IN_DATABASE']]

### DeleteBehavior
- **Type**: typing.Optional[typing.Literal['DELETE_FROM_DATABASE', 'DEPRECATE_IN_DATABASE', 'LOG']]


# SchemaColumnTypeDef

### Name
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]


# SchemaIdTypeDef

### SchemaArn
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### RegistryName
- **Type**: typing.Optional[str]


# SchemaListItemTypeDef

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


# SchemaReferenceTypeDef

### SchemaId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef]

### SchemaVersionId
- **Type**: typing.Optional[str]

### SchemaVersionNumber
- **Type**: typing.Optional[int]


# SchemaVersionErrorItemTypeDef

### VersionNumber
- **Type**: typing.Optional[int]

### ErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailsTypeDef]


# SchemaVersionListItemTypeDef

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


# SchemaVersionNumberTypeDef

### LatestVersion
- **Type**: typing.Optional[bool]

### VersionNumber
- **Type**: typing.Optional[int]


# SearchTablesRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.PropertyPredicateTypeDef]]

### SearchText
- **Type**: typing.Optional[str]

### SortCriteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.SortCriterionTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FEDERATED', 'FOREIGN']]

### IncludeStatusDetails
- **Type**: typing.Optional[bool]


# SearchTablesResponseTypeDef

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.TableTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SecurityConfigurationTypeDef

### Name
- **Type**: typing.Optional[str]

### CreatedTimeStamp
- **Type**: typing.Optional[datetime.datetime]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.EncryptionConfigurationOutputTypeDef]


# SegmentTypeDef

### SegmentNumber
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSegments
- **Type**: <class 'int'>
- **Required**: Yes


# SelectFieldsOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# SelectFieldsTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Paths
- **Type**: typing.Sequence[typing.Sequence[str]]
- **Required**: Yes


# SelectFromCollectionOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Index
- **Type**: <class 'int'>
- **Required**: Yes


# SelectFromCollectionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Index
- **Type**: <class 'int'>
- **Required**: Yes


# SerDeInfoOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### SerializationLibrary
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# SerDeInfoTypeDef

### Name
- **Type**: typing.Optional[str]

### SerializationLibrary
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SerDeInfoUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SessionCommandTypeDef

### Name
- **Type**: typing.Optional[str]

### PythonVersion
- **Type**: typing.Optional[str]


# SessionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SessionCommandTypeDef]

### DefaultArguments
- **Type**: typing.Optional[typing.Dict[str, str]]

### Connections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ConnectionsListOutputTypeDef]

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


# SkewedInfoOutputTypeDef

### SkewedColumnNames
- **Type**: typing.Optional[typing.List[str]]

### SkewedColumnValues
- **Type**: typing.Optional[typing.List[str]]

### SkewedColumnValueLocationMaps
- **Type**: typing.Optional[typing.Dict[str, str]]


# SkewedInfoTypeDef

### SkewedColumnNames
- **Type**: typing.Optional[typing.Sequence[str]]

### SkewedColumnValues
- **Type**: typing.Optional[typing.Sequence[str]]

### SkewedColumnValueLocationMaps
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SkewedInfoUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnowflakeNodeDataOutputTypeDef

### SourceType
- **Type**: typing.Optional[str]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### Schema
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### TempDir
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]]

### AutoPushdown
- **Type**: typing.Optional[bool]

### TableSchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]]


# SnowflakeNodeDataTypeDef

### SourceType
- **Type**: typing.Optional[str]

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### Schema
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### TempDir
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]

### AdditionalOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]]

### AutoPushdown
- **Type**: typing.Optional[bool]

### TableSchema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.OptionTypeDef]]


# SnowflakeNodeDataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnowflakeSourceOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SnowflakeNodeDataOutputTypeDef'>
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# SnowflakeSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SnowflakeNodeDataUnionTypeDef'>
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaUnionTypeDef]]


# SnowflakeTargetOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SnowflakeNodeDataOutputTypeDef'>
- **Required**: Yes

### Inputs
- **Type**: typing.Optional[typing.List[str]]


# SnowflakeTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SnowflakeNodeDataUnionTypeDef'>
- **Required**: Yes

### Inputs
- **Type**: typing.Optional[typing.Sequence[str]]


# SortCriterionTypeDef

### FieldName
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# SourceControlDetailsTypeDef

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


# SourceProcessingPropertiesTypeDef

### RoleArn
- **Type**: typing.Optional[str]


# SourceTableConfigOutputTypeDef

### Fields
- **Type**: typing.Optional[typing.List[str]]

### FilterPredicate
- **Type**: typing.Optional[str]

### PrimaryKey
- **Type**: typing.Optional[typing.List[str]]

### RecordUpdateField
- **Type**: typing.Optional[str]


# SourceTableConfigTypeDef

### Fields
- **Type**: typing.Optional[typing.Sequence[str]]

### FilterPredicate
- **Type**: typing.Optional[str]

### PrimaryKey
- **Type**: typing.Optional[typing.Sequence[str]]

### RecordUpdateField
- **Type**: typing.Optional[str]


# SourceTableConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SparkConnectorSourceOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# SparkConnectorSourceTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# SparkConnectorTargetOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# SparkConnectorTargetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# SparkSQLOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.SqlAliasTypeDef]
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaOutputTypeDef]]


# SparkSQLTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### SqlAliases
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.SqlAliasTypeDef]
- **Required**: Yes

### OutputSchemas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.GlueSchemaTypeDef]]


# SpigotOutputTypeDef

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


# SpigotTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Topk
- **Type**: typing.Optional[int]

### Prob
- **Type**: typing.Optional[float]


# SplitFieldsOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### Paths
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# SplitFieldsTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Paths
- **Type**: typing.Sequence[typing.Sequence[str]]
- **Required**: Yes


# SqlAliasTypeDef

### From
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# StartBlueprintRunRequestTypeDef

### BlueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[str]


# StartBlueprintRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartColumnStatisticsTaskRunRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### SampleSize
- **Type**: typing.Optional[float]

### CatalogID
- **Type**: typing.Optional[str]

### SecurityConfiguration
- **Type**: typing.Optional[str]


# StartColumnStatisticsTaskRunResponseTypeDef

### ColumnStatisticsTaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartColumnStatisticsTaskRunScheduleRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# StartCrawlerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartCrawlerScheduleRequestTypeDef

### CrawlerName
- **Type**: <class 'str'>
- **Required**: Yes


# StartDataQualityRuleRecommendationRunRequestTypeDef

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataSourceUnionTypeDef'>
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


# StartDataQualityRuleRecommendationRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDataQualityRulesetEvaluationRunRequestTypeDef

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DataSourceUnionTypeDef'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### RulesetNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NumberOfWorkers
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### ClientToken
- **Type**: typing.Optional[str]

### AdditionalRunOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DataQualityEvaluationRunAdditionalRunOptionsTypeDef]

### AdditionalDataSources
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.glue_classes.DataSourceUnionTypeDef]]


# StartDataQualityRulesetEvaluationRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartExportLabelsTaskRunRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputS3Path
- **Type**: <class 'str'>
- **Required**: Yes


# StartExportLabelsTaskRunResponseTypeDef

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartImportLabelsTaskRunRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### InputS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### ReplaceAllLabels
- **Type**: typing.Optional[bool]


# StartImportLabelsTaskRunResponseTypeDef

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartJobRunRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobRunQueuingEnabled
- **Type**: typing.Optional[bool]

### JobRunId
- **Type**: typing.Optional[str]

### Arguments
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AllocatedCapacity
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[float]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### NotificationProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.NotificationPropertyTypeDef]

### WorkerType
- **Type**: typing.Optional[typing.Literal['G.025X', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'Standard', 'Z.2X']]

### NumberOfWorkers
- **Type**: typing.Optional[int]

### ExecutionClass
- **Type**: typing.Optional[typing.Literal['FLEX', 'STANDARD']]


# StartJobRunResponseTypeDef

### JobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMLEvaluationTaskRunRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes


# StartMLEvaluationTaskRunResponseTypeDef

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMLLabelingSetGenerationTaskRunRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputS3Path
- **Type**: <class 'str'>
- **Required**: Yes


# StartMLLabelingSetGenerationTaskRunResponseTypeDef

### TaskRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTriggerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartTriggerResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartWorkflowRunRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartWorkflowRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartingEventBatchConditionTypeDef

### BatchSize
- **Type**: typing.Optional[int]

### BatchWindow
- **Type**: typing.Optional[int]


# StatementOutputDataTypeDef

### TextPlain
- **Type**: typing.Optional[str]


# StatementOutputTypeDef

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StatementOutputDataTypeDef]

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


# StatementTypeDef

### Id
- **Type**: typing.Optional[int]

### Code
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CANCELLED', 'CANCELLING', 'ERROR', 'RUNNING', 'WAITING']]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StatementOutputTypeDef]

### Progress
- **Type**: typing.Optional[float]

### StartedOn
- **Type**: typing.Optional[int]

### CompletedOn
- **Type**: typing.Optional[int]


# StatisticAnnotationTypeDef

### ProfileId
- **Type**: typing.Optional[str]

### StatisticId
- **Type**: typing.Optional[str]

### StatisticRecordedOn
- **Type**: typing.Optional[datetime.datetime]

### InclusionAnnotation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampedInclusionAnnotationTypeDef]


# StatisticModelResultTypeDef

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


# StatisticSummaryTypeDef

### StatisticId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### RunIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RunIdentifierTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampedInclusionAnnotationTypeDef]


# StatusDetailsPaginatorTypeDef

### RequestedChange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ViewValidations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ViewValidationTypeDef]]


# StatusDetailsTypeDef

### RequestedChange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ViewValidations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ViewValidationTypeDef]]


# StopColumnStatisticsTaskRunRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# StopColumnStatisticsTaskRunScheduleRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# StopCrawlerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopCrawlerScheduleRequestTypeDef

### CrawlerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopSessionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RequestOrigin
- **Type**: typing.Optional[str]


# StopSessionResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopTriggerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopTriggerResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopWorkflowRunRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# StorageDescriptorOutputTypeDef

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnOutputTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SerDeInfoOutputTypeDef]

### BucketColumns
- **Type**: typing.Optional[typing.List[str]]

### SortColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.OrderTypeDef]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### SkewedInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SkewedInfoOutputTypeDef]

### StoredAsSubDirectories
- **Type**: typing.Optional[bool]

### SchemaReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaReferenceTypeDef]


# StorageDescriptorTypeDef

### Columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ColumnUnionTypeDef]]

### Location
- **Type**: typing.Optional[str]

### AdditionalLocations
- **Type**: typing.Optional[typing.Sequence[str]]

### InputFormat
- **Type**: typing.Optional[str]

### OutputFormat
- **Type**: typing.Optional[str]

### Compressed
- **Type**: typing.Optional[bool]

### NumberOfBuckets
- **Type**: typing.Optional[int]

### SerdeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SerDeInfoUnionTypeDef]

### BucketColumns
- **Type**: typing.Optional[typing.Sequence[str]]

### SortColumns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.OrderTypeDef]]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SkewedInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SkewedInfoUnionTypeDef]

### StoredAsSubDirectories
- **Type**: typing.Optional[bool]

### SchemaReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaReferenceTypeDef]


# StorageDescriptorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StreamingDataPreviewOptionsTypeDef

### PollingTime
- **Type**: typing.Optional[int]

### RecordPollingLimit
- **Type**: typing.Optional[int]


# StringColumnStatisticsDataTypeDef

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


# SupportedDialectTypeDef

### Dialect
- **Type**: typing.Optional[typing.Literal['ATHENA', 'REDSHIFT', 'SPARK']]

### DialectVersion
- **Type**: typing.Optional[str]


# TableErrorTypeDef

### TableName
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]


# TableIdentifierTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# TableInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### LastAccessTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### LastAnalyzedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### Retention
- **Type**: typing.Optional[int]

### StorageDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StorageDescriptorUnionTypeDef]

### PartitionKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ColumnUnionTypeDef]]

### ViewOriginalText
- **Type**: typing.Optional[str]

### ViewExpandedText
- **Type**: typing.Optional[str]

### TableType
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TargetTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TableIdentifierTypeDef]

### ViewDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ViewDefinitionInputTypeDef]


# TableOptimizerConfigurationTypeDef

### roleArn
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TableOptimizerVpcConfigurationTypeDef]

### retentionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RetentionConfigurationTypeDef]

### orphanFileDeletionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OrphanFileDeletionConfigurationTypeDef]


# TableOptimizerRunTypeDef

### eventType
- **Type**: typing.Optional[typing.Literal['completed', 'failed', 'in_progress', 'starting']]

### startTimestamp
- **Type**: typing.Optional[datetime.datetime]

### endTimestamp
- **Type**: typing.Optional[datetime.datetime]

### metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RunMetricsTypeDef]

### error
- **Type**: typing.Optional[str]

### compactionMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CompactionMetricsTypeDef]

### retentionMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RetentionMetricsTypeDef]

### orphanFileDeletionMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.OrphanFileDeletionMetricsTypeDef]


# TableOptimizerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TableOptimizerVpcConfigurationTypeDef

### glueConnectionName
- **Type**: typing.Optional[str]


# TablePaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StorageDescriptorOutputTypeDef]

### PartitionKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnOutputTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TableIdentifierTypeDef]

### CatalogId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### FederatedTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FederatedTableTypeDef]

### ViewDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ViewDefinitionTypeDef]

### IsMultiDialectView
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TableStatusPaginatorTypeDef]


# TableStatusPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StatusDetailsPaginatorTypeDef]


# TableStatusTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StatusDetailsTypeDef]


# TableTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StorageDescriptorOutputTypeDef]

### PartitionKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnOutputTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TableIdentifierTypeDef]

### CatalogId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### FederatedTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FederatedTableTypeDef]

### ViewDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ViewDefinitionTypeDef]

### IsMultiDialectView
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TableStatusTypeDef]


# TableVersionErrorTypeDef

### TableName
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]


# TableVersionPaginatorTypeDef

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TablePaginatorTypeDef]

### VersionId
- **Type**: typing.Optional[str]


# TableVersionTypeDef

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TableTypeDef]

### VersionId
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToAdd
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TargetProcessingPropertiesTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### KmsArn
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### EventBusArn
- **Type**: typing.Optional[str]


# TargetRedshiftCatalogTypeDef

### CatalogArn
- **Type**: <class 'str'>
- **Required**: Yes


# TargetTableConfigOutputTypeDef

### UnnestSpec
- **Type**: typing.Optional[typing.Literal['FULL', 'NOUNNEST', 'TOPLEVEL']]

### PartitionSpec
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.IntegrationPartitionTypeDef]]

### TargetTableName
- **Type**: typing.Optional[str]


# TargetTableConfigTypeDef

### UnnestSpec
- **Type**: typing.Optional[typing.Literal['FULL', 'NOUNNEST', 'TOPLEVEL']]

### PartitionSpec
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.IntegrationPartitionTypeDef]]

### TargetTableName
- **Type**: typing.Optional[str]


# TargetTableConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskRunFilterCriteriaTypeDef

### TaskRunType
- **Type**: typing.Optional[typing.Literal['EVALUATION', 'EXPORT_LABELS', 'FIND_MATCHES', 'IMPORT_LABELS', 'LABELING_SET_GENERATION']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### StartedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### StartedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# TaskRunPropertiesTypeDef

### TaskType
- **Type**: typing.Optional[typing.Literal['EVALUATION', 'EXPORT_LABELS', 'FIND_MATCHES', 'IMPORT_LABELS', 'LABELING_SET_GENERATION']]

### ImportLabelsTaskRunProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ImportLabelsTaskRunPropertiesTypeDef]

### ExportLabelsTaskRunProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ExportLabelsTaskRunPropertiesTypeDef]

### LabelingSetGenerationTaskRunProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LabelingSetGenerationTaskRunPropertiesTypeDef]

### FindMatchesTaskRunProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FindMatchesTaskRunPropertiesTypeDef]


# TaskRunSortCriteriaTypeDef

### Column
- **Type**: typing.Literal['STARTED', 'STATUS', 'TASK_RUN_TYPE']
- **Required**: Yes

### SortDirection
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# TaskRunTypeDef

### TransformId
- **Type**: typing.Optional[str]

### TaskRunId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### LogGroupName
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TaskRunPropertiesTypeDef]

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


# TestConnectionInputTypeDef

### ConnectionType
- **Type**: typing.Literal['CUSTOM', 'FACEBOOKADS', 'GOOGLEADS', 'GOOGLEANALYTICS4', 'GOOGLESHEETS', 'HUBSPOT', 'INSTAGRAMADS', 'INTERCOM', 'JDBC', 'JIRACLOUD', 'KAFKA', 'MARKETO', 'MARKETPLACE', 'MONGODB', 'NETSUITEERP', 'NETWORK', 'SALESFORCE', 'SALESFORCEMARKETINGCLOUD', 'SALESFORCEPARDOT', 'SAPODATA', 'SERVICENOW', 'SFTP', 'SLACK', 'SNAPCHATADS', 'STRIPE', 'VIEW_VALIDATION_ATHENA', 'VIEW_VALIDATION_REDSHIFT', 'ZENDESK', 'ZOHOCRM']
- **Required**: Yes

### ConnectionProperties
- **Type**: typing.Mapping[typing.Literal['CLUSTER_IDENTIFIER', 'CONFIG_FILES', 'CONNECTION_URL', 'CONNECTOR_CLASS_NAME', 'CONNECTOR_TYPE', 'CONNECTOR_URL', 'CUSTOM_JDBC_CERT', 'CUSTOM_JDBC_CERT_STRING', 'DATABASE', 'ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD', 'ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD', 'ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD', 'ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD', 'ENCRYPTED_PASSWORD', 'ENDPOINT', 'ENDPOINT_TYPE', 'HOST', 'INSTANCE_ID', 'JDBC_CONNECTION_URL', 'JDBC_DRIVER_CLASS_NAME', 'JDBC_DRIVER_JAR_URI', 'JDBC_ENFORCE_SSL', 'JDBC_ENGINE', 'JDBC_ENGINE_VERSION', 'KAFKA_BOOTSTRAP_SERVERS', 'KAFKA_CLIENT_KEYSTORE', 'KAFKA_CLIENT_KEYSTORE_PASSWORD', 'KAFKA_CLIENT_KEY_PASSWORD', 'KAFKA_CUSTOM_CERT', 'KAFKA_SASL_GSSAPI_KEYTAB', 'KAFKA_SASL_GSSAPI_KRB5_CONF', 'KAFKA_SASL_GSSAPI_PRINCIPAL', 'KAFKA_SASL_GSSAPI_SERVICE', 'KAFKA_SASL_MECHANISM', 'KAFKA_SASL_PLAIN_PASSWORD', 'KAFKA_SASL_PLAIN_USERNAME', 'KAFKA_SASL_SCRAM_PASSWORD', 'KAFKA_SASL_SCRAM_SECRETS_ARN', 'KAFKA_SASL_SCRAM_USERNAME', 'KAFKA_SKIP_CUSTOM_CERT_VALIDATION', 'KAFKA_SSL_ENABLED', 'PASSWORD', 'PORT', 'REGION', 'ROLE_ARN', 'SECRET_ID', 'SKIP_CUSTOM_JDBC_CERT_VALIDATION', 'USERNAME', 'WORKGROUP_NAME'], str]
- **Required**: Yes

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.AuthenticationConfigurationInputTypeDef]


# TestConnectionRequestTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### TestConnectionInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TestConnectionInputTypeDef]


# TimestampFilterTypeDef

### RecordedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### RecordedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampedInclusionAnnotationTypeDef

### Value
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]


# TransformConfigParameterOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransformConfigParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransformEncryptionTypeDef

### MlUserDataEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.MLUserDataEncryptionTypeDef]

### TaskRunSecurityConfigurationName
- **Type**: typing.Optional[str]


# TransformFilterCriteriaTypeDef

### Name
- **Type**: typing.Optional[str]

### TransformType
- **Type**: typing.Optional[typing.Literal['FIND_MATCHES']]

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'NOT_READY', 'READY']]

### GlueVersion
- **Type**: typing.Optional[str]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### LastModifiedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### LastModifiedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TimestampTypeDef]

### Schema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.SchemaColumnTypeDef]]


# TransformParametersTypeDef

### TransformType
- **Type**: typing.Literal['FIND_MATCHES']
- **Required**: Yes

### FindMatchesParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.FindMatchesParametersTypeDef]


# TransformSortCriteriaTypeDef

### Column
- **Type**: typing.Literal['CREATED', 'LAST_MODIFIED', 'NAME', 'STATUS', 'TRANSFORM_TYPE']
- **Required**: Yes

### SortDirection
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# TriggerNodeDetailsTypeDef

### Trigger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TriggerTypeDef]


# TriggerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TriggerUpdateTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ActionUnionTypeDef]]

### Predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PredicateUnionTypeDef]

### EventBatchingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.EventBatchingConditionTypeDef]


# UnfilteredPartitionTypeDef

### Partition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.PartitionTypeDef]

### AuthorizedColumns
- **Type**: typing.Optional[typing.List[str]]

### IsRegisteredWithLakeFormation
- **Type**: typing.Optional[bool]


# UnionOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### UnionType
- **Type**: typing.Literal['ALL', 'DISTINCT']
- **Required**: Yes


# UnionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UnionType
- **Type**: typing.Literal['ALL', 'DISTINCT']
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagsToRemove
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBlueprintRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BlueprintLocation
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateBlueprintResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCatalogRequestTypeDef

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.CatalogInputTypeDef'>
- **Required**: Yes


# UpdateClassifierRequestTypeDef

### GrokClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.UpdateGrokClassifierRequestTypeDef]

### XMLClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.UpdateXMLClassifierRequestTypeDef]

### JsonClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.UpdateJsonClassifierRequestTypeDef]

### CsvClassifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.UpdateCsvClassifierRequestTypeDef]


# UpdateColumnStatisticsForPartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ColumnStatisticsList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsUnionTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateColumnStatisticsForPartitionResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateColumnStatisticsForTableRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnStatisticsList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsUnionTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateColumnStatisticsForTableResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.glue_classes.ColumnStatisticsErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateColumnStatisticsTaskSettingsRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### SampleSize
- **Type**: typing.Optional[float]

### CatalogID
- **Type**: typing.Optional[str]

### SecurityConfiguration
- **Type**: typing.Optional[str]


# UpdateConnectionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ConnectionInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateCrawlerRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.CrawlerTargetsUnionTypeDef]

### Schedule
- **Type**: typing.Optional[str]

### Classifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### TablePrefix
- **Type**: typing.Optional[str]

### SchemaChangePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaChangePolicyTypeDef]

### RecrawlPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.RecrawlPolicyTypeDef]

### LineageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LineageConfigurationTypeDef]

### LakeFormationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.LakeFormationConfigurationTypeDef]

### Configuration
- **Type**: typing.Optional[str]

### CrawlerSecurityConfiguration
- **Type**: typing.Optional[str]


# UpdateCrawlerScheduleRequestTypeDef

### CrawlerName
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Optional[str]


# UpdateCsvClassifierRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### DisableValueTrimming
- **Type**: typing.Optional[bool]

### AllowSingleColumn
- **Type**: typing.Optional[bool]

### CustomDatatypeConfigured
- **Type**: typing.Optional[bool]

### CustomDatatypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Serde
- **Type**: typing.Optional[typing.Literal['LazySimpleSerDe', 'None', 'OpenCSVSerDe']]


# UpdateDataQualityRulesetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Ruleset
- **Type**: typing.Optional[str]


# UpdateDataQualityRulesetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDatabaseRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.DatabaseInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateDevEndpointRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### PublicKey
- **Type**: typing.Optional[str]

### AddPublicKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### DeletePublicKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### CustomLibraries
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.DevEndpointCustomLibrariesTypeDef]

### UpdateEtlLibraries
- **Type**: typing.Optional[bool]

### DeleteArguments
- **Type**: typing.Optional[typing.Sequence[str]]

### AddArguments
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateGrokClassifierRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Classification
- **Type**: typing.Optional[str]

### GrokPattern
- **Type**: typing.Optional[str]

### CustomPatterns
- **Type**: typing.Optional[str]


# UpdateIntegrationResourcePropertyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SourceProcessingPropertiesTypeDef]

### TargetProcessingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TargetProcessingPropertiesTypeDef]


# UpdateIntegrationResourcePropertyResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SourceProcessingPropertiesTypeDef'>
- **Required**: Yes

### TargetProcessingProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TargetProcessingPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIntegrationTablePropertiesRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTableConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SourceTableConfigUnionTypeDef]

### TargetTableConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TargetTableConfigUnionTypeDef]


# UpdateJobFromSourceControlRequestTypeDef

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


# UpdateJobFromSourceControlResponseTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateJobRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.JobUpdateTypeDef'>
- **Required**: Yes


# UpdateJobResponseTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateJsonClassifierRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JsonPath
- **Type**: typing.Optional[str]


# UpdateMLTransformRequestTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.TransformParametersTypeDef]

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


# UpdateMLTransformResponseTypeDef

### TransformId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePartitionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionValueList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PartitionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.PartitionInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateRegistryInputTypeDef

### RegistryId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.RegistryIdTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRegistryResponseTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSchemaInputTypeDef

### SchemaId
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.SchemaIdTypeDef'>
- **Required**: Yes

### SchemaVersionNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.SchemaVersionNumberTypeDef]

### Compatibility
- **Type**: typing.Optional[typing.Literal['BACKWARD', 'BACKWARD_ALL', 'DISABLED', 'FORWARD', 'FORWARD_ALL', 'FULL', 'FULL_ALL', 'NONE']]

### Description
- **Type**: typing.Optional[str]


# UpdateSchemaResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSourceControlFromJobRequestTypeDef

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


# UpdateSourceControlFromJobResponseTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTableRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TableInputTypeDef'>
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


# UpdateTriggerRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TriggerUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TriggerUpdateTypeDef'>
- **Required**: Yes


# UpdateTriggerResponseTypeDef

### Trigger
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.TriggerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUsageProfileRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ProfileConfigurationUnionTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateUsageProfileResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserDefinedFunctionRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionInput
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.UserDefinedFunctionInputTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateWorkflowRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DefaultRunProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### MaxConcurrentRuns
- **Type**: typing.Optional[int]


# UpdateWorkflowResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glue_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateXMLClassifierRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Classification
- **Type**: typing.Optional[str]

### RowTag
- **Type**: typing.Optional[str]


# UpsertRedshiftTargetOptionsOutputTypeDef

### TableLocation
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### UpsertKeys
- **Type**: typing.Optional[typing.List[str]]


# UpsertRedshiftTargetOptionsTypeDef

### TableLocation
- **Type**: typing.Optional[str]

### ConnectionName
- **Type**: typing.Optional[str]

### UpsertKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# UpsertRedshiftTargetOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsageProfileDefinitionTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedOn
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedOn
- **Type**: typing.Optional[datetime.datetime]


# UserDefinedFunctionInputTypeDef

### FunctionName
- **Type**: typing.Optional[str]

### ClassName
- **Type**: typing.Optional[str]

### OwnerName
- **Type**: typing.Optional[str]

### OwnerType
- **Type**: typing.Optional[typing.Literal['GROUP', 'ROLE', 'USER']]

### ResourceUris
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ResourceUriTypeDef]]


# UserDefinedFunctionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ResourceUriTypeDef]]

### CatalogId
- **Type**: typing.Optional[str]


# ViewDefinitionInputTypeDef

### IsProtected
- **Type**: typing.Optional[bool]

### Definer
- **Type**: typing.Optional[str]

### Representations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glue_classes.ViewRepresentationInputTypeDef]]

### SubObjects
- **Type**: typing.Optional[typing.Sequence[str]]


# ViewDefinitionTypeDef

### IsProtected
- **Type**: typing.Optional[bool]

### Definer
- **Type**: typing.Optional[str]

### SubObjects
- **Type**: typing.Optional[typing.List[str]]

### Representations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.ViewRepresentationTypeDef]]


# ViewRepresentationInputTypeDef

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


# ViewRepresentationTypeDef

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


# ViewValidationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.ErrorDetailTypeDef]


# WorkflowGraphTypeDef

### Nodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.NodeTypeDef]]

### Edges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glue_classes.EdgeTypeDef]]


# WorkflowRunStatisticsTypeDef

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


# WorkflowRunTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.WorkflowRunStatisticsTypeDef]

### Graph
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.WorkflowGraphTypeDef]

### StartingEventBatchCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.StartingEventBatchConditionTypeDef]


# WorkflowTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.WorkflowRunTypeDef]

### Graph
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.WorkflowGraphTypeDef]

### MaxConcurrentRuns
- **Type**: typing.Optional[int]

### BlueprintDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glue_classes.BlueprintDetailsTypeDef]


# XMLClassifierTypeDef

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



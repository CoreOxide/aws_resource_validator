# Databrew Classes

# AllowedStatistics

### Statistics
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AllowedStatisticsOutput

### Statistics
- **Type**: typing.List[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteRecipeVersionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteRecipeVersionResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeVersionErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# ColumnSelector

### Regex
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ColumnStatisticsConfiguration

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.StatisticsConfiguration'>
- **Required**: Yes

### Selectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelector]]


# ColumnStatisticsConfigurationOutput

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.StatisticsConfigurationOutput'>
- **Required**: Yes

### Selectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelector]]


# ConditionExpression

### Condition
- **Type**: <class 'str'>
- **Required**: Yes

### TargetColumn
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# CreateDatasetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.Input'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'EXCEL', 'JSON', 'ORC', 'PARQUET']]

### FormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsUnion]

### PathOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PathOptionsUnion]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDatasetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfileJobRequest

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3Location'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['SSE-KMS', 'SSE-S3']]

### LogSubscription
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### MaxCapacity
- **Type**: typing.Optional[int]

### MaxRetries
- **Type**: typing.Optional[int]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ProfileConfigurationUnion]

### ValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfiguration]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Timeout
- **Type**: typing.Optional[int]

### JobSample
- **Type**: <class 'NoneType'>


# CreateProfileJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectRequest

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sample
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRecipeJobRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['SSE-KMS', 'SSE-S3']]

### LogSubscription
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### MaxCapacity
- **Type**: typing.Optional[int]

### MaxRetries
- **Type**: typing.Optional[int]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.Union]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutput]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutput]]

### ProjectName
- **Type**: typing.Optional[str]

### RecipeReference
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Timeout
- **Type**: typing.Optional[int]


# CreateRecipeJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRecipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Steps
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepUnion]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRecipeResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.RuleUnion]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScheduleRequest

### CronExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JobNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateScheduleResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CsvOptions

### Delimiter
- **Type**: typing.Optional[str]

### HeaderRow
- **Type**: typing.Optional[bool]


# CsvOutputOptions

### Delimiter
- **Type**: typing.Optional[str]


# DataCatalogInputDefinition

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TempDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3Location]


# DataCatalogOutput

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### S3Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3TableOutputOptions]

### DatabaseOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.DatabaseTableOutputOptions]

### Overwrite
- **Type**: typing.Optional[bool]


# DatabaseInputDefinition

### GlueConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseTableName
- **Type**: typing.Optional[str]

### TempDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3Location]

### QueryString
- **Type**: typing.Optional[str]


# DatabaseOutput

### GlueConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.DatabaseTableOutputOptions'>
- **Required**: Yes

### DatabaseOutputMode
- **Type**: typing.Optional[typing.Literal['NEW_TABLE']]


# DatabaseTableOutputOptions

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TempDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3Location]


# Dataset

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.Input'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'EXCEL', 'JSON', 'ORC', 'PARQUET']]

### FormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsOutput]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[typing.Literal['DATA-CATALOG', 'DATABASE', 'S3']]

### PathOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PathOptionsOutput]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceArn
- **Type**: typing.Optional[str]


# DatasetParameter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatasetParameterOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatetimeOptions

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### TimezoneOffset
- **Type**: typing.Optional[str]

### LocaleCode
- **Type**: typing.Optional[str]


# DeleteDatasetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteJobRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProjectRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRecipeVersionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecipeVersionResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteScheduleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduleResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['CSV', 'EXCEL', 'JSON', 'ORC', 'PARQUET']
- **Required**: Yes

### FormatOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsOutput'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.Input'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Literal['DATA-CATALOG', 'DATABASE', 'S3']
- **Required**: Yes

### PathOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.PathOptionsOutput'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobRunRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobRunResponse

### Attempt
- **Type**: <class 'int'>
- **Required**: Yes

### CompletedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionTime
- **Type**: <class 'int'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ProfileConfigurationOutput'>
- **Required**: Yes

### ValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfiguration]
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']
- **Required**: Yes

### LogSubscription
- **Type**: typing.Literal['DISABLE', 'ENABLE']
- **Required**: Yes

### LogGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.Extra]
- **Required**: Yes

### DataCatalogOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutput]
- **Required**: Yes

### DatabaseOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutput]
- **Required**: Yes

### RecipeReference
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.RecipeReference'>
- **Required**: Yes

### StartedBy
- **Type**: <class 'str'>
- **Required**: Yes

### StartedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobSample
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.JobSample'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProjectRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResponse

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sample
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.Sample'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### SessionStatus
- **Type**: typing.Literal['ASSIGNED', 'FAILED', 'INITIALIZING', 'PROVISIONING', 'READY', 'RECYCLING', 'ROTATING', 'TERMINATED', 'TERMINATING', 'UPDATING']
- **Required**: Yes

### OpenedBy
- **Type**: <class 'str'>
- **Required**: Yes

### OpenDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRecipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: typing.Optional[str]


# DescribeRecipeResponse

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### PublishedBy
- **Type**: <class 'str'>
- **Required**: Yes

### PublishedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RuleOutput]
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeScheduleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScheduleResponse

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### JobNames
- **Type**: typing.List[str]
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CronExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# EntityDetectorConfiguration

### EntityTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AllowedStatistics
- **Type**: typing.Optional[typing.Sequence[NoneType]]


# EntityDetectorConfigurationOutput

### EntityTypes
- **Type**: typing.List[str]
- **Required**: Yes

### AllowedStatistics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.AllowedStatisticsOutput]]


# ExcelOptions

### SheetNames
- **Type**: typing.Optional[typing.Sequence[str]]

### SheetIndexes
- **Type**: typing.Optional[typing.Sequence[int]]

### HeaderRow
- **Type**: typing.Optional[bool]


# ExcelOptionsOutput

### SheetNames
- **Type**: typing.Optional[typing.List[str]]

### SheetIndexes
- **Type**: typing.Optional[typing.List[int]]

### HeaderRow
- **Type**: typing.Optional[bool]


# Extra

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3Location'>
- **Required**: Yes

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['BROTLI', 'BZIP2', 'DEFLATE', 'GZIP', 'LZ4', 'LZO', 'SNAPPY', 'ZLIB', 'ZSTD']]

### Format
- **Type**: typing.Optional[typing.Literal['AVRO', 'CSV', 'GLUEPARQUET', 'JSON', 'ORC', 'PARQUET', 'TABLEAUHYPER', 'XML']]

### PartitionColumns
- **Type**: typing.Optional[typing.List[str]]

### Overwrite
- **Type**: typing.Optional[bool]

### FormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.OutputFormatOptions]

### MaxOutputFiles
- **Type**: typing.Optional[int]


# FilesLimit

### MaxFiles
- **Type**: <class 'int'>
- **Required**: Yes

### OrderedBy
- **Type**: typing.Optional[typing.Literal['LAST_MODIFIED_DATE']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# FilterExpression

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ValuesMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# FilterExpressionOutput

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ValuesMap
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# FormatOptions

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JsonOptions]

### Excel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ExcelOptions]

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.CsvOptions]


# FormatOptionsOutput

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JsonOptions]

### Excel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ExcelOptionsOutput]

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.CsvOptions]


# FormatOptionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Input

### S3InputDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3Location]

### DataCatalogInputDefinition
- **Type**: <class 'NoneType'>

### DatabaseInputDefinition
- **Type**: <class 'NoneType'>

### Metadata
- **Type**: <class 'NoneType'>


# Job

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRun

### Attempt
- **Type**: typing.Optional[int]

### CompletedOn
- **Type**: typing.Optional[datetime.datetime]

### DatasetName
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### ExecutionTime
- **Type**: typing.Optional[int]

### JobName
- **Type**: typing.Optional[str]

### RunId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'TIMEOUT']]

### LogSubscription
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### LogGroupName
- **Type**: typing.Optional[str]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.Extra]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutput]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutput]]

### RecipeReference
- **Type**: <class 'NoneType'>

### StartedBy
- **Type**: typing.Optional[str]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### JobSample
- **Type**: <class 'NoneType'>

### ValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfiguration]]


# JobSample

### Mode
- **Type**: typing.Optional[typing.Literal['CUSTOM_ROWS', 'FULL_DATASET']]

### Size
- **Type**: typing.Optional[int]


# JsonOptions

### MultiLine
- **Type**: typing.Optional[bool]


# ListDatasetsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfig]


# ListDatasetsResponse

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.Dataset]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobRunsRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJobRunsRequestPaginate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfig]


# ListJobRunsResponse

### JobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.JobRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

### DatasetName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]


# ListJobsRequestPaginate

### DatasetName
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfig]


# ListJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProjectsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProjectsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfig]


# ListProjectsResponse

### Projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.Project]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecipeVersionsRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRecipeVersionsRequestPaginate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfig]


# ListRecipeVersionsResponse

### Recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.Recipe]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecipesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RecipeVersion
- **Type**: typing.Optional[str]


# ListRecipesRequestPaginate

### RecipeVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfig]


# ListRecipesResponse

### Recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.Recipe]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRulesetsRequest

### TargetArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRulesetsRequestPaginate

### TargetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfig]


# ListRulesetsResponse

### Rulesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RulesetItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchedulesRequest

### JobName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSchedulesRequestPaginate

### JobName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfig]


# ListSchedulesResponse

### Schedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.Schedule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# Metadata

### SourceArn
- **Type**: typing.Optional[str]


# Output

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3Location'>
- **Required**: Yes

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['BROTLI', 'BZIP2', 'DEFLATE', 'GZIP', 'LZ4', 'LZO', 'SNAPPY', 'ZLIB', 'ZSTD']]

### Format
- **Type**: typing.Optional[typing.Literal['AVRO', 'CSV', 'GLUEPARQUET', 'JSON', 'ORC', 'PARQUET', 'TABLEAUHYPER', 'XML']]

### PartitionColumns
- **Type**: typing.Optional[typing.Sequence[str]]

### Overwrite
- **Type**: typing.Optional[bool]

### FormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.OutputFormatOptions]

### MaxOutputFiles
- **Type**: typing.Optional[int]


# OutputFormatOptions

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.CsvOutputOptions]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathOptions

### LastModifiedDateCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FilterExpression]

### FilesLimit
- **Type**: <class 'NoneType'>

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.databrew_classes.DatasetParameter]]


# PathOptionsOutput

### LastModifiedDateCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FilterExpressionOutput]

### FilesLimit
- **Type**: <class 'NoneType'>

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.databrew_classes.DatasetParameterOutput]]


# PathOptionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProfileConfiguration

### DatasetStatisticsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.StatisticsConfiguration]

### ProfileColumns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelector]]

### ColumnStatisticsConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ColumnStatisticsConfiguration]]

### EntityDetectorConfiguration
- **Type**: <class 'NoneType'>


# ProfileConfigurationOutput

### DatasetStatisticsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.StatisticsConfigurationOutput]

### ProfileColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelector]]

### ColumnStatisticsConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ColumnStatisticsConfigurationOutput]]

### EntityDetectorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.EntityDetectorConfigurationOutput]


# ProfileConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Project

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### Sample
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RoleArn
- **Type**: typing.Optional[str]

### OpenedBy
- **Type**: typing.Optional[str]

### OpenDate
- **Type**: typing.Optional[datetime.datetime]


# PublishRecipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# PublishRecipeResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# Recipe

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### ProjectName
- **Type**: typing.Optional[str]

### PublishedBy
- **Type**: typing.Optional[str]

### PublishedDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepOutput]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RecipeVersion
- **Type**: typing.Optional[str]


# RecipeAction

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RecipeActionOutput

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecipeActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecipeReference

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: typing.Optional[str]


# RecipeStep

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.RecipeActionUnion'>
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ConditionExpression]]


# RecipeStepOutput

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.RecipeActionOutput'>
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ConditionExpression]]


# RecipeStepUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecipeVersionErrorDetail

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### RecipeVersion
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


# Rule

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CheckExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]

### SubstitutionMap
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Threshold
- **Type**: <class 'NoneType'>

### ColumnSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelector]]


# RuleOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CheckExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]

### SubstitutionMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### Threshold
- **Type**: <class 'NoneType'>

### ColumnSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelector]]


# RuleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RulesetItem

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### ResourceArn
- **Type**: typing.Optional[str]

### RuleCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# S3Location

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]

### BucketOwner
- **Type**: typing.Optional[str]


# S3TableOutputOptions

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3Location'>
- **Required**: Yes


# Sample

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Schedule

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### JobNames
- **Type**: typing.Optional[typing.List[str]]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### ResourceArn
- **Type**: typing.Optional[str]

### CronExpression
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SendProjectSessionActionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Preview
- **Type**: typing.Optional[bool]

### RecipeStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepUnion]

### StepIndex
- **Type**: typing.Optional[int]

### ClientSessionId
- **Type**: typing.Optional[str]

### ViewFrame
- **Type**: <class 'NoneType'>


# SendProjectSessionActionResponse

### Result
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActionId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# StartJobRunRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartJobRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# StartProjectSessionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AssumeControl
- **Type**: typing.Optional[bool]


# StartProjectSessionResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# StatisticOverride

### Statistic
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# StatisticOverrideOutput

### Statistic
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# StatisticsConfiguration

### IncludedStatistics
- **Type**: typing.Optional[typing.Sequence[str]]

### Overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.StatisticOverride]]


# StatisticsConfigurationOutput

### IncludedStatistics
- **Type**: typing.Optional[typing.List[str]]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.StatisticOverrideOutput]]


# StopJobRunRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# StopJobRunResponse

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Threshold

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Union

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.Input'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'EXCEL', 'JSON', 'ORC', 'PARQUET']]

### FormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsUnion]

### PathOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PathOptionsUnion]


# UpdateDatasetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProfileJobRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3Location'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ProfileConfigurationUnion]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['SSE-KMS', 'SSE-S3']]

### LogSubscription
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### MaxCapacity
- **Type**: typing.Optional[int]

### MaxRetries
- **Type**: typing.Optional[int]

### ValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfiguration]]

### Timeout
- **Type**: typing.Optional[int]

### JobSample
- **Type**: <class 'NoneType'>


# UpdateProfileJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectRequest

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Sample
- **Type**: <class 'NoneType'>


# UpdateProjectResponse

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRecipeJobRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['SSE-KMS', 'SSE-S3']]

### LogSubscription
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### MaxCapacity
- **Type**: typing.Optional[int]

### MaxRetries
- **Type**: typing.Optional[int]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.Union]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutput]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutput]]

### Timeout
- **Type**: typing.Optional[int]


# UpdateRecipeJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRecipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepUnion]]


# UpdateRecipeResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.RuleUnion]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScheduleRequest

### CronExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JobNames
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateScheduleResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# ValidationConfiguration

### RulesetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationMode
- **Type**: typing.Optional[typing.Literal['CHECK_ALL']]


# ViewFrame

### StartColumnIndex
- **Type**: <class 'int'>
- **Required**: Yes

### ColumnRange
- **Type**: typing.Optional[int]

### HiddenColumns
- **Type**: typing.Optional[typing.Sequence[str]]

### StartRowIndex
- **Type**: typing.Optional[int]

### RowRange
- **Type**: typing.Optional[int]

### Analytics
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]



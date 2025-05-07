# Databrew Classes

# AllowedStatistics

### Statistics
- **Type**: typing.List[str]
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
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteRecipeVersionResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeVersionErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# ColumnSelector

### Regex
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ColumnStatisticsConfiguration

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.StatisticsConfiguration'>
- **Required**: Yes

### Selectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ColumnSelector]]


# ColumnStatisticsConfigurationOutput

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.StatisticsConfigurationOutput'>
- **Required**: Yes

### Selectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ColumnSelector]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.Input'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'EXCEL', 'JSON', 'ORC', 'PARQUET']]

### FormatOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.FormatOptions, aws_resource_validator.pydantic_models.databrew.databrew_classes.FormatOptionsOutput, NoneType]

### PathOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.PathOptions, aws_resource_validator.pydantic_models.databrew.databrew_classes.PathOptionsOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDatasetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfileJobRequest

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.ProfileConfiguration, aws_resource_validator.pydantic_models.databrew.databrew_classes.ProfileConfigurationOutput, NoneType]

### ValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ValidationConfiguration]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Timeout
- **Type**: typing.Optional[int]

### JobSample
- **Type**: <class 'NoneType'>


# CreateProfileJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateProjectResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.Output, aws_resource_validator.pydantic_models.databrew.databrew_classes.Extra]]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DataCatalogOutput]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DatabaseOutput]]

### ProjectName
- **Type**: typing.Optional[str]

### RecipeReference
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Timeout
- **Type**: typing.Optional[int]


# CreateRecipeJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRecipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Steps
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeStep, aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeStepOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRecipeResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.Rule, aws_resource_validator.pydantic_models.databrew.databrew_classes.RuleOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScheduleRequest

### CronExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JobNames
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateScheduleResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.S3TableOutputOptions]

### DatabaseOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.DatabaseTableOutputOptions]

### Overwrite
- **Type**: typing.Optional[bool]


# DatabaseInputDefinition

### GlueConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseTableName
- **Type**: typing.Optional[str]

### TempDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location]

### QueryString
- **Type**: typing.Optional[str]


# DatabaseOutput

### GlueConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.DatabaseTableOutputOptions'>
- **Required**: Yes

### DatabaseOutputMode
- **Type**: typing.Optional[typing.Literal['NEW_TABLE']]


# DatabaseTableOutputOptions

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TempDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location]


# Dataset

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.Input'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.FormatOptionsOutput]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[typing.Literal['DATA-CATALOG', 'DATABASE', 'S3']]

### PathOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PathOptionsOutput]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceArn
- **Type**: typing.Optional[str]


# DatasetParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Datetime', 'Number', 'String']
- **Required**: Yes

### DatetimeOptions
- **Type**: <class 'NoneType'>

### CreateColumn
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.FilterExpression]


# DatasetParameterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Datetime', 'Number', 'String']
- **Required**: Yes

### DatetimeOptions
- **Type**: <class 'NoneType'>

### CreateColumn
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.FilterExpressionOutput]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.FormatOptionsOutput'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.Input'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.PathOptionsOutput'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobResponse

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionMode
- **Type**: typing.Literal['SSE-KMS', 'SSE-S3']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROFILE', 'RECIPE']
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LogSubscription
- **Type**: typing.Literal['DISABLE', 'ENABLE']
- **Required**: Yes

### MaxCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### MaxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Extra]
- **Required**: Yes

### DataCatalogOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DataCatalogOutput]
- **Required**: Yes

### DatabaseOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DatabaseOutput]
- **Required**: Yes

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ProfileConfigurationOutput'>
- **Required**: Yes

### ValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ValidationConfiguration]
- **Required**: Yes

### RecipeReference
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeReference'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Timeout
- **Type**: <class 'int'>
- **Required**: Yes

### JobSample
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.JobSample'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ProfileConfigurationOutput'>
- **Required**: Yes

### ValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ValidationConfiguration]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Extra]
- **Required**: Yes

### DataCatalogOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DataCatalogOutput]
- **Required**: Yes

### DatabaseOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DatabaseOutput]
- **Required**: Yes

### RecipeReference
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeReference'>
- **Required**: Yes

### StartedBy
- **Type**: <class 'str'>
- **Required**: Yes

### StartedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobSample
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.JobSample'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.Sample'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeStepOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.RuleOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# EntityDetectorConfiguration

### EntityTypes
- **Type**: typing.List[str]
- **Required**: Yes

### AllowedStatistics
- **Type**: typing.Optional[typing.List[NoneType]]


# EntityDetectorConfigurationOutput

### EntityTypes
- **Type**: typing.List[str]
- **Required**: Yes

### AllowedStatistics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.AllowedStatisticsOutput]]


# ExcelOptions

### SheetNames
- **Type**: typing.Optional[typing.List[str]]

### SheetIndexes
- **Type**: typing.Optional[typing.List[int]]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.OutputFormatOptions]

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
- **Type**: typing.Dict[str, str]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.JsonOptions]

### Excel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.ExcelOptions]

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.CsvOptions]


# FormatOptionsOutput

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.JsonOptions]

### Excel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.ExcelOptionsOutput]

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.CsvOptions]


# Input

### S3InputDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location]

### DataCatalogInputDefinition
- **Type**: <class 'NoneType'>

### DatabaseInputDefinition
- **Type**: <class 'NoneType'>

### Metadata
- **Type**: <class 'NoneType'>


# Job

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### DatasetName
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['SSE-KMS', 'SSE-S3']]

### Type
- **Type**: typing.Optional[typing.Literal['PROFILE', 'RECIPE']]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LogSubscription
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]

### MaxCapacity
- **Type**: typing.Optional[int]

### MaxRetries
- **Type**: typing.Optional[int]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Extra]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DataCatalogOutput]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DatabaseOutput]]

### ProjectName
- **Type**: typing.Optional[str]

### RecipeReference
- **Type**: <class 'NoneType'>

### ResourceArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### JobSample
- **Type**: <class 'NoneType'>

### ValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ValidationConfiguration]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Extra]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DataCatalogOutput]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DatabaseOutput]]

### RecipeReference
- **Type**: <class 'NoneType'>

### StartedBy
- **Type**: typing.Optional[str]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### JobSample
- **Type**: <class 'NoneType'>

### ValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ValidationConfiguration]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PaginatorConfig]


# ListDatasetsResponse

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Dataset]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PaginatorConfig]


# ListJobRunsResponse

### JobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.JobRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PaginatorConfig]


# ListJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PaginatorConfig]


# ListProjectsResponse

### Projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Project]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PaginatorConfig]


# ListRecipeVersionsResponse

### Recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Recipe]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PaginatorConfig]


# ListRecipesResponse

### Recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Recipe]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PaginatorConfig]


# ListRulesetsResponse

### Rulesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.RulesetItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.PaginatorConfig]


# ListSchedulesResponse

### Schedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.Schedule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# Metadata

### SourceArn
- **Type**: typing.Optional[str]


# Output

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.OutputFormatOptions]

### MaxOutputFiles
- **Type**: typing.Optional[int]


# OutputFormatOptions

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.CsvOutputOptions]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathOptions

### LastModifiedDateCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.FilterExpression]

### FilesLimit
- **Type**: <class 'NoneType'>

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.databrew.databrew_classes.DatasetParameter]]


# PathOptionsOutput

### LastModifiedDateCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.FilterExpressionOutput]

### FilesLimit
- **Type**: <class 'NoneType'>

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.databrew.databrew_classes.DatasetParameterOutput]]


# ProfileConfiguration

### DatasetStatisticsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.StatisticsConfiguration]

### ProfileColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ColumnSelector]]

### ColumnStatisticsConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ColumnStatisticsConfiguration]]

### EntityDetectorConfiguration
- **Type**: <class 'NoneType'>


# ProfileConfigurationOutput

### DatasetStatisticsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.StatisticsConfigurationOutput]

### ProfileColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ColumnSelector]]

### ColumnStatisticsConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ColumnStatisticsConfigurationOutput]]

### EntityDetectorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew.databrew_classes.EntityDetectorConfigurationOutput]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeStepOutput]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RecipeVersion
- **Type**: typing.Optional[str]


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


# RecipeReference

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: typing.Optional[str]


# RecipeStep

### Action
- **Type**: typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeAction, aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeActionOutput]
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ConditionExpression]]


# RecipeStepOutput

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeActionOutput'>
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ConditionExpression]]


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
- **Type**: typing.Optional[typing.Dict[str, str]]

### Threshold
- **Type**: <class 'NoneType'>

### ColumnSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ColumnSelector]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ColumnSelector]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location'>
- **Required**: Yes


# Sample

### Type
- **Type**: typing.Literal['FIRST_N', 'LAST_N', 'RANDOM']
- **Required**: Yes

### Size
- **Type**: typing.Optional[int]


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeStep, aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeStepOutput, NoneType]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# StatisticOverride

### Statistic
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, str]
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
- **Type**: typing.Optional[typing.List[str]]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.StatisticOverride]]


# StatisticsConfigurationOutput

### IncludedStatistics
- **Type**: typing.Optional[typing.List[str]]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.StatisticOverrideOutput]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Threshold

### Value
- **Type**: <class 'float'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL']]

### Unit
- **Type**: typing.Optional[typing.Literal['COUNT', 'PERCENTAGE']]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDatasetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.Input'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'EXCEL', 'JSON', 'ORC', 'PARQUET']]

### FormatOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.FormatOptions, aws_resource_validator.pydantic_models.databrew.databrew_classes.FormatOptionsOutput, NoneType]

### PathOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.PathOptions, aws_resource_validator.pydantic_models.databrew.databrew_classes.PathOptionsOutput, NoneType]


# UpdateDatasetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProfileJobRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.S3Location'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.ProfileConfiguration, aws_resource_validator.pydantic_models.databrew.databrew_classes.ProfileConfigurationOutput, NoneType]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.ValidationConfiguration]]

### Timeout
- **Type**: typing.Optional[int]

### JobSample
- **Type**: <class 'NoneType'>


# UpdateProfileJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.Output, aws_resource_validator.pydantic_models.databrew.databrew_classes.Extra]]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DataCatalogOutput]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew.databrew_classes.DatabaseOutput]]

### Timeout
- **Type**: typing.Optional[int]


# UpdateRecipeJobResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRecipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeStep, aws_resource_validator.pydantic_models.databrew.databrew_classes.RecipeStepOutput]]]


# UpdateRecipeResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRulesetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.databrew.databrew_classes.Rule, aws_resource_validator.pydantic_models.databrew.databrew_classes.RuleOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateRulesetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScheduleRequest

### CronExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JobNames
- **Type**: typing.Optional[typing.List[str]]


# UpdateScheduleResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew.databrew_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[str]]

### StartRowIndex
- **Type**: typing.Optional[int]

### RowRange
- **Type**: typing.Optional[int]

### Analytics
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]



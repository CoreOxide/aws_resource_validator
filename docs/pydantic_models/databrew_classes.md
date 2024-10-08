# Pydantic Models in databrew_classes

# AllowedStatisticsTypeDef

### Statistics
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteRecipeVersionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteRecipeVersionResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeVersionErrorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ColumnSelectorTypeDef

### Regex
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ColumnStatisticsConfigurationTypeDef

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.StatisticsConfigurationTypeDef'>
- **Required**: Yes

### Selectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelectorTypeDef]]


# ConditionExpressionTypeDef

### Condition
- **Type**: <class 'str'>
- **Required**: Yes

### TargetColumn
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# CreateDatasetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.InputTypeDef'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'EXCEL', 'JSON', 'ORC', 'PARQUET']]

### FormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsTypeDef]

### PathOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PathOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDatasetResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProfileJobRequestRequestTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ProfileConfigurationTypeDef]

### ValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfigurationTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Timeout
- **Type**: typing.Optional[int]

### JobSample
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JobSampleTypeDef]


# CreateProfileJobResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.SampleTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRecipeJobRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.OutputTypeDef]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutputTypeDef]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutputTypeDef]]

### ProjectName
- **Type**: typing.Optional[str]

### RecipeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.RecipeReferenceTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Timeout
- **Type**: typing.Optional[int]


# CreateRecipeJobResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRecipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Steps
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRecipeResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRulesetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.RuleTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRulesetResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateScheduleRequestRequestTypeDef

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


# CreateScheduleResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CsvOptionsTypeDef

### Delimiter
- **Type**: typing.Optional[str]

### HeaderRow
- **Type**: typing.Optional[bool]


# CsvOutputOptionsTypeDef

### Delimiter
- **Type**: typing.Optional[str]


# DataCatalogInputDefinitionTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TempDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef]


# DataCatalogOutputTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### S3Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3TableOutputOptionsTypeDef]

### DatabaseOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.DatabaseTableOutputOptionsTypeDef]

### Overwrite
- **Type**: typing.Optional[bool]


# DatabaseInputDefinitionTypeDef

### GlueConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseTableName
- **Type**: typing.Optional[str]

### TempDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef]

### QueryString
- **Type**: typing.Optional[str]


# DatabaseOutputTypeDef

### GlueConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.DatabaseTableOutputOptionsTypeDef'>
- **Required**: Yes

### DatabaseOutputMode
- **Type**: typing.Optional[typing.Literal['NEW_TABLE']]


# DatabaseTableOutputOptionsTypeDef

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TempDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef]


# DatasetPaginatorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.InputTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsPaginatorTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[typing.Literal['DATA-CATALOG', 'DATABASE', 'S3']]

### PathOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PathOptionsPaginatorTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceArn
- **Type**: typing.Optional[str]


# DatasetParameterPaginatorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Datetime', 'Number', 'String']
- **Required**: Yes

### DatetimeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.DatetimeOptionsTypeDef]

### CreateColumn
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FilterExpressionPaginatorTypeDef]


# DatasetParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Datetime', 'Number', 'String']
- **Required**: Yes

### DatetimeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.DatetimeOptionsTypeDef]

### CreateColumn
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FilterExpressionTypeDef]


# DatasetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.InputTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[typing.Literal['DATA-CATALOG', 'DATABASE', 'S3']]

### PathOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PathOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceArn
- **Type**: typing.Optional[str]


# DatetimeOptionsTypeDef

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### TimezoneOffset
- **Type**: typing.Optional[str]

### LocaleCode
- **Type**: typing.Optional[str]


# DeleteDatasetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteJobRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRecipeVersionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecipeVersionResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRulesetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRulesetResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteScheduleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduleResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsTypeDef'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.InputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.PathOptionsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.OutputTypeDef]
- **Required**: Yes

### DataCatalogOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutputTypeDef]
- **Required**: Yes

### DatabaseOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutputTypeDef]
- **Required**: Yes

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ProfileConfigurationTypeDef'>
- **Required**: Yes

### ValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfigurationTypeDef]
- **Required**: Yes

### RecipeReference
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.RecipeReferenceTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.JobSampleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobRunRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobRunResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ProfileConfigurationTypeDef'>
- **Required**: Yes

### ValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfigurationTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.OutputTypeDef]
- **Required**: Yes

### DataCatalogOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutputTypeDef]
- **Required**: Yes

### DatabaseOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutputTypeDef]
- **Required**: Yes

### RecipeReference
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.RecipeReferenceTypeDef'>
- **Required**: Yes

### StartedBy
- **Type**: <class 'str'>
- **Required**: Yes

### StartedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobSample
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.JobSampleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProjectRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.SampleTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRecipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: typing.Optional[str]


# DescribeRecipeResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRulesetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRulesetResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RuleTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeScheduleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScheduleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EntityDetectorConfigurationTypeDef

### EntityTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AllowedStatistics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.AllowedStatisticsTypeDef]]


# ExcelOptionsPaginatorTypeDef

### SheetNames
- **Type**: typing.Optional[typing.List[str]]

### SheetIndexes
- **Type**: typing.Optional[typing.List[int]]

### HeaderRow
- **Type**: typing.Optional[bool]


# ExcelOptionsTypeDef

### SheetNames
- **Type**: typing.Optional[typing.Sequence[str]]

### SheetIndexes
- **Type**: typing.Optional[typing.Sequence[int]]

### HeaderRow
- **Type**: typing.Optional[bool]


# FilesLimitTypeDef

### MaxFiles
- **Type**: <class 'int'>
- **Required**: Yes

### OrderedBy
- **Type**: typing.Optional[typing.Literal['LAST_MODIFIED_DATE']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# FilterExpressionPaginatorTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ValuesMap
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# FilterExpressionTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ValuesMap
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# FormatOptionsPaginatorTypeDef

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JsonOptionsTypeDef]

### Excel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ExcelOptionsPaginatorTypeDef]

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.CsvOptionsTypeDef]


# FormatOptionsTypeDef

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JsonOptionsTypeDef]

### Excel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ExcelOptionsTypeDef]

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.CsvOptionsTypeDef]


# InputTypeDef

### S3InputDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef]

### DataCatalogInputDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogInputDefinitionTypeDef]

### DatabaseInputDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.DatabaseInputDefinitionTypeDef]

### Metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.MetadataTypeDef]


# JobPaginatorTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.OutputPaginatorTypeDef]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutputTypeDef]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutputTypeDef]]

### ProjectName
- **Type**: typing.Optional[str]

### RecipeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.RecipeReferenceTypeDef]

### ResourceArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### JobSample
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JobSampleTypeDef]

### ValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfigurationTypeDef]]


# JobRunPaginatorTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.OutputPaginatorTypeDef]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutputTypeDef]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutputTypeDef]]

### RecipeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.RecipeReferenceTypeDef]

### StartedBy
- **Type**: typing.Optional[str]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### JobSample
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JobSampleTypeDef]

### ValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfigurationTypeDef]]


# JobRunTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.OutputTypeDef]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutputTypeDef]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutputTypeDef]]

### RecipeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.RecipeReferenceTypeDef]

### StartedBy
- **Type**: typing.Optional[str]

### StartedOn
- **Type**: typing.Optional[datetime.datetime]

### JobSample
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JobSampleTypeDef]

### ValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfigurationTypeDef]]


# JobSampleTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['CUSTOM_ROWS', 'FULL_DATASET']]

### Size
- **Type**: typing.Optional[int]


# JobTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.OutputTypeDef]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutputTypeDef]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutputTypeDef]]

### ProjectName
- **Type**: typing.Optional[str]

### RecipeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.RecipeReferenceTypeDef]

### ResourceArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### JobSample
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JobSampleTypeDef]

### ValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfigurationTypeDef]]


# JsonOptionsTypeDef

### MultiLine
- **Type**: typing.Optional[bool]


# ListDatasetsRequestListDatasetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfigTypeDef]


# ListDatasetsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetsResponsePaginatorTypeDef

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatasetPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetsResponseTypeDef

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.DatasetTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobRunsRequestListJobRunsPaginateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfigTypeDef]


# ListJobRunsRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJobRunsResponsePaginatorTypeDef

### JobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.JobRunPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobRunsResponseTypeDef

### JobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.JobRunTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsRequestListJobsPaginateTypeDef

### DatasetName
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfigTypeDef]


# ListJobsRequestRequestTypeDef

### DatasetName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]


# ListJobsResponsePaginatorTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.JobPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.JobTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsRequestListProjectsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProjectsResponseTypeDef

### Projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.ProjectTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfigTypeDef]


# ListRecipeVersionsRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRecipeVersionsResponsePaginatorTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipePaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecipeVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecipesRequestListRecipesPaginateTypeDef

### RecipeVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfigTypeDef]


# ListRecipesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RecipeVersion
- **Type**: typing.Optional[str]


# ListRecipesResponsePaginatorTypeDef

### Recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipePaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecipesResponseTypeDef

### Recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRulesetsRequestListRulesetsPaginateTypeDef

### TargetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfigTypeDef]


# ListRulesetsRequestRequestTypeDef

### TargetArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRulesetsResponseTypeDef

### Rulesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.RulesetItemTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSchedulesRequestListSchedulesPaginateTypeDef

### JobName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PaginatorConfigTypeDef]


# ListSchedulesRequestRequestTypeDef

### JobName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSchedulesResponseTypeDef

### Schedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.databrew_classes.ScheduleTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetadataTypeDef

### SourceArn
- **Type**: typing.Optional[str]


# OutputFormatOptionsTypeDef

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.CsvOutputOptionsTypeDef]


# OutputPaginatorTypeDef

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.OutputFormatOptionsTypeDef]

### MaxOutputFiles
- **Type**: typing.Optional[int]


# OutputTypeDef

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.OutputFormatOptionsTypeDef]

### MaxOutputFiles
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathOptionsPaginatorTypeDef

### LastModifiedDateCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FilterExpressionPaginatorTypeDef]

### FilesLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FilesLimitTypeDef]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.databrew_classes.DatasetParameterPaginatorTypeDef]]


# PathOptionsTypeDef

### LastModifiedDateCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FilterExpressionTypeDef]

### FilesLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FilesLimitTypeDef]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.databrew_classes.DatasetParameterTypeDef]]


# ProfileConfigurationTypeDef

### DatasetStatisticsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.StatisticsConfigurationTypeDef]

### ProfileColumns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelectorTypeDef]]

### ColumnStatisticsConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ColumnStatisticsConfigurationTypeDef]]

### EntityDetectorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.EntityDetectorConfigurationTypeDef]


# ProjectTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.SampleTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RoleArn
- **Type**: typing.Optional[str]

### OpenedBy
- **Type**: typing.Optional[str]

### OpenDate
- **Type**: typing.Optional[datetime.datetime]


# PublishRecipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# PublishRecipeResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecipeActionPaginatorTypeDef

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


# RecipePaginatorTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepPaginatorTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RecipeVersion
- **Type**: typing.Optional[str]


# RecipeReferenceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RecipeVersion
- **Type**: typing.Optional[str]


# RecipeStepPaginatorTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.RecipeActionPaginatorTypeDef'>
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.ConditionExpressionTypeDef]]


# RecipeStepTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.RecipeActionTypeDef'>
- **Required**: Yes

### ConditionExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ConditionExpressionTypeDef]]


# RecipeTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RecipeVersion
- **Type**: typing.Optional[str]


# RecipeVersionErrorDetailTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### RecipeVersion
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# RuleTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ThresholdTypeDef]

### ColumnSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ColumnSelectorTypeDef]]


# RulesetItemTypeDef

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


# S3LocationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]

### BucketOwner
- **Type**: typing.Optional[str]


# S3TableOutputOptionsTypeDef

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef'>
- **Required**: Yes


# SampleTypeDef

### Type
- **Type**: typing.Literal['FIRST_N', 'LAST_N', 'RANDOM']
- **Required**: Yes

### Size
- **Type**: typing.Optional[int]


# ScheduleTypeDef

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


# SendProjectSessionActionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Preview
- **Type**: typing.Optional[bool]

### RecipeStep
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepTypeDef]

### StepIndex
- **Type**: typing.Optional[int]

### ClientSessionId
- **Type**: typing.Optional[str]

### ViewFrame
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ViewFrameTypeDef]


# SendProjectSessionActionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartJobRunRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartJobRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartProjectSessionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AssumeControl
- **Type**: typing.Optional[bool]


# StartProjectSessionResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatisticOverrideTypeDef

### Statistic
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# StatisticsConfigurationTypeDef

### IncludedStatistics
- **Type**: typing.Optional[typing.Sequence[str]]

### Overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.StatisticOverrideTypeDef]]


# StopJobRunRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# StopJobRunResponseTypeDef

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ThresholdTypeDef

### Value
- **Type**: <class 'float'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL']]

### Unit
- **Type**: typing.Optional[typing.Literal['COUNT', 'PERCENTAGE']]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.InputTypeDef'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'EXCEL', 'JSON', 'ORC', 'PARQUET']]

### FormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.FormatOptionsTypeDef]

### PathOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.PathOptionsTypeDef]


# UpdateDatasetResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProfileJobRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.S3LocationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.ProfileConfigurationTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.ValidationConfigurationTypeDef]]

### Timeout
- **Type**: typing.Optional[int]

### JobSample
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.JobSampleTypeDef]


# UpdateProfileJobResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectRequestRequestTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Sample
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.databrew_classes.SampleTypeDef]


# UpdateProjectResponseTypeDef

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRecipeJobRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.OutputTypeDef]]

### DataCatalogOutputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.DataCatalogOutputTypeDef]]

### DatabaseOutputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.DatabaseOutputTypeDef]]

### Timeout
- **Type**: typing.Optional[int]


# UpdateRecipeJobResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRecipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.RecipeStepTypeDef]]


# UpdateRecipeResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRulesetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.databrew_classes.RuleTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateRulesetResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScheduleRequestRequestTypeDef

### CronExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### JobNames
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateScheduleResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.databrew_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidationConfigurationTypeDef

### RulesetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationMode
- **Type**: typing.Optional[typing.Literal['CHECK_ALL']]


# ViewFrameTypeDef

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



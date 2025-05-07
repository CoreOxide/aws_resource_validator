# Machinelearning Classes

# AddTagsInput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.Tag]
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes


# AddTagsOutput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchPrediction

### BatchPredictionId
- **Type**: typing.Optional[str]

### MLModelId
- **Type**: typing.Optional[str]

### BatchPredictionDataSourceId
- **Type**: typing.Optional[str]

### InputDataLocationS3
- **Type**: typing.Optional[str]

### CreatedByIamUser
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'FAILED', 'INPROGRESS', 'PENDING']]

### OutputUri
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### ComputeTime
- **Type**: typing.Optional[int]

### FinishedAt
- **Type**: typing.Optional[datetime.datetime]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]

### TotalRecordCount
- **Type**: typing.Optional[int]

### InvalidRecordCount
- **Type**: typing.Optional[int]


# CreateBatchPredictionInput

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### BatchPredictionDataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputUri
- **Type**: <class 'str'>
- **Required**: Yes

### BatchPredictionName
- **Type**: typing.Optional[str]


# CreateBatchPredictionOutput

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceFromRDSInput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### RDSData
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RDSDataSpec'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceName
- **Type**: typing.Optional[str]

### ComputeStatistics
- **Type**: typing.Optional[bool]


# CreateDataSourceFromRDSOutput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceFromRedshiftInput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSpec
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RedshiftDataSpec'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceName
- **Type**: typing.Optional[str]

### ComputeStatistics
- **Type**: typing.Optional[bool]


# CreateDataSourceFromRedshiftOutput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceFromS3Input

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSpec
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.S3DataSpec'>
- **Required**: Yes

### DataSourceName
- **Type**: typing.Optional[str]

### ComputeStatistics
- **Type**: typing.Optional[bool]


# CreateDataSourceFromS3Output

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEvaluationInput

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationDataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationName
- **Type**: typing.Optional[str]


# CreateEvaluationOutput

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMLModelInput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelType
- **Type**: typing.Literal['BINARY', 'MULTICLASS', 'REGRESSION']
- **Required**: Yes

### TrainingDataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelName
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### Recipe
- **Type**: typing.Optional[str]

### RecipeUri
- **Type**: typing.Optional[str]


# CreateMLModelOutput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRealtimeEndpointInput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRealtimeEndpointOutput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### RealtimeEndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RealtimeEndpointInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# DataSource

### DataSourceId
- **Type**: typing.Optional[str]

### DataLocationS3
- **Type**: typing.Optional[str]

### DataRearrangement
- **Type**: typing.Optional[str]

### CreatedByIamUser
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### DataSizeInBytes
- **Type**: typing.Optional[int]

### NumberOfFiles
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'FAILED', 'INPROGRESS', 'PENDING']]

### Message
- **Type**: typing.Optional[str]

### RedshiftMetadata
- **Type**: <class 'NoneType'>

### RDSMetadata
- **Type**: <class 'NoneType'>

### RoleARN
- **Type**: typing.Optional[str]

### ComputeStatistics
- **Type**: typing.Optional[bool]

### ComputeTime
- **Type**: typing.Optional[int]

### FinishedAt
- **Type**: typing.Optional[datetime.datetime]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteBatchPredictionInput

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBatchPredictionOutput

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataSourceInput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceOutput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEvaluationInput

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEvaluationOutput

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMLModelInput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMLModelOutput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRealtimeEndpointInput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRealtimeEndpointOutput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### RealtimeEndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RealtimeEndpointInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTagsInput

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes


# DeleteTagsOutput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBatchPredictionsInput

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataSourceId', 'DataURI', 'IAMUser', 'LastUpdatedAt', 'MLModelId', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeBatchPredictionsInputPaginate

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataSourceId', 'DataURI', 'IAMUser', 'LastUpdatedAt', 'MLModelId', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.PaginatorConfig]


# DescribeBatchPredictionsInputWait

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataSourceId', 'DataURI', 'IAMUser', 'LastUpdatedAt', 'MLModelId', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeBatchPredictionsOutput

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.BatchPrediction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataSourcesInput

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataLocationS3', 'IAMUser', 'LastUpdatedAt', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeDataSourcesInputPaginate

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataLocationS3', 'IAMUser', 'LastUpdatedAt', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.PaginatorConfig]


# DescribeDataSourcesInputWait

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataLocationS3', 'IAMUser', 'LastUpdatedAt', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeDataSourcesOutput

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.DataSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEvaluationsInput

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataSourceId', 'DataURI', 'IAMUser', 'LastUpdatedAt', 'MLModelId', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeEvaluationsInputPaginate

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataSourceId', 'DataURI', 'IAMUser', 'LastUpdatedAt', 'MLModelId', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.PaginatorConfig]


# DescribeEvaluationsInputWait

### FilterVariable
- **Type**: typing.Optional[typing.Literal['CreatedAt', 'DataSourceId', 'DataURI', 'IAMUser', 'LastUpdatedAt', 'MLModelId', 'Name', 'Status']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEvaluationsOutput

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.Evaluation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMLModelsInput

### FilterVariable
- **Type**: typing.Optional[typing.Literal['Algorithm', 'CreatedAt', 'IAMUser', 'LastUpdatedAt', 'MLModelType', 'Name', 'RealtimeEndpointStatus', 'Status', 'TrainingDataSourceId', 'TrainingDataURI']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeMLModelsInputPaginate

### FilterVariable
- **Type**: typing.Optional[typing.Literal['Algorithm', 'CreatedAt', 'IAMUser', 'LastUpdatedAt', 'MLModelType', 'Name', 'RealtimeEndpointStatus', 'Status', 'TrainingDataSourceId', 'TrainingDataURI']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.PaginatorConfig]


# DescribeMLModelsInputWait

### FilterVariable
- **Type**: typing.Optional[typing.Literal['Algorithm', 'CreatedAt', 'IAMUser', 'LastUpdatedAt', 'MLModelType', 'Name', 'RealtimeEndpointStatus', 'Status', 'TrainingDataSourceId', 'TrainingDataURI']]

### EQ
- **Type**: typing.Optional[str]

### GT
- **Type**: typing.Optional[str]

### LT
- **Type**: typing.Optional[str]

### GE
- **Type**: typing.Optional[str]

### LE
- **Type**: typing.Optional[str]

### NE
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'dsc']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeMLModelsOutput

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.MLModel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTagsInput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes


# DescribeTagsOutput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# Evaluation

### EvaluationId
- **Type**: typing.Optional[str]

### MLModelId
- **Type**: typing.Optional[str]

### EvaluationDataSourceId
- **Type**: typing.Optional[str]

### InputDataLocationS3
- **Type**: typing.Optional[str]

### CreatedByIamUser
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'FAILED', 'INPROGRESS', 'PENDING']]

### PerformanceMetrics
- **Type**: <class 'NoneType'>

### Message
- **Type**: typing.Optional[str]

### ComputeTime
- **Type**: typing.Optional[int]

### FinishedAt
- **Type**: typing.Optional[datetime.datetime]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]


# GetBatchPredictionInput

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBatchPredictionOutput

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### BatchPredictionDataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataLocationS3
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByIamUser
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'FAILED', 'INPROGRESS', 'PENDING']
- **Required**: Yes

### OutputUri
- **Type**: <class 'str'>
- **Required**: Yes

### LogUri
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeTime
- **Type**: <class 'int'>
- **Required**: Yes

### FinishedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TotalRecordCount
- **Type**: <class 'int'>
- **Required**: Yes

### InvalidRecordCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSourceInput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Verbose
- **Type**: typing.Optional[bool]


# GetDataSourceOutput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataLocationS3
- **Type**: <class 'str'>
- **Required**: Yes

### DataRearrangement
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByIamUser
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfFiles
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'FAILED', 'INPROGRESS', 'PENDING']
- **Required**: Yes

### LogUri
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### RedshiftMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RedshiftMetadata'>
- **Required**: Yes

### RDSMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RDSMetadata'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeStatistics
- **Type**: <class 'bool'>
- **Required**: Yes

### ComputeTime
- **Type**: <class 'int'>
- **Required**: Yes

### FinishedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSourceSchema
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# GetEvaluationInput

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvaluationOutput

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationDataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataLocationS3
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByIamUser
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'FAILED', 'INPROGRESS', 'PENDING']
- **Required**: Yes

### PerformanceMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.PerformanceMetrics'>
- **Required**: Yes

### LogUri
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeTime
- **Type**: <class 'int'>
- **Required**: Yes

### FinishedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLModelInput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### Verbose
- **Type**: typing.Optional[bool]


# GetMLModelOutput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingDataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByIamUser
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'FAILED', 'INPROGRESS', 'PENDING']
- **Required**: Yes

### SizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### EndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RealtimeEndpointInfo'>
- **Required**: Yes

### TrainingParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### InputDataLocationS3
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelType
- **Type**: typing.Literal['BINARY', 'MULTICLASS', 'REGRESSION']
- **Required**: Yes

### ScoreThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### ScoreThresholdLastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LogUri
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeTime
- **Type**: <class 'int'>
- **Required**: Yes

### FinishedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Recipe
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# MLModel

### MLModelId
- **Type**: typing.Optional[str]

### TrainingDataSourceId
- **Type**: typing.Optional[str]

### CreatedByIamUser
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'FAILED', 'INPROGRESS', 'PENDING']]

### SizeInBytes
- **Type**: typing.Optional[int]

### EndpointInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RealtimeEndpointInfo]

### TrainingParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### InputDataLocationS3
- **Type**: typing.Optional[str]

### Algorithm
- **Type**: typing.Optional[typing.Literal['sgd']]

### MLModelType
- **Type**: typing.Optional[typing.Literal['BINARY', 'MULTICLASS', 'REGRESSION']]

### ScoreThreshold
- **Type**: typing.Optional[float]

### ScoreThresholdLastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Message
- **Type**: typing.Optional[str]

### ComputeTime
- **Type**: typing.Optional[int]

### FinishedAt
- **Type**: typing.Optional[datetime.datetime]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceMetrics

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]


# PredictInput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### Record
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### PredictEndpoint
- **Type**: <class 'str'>
- **Required**: Yes


# PredictOutput

### Prediction
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.Prediction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# Prediction

### predictedLabel
- **Type**: typing.Optional[str]

### predictedValue
- **Type**: typing.Optional[float]

### predictedScores
- **Type**: typing.Optional[typing.Dict[str, float]]

### details
- **Type**: typing.Optional[typing.Dict[typing.Literal['Algorithm', 'PredictiveModelType'], str]]


# RDSDataSpec

### DatabaseInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RDSDatabase'>
- **Required**: Yes

### SelectSqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RDSDatabaseCredentials'>
- **Required**: Yes

### S3StagingLocation
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceRole
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRole
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### DataRearrangement
- **Type**: typing.Optional[str]

### DataSchema
- **Type**: typing.Optional[str]

### DataSchemaUri
- **Type**: typing.Optional[str]


# RDSDatabase

### InstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# RDSDatabaseCredentials

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# RDSMetadata

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RDSDatabase]

### DatabaseUserName
- **Type**: typing.Optional[str]

### SelectSqlQuery
- **Type**: typing.Optional[str]

### ResourceRole
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### DataPipelineId
- **Type**: typing.Optional[str]


# RealtimeEndpointInfo

### PeakRequestsPerSecond
- **Type**: typing.Optional[int]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### EndpointUrl
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'NONE', 'READY', 'UPDATING']]


# RedshiftDataSpec

### DatabaseInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RedshiftDatabase'>
- **Required**: Yes

### SelectSqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.RedshiftDatabaseCredentials'>
- **Required**: Yes

### S3StagingLocation
- **Type**: <class 'str'>
- **Required**: Yes

### DataRearrangement
- **Type**: typing.Optional[str]

### DataSchema
- **Type**: typing.Optional[str]

### DataSchemaUri
- **Type**: typing.Optional[str]


# RedshiftDatabase

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftDatabaseCredentials

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftMetadata

### RedshiftDatabase
- **Type**: <class 'NoneType'>

### DatabaseUserName
- **Type**: typing.Optional[str]

### SelectSqlQuery
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


# S3DataSpec

### DataLocationS3
- **Type**: <class 'str'>
- **Required**: Yes

### DataRearrangement
- **Type**: typing.Optional[str]

### DataSchema
- **Type**: typing.Optional[str]

### DataSchemaLocationS3
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UpdateBatchPredictionInput

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### BatchPredictionName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBatchPredictionOutput

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSourceInput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDataSourceOutput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEvaluationInput

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateEvaluationOutput

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMLModelInput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelName
- **Type**: typing.Optional[str]

### ScoreThreshold
- **Type**: typing.Optional[float]


# UpdateMLModelOutput

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning.machinelearning_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



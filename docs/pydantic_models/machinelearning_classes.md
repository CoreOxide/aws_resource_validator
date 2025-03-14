# Machinelearning Classes

# AddTagsInputTypeDef

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.machinelearning_classes.TagTypeDef]
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes


# AddTagsOutputTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchPredictionTypeDef

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


# CreateBatchPredictionInputTypeDef

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


# CreateBatchPredictionOutputTypeDef

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceFromRDSInputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### RDSData
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RDSDataSpecTypeDef'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceName
- **Type**: typing.Optional[str]

### ComputeStatistics
- **Type**: typing.Optional[bool]


# CreateDataSourceFromRDSOutputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceFromRedshiftInputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSpec
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RedshiftDataSpecTypeDef'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceName
- **Type**: typing.Optional[str]

### ComputeStatistics
- **Type**: typing.Optional[bool]


# CreateDataSourceFromRedshiftOutputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceFromS3InputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSpec
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.S3DataSpecTypeDef'>
- **Required**: Yes

### DataSourceName
- **Type**: typing.Optional[str]

### ComputeStatistics
- **Type**: typing.Optional[bool]


# CreateDataSourceFromS3OutputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEvaluationInputTypeDef

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


# CreateEvaluationOutputTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMLModelInputTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Recipe
- **Type**: typing.Optional[str]

### RecipeUri
- **Type**: typing.Optional[str]


# CreateMLModelOutputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRealtimeEndpointInputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRealtimeEndpointOutputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### RealtimeEndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RealtimeEndpointInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSourceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.RedshiftMetadataTypeDef]

### RDSMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.RDSMetadataTypeDef]

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


# DeleteBatchPredictionInputTypeDef

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBatchPredictionOutputTypeDef

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataSourceInputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceOutputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEvaluationInputTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEvaluationOutputTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMLModelInputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMLModelOutputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRealtimeEndpointInputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRealtimeEndpointOutputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### RealtimeEndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RealtimeEndpointInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTagsInputTypeDef

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes


# DeleteTagsOutputTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBatchPredictionsInputPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.PaginatorConfigTypeDef]


# DescribeBatchPredictionsInputTypeDef

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


# DescribeBatchPredictionsInputWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.WaiterConfigTypeDef]


# DescribeBatchPredictionsOutputTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning_classes.BatchPredictionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataSourcesInputPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.PaginatorConfigTypeDef]


# DescribeDataSourcesInputTypeDef

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


# DescribeDataSourcesInputWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.WaiterConfigTypeDef]


# DescribeDataSourcesOutputTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning_classes.DataSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEvaluationsInputPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.PaginatorConfigTypeDef]


# DescribeEvaluationsInputTypeDef

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


# DescribeEvaluationsInputWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.WaiterConfigTypeDef]


# DescribeEvaluationsOutputTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning_classes.EvaluationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMLModelsInputPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.PaginatorConfigTypeDef]


# DescribeMLModelsInputTypeDef

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


# DescribeMLModelsInputWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.WaiterConfigTypeDef]


# DescribeMLModelsOutputTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning_classes.MLModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTagsInputTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes


# DescribeTagsOutputTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['BatchPrediction', 'DataSource', 'Evaluation', 'MLModel']
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.machinelearning_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EvaluationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.PerformanceMetricsTypeDef]

### Message
- **Type**: typing.Optional[str]

### ComputeTime
- **Type**: typing.Optional[int]

### FinishedAt
- **Type**: typing.Optional[datetime.datetime]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]


# GetBatchPredictionInputTypeDef

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBatchPredictionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSourceInputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Verbose
- **Type**: typing.Optional[bool]


# GetDataSourceOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RedshiftMetadataTypeDef'>
- **Required**: Yes

### RDSMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RDSMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvaluationInputTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvaluationOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.PerformanceMetricsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLModelInputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### Verbose
- **Type**: typing.Optional[bool]


# GetMLModelOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RealtimeEndpointInfoTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MLModelTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.RealtimeEndpointInfoTypeDef]

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceMetricsTypeDef

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]


# PredictInputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### Record
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PredictEndpoint
- **Type**: <class 'str'>
- **Required**: Yes


# PredictOutputTypeDef

### Prediction
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.PredictionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PredictionTypeDef

### predictedLabel
- **Type**: typing.Optional[str]

### predictedValue
- **Type**: typing.Optional[float]

### predictedScores
- **Type**: typing.Optional[typing.Dict[str, float]]

### details
- **Type**: typing.Optional[typing.Dict[typing.Literal['Algorithm', 'PredictiveModelType'], str]]


# RDSDataSpecTypeDef

### DatabaseInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RDSDatabaseTypeDef'>
- **Required**: Yes

### SelectSqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RDSDatabaseCredentialsTypeDef'>
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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DataRearrangement
- **Type**: typing.Optional[str]

### DataSchema
- **Type**: typing.Optional[str]

### DataSchemaUri
- **Type**: typing.Optional[str]


# RDSDatabaseCredentialsTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# RDSDatabaseTypeDef

### InstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# RDSMetadataTypeDef

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.RDSDatabaseTypeDef]

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


# RealtimeEndpointInfoTypeDef

### PeakRequestsPerSecond
- **Type**: typing.Optional[int]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### EndpointUrl
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'NONE', 'READY', 'UPDATING']]


# RedshiftDataSpecTypeDef

### DatabaseInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RedshiftDatabaseTypeDef'>
- **Required**: Yes

### SelectSqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.RedshiftDatabaseCredentialsTypeDef'>
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


# RedshiftDatabaseCredentialsTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftDatabaseTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftMetadataTypeDef

### RedshiftDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.machinelearning_classes.RedshiftDatabaseTypeDef]

### DatabaseUserName
- **Type**: typing.Optional[str]

### SelectSqlQuery
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


# S3DataSpecTypeDef

### DataLocationS3
- **Type**: <class 'str'>
- **Required**: Yes

### DataRearrangement
- **Type**: typing.Optional[str]

### DataSchema
- **Type**: typing.Optional[str]

### DataSchemaLocationS3
- **Type**: typing.Optional[str]


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UpdateBatchPredictionInputTypeDef

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### BatchPredictionName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBatchPredictionOutputTypeDef

### BatchPredictionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSourceInputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDataSourceOutputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEvaluationInputTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateEvaluationOutputTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMLModelInputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### MLModelName
- **Type**: typing.Optional[str]

### ScoreThreshold
- **Type**: typing.Optional[float]


# UpdateMLModelOutputTypeDef

### MLModelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.machinelearning_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



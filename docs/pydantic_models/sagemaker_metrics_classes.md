# Sagemaker Metrics Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetMetricsRequestTypeDef

### MetricQueries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_metrics_classes.MetricQueryTypeDef]
- **Required**: Yes


# BatchGetMetricsResponseTypeDef

### MetricQueryResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_metrics_classes.MetricQueryResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_metrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutMetricsErrorTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['CONFLICT_ERROR', 'INTERNAL_ERROR', 'METRIC_LIMIT_EXCEEDED', 'VALIDATION_ERROR']]

### MetricIndex
- **Type**: typing.Optional[int]


# BatchPutMetricsRequestTypeDef

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricData
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_metrics_classes.RawMetricDataTypeDef]
- **Required**: Yes


# BatchPutMetricsResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_metrics_classes.BatchPutMetricsErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_metrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricQueryResultTypeDef

### Status
- **Type**: typing.Literal['Complete', 'InternalError', 'Truncated', 'ValidationError']
- **Required**: Yes

### XAxisValues
- **Type**: typing.List[int]
- **Required**: Yes

### MetricValues
- **Type**: typing.List[float]
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]


# MetricQueryTypeDef

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Literal['Avg', 'Count', 'Last', 'Max', 'Min', 'StdDev']
- **Required**: Yes

### Period
- **Type**: typing.Literal['FiveMinute', 'IterationNumber', 'OneHour', 'OneMinute']
- **Required**: Yes

### XAxisType
- **Type**: typing.Literal['IterationNumber', 'Timestamp']
- **Required**: Yes

### Start
- **Type**: typing.Optional[int]

### End
- **Type**: typing.Optional[int]


# RawMetricDataTypeDef

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_metrics_classes.TimestampTypeDef'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes

### Step
- **Type**: typing.Optional[int]


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


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


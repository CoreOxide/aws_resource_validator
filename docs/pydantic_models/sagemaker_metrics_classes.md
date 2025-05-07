# Sagemaker Metrics Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetMetricsRequest

### MetricQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_metrics.sagemaker_metrics_classes.MetricQuery]
- **Required**: Yes


# BatchGetMetricsResponse

### MetricQueryResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_metrics.sagemaker_metrics_classes.MetricQueryResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_metrics.sagemaker_metrics_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutMetricsError

### Code
- **Type**: typing.Optional[typing.Literal['CONFLICT_ERROR', 'INTERNAL_ERROR', 'METRIC_LIMIT_EXCEEDED', 'VALIDATION_ERROR']]

### MetricIndex
- **Type**: typing.Optional[int]


# BatchPutMetricsRequest

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_metrics.sagemaker_metrics_classes.RawMetricData]
- **Required**: Yes


# BatchPutMetricsResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_metrics.sagemaker_metrics_classes.BatchPutMetricsError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_metrics.sagemaker_metrics_classes.ResponseMetadata'>
- **Required**: Yes


# MetricQuery

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


# MetricQueryResult

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


# RawMetricData

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes

### Step
- **Type**: typing.Optional[int]


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



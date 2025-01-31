# Sagemaker Metrics Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchPutMetricsErrorTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['CONFLICT_ERROR', 'INTERNAL_ERROR', 'METRIC_LIMIT_EXCEEDED', 'VALIDATION_ERROR']]

### MetricIndex
- **Type**: typing.Optional[int]


# BatchPutMetricsRequestRequestTypeDef

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


# RawMetricDataTypeDef

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



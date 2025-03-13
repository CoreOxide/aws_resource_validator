# Sagemakermetrics Service

### ExperimentEntityName
- **Type**: string
- **Pattern**: `^[a-z0-9](-*[a-z0-9]){0,119}`
- **Min Length**: 1
- **Max Length**: 120

### Message
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 2048

### MetricName
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 255

### SageMakerResourceArn
- **Type**: string
- **Pattern**: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-].*/.*`
- **Max Length**: 2048


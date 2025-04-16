# Sagemaker Edge Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Checksum

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Definition

### ModelHandle
- **Type**: typing.Optional[str]

### S3Url
- **Type**: typing.Optional[str]

### Checksum
- **Type**: <class 'NoneType'>

### State
- **Type**: typing.Optional[typing.Literal['DEPLOY', 'UNDEPLOY']]


# DeploymentModel

### ModelHandle
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### DesiredState
- **Type**: typing.Optional[typing.Literal['DEPLOY', 'UNDEPLOY']]

### State
- **Type**: typing.Optional[typing.Literal['DEPLOY', 'UNDEPLOY']]

### Status
- **Type**: typing.Optional[typing.Literal['FAIL', 'SUCCESS']]

### StatusReason
- **Type**: typing.Optional[str]

### RollbackFailureReason
- **Type**: typing.Optional[str]


# DeploymentResult

### DeploymentName
- **Type**: typing.Optional[str]

### DeploymentStatus
- **Type**: typing.Optional[str]

### DeploymentStatusMessage
- **Type**: typing.Optional[str]

### DeploymentStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.Timestamp]

### DeploymentEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.Timestamp]

### DeploymentModels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.DeploymentModel]]


# EdgeDeployment

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EdgeMetric

### Dimension
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]

### Timestamp
- **Type**: <class 'NoneType'>


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentsRequest

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentsResult

### Deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_edge_classes.EdgeDeployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceRegistrationRequest

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceRegistrationResult

### DeviceRegistration
- **Type**: <class 'str'>
- **Required**: Yes

### CacheTTL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge_classes.ResponseMetadata'>
- **Required**: Yes


# Model

### ModelName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### LatestSampleTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.Timestamp]

### LatestInference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.Timestamp]

### ModelMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.EdgeMetric]]


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


# SendHeartbeatRequest

### AgentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### AgentMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.EdgeMetric]]

### Models
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.Model]]

### DeploymentResult
- **Type**: <class 'NoneType'>


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


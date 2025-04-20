# Sagemaker Edge Sagemaker Edge Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Checksum

### Type
- **Type**: typing.Optional[typing.Literal['SHA1']]

### Sum
- **Type**: typing.Optional[str]


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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DeploymentEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DeploymentModels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.DeploymentModel]]


# EdgeDeployment

### DeploymentName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['Model']]

### FailureHandlingPolicy
- **Type**: typing.Optional[typing.Literal['DO_NOTHING', 'ROLLBACK_ON_FAILURE']]

### Definitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.Definition]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.EdgeDeployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.ResponseMetadata'>
- **Required**: Yes


# Model

### ModelName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### LatestSampleTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LatestInference
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModelMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.EdgeMetric]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.EdgeMetric]]

### Models
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_edge.sagemaker_edge_classes.Model]]

### DeploymentResult
- **Type**: <class 'NoneType'>



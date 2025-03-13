# Sagemaker Edge Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChecksumTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefinitionTypeDef

### ModelHandle
- **Type**: typing.Optional[str]

### S3Url
- **Type**: typing.Optional[str]

### Checksum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.ChecksumTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['DEPLOY', 'UNDEPLOY']]


# DeploymentModelTypeDef

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


# DeploymentResultTypeDef

### DeploymentName
- **Type**: typing.Optional[str]

### DeploymentStatus
- **Type**: typing.Optional[str]

### DeploymentStatusMessage
- **Type**: typing.Optional[str]

### DeploymentStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.TimestampTypeDef]

### DeploymentEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.TimestampTypeDef]

### DeploymentModels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.DeploymentModelTypeDef]]


# EdgeDeploymentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EdgeMetricTypeDef

### Dimension
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]

### Timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.TimestampTypeDef]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentsRequestTypeDef

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentsResultTypeDef

### Deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_edge_classes.EdgeDeploymentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeviceRegistrationRequestTypeDef

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceRegistrationResultTypeDef

### DeviceRegistration
- **Type**: <class 'str'>
- **Required**: Yes

### CacheTTL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModelTypeDef

### ModelName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### LatestSampleTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.TimestampTypeDef]

### LatestInference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.TimestampTypeDef]

### ModelMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.EdgeMetricTypeDef]]


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


# SendHeartbeatRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.EdgeMetricTypeDef]]

### Models
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.ModelTypeDef]]

### DeploymentResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_edge_classes.DeploymentResultTypeDef]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


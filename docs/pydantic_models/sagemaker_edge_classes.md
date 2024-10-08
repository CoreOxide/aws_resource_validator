# Pydantic Models in sagemaker_edge_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChecksumTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['SHA1']]

### Sum
- **Type**: typing.Optional[str]


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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DeploymentEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DeploymentModels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.DeploymentModelTypeDef]]


# EdgeDeploymentTypeDef

### DeploymentName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['Model']]

### FailureHandlingPolicy
- **Type**: typing.Optional[typing.Literal['DO_NOTHING', 'ROLLBACK_ON_FAILURE']]

### Definitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_edge_classes.DefinitionTypeDef]]


# EdgeMetricTypeDef

### Dimension
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]

### Timestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_edge_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentsRequestRequestTypeDef

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


# GetDeviceRegistrationRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LatestInference
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ModelMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_edge_classes.EdgeMetricTypeDef]]


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


# SendHeartbeatRequestRequestTypeDef

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



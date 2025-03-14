# Simspaceweaver Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsLogGroupTypeDef

### LogGroupArn
- **Type**: typing.Optional[str]


# CreateSnapshotInputTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.S3DestinationTypeDef'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInputTypeDef

### App
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSimulationInputTypeDef

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInputTypeDef

### App
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppOutputTypeDef

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationAppEndpointInfoTypeDef'>
- **Required**: Yes

### LaunchOverrides
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.LaunchOverridesOutputTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ERROR', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'UNKNOWN']
- **Required**: Yes

### TargetStatus
- **Type**: typing.Literal['STARTED', 'STOPPED', 'UNKNOWN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSimulationInputTypeDef

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSimulationOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### LiveSimulationState
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.LiveSimulationStateTypeDef'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes

### MaximumDuration
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaError
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.S3LocationTypeDef'>
- **Required**: Yes

### SnapshotS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.S3LocationTypeDef'>
- **Required**: Yes

### StartError
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DELETED', 'DELETING', 'FAILED', 'SNAPSHOT_IN_PROGRESS', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'UNKNOWN']
- **Required**: Yes

### TargetStatus
- **Type**: typing.Literal['DELETED', 'STARTED', 'STOPPED', 'UNKNOWN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainTypeDef

### Lifecycle
- **Type**: typing.Optional[typing.Literal['ByRequest', 'BySpatialSubdivision', 'PerWorker', 'Unknown']]

### Name
- **Type**: typing.Optional[str]


# LaunchOverridesOutputTypeDef

### LaunchCommands
- **Type**: typing.Optional[typing.List[str]]


# LaunchOverridesTypeDef

### LaunchCommands
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchOverridesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAppsInputTypeDef

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppsOutputTypeDef

### Apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationAppMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSimulationsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSimulationsOutputTypeDef

### Simulations
- **Type**: typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LiveSimulationStateTypeDef

### Clocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationClockTypeDef]]

### Domains
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.DomainTypeDef]]


# LogDestinationTypeDef

### CloudWatchLogsLogGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.simspaceweaver_classes.CloudWatchLogsLogGroupTypeDef]


# LoggingConfigurationTypeDef

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.LogDestinationTypeDef]]


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


# S3DestinationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKeyPrefix
- **Type**: typing.Optional[str]


# S3LocationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes


# SimulationAppEndpointInfoTypeDef

### Address
- **Type**: typing.Optional[str]

### IngressPortMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationAppPortMappingTypeDef]]


# SimulationAppMetadataTypeDef

### Domain
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Simulation
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ERROR', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'UNKNOWN']]

### TargetStatus
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED', 'UNKNOWN']]


# SimulationAppPortMappingTypeDef

### Actual
- **Type**: typing.Optional[int]

### Declared
- **Type**: typing.Optional[int]


# SimulationClockTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'UNKNOWN']]

### TargetStatus
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED', 'UNKNOWN']]


# SimulationMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'FAILED', 'SNAPSHOT_IN_PROGRESS', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'UNKNOWN']]

### TargetStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'STARTED', 'STOPPED', 'UNKNOWN']]


# StartAppInputTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LaunchOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.simspaceweaver_classes.LaunchOverridesUnionTypeDef]


# StartAppOutputTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartClockInputTypeDef

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# StartSimulationInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### MaximumDuration
- **Type**: typing.Optional[str]

### SchemaS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.simspaceweaver_classes.S3LocationTypeDef]

### SnapshotS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.simspaceweaver_classes.S3LocationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartSimulationOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopAppInputTypeDef

### App
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# StopClockInputTypeDef

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# StopSimulationInputTypeDef

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes



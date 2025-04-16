# Simspaceweaver Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsLogGroup

### LogGroupArn
- **Type**: typing.Optional[str]


# CreateSnapshotInput

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.S3Destination'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInput

### App
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSimulationInput

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInput

### App
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppOutput

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationAppEndpointInfo'>
- **Required**: Yes

### LaunchOverrides
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.LaunchOverridesOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSimulationInput

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSimulationOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.LiveSimulationState'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.LoggingConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.S3Location'>
- **Required**: Yes

### SnapshotS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.S3Location'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadata'>
- **Required**: Yes


# Domain

### Lifecycle
- **Type**: typing.Optional[typing.Literal['ByRequest', 'BySpatialSubdivision', 'PerWorker', 'Unknown']]

### Name
- **Type**: typing.Optional[str]


# LaunchOverrides

### LaunchCommands
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchOverridesOutput

### LaunchCommands
- **Type**: typing.Optional[typing.List[str]]


# LaunchOverridesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAppsInput

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppsOutput

### Apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationAppMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSimulationsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSimulationsOutput

### Simulations
- **Type**: typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadata'>
- **Required**: Yes


# LiveSimulationState

### Clocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationClock]]

### Domains
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.Domain]]


# LogDestination

### CloudWatchLogsLogGroup
- **Type**: <class 'NoneType'>


# LoggingConfiguration

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.LogDestination]]


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


# S3Destination

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKeyPrefix
- **Type**: typing.Optional[str]


# S3Location

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes


# SimulationAppEndpointInfo

### Address
- **Type**: typing.Optional[str]

### IngressPortMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.simspaceweaver_classes.SimulationAppPortMapping]]


# SimulationAppMetadata

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


# SimulationAppPortMapping

### Actual
- **Type**: typing.Optional[int]

### Declared
- **Type**: typing.Optional[int]


# SimulationClock

### Status
- **Type**: typing.Optional[typing.Literal['STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'UNKNOWN']]

### TargetStatus
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED', 'UNKNOWN']]


# SimulationMetadata

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


# StartAppInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.simspaceweaver_classes.LaunchOverridesUnion]


# StartAppOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadata'>
- **Required**: Yes


# StartClockInput

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# StartSimulationInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.simspaceweaver_classes.S3Location]

### SnapshotS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.simspaceweaver_classes.S3Location]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartSimulationOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.simspaceweaver_classes.ResponseMetadata'>
- **Required**: Yes


# StopAppInput

### App
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# StopClockInput

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# StopSimulationInput

### Simulation
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes



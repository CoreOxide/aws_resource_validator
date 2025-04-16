# Scheduler Classes

# AwsVpcConfiguration

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsVpcConfigurationOutput

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityProviderStrategyItem

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes

### base
- **Type**: typing.Optional[int]

### weight
- **Type**: typing.Optional[int]


# CreateScheduleGroupInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.Tag]]


# CreateScheduleGroupOutput

### ScheduleGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScheduleInput

### FlexibleTimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.FlexibleTimeWindow'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.TargetUnion'>
- **Required**: Yes

### ActionAfterCompletion
- **Type**: typing.Optional[typing.Literal['DELETE', 'NONE']]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.Timestamp]

### GroupName
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.Timestamp]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateScheduleOutput

### ScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadata'>
- **Required**: Yes


# DeadLetterConfig

### Arn
- **Type**: typing.Optional[str]


# DeleteScheduleGroupInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteScheduleInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# EcsParameters

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.CapacityProviderStrategyItem]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### Group
- **Type**: typing.Optional[str]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: <class 'NoneType'>

### PlacementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.PlacementConstraint]]

### PlacementStrategy
- **Type**: typing.Optional[typing.Sequence[NoneType]]

### PlatformVersion
- **Type**: typing.Optional[str]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, str]]]

### TaskCount
- **Type**: typing.Optional[int]


# EcsParametersOutput

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.scheduler_classes.CapacityProviderStrategyItem]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### Group
- **Type**: typing.Optional[str]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.NetworkConfigurationOutput]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.scheduler_classes.PlacementConstraint]]

### PlacementStrategy
- **Type**: typing.Optional[typing.List[NoneType]]

### PlatformVersion
- **Type**: typing.Optional[str]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]

### TaskCount
- **Type**: typing.Optional[int]


# EventBridgeParameters

### DetailType
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes


# FlexibleTimeWindow

### Mode
- **Type**: typing.Literal['FLEXIBLE', 'OFF']
- **Required**: Yes

### MaximumWindowInMinutes
- **Type**: typing.Optional[int]


# GetScheduleGroupInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetScheduleGroupOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadata'>
- **Required**: Yes


# GetScheduleInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]


# GetScheduleOutput

### ActionAfterCompletion
- **Type**: typing.Literal['DELETE', 'NONE']
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EndDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FlexibleTimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.FlexibleTimeWindow'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastModificationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpressionTimezone
- **Type**: <class 'str'>
- **Required**: Yes

### StartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.TargetOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadata'>
- **Required**: Yes


# KinesisParameters

### PartitionKey
- **Type**: <class 'str'>
- **Required**: Yes


# ListScheduleGroupsInput

### MaxResults
- **Type**: typing.Optional[int]

### NamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListScheduleGroupsInputPaginate

### NamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.PaginatorConfig]


# ListScheduleGroupsOutput

### ScheduleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.scheduler_classes.ScheduleGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchedulesInput

### GroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ListSchedulesInputPaginate

### GroupName
- **Type**: typing.Optional[str]

### NamePrefix
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.PaginatorConfig]


# ListSchedulesOutput

### Schedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.scheduler_classes.ScheduleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.scheduler_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadata'>
- **Required**: Yes


# NetworkConfiguration

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.AwsVpcConfiguration]


# NetworkConfigurationOutput

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.AwsVpcConfigurationOutput]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacementConstraint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PlacementStrategy

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RetryPolicy

### MaximumEventAgeInSeconds
- **Type**: typing.Optional[int]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]


# SageMakerPipelineParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SageMakerPipelineParameters

### PipelineParameterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.SageMakerPipelineParameter]]


# SageMakerPipelineParametersOutput

### PipelineParameterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.scheduler_classes.SageMakerPipelineParameter]]


# ScheduleGroupSummary

### Arn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### LastModificationDate
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]


# ScheduleSummary

### Arn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### GroupName
- **Type**: typing.Optional[str]

### LastModificationDate
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.TargetSummary]


# SqsParameters

### MessageGroupId
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.Tag]
- **Required**: Yes


# Target

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterConfig
- **Type**: <class 'NoneType'>

### EcsParameters
- **Type**: <class 'NoneType'>

### EventBridgeParameters
- **Type**: <class 'NoneType'>

### Input
- **Type**: typing.Optional[str]

### KinesisParameters
- **Type**: <class 'NoneType'>

### RetryPolicy
- **Type**: <class 'NoneType'>

### SageMakerPipelineParameters
- **Type**: <class 'NoneType'>

### SqsParameters
- **Type**: <class 'NoneType'>


# TargetOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterConfig
- **Type**: <class 'NoneType'>

### EcsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.EcsParametersOutput]

### EventBridgeParameters
- **Type**: <class 'NoneType'>

### Input
- **Type**: typing.Optional[str]

### KinesisParameters
- **Type**: <class 'NoneType'>

### RetryPolicy
- **Type**: <class 'NoneType'>

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.SageMakerPipelineParametersOutput]

### SqsParameters
- **Type**: <class 'NoneType'>


# TargetSummary

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# TargetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateScheduleInput

### FlexibleTimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.FlexibleTimeWindow'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.TargetUnion'>
- **Required**: Yes

### ActionAfterCompletion
- **Type**: typing.Optional[typing.Literal['DELETE', 'NONE']]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.Timestamp]

### GroupName
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.Timestamp]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateScheduleOutput

### ScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadata'>
- **Required**: Yes



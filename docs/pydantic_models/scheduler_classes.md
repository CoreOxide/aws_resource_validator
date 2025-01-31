# scheduler_classes

# AwsVpcConfigurationTypeDef

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityProviderStrategyItemTypeDef

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes

### base
- **Type**: typing.Optional[int]

### weight
- **Type**: typing.Optional[int]


# CreateScheduleGroupInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.TagTypeDef]]


# CreateScheduleGroupOutputTypeDef

### ScheduleGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateScheduleInputRequestTypeDef

### FlexibleTimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.FlexibleTimeWindowTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.TargetTypeDef'>
- **Required**: Yes

### ActionAfterCompletion
- **Type**: typing.Optional[typing.Literal['DELETE', 'NONE']]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### GroupName
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateScheduleOutputTypeDef

### ScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeadLetterConfigTypeDef

### Arn
- **Type**: typing.Optional[str]


# DeleteScheduleGroupInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteScheduleInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# EcsParametersTypeDef

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.CapacityProviderStrategyItemTypeDef]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### Group
- **Type**: typing.Optional[str]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.NetworkConfigurationTypeDef]

### PlacementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.PlacementConstraintTypeDef]]

### PlacementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.PlacementStrategyTypeDef]]

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


# EventBridgeParametersTypeDef

### DetailType
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes


# FlexibleTimeWindowTypeDef

### Mode
- **Type**: typing.Literal['FLEXIBLE', 'OFF']
- **Required**: Yes

### MaximumWindowInMinutes
- **Type**: typing.Optional[int]


# GetScheduleGroupInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetScheduleGroupOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetScheduleInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]


# GetScheduleOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.FlexibleTimeWindowTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.TargetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KinesisParametersTypeDef

### PartitionKey
- **Type**: <class 'str'>
- **Required**: Yes


# ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.PaginatorConfigTypeDef]


# ListScheduleGroupsInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListScheduleGroupsOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.scheduler_classes.ScheduleGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSchedulesInputListSchedulesPaginateTypeDef

### GroupName
- **Type**: typing.Optional[str]

### NamePrefix
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.PaginatorConfigTypeDef]


# ListSchedulesInputRequestTypeDef

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


# ListSchedulesOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Schedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.scheduler_classes.ScheduleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.scheduler_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NetworkConfigurationTypeDef

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.AwsVpcConfigurationTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacementConstraintTypeDef

### expression
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['distinctInstance', 'memberOf']]


# PlacementStrategyTypeDef

### field
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['binpack', 'random', 'spread']]


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


# RetryPolicyTypeDef

### MaximumEventAgeInSeconds
- **Type**: typing.Optional[int]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]


# SageMakerPipelineParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SageMakerPipelineParametersTypeDef

### PipelineParameterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.SageMakerPipelineParameterTypeDef]]


# ScheduleGroupSummaryTypeDef

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


# ScheduleSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.TargetSummaryTypeDef]


# SqsParametersTypeDef

### MessageGroupId
- **Type**: typing.Optional[str]


# TagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.scheduler_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# TargetTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.DeadLetterConfigTypeDef]

### EcsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.EcsParametersTypeDef]

### EventBridgeParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.EventBridgeParametersTypeDef]

### Input
- **Type**: typing.Optional[str]

### KinesisParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.KinesisParametersTypeDef]

### RetryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.RetryPolicyTypeDef]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.SageMakerPipelineParametersTypeDef]

### SqsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.scheduler_classes.SqsParametersTypeDef]


# UntagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateScheduleInputRequestTypeDef

### FlexibleTimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.FlexibleTimeWindowTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.TargetTypeDef'>
- **Required**: Yes

### ActionAfterCompletion
- **Type**: typing.Optional[typing.Literal['DELETE', 'NONE']]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### GroupName
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateScheduleOutputTypeDef

### ScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.scheduler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



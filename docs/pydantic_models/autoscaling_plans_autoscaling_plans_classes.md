# Autoscaling Plans Autoscaling Plans Classes

# ApplicationSource

### CloudFormationStackARN
- **Type**: typing.Optional[str]

### TagFilters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.TagFilter, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.TagFilterOutput]]]


# ApplicationSourceOutput

### CloudFormationStackARN
- **Type**: typing.Optional[str]

### TagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.TagFilterOutput]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateScalingPlanRequest

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSource, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSourceOutput]
- **Required**: Yes

### ScalingInstructions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ScalingInstruction, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ScalingInstructionOutput]]
- **Required**: Yes


# CreateScalingPlanResponse

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ResponseMetadata'>
- **Required**: Yes


# CustomizedLoadMetricSpecification

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.MetricDimension]]

### Unit
- **Type**: typing.Optional[str]


# CustomizedLoadMetricSpecificationOutput

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.MetricDimension]]

### Unit
- **Type**: typing.Optional[str]


# CustomizedScalingMetricSpecification

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.MetricDimension]]

### Unit
- **Type**: typing.Optional[str]


# CustomizedScalingMetricSpecificationOutput

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.MetricDimension]]

### Unit
- **Type**: typing.Optional[str]


# Datapoint

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Value
- **Type**: typing.Optional[float]


# DeleteScalingPlanRequest

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeScalingPlanResourcesRequest

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPlanResourcesRequestPaginate

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.PaginatorConfig]


# DescribeScalingPlanResourcesResponse

### ScalingPlanResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ScalingPlanResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPlansRequest

### ScalingPlanNames
- **Type**: typing.Optional[typing.List[str]]

### ScalingPlanVersion
- **Type**: typing.Optional[int]

### ApplicationSources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSource, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSourceOutput]]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPlansRequestPaginate

### ScalingPlanNames
- **Type**: typing.Optional[typing.List[str]]

### ScalingPlanVersion
- **Type**: typing.Optional[int]

### ApplicationSources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSource, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSourceOutput]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.PaginatorConfig]


# DescribeScalingPlansResponse

### ScalingPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ScalingPlan]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetScalingPlanResourceForecastDataRequest

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ServiceNamespace
- **Type**: typing.Literal['autoscaling', 'dynamodb', 'ec2', 'ecs', 'rds']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['autoscaling:autoScalingGroup:DesiredCapacity', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'rds:cluster:ReadReplicaCount']
- **Required**: Yes

### ForecastDataType
- **Type**: typing.Literal['CapacityForecast', 'LoadForecast', 'ScheduledActionMaxCapacity', 'ScheduledActionMinCapacity']
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# GetScalingPlanResourceForecastDataResponse

### Datapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.Datapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ResponseMetadata'>
- **Required**: Yes


# MetricDimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredefinedLoadMetricSpecification

### PredefinedLoadMetricType
- **Type**: typing.Literal['ALBTargetGroupRequestCount', 'ASGTotalCPUUtilization', 'ASGTotalNetworkIn', 'ASGTotalNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredefinedScalingMetricSpecification

### PredefinedScalingMetricType
- **Type**: typing.Literal['ALBRequestCountPerTarget', 'ASGAverageCPUUtilization', 'ASGAverageNetworkIn', 'ASGAverageNetworkOut', 'DynamoDBReadCapacityUtilization', 'DynamoDBWriteCapacityUtilization', 'EC2SpotFleetRequestAverageCPUUtilization', 'EC2SpotFleetRequestAverageNetworkIn', 'EC2SpotFleetRequestAverageNetworkOut', 'ECSServiceAverageCPUUtilization', 'ECSServiceAverageMemoryUtilization', 'RDSReaderAverageCPUUtilization', 'RDSReaderAverageDatabaseConnections']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


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


# ScalingInstruction

### ServiceNamespace
- **Type**: typing.Literal['autoscaling', 'dynamodb', 'ec2', 'ecs', 'rds']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['autoscaling:autoScalingGroup:DesiredCapacity', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'rds:cluster:ReadReplicaCount']
- **Required**: Yes

### MinCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### MaxCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### TargetTrackingConfigurations
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.TargetTrackingConfiguration, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.TargetTrackingConfigurationOutput]]
- **Required**: Yes

### PredefinedLoadMetricSpecification
- **Type**: <class 'NoneType'>

### CustomizedLoadMetricSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.CustomizedLoadMetricSpecification, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.CustomizedLoadMetricSpecificationOutput, NoneType]

### ScheduledActionBufferTime
- **Type**: typing.Optional[int]

### PredictiveScalingMaxCapacityBehavior
- **Type**: typing.Optional[typing.Literal['SetForecastCapacityToMaxCapacity', 'SetMaxCapacityAboveForecastCapacity', 'SetMaxCapacityToForecastCapacity']]

### PredictiveScalingMaxCapacityBuffer
- **Type**: typing.Optional[int]

### PredictiveScalingMode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### ScalingPolicyUpdateBehavior
- **Type**: typing.Optional[typing.Literal['KeepExternalPolicies', 'ReplaceExternalPolicies']]

### DisableDynamicScaling
- **Type**: typing.Optional[bool]


# ScalingInstructionOutput

### ServiceNamespace
- **Type**: typing.Literal['autoscaling', 'dynamodb', 'ec2', 'ecs', 'rds']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['autoscaling:autoScalingGroup:DesiredCapacity', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'rds:cluster:ReadReplicaCount']
- **Required**: Yes

### MinCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### MaxCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### TargetTrackingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.TargetTrackingConfigurationOutput]
- **Required**: Yes

### PredefinedLoadMetricSpecification
- **Type**: <class 'NoneType'>

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.CustomizedLoadMetricSpecificationOutput]

### ScheduledActionBufferTime
- **Type**: typing.Optional[int]

### PredictiveScalingMaxCapacityBehavior
- **Type**: typing.Optional[typing.Literal['SetForecastCapacityToMaxCapacity', 'SetMaxCapacityAboveForecastCapacity', 'SetMaxCapacityToForecastCapacity']]

### PredictiveScalingMaxCapacityBuffer
- **Type**: typing.Optional[int]

### PredictiveScalingMode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### ScalingPolicyUpdateBehavior
- **Type**: typing.Optional[typing.Literal['KeepExternalPolicies', 'ReplaceExternalPolicies']]

### DisableDynamicScaling
- **Type**: typing.Optional[bool]


# ScalingPlan

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationSource
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSourceOutput'>
- **Required**: Yes

### ScalingInstructions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ScalingInstructionOutput]
- **Required**: Yes

### StatusCode
- **Type**: typing.Literal['Active', 'ActiveWithProblems', 'CreationFailed', 'CreationInProgress', 'DeletionFailed', 'DeletionInProgress', 'UpdateFailed', 'UpdateInProgress']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Optional[str]

### StatusStartTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# ScalingPlanResource

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ServiceNamespace
- **Type**: typing.Literal['autoscaling', 'dynamodb', 'ec2', 'ecs', 'rds']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['autoscaling:autoScalingGroup:DesiredCapacity', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'rds:cluster:ReadReplicaCount']
- **Required**: Yes

### ScalingStatusCode
- **Type**: typing.Literal['Active', 'Inactive', 'PartiallyActive']
- **Required**: Yes

### ScalingPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ScalingPolicy]]

### ScalingStatusMessage
- **Type**: typing.Optional[str]


# ScalingPolicy

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['TargetTrackingScaling']
- **Required**: Yes

### TargetTrackingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.TargetTrackingConfigurationOutput]


# TagFilter

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TagFilterOutput

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TargetTrackingConfiguration

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedScalingMetricSpecification
- **Type**: <class 'NoneType'>

### CustomizedScalingMetricSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.CustomizedScalingMetricSpecification, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.CustomizedScalingMetricSpecificationOutput, NoneType]

### DisableScaleIn
- **Type**: typing.Optional[bool]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]


# TargetTrackingConfigurationOutput

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedScalingMetricSpecification
- **Type**: <class 'NoneType'>

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.CustomizedScalingMetricSpecificationOutput]

### DisableScaleIn
- **Type**: typing.Optional[bool]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]


# UpdateScalingPlanRequest

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSource, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ApplicationSourceOutput, NoneType]

### ScalingInstructions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ScalingInstruction, aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_classes.ScalingInstructionOutput]]]



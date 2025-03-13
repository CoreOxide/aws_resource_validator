# Autoscaling Plans Classes

# ApplicationSourceOutputTypeDef

### CloudFormationStackARN
- **Type**: typing.Optional[str]

### TagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.TagFilterOutputTypeDef]]


# ApplicationSourceTypeDef

### CloudFormationStackARN
- **Type**: typing.Optional[str]

### TagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_plans_classes.TagFilterUnionTypeDef]]


# ApplicationSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateScalingPlanRequestTypeDef

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationSource
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans_classes.ApplicationSourceUnionTypeDef'>
- **Required**: Yes

### ScalingInstructions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ScalingInstructionUnionTypeDef]
- **Required**: Yes


# CreateScalingPlanResponseTypeDef

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomizedLoadMetricSpecificationOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.MetricDimensionTypeDef]]

### Unit
- **Type**: typing.Optional[str]


# CustomizedLoadMetricSpecificationTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_plans_classes.MetricDimensionTypeDef]]

### Unit
- **Type**: typing.Optional[str]


# CustomizedLoadMetricSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomizedScalingMetricSpecificationOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.MetricDimensionTypeDef]]

### Unit
- **Type**: typing.Optional[str]


# CustomizedScalingMetricSpecificationTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_plans_classes.MetricDimensionTypeDef]]

### Unit
- **Type**: typing.Optional[str]


# CustomizedScalingMetricSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatapointTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Value
- **Type**: typing.Optional[float]


# DeleteScalingPlanRequestTypeDef

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeScalingPlanResourcesRequestPaginateTypeDef

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.PaginatorConfigTypeDef]


# DescribeScalingPlanResourcesRequestTypeDef

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


# DescribeScalingPlanResourcesResponseTypeDef

### ScalingPlanResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ScalingPlanResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPlansRequestPaginateTypeDef

### ScalingPlanNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ScalingPlanVersion
- **Type**: typing.Optional[int]

### ApplicationSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ApplicationSourceUnionTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.PaginatorConfigTypeDef]


# DescribeScalingPlansRequestTypeDef

### ScalingPlanNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ScalingPlanVersion
- **Type**: typing.Optional[int]

### ApplicationSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ApplicationSourceUnionTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPlansResponseTypeDef

### ScalingPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ScalingPlanTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetScalingPlanResourceForecastDataRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans_classes.TimestampTypeDef'>
- **Required**: Yes


# GetScalingPlanResourceForecastDataResponseTypeDef

### Datapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.DatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricDimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredefinedLoadMetricSpecificationTypeDef

### PredefinedLoadMetricType
- **Type**: typing.Literal['ALBTargetGroupRequestCount', 'ASGTotalCPUUtilization', 'ASGTotalNetworkIn', 'ASGTotalNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredefinedScalingMetricSpecificationTypeDef

### PredefinedScalingMetricType
- **Type**: typing.Literal['ALBRequestCountPerTarget', 'ASGAverageCPUUtilization', 'ASGAverageNetworkIn', 'ASGAverageNetworkOut', 'DynamoDBReadCapacityUtilization', 'DynamoDBWriteCapacityUtilization', 'EC2SpotFleetRequestAverageCPUUtilization', 'EC2SpotFleetRequestAverageNetworkIn', 'EC2SpotFleetRequestAverageNetworkOut', 'ECSServiceAverageCPUUtilization', 'ECSServiceAverageMemoryUtilization', 'RDSReaderAverageCPUUtilization', 'RDSReaderAverageDatabaseConnections']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


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


# ScalingInstructionOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.TargetTrackingConfigurationOutputTypeDef]
- **Required**: Yes

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.PredefinedLoadMetricSpecificationTypeDef]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.CustomizedLoadMetricSpecificationOutputTypeDef]

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


# ScalingInstructionTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_plans_classes.TargetTrackingConfigurationUnionTypeDef]
- **Required**: Yes

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.PredefinedLoadMetricSpecificationTypeDef]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.CustomizedLoadMetricSpecificationUnionTypeDef]

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


# ScalingInstructionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScalingPlanResourceTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ScalingPolicyTypeDef]]

### ScalingStatusMessage
- **Type**: typing.Optional[str]


# ScalingPlanTypeDef

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationSource
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_plans_classes.ApplicationSourceOutputTypeDef'>
- **Required**: Yes

### ScalingInstructions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ScalingInstructionOutputTypeDef]
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


# ScalingPolicyTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['TargetTrackingScaling']
- **Required**: Yes

### TargetTrackingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.TargetTrackingConfigurationOutputTypeDef]


# TagFilterOutputTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TagFilterTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# TagFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetTrackingConfigurationOutputTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.PredefinedScalingMetricSpecificationTypeDef]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.CustomizedScalingMetricSpecificationOutputTypeDef]

### DisableScaleIn
- **Type**: typing.Optional[bool]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]


# TargetTrackingConfigurationTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.PredefinedScalingMetricSpecificationTypeDef]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.CustomizedScalingMetricSpecificationUnionTypeDef]

### DisableScaleIn
- **Type**: typing.Optional[bool]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]


# TargetTrackingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateScalingPlanRequestTypeDef

### ScalingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingPlanVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ApplicationSourceUnionTypeDef]

### ScalingInstructions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_plans_classes.ScalingInstructionUnionTypeDef]]



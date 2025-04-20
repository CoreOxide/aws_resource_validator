# Application Autoscaling Application Autoscaling Classes

# Alarm

### AlarmName
- **Type**: <class 'str'>
- **Required**: Yes

### AlarmARN
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityForecast

### Timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes


# CustomizedMetricSpecification

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.MetricDimension]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingMetricDataQuery]]


# CustomizedMetricSpecificationOutput

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.MetricDimension]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingMetricDataQueryOutput]]


# DeleteScalingPolicyRequest

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes


# DeleteScheduledActionRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes


# DeregisterScalableTargetRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes


# DescribeScalableTargetsRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalableTargetsRequestPaginate

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PaginatorConfig]


# DescribeScalableTargetsResponse

### ScalableTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ScalableTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingActivitiesRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### IncludeNotScaledActivities
- **Type**: typing.Optional[bool]


# DescribeScalingActivitiesRequestPaginate

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### IncludeNotScaledActivities
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PaginatorConfig]


# DescribeScalingActivitiesResponse

### ScalingActivities
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ScalingActivity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPoliciesRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPoliciesRequestPaginate

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PaginatorConfig]


# DescribeScalingPoliciesResponse

### ScalingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ScalingPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScheduledActionsRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ScheduledActionNames
- **Type**: typing.Optional[typing.List[str]]

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScheduledActionsRequestPaginate

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ScheduledActionNames
- **Type**: typing.Optional[typing.List[str]]

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PaginatorConfig]


# DescribeScheduledActionsResponse

### ScheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ScheduledAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPredictiveScalingForecastRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# GetPredictiveScalingForecastResponse

### LoadForecast
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.LoadForecast]
- **Required**: Yes

### CapacityForecast
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.CapacityForecast'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# LoadForecast

### Timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes

### MetricSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricSpecificationOutput'>
- **Required**: Yes


# MetricDimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# NotScaledReason

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### MaxCapacity
- **Type**: typing.Optional[int]

### MinCapacity
- **Type**: typing.Optional[int]

### CurrentCapacity
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredefinedMetricSpecification

### PredefinedMetricType
- **Type**: typing.Literal['ALBRequestCountPerTarget', 'AppStreamAverageCapacityUtilization', 'CassandraReadCapacityUtilization', 'CassandraWriteCapacityUtilization', 'ComprehendInferenceUtilization', 'DynamoDBReadCapacityUtilization', 'DynamoDBWriteCapacityUtilization', 'EC2SpotFleetRequestAverageCPUUtilization', 'EC2SpotFleetRequestAverageNetworkIn', 'EC2SpotFleetRequestAverageNetworkOut', 'ECSServiceAverageCPUUtilization', 'ECSServiceAverageMemoryUtilization', 'ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage', 'ElastiCacheDatabaseMemoryUsageCountedForEvictPercentage', 'ElastiCachePrimaryEngineCPUUtilization', 'ElastiCacheReplicaEngineCPUUtilization', 'KafkaBrokerStorageUtilization', 'LambdaProvisionedConcurrencyUtilization', 'NeptuneReaderAverageCPUUtilization', 'RDSReaderAverageCPUUtilization', 'RDSReaderAverageDatabaseConnections', 'SageMakerInferenceComponentConcurrentRequestsPerCopyHighResolution', 'SageMakerInferenceComponentInvocationsPerCopy', 'SageMakerVariantConcurrentRequestsPerModelHighResolution', 'SageMakerVariantInvocationsPerInstance', 'SageMakerVariantProvisionedConcurrencyUtilization', 'WorkSpacesAverageUserSessionsCapacityUtilization']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingCustomizedMetricSpecification

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricDataQuery]
- **Required**: Yes


# PredictiveScalingCustomizedMetricSpecificationOutput

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricDataQueryOutput]
- **Required**: Yes


# PredictiveScalingMetric

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricDimension]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# PredictiveScalingMetricDataQuery

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricStat]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# PredictiveScalingMetricDataQueryOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricStatOutput]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# PredictiveScalingMetricDimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PredictiveScalingMetricOutput

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricDimension]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# PredictiveScalingMetricSpecification

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricPairSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPredefinedMetricPairSpecification]

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPredefinedScalingMetricSpecification]

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPredefinedLoadMetricSpecification]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingCustomizedMetricSpecification]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingCustomizedMetricSpecification]

### CustomizedCapacityMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingCustomizedMetricSpecification]


# PredictiveScalingMetricSpecificationOutput

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricPairSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPredefinedMetricPairSpecification]

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPredefinedScalingMetricSpecification]

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPredefinedLoadMetricSpecification]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingCustomizedMetricSpecificationOutput]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingCustomizedMetricSpecificationOutput]

### CustomizedCapacityMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingCustomizedMetricSpecificationOutput]


# PredictiveScalingMetricStat

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetric'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# PredictiveScalingMetricStatOutput

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricOutput'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# PredictiveScalingPolicyConfiguration

### MetricSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricSpecification]
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### SchedulingBufferTime
- **Type**: typing.Optional[int]

### MaxCapacityBreachBehavior
- **Type**: typing.Optional[typing.Literal['HonorMaxCapacity', 'IncreaseMaxCapacity']]

### MaxCapacityBuffer
- **Type**: typing.Optional[int]


# PredictiveScalingPolicyConfigurationOutput

### MetricSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingMetricSpecificationOutput]
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### SchedulingBufferTime
- **Type**: typing.Optional[int]

### MaxCapacityBreachBehavior
- **Type**: typing.Optional[typing.Literal['HonorMaxCapacity', 'IncreaseMaxCapacity']]

### MaxCapacityBuffer
- **Type**: typing.Optional[int]


# PredictiveScalingPredefinedLoadMetricSpecification

### PredefinedMetricType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingPredefinedMetricPairSpecification

### PredefinedMetricType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingPredefinedScalingMetricSpecification

### PredefinedMetricType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PutScalingPolicyRequest

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes

### PolicyType
- **Type**: typing.Optional[typing.Literal['PredictiveScaling', 'StepScaling', 'TargetTrackingScaling']]

### StepScalingPolicyConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.StepScalingPolicyConfiguration, aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.StepScalingPolicyConfigurationOutput, NoneType]

### TargetTrackingScalingPolicyConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingScalingPolicyConfiguration, aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingScalingPolicyConfigurationOutput, NoneType]

### PredictiveScalingPolicyConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPolicyConfiguration, aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPolicyConfigurationOutput, NoneType]


# PutScalingPolicyResponse

### PolicyARN
- **Type**: <class 'str'>
- **Required**: Yes

### Alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.Alarm]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# PutScheduledActionRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes

### Schedule
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ScalableTargetAction
- **Type**: <class 'NoneType'>


# RegisterScalableTargetRequest

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes

### MinCapacity
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[int]

### RoleARN
- **Type**: typing.Optional[str]

### SuspendedState
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RegisterScalableTargetResponse

### ScalableTargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


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


# ScalableTarget

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes

### MinCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### MaxCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PredictedCapacity
- **Type**: typing.Optional[int]

### SuspendedState
- **Type**: <class 'NoneType'>

### ScalableTargetARN
- **Type**: typing.Optional[str]


# ScalableTargetAction

### MinCapacity
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[int]


# ScalingActivity

### ActivityId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Cause
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StatusCode
- **Type**: typing.Literal['Failed', 'InProgress', 'Overridden', 'Pending', 'Successful', 'Unfulfilled']
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]

### Details
- **Type**: typing.Optional[str]

### NotScaledReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.NotScaledReason]]


# ScalingPolicy

### PolicyARN
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['PredictiveScaling', 'StepScaling', 'TargetTrackingScaling']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StepScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.StepScalingPolicyConfigurationOutput]

### TargetTrackingScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingScalingPolicyConfigurationOutput]

### PredictiveScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.PredictiveScalingPolicyConfigurationOutput]

### Alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.Alarm]]


# ScheduledAction

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActionARN
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### Schedule
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Timezone
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### ScalableTargetAction
- **Type**: <class 'NoneType'>


# StepAdjustment

### ScalingAdjustment
- **Type**: <class 'int'>
- **Required**: Yes

### MetricIntervalLowerBound
- **Type**: typing.Optional[float]

### MetricIntervalUpperBound
- **Type**: typing.Optional[float]


# StepScalingPolicyConfiguration

### AdjustmentType
- **Type**: typing.Optional[typing.Literal['ChangeInCapacity', 'ExactCapacity', 'PercentChangeInCapacity']]

### StepAdjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.StepAdjustment]]

### MinAdjustmentMagnitude
- **Type**: typing.Optional[int]

### Cooldown
- **Type**: typing.Optional[int]

### MetricAggregationType
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum']]


# StepScalingPolicyConfigurationOutput

### AdjustmentType
- **Type**: typing.Optional[typing.Literal['ChangeInCapacity', 'ExactCapacity', 'PercentChangeInCapacity']]

### StepAdjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.StepAdjustment]]

### MinAdjustmentMagnitude
- **Type**: typing.Optional[int]

### Cooldown
- **Type**: typing.Optional[int]

### MetricAggregationType
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum']]


# SuspendedState

### DynamicScalingInSuspended
- **Type**: typing.Optional[bool]

### DynamicScalingOutSuspended
- **Type**: typing.Optional[bool]

### ScheduledScalingSuspended
- **Type**: typing.Optional[bool]


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TargetTrackingMetric

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingMetricDimension]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# TargetTrackingMetricDataQuery

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingMetricStat]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDataQueryOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingMetricStatOutput]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetTrackingMetricOutput

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingMetricDimension]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# TargetTrackingMetricStat

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingMetric'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# TargetTrackingMetricStatOutput

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.TargetTrackingMetricOutput'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# TargetTrackingScalingPolicyConfiguration

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: <class 'NoneType'>

### CustomizedMetricSpecification
- **Type**: <class 'NoneType'>

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# TargetTrackingScalingPolicyConfigurationOutput

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: <class 'NoneType'>

### CustomizedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_classes.CustomizedMetricSpecificationOutput]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes



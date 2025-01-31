# Application Autoscaling Classes

# AlarmTypeDef

### AlarmName
- **Type**: <class 'str'>
- **Required**: Yes

### AlarmARN
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomizedMetricSpecificationExtraOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.MetricDimensionTypeDef]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricDataQueryExtraOutputTypeDef]]


# CustomizedMetricSpecificationOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.MetricDimensionTypeDef]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricDataQueryOutputTypeDef]]


# CustomizedMetricSpecificationTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_autoscaling_classes.MetricDimensionTypeDef]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricDataQueryTypeDef]]


# DeleteScalingPolicyRequestRequestTypeDef

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


# DeleteScheduledActionRequestRequestTypeDef

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


# DeregisterScalableTargetRequestRequestTypeDef

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ScalableDimension
- **Type**: typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']
- **Required**: Yes


# DescribeScalableTargetsRequestDescribeScalableTargetsPaginateTypeDef

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.PaginatorConfigTypeDef]


# DescribeScalableTargetsRequestRequestTypeDef

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalableTargetsResponseTypeDef

### ScalableTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.ScalableTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingActivitiesRequestDescribeScalingActivitiesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.PaginatorConfigTypeDef]


# DescribeScalingActivitiesRequestRequestTypeDef

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


# DescribeScalingActivitiesResponseTypeDef

### ScalingActivities
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.ScalingActivityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPoliciesRequestDescribeScalingPoliciesPaginateTypeDef

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.PaginatorConfigTypeDef]


# DescribeScalingPoliciesRequestRequestTypeDef

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingPoliciesResponseTypeDef

### ScalingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.ScalingPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScheduledActionsRequestDescribeScheduledActionsPaginateTypeDef

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ScheduledActionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.PaginatorConfigTypeDef]


# DescribeScheduledActionsRequestRequestTypeDef

### ServiceNamespace
- **Type**: typing.Literal['appstream', 'cassandra', 'comprehend', 'custom-resource', 'dynamodb', 'ec2', 'ecs', 'elasticache', 'elasticmapreduce', 'kafka', 'lambda', 'neptune', 'rds', 'sagemaker', 'workspaces']
- **Required**: Yes

### ScheduledActionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceId
- **Type**: typing.Optional[str]

### ScalableDimension
- **Type**: typing.Optional[typing.Literal['appstream:fleet:DesiredCapacity', 'cassandra:table:ReadCapacityUnits', 'cassandra:table:WriteCapacityUnits', 'comprehend:document-classifier-endpoint:DesiredInferenceUnits', 'comprehend:entity-recognizer-endpoint:DesiredInferenceUnits', 'custom-resource:ResourceType:Property', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'ec2:spot-fleet-request:TargetCapacity', 'ecs:service:DesiredCount', 'elasticache:replication-group:NodeGroups', 'elasticache:replication-group:Replicas', 'elasticmapreduce:instancegroup:InstanceCount', 'kafka:broker-storage:VolumeSize', 'lambda:function:ProvisionedConcurrency', 'neptune:cluster:ReadReplicaCount', 'rds:cluster:ReadReplicaCount', 'sagemaker:inference-component:DesiredCopyCount', 'sagemaker:variant:DesiredInstanceCount', 'sagemaker:variant:DesiredProvisionedConcurrency', 'workspaces:workspacespool:DesiredUserSessions']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScheduledActionsResponseTypeDef

### ScheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.ScheduledActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricDimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# NotScaledReasonTypeDef

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### MaxCapacity
- **Type**: typing.Optional[int]

### MinCapacity
- **Type**: typing.Optional[int]

### CurrentCapacity
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredefinedMetricSpecificationTypeDef

### PredefinedMetricType
- **Type**: typing.Literal['ALBRequestCountPerTarget', 'AppStreamAverageCapacityUtilization', 'CassandraReadCapacityUtilization', 'CassandraWriteCapacityUtilization', 'ComprehendInferenceUtilization', 'DynamoDBReadCapacityUtilization', 'DynamoDBWriteCapacityUtilization', 'EC2SpotFleetRequestAverageCPUUtilization', 'EC2SpotFleetRequestAverageNetworkIn', 'EC2SpotFleetRequestAverageNetworkOut', 'ECSServiceAverageCPUUtilization', 'ECSServiceAverageMemoryUtilization', 'ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage', 'ElastiCacheDatabaseMemoryUsageCountedForEvictPercentage', 'ElastiCachePrimaryEngineCPUUtilization', 'ElastiCacheReplicaEngineCPUUtilization', 'KafkaBrokerStorageUtilization', 'LambdaProvisionedConcurrencyUtilization', 'NeptuneReaderAverageCPUUtilization', 'RDSReaderAverageCPUUtilization', 'RDSReaderAverageDatabaseConnections', 'SageMakerInferenceComponentInvocationsPerCopy', 'SageMakerVariantInvocationsPerInstance', 'SageMakerVariantProvisionedConcurrencyUtilization', 'WorkSpacesAverageUserSessionsCapacityUtilization']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PutScalingPolicyRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['StepScaling', 'TargetTrackingScaling']]

### StepScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.StepScalingPolicyConfigurationTypeDef]

### TargetTrackingScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingScalingPolicyConfigurationTypeDef]


# PutScalingPolicyResponseTypeDef

### PolicyARN
- **Type**: <class 'str'>
- **Required**: Yes

### Alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.AlarmTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutScheduledActionRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.ScalableTargetActionTypeDef]


# RegisterScalableTargetRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.SuspendedStateTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterScalableTargetResponseTypeDef

### ScalableTargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ScalableTargetActionTypeDef

### MinCapacity
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[int]


# ScalableTargetTypeDef

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

### SuspendedState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.SuspendedStateTypeDef]

### ScalableTargetARN
- **Type**: typing.Optional[str]


# ScalingActivityTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.NotScaledReasonTypeDef]]


# ScalingPolicyTypeDef

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
- **Type**: typing.Literal['StepScaling', 'TargetTrackingScaling']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StepScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.StepScalingPolicyConfigurationOutputTypeDef]

### TargetTrackingScalingPolicyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingScalingPolicyConfigurationOutputTypeDef]

### Alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.AlarmTypeDef]]


# ScheduledActionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.ScalableTargetActionTypeDef]


# StepAdjustmentTypeDef

### ScalingAdjustment
- **Type**: <class 'int'>
- **Required**: Yes

### MetricIntervalLowerBound
- **Type**: typing.Optional[float]

### MetricIntervalUpperBound
- **Type**: typing.Optional[float]


# StepScalingPolicyConfigurationExtraOutputTypeDef

### AdjustmentType
- **Type**: typing.Optional[typing.Literal['ChangeInCapacity', 'ExactCapacity', 'PercentChangeInCapacity']]

### StepAdjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.StepAdjustmentTypeDef]]

### MinAdjustmentMagnitude
- **Type**: typing.Optional[int]

### Cooldown
- **Type**: typing.Optional[int]

### MetricAggregationType
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum']]


# StepScalingPolicyConfigurationOutputTypeDef

### AdjustmentType
- **Type**: typing.Optional[typing.Literal['ChangeInCapacity', 'ExactCapacity', 'PercentChangeInCapacity']]

### StepAdjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.StepAdjustmentTypeDef]]

### MinAdjustmentMagnitude
- **Type**: typing.Optional[int]

### Cooldown
- **Type**: typing.Optional[int]

### MetricAggregationType
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum']]


# StepScalingPolicyConfigurationTypeDef

### AdjustmentType
- **Type**: typing.Optional[typing.Literal['ChangeInCapacity', 'ExactCapacity', 'PercentChangeInCapacity']]

### StepAdjustments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_autoscaling_classes.StepAdjustmentTypeDef]]

### MinAdjustmentMagnitude
- **Type**: typing.Optional[int]

### Cooldown
- **Type**: typing.Optional[int]

### MetricAggregationType
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum']]


# SuspendedStateTypeDef

### DynamicScalingInSuspended
- **Type**: typing.Optional[bool]

### DynamicScalingOutSuspended
- **Type**: typing.Optional[bool]

### ScheduledScalingSuspended
- **Type**: typing.Optional[bool]


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetTrackingMetricDataQueryExtraOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricStatExtraOutputTypeDef]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDataQueryOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricStatOutputTypeDef]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDataQueryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricStatTypeDef]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetTrackingMetricExtraOutputTypeDef

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricDimensionTypeDef]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# TargetTrackingMetricOutputTypeDef

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricDimensionTypeDef]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# TargetTrackingMetricStatExtraOutputTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricExtraOutputTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# TargetTrackingMetricStatOutputTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricOutputTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# TargetTrackingMetricStatTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# TargetTrackingMetricTypeDef

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_autoscaling_classes.TargetTrackingMetricDimensionTypeDef]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# TargetTrackingScalingPolicyConfigurationExtraOutputTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.PredefinedMetricSpecificationTypeDef]

### CustomizedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.CustomizedMetricSpecificationExtraOutputTypeDef]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# TargetTrackingScalingPolicyConfigurationOutputTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.PredefinedMetricSpecificationTypeDef]

### CustomizedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.CustomizedMetricSpecificationOutputTypeDef]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# TargetTrackingScalingPolicyConfigurationTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.PredefinedMetricSpecificationTypeDef]

### CustomizedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_autoscaling_classes.CustomizedMetricSpecificationTypeDef]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes



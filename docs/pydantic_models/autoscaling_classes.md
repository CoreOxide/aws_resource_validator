# Pydantic Models in autoscaling_classes

# AcceleratorCountRequestTypeDef

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# AcceleratorTotalMemoryMiBRequestTypeDef

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# ActivitiesTypeTypeDef

### Activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.ActivityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ActivityTypeDef

### ActivityId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Cause
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StatusCode
- **Type**: typing.Literal['Cancelled', 'Failed', 'InProgress', 'MidLifecycleAction', 'PendingSpotBidPlacement', 'PreInService', 'Successful', 'WaitingForConnectionDraining', 'WaitingForELBConnectionDraining', 'WaitingForInstanceId', 'WaitingForInstanceWarmup', 'WaitingForSpotInstanceId', 'WaitingForSpotInstanceRequestId']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]

### Progress
- **Type**: typing.Optional[int]

### Details
- **Type**: typing.Optional[str]

### AutoScalingGroupState
- **Type**: typing.Optional[str]

### AutoScalingGroupARN
- **Type**: typing.Optional[str]


# ActivityTypeTypeDef

### Activity
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ActivityTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdjustmentTypeTypeDef

### AdjustmentType
- **Type**: typing.Optional[str]


# AlarmSpecificationOutputTypeDef

### Alarms
- **Type**: typing.Optional[typing.List[str]]


# AlarmSpecificationTypeDef

### Alarms
- **Type**: typing.Optional[typing.Sequence[str]]


# AlarmTypeDef

### AlarmName
- **Type**: typing.Optional[str]

### AlarmARN
- **Type**: typing.Optional[str]


# AttachInstancesQueryRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# AttachLoadBalancerTargetGroupsTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupARNs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AttachLoadBalancersTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AttachTrafficSourcesTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficSources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.TrafficSourceIdentifierTypeDef]
- **Required**: Yes


# AutoScalingGroupNamesTypeDescribeAutoScalingGroupsPaginateTypeDef

### AutoScalingGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# AutoScalingGroupNamesTypeRequestTypeDef

### AutoScalingGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.FilterTypeDef]]


# AutoScalingGroupTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MinSize
- **Type**: <class 'int'>
- **Required**: Yes

### MaxSize
- **Type**: <class 'int'>
- **Required**: Yes

### DesiredCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultCooldown
- **Type**: <class 'int'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### HealthCheckType
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AutoScalingGroupARN
- **Type**: typing.Optional[str]

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MixedInstancesPolicyOutputTypeDef]

### PredictedCapacity
- **Type**: typing.Optional[int]

### LoadBalancerNames
- **Type**: typing.Optional[typing.List[str]]

### TargetGroupARNs
- **Type**: typing.Optional[typing.List[str]]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceTypeDef]]

### SuspendedProcesses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.SuspendedProcessTypeDef]]

### PlacementGroup
- **Type**: typing.Optional[str]

### VPCZoneIdentifier
- **Type**: typing.Optional[str]

### EnabledMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.EnabledMetricTypeDef]]

### Status
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.TagDescriptionTypeDef]]

### TerminationPolicies
- **Type**: typing.Optional[typing.List[str]]

### NewInstancesProtectedFromScaleIn
- **Type**: typing.Optional[bool]

### ServiceLinkedRoleARN
- **Type**: typing.Optional[str]

### MaxInstanceLifetime
- **Type**: typing.Optional[int]

### CapacityRebalance
- **Type**: typing.Optional[bool]

### WarmPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.WarmPoolConfigurationTypeDef]

### WarmPoolSize
- **Type**: typing.Optional[int]

### Context
- **Type**: typing.Optional[str]

### DesiredCapacityType
- **Type**: typing.Optional[str]

### DefaultInstanceWarmup
- **Type**: typing.Optional[int]

### TrafficSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.TrafficSourceIdentifierTypeDef]]

### InstanceMaintenancePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceMaintenancePolicyTypeDef]


# AutoScalingGroupsTypeTypeDef

### AutoScalingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.AutoScalingGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AutoScalingInstanceDetailsTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleState
- **Type**: <class 'str'>
- **Required**: Yes

### HealthStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedFromScaleIn
- **Type**: <class 'bool'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[str]

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### WeightedCapacity
- **Type**: typing.Optional[str]


# AutoScalingInstancesTypeTypeDef

### AutoScalingInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.AutoScalingInstanceDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaselineEbsBandwidthMbpsRequestTypeDef

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# BatchDeleteScheduledActionAnswerTypeDef

### FailedScheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.FailedScheduledUpdateGroupActionRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteScheduledActionTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActionNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchPutScheduledUpdateGroupActionAnswerTypeDef

### FailedScheduledUpdateGroupActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.FailedScheduledUpdateGroupActionRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutScheduledUpdateGroupActionTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledUpdateGroupActions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.ScheduledUpdateGroupActionRequestTypeDef]
- **Required**: Yes


# BlockDeviceMappingTypeDef

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### VirtualName
- **Type**: typing.Optional[str]

### Ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.EbsTypeDef]

### NoDevice
- **Type**: typing.Optional[bool]


# CancelInstanceRefreshAnswerTypeDef

### InstanceRefreshId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelInstanceRefreshTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CapacityForecastTypeDef

### Timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes


# CompleteLifecycleActionTypeRequestTypeDef

### LifecycleHookName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleActionResult
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleActionToken
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]


# CreateAutoScalingGroupTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MinSize
- **Type**: <class 'int'>
- **Required**: Yes

### MaxSize
- **Type**: <class 'int'>
- **Required**: Yes

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MixedInstancesPolicyTypeDef]

### InstanceId
- **Type**: typing.Optional[str]

### DesiredCapacity
- **Type**: typing.Optional[int]

### DefaultCooldown
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### LoadBalancerNames
- **Type**: typing.Optional[typing.Sequence[str]]

### TargetGroupARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### PlacementGroup
- **Type**: typing.Optional[str]

### VPCZoneIdentifier
- **Type**: typing.Optional[str]

### TerminationPolicies
- **Type**: typing.Optional[typing.Sequence[str]]

### NewInstancesProtectedFromScaleIn
- **Type**: typing.Optional[bool]

### CapacityRebalance
- **Type**: typing.Optional[bool]

### LifecycleHookSpecificationList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.LifecycleHookSpecificationTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.TagTypeDef]]

### ServiceLinkedRoleARN
- **Type**: typing.Optional[str]

### MaxInstanceLifetime
- **Type**: typing.Optional[int]

### Context
- **Type**: typing.Optional[str]

### DesiredCapacityType
- **Type**: typing.Optional[str]

### DefaultInstanceWarmup
- **Type**: typing.Optional[int]

### TrafficSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.TrafficSourceIdentifierTypeDef]]

### InstanceMaintenancePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceMaintenancePolicyTypeDef]


# CreateLaunchConfigurationTypeRequestTypeDef

### LaunchConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### ClassicLinkVPCId
- **Type**: typing.Optional[str]

### ClassicLinkVPCSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### UserData
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### RamdiskId
- **Type**: typing.Optional[str]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.BlockDeviceMappingTypeDef]]

### InstanceMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceMonitoringTypeDef]

### SpotPrice
- **Type**: typing.Optional[str]

### IamInstanceProfile
- **Type**: typing.Optional[str]

### EbsOptimized
- **Type**: typing.Optional[bool]

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### PlacementTenancy
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceMetadataOptionsTypeDef]


# CreateOrUpdateTagsTypeRequestTypeDef

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.TagTypeDef]
- **Required**: Yes


# CustomizedMetricSpecificationExtraOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDimensionTypeDef]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.TargetTrackingMetricDataQueryExtraOutputTypeDef]]


# CustomizedMetricSpecificationOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDimensionTypeDef]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.TargetTrackingMetricDataQueryOutputTypeDef]]


# CustomizedMetricSpecificationTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDimensionTypeDef]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.TargetTrackingMetricDataQueryTypeDef]]


# DeleteAutoScalingGroupTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DeleteLifecycleHookTypeRequestTypeDef

### LifecycleHookName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotificationConfigurationTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TopicARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyTypeRequestTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: typing.Optional[str]


# DeleteScheduledActionTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsTypeRequestTypeDef

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.TagTypeDef]
- **Required**: Yes


# DeleteWarmPoolTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DescribeAccountLimitsAnswerTypeDef

### MaxNumberOfAutoScalingGroups
- **Type**: <class 'int'>
- **Required**: Yes

### MaxNumberOfLaunchConfigurations
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfAutoScalingGroups
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfLaunchConfigurations
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAdjustmentTypesAnswerTypeDef

### AdjustmentTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.AdjustmentTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAutoScalingInstancesTypeDescribeAutoScalingInstancesPaginateTypeDef

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribeAutoScalingInstancesTypeRequestTypeDef

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAutoScalingNotificationTypesAnswerTypeDef

### AutoScalingNotificationTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInstanceRefreshesAnswerTypeDef

### InstanceRefreshes
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceRefreshTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceRefreshesTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceRefreshIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeLifecycleHookTypesAnswerTypeDef

### LifecycleHookTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLifecycleHooksAnswerTypeDef

### LifecycleHooks
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.LifecycleHookTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLifecycleHooksTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleHookNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeLoadBalancerTargetGroupsRequestDescribeLoadBalancerTargetGroupsPaginateTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribeLoadBalancerTargetGroupsRequestRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeLoadBalancerTargetGroupsResponseTypeDef

### LoadBalancerTargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.LoadBalancerTargetGroupStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeLoadBalancersRequestDescribeLoadBalancersPaginateTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribeLoadBalancersRequestRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeLoadBalancersResponseTypeDef

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.LoadBalancerStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMetricCollectionTypesAnswerTypeDef

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricCollectionTypeTypeDef]
- **Required**: Yes

### Granularities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricGranularityTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNotificationConfigurationsAnswerTypeDef

### NotificationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.NotificationConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeNotificationConfigurationsTypeDescribeNotificationConfigurationsPaginateTypeDef

### AutoScalingGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribeNotificationConfigurationsTypeRequestTypeDef

### AutoScalingGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribePoliciesTypeDescribePoliciesPaginateTypeDef

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PolicyTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribePoliciesTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PolicyTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeScalingActivitiesTypeDescribeScalingActivitiesPaginateTypeDef

### ActivityIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### IncludeDeletedGroups
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribeScalingActivitiesTypeRequestTypeDef

### ActivityIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### IncludeDeletedGroups
- **Type**: typing.Optional[bool]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScheduledActionsTypeDescribeScheduledActionsPaginateTypeDef

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### ScheduledActionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribeScheduledActionsTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### ScheduledActionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeTagsTypeDescribeTagsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribeTagsTypeRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.FilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeTerminationPolicyTypesAnswerTypeDef

### TerminationPolicyTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrafficSourcesRequestRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficSourceType
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeTrafficSourcesResponseTypeDef

### TrafficSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.TrafficSourceStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWarmPoolAnswerTypeDef

### WarmPoolConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.WarmPoolConfigurationTypeDef'>
- **Required**: Yes

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWarmPoolTypeDescribeWarmPoolPaginateTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# DescribeWarmPoolTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DesiredConfigurationOutputTypeDef

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MixedInstancesPolicyOutputTypeDef]


# DesiredConfigurationTypeDef

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MixedInstancesPolicyTypeDef]


# DetachInstancesAnswerTypeDef

### Activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.ActivityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachInstancesQueryRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ShouldDecrementDesiredCapacity
- **Type**: <class 'bool'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DetachLoadBalancerTargetGroupsTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupARNs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DetachLoadBalancersTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DetachTrafficSourcesTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficSources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.TrafficSourceIdentifierTypeDef]
- **Required**: Yes


# DisableMetricsCollectionQueryRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Optional[typing.Sequence[str]]


# EbsTypeDef

### SnapshotId
- **Type**: typing.Optional[str]

### VolumeSize
- **Type**: typing.Optional[int]

### VolumeType
- **Type**: typing.Optional[str]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Iops
- **Type**: typing.Optional[int]

### Encrypted
- **Type**: typing.Optional[bool]

### Throughput
- **Type**: typing.Optional[int]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableMetricsCollectionQueryRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Granularity
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Optional[typing.Sequence[str]]


# EnabledMetricTypeDef

### Metric
- **Type**: typing.Optional[str]

### Granularity
- **Type**: typing.Optional[str]


# EnterStandbyAnswerTypeDef

### Activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.ActivityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnterStandbyQueryRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ShouldDecrementDesiredCapacity
- **Type**: <class 'bool'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ExecutePolicyTypeRequestTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### HonorCooldown
- **Type**: typing.Optional[bool]

### MetricValue
- **Type**: typing.Optional[float]

### BreachThreshold
- **Type**: typing.Optional[float]


# ExitStandbyAnswerTypeDef

### Activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.ActivityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExitStandbyQueryRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# FailedScheduledUpdateGroupActionRequestTypeDef

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FilterTypeDef

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetPredictiveScalingForecastAnswerTypeDef

### LoadForecast
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.LoadForecastTypeDef]
- **Required**: Yes

### CapacityForecast
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.CapacityForecastTypeDef'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPredictiveScalingForecastTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
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


# InstanceMaintenancePolicyTypeDef

### MinHealthyPercentage
- **Type**: typing.Optional[int]

### MaxHealthyPercentage
- **Type**: typing.Optional[int]


# InstanceMetadataOptionsTypeDef

### HttpTokens
- **Type**: typing.Optional[typing.Literal['optional', 'required']]

### HttpPutResponseHopLimit
- **Type**: typing.Optional[int]

### HttpEndpoint
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]


# InstanceMonitoringTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# InstanceRefreshLivePoolProgressTypeDef

### PercentageComplete
- **Type**: typing.Optional[int]

### InstancesToUpdate
- **Type**: typing.Optional[int]


# InstanceRefreshProgressDetailsTypeDef

### LivePoolProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceRefreshLivePoolProgressTypeDef]

### WarmPoolProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceRefreshWarmPoolProgressTypeDef]


# InstanceRefreshTypeDef

### InstanceRefreshId
- **Type**: typing.Optional[str]

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Failed', 'InProgress', 'Pending', 'RollbackFailed', 'RollbackInProgress', 'RollbackSuccessful', 'Successful']]

### StatusReason
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### PercentageComplete
- **Type**: typing.Optional[int]

### InstancesToUpdate
- **Type**: typing.Optional[int]

### ProgressDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceRefreshProgressDetailsTypeDef]

### Preferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.RefreshPreferencesOutputTypeDef]

### DesiredConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.DesiredConfigurationOutputTypeDef]

### RollbackDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.RollbackDetailsTypeDef]


# InstanceRefreshWarmPoolProgressTypeDef

### PercentageComplete
- **Type**: typing.Optional[int]

### InstancesToUpdate
- **Type**: typing.Optional[int]


# InstanceRequirementsExtraOutputTypeDef

### VCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.VCpuCountRequestTypeDef'>
- **Required**: Yes

### MemoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MemoryMiBRequestTypeDef'>
- **Required**: Yes

### CpuManufacturers
- **Type**: typing.Optional[typing.List[typing.Literal['amazon-web-services', 'amd', 'intel']]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MemoryGiBPerVCpuRequestTypeDef]

### ExcludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### InstanceGenerations
- **Type**: typing.Optional[typing.List[typing.Literal['current', 'previous']]]

### SpotMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### MaxSpotPriceAsPercentageOfOptimalOnDemandPrice
- **Type**: typing.Optional[int]

### OnDemandMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### BareMetal
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### BurstablePerformance
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### RequireHibernateSupport
- **Type**: typing.Optional[bool]

### NetworkInterfaceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.NetworkInterfaceCountRequestTypeDef]

### LocalStorage
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### LocalStorageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['hdd', 'ssd']]]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.TotalLocalStorageGBRequestTypeDef]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.BaselineEbsBandwidthMbpsRequestTypeDef]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['fpga', 'gpu', 'inference']]]

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.AcceleratorCountRequestTypeDef]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.List[typing.Literal['amazon-web-services', 'amd', 'nvidia', 'xilinx']]]

### AcceleratorNames
- **Type**: typing.Optional[typing.List[typing.Literal['a100', 'k80', 'm60', 'radeon-pro-v520', 't4', 'v100', 'vu9p']]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.AcceleratorTotalMemoryMiBRequestTypeDef]

### NetworkBandwidthGbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.NetworkBandwidthGbpsRequestTypeDef]

### AllowedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]


# InstanceRequirementsOutputTypeDef

### VCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.VCpuCountRequestTypeDef'>
- **Required**: Yes

### MemoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MemoryMiBRequestTypeDef'>
- **Required**: Yes

### CpuManufacturers
- **Type**: typing.Optional[typing.List[typing.Literal['amazon-web-services', 'amd', 'intel']]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MemoryGiBPerVCpuRequestTypeDef]

### ExcludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### InstanceGenerations
- **Type**: typing.Optional[typing.List[typing.Literal['current', 'previous']]]

### SpotMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### MaxSpotPriceAsPercentageOfOptimalOnDemandPrice
- **Type**: typing.Optional[int]

### OnDemandMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### BareMetal
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### BurstablePerformance
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### RequireHibernateSupport
- **Type**: typing.Optional[bool]

### NetworkInterfaceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.NetworkInterfaceCountRequestTypeDef]

### LocalStorage
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### LocalStorageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['hdd', 'ssd']]]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.TotalLocalStorageGBRequestTypeDef]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.BaselineEbsBandwidthMbpsRequestTypeDef]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['fpga', 'gpu', 'inference']]]

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.AcceleratorCountRequestTypeDef]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.List[typing.Literal['amazon-web-services', 'amd', 'nvidia', 'xilinx']]]

### AcceleratorNames
- **Type**: typing.Optional[typing.List[typing.Literal['a100', 'k80', 'm60', 'radeon-pro-v520', 't4', 'v100', 'vu9p']]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.AcceleratorTotalMemoryMiBRequestTypeDef]

### NetworkBandwidthGbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.NetworkBandwidthGbpsRequestTypeDef]

### AllowedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]


# InstanceRequirementsTypeDef

### VCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.VCpuCountRequestTypeDef'>
- **Required**: Yes

### MemoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MemoryMiBRequestTypeDef'>
- **Required**: Yes

### CpuManufacturers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['amazon-web-services', 'amd', 'intel']]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MemoryGiBPerVCpuRequestTypeDef]

### ExcludedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### InstanceGenerations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['current', 'previous']]]

### SpotMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### MaxSpotPriceAsPercentageOfOptimalOnDemandPrice
- **Type**: typing.Optional[int]

### OnDemandMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### BareMetal
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### BurstablePerformance
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### RequireHibernateSupport
- **Type**: typing.Optional[bool]

### NetworkInterfaceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.NetworkInterfaceCountRequestTypeDef]

### LocalStorage
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### LocalStorageTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['hdd', 'ssd']]]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.TotalLocalStorageGBRequestTypeDef]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.BaselineEbsBandwidthMbpsRequestTypeDef]

### AcceleratorTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['fpga', 'gpu', 'inference']]]

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.AcceleratorCountRequestTypeDef]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['amazon-web-services', 'amd', 'nvidia', 'xilinx']]]

### AcceleratorNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['a100', 'k80', 'm60', 'radeon-pro-v520', 't4', 'v100', 'vu9p']]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.AcceleratorTotalMemoryMiBRequestTypeDef]

### NetworkBandwidthGbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.NetworkBandwidthGbpsRequestTypeDef]

### AllowedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# InstanceReusePolicyTypeDef

### ReuseOnScaleIn
- **Type**: typing.Optional[bool]


# InstanceTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleState
- **Type**: typing.Literal['Detached', 'Detaching', 'EnteringStandby', 'InService', 'Pending', 'Pending:Proceed', 'Pending:Wait', 'Quarantined', 'Standby', 'Terminated', 'Terminating', 'Terminating:Proceed', 'Terminating:Wait', 'Warmed:Hibernated', 'Warmed:Pending', 'Warmed:Pending:Proceed', 'Warmed:Pending:Wait', 'Warmed:Running', 'Warmed:Stopped', 'Warmed:Terminated', 'Warmed:Terminating', 'Warmed:Terminating:Proceed', 'Warmed:Terminating:Wait']
- **Required**: Yes

### HealthStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedFromScaleIn
- **Type**: <class 'bool'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[str]

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### WeightedCapacity
- **Type**: typing.Optional[str]


# InstancesDistributionTypeDef

### OnDemandAllocationStrategy
- **Type**: typing.Optional[str]

### OnDemandBaseCapacity
- **Type**: typing.Optional[int]

### OnDemandPercentageAboveBaseCapacity
- **Type**: typing.Optional[int]

### SpotAllocationStrategy
- **Type**: typing.Optional[str]

### SpotInstancePools
- **Type**: typing.Optional[int]

### SpotMaxPrice
- **Type**: typing.Optional[str]


# LaunchConfigurationNameTypeRequestTypeDef

### LaunchConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# LaunchConfigurationNamesTypeDescribeLaunchConfigurationsPaginateTypeDef

### LaunchConfigurationNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PaginatorConfigTypeDef]


# LaunchConfigurationNamesTypeRequestTypeDef

### LaunchConfigurationNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# LaunchConfigurationTypeDef

### LaunchConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LaunchConfigurationARN
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### ClassicLinkVPCId
- **Type**: typing.Optional[str]

### ClassicLinkVPCSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### UserData
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### RamdiskId
- **Type**: typing.Optional[str]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.BlockDeviceMappingTypeDef]]

### InstanceMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceMonitoringTypeDef]

### SpotPrice
- **Type**: typing.Optional[str]

### IamInstanceProfile
- **Type**: typing.Optional[str]

### EbsOptimized
- **Type**: typing.Optional[bool]

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### PlacementTenancy
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceMetadataOptionsTypeDef]


# LaunchConfigurationsTypeTypeDef

### LaunchConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LaunchTemplateExtraOutputTypeDef

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateOverridesExtraOutputTypeDef]]


# LaunchTemplateOutputTypeDef

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateOverridesOutputTypeDef]]


# LaunchTemplateOverridesExtraOutputTypeDef

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[str]

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceRequirementsExtraOutputTypeDef]


# LaunchTemplateOverridesOutputTypeDef

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[str]

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceRequirementsOutputTypeDef]


# LaunchTemplateOverridesTypeDef

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[str]

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceRequirementsTypeDef]


# LaunchTemplateSpecificationTypeDef

### LaunchTemplateId
- **Type**: typing.Optional[str]

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# LaunchTemplateTypeDef

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### Overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateOverridesTypeDef]]


# LifecycleHookSpecificationTypeDef

### LifecycleHookName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleTransition
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationMetadata
- **Type**: typing.Optional[str]

### HeartbeatTimeout
- **Type**: typing.Optional[int]

### DefaultResult
- **Type**: typing.Optional[str]

### NotificationTargetARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# LifecycleHookTypeDef

### LifecycleHookName
- **Type**: typing.Optional[str]

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### LifecycleTransition
- **Type**: typing.Optional[str]

### NotificationTargetARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### NotificationMetadata
- **Type**: typing.Optional[str]

### HeartbeatTimeout
- **Type**: typing.Optional[int]

### GlobalTimeout
- **Type**: typing.Optional[int]

### DefaultResult
- **Type**: typing.Optional[str]


# LoadBalancerStateTypeDef

### LoadBalancerName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# LoadBalancerTargetGroupStateTypeDef

### LoadBalancerTargetGroupARN
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# LoadForecastTypeDef

### Timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes

### MetricSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingMetricSpecificationOutputTypeDef'>
- **Required**: Yes


# MemoryGiBPerVCpuRequestTypeDef

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# MemoryMiBRequestTypeDef

### Min
- **Type**: <class 'int'>
- **Required**: Yes

### Max
- **Type**: typing.Optional[int]


# MetricCollectionTypeTypeDef

### Metric
- **Type**: typing.Optional[str]


# MetricDataQueryExtraOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MetricStatExtraOutputTypeDef]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# MetricDataQueryOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MetricStatOutputTypeDef]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# MetricDataQueryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MetricStatTypeDef]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# MetricDimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# MetricExtraOutputTypeDef

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDimensionTypeDef]]


# MetricGranularityTypeTypeDef

### Granularity
- **Type**: typing.Optional[str]


# MetricOutputTypeDef

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDimensionTypeDef]]


# MetricStatExtraOutputTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MetricExtraOutputTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# MetricStatOutputTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MetricOutputTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# MetricStatTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MetricTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# MetricTypeDef

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDimensionTypeDef]]


# MixedInstancesPolicyExtraOutputTypeDef

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateExtraOutputTypeDef]

### InstancesDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstancesDistributionTypeDef]


# MixedInstancesPolicyOutputTypeDef

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateOutputTypeDef]

### InstancesDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstancesDistributionTypeDef]


# MixedInstancesPolicyTypeDef

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateTypeDef]

### InstancesDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstancesDistributionTypeDef]


# NetworkBandwidthGbpsRequestTypeDef

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# NetworkInterfaceCountRequestTypeDef

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# NotificationConfigurationTypeDef

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### TopicARN
- **Type**: typing.Optional[str]

### NotificationType
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PoliciesTypeTypeDef

### ScalingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.ScalingPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PolicyARNTypeTypeDef

### PolicyARN
- **Type**: <class 'str'>
- **Required**: Yes

### Alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.AlarmTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PredefinedMetricSpecificationTypeDef

### PredefinedMetricType
- **Type**: typing.Literal['ALBRequestCountPerTarget', 'ASGAverageCPUUtilization', 'ASGAverageNetworkIn', 'ASGAverageNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingConfigurationExtraOutputTypeDef

### MetricSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingMetricSpecificationExtraOutputTypeDef]
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### SchedulingBufferTime
- **Type**: typing.Optional[int]

### MaxCapacityBreachBehavior
- **Type**: typing.Optional[typing.Literal['HonorMaxCapacity', 'IncreaseMaxCapacity']]

### MaxCapacityBuffer
- **Type**: typing.Optional[int]


# PredictiveScalingConfigurationOutputTypeDef

### MetricSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingMetricSpecificationOutputTypeDef]
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### SchedulingBufferTime
- **Type**: typing.Optional[int]

### MaxCapacityBreachBehavior
- **Type**: typing.Optional[typing.Literal['HonorMaxCapacity', 'IncreaseMaxCapacity']]

### MaxCapacityBuffer
- **Type**: typing.Optional[int]


# PredictiveScalingConfigurationTypeDef

### MetricSpecifications
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingMetricSpecificationTypeDef]
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### SchedulingBufferTime
- **Type**: typing.Optional[int]

### MaxCapacityBreachBehavior
- **Type**: typing.Optional[typing.Literal['HonorMaxCapacity', 'IncreaseMaxCapacity']]

### MaxCapacityBuffer
- **Type**: typing.Optional[int]


# PredictiveScalingCustomizedCapacityMetricExtraOutputTypeDef

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryExtraOutputTypeDef]
- **Required**: Yes


# PredictiveScalingCustomizedCapacityMetricOutputTypeDef

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryOutputTypeDef]
- **Required**: Yes


# PredictiveScalingCustomizedCapacityMetricTypeDef

### MetricDataQueries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryTypeDef]
- **Required**: Yes


# PredictiveScalingCustomizedLoadMetricExtraOutputTypeDef

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryExtraOutputTypeDef]
- **Required**: Yes


# PredictiveScalingCustomizedLoadMetricOutputTypeDef

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryOutputTypeDef]
- **Required**: Yes


# PredictiveScalingCustomizedLoadMetricTypeDef

### MetricDataQueries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryTypeDef]
- **Required**: Yes


# PredictiveScalingCustomizedScalingMetricExtraOutputTypeDef

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryExtraOutputTypeDef]
- **Required**: Yes


# PredictiveScalingCustomizedScalingMetricOutputTypeDef

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryOutputTypeDef]
- **Required**: Yes


# PredictiveScalingCustomizedScalingMetricTypeDef

### MetricDataQueries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.MetricDataQueryTypeDef]
- **Required**: Yes


# PredictiveScalingMetricSpecificationExtraOutputTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricPairSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedMetricPairTypeDef]

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedScalingMetricTypeDef]

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedLoadMetricTypeDef]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedScalingMetricExtraOutputTypeDef]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedLoadMetricExtraOutputTypeDef]

### CustomizedCapacityMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedCapacityMetricExtraOutputTypeDef]


# PredictiveScalingMetricSpecificationOutputTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricPairSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedMetricPairTypeDef]

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedScalingMetricTypeDef]

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedLoadMetricTypeDef]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedScalingMetricOutputTypeDef]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedLoadMetricOutputTypeDef]

### CustomizedCapacityMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedCapacityMetricOutputTypeDef]


# PredictiveScalingMetricSpecificationTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricPairSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedMetricPairTypeDef]

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedScalingMetricTypeDef]

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingPredefinedLoadMetricTypeDef]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedScalingMetricTypeDef]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedLoadMetricTypeDef]

### CustomizedCapacityMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingCustomizedCapacityMetricTypeDef]


# PredictiveScalingPredefinedLoadMetricTypeDef

### PredefinedMetricType
- **Type**: typing.Literal['ALBTargetGroupRequestCount', 'ASGTotalCPUUtilization', 'ASGTotalNetworkIn', 'ASGTotalNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingPredefinedMetricPairTypeDef

### PredefinedMetricType
- **Type**: typing.Literal['ALBRequestCount', 'ASGCPUUtilization', 'ASGNetworkIn', 'ASGNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingPredefinedScalingMetricTypeDef

### PredefinedMetricType
- **Type**: typing.Literal['ALBRequestCountPerTarget', 'ASGAverageCPUUtilization', 'ASGAverageNetworkIn', 'ASGAverageNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# ProcessTypeTypeDef

### ProcessName
- **Type**: <class 'str'>
- **Required**: Yes


# ProcessesTypeTypeDef

### Processes
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.ProcessTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutLifecycleHookTypeRequestTypeDef

### LifecycleHookName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleTransition
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### NotificationTargetARN
- **Type**: typing.Optional[str]

### NotificationMetadata
- **Type**: typing.Optional[str]

### HeartbeatTimeout
- **Type**: typing.Optional[int]

### DefaultResult
- **Type**: typing.Optional[str]


# PutNotificationConfigurationTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TopicARN
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PutScalingPolicyTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Optional[str]

### AdjustmentType
- **Type**: typing.Optional[str]

### MinAdjustmentStep
- **Type**: typing.Optional[int]

### MinAdjustmentMagnitude
- **Type**: typing.Optional[int]

### ScalingAdjustment
- **Type**: typing.Optional[int]

### Cooldown
- **Type**: typing.Optional[int]

### MetricAggregationType
- **Type**: typing.Optional[str]

### StepAdjustments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.autoscaling_classes.StepAdjustmentTypeDef]]

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]

### TargetTrackingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.TargetTrackingConfigurationTypeDef]

### Enabled
- **Type**: typing.Optional[bool]

### PredictiveScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingConfigurationTypeDef]


# PutScheduledUpdateGroupActionTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### Time
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Recurrence
- **Type**: typing.Optional[str]

### MinSize
- **Type**: typing.Optional[int]

### MaxSize
- **Type**: typing.Optional[int]

### DesiredCapacity
- **Type**: typing.Optional[int]

### TimeZone
- **Type**: typing.Optional[str]


# PutWarmPoolTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxGroupPreparedCapacity
- **Type**: typing.Optional[int]

### MinSize
- **Type**: typing.Optional[int]

### PoolState
- **Type**: typing.Optional[typing.Literal['Hibernated', 'Running', 'Stopped']]

### InstanceReusePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceReusePolicyTypeDef]


# RecordLifecycleActionHeartbeatTypeRequestTypeDef

### LifecycleHookName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleActionToken
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]


# RefreshPreferencesOutputTypeDef

### MinHealthyPercentage
- **Type**: typing.Optional[int]

### InstanceWarmup
- **Type**: typing.Optional[int]

### CheckpointPercentages
- **Type**: typing.Optional[typing.List[int]]

### CheckpointDelay
- **Type**: typing.Optional[int]

### SkipMatching
- **Type**: typing.Optional[bool]

### AutoRollback
- **Type**: typing.Optional[bool]

### ScaleInProtectedInstances
- **Type**: typing.Optional[typing.Literal['Ignore', 'Refresh', 'Wait']]

### StandbyInstances
- **Type**: typing.Optional[typing.Literal['Ignore', 'Terminate', 'Wait']]

### AlarmSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.AlarmSpecificationOutputTypeDef]

### MaxHealthyPercentage
- **Type**: typing.Optional[int]


# RefreshPreferencesTypeDef

### MinHealthyPercentage
- **Type**: typing.Optional[int]

### InstanceWarmup
- **Type**: typing.Optional[int]

### CheckpointPercentages
- **Type**: typing.Optional[typing.Sequence[int]]

### CheckpointDelay
- **Type**: typing.Optional[int]

### SkipMatching
- **Type**: typing.Optional[bool]

### AutoRollback
- **Type**: typing.Optional[bool]

### ScaleInProtectedInstances
- **Type**: typing.Optional[typing.Literal['Ignore', 'Refresh', 'Wait']]

### StandbyInstances
- **Type**: typing.Optional[typing.Literal['Ignore', 'Terminate', 'Wait']]

### AlarmSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.AlarmSpecificationTypeDef]

### MaxHealthyPercentage
- **Type**: typing.Optional[int]


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


# RollbackDetailsTypeDef

### RollbackReason
- **Type**: typing.Optional[str]

### RollbackStartTime
- **Type**: typing.Optional[datetime.datetime]

### PercentageCompleteOnRollback
- **Type**: typing.Optional[int]

### InstancesToUpdateOnRollback
- **Type**: typing.Optional[int]

### ProgressDetailsOnRollback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceRefreshProgressDetailsTypeDef]


# RollbackInstanceRefreshAnswerTypeDef

### InstanceRefreshId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RollbackInstanceRefreshTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ScalingPolicyTypeDef

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### PolicyARN
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[str]

### AdjustmentType
- **Type**: typing.Optional[str]

### MinAdjustmentStep
- **Type**: typing.Optional[int]

### MinAdjustmentMagnitude
- **Type**: typing.Optional[int]

### ScalingAdjustment
- **Type**: typing.Optional[int]

### Cooldown
- **Type**: typing.Optional[int]

### StepAdjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.StepAdjustmentTypeDef]]

### MetricAggregationType
- **Type**: typing.Optional[str]

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]

### Alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.AlarmTypeDef]]

### TargetTrackingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.TargetTrackingConfigurationOutputTypeDef]

### Enabled
- **Type**: typing.Optional[bool]

### PredictiveScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredictiveScalingConfigurationOutputTypeDef]


# ScalingProcessQueryRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingProcesses
- **Type**: typing.Optional[typing.Sequence[str]]


# ScheduledActionsTypeTypeDef

### ScheduledUpdateGroupActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.ScheduledUpdateGroupActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ScheduledUpdateGroupActionRequestTypeDef

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Recurrence
- **Type**: typing.Optional[str]

### MinSize
- **Type**: typing.Optional[int]

### MaxSize
- **Type**: typing.Optional[int]

### DesiredCapacity
- **Type**: typing.Optional[int]

### TimeZone
- **Type**: typing.Optional[str]


# ScheduledUpdateGroupActionTypeDef

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### ScheduledActionName
- **Type**: typing.Optional[str]

### ScheduledActionARN
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Recurrence
- **Type**: typing.Optional[str]

### MinSize
- **Type**: typing.Optional[int]

### MaxSize
- **Type**: typing.Optional[int]

### DesiredCapacity
- **Type**: typing.Optional[int]

### TimeZone
- **Type**: typing.Optional[str]


# SetDesiredCapacityTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### HonorCooldown
- **Type**: typing.Optional[bool]


# SetInstanceHealthQueryRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HealthStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ShouldRespectGracePeriod
- **Type**: typing.Optional[bool]


# SetInstanceProtectionQueryRequestTypeDef

### InstanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedFromScaleIn
- **Type**: <class 'bool'>
- **Required**: Yes


# StartInstanceRefreshAnswerTypeDef

### InstanceRefreshId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartInstanceRefreshTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Strategy
- **Type**: typing.Optional[typing.Literal['Rolling']]

### DesiredConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.DesiredConfigurationTypeDef]

### Preferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.RefreshPreferencesTypeDef]


# StepAdjustmentTypeDef

### ScalingAdjustment
- **Type**: <class 'int'>
- **Required**: Yes

### MetricIntervalLowerBound
- **Type**: typing.Optional[float]

### MetricIntervalUpperBound
- **Type**: typing.Optional[float]


# SuspendedProcessTypeDef

### ProcessName
- **Type**: typing.Optional[str]

### SuspensionReason
- **Type**: typing.Optional[str]


# TagDescriptionTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### PropagateAtLaunch
- **Type**: typing.Optional[bool]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### PropagateAtLaunch
- **Type**: typing.Optional[bool]


# TagsTypeTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling_classes.TagDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# TargetTrackingConfigurationExtraOutputTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredefinedMetricSpecificationTypeDef]

### CustomizedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.CustomizedMetricSpecificationExtraOutputTypeDef]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# TargetTrackingConfigurationOutputTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredefinedMetricSpecificationTypeDef]

### CustomizedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.CustomizedMetricSpecificationOutputTypeDef]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# TargetTrackingConfigurationTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.PredefinedMetricSpecificationTypeDef]

### CustomizedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.CustomizedMetricSpecificationTypeDef]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDataQueryExtraOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.TargetTrackingMetricStatExtraOutputTypeDef]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDataQueryOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.TargetTrackingMetricStatOutputTypeDef]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDataQueryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.TargetTrackingMetricStatTypeDef]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricStatExtraOutputTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MetricExtraOutputTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# TargetTrackingMetricStatOutputTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MetricOutputTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# TargetTrackingMetricStatTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling_classes.MetricTypeDef'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# TerminateInstanceInAutoScalingGroupTypeRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ShouldDecrementDesiredCapacity
- **Type**: <class 'bool'>
- **Required**: Yes


# TotalLocalStorageGBRequestTypeDef

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# TrafficSourceIdentifierTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[str]


# TrafficSourceStateTypeDef

### TrafficSource
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### Identifier
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# UpdateAutoScalingGroupTypeRequestTypeDef

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.LaunchTemplateSpecificationTypeDef]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.MixedInstancesPolicyTypeDef]

### MinSize
- **Type**: typing.Optional[int]

### MaxSize
- **Type**: typing.Optional[int]

### DesiredCapacity
- **Type**: typing.Optional[int]

### DefaultCooldown
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### PlacementGroup
- **Type**: typing.Optional[str]

### VPCZoneIdentifier
- **Type**: typing.Optional[str]

### TerminationPolicies
- **Type**: typing.Optional[typing.Sequence[str]]

### NewInstancesProtectedFromScaleIn
- **Type**: typing.Optional[bool]

### ServiceLinkedRoleARN
- **Type**: typing.Optional[str]

### MaxInstanceLifetime
- **Type**: typing.Optional[int]

### CapacityRebalance
- **Type**: typing.Optional[bool]

### Context
- **Type**: typing.Optional[str]

### DesiredCapacityType
- **Type**: typing.Optional[str]

### DefaultInstanceWarmup
- **Type**: typing.Optional[int]

### InstanceMaintenancePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceMaintenancePolicyTypeDef]


# VCpuCountRequestTypeDef

### Min
- **Type**: <class 'int'>
- **Required**: Yes

### Max
- **Type**: typing.Optional[int]


# WarmPoolConfigurationTypeDef

### MaxGroupPreparedCapacity
- **Type**: typing.Optional[int]

### MinSize
- **Type**: typing.Optional[int]

### PoolState
- **Type**: typing.Optional[typing.Literal['Hibernated', 'Running', 'Stopped']]

### Status
- **Type**: typing.Optional[typing.Literal['PendingDelete']]

### InstanceReusePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling_classes.InstanceReusePolicyTypeDef]



# Autoscaling Classes

# AcceleratorCountRequest

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# AcceleratorTotalMemoryMiBRequest

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# ActivitiesType

### Activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Activity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Activity

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


# ActivityType

### Activity
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Activity'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# AdjustmentType

### AdjustmentType
- **Type**: typing.Optional[str]


# Alarm

### AlarmName
- **Type**: typing.Optional[str]

### AlarmARN
- **Type**: typing.Optional[str]


# AlarmSpecification

### Alarms
- **Type**: typing.Optional[typing.List[str]]


# AlarmSpecificationOutput

### Alarms
- **Type**: typing.Optional[typing.List[str]]


# AttachInstancesQuery

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# AttachLoadBalancerTargetGroupsType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupARNs
- **Type**: typing.List[str]
- **Required**: Yes


# AttachLoadBalancersType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerNames
- **Type**: typing.List[str]
- **Required**: Yes


# AttachTrafficSourcesType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TrafficSourceIdentifier]
- **Required**: Yes

### SkipZonalShiftValidation
- **Type**: typing.Optional[bool]


# AutoScalingGroup

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateSpecification]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MixedInstancesPolicyOutput]

### PredictedCapacity
- **Type**: typing.Optional[int]

### LoadBalancerNames
- **Type**: typing.Optional[typing.List[str]]

### TargetGroupARNs
- **Type**: typing.Optional[typing.List[str]]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Instance]]

### SuspendedProcesses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.SuspendedProcess]]

### PlacementGroup
- **Type**: typing.Optional[str]

### VPCZoneIdentifier
- **Type**: typing.Optional[str]

### EnabledMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.EnabledMetric]]

### Status
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TagDescription]]

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
- **Type**: <class 'NoneType'>

### WarmPoolSize
- **Type**: typing.Optional[int]

### Context
- **Type**: typing.Optional[str]

### DesiredCapacityType
- **Type**: typing.Optional[str]

### DefaultInstanceWarmup
- **Type**: typing.Optional[int]

### TrafficSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TrafficSourceIdentifier]]

### InstanceMaintenancePolicy
- **Type**: <class 'NoneType'>

### AvailabilityZoneDistribution
- **Type**: <class 'NoneType'>

### AvailabilityZoneImpairmentPolicy
- **Type**: <class 'NoneType'>

### CapacityReservationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CapacityReservationSpecificationOutput]


# AutoScalingGroupNamesType

### AutoScalingGroupNames
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Filter]]


# AutoScalingGroupNamesTypePaginate

### AutoScalingGroupNames
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# AutoScalingGroupsType

### AutoScalingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.AutoScalingGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AutoScalingInstanceDetails

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateSpecification]

### WeightedCapacity
- **Type**: typing.Optional[str]


# AutoScalingInstancesType

### AutoScalingInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.AutoScalingInstanceDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AvailabilityZoneDistribution

### CapacityDistributionStrategy
- **Type**: typing.Optional[typing.Literal['balanced-best-effort', 'balanced-only']]


# AvailabilityZoneImpairmentPolicy

### ZonalShiftEnabled
- **Type**: typing.Optional[bool]

### ImpairedZoneHealthCheckBehavior
- **Type**: typing.Optional[typing.Literal['IgnoreUnhealthy', 'ReplaceUnhealthy']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaselineEbsBandwidthMbpsRequest

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# BaselinePerformanceFactorsRequest

### Cpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CpuPerformanceFactorRequest]


# BaselinePerformanceFactorsRequestOutput

### Cpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CpuPerformanceFactorRequestOutput]


# BatchDeleteScheduledActionAnswer

### FailedScheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.FailedScheduledUpdateGroupActionRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteScheduledActionType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActionNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchPutScheduledUpdateGroupActionAnswer

### FailedScheduledUpdateGroupActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.FailedScheduledUpdateGroupActionRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutScheduledUpdateGroupActionType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledUpdateGroupActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ScheduledUpdateGroupActionRequest]
- **Required**: Yes


# BlockDeviceMapping

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### VirtualName
- **Type**: typing.Optional[str]

### Ebs
- **Type**: <class 'NoneType'>

### NoDevice
- **Type**: typing.Optional[bool]


# CancelInstanceRefreshAnswer

### InstanceRefreshId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# CancelInstanceRefreshType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CapacityForecast

### Timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes


# CapacityReservationSpecification

### CapacityReservationPreference
- **Type**: typing.Optional[typing.Literal['capacity-reservations-first', 'capacity-reservations-only', 'default', 'none']]

### CapacityReservationTarget
- **Type**: <class 'NoneType'>


# CapacityReservationSpecificationOutput

### CapacityReservationPreference
- **Type**: typing.Optional[typing.Literal['capacity-reservations-first', 'capacity-reservations-only', 'default', 'none']]

### CapacityReservationTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CapacityReservationTargetOutput]


# CapacityReservationTarget

### CapacityReservationIds
- **Type**: typing.Optional[typing.List[str]]

### CapacityReservationResourceGroupArns
- **Type**: typing.Optional[typing.List[str]]


# CapacityReservationTargetOutput

### CapacityReservationIds
- **Type**: typing.Optional[typing.List[str]]

### CapacityReservationResourceGroupArns
- **Type**: typing.Optional[typing.List[str]]


# CompleteLifecycleActionType

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


# CpuPerformanceFactorRequest

### References
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PerformanceFactorReferenceRequest]]


# CpuPerformanceFactorRequestOutput

### References
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PerformanceFactorReferenceRequest]]


# CreateAutoScalingGroupType

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateSpecification]

### MixedInstancesPolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MixedInstancesPolicy, aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MixedInstancesPolicyOutput, NoneType]

### InstanceId
- **Type**: typing.Optional[str]

### DesiredCapacity
- **Type**: typing.Optional[int]

### DefaultCooldown
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### LoadBalancerNames
- **Type**: typing.Optional[typing.List[str]]

### TargetGroupARNs
- **Type**: typing.Optional[typing.List[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### PlacementGroup
- **Type**: typing.Optional[str]

### VPCZoneIdentifier
- **Type**: typing.Optional[str]

### TerminationPolicies
- **Type**: typing.Optional[typing.List[str]]

### NewInstancesProtectedFromScaleIn
- **Type**: typing.Optional[bool]

### CapacityRebalance
- **Type**: typing.Optional[bool]

### LifecycleHookSpecificationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LifecycleHookSpecification]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Tag]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TrafficSourceIdentifier]]

### InstanceMaintenancePolicy
- **Type**: <class 'NoneType'>

### AvailabilityZoneDistribution
- **Type**: <class 'NoneType'>

### AvailabilityZoneImpairmentPolicy
- **Type**: <class 'NoneType'>

### SkipZonalShiftValidation
- **Type**: typing.Optional[bool]

### CapacityReservationSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CapacityReservationSpecification, aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CapacityReservationSpecificationOutput, NoneType]


# CreateLaunchConfigurationType

### LaunchConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageId
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

### InstanceId
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### RamdiskId
- **Type**: typing.Optional[str]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.BlockDeviceMapping]]

### InstanceMonitoring
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.InstanceMetadataOptions]


# CreateOrUpdateTagsType

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Tag]
- **Required**: Yes


# CustomizedMetricSpecification

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDimension]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TargetTrackingMetricDataQuery]]


# CustomizedMetricSpecificationOutput

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDimension]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### Unit
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TargetTrackingMetricDataQueryOutput]]


# DeleteAutoScalingGroupType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DeleteLifecycleHookType

### LifecycleHookName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotificationConfigurationType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TopicARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyType

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingGroupName
- **Type**: typing.Optional[str]


# DeleteScheduledActionType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsType

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Tag]
- **Required**: Yes


# DeleteWarmPoolType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DescribeAccountLimitsAnswer

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
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAdjustmentTypesAnswer

### AdjustmentTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.AdjustmentType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAutoScalingInstancesType

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAutoScalingInstancesTypePaginate

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DescribeAutoScalingNotificationTypesAnswer

### AutoScalingNotificationTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInstanceRefreshesAnswer

### InstanceRefreshes
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.InstanceRefresh]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceRefreshesType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceRefreshIds
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeLifecycleHookTypesAnswer

### LifecycleHookTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLifecycleHooksAnswer

### LifecycleHooks
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LifecycleHook]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLifecycleHooksType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleHookNames
- **Type**: typing.Optional[typing.List[str]]


# DescribeLoadBalancerTargetGroupsRequest

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeLoadBalancerTargetGroupsRequestPaginate

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DescribeLoadBalancerTargetGroupsResponse

### LoadBalancerTargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LoadBalancerTargetGroupState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeLoadBalancersRequest

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeLoadBalancersRequestPaginate

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DescribeLoadBalancersResponse

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LoadBalancerState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMetricCollectionTypesAnswer

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricCollectionType]
- **Required**: Yes

### Granularities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricGranularityType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNotificationConfigurationsAnswer

### NotificationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.NotificationConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeNotificationConfigurationsType

### AutoScalingGroupNames
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeNotificationConfigurationsTypePaginate

### AutoScalingGroupNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DescribePoliciesType

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]

### PolicyTypes
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribePoliciesTypePaginate

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]

### PolicyTypes
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DescribeScalingActivitiesType

### ActivityIds
- **Type**: typing.Optional[typing.List[str]]

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### IncludeDeletedGroups
- **Type**: typing.Optional[bool]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScalingActivitiesTypePaginate

### ActivityIds
- **Type**: typing.Optional[typing.List[str]]

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### IncludeDeletedGroups
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DescribeScheduledActionsType

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### ScheduledActionNames
- **Type**: typing.Optional[typing.List[str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeScheduledActionsTypePaginate

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### ScheduledActionNames
- **Type**: typing.Optional[typing.List[str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DescribeTagsType

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Filter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeTagsTypePaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DescribeTerminationPolicyTypesAnswer

### TerminationPolicyTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrafficSourcesRequest

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficSourceType
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeTrafficSourcesResponse

### TrafficSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TrafficSourceState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWarmPoolAnswer

### WarmPoolConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.WarmPoolConfiguration'>
- **Required**: Yes

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Instance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWarmPoolType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWarmPoolTypePaginate

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# DesiredConfiguration

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateSpecification]

### MixedInstancesPolicy
- **Type**: <class 'NoneType'>


# DesiredConfigurationOutput

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateSpecification]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MixedInstancesPolicyOutput]


# DetachInstancesAnswer

### Activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Activity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# DetachInstancesQuery

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ShouldDecrementDesiredCapacity
- **Type**: <class 'bool'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# DetachLoadBalancerTargetGroupsType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupARNs
- **Type**: typing.List[str]
- **Required**: Yes


# DetachLoadBalancersType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerNames
- **Type**: typing.List[str]
- **Required**: Yes


# DetachTrafficSourcesType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TrafficSourceIdentifier]
- **Required**: Yes


# DisableMetricsCollectionQuery

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Optional[typing.List[str]]


# Ebs

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# EnableMetricsCollectionQuery

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Granularity
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Optional[typing.List[str]]


# EnabledMetric

### Metric
- **Type**: typing.Optional[str]

### Granularity
- **Type**: typing.Optional[str]


# EnterStandbyAnswer

### Activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Activity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# EnterStandbyQuery

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ShouldDecrementDesiredCapacity
- **Type**: <class 'bool'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# ExecutePolicyType

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


# ExitStandbyAnswer

### Activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Activity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# ExitStandbyQuery

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# FailedScheduledUpdateGroupActionRequest

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# Filter

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# GetPredictiveScalingForecastAnswer

### LoadForecast
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LoadForecast]
- **Required**: Yes

### CapacityForecast
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CapacityForecast'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# GetPredictiveScalingForecastType

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


# Instance

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateSpecification]

### WeightedCapacity
- **Type**: typing.Optional[str]


# InstanceMaintenancePolicy

### MinHealthyPercentage
- **Type**: typing.Optional[int]

### MaxHealthyPercentage
- **Type**: typing.Optional[int]


# InstanceMetadataOptions

### HttpTokens
- **Type**: typing.Optional[typing.Literal['optional', 'required']]

### HttpPutResponseHopLimit
- **Type**: typing.Optional[int]

### HttpEndpoint
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]


# InstanceMonitoring

### Enabled
- **Type**: typing.Optional[bool]


# InstanceRefresh

### InstanceRefreshId
- **Type**: typing.Optional[str]

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Baking', 'Cancelled', 'Cancelling', 'Failed', 'InProgress', 'Pending', 'RollbackFailed', 'RollbackInProgress', 'RollbackSuccessful', 'Successful']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.InstanceRefreshProgressDetails]

### Preferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.RefreshPreferencesOutput]

### DesiredConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.DesiredConfigurationOutput]

### RollbackDetails
- **Type**: <class 'NoneType'>


# InstanceRefreshLivePoolProgress

### PercentageComplete
- **Type**: typing.Optional[int]

### InstancesToUpdate
- **Type**: typing.Optional[int]


# InstanceRefreshProgressDetails

### LivePoolProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.InstanceRefreshLivePoolProgress]

### WarmPoolProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.InstanceRefreshWarmPoolProgress]


# InstanceRefreshWarmPoolProgress

### PercentageComplete
- **Type**: typing.Optional[int]

### InstancesToUpdate
- **Type**: typing.Optional[int]


# InstanceRequirements

### VCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.VCpuCountRequest'>
- **Required**: Yes

### MemoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MemoryMiBRequest'>
- **Required**: Yes

### CpuManufacturers
- **Type**: typing.Optional[typing.List[typing.Literal['amazon-web-services', 'amd', 'intel']]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MemoryGiBPerVCpuRequest]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.NetworkInterfaceCountRequest]

### LocalStorage
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### LocalStorageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['hdd', 'ssd']]]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TotalLocalStorageGBRequest]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.BaselineEbsBandwidthMbpsRequest]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['fpga', 'gpu', 'inference']]]

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.AcceleratorCountRequest]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.List[typing.Literal['amazon-web-services', 'amd', 'nvidia', 'xilinx']]]

### AcceleratorNames
- **Type**: typing.Optional[typing.List[typing.Literal['a100', 'k80', 'm60', 'radeon-pro-v520', 't4', 'v100', 'vu9p']]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.AcceleratorTotalMemoryMiBRequest]

### NetworkBandwidthGbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.NetworkBandwidthGbpsRequest]

### AllowedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### BaselinePerformanceFactors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.BaselinePerformanceFactorsRequest]


# InstanceRequirementsOutput

### VCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.VCpuCountRequest'>
- **Required**: Yes

### MemoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MemoryMiBRequest'>
- **Required**: Yes

### CpuManufacturers
- **Type**: typing.Optional[typing.List[typing.Literal['amazon-web-services', 'amd', 'intel']]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MemoryGiBPerVCpuRequest]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.NetworkInterfaceCountRequest]

### LocalStorage
- **Type**: typing.Optional[typing.Literal['excluded', 'included', 'required']]

### LocalStorageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['hdd', 'ssd']]]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TotalLocalStorageGBRequest]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.BaselineEbsBandwidthMbpsRequest]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['fpga', 'gpu', 'inference']]]

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.AcceleratorCountRequest]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.List[typing.Literal['amazon-web-services', 'amd', 'nvidia', 'xilinx']]]

### AcceleratorNames
- **Type**: typing.Optional[typing.List[typing.Literal['a100', 'k80', 'm60', 'radeon-pro-v520', 't4', 'v100', 'vu9p']]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.AcceleratorTotalMemoryMiBRequest]

### NetworkBandwidthGbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.NetworkBandwidthGbpsRequest]

### AllowedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### BaselinePerformanceFactors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.BaselinePerformanceFactorsRequestOutput]


# InstanceReusePolicy

### ReuseOnScaleIn
- **Type**: typing.Optional[bool]


# InstancesDistribution

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


# LaunchConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.BlockDeviceMapping]]

### InstanceMonitoring
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.InstanceMetadataOptions]


# LaunchConfigurationNameType

### LaunchConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# LaunchConfigurationNamesType

### LaunchConfigurationNames
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# LaunchConfigurationNamesTypePaginate

### LaunchConfigurationNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PaginatorConfig]


# LaunchConfigurationsType

### LaunchConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LaunchTemplate

### LaunchTemplateSpecification
- **Type**: <class 'NoneType'>

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateOverrides]]


# LaunchTemplateOutput

### LaunchTemplateSpecification
- **Type**: <class 'NoneType'>

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateOverridesOutput]]


# LaunchTemplateOverrides

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[str]

### LaunchTemplateSpecification
- **Type**: <class 'NoneType'>

### InstanceRequirements
- **Type**: <class 'NoneType'>


# LaunchTemplateOverridesOutput

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[str]

### LaunchTemplateSpecification
- **Type**: <class 'NoneType'>

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.InstanceRequirementsOutput]


# LaunchTemplateSpecification

### LaunchTemplateId
- **Type**: typing.Optional[str]

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# LifecycleHook

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


# LifecycleHookSpecification

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


# LoadBalancerState

### LoadBalancerName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# LoadBalancerTargetGroupState

### LoadBalancerTargetGroupARN
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# LoadForecast

### Timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes

### MetricSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingMetricSpecificationOutput'>
- **Required**: Yes


# MemoryGiBPerVCpuRequest

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# MemoryMiBRequest

### Min
- **Type**: <class 'int'>
- **Required**: Yes

### Max
- **Type**: typing.Optional[int]


# Metric

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDimension]]


# MetricCollectionType

### Metric
- **Type**: typing.Optional[str]


# MetricDataQuery

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: <class 'NoneType'>

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# MetricDataQueryOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricStatOutput]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]


# MetricDimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# MetricGranularityType

### Granularity
- **Type**: typing.Optional[str]


# MetricOutput

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDimension]]


# MetricStat

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Metric'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# MetricStatOutput

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricOutput'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]


# MixedInstancesPolicy

### LaunchTemplate
- **Type**: <class 'NoneType'>

### InstancesDistribution
- **Type**: <class 'NoneType'>


# MixedInstancesPolicyOutput

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateOutput]

### InstancesDistribution
- **Type**: <class 'NoneType'>


# NetworkBandwidthGbpsRequest

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# NetworkInterfaceCountRequest

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# NotificationConfiguration

### AutoScalingGroupName
- **Type**: typing.Optional[str]

### TopicARN
- **Type**: typing.Optional[str]

### NotificationType
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceFactorReferenceRequest

### InstanceFamily
- **Type**: typing.Optional[str]


# PoliciesType

### ScalingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ScalingPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PolicyARNType

### PolicyARN
- **Type**: <class 'str'>
- **Required**: Yes

### Alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Alarm]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# PredefinedMetricSpecification

### PredefinedMetricType
- **Type**: typing.Literal['ALBRequestCountPerTarget', 'ASGAverageCPUUtilization', 'ASGAverageNetworkIn', 'ASGAverageNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingConfiguration

### MetricSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingMetricSpecification]
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### SchedulingBufferTime
- **Type**: typing.Optional[int]

### MaxCapacityBreachBehavior
- **Type**: typing.Optional[typing.Literal['HonorMaxCapacity', 'IncreaseMaxCapacity']]

### MaxCapacityBuffer
- **Type**: typing.Optional[int]


# PredictiveScalingConfigurationOutput

### MetricSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingMetricSpecificationOutput]
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['ForecastAndScale', 'ForecastOnly']]

### SchedulingBufferTime
- **Type**: typing.Optional[int]

### MaxCapacityBreachBehavior
- **Type**: typing.Optional[typing.Literal['HonorMaxCapacity', 'IncreaseMaxCapacity']]

### MaxCapacityBuffer
- **Type**: typing.Optional[int]


# PredictiveScalingCustomizedCapacityMetric

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDataQuery]
- **Required**: Yes


# PredictiveScalingCustomizedCapacityMetricOutput

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDataQueryOutput]
- **Required**: Yes


# PredictiveScalingCustomizedLoadMetric

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDataQuery]
- **Required**: Yes


# PredictiveScalingCustomizedLoadMetricOutput

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDataQueryOutput]
- **Required**: Yes


# PredictiveScalingCustomizedScalingMetric

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDataQuery]
- **Required**: Yes


# PredictiveScalingCustomizedScalingMetricOutput

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricDataQueryOutput]
- **Required**: Yes


# PredictiveScalingMetricSpecification

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricPairSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingPredefinedMetricPair]

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingPredefinedScalingMetric]

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingPredefinedLoadMetric]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingCustomizedScalingMetric]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingCustomizedLoadMetric]

### CustomizedCapacityMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingCustomizedCapacityMetric]


# PredictiveScalingMetricSpecificationOutput

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricPairSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingPredefinedMetricPair]

### PredefinedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingPredefinedScalingMetric]

### PredefinedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingPredefinedLoadMetric]

### CustomizedScalingMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingCustomizedScalingMetricOutput]

### CustomizedLoadMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingCustomizedLoadMetricOutput]

### CustomizedCapacityMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingCustomizedCapacityMetricOutput]


# PredictiveScalingPredefinedLoadMetric

### PredefinedMetricType
- **Type**: typing.Literal['ALBTargetGroupRequestCount', 'ASGTotalCPUUtilization', 'ASGTotalNetworkIn', 'ASGTotalNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingPredefinedMetricPair

### PredefinedMetricType
- **Type**: typing.Literal['ALBRequestCount', 'ASGCPUUtilization', 'ASGNetworkIn', 'ASGNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# PredictiveScalingPredefinedScalingMetric

### PredefinedMetricType
- **Type**: typing.Literal['ALBRequestCountPerTarget', 'ASGAverageCPUUtilization', 'ASGAverageNetworkIn', 'ASGAverageNetworkOut']
- **Required**: Yes

### ResourceLabel
- **Type**: typing.Optional[str]


# ProcessType

### ProcessName
- **Type**: <class 'str'>
- **Required**: Yes


# ProcessesType

### Processes
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ProcessType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# PutLifecycleHookType

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


# PutNotificationConfigurationType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TopicARN
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationTypes
- **Type**: typing.List[str]
- **Required**: Yes


# PutScalingPolicyType

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.StepAdjustment]]

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]

### TargetTrackingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TargetTrackingConfiguration, aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TargetTrackingConfigurationOutput, NoneType]

### Enabled
- **Type**: typing.Optional[bool]

### PredictiveScalingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingConfiguration, aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingConfigurationOutput, NoneType]


# PutScheduledUpdateGroupActionType

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


# PutWarmPoolType

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
- **Type**: <class 'NoneType'>


# RecordLifecycleActionHeartbeatType

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


# RefreshPreferences

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
- **Type**: <class 'NoneType'>

### MaxHealthyPercentage
- **Type**: typing.Optional[int]

### BakeTime
- **Type**: typing.Optional[int]


# RefreshPreferencesOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.AlarmSpecificationOutput]

### MaxHealthyPercentage
- **Type**: typing.Optional[int]

### BakeTime
- **Type**: typing.Optional[int]


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


# RollbackDetails

### RollbackReason
- **Type**: typing.Optional[str]

### RollbackStartTime
- **Type**: typing.Optional[datetime.datetime]

### PercentageCompleteOnRollback
- **Type**: typing.Optional[int]

### InstancesToUpdateOnRollback
- **Type**: typing.Optional[int]

### ProgressDetailsOnRollback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.InstanceRefreshProgressDetails]


# RollbackInstanceRefreshAnswer

### InstanceRefreshId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# RollbackInstanceRefreshType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ScalingPolicy

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.StepAdjustment]]

### MetricAggregationType
- **Type**: typing.Optional[str]

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]

### Alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Alarm]]

### TargetTrackingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TargetTrackingConfigurationOutput]

### Enabled
- **Type**: typing.Optional[bool]

### PredictiveScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.PredictiveScalingConfigurationOutput]


# ScalingProcessQuery

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingProcesses
- **Type**: typing.Optional[typing.List[str]]


# ScalingProcessQueryRequest

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingProcesses
- **Type**: typing.Optional[typing.List[str]]


# ScheduledActionsType

### ScheduledUpdateGroupActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ScheduledUpdateGroupAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ScheduledUpdateGroupAction

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


# ScheduledUpdateGroupActionRequest

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


# SetDesiredCapacityType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### HonorCooldown
- **Type**: typing.Optional[bool]


# SetInstanceHealthQuery

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HealthStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ShouldRespectGracePeriod
- **Type**: typing.Optional[bool]


# SetInstanceProtectionQuery

### InstanceIds
- **Type**: typing.List[str]
- **Required**: Yes

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedFromScaleIn
- **Type**: <class 'bool'>
- **Required**: Yes


# StartInstanceRefreshAnswer

### InstanceRefreshId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes


# StartInstanceRefreshType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Strategy
- **Type**: typing.Optional[typing.Literal['Rolling']]

### DesiredConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.DesiredConfiguration, aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.DesiredConfigurationOutput, NoneType]

### Preferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.RefreshPreferences, aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.RefreshPreferencesOutput, NoneType]


# StepAdjustment

### ScalingAdjustment
- **Type**: <class 'int'>
- **Required**: Yes

### MetricIntervalLowerBound
- **Type**: typing.Optional[float]

### MetricIntervalUpperBound
- **Type**: typing.Optional[float]


# SuspendedProcess

### ProcessName
- **Type**: typing.Optional[str]

### SuspensionReason
- **Type**: typing.Optional[str]


# Tag

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


# TagDescription

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


# TagsType

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TagDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# TargetTrackingConfiguration

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: <class 'NoneType'>

### CustomizedMetricSpecification
- **Type**: <class 'NoneType'>

### DisableScaleIn
- **Type**: typing.Optional[bool]


# TargetTrackingConfigurationOutput

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes

### PredefinedMetricSpecification
- **Type**: <class 'NoneType'>

### CustomizedMetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CustomizedMetricSpecificationOutput]

### DisableScaleIn
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDataQuery

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TargetTrackingMetricStat]

### Label
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricDataQueryOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Optional[str]

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.TargetTrackingMetricStatOutput]

### Label
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### ReturnData
- **Type**: typing.Optional[bool]


# TargetTrackingMetricStat

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.Metric'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]


# TargetTrackingMetricStatOutput

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MetricOutput'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]


# TerminateInstanceInAutoScalingGroupType

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ShouldDecrementDesiredCapacity
- **Type**: <class 'bool'>
- **Required**: Yes


# TotalLocalStorageGBRequest

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# TrafficSourceIdentifier

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[str]


# TrafficSourceState

### TrafficSource
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### Identifier
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# UpdateAutoScalingGroupType

### AutoScalingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.LaunchTemplateSpecification]

### MixedInstancesPolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MixedInstancesPolicy, aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.MixedInstancesPolicyOutput, NoneType]

### MinSize
- **Type**: typing.Optional[int]

### MaxSize
- **Type**: typing.Optional[int]

### DesiredCapacity
- **Type**: typing.Optional[int]

### DefaultCooldown
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### PlacementGroup
- **Type**: typing.Optional[str]

### VPCZoneIdentifier
- **Type**: typing.Optional[str]

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

### Context
- **Type**: typing.Optional[str]

### DesiredCapacityType
- **Type**: typing.Optional[str]

### DefaultInstanceWarmup
- **Type**: typing.Optional[int]

### InstanceMaintenancePolicy
- **Type**: <class 'NoneType'>

### AvailabilityZoneDistribution
- **Type**: <class 'NoneType'>

### AvailabilityZoneImpairmentPolicy
- **Type**: <class 'NoneType'>

### SkipZonalShiftValidation
- **Type**: typing.Optional[bool]

### CapacityReservationSpecification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CapacityReservationSpecification, aws_resource_validator.pydantic_models.autoscaling.autoscaling_classes.CapacityReservationSpecificationOutput, NoneType]


# VCpuCountRequest

### Min
- **Type**: <class 'int'>
- **Required**: Yes

### Max
- **Type**: typing.Optional[int]


# WarmPoolConfiguration

### MaxGroupPreparedCapacity
- **Type**: typing.Optional[int]

### MinSize
- **Type**: typing.Optional[int]

### PoolState
- **Type**: typing.Optional[typing.Literal['Hibernated', 'Running', 'Stopped']]

### Status
- **Type**: typing.Optional[typing.Literal['PendingDelete']]

### InstanceReusePolicy
- **Type**: <class 'NoneType'>



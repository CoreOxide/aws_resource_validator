from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.autoscaling.autoscaling_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceleratorCountRequest(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class AcceleratorTotalMemoryMiBRequest(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class Activity(BaseValidatorModel):
    ActivityId: str
    AutoScalingGroupName: str
    Cause: str
    StartTime: datetime
    StatusCode: ScalingActivityStatusCodeType
    Description: Optional[str] = None
    EndTime: Optional[datetime] = None
    StatusMessage: Optional[str] = None
    Progress: Optional[int] = None
    Details: Optional[str] = None
    AutoScalingGroupState: Optional[str] = None
    AutoScalingGroupARN: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AdjustmentType(BaseValidatorModel):
    AdjustmentType: Optional[str] = None


class AlarmSpecificationOutput(BaseValidatorModel):
    Alarms: Optional[List[str]] = None


class AlarmSpecification(BaseValidatorModel):
    Alarms: Optional[List[str]] = None


class Alarm(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmARN: Optional[str] = None


# This class is the input for the 'attach_instances' function.
class AttachInstancesQuery(BaseValidatorModel):
    AutoScalingGroupName: str
    InstanceIds: Optional[List[str]] = None


class AttachLoadBalancerTargetGroupsType(BaseValidatorModel):
    AutoScalingGroupName: str
    TargetGroupARNs: List[str]


class AttachLoadBalancersType(BaseValidatorModel):
    AutoScalingGroupName: str
    LoadBalancerNames: List[str]


class TrafficSourceIdentifier(BaseValidatorModel):
    Identifier: str
    Type: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class AvailabilityZoneDistribution(BaseValidatorModel):
    CapacityDistributionStrategy: Optional[CapacityDistributionStrategyType] = None


class AvailabilityZoneImpairmentPolicy(BaseValidatorModel):
    ZonalShiftEnabled: Optional[bool] = None
    ImpairedZoneHealthCheckBehavior: Optional[ImpairedZoneHealthCheckBehaviorType] = None


class EnabledMetric(BaseValidatorModel):
    Metric: Optional[str] = None
    Granularity: Optional[str] = None


class InstanceMaintenancePolicy(BaseValidatorModel):
    MinHealthyPercentage: Optional[int] = None
    MaxHealthyPercentage: Optional[int] = None


class LaunchTemplateSpecification(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class SuspendedProcess(BaseValidatorModel):
    ProcessName: Optional[str] = None
    SuspensionReason: Optional[str] = None


class TagDescription(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Key: Optional[str] = None
    Value: Optional[str] = None
    PropagateAtLaunch: Optional[bool] = None


class BaselineEbsBandwidthMbpsRequest(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class FailedScheduledUpdateGroupActionRequest(BaseValidatorModel):
    ScheduledActionName: str
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'batch_delete_scheduled_action' function.
class BatchDeleteScheduledActionType(BaseValidatorModel):
    AutoScalingGroupName: str
    ScheduledActionNames: List[str]


class Ebs(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    Encrypted: Optional[bool] = None
    Throughput: Optional[int] = None


# This class is the input for the 'cancel_instance_refresh' function.
class CancelInstanceRefreshType(BaseValidatorModel):
    AutoScalingGroupName: str


class CapacityForecast(BaseValidatorModel):
    Timestamps: List[datetime]
    Values: List[float]


class CapacityReservationTargetOutput(BaseValidatorModel):
    CapacityReservationIds: Optional[List[str]] = None
    CapacityReservationResourceGroupArns: Optional[List[str]] = None


class CapacityReservationTarget(BaseValidatorModel):
    CapacityReservationIds: Optional[List[str]] = None
    CapacityReservationResourceGroupArns: Optional[List[str]] = None


class CompleteLifecycleActionType(BaseValidatorModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleActionResult: str
    LifecycleActionToken: Optional[str] = None
    InstanceId: Optional[str] = None


class PerformanceFactorReferenceRequest(BaseValidatorModel):
    InstanceFamily: Optional[str] = None


class LifecycleHookSpecification(BaseValidatorModel):
    LifecycleHookName: str
    LifecycleTransition: str
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    RoleARN: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Value: Optional[str] = None
    PropagateAtLaunch: Optional[bool] = None


class InstanceMetadataOptions(BaseValidatorModel):
    HttpTokens: Optional[InstanceMetadataHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None


class InstanceMonitoring(BaseValidatorModel):
    Enabled: Optional[bool] = None


class MetricDimension(BaseValidatorModel):
    Name: str
    Value: str


# This class is the input for the 'delete_auto_scaling_group' function.
class DeleteAutoScalingGroupType(BaseValidatorModel):
    AutoScalingGroupName: str
    ForceDelete: Optional[bool] = None


class DeleteLifecycleHookType(BaseValidatorModel):
    LifecycleHookName: str
    AutoScalingGroupName: str


# This class is the input for the 'delete_notification_configuration' function.
class DeleteNotificationConfigurationType(BaseValidatorModel):
    AutoScalingGroupName: str
    TopicARN: str


# This class is the input for the 'delete_policy' function.
class DeletePolicyType(BaseValidatorModel):
    PolicyName: str
    AutoScalingGroupName: Optional[str] = None


# This class is the input for the 'delete_scheduled_action' function.
class DeleteScheduledActionType(BaseValidatorModel):
    AutoScalingGroupName: str
    ScheduledActionName: str


class DeleteWarmPoolType(BaseValidatorModel):
    AutoScalingGroupName: str
    ForceDelete: Optional[bool] = None


# This class is the input for the 'describe_auto_scaling_instances' function.
class DescribeAutoScalingInstancesType(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_instance_refreshes' function.
class DescribeInstanceRefreshesType(BaseValidatorModel):
    AutoScalingGroupName: str
    InstanceRefreshIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class LifecycleHook(BaseValidatorModel):
    LifecycleHookName: Optional[str] = None
    AutoScalingGroupName: Optional[str] = None
    LifecycleTransition: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    RoleARN: Optional[str] = None
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    GlobalTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None


# This class is the input for the 'describe_lifecycle_hooks' function.
class DescribeLifecycleHooksType(BaseValidatorModel):
    AutoScalingGroupName: str
    LifecycleHookNames: Optional[List[str]] = None


# This class is the input for the 'describe_load_balancer_target_groups' function.
class DescribeLoadBalancerTargetGroupsRequest(BaseValidatorModel):
    AutoScalingGroupName: str
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class LoadBalancerTargetGroupState(BaseValidatorModel):
    LoadBalancerTargetGroupARN: Optional[str] = None
    State: Optional[str] = None


# This class is the input for the 'describe_load_balancers' function.
class DescribeLoadBalancersRequest(BaseValidatorModel):
    AutoScalingGroupName: str
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class LoadBalancerState(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    State: Optional[str] = None


class MetricCollectionType(BaseValidatorModel):
    Metric: Optional[str] = None


class MetricGranularityType(BaseValidatorModel):
    Granularity: Optional[str] = None


class NotificationConfiguration(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    TopicARN: Optional[str] = None
    NotificationType: Optional[str] = None


# This class is the input for the 'describe_notification_configurations' function.
class DescribeNotificationConfigurationsType(BaseValidatorModel):
    AutoScalingGroupNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_policies' function.
class DescribePoliciesType(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    PolicyNames: Optional[List[str]] = None
    PolicyTypes: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_scaling_activities' function.
class DescribeScalingActivitiesType(BaseValidatorModel):
    ActivityIds: Optional[List[str]] = None
    AutoScalingGroupName: Optional[str] = None
    IncludeDeletedGroups: Optional[bool] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'describe_traffic_sources' function.
class DescribeTrafficSourcesRequest(BaseValidatorModel):
    AutoScalingGroupName: str
    TrafficSourceType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class TrafficSourceState(BaseValidatorModel):
    TrafficSource: Optional[str] = None
    State: Optional[str] = None
    Identifier: Optional[str] = None
    Type: Optional[str] = None


# This class is the input for the 'describe_warm_pool' function.
class DescribeWarmPoolType(BaseValidatorModel):
    AutoScalingGroupName: str
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'detach_instances' function.
class DetachInstancesQuery(BaseValidatorModel):
    AutoScalingGroupName: str
    ShouldDecrementDesiredCapacity: bool
    InstanceIds: Optional[List[str]] = None


class DetachLoadBalancerTargetGroupsType(BaseValidatorModel):
    AutoScalingGroupName: str
    TargetGroupARNs: List[str]


class DetachLoadBalancersType(BaseValidatorModel):
    AutoScalingGroupName: str
    LoadBalancerNames: List[str]


# This class is the input for the 'disable_metrics_collection' function.
class DisableMetricsCollectionQuery(BaseValidatorModel):
    AutoScalingGroupName: str
    Metrics: Optional[List[str]] = None


# This class is the input for the 'enable_metrics_collection' function.
class EnableMetricsCollectionQuery(BaseValidatorModel):
    AutoScalingGroupName: str
    Granularity: str
    Metrics: Optional[List[str]] = None


# This class is the input for the 'enter_standby' function.
class EnterStandbyQuery(BaseValidatorModel):
    AutoScalingGroupName: str
    ShouldDecrementDesiredCapacity: bool
    InstanceIds: Optional[List[str]] = None


# This class is the input for the 'execute_policy' function.
class ExecutePolicyType(BaseValidatorModel):
    PolicyName: str
    AutoScalingGroupName: Optional[str] = None
    HonorCooldown: Optional[bool] = None
    MetricValue: Optional[float] = None
    BreachThreshold: Optional[float] = None


# This class is the input for the 'exit_standby' function.
class ExitStandbyQuery(BaseValidatorModel):
    AutoScalingGroupName: str
    InstanceIds: Optional[List[str]] = None


class InstanceRefreshLivePoolProgress(BaseValidatorModel):
    PercentageComplete: Optional[int] = None
    InstancesToUpdate: Optional[int] = None


class InstanceRefreshWarmPoolProgress(BaseValidatorModel):
    PercentageComplete: Optional[int] = None
    InstancesToUpdate: Optional[int] = None


class MemoryGiBPerVCpuRequest(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class MemoryMiBRequest(BaseValidatorModel):
    Min: int
    Max: Optional[int] = None


class NetworkBandwidthGbpsRequest(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class NetworkInterfaceCountRequest(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class TotalLocalStorageGBRequest(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class VCpuCountRequest(BaseValidatorModel):
    Min: int
    Max: Optional[int] = None


class InstanceReusePolicy(BaseValidatorModel):
    ReuseOnScaleIn: Optional[bool] = None


class InstancesDistribution(BaseValidatorModel):
    OnDemandAllocationStrategy: Optional[str] = None
    OnDemandBaseCapacity: Optional[int] = None
    OnDemandPercentageAboveBaseCapacity: Optional[int] = None
    SpotAllocationStrategy: Optional[str] = None
    SpotInstancePools: Optional[int] = None
    SpotMaxPrice: Optional[str] = None


# This class is the input for the 'delete_launch_configuration' function.
class LaunchConfigurationNameType(BaseValidatorModel):
    LaunchConfigurationName: str


# This class is the input for the 'describe_launch_configurations' function.
class LaunchConfigurationNamesType(BaseValidatorModel):
    LaunchConfigurationNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class PredefinedMetricSpecification(BaseValidatorModel):
    PredefinedMetricType: MetricTypeType
    ResourceLabel: Optional[str] = None


class PredictiveScalingPredefinedLoadMetric(BaseValidatorModel):
    PredefinedMetricType: PredefinedLoadMetricTypeType
    ResourceLabel: Optional[str] = None


class PredictiveScalingPredefinedMetricPair(BaseValidatorModel):
    PredefinedMetricType: PredefinedMetricPairTypeType
    ResourceLabel: Optional[str] = None


class PredictiveScalingPredefinedScalingMetric(BaseValidatorModel):
    PredefinedMetricType: PredefinedScalingMetricTypeType
    ResourceLabel: Optional[str] = None


class ProcessType(BaseValidatorModel):
    ProcessName: str


class PutLifecycleHookType(BaseValidatorModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleTransition: Optional[str] = None
    RoleARN: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None


# This class is the input for the 'put_notification_configuration' function.
class PutNotificationConfigurationType(BaseValidatorModel):
    AutoScalingGroupName: str
    TopicARN: str
    NotificationTypes: List[str]


class StepAdjustment(BaseValidatorModel):
    ScalingAdjustment: int
    MetricIntervalLowerBound: Optional[float] = None
    MetricIntervalUpperBound: Optional[float] = None


class RecordLifecycleActionHeartbeatType(BaseValidatorModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleActionToken: Optional[str] = None
    InstanceId: Optional[str] = None


# This class is the input for the 'rollback_instance_refresh' function.
class RollbackInstanceRefreshType(BaseValidatorModel):
    AutoScalingGroupName: str


# This class is the input for the 'suspend_processes' function.
class ScalingProcessQueryRequest(BaseValidatorModel):
    AutoScalingGroupName: str
    ScalingProcesses: Optional[List[str]] = None


# This class is the input for the 'resume_processes' function.
class ScalingProcessQuery(BaseValidatorModel):
    AutoScalingGroupName: str
    ScalingProcesses: Optional[List[str]] = None


class ScheduledUpdateGroupAction(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    ScheduledActionName: Optional[str] = None
    ScheduledActionARN: Optional[str] = None
    Time: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Recurrence: Optional[str] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    TimeZone: Optional[str] = None


# This class is the input for the 'set_desired_capacity' function.
class SetDesiredCapacityType(BaseValidatorModel):
    AutoScalingGroupName: str
    DesiredCapacity: int
    HonorCooldown: Optional[bool] = None


# This class is the input for the 'set_instance_health' function.
class SetInstanceHealthQuery(BaseValidatorModel):
    InstanceId: str
    HealthStatus: str
    ShouldRespectGracePeriod: Optional[bool] = None


class SetInstanceProtectionQuery(BaseValidatorModel):
    InstanceIds: List[str]
    AutoScalingGroupName: str
    ProtectedFromScaleIn: bool


# This class is the input for the 'terminate_instance_in_auto_scaling_group' function.
class TerminateInstanceInAutoScalingGroupType(BaseValidatorModel):
    InstanceId: str
    ShouldDecrementDesiredCapacity: bool


# This class is the output for the 'describe_scaling_activities' function.
class ActivitiesType(BaseValidatorModel):
    Activities: List[Activity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'terminate_instance_in_auto_scaling_group' function.
class ActivityType(BaseValidatorModel):
    Activity: Activity
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_instance_refresh' function.
class CancelInstanceRefreshAnswer(BaseValidatorModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadata


class DescribeAccountLimitsAnswer(BaseValidatorModel):
    MaxNumberOfAutoScalingGroups: int
    MaxNumberOfLaunchConfigurations: int
    NumberOfAutoScalingGroups: int
    NumberOfLaunchConfigurations: int
    ResponseMetadata: ResponseMetadata


class DescribeAutoScalingNotificationTypesAnswer(BaseValidatorModel):
    AutoScalingNotificationTypes: List[str]
    ResponseMetadata: ResponseMetadata


class DescribeLifecycleHookTypesAnswer(BaseValidatorModel):
    LifecycleHookTypes: List[str]
    ResponseMetadata: ResponseMetadata


class DescribeTerminationPolicyTypesAnswer(BaseValidatorModel):
    TerminationPolicyTypes: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_instances' function.
class DetachInstancesAnswer(BaseValidatorModel):
    Activities: List[Activity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_auto_scaling_group' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enter_standby' function.
class EnterStandbyAnswer(BaseValidatorModel):
    Activities: List[Activity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'exit_standby' function.
class ExitStandbyAnswer(BaseValidatorModel):
    Activities: List[Activity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rollback_instance_refresh' function.
class RollbackInstanceRefreshAnswer(BaseValidatorModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_instance_refresh' function.
class StartInstanceRefreshAnswer(BaseValidatorModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadata


class DescribeAdjustmentTypesAnswer(BaseValidatorModel):
    AdjustmentTypes: List[AdjustmentType]
    ResponseMetadata: ResponseMetadata


class RefreshPreferencesOutput(BaseValidatorModel):
    MinHealthyPercentage: Optional[int] = None
    InstanceWarmup: Optional[int] = None
    CheckpointPercentages: Optional[List[int]] = None
    CheckpointDelay: Optional[int] = None
    SkipMatching: Optional[bool] = None
    AutoRollback: Optional[bool] = None
    ScaleInProtectedInstances: Optional[ScaleInProtectedInstancesType] = None
    StandbyInstances: Optional[StandbyInstancesType] = None
    AlarmSpecification: Optional[AlarmSpecificationOutput] = None
    MaxHealthyPercentage: Optional[int] = None
    BakeTime: Optional[int] = None


class RefreshPreferences(BaseValidatorModel):
    MinHealthyPercentage: Optional[int] = None
    InstanceWarmup: Optional[int] = None
    CheckpointPercentages: Optional[List[int]] = None
    CheckpointDelay: Optional[int] = None
    SkipMatching: Optional[bool] = None
    AutoRollback: Optional[bool] = None
    ScaleInProtectedInstances: Optional[ScaleInProtectedInstancesType] = None
    StandbyInstances: Optional[StandbyInstancesType] = None
    AlarmSpecification: Optional[AlarmSpecification] = None
    MaxHealthyPercentage: Optional[int] = None
    BakeTime: Optional[int] = None


# This class is the output for the 'put_scaling_policy' function.
class PolicyARNType(BaseValidatorModel):
    PolicyARN: str
    Alarms: List[Alarm]
    ResponseMetadata: ResponseMetadata


class AttachTrafficSourcesType(BaseValidatorModel):
    AutoScalingGroupName: str
    TrafficSources: List[TrafficSourceIdentifier]
    SkipZonalShiftValidation: Optional[bool] = None


class DetachTrafficSourcesType(BaseValidatorModel):
    AutoScalingGroupName: str
    TrafficSources: List[TrafficSourceIdentifier]


# This class is the input for the 'describe_auto_scaling_groups' function.
class AutoScalingGroupNamesType(BaseValidatorModel):
    AutoScalingGroupNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsType(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class AutoScalingGroupNamesTypePaginate(BaseValidatorModel):
    AutoScalingGroupNames: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAutoScalingInstancesTypePaginate(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLoadBalancerTargetGroupsRequestPaginate(BaseValidatorModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLoadBalancersRequestPaginate(BaseValidatorModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeNotificationConfigurationsTypePaginate(BaseValidatorModel):
    AutoScalingGroupNames: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePoliciesTypePaginate(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    PolicyNames: Optional[List[str]] = None
    PolicyTypes: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeScalingActivitiesTypePaginate(BaseValidatorModel):
    ActivityIds: Optional[List[str]] = None
    AutoScalingGroupName: Optional[str] = None
    IncludeDeletedGroups: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTagsTypePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeWarmPoolTypePaginate(BaseValidatorModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class LaunchConfigurationNamesTypePaginate(BaseValidatorModel):
    LaunchConfigurationNames: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class AutoScalingInstanceDetails(BaseValidatorModel):
    InstanceId: str
    AutoScalingGroupName: str
    AvailabilityZone: str
    LifecycleState: str
    HealthStatus: str
    ProtectedFromScaleIn: bool
    InstanceType: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    WeightedCapacity: Optional[str] = None


class Instance(BaseValidatorModel):
    InstanceId: str
    AvailabilityZone: str
    LifecycleState: LifecycleStateType
    HealthStatus: str
    ProtectedFromScaleIn: bool
    InstanceType: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    WeightedCapacity: Optional[str] = None


# This class is the output for the 'describe_tags' function.
class TagsType(BaseValidatorModel):
    Tags: List[TagDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'batch_delete_scheduled_action' function.
class BatchDeleteScheduledActionAnswer(BaseValidatorModel):
    FailedScheduledActions: List[FailedScheduledUpdateGroupActionRequest]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_put_scheduled_update_group_action' function.
class BatchPutScheduledUpdateGroupActionAnswer(BaseValidatorModel):
    FailedScheduledUpdateGroupActions: List[FailedScheduledUpdateGroupActionRequest]
    ResponseMetadata: ResponseMetadata


class BlockDeviceMapping(BaseValidatorModel):
    DeviceName: str
    VirtualName: Optional[str] = None
    Ebs: Optional[Ebs] = None
    NoDevice: Optional[bool] = None


class CapacityReservationSpecificationOutput(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetOutput] = None


class CapacityReservationSpecification(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTarget] = None


class CpuPerformanceFactorRequestOutput(BaseValidatorModel):
    References: Optional[List[PerformanceFactorReferenceRequest]] = None


class CpuPerformanceFactorRequest(BaseValidatorModel):
    References: Optional[List[PerformanceFactorReferenceRequest]] = None


# This class is the input for the 'create_or_update_tags' function.
class CreateOrUpdateTagsType(BaseValidatorModel):
    Tags: List[Tag]


# This class is the input for the 'delete_tags' function.
class DeleteTagsType(BaseValidatorModel):
    Tags: List[Tag]


class MetricOutput(BaseValidatorModel):
    Namespace: str
    MetricName: str
    Dimensions: Optional[List[MetricDimension]] = None


class Metric(BaseValidatorModel):
    Namespace: str
    MetricName: str
    Dimensions: Optional[List[MetricDimension]] = None


# This class is the output for the 'describe_lifecycle_hooks' function.
class DescribeLifecycleHooksAnswer(BaseValidatorModel):
    LifecycleHooks: List[LifecycleHook]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_load_balancer_target_groups' function.
class DescribeLoadBalancerTargetGroupsResponse(BaseValidatorModel):
    LoadBalancerTargetGroups: List[LoadBalancerTargetGroupState]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_load_balancers' function.
class DescribeLoadBalancersResponse(BaseValidatorModel):
    LoadBalancers: List[LoadBalancerState]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeMetricCollectionTypesAnswer(BaseValidatorModel):
    Metrics: List[MetricCollectionType]
    Granularities: List[MetricGranularityType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_notification_configurations' function.
class DescribeNotificationConfigurationsAnswer(BaseValidatorModel):
    NotificationConfigurations: List[NotificationConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeScheduledActionsTypePaginate(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    ScheduledActionNames: Optional[List[str]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_scheduled_actions' function.
class DescribeScheduledActionsType(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    ScheduledActionNames: Optional[List[str]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'get_predictive_scaling_forecast' function.
class GetPredictiveScalingForecastType(BaseValidatorModel):
    AutoScalingGroupName: str
    PolicyName: str
    StartTime: Timestamp
    EndTime: Timestamp


# This class is the input for the 'put_scheduled_update_group_action' function.
class PutScheduledUpdateGroupActionType(BaseValidatorModel):
    AutoScalingGroupName: str
    ScheduledActionName: str
    Time: Optional[Timestamp] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Recurrence: Optional[str] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    TimeZone: Optional[str] = None


class ScheduledUpdateGroupActionRequest(BaseValidatorModel):
    ScheduledActionName: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Recurrence: Optional[str] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    TimeZone: Optional[str] = None


# This class is the output for the 'describe_traffic_sources' function.
class DescribeTrafficSourcesResponse(BaseValidatorModel):
    TrafficSources: List[TrafficSourceState]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InstanceRefreshProgressDetails(BaseValidatorModel):
    LivePoolProgress: Optional[InstanceRefreshLivePoolProgress] = None
    WarmPoolProgress: Optional[InstanceRefreshWarmPoolProgress] = None


class PutWarmPoolType(BaseValidatorModel):
    AutoScalingGroupName: str
    MaxGroupPreparedCapacity: Optional[int] = None
    MinSize: Optional[int] = None
    PoolState: Optional[WarmPoolStateType] = None
    InstanceReusePolicy: Optional[InstanceReusePolicy] = None


class WarmPoolConfiguration(BaseValidatorModel):
    MaxGroupPreparedCapacity: Optional[int] = None
    MinSize: Optional[int] = None
    PoolState: Optional[WarmPoolStateType] = None
    Status: Optional[Literal['PendingDelete']] = None
    InstanceReusePolicy: Optional[InstanceReusePolicy] = None


class ProcessesType(BaseValidatorModel):
    Processes: List[ProcessType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_scheduled_actions' function.
class ScheduledActionsType(BaseValidatorModel):
    ScheduledUpdateGroupActions: List[ScheduledUpdateGroupAction]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

RefreshPreferencesUnion = Union[RefreshPreferences, RefreshPreferencesOutput]


# This class is the output for the 'describe_auto_scaling_instances' function.
class AutoScalingInstancesType(BaseValidatorModel):
    AutoScalingInstances: List[AutoScalingInstanceDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_launch_configuration' function.
class CreateLaunchConfigurationType(BaseValidatorModel):
    LaunchConfigurationName: str
    ImageId: Optional[str] = None
    KeyName: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    ClassicLinkVPCId: Optional[str] = None
    ClassicLinkVPCSecurityGroups: Optional[List[str]] = None
    UserData: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    RamdiskId: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    InstanceMonitoring: Optional[InstanceMonitoring] = None
    SpotPrice: Optional[str] = None
    IamInstanceProfile: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    PlacementTenancy: Optional[str] = None
    MetadataOptions: Optional[InstanceMetadataOptions] = None


class LaunchConfiguration(BaseValidatorModel):
    LaunchConfigurationName: str
    ImageId: str
    InstanceType: str
    CreatedTime: datetime
    LaunchConfigurationARN: Optional[str] = None
    KeyName: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    ClassicLinkVPCId: Optional[str] = None
    ClassicLinkVPCSecurityGroups: Optional[List[str]] = None
    UserData: Optional[str] = None
    KernelId: Optional[str] = None
    RamdiskId: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    InstanceMonitoring: Optional[InstanceMonitoring] = None
    SpotPrice: Optional[str] = None
    IamInstanceProfile: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    PlacementTenancy: Optional[str] = None
    MetadataOptions: Optional[InstanceMetadataOptions] = None

CapacityReservationSpecificationUnion = Union[CapacityReservationSpecification, CapacityReservationSpecificationOutput]


class BaselinePerformanceFactorsRequestOutput(BaseValidatorModel):
    Cpu: Optional[CpuPerformanceFactorRequestOutput] = None


class BaselinePerformanceFactorsRequest(BaseValidatorModel):
    Cpu: Optional[CpuPerformanceFactorRequest] = None


class MetricStatOutput(BaseValidatorModel):
    Metric: MetricOutput
    Stat: str
    Unit: Optional[str] = None


class TargetTrackingMetricStatOutput(BaseValidatorModel):
    Metric: MetricOutput
    Stat: str
    Unit: Optional[str] = None
    Period: Optional[int] = None


class MetricStat(BaseValidatorModel):
    Metric: Metric
    Stat: str
    Unit: Optional[str] = None


class TargetTrackingMetricStat(BaseValidatorModel):
    Metric: Metric
    Stat: str
    Unit: Optional[str] = None
    Period: Optional[int] = None


# This class is the input for the 'batch_put_scheduled_update_group_action' function.
class BatchPutScheduledUpdateGroupActionType(BaseValidatorModel):
    AutoScalingGroupName: str
    ScheduledUpdateGroupActions: List[ScheduledUpdateGroupActionRequest]


class RollbackDetails(BaseValidatorModel):
    RollbackReason: Optional[str] = None
    RollbackStartTime: Optional[datetime] = None
    PercentageCompleteOnRollback: Optional[int] = None
    InstancesToUpdateOnRollback: Optional[int] = None
    ProgressDetailsOnRollback: Optional[InstanceRefreshProgressDetails] = None


# This class is the output for the 'describe_warm_pool' function.
class DescribeWarmPoolAnswer(BaseValidatorModel):
    WarmPoolConfiguration: WarmPoolConfiguration
    Instances: List[Instance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_launch_configurations' function.
class LaunchConfigurationsType(BaseValidatorModel):
    LaunchConfigurations: List[LaunchConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InstanceRequirementsOutput(BaseValidatorModel):
    VCpuCount: VCpuCountRequest
    MemoryMiB: MemoryMiBRequest
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuRequest] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountRequest] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBRequest] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsRequest] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountRequest] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRequest] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsRequest] = None
    AllowedInstanceTypes: Optional[List[str]] = None
    BaselinePerformanceFactors: Optional[BaselinePerformanceFactorsRequestOutput] = None


class InstanceRequirements(BaseValidatorModel):
    VCpuCount: VCpuCountRequest
    MemoryMiB: MemoryMiBRequest
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuRequest] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountRequest] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBRequest] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsRequest] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountRequest] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRequest] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsRequest] = None
    AllowedInstanceTypes: Optional[List[str]] = None
    BaselinePerformanceFactors: Optional[BaselinePerformanceFactorsRequest] = None


class MetricDataQueryOutput(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[MetricStatOutput] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None


class TargetTrackingMetricDataQueryOutput(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatOutput] = None
    Label: Optional[str] = None
    Period: Optional[int] = None
    ReturnData: Optional[bool] = None


class MetricDataQuery(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[MetricStat] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None


class TargetTrackingMetricDataQuery(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStat] = None
    Label: Optional[str] = None
    Period: Optional[int] = None
    ReturnData: Optional[bool] = None


class LaunchTemplateOverridesOutput(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecification] = None
    InstanceRequirements: Optional[InstanceRequirementsOutput] = None


class LaunchTemplateOverrides(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecification] = None
    InstanceRequirements: Optional[InstanceRequirements] = None


class PredictiveScalingCustomizedCapacityMetricOutput(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutput]


class PredictiveScalingCustomizedLoadMetricOutput(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutput]


class PredictiveScalingCustomizedScalingMetricOutput(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutput]


class CustomizedMetricSpecificationOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimension]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Period: Optional[int] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryOutput]] = None


class PredictiveScalingCustomizedCapacityMetric(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQuery]


class PredictiveScalingCustomizedLoadMetric(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQuery]


class PredictiveScalingCustomizedScalingMetric(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQuery]


class CustomizedMetricSpecification(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimension]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Period: Optional[int] = None
    Metrics: Optional[List[TargetTrackingMetricDataQuery]] = None


class LaunchTemplateOutput(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecification] = None
    Overrides: Optional[List[LaunchTemplateOverridesOutput]] = None


class LaunchTemplate(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecification] = None
    Overrides: Optional[List[LaunchTemplateOverrides]] = None


class PredictiveScalingMetricSpecificationOutput(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[PredictiveScalingPredefinedMetricPair] = None
    PredefinedScalingMetricSpecification: Optional[PredictiveScalingPredefinedScalingMetric] = None
    PredefinedLoadMetricSpecification: Optional[PredictiveScalingPredefinedLoadMetric] = None
    CustomizedScalingMetricSpecification: Optional[PredictiveScalingCustomizedScalingMetricOutput] = None
    CustomizedLoadMetricSpecification: Optional[PredictiveScalingCustomizedLoadMetricOutput] = None
    CustomizedCapacityMetricSpecification: Optional[PredictiveScalingCustomizedCapacityMetricOutput] = None


class TargetTrackingConfigurationOutput(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecification] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationOutput] = None
    DisableScaleIn: Optional[bool] = None


class PredictiveScalingMetricSpecification(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[PredictiveScalingPredefinedMetricPair] = None
    PredefinedScalingMetricSpecification: Optional[PredictiveScalingPredefinedScalingMetric] = None
    PredefinedLoadMetricSpecification: Optional[PredictiveScalingPredefinedLoadMetric] = None
    CustomizedScalingMetricSpecification: Optional[PredictiveScalingCustomizedScalingMetric] = None
    CustomizedLoadMetricSpecification: Optional[PredictiveScalingCustomizedLoadMetric] = None
    CustomizedCapacityMetricSpecification: Optional[PredictiveScalingCustomizedCapacityMetric] = None


class TargetTrackingConfiguration(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecification] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecification] = None
    DisableScaleIn: Optional[bool] = None


class MixedInstancesPolicyOutput(BaseValidatorModel):
    LaunchTemplate: Optional[LaunchTemplateOutput] = None
    InstancesDistribution: Optional[InstancesDistribution] = None


class MixedInstancesPolicy(BaseValidatorModel):
    LaunchTemplate: Optional[LaunchTemplate] = None
    InstancesDistribution: Optional[InstancesDistribution] = None


class LoadForecast(BaseValidatorModel):
    Timestamps: List[datetime]
    Values: List[float]
    MetricSpecification: PredictiveScalingMetricSpecificationOutput


class PredictiveScalingConfigurationOutput(BaseValidatorModel):
    MetricSpecifications: List[PredictiveScalingMetricSpecificationOutput]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None


class PredictiveScalingConfiguration(BaseValidatorModel):
    MetricSpecifications: List[PredictiveScalingMetricSpecification]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None

TargetTrackingConfigurationUnion = Union[TargetTrackingConfiguration, TargetTrackingConfigurationOutput]


class AutoScalingGroup(BaseValidatorModel):
    AutoScalingGroupName: str
    MinSize: int
    MaxSize: int
    DesiredCapacity: int
    DefaultCooldown: int
    AvailabilityZones: List[str]
    HealthCheckType: str
    CreatedTime: datetime
    AutoScalingGroupARN: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyOutput] = None
    PredictedCapacity: Optional[int] = None
    LoadBalancerNames: Optional[List[str]] = None
    TargetGroupARNs: Optional[List[str]] = None
    HealthCheckGracePeriod: Optional[int] = None
    Instances: Optional[List[Instance]] = None
    SuspendedProcesses: Optional[List[SuspendedProcess]] = None
    PlacementGroup: Optional[str] = None
    VPCZoneIdentifier: Optional[str] = None
    EnabledMetrics: Optional[List[EnabledMetric]] = None
    Status: Optional[str] = None
    Tags: Optional[List[TagDescription]] = None
    TerminationPolicies: Optional[List[str]] = None
    NewInstancesProtectedFromScaleIn: Optional[bool] = None
    ServiceLinkedRoleARN: Optional[str] = None
    MaxInstanceLifetime: Optional[int] = None
    CapacityRebalance: Optional[bool] = None
    WarmPoolConfiguration: Optional[WarmPoolConfiguration] = None
    WarmPoolSize: Optional[int] = None
    Context: Optional[str] = None
    DesiredCapacityType: Optional[str] = None
    DefaultInstanceWarmup: Optional[int] = None
    TrafficSources: Optional[List[TrafficSourceIdentifier]] = None
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicy] = None
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistribution] = None
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicy] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationOutput] = None


class DesiredConfigurationOutput(BaseValidatorModel):
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyOutput] = None


class DesiredConfiguration(BaseValidatorModel):
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicy] = None

MixedInstancesPolicyUnion = Union[MixedInstancesPolicy, MixedInstancesPolicyOutput]


# This class is the output for the 'get_predictive_scaling_forecast' function.
class GetPredictiveScalingForecastAnswer(BaseValidatorModel):
    LoadForecast: List[LoadForecast]
    CapacityForecast: CapacityForecast
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class ScalingPolicy(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyARN: Optional[str] = None
    PolicyType: Optional[str] = None
    AdjustmentType: Optional[str] = None
    MinAdjustmentStep: Optional[int] = None
    MinAdjustmentMagnitude: Optional[int] = None
    ScalingAdjustment: Optional[int] = None
    Cooldown: Optional[int] = None
    StepAdjustments: Optional[List[StepAdjustment]] = None
    MetricAggregationType: Optional[str] = None
    EstimatedInstanceWarmup: Optional[int] = None
    Alarms: Optional[List[Alarm]] = None
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationOutput] = None
    Enabled: Optional[bool] = None
    PredictiveScalingConfiguration: Optional[PredictiveScalingConfigurationOutput] = None

PredictiveScalingConfigurationUnion = Union[PredictiveScalingConfiguration, PredictiveScalingConfigurationOutput]


# This class is the output for the 'describe_auto_scaling_groups' function.
class AutoScalingGroupsType(BaseValidatorModel):
    AutoScalingGroups: List[AutoScalingGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InstanceRefresh(BaseValidatorModel):
    InstanceRefreshId: Optional[str] = None
    AutoScalingGroupName: Optional[str] = None
    Status: Optional[InstanceRefreshStatusType] = None
    StatusReason: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    PercentageComplete: Optional[int] = None
    InstancesToUpdate: Optional[int] = None
    ProgressDetails: Optional[InstanceRefreshProgressDetails] = None
    Preferences: Optional[RefreshPreferencesOutput] = None
    DesiredConfiguration: Optional[DesiredConfigurationOutput] = None
    RollbackDetails: Optional[RollbackDetails] = None

DesiredConfigurationUnion = Union[DesiredConfiguration, DesiredConfigurationOutput]


# This class is the input for the 'create_auto_scaling_group' function.
class CreateAutoScalingGroupType(BaseValidatorModel):
    AutoScalingGroupName: str
    MinSize: int
    MaxSize: int
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyUnion] = None
    InstanceId: Optional[str] = None
    DesiredCapacity: Optional[int] = None
    DefaultCooldown: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    LoadBalancerNames: Optional[List[str]] = None
    TargetGroupARNs: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    PlacementGroup: Optional[str] = None
    VPCZoneIdentifier: Optional[str] = None
    TerminationPolicies: Optional[List[str]] = None
    NewInstancesProtectedFromScaleIn: Optional[bool] = None
    CapacityRebalance: Optional[bool] = None
    LifecycleHookSpecificationList: Optional[List[LifecycleHookSpecification]] = None
    Tags: Optional[List[Tag]] = None
    ServiceLinkedRoleARN: Optional[str] = None
    MaxInstanceLifetime: Optional[int] = None
    Context: Optional[str] = None
    DesiredCapacityType: Optional[str] = None
    DefaultInstanceWarmup: Optional[int] = None
    TrafficSources: Optional[List[TrafficSourceIdentifier]] = None
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicy] = None
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistribution] = None
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicy] = None
    SkipZonalShiftValidation: Optional[bool] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationUnion] = None


# This class is the input for the 'update_auto_scaling_group' function.
class UpdateAutoScalingGroupType(BaseValidatorModel):
    AutoScalingGroupName: str
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyUnion] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    DefaultCooldown: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    PlacementGroup: Optional[str] = None
    VPCZoneIdentifier: Optional[str] = None
    TerminationPolicies: Optional[List[str]] = None
    NewInstancesProtectedFromScaleIn: Optional[bool] = None
    ServiceLinkedRoleARN: Optional[str] = None
    MaxInstanceLifetime: Optional[int] = None
    CapacityRebalance: Optional[bool] = None
    Context: Optional[str] = None
    DesiredCapacityType: Optional[str] = None
    DefaultInstanceWarmup: Optional[int] = None
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicy] = None
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistribution] = None
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicy] = None
    SkipZonalShiftValidation: Optional[bool] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationUnion] = None


# This class is the output for the 'describe_policies' function.
class PoliciesType(BaseValidatorModel):
    ScalingPolicies: List[ScalingPolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'put_scaling_policy' function.
class PutScalingPolicyType(BaseValidatorModel):
    AutoScalingGroupName: str
    PolicyName: str
    PolicyType: Optional[str] = None
    AdjustmentType: Optional[str] = None
    MinAdjustmentStep: Optional[int] = None
    MinAdjustmentMagnitude: Optional[int] = None
    ScalingAdjustment: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[str] = None
    StepAdjustments: Optional[List[StepAdjustment]] = None
    EstimatedInstanceWarmup: Optional[int] = None
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationUnion] = None
    Enabled: Optional[bool] = None
    PredictiveScalingConfiguration: Optional[PredictiveScalingConfigurationUnion] = None


# This class is the output for the 'describe_instance_refreshes' function.
class DescribeInstanceRefreshesAnswer(BaseValidatorModel):
    InstanceRefreshes: List[InstanceRefresh]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'start_instance_refresh' function.
class StartInstanceRefreshType(BaseValidatorModel):
    AutoScalingGroupName: str
    Strategy: Optional[Literal['Rolling']] = None
    DesiredConfiguration: Optional[DesiredConfigurationUnion] = None
    Preferences: Optional[RefreshPreferencesUnion] = None
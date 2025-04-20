from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.application_autoscaling.application_autoscaling_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Alarm(BaseValidatorModel):
    AlarmName: str
    AlarmARN: str


class CapacityForecast(BaseValidatorModel):
    Timestamps: List[datetime]
    Values: List[float]


class MetricDimension(BaseValidatorModel):
    Name: str
    Value: str


class DeleteScalingPolicyRequest(BaseValidatorModel):
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType


class DeleteScheduledActionRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionName: str
    ResourceId: str
    ScalableDimension: ScalableDimensionType


class DeregisterScalableTargetRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeScalableTargetsRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceIds: Optional[List[str]] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeScalingActivitiesRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeNotScaledActivities: Optional[bool] = None


class DescribeScalingPoliciesRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    PolicyNames: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeScheduledActionsRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionNames: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

Timestamp = Union[datetime, str]


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class NotScaledReason(BaseValidatorModel):
    Code: str
    MaxCapacity: Optional[int] = None
    MinCapacity: Optional[int] = None
    CurrentCapacity: Optional[int] = None


class PredefinedMetricSpecification(BaseValidatorModel):
    PredefinedMetricType: MetricTypeType
    ResourceLabel: Optional[str] = None


class PredictiveScalingMetricDimension(BaseValidatorModel):
    Name: str
    Value: str


class PredictiveScalingPredefinedLoadMetricSpecification(BaseValidatorModel):
    PredefinedMetricType: str
    ResourceLabel: Optional[str] = None


class PredictiveScalingPredefinedMetricPairSpecification(BaseValidatorModel):
    PredefinedMetricType: str
    ResourceLabel: Optional[str] = None


class PredictiveScalingPredefinedScalingMetricSpecification(BaseValidatorModel):
    PredefinedMetricType: str
    ResourceLabel: Optional[str] = None


class ScalableTargetAction(BaseValidatorModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None


class SuspendedState(BaseValidatorModel):
    DynamicScalingInSuspended: Optional[bool] = None
    DynamicScalingOutSuspended: Optional[bool] = None
    ScheduledScalingSuspended: Optional[bool] = None


class StepAdjustment(BaseValidatorModel):
    ScalingAdjustment: int
    MetricIntervalLowerBound: Optional[float] = None
    MetricIntervalUpperBound: Optional[float] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Dict[str, str]


class TargetTrackingMetricDimension(BaseValidatorModel):
    Name: str
    Value: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class DescribeScalableTargetsRequestPaginate(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceIds: Optional[List[str]] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeScalingActivitiesRequestPaginate(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    IncludeNotScaledActivities: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeScalingPoliciesRequestPaginate(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    PolicyNames: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeScheduledActionsRequestPaginate(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionNames: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutScalingPolicyResponse(BaseValidatorModel):
    PolicyARN: str
    Alarms: List[Alarm]
    ResponseMetadata: ResponseMetadata


class RegisterScalableTargetResponse(BaseValidatorModel):
    ScalableTargetARN: str
    ResponseMetadata: ResponseMetadata


class GetPredictiveScalingForecastRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyName: str
    StartTime: Timestamp
    EndTime: Timestamp


class ScalingActivity(BaseValidatorModel):
    ActivityId: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    Description: str
    Cause: str
    StartTime: datetime
    StatusCode: ScalingActivityStatusCodeType
    EndTime: Optional[datetime] = None
    StatusMessage: Optional[str] = None
    Details: Optional[str] = None
    NotScaledReasons: Optional[List[NotScaledReason]] = None


class PredictiveScalingMetricOutput(BaseValidatorModel):
    Dimensions: Optional[List[PredictiveScalingMetricDimension]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None


class PredictiveScalingMetric(BaseValidatorModel):
    Dimensions: Optional[List[PredictiveScalingMetricDimension]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None


class PutScheduledActionRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionName: str
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    Schedule: Optional[str] = None
    Timezone: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    ScalableTargetAction: Optional[ScalableTargetAction] = None


class ScheduledAction(BaseValidatorModel):
    ScheduledActionName: str
    ScheduledActionARN: str
    ServiceNamespace: ServiceNamespaceType
    Schedule: str
    ResourceId: str
    CreationTime: datetime
    Timezone: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ScalableTargetAction: Optional[ScalableTargetAction] = None


class RegisterScalableTargetRequest(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    RoleARN: Optional[str] = None
    SuspendedState: Optional[SuspendedState] = None
    Tags: Optional[Dict[str, str]] = None


class ScalableTarget(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    RoleARN: str
    CreationTime: datetime
    PredictedCapacity: Optional[int] = None
    SuspendedState: Optional[SuspendedState] = None
    ScalableTargetARN: Optional[str] = None


class StepScalingPolicyConfigurationOutput(BaseValidatorModel):
    AdjustmentType: Optional[AdjustmentTypeType] = None
    StepAdjustments: Optional[List[StepAdjustment]] = None
    MinAdjustmentMagnitude: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[MetricAggregationTypeType] = None


class StepScalingPolicyConfiguration(BaseValidatorModel):
    AdjustmentType: Optional[AdjustmentTypeType] = None
    StepAdjustments: Optional[List[StepAdjustment]] = None
    MinAdjustmentMagnitude: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[MetricAggregationTypeType] = None


class TargetTrackingMetricOutput(BaseValidatorModel):
    Dimensions: Optional[List[TargetTrackingMetricDimension]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None


class TargetTrackingMetric(BaseValidatorModel):
    Dimensions: Optional[List[TargetTrackingMetricDimension]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None


class DescribeScalingActivitiesResponse(BaseValidatorModel):
    ScalingActivities: List[ScalingActivity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PredictiveScalingMetricStatOutput(BaseValidatorModel):
    Metric: PredictiveScalingMetricOutput
    Stat: str
    Unit: Optional[str] = None


class PredictiveScalingMetricStat(BaseValidatorModel):
    Metric: PredictiveScalingMetric
    Stat: str
    Unit: Optional[str] = None


class DescribeScheduledActionsResponse(BaseValidatorModel):
    ScheduledActions: List[ScheduledAction]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeScalableTargetsResponse(BaseValidatorModel):
    ScalableTargets: List[ScalableTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

StepScalingPolicyConfigurationUnion = Union[StepScalingPolicyConfiguration, StepScalingPolicyConfigurationOutput]


class TargetTrackingMetricStatOutput(BaseValidatorModel):
    Metric: TargetTrackingMetricOutput
    Stat: str
    Unit: Optional[str] = None


class TargetTrackingMetricStat(BaseValidatorModel):
    Metric: TargetTrackingMetric
    Stat: str
    Unit: Optional[str] = None


class PredictiveScalingMetricDataQueryOutput(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[PredictiveScalingMetricStatOutput] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None


class PredictiveScalingMetricDataQuery(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[PredictiveScalingMetricStat] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None


class TargetTrackingMetricDataQueryOutput(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    Label: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatOutput] = None
    ReturnData: Optional[bool] = None


class TargetTrackingMetricDataQuery(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    Label: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStat] = None
    ReturnData: Optional[bool] = None


class PredictiveScalingCustomizedMetricSpecificationOutput(BaseValidatorModel):
    MetricDataQueries: List[PredictiveScalingMetricDataQueryOutput]


class PredictiveScalingCustomizedMetricSpecification(BaseValidatorModel):
    MetricDataQueries: List[PredictiveScalingMetricDataQuery]


class CustomizedMetricSpecificationOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimension]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryOutput]] = None


class CustomizedMetricSpecification(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimension]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[List[TargetTrackingMetricDataQuery]] = None


class PredictiveScalingMetricSpecificationOutput(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[PredictiveScalingPredefinedMetricPairSpecification] = None
    PredefinedScalingMetricSpecification: Optional[PredictiveScalingPredefinedScalingMetricSpecification] = None
    PredefinedLoadMetricSpecification: Optional[PredictiveScalingPredefinedLoadMetricSpecification] = None
    CustomizedScalingMetricSpecification: Optional[PredictiveScalingCustomizedMetricSpecificationOutput] = None
    CustomizedLoadMetricSpecification: Optional[PredictiveScalingCustomizedMetricSpecificationOutput] = None
    CustomizedCapacityMetricSpecification: Optional[PredictiveScalingCustomizedMetricSpecificationOutput] = None


class PredictiveScalingMetricSpecification(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[PredictiveScalingPredefinedMetricPairSpecification] = None
    PredefinedScalingMetricSpecification: Optional[PredictiveScalingPredefinedScalingMetricSpecification] = None
    PredefinedLoadMetricSpecification: Optional[PredictiveScalingPredefinedLoadMetricSpecification] = None
    CustomizedScalingMetricSpecification: Optional[PredictiveScalingCustomizedMetricSpecification] = None
    CustomizedLoadMetricSpecification: Optional[PredictiveScalingCustomizedMetricSpecification] = None
    CustomizedCapacityMetricSpecification: Optional[PredictiveScalingCustomizedMetricSpecification] = None


class TargetTrackingScalingPolicyConfigurationOutput(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecification] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationOutput] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    DisableScaleIn: Optional[bool] = None


class TargetTrackingScalingPolicyConfiguration(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecification] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecification] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    DisableScaleIn: Optional[bool] = None


class LoadForecast(BaseValidatorModel):
    Timestamps: List[datetime]
    Values: List[float]
    MetricSpecification: PredictiveScalingMetricSpecificationOutput


class PredictiveScalingPolicyConfigurationOutput(BaseValidatorModel):
    MetricSpecifications: List[PredictiveScalingMetricSpecificationOutput]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None


class PredictiveScalingPolicyConfiguration(BaseValidatorModel):
    MetricSpecifications: List[PredictiveScalingMetricSpecification]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None

TargetTrackingScalingPolicyConfigurationUnion = Union[TargetTrackingScalingPolicyConfiguration, TargetTrackingScalingPolicyConfigurationOutput]


class GetPredictiveScalingForecastResponse(BaseValidatorModel):
    LoadForecast: List[LoadForecast]
    CapacityForecast: CapacityForecast
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class ScalingPolicy(BaseValidatorModel):
    PolicyARN: str
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyType: PolicyTypeType
    CreationTime: datetime
    StepScalingPolicyConfiguration: Optional[StepScalingPolicyConfigurationOutput] = None
    TargetTrackingScalingPolicyConfiguration: Optional[TargetTrackingScalingPolicyConfigurationOutput] = None
    PredictiveScalingPolicyConfiguration: Optional[PredictiveScalingPolicyConfigurationOutput] = None
    Alarms: Optional[List[Alarm]] = None

PredictiveScalingPolicyConfigurationUnion = Union[PredictiveScalingPolicyConfiguration, PredictiveScalingPolicyConfigurationOutput]


class DescribeScalingPoliciesResponse(BaseValidatorModel):
    ScalingPolicies: List[ScalingPolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutScalingPolicyRequest(BaseValidatorModel):
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyType: Optional[PolicyTypeType] = None
    StepScalingPolicyConfiguration: Optional[StepScalingPolicyConfigurationUnion] = None
    TargetTrackingScalingPolicyConfiguration: Optional[TargetTrackingScalingPolicyConfigurationUnion] = None
    PredictiveScalingPolicyConfiguration: Optional[PredictiveScalingPolicyConfigurationUnion] = None
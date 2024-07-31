from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.application_autoscaling_constants import *

class AlarmTypeDef(BaseModel):
    AlarmName: str
    AlarmARN: str

class MetricDimensionTypeDef(BaseModel):
    Name: str
    Value: str

class DeleteScalingPolicyRequestRequestTypeDef(BaseModel):
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class DeleteScheduledActionRequestRequestTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionName: str
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class DeregisterScalableTargetRequestRequestTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeScalableTargetsRequestRequestTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceIds: Optional[Sequence[str]] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DescribeScalingActivitiesRequestRequestTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeNotScaledActivities: Optional[bool] = None

class DescribeScalingPoliciesRequestRequestTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    PolicyNames: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeScheduledActionsRequestRequestTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionNames: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class NotScaledReasonTypeDef(BaseModel):
    Code: str
    MaxCapacity: Optional[int] = None
    MinCapacity: Optional[int] = None
    CurrentCapacity: Optional[int] = None

class PredefinedMetricSpecificationTypeDef(BaseModel):
    PredefinedMetricType: MetricTypeType
    ResourceLabel: Optional[str] = None

class ScalableTargetActionTypeDef(BaseModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None

class SuspendedStateTypeDef(BaseModel):
    DynamicScalingInSuspended: Optional[bool] = None
    DynamicScalingOutSuspended: Optional[bool] = None
    ScheduledScalingSuspended: Optional[bool] = None

class StepAdjustmentTypeDef(BaseModel):
    ScalingAdjustment: int
    MetricIntervalLowerBound: Optional[float] = None
    MetricIntervalUpperBound: Optional[float] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Mapping[str, str]

class TargetTrackingMetricDimensionTypeDef(BaseModel):
    Name: str
    Value: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class DescribeScalableTargetsRequestDescribeScalableTargetsPaginateTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceIds: Optional[Sequence[str]] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingActivitiesRequestDescribeScalingActivitiesPaginateTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    IncludeNotScaledActivities: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingPoliciesRequestDescribeScalingPoliciesPaginateTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    PolicyNames: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledActionsRequestDescribeScheduledActionsPaginateTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionNames: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutScalingPolicyResponseTypeDef(BaseModel):
    PolicyARN: str
    Alarms: List[AlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterScalableTargetResponseTypeDef(BaseModel):
    ScalableTargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScalingActivityTypeDef(BaseModel):
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
    NotScaledReasons: Optional[List[NotScaledReasonTypeDef]] = None

class ScheduledActionTypeDef(BaseModel):
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
    ScalableTargetAction: Optional[ScalableTargetActionTypeDef] = None

class PutScheduledActionRequestRequestTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionName: str
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    Schedule: Optional[str] = None
    Timezone: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    ScalableTargetAction: Optional[ScalableTargetActionTypeDef] = None

class RegisterScalableTargetRequestRequestTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    RoleARN: Optional[str] = None
    SuspendedState: Optional[SuspendedStateTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class ScalableTargetTypeDef(BaseModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    RoleARN: str
    CreationTime: datetime
    SuspendedState: Optional[SuspendedStateTypeDef] = None
    ScalableTargetARN: Optional[str] = None

class StepScalingPolicyConfigurationExtraOutputTypeDef(BaseModel):
    AdjustmentType: Optional[AdjustmentTypeType] = None
    StepAdjustments: Optional[List[StepAdjustmentTypeDef]] = None
    MinAdjustmentMagnitude: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[MetricAggregationTypeType] = None

class StepScalingPolicyConfigurationOutputTypeDef(BaseModel):
    AdjustmentType: Optional[AdjustmentTypeType] = None
    StepAdjustments: Optional[List[StepAdjustmentTypeDef]] = None
    MinAdjustmentMagnitude: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[MetricAggregationTypeType] = None

class StepScalingPolicyConfigurationTypeDef(BaseModel):
    AdjustmentType: Optional[AdjustmentTypeType] = None
    StepAdjustments: Optional[Sequence[StepAdjustmentTypeDef]] = None
    MinAdjustmentMagnitude: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[MetricAggregationTypeType] = None

class TargetTrackingMetricExtraOutputTypeDef(BaseModel):
    Dimensions: Optional[List[TargetTrackingMetricDimensionTypeDef]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None

class TargetTrackingMetricOutputTypeDef(BaseModel):
    Dimensions: Optional[List[TargetTrackingMetricDimensionTypeDef]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None

class TargetTrackingMetricTypeDef(BaseModel):
    Dimensions: Optional[Sequence[TargetTrackingMetricDimensionTypeDef]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None

class DescribeScalingActivitiesResponseTypeDef(BaseModel):
    ScalingActivities: List[ScalingActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeScheduledActionsResponseTypeDef(BaseModel):
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeScalableTargetsResponseTypeDef(BaseModel):
    ScalableTargets: List[ScalableTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TargetTrackingMetricStatExtraOutputTypeDef(BaseModel):
    Metric: TargetTrackingMetricExtraOutputTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricStatOutputTypeDef(BaseModel):
    Metric: TargetTrackingMetricOutputTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricStatTypeDef(BaseModel):
    Metric: TargetTrackingMetricTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricDataQueryExtraOutputTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    Label: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatExtraOutputTypeDef] = None
    ReturnData: Optional[bool] = None

class TargetTrackingMetricDataQueryOutputTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    Label: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatOutputTypeDef] = None
    ReturnData: Optional[bool] = None

class TargetTrackingMetricDataQueryTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    Label: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatTypeDef] = None
    ReturnData: Optional[bool] = None

class CustomizedMetricSpecificationExtraOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryExtraOutputTypeDef]] = None

class CustomizedMetricSpecificationOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryOutputTypeDef]] = None

class CustomizedMetricSpecificationTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[Sequence[TargetTrackingMetricDataQueryTypeDef]] = None

class TargetTrackingScalingPolicyConfigurationExtraOutputTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[       CustomizedMetricSpecificationExtraOutputTypeDef     ] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    DisableScaleIn: Optional[bool] = None

class TargetTrackingScalingPolicyConfigurationOutputTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationOutputTypeDef] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    DisableScaleIn: Optional[bool] = None

class TargetTrackingScalingPolicyConfigurationTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationTypeDef] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    DisableScaleIn: Optional[bool] = None

class ScalingPolicyTypeDef(BaseModel):
    PolicyARN: str
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyType: PolicyTypeType
    CreationTime: datetime
    StepScalingPolicyConfiguration: Optional[StepScalingPolicyConfigurationOutputTypeDef] = None
    TargetTrackingScalingPolicyConfiguration: Optional[       TargetTrackingScalingPolicyConfigurationOutputTypeDef     ] = None
    Alarms: Optional[List[AlarmTypeDef]] = None

class PutScalingPolicyRequestRequestTypeDef(BaseModel):
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyType: Optional[PolicyTypeType] = None
    StepScalingPolicyConfiguration: Optional[StepScalingPolicyConfigurationTypeDef] = None
    TargetTrackingScalingPolicyConfiguration: Optional[       TargetTrackingScalingPolicyConfigurationTypeDef     ] = None

class DescribeScalingPoliciesResponseTypeDef(BaseModel):
    ScalingPolicies: List[ScalingPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AlarmTypeDef(BaseValidatorModel):
    AlarmName: str
    AlarmARN: str

class MetricDimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class DeleteScalingPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class DeleteScheduledActionRequestRequestTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionName: str
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class DeregisterScalableTargetRequestRequestTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeScalableTargetsRequestRequestTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceIds: Optional[Sequence[str]] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DescribeScalingActivitiesRequestRequestTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeNotScaledActivities: Optional[bool] = None

class DescribeScalingPoliciesRequestRequestTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    PolicyNames: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeScheduledActionsRequestRequestTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionNames: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class NotScaledReasonTypeDef(BaseValidatorModel):
    Code: str
    MaxCapacity: Optional[int] = None
    MinCapacity: Optional[int] = None
    CurrentCapacity: Optional[int] = None

class PredefinedMetricSpecificationTypeDef(BaseValidatorModel):
    PredefinedMetricType: MetricTypeType
    ResourceLabel: Optional[str] = None

class ScalableTargetActionTypeDef(BaseValidatorModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None

class SuspendedStateTypeDef(BaseValidatorModel):
    DynamicScalingInSuspended: Optional[bool] = None
    DynamicScalingOutSuspended: Optional[bool] = None
    ScheduledScalingSuspended: Optional[bool] = None

class StepAdjustmentTypeDef(BaseValidatorModel):
    ScalingAdjustment: int
    MetricIntervalLowerBound: Optional[float] = None
    MetricIntervalUpperBound: Optional[float] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Mapping[str, str]

class TargetTrackingMetricDimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class DescribeScalableTargetsRequestDescribeScalableTargetsPaginateTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceIds: Optional[Sequence[str]] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingActivitiesRequestDescribeScalingActivitiesPaginateTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    IncludeNotScaledActivities: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingPoliciesRequestDescribeScalingPoliciesPaginateTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    PolicyNames: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledActionsRequestDescribeScheduledActionsPaginateTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionNames: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    ScalableDimension: Optional[ScalableDimensionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutScalingPolicyResponseTypeDef(BaseValidatorModel):
    PolicyARN: str
    Alarms: List[AlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterScalableTargetResponseTypeDef(BaseValidatorModel):
    ScalableTargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScalingActivityTypeDef(BaseValidatorModel):
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

class ScheduledActionTypeDef(BaseValidatorModel):
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

class PutScheduledActionRequestRequestTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ScheduledActionName: str
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    Schedule: Optional[str] = None
    Timezone: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    ScalableTargetAction: Optional[ScalableTargetActionTypeDef] = None

class RegisterScalableTargetRequestRequestTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    RoleARN: Optional[str] = None
    SuspendedState: Optional[SuspendedStateTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class ScalableTargetTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    RoleARN: str
    CreationTime: datetime
    SuspendedState: Optional[SuspendedStateTypeDef] = None
    ScalableTargetARN: Optional[str] = None

class StepScalingPolicyConfigurationExtraOutputTypeDef(BaseValidatorModel):
    AdjustmentType: Optional[AdjustmentTypeType] = None
    StepAdjustments: Optional[List[StepAdjustmentTypeDef]] = None
    MinAdjustmentMagnitude: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[MetricAggregationTypeType] = None

class StepScalingPolicyConfigurationOutputTypeDef(BaseValidatorModel):
    AdjustmentType: Optional[AdjustmentTypeType] = None
    StepAdjustments: Optional[List[StepAdjustmentTypeDef]] = None
    MinAdjustmentMagnitude: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[MetricAggregationTypeType] = None

class StepScalingPolicyConfigurationTypeDef(BaseValidatorModel):
    AdjustmentType: Optional[AdjustmentTypeType] = None
    StepAdjustments: Optional[Sequence[StepAdjustmentTypeDef]] = None
    MinAdjustmentMagnitude: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[MetricAggregationTypeType] = None

class TargetTrackingMetricExtraOutputTypeDef(BaseValidatorModel):
    Dimensions: Optional[List[TargetTrackingMetricDimensionTypeDef]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None

class TargetTrackingMetricOutputTypeDef(BaseValidatorModel):
    Dimensions: Optional[List[TargetTrackingMetricDimensionTypeDef]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None

class TargetTrackingMetricTypeDef(BaseValidatorModel):
    Dimensions: Optional[Sequence[TargetTrackingMetricDimensionTypeDef]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None

class DescribeScalingActivitiesResponseTypeDef(BaseValidatorModel):
    ScalingActivities: List[ScalingActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeScheduledActionsResponseTypeDef(BaseValidatorModel):
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeScalableTargetsResponseTypeDef(BaseValidatorModel):
    ScalableTargets: List[ScalableTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TargetTrackingMetricStatExtraOutputTypeDef(BaseValidatorModel):
    Metric: TargetTrackingMetricExtraOutputTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricStatOutputTypeDef(BaseValidatorModel):
    Metric: TargetTrackingMetricOutputTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricStatTypeDef(BaseValidatorModel):
    Metric: TargetTrackingMetricTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricDataQueryExtraOutputTypeDef(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    Label: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatExtraOutputTypeDef] = None
    ReturnData: Optional[bool] = None

class TargetTrackingMetricDataQueryOutputTypeDef(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    Label: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatOutputTypeDef] = None
    ReturnData: Optional[bool] = None

class TargetTrackingMetricDataQueryTypeDef(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    Label: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatTypeDef] = None
    ReturnData: Optional[bool] = None

class CustomizedMetricSpecificationExtraOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryExtraOutputTypeDef]] = None

class CustomizedMetricSpecificationOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryOutputTypeDef]] = None

class CustomizedMetricSpecificationTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[Sequence[TargetTrackingMetricDataQueryTypeDef]] = None

class TargetTrackingScalingPolicyConfigurationExtraOutputTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[       CustomizedMetricSpecificationExtraOutputTypeDef     ] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    DisableScaleIn: Optional[bool] = None

class TargetTrackingScalingPolicyConfigurationOutputTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationOutputTypeDef] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    DisableScaleIn: Optional[bool] = None

class TargetTrackingScalingPolicyConfigurationTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationTypeDef] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    DisableScaleIn: Optional[bool] = None

class ScalingPolicyTypeDef(BaseValidatorModel):
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

class PutScalingPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyName: str
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    PolicyType: Optional[PolicyTypeType] = None
    StepScalingPolicyConfiguration: Optional[StepScalingPolicyConfigurationTypeDef] = None
    TargetTrackingScalingPolicyConfiguration: Optional[       TargetTrackingScalingPolicyConfigurationTypeDef     ] = None

class DescribeScalingPoliciesResponseTypeDef(BaseValidatorModel):
    ScalingPolicies: List[ScalingPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


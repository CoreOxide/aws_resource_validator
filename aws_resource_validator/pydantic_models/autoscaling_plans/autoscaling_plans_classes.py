from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.autoscaling_plans.autoscaling_plans_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class TagFilterOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MetricDimension(BaseValidatorModel):
    Name: str
    Value: str


class Datapoint(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Value: Optional[float] = None


class DeleteScalingPlanRequest(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_scaling_plan_resources' function.
class DescribeScalingPlanResourcesRequest(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

Timestamp = Union[datetime, str]


class PredefinedLoadMetricSpecification(BaseValidatorModel):
    PredefinedLoadMetricType: LoadMetricTypeType
    ResourceLabel: Optional[str] = None


class PredefinedScalingMetricSpecification(BaseValidatorModel):
    PredefinedScalingMetricType: ScalingMetricTypeType
    ResourceLabel: Optional[str] = None


class TagFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class ApplicationSourceOutput(BaseValidatorModel):
    CloudFormationStackARN: Optional[str] = None
    TagFilters: Optional[List[TagFilterOutput]] = None


# This class is the output for the 'create_scaling_plan' function.
class CreateScalingPlanResponse(BaseValidatorModel):
    ScalingPlanVersion: int
    ResponseMetadata: ResponseMetadata


class CustomizedLoadMetricSpecificationOutput(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[List[MetricDimension]] = None
    Unit: Optional[str] = None


class CustomizedLoadMetricSpecification(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[List[MetricDimension]] = None
    Unit: Optional[str] = None


class CustomizedScalingMetricSpecificationOutput(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[List[MetricDimension]] = None
    Unit: Optional[str] = None


class CustomizedScalingMetricSpecification(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[List[MetricDimension]] = None
    Unit: Optional[str] = None


# This class is the output for the 'get_scaling_plan_resource_forecast_data' function.
class GetScalingPlanResourceForecastDataResponse(BaseValidatorModel):
    Datapoints: List[Datapoint]
    ResponseMetadata: ResponseMetadata


class DescribeScalingPlanResourcesRequestPaginate(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_scaling_plan_resource_forecast_data' function.
class GetScalingPlanResourceForecastDataRequest(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ForecastDataType: ForecastDataTypeType
    StartTime: Timestamp
    EndTime: Timestamp

TagFilterUnion = Union[TagFilter, TagFilterOutput]

CustomizedLoadMetricSpecificationUnion = Union[CustomizedLoadMetricSpecification, CustomizedLoadMetricSpecificationOutput]


class TargetTrackingConfigurationOutput(BaseValidatorModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[PredefinedScalingMetricSpecification] = None
    CustomizedScalingMetricSpecification: Optional[CustomizedScalingMetricSpecificationOutput] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None

CustomizedScalingMetricSpecificationUnion = Union[CustomizedScalingMetricSpecification, CustomizedScalingMetricSpecificationOutput]


class ApplicationSource(BaseValidatorModel):
    CloudFormationStackARN: Optional[str] = None
    TagFilters: Optional[List[TagFilterUnion]] = None


class ScalingInstructionOutput(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    TargetTrackingConfigurations: List[TargetTrackingConfigurationOutput]
    PredefinedLoadMetricSpecification: Optional[PredefinedLoadMetricSpecification] = None
    CustomizedLoadMetricSpecification: Optional[CustomizedLoadMetricSpecificationOutput] = None
    ScheduledActionBufferTime: Optional[int] = None
    PredictiveScalingMaxCapacityBehavior: Optional[PredictiveScalingMaxCapacityBehaviorType] = None
    PredictiveScalingMaxCapacityBuffer: Optional[int] = None
    PredictiveScalingMode: Optional[PredictiveScalingModeType] = None
    ScalingPolicyUpdateBehavior: Optional[ScalingPolicyUpdateBehaviorType] = None
    DisableDynamicScaling: Optional[bool] = None


class ScalingPolicy(BaseValidatorModel):
    PolicyName: str
    PolicyType: Literal['TargetTrackingScaling']
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationOutput] = None


class TargetTrackingConfiguration(BaseValidatorModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[PredefinedScalingMetricSpecification] = None
    CustomizedScalingMetricSpecification: Optional[CustomizedScalingMetricSpecificationUnion] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None

ApplicationSourceUnion = Union[ApplicationSource, ApplicationSourceOutput]


class ScalingPlan(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: ApplicationSourceOutput
    ScalingInstructions: List[ScalingInstructionOutput]
    StatusCode: ScalingPlanStatusCodeType
    StatusMessage: Optional[str] = None
    StatusStartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None


class ScalingPlanResource(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ScalingStatusCode: ScalingStatusCodeType
    ScalingPolicies: Optional[List[ScalingPolicy]] = None
    ScalingStatusMessage: Optional[str] = None

TargetTrackingConfigurationUnion = Union[TargetTrackingConfiguration, TargetTrackingConfigurationOutput]


class DescribeScalingPlansRequestPaginate(BaseValidatorModel):
    ScalingPlanNames: Optional[List[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[List[ApplicationSourceUnion]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_scaling_plans' function.
class DescribeScalingPlansRequest(BaseValidatorModel):
    ScalingPlanNames: Optional[List[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[List[ApplicationSourceUnion]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'describe_scaling_plans' function.
class DescribeScalingPlansResponse(BaseValidatorModel):
    ScalingPlans: List[ScalingPlan]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_scaling_plan_resources' function.
class DescribeScalingPlanResourcesResponse(BaseValidatorModel):
    ScalingPlanResources: List[ScalingPlanResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ScalingInstruction(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    TargetTrackingConfigurations: List[TargetTrackingConfigurationUnion]
    PredefinedLoadMetricSpecification: Optional[PredefinedLoadMetricSpecification] = None
    CustomizedLoadMetricSpecification: Optional[CustomizedLoadMetricSpecificationUnion] = None
    ScheduledActionBufferTime: Optional[int] = None
    PredictiveScalingMaxCapacityBehavior: Optional[PredictiveScalingMaxCapacityBehaviorType] = None
    PredictiveScalingMaxCapacityBuffer: Optional[int] = None
    PredictiveScalingMode: Optional[PredictiveScalingModeType] = None
    ScalingPolicyUpdateBehavior: Optional[ScalingPolicyUpdateBehaviorType] = None
    DisableDynamicScaling: Optional[bool] = None

ScalingInstructionUnion = Union[ScalingInstruction, ScalingInstructionOutput]


# This class is the input for the 'create_scaling_plan' function.
class CreateScalingPlanRequest(BaseValidatorModel):
    ScalingPlanName: str
    ApplicationSource: ApplicationSourceUnion
    ScalingInstructions: List[ScalingInstructionUnion]


class UpdateScalingPlanRequest(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: Optional[ApplicationSourceUnion] = None
    ScalingInstructions: Optional[List[ScalingInstructionUnion]] = None
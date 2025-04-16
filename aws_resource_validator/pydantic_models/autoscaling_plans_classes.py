from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.autoscaling_plans_constants import *

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


class DescribeScalingPlanResourcesRequest(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PredefinedLoadMetricSpecification(BaseValidatorModel):
    PredefinedLoadMetricType: LoadMetricTypeType
    ResourceLabel: Optional[str] = None


class PredefinedScalingMetricSpecification(BaseValidatorModel):
    PredefinedScalingMetricType: ScalingMetricTypeType
    ResourceLabel: Optional[str] = None


class TagFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class ApplicationSourceOutput(BaseValidatorModel):
    CloudFormationStackARN: Optional[str] = None
    TagFilters: Optional[List[TagFilterOutput]] = None


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
    Dimensions: Optional[Sequence[MetricDimension]] = None
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
    Dimensions: Optional[Sequence[MetricDimension]] = None
    Unit: Optional[str] = None


class GetScalingPlanResourceForecastDataResponse(BaseValidatorModel):
    Datapoints: List[Datapoint]
    ResponseMetadata: ResponseMetadata


class DescribeScalingPlanResourcesRequestPaginate(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class GetScalingPlanResourceForecastDataRequest(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ForecastDataType: ForecastDataTypeType
    StartTime: Timestamp
    EndTime: Timestamp


class TargetTrackingConfigurationOutput(BaseValidatorModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[PredefinedScalingMetricSpecification] = None
    CustomizedScalingMetricSpecification: Optional[ CustomizedScalingMetricSpecificationOutput ] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None


class TagFilterUnion(BaseValidatorModel):
    pass


class ApplicationSource(BaseValidatorModel):
    CloudFormationStackARN: Optional[str] = None
    TagFilters: Optional[Sequence[TagFilterUnion]] = None


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
    PolicyType: Literal["TargetTrackingScaling"]
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationOutput] = None


class CustomizedScalingMetricSpecificationUnion(BaseValidatorModel):
    pass


class TargetTrackingConfiguration(BaseValidatorModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[PredefinedScalingMetricSpecification] = None
    CustomizedScalingMetricSpecification: Optional[ CustomizedScalingMetricSpecificationUnion ] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None


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


class ApplicationSourceUnion(BaseValidatorModel):
    pass


class DescribeScalingPlansRequestPaginate(BaseValidatorModel):
    ScalingPlanNames: Optional[Sequence[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[Sequence[ApplicationSourceUnion]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeScalingPlansRequest(BaseValidatorModel):
    ScalingPlanNames: Optional[Sequence[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[Sequence[ApplicationSourceUnion]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeScalingPlansResponse(BaseValidatorModel):
    ScalingPlans: List[ScalingPlan]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeScalingPlanResourcesResponse(BaseValidatorModel):
    ScalingPlanResources: List[ScalingPlanResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TargetTrackingConfigurationUnion(BaseValidatorModel):
    pass


class CustomizedLoadMetricSpecificationUnion(BaseValidatorModel):
    pass


class ScalingInstruction(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    TargetTrackingConfigurations: Sequence[TargetTrackingConfigurationUnion]
    PredefinedLoadMetricSpecification: Optional[PredefinedLoadMetricSpecification] = None
    CustomizedLoadMetricSpecification: Optional[CustomizedLoadMetricSpecificationUnion] = None
    ScheduledActionBufferTime: Optional[int] = None
    PredictiveScalingMaxCapacityBehavior: Optional[PredictiveScalingMaxCapacityBehaviorType] = None
    PredictiveScalingMaxCapacityBuffer: Optional[int] = None
    PredictiveScalingMode: Optional[PredictiveScalingModeType] = None
    ScalingPolicyUpdateBehavior: Optional[ScalingPolicyUpdateBehaviorType] = None
    DisableDynamicScaling: Optional[bool] = None


class ScalingInstructionUnion(BaseValidatorModel):
    pass


class CreateScalingPlanRequest(BaseValidatorModel):
    ScalingPlanName: str
    ApplicationSource: ApplicationSourceUnion
    ScalingInstructions: Sequence[ScalingInstructionUnion]


class UpdateScalingPlanRequest(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: Optional[ApplicationSourceUnion] = None
    ScalingInstructions: Optional[Sequence[ScalingInstructionUnion]] = None



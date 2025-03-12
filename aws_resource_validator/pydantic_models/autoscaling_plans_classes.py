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

class TagFilterOutputTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MetricDimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class DatapointTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Value: Optional[float] = None


class DeleteScalingPlanRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeScalingPlanResourcesRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PredefinedLoadMetricSpecificationTypeDef(BaseValidatorModel):
    PredefinedLoadMetricType: LoadMetricTypeType
    ResourceLabel: Optional[str] = None


class PredefinedScalingMetricSpecificationTypeDef(BaseValidatorModel):
    PredefinedScalingMetricType: ScalingMetricTypeType
    ResourceLabel: Optional[str] = None


class TagFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class ApplicationSourceOutputTypeDef(BaseValidatorModel):
    CloudFormationStackARN: Optional[str] = None
    TagFilters: Optional[List[TagFilterOutputTypeDef]] = None


class CreateScalingPlanResponseTypeDef(BaseValidatorModel):
    ScalingPlanVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class CustomizedLoadMetricSpecificationOutputTypeDef(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Unit: Optional[str] = None


class CustomizedLoadMetricSpecificationTypeDef(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None
    Unit: Optional[str] = None


class CustomizedScalingMetricSpecificationOutputTypeDef(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Unit: Optional[str] = None


class CustomizedScalingMetricSpecificationTypeDef(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None
    Unit: Optional[str] = None


class GetScalingPlanResourceForecastDataResponseTypeDef(BaseValidatorModel):
    Datapoints: List[DatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeScalingPlanResourcesRequestPaginateTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetScalingPlanResourceForecastDataRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ForecastDataType: ForecastDataTypeType
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef


class TargetTrackingConfigurationOutputTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[PredefinedScalingMetricSpecificationTypeDef] = None
    CustomizedScalingMetricSpecification: Optional[ CustomizedScalingMetricSpecificationOutputTypeDef ] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None


class TagFilterUnionTypeDef(BaseValidatorModel):
    pass


class ApplicationSourceTypeDef(BaseValidatorModel):
    CloudFormationStackARN: Optional[str] = None
    TagFilters: Optional[Sequence[TagFilterUnionTypeDef]] = None


class ScalingInstructionOutputTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    TargetTrackingConfigurations: List[TargetTrackingConfigurationOutputTypeDef]
    PredefinedLoadMetricSpecification: Optional[PredefinedLoadMetricSpecificationTypeDef] = None
    CustomizedLoadMetricSpecification: Optional[CustomizedLoadMetricSpecificationOutputTypeDef] = None
    ScheduledActionBufferTime: Optional[int] = None
    PredictiveScalingMaxCapacityBehavior: Optional[PredictiveScalingMaxCapacityBehaviorType] = None
    PredictiveScalingMaxCapacityBuffer: Optional[int] = None
    PredictiveScalingMode: Optional[PredictiveScalingModeType] = None
    ScalingPolicyUpdateBehavior: Optional[ScalingPolicyUpdateBehaviorType] = None
    DisableDynamicScaling: Optional[bool] = None


class ScalingPolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyType: Literal["TargetTrackingScaling"]
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationOutputTypeDef] = None


class CustomizedScalingMetricSpecificationUnionTypeDef(BaseValidatorModel):
    pass


class TargetTrackingConfigurationTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[PredefinedScalingMetricSpecificationTypeDef] = None
    CustomizedScalingMetricSpecification: Optional[ CustomizedScalingMetricSpecificationUnionTypeDef ] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None


class ScalingPlanTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: ApplicationSourceOutputTypeDef
    ScalingInstructions: List[ScalingInstructionOutputTypeDef]
    StatusCode: ScalingPlanStatusCodeType
    StatusMessage: Optional[str] = None
    StatusStartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None


class ScalingPlanResourceTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ScalingStatusCode: ScalingStatusCodeType
    ScalingPolicies: Optional[List[ScalingPolicyTypeDef]] = None
    ScalingStatusMessage: Optional[str] = None


class ApplicationSourceUnionTypeDef(BaseValidatorModel):
    pass


class DescribeScalingPlansRequestPaginateTypeDef(BaseValidatorModel):
    ScalingPlanNames: Optional[Sequence[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[Sequence[ApplicationSourceUnionTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeScalingPlansRequestTypeDef(BaseValidatorModel):
    ScalingPlanNames: Optional[Sequence[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[Sequence[ApplicationSourceUnionTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeScalingPlansResponseTypeDef(BaseValidatorModel):
    ScalingPlans: List[ScalingPlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeScalingPlanResourcesResponseTypeDef(BaseValidatorModel):
    ScalingPlanResources: List[ScalingPlanResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TargetTrackingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CustomizedLoadMetricSpecificationUnionTypeDef(BaseValidatorModel):
    pass


class ScalingInstructionTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    TargetTrackingConfigurations: Sequence[TargetTrackingConfigurationUnionTypeDef]
    PredefinedLoadMetricSpecification: Optional[PredefinedLoadMetricSpecificationTypeDef] = None
    CustomizedLoadMetricSpecification: Optional[CustomizedLoadMetricSpecificationUnionTypeDef] = None
    ScheduledActionBufferTime: Optional[int] = None
    PredictiveScalingMaxCapacityBehavior: Optional[PredictiveScalingMaxCapacityBehaviorType] = None
    PredictiveScalingMaxCapacityBuffer: Optional[int] = None
    PredictiveScalingMode: Optional[PredictiveScalingModeType] = None
    ScalingPolicyUpdateBehavior: Optional[ScalingPolicyUpdateBehaviorType] = None
    DisableDynamicScaling: Optional[bool] = None


class ScalingInstructionUnionTypeDef(BaseValidatorModel):
    pass


class CreateScalingPlanRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ApplicationSource: ApplicationSourceUnionTypeDef
    ScalingInstructions: Sequence[ScalingInstructionUnionTypeDef]


class UpdateScalingPlanRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: Optional[ApplicationSourceUnionTypeDef] = None
    ScalingInstructions: Optional[Sequence[ScalingInstructionUnionTypeDef]] = None



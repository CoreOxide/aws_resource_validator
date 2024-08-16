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
from aws_resource_validator.pydantic_models.autoscaling_plans_constants import *

class TagFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class MetricDimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class DatapointTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Value: Optional[float] = None

class DeleteScalingPlanRequestRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeScalingPlanResourcesRequestRequestTypeDef(BaseValidatorModel):
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

class ApplicationSourceTypeDef(BaseValidatorModel):
    CloudFormationStackARN: Optional[str] = None
    TagFilters: Optional[Sequence[TagFilterTypeDef]] = None

class CreateScalingPlanResponseTypeDef(BaseValidatorModel):
    ScalingPlanVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CustomizedLoadMetricSpecificationPaginatorTypeDef(BaseValidatorModel):
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

class CustomizedScalingMetricSpecificationPaginatorTypeDef(BaseValidatorModel):
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

class DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetScalingPlanResourceForecastDataRequestRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ForecastDataType: ForecastDataTypeType
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef(BaseValidatorModel):
    ScalingPlanNames: Optional[Sequence[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[Sequence[ApplicationSourceTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingPlansRequestRequestTypeDef(BaseValidatorModel):
    ScalingPlanNames: Optional[Sequence[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[Sequence[ApplicationSourceTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TargetTrackingConfigurationPaginatorTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[       PredefinedScalingMetricSpecificationTypeDef     ] = None
    CustomizedScalingMetricSpecification: Optional[       CustomizedScalingMetricSpecificationPaginatorTypeDef     ] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None

class TargetTrackingConfigurationTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[       PredefinedScalingMetricSpecificationTypeDef     ] = None
    CustomizedScalingMetricSpecification: Optional[       CustomizedScalingMetricSpecificationTypeDef     ] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None

class ScalingInstructionPaginatorTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    TargetTrackingConfigurations: List[TargetTrackingConfigurationPaginatorTypeDef]
    PredefinedLoadMetricSpecification: Optional[PredefinedLoadMetricSpecificationTypeDef] = None
    CustomizedLoadMetricSpecification: Optional[       CustomizedLoadMetricSpecificationPaginatorTypeDef     ] = None
    ScheduledActionBufferTime: Optional[int] = None
    PredictiveScalingMaxCapacityBehavior: Optional[       PredictiveScalingMaxCapacityBehaviorType     ] = None
    PredictiveScalingMaxCapacityBuffer: Optional[int] = None
    PredictiveScalingMode: Optional[PredictiveScalingModeType] = None
    ScalingPolicyUpdateBehavior: Optional[ScalingPolicyUpdateBehaviorType] = None
    DisableDynamicScaling: Optional[bool] = None

class ScalingPolicyPaginatorTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyType: Literal["TargetTrackingScaling"]
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationPaginatorTypeDef] = None

class ScalingInstructionTypeDef(BaseValidatorModel):
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    MinCapacity: int
    MaxCapacity: int
    TargetTrackingConfigurations: Sequence[TargetTrackingConfigurationTypeDef]
    PredefinedLoadMetricSpecification: Optional[PredefinedLoadMetricSpecificationTypeDef] = None
    CustomizedLoadMetricSpecification: Optional[CustomizedLoadMetricSpecificationTypeDef] = None
    ScheduledActionBufferTime: Optional[int] = None
    PredictiveScalingMaxCapacityBehavior: Optional[       PredictiveScalingMaxCapacityBehaviorType     ] = None
    PredictiveScalingMaxCapacityBuffer: Optional[int] = None
    PredictiveScalingMode: Optional[PredictiveScalingModeType] = None
    ScalingPolicyUpdateBehavior: Optional[ScalingPolicyUpdateBehaviorType] = None
    DisableDynamicScaling: Optional[bool] = None

class ScalingPolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyType: Literal["TargetTrackingScaling"]
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationTypeDef] = None

class ScalingPlanPaginatorTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: ApplicationSourceTypeDef
    ScalingInstructions: List[ScalingInstructionPaginatorTypeDef]
    StatusCode: ScalingPlanStatusCodeType
    StatusMessage: Optional[str] = None
    StatusStartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None

class ScalingPlanResourcePaginatorTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ScalingStatusCode: ScalingStatusCodeType
    ScalingPolicies: Optional[List[ScalingPolicyPaginatorTypeDef]] = None
    ScalingStatusMessage: Optional[str] = None

class CreateScalingPlanRequestRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ApplicationSource: ApplicationSourceTypeDef
    ScalingInstructions: Sequence[ScalingInstructionTypeDef]

class ScalingPlanTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: ApplicationSourceTypeDef
    ScalingInstructions: List[ScalingInstructionTypeDef]
    StatusCode: ScalingPlanStatusCodeType
    StatusMessage: Optional[str] = None
    StatusStartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None

class UpdateScalingPlanRequestRequestTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: Optional[ApplicationSourceTypeDef] = None
    ScalingInstructions: Optional[Sequence[ScalingInstructionTypeDef]] = None

class ScalingPlanResourceTypeDef(BaseValidatorModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ScalingStatusCode: ScalingStatusCodeType
    ScalingPolicies: Optional[List[ScalingPolicyTypeDef]] = None
    ScalingStatusMessage: Optional[str] = None

class DescribeScalingPlansResponsePaginatorTypeDef(BaseValidatorModel):
    ScalingPlans: List[ScalingPlanPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPlanResourcesResponsePaginatorTypeDef(BaseValidatorModel):
    ScalingPlanResources: List[ScalingPlanResourcePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPlansResponseTypeDef(BaseValidatorModel):
    ScalingPlans: List[ScalingPlanTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPlanResourcesResponseTypeDef(BaseValidatorModel):
    ScalingPlanResources: List[ScalingPlanResourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


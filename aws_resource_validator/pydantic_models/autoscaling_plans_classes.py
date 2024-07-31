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
from aws_resource_validator.pydantic_models.autoscaling_plans_constants import *

class TagFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class MetricDimensionTypeDef(BaseModel):
    Name: str
    Value: str

class DatapointTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    Value: Optional[float] = None

class DeleteScalingPlanRequestRequestTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeScalingPlanResourcesRequestRequestTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PredefinedLoadMetricSpecificationTypeDef(BaseModel):
    PredefinedLoadMetricType: LoadMetricTypeType
    ResourceLabel: Optional[str] = None

class PredefinedScalingMetricSpecificationTypeDef(BaseModel):
    PredefinedScalingMetricType: ScalingMetricTypeType
    ResourceLabel: Optional[str] = None

class ApplicationSourceTypeDef(BaseModel):
    CloudFormationStackARN: Optional[str] = None
    TagFilters: Optional[Sequence[TagFilterTypeDef]] = None

class CreateScalingPlanResponseTypeDef(BaseModel):
    ScalingPlanVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CustomizedLoadMetricSpecificationPaginatorTypeDef(BaseModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Unit: Optional[str] = None

class CustomizedLoadMetricSpecificationTypeDef(BaseModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None
    Unit: Optional[str] = None

class CustomizedScalingMetricSpecificationPaginatorTypeDef(BaseModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Unit: Optional[str] = None

class CustomizedScalingMetricSpecificationTypeDef(BaseModel):
    MetricName: str
    Namespace: str
    Statistic: MetricStatisticType
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None
    Unit: Optional[str] = None

class GetScalingPlanResourceForecastDataResponseTypeDef(BaseModel):
    Datapoints: List[DatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetScalingPlanResourceForecastDataRequestRequestTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ForecastDataType: ForecastDataTypeType
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef(BaseModel):
    ScalingPlanNames: Optional[Sequence[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[Sequence[ApplicationSourceTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingPlansRequestRequestTypeDef(BaseModel):
    ScalingPlanNames: Optional[Sequence[str]] = None
    ScalingPlanVersion: Optional[int] = None
    ApplicationSources: Optional[Sequence[ApplicationSourceTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TargetTrackingConfigurationPaginatorTypeDef(BaseModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[       PredefinedScalingMetricSpecificationTypeDef     ] = None
    CustomizedScalingMetricSpecification: Optional[       CustomizedScalingMetricSpecificationPaginatorTypeDef     ] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None

class TargetTrackingConfigurationTypeDef(BaseModel):
    TargetValue: float
    PredefinedScalingMetricSpecification: Optional[       PredefinedScalingMetricSpecificationTypeDef     ] = None
    CustomizedScalingMetricSpecification: Optional[       CustomizedScalingMetricSpecificationTypeDef     ] = None
    DisableScaleIn: Optional[bool] = None
    ScaleOutCooldown: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    EstimatedInstanceWarmup: Optional[int] = None

class ScalingInstructionPaginatorTypeDef(BaseModel):
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

class ScalingPolicyPaginatorTypeDef(BaseModel):
    PolicyName: str
    PolicyType: Literal["TargetTrackingScaling"]
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationPaginatorTypeDef] = None

class ScalingInstructionTypeDef(BaseModel):
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

class ScalingPolicyTypeDef(BaseModel):
    PolicyName: str
    PolicyType: Literal["TargetTrackingScaling"]
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationTypeDef] = None

class ScalingPlanPaginatorTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: ApplicationSourceTypeDef
    ScalingInstructions: List[ScalingInstructionPaginatorTypeDef]
    StatusCode: ScalingPlanStatusCodeType
    StatusMessage: Optional[str] = None
    StatusStartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None

class ScalingPlanResourcePaginatorTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ScalingStatusCode: ScalingStatusCodeType
    ScalingPolicies: Optional[List[ScalingPolicyPaginatorTypeDef]] = None
    ScalingStatusMessage: Optional[str] = None

class CreateScalingPlanRequestRequestTypeDef(BaseModel):
    ScalingPlanName: str
    ApplicationSource: ApplicationSourceTypeDef
    ScalingInstructions: Sequence[ScalingInstructionTypeDef]

class ScalingPlanTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: ApplicationSourceTypeDef
    ScalingInstructions: List[ScalingInstructionTypeDef]
    StatusCode: ScalingPlanStatusCodeType
    StatusMessage: Optional[str] = None
    StatusStartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None

class UpdateScalingPlanRequestRequestTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: Optional[ApplicationSourceTypeDef] = None
    ScalingInstructions: Optional[Sequence[ScalingInstructionTypeDef]] = None

class ScalingPlanResourceTypeDef(BaseModel):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespaceType
    ResourceId: str
    ScalableDimension: ScalableDimensionType
    ScalingStatusCode: ScalingStatusCodeType
    ScalingPolicies: Optional[List[ScalingPolicyTypeDef]] = None
    ScalingStatusMessage: Optional[str] = None

class DescribeScalingPlansResponsePaginatorTypeDef(BaseModel):
    ScalingPlans: List[ScalingPlanPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPlanResourcesResponsePaginatorTypeDef(BaseModel):
    ScalingPlanResources: List[ScalingPlanResourcePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPlansResponseTypeDef(BaseModel):
    ScalingPlans: List[ScalingPlanTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScalingPlanResourcesResponseTypeDef(BaseModel):
    ScalingPlanResources: List[ScalingPlanResourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


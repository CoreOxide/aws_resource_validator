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
from aws_resource_validator.pydantic_models.cost_optimization_hub_constants import *

class AccountEnrollmentStatusTypeDef(BaseModel):
    accountId: Optional[str] = None
    status: Optional[EnrollmentStatusType] = None
    lastUpdatedTimestamp: Optional[datetime] = None
    createdTimestamp: Optional[datetime] = None

class BlockStoragePerformanceConfigurationTypeDef(BaseModel):
    iops: Optional[float] = None
    throughput: Optional[float] = None

class ComputeConfigurationTypeDef(BaseModel):
    vCpu: Optional[float] = None
    memorySizeInMB: Optional[int] = None
    architecture: Optional[str] = None
    platform: Optional[str] = None

class ComputeSavingsPlansConfigurationTypeDef(BaseModel):
    accountScope: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    hourlyCommitment: Optional[str] = None

class DbInstanceConfigurationTypeDef(BaseModel):
    dbInstanceClass: Optional[str] = None

class StorageConfigurationTypeDef(BaseModel):
    type: Optional[str] = None
    sizeInGb: Optional[float] = None

class InstanceConfigurationTypeDef(BaseModel):
    type: Optional[str] = None

class Ec2InstanceSavingsPlansConfigurationTypeDef(BaseModel):
    accountScope: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    hourlyCommitment: Optional[str] = None
    instanceFamily: Optional[str] = None
    savingsPlansRegion: Optional[str] = None

class Ec2ReservedInstancesConfigurationTypeDef(BaseModel):
    accountScope: Optional[str] = None
    service: Optional[str] = None
    normalizedUnitsToPurchase: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    numberOfInstancesToPurchase: Optional[str] = None
    offeringClass: Optional[str] = None
    instanceFamily: Optional[str] = None
    instanceType: Optional[str] = None
    reservedInstancesRegion: Optional[str] = None
    currentGeneration: Optional[str] = None
    platform: Optional[str] = None
    tenancy: Optional[str] = None
    sizeFlexEligible: Optional[bool] = None
    upfrontCost: Optional[str] = None
    monthlyRecurringCost: Optional[str] = None

class ElastiCacheReservedInstancesConfigurationTypeDef(BaseModel):
    accountScope: Optional[str] = None
    service: Optional[str] = None
    normalizedUnitsToPurchase: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    numberOfInstancesToPurchase: Optional[str] = None
    instanceFamily: Optional[str] = None
    instanceType: Optional[str] = None
    reservedInstancesRegion: Optional[str] = None
    currentGeneration: Optional[str] = None
    sizeFlexEligible: Optional[bool] = None
    upfrontCost: Optional[str] = None
    monthlyRecurringCost: Optional[str] = None

class EstimatedDiscountsTypeDef(BaseModel):
    savingsPlansDiscount: Optional[float] = None
    reservedInstancesDiscount: Optional[float] = None
    otherDiscount: Optional[float] = None

class TagTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GetRecommendationRequestRequestTypeDef(BaseModel):
    recommendationId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEnrollmentStatusesRequestRequestTypeDef(BaseModel):
    includeOrganizationInfo: Optional[bool] = None
    accountId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RecommendationSummaryTypeDef(BaseModel):
    group: Optional[str] = None
    estimatedMonthlySavings: Optional[float] = None
    recommendationCount: Optional[int] = None

class OrderByTypeDef(BaseModel):
    dimension: Optional[str] = None
    order: Optional[OrderType] = None

class OpenSearchReservedInstancesConfigurationTypeDef(BaseModel):
    accountScope: Optional[str] = None
    service: Optional[str] = None
    normalizedUnitsToPurchase: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    numberOfInstancesToPurchase: Optional[str] = None
    instanceType: Optional[str] = None
    reservedInstancesRegion: Optional[str] = None
    currentGeneration: Optional[str] = None
    sizeFlexEligible: Optional[bool] = None
    upfrontCost: Optional[str] = None
    monthlyRecurringCost: Optional[str] = None

class RdsDbInstanceStorageConfigurationTypeDef(BaseModel):
    storageType: Optional[str] = None
    allocatedStorageInGb: Optional[float] = None
    iops: Optional[float] = None
    storageThroughput: Optional[float] = None

class RdsReservedInstancesConfigurationTypeDef(BaseModel):
    accountScope: Optional[str] = None
    service: Optional[str] = None
    normalizedUnitsToPurchase: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    numberOfInstancesToPurchase: Optional[str] = None
    instanceFamily: Optional[str] = None
    instanceType: Optional[str] = None
    reservedInstancesRegion: Optional[str] = None
    sizeFlexEligible: Optional[bool] = None
    currentGeneration: Optional[str] = None
    upfrontCost: Optional[str] = None
    monthlyRecurringCost: Optional[str] = None
    licenseModel: Optional[str] = None
    databaseEdition: Optional[str] = None
    databaseEngine: Optional[str] = None
    deploymentOption: Optional[str] = None

class RedshiftReservedInstancesConfigurationTypeDef(BaseModel):
    accountScope: Optional[str] = None
    service: Optional[str] = None
    normalizedUnitsToPurchase: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    numberOfInstancesToPurchase: Optional[str] = None
    instanceFamily: Optional[str] = None
    instanceType: Optional[str] = None
    reservedInstancesRegion: Optional[str] = None
    sizeFlexEligible: Optional[bool] = None
    currentGeneration: Optional[str] = None
    upfrontCost: Optional[str] = None
    monthlyRecurringCost: Optional[str] = None

class ReservedInstancesPricingTypeDef(BaseModel):
    estimatedOnDemandCost: Optional[float] = None
    monthlyReservationEligibleCost: Optional[float] = None
    savingsPercentage: Optional[float] = None
    estimatedMonthlyAmortizedReservationCost: Optional[float] = None

class UsageTypeDef(BaseModel):
    usageType: Optional[str] = None
    usageAmount: Optional[float] = None
    operation: Optional[str] = None
    productCode: Optional[str] = None
    unit: Optional[str] = None

class SageMakerSavingsPlansConfigurationTypeDef(BaseModel):
    accountScope: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    hourlyCommitment: Optional[str] = None

class SavingsPlansPricingTypeDef(BaseModel):
    monthlySavingsPlansEligibleCost: Optional[float] = None
    estimatedMonthlyCommitment: Optional[float] = None
    savingsPercentage: Optional[float] = None
    estimatedOnDemandCost: Optional[float] = None

class UpdateEnrollmentStatusRequestRequestTypeDef(BaseModel):
    status: EnrollmentStatusType
    includeMemberAccounts: Optional[bool] = None

class UpdatePreferencesRequestRequestTypeDef(BaseModel):
    savingsEstimationMode: Optional[SavingsEstimationModeType] = None
    memberAccountDiscountVisibility: Optional[MemberAccountDiscountVisibilityType] = None

class EcsServiceConfigurationTypeDef(BaseModel):
    compute: Optional[ComputeConfigurationTypeDef] = None

class LambdaFunctionConfigurationTypeDef(BaseModel):
    compute: Optional[ComputeConfigurationTypeDef] = None

class RdsDbInstanceConfigurationTypeDef(BaseModel):
    instance: Optional[DbInstanceConfigurationTypeDef] = None

class EbsVolumeConfigurationTypeDef(BaseModel):
    storage: Optional[StorageConfigurationTypeDef] = None
    performance: Optional[BlockStoragePerformanceConfigurationTypeDef] = None
    attachmentState: Optional[str] = None

class Ec2AutoScalingGroupConfigurationTypeDef(BaseModel):
    instance: Optional[InstanceConfigurationTypeDef] = None

class Ec2InstanceConfigurationTypeDef(BaseModel):
    instance: Optional[InstanceConfigurationTypeDef] = None

class ResourcePricingTypeDef(BaseModel):
    estimatedCostBeforeDiscounts: Optional[float] = None
    estimatedNetUnusedAmortizedCommitments: Optional[float] = None
    estimatedDiscounts: Optional[EstimatedDiscountsTypeDef] = None
    estimatedCostAfterDiscounts: Optional[float] = None

class FilterTypeDef(BaseModel):
    restartNeeded: Optional[bool] = None
    rollbackPossible: Optional[bool] = None
    implementationEfforts: Optional[Sequence[ImplementationEffortType]] = None
    accountIds: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    resourceTypes: Optional[Sequence[ResourceTypeType]] = None
    actionTypes: Optional[Sequence[ActionTypeType]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    resourceIds: Optional[Sequence[str]] = None
    resourceArns: Optional[Sequence[str]] = None
    recommendationIds: Optional[Sequence[str]] = None

class RecommendationTypeDef(BaseModel):
    recommendationId: Optional[str] = None
    accountId: Optional[str] = None
    region: Optional[str] = None
    resourceId: Optional[str] = None
    resourceArn: Optional[str] = None
    currentResourceType: Optional[str] = None
    recommendedResourceType: Optional[str] = None
    estimatedMonthlySavings: Optional[float] = None
    estimatedSavingsPercentage: Optional[float] = None
    estimatedMonthlyCost: Optional[float] = None
    currencyCode: Optional[str] = None
    implementationEffort: Optional[str] = None
    restartNeeded: Optional[bool] = None
    actionType: Optional[str] = None
    rollbackPossible: Optional[bool] = None
    currentResourceSummary: Optional[str] = None
    recommendedResourceSummary: Optional[str] = None
    lastRefreshTimestamp: Optional[datetime] = None
    recommendationLookbackPeriodInDays: Optional[int] = None
    source: Optional[SourceType] = None
    tags: Optional[List[TagTypeDef]] = None

class GetPreferencesResponseTypeDef(BaseModel):
    savingsEstimationMode: SavingsEstimationModeType
    memberAccountDiscountVisibility: MemberAccountDiscountVisibilityType
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnrollmentStatusesResponseTypeDef(BaseModel):
    items: List[AccountEnrollmentStatusTypeDef]
    includeMemberAccounts: bool
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnrollmentStatusResponseTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePreferencesResponseTypeDef(BaseModel):
    savingsEstimationMode: SavingsEstimationModeType
    memberAccountDiscountVisibility: MemberAccountDiscountVisibilityType
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnrollmentStatusesRequestListEnrollmentStatusesPaginateTypeDef(BaseModel):
    includeOrganizationInfo: Optional[bool] = None
    accountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationSummariesResponseTypeDef(BaseModel):
    estimatedTotalDedupedSavings: float
    items: List[RecommendationSummaryTypeDef]
    groupBy: str
    currencyCode: str
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedInstancesCostCalculationTypeDef(BaseModel):
    pricing: Optional[ReservedInstancesPricingTypeDef] = None

class SavingsPlansCostCalculationTypeDef(BaseModel):
    pricing: Optional[SavingsPlansPricingTypeDef] = None

class ResourceCostCalculationTypeDef(BaseModel):
    usages: Optional[List[UsageTypeDef]] = None
    pricing: Optional[ResourcePricingTypeDef] = None

class ListRecommendationSummariesRequestListRecommendationSummariesPaginateTypeDef(BaseModel):
    groupBy: str
    filter: Optional[FilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationSummariesRequestRequestTypeDef(BaseModel):
    groupBy: str
    filter: Optional[FilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRecommendationsRequestListRecommendationsPaginateTypeDef(BaseModel):
    filter: Optional[FilterTypeDef] = None
    orderBy: Optional[OrderByTypeDef] = None
    includeAllRecommendations: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationsRequestRequestTypeDef(BaseModel):
    filter: Optional[FilterTypeDef] = None
    orderBy: Optional[OrderByTypeDef] = None
    includeAllRecommendations: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRecommendationsResponseTypeDef(BaseModel):
    items: List[RecommendationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class Ec2ReservedInstancesTypeDef(BaseModel):
    configuration: Optional[Ec2ReservedInstancesConfigurationTypeDef] = None
    costCalculation: Optional[ReservedInstancesCostCalculationTypeDef] = None

class ElastiCacheReservedInstancesTypeDef(BaseModel):
    configuration: Optional[ElastiCacheReservedInstancesConfigurationTypeDef] = None
    costCalculation: Optional[ReservedInstancesCostCalculationTypeDef] = None

class OpenSearchReservedInstancesTypeDef(BaseModel):
    configuration: Optional[OpenSearchReservedInstancesConfigurationTypeDef] = None
    costCalculation: Optional[ReservedInstancesCostCalculationTypeDef] = None

class RdsReservedInstancesTypeDef(BaseModel):
    configuration: Optional[RdsReservedInstancesConfigurationTypeDef] = None
    costCalculation: Optional[ReservedInstancesCostCalculationTypeDef] = None

class RedshiftReservedInstancesTypeDef(BaseModel):
    configuration: Optional[RedshiftReservedInstancesConfigurationTypeDef] = None
    costCalculation: Optional[ReservedInstancesCostCalculationTypeDef] = None

class ComputeSavingsPlansTypeDef(BaseModel):
    configuration: Optional[ComputeSavingsPlansConfigurationTypeDef] = None
    costCalculation: Optional[SavingsPlansCostCalculationTypeDef] = None

class Ec2InstanceSavingsPlansTypeDef(BaseModel):
    configuration: Optional[Ec2InstanceSavingsPlansConfigurationTypeDef] = None
    costCalculation: Optional[SavingsPlansCostCalculationTypeDef] = None

class SageMakerSavingsPlansTypeDef(BaseModel):
    configuration: Optional[SageMakerSavingsPlansConfigurationTypeDef] = None
    costCalculation: Optional[SavingsPlansCostCalculationTypeDef] = None

class EbsVolumeTypeDef(BaseModel):
    configuration: Optional[EbsVolumeConfigurationTypeDef] = None
    costCalculation: Optional[ResourceCostCalculationTypeDef] = None

class Ec2AutoScalingGroupTypeDef(BaseModel):
    configuration: Optional[Ec2AutoScalingGroupConfigurationTypeDef] = None
    costCalculation: Optional[ResourceCostCalculationTypeDef] = None

class Ec2InstanceTypeDef(BaseModel):
    configuration: Optional[Ec2InstanceConfigurationTypeDef] = None
    costCalculation: Optional[ResourceCostCalculationTypeDef] = None

class EcsServiceTypeDef(BaseModel):
    configuration: Optional[EcsServiceConfigurationTypeDef] = None
    costCalculation: Optional[ResourceCostCalculationTypeDef] = None

class LambdaFunctionTypeDef(BaseModel):
    configuration: Optional[LambdaFunctionConfigurationTypeDef] = None
    costCalculation: Optional[ResourceCostCalculationTypeDef] = None

class RdsDbInstanceStorageTypeDef(BaseModel):
    configuration: Optional[RdsDbInstanceStorageConfigurationTypeDef] = None
    costCalculation: Optional[ResourceCostCalculationTypeDef] = None

class RdsDbInstanceTypeDef(BaseModel):
    configuration: Optional[RdsDbInstanceConfigurationTypeDef] = None
    costCalculation: Optional[ResourceCostCalculationTypeDef] = None

class ResourceDetailsTypeDef(BaseModel):
    lambdaFunction: Optional[LambdaFunctionTypeDef] = None
    ecsService: Optional[EcsServiceTypeDef] = None
    ec2Instance: Optional[Ec2InstanceTypeDef] = None
    ebsVolume: Optional[EbsVolumeTypeDef] = None
    ec2AutoScalingGroup: Optional[Ec2AutoScalingGroupTypeDef] = None
    ec2ReservedInstances: Optional[Ec2ReservedInstancesTypeDef] = None
    rdsReservedInstances: Optional[RdsReservedInstancesTypeDef] = None
    elastiCacheReservedInstances: Optional[ElastiCacheReservedInstancesTypeDef] = None
    openSearchReservedInstances: Optional[OpenSearchReservedInstancesTypeDef] = None
    redshiftReservedInstances: Optional[RedshiftReservedInstancesTypeDef] = None
    ec2InstanceSavingsPlans: Optional[Ec2InstanceSavingsPlansTypeDef] = None
    computeSavingsPlans: Optional[ComputeSavingsPlansTypeDef] = None
    sageMakerSavingsPlans: Optional[SageMakerSavingsPlansTypeDef] = None
    rdsDbInstance: Optional[RdsDbInstanceTypeDef] = None
    rdsDbInstanceStorage: Optional[RdsDbInstanceStorageTypeDef] = None

class GetRecommendationResponseTypeDef(BaseModel):
    recommendationId: str
    resourceId: str
    resourceArn: str
    accountId: str
    currencyCode: str
    recommendationLookbackPeriodInDays: int
    costCalculationLookbackPeriodInDays: int
    estimatedSavingsPercentage: float
    estimatedSavingsOverCostCalculationLookbackPeriod: float
    currentResourceType: ResourceTypeType
    recommendedResourceType: ResourceTypeType
    region: str
    source: SourceType
    lastRefreshTimestamp: datetime
    estimatedMonthlySavings: float
    estimatedMonthlyCost: float
    implementationEffort: ImplementationEffortType
    restartNeeded: bool
    actionType: ActionTypeType
    rollbackPossible: bool
    currentResourceDetails: ResourceDetailsTypeDef
    recommendedResourceDetails: ResourceDetailsTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


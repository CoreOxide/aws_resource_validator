from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountEnrollmentStatus(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[EnrollmentStatusType] = None
    lastUpdatedTimestamp: Optional[datetime] = None
    createdTimestamp: Optional[datetime] = None


class BlockStoragePerformanceConfiguration(BaseValidatorModel):
    iops: Optional[float] = None
    throughput: Optional[float] = None


class ComputeConfiguration(BaseValidatorModel):
    vCpu: Optional[float] = None
    memorySizeInMB: Optional[int] = None
    architecture: Optional[str] = None
    platform: Optional[str] = None


class ComputeSavingsPlansConfiguration(BaseValidatorModel):
    accountScope: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    hourlyCommitment: Optional[str] = None


class DbInstanceConfiguration(BaseValidatorModel):
    dbInstanceClass: Optional[str] = None


class StorageConfiguration(BaseValidatorModel):
    type: Optional[str] = None
    sizeInGb: Optional[float] = None


class InstanceConfiguration(BaseValidatorModel):
    type: Optional[str] = None


class MixedInstanceConfiguration(BaseValidatorModel):
    type: Optional[str] = None


class Ec2InstanceSavingsPlansConfiguration(BaseValidatorModel):
    accountScope: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    hourlyCommitment: Optional[str] = None
    instanceFamily: Optional[str] = None
    savingsPlansRegion: Optional[str] = None


class Ec2ReservedInstancesConfiguration(BaseValidatorModel):
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


class ElastiCacheReservedInstancesConfiguration(BaseValidatorModel):
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


class EstimatedDiscounts(BaseValidatorModel):
    savingsPlansDiscount: Optional[float] = None
    reservedInstancesDiscount: Optional[float] = None
    otherDiscount: Optional[float] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'get_recommendation' function.
class GetRecommendationRequest(BaseValidatorModel):
    recommendationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_enrollment_statuses' function.
class ListEnrollmentStatusesRequest(BaseValidatorModel):
    includeOrganizationInfo: Optional[bool] = None
    accountId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RecommendationSummary(BaseValidatorModel):
    group: Optional[str] = None
    estimatedMonthlySavings: Optional[float] = None
    recommendationCount: Optional[int] = None


class SummaryMetricsResult(BaseValidatorModel):
    savingsPercentage: Optional[str] = None


class OrderBy(BaseValidatorModel):
    dimension: Optional[str] = None
    order: Optional[OrderType] = None


class OpenSearchReservedInstancesConfiguration(BaseValidatorModel):
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


class RdsDbInstanceStorageConfiguration(BaseValidatorModel):
    storageType: Optional[str] = None
    allocatedStorageInGb: Optional[float] = None
    iops: Optional[float] = None
    storageThroughput: Optional[float] = None


class RdsReservedInstancesConfiguration(BaseValidatorModel):
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


class RedshiftReservedInstancesConfiguration(BaseValidatorModel):
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


class ReservedInstancesPricing(BaseValidatorModel):
    estimatedOnDemandCost: Optional[float] = None
    monthlyReservationEligibleCost: Optional[float] = None
    savingsPercentage: Optional[float] = None
    estimatedMonthlyAmortizedReservationCost: Optional[float] = None


class Usage(BaseValidatorModel):
    usageType: Optional[str] = None
    usageAmount: Optional[float] = None
    operation: Optional[str] = None
    productCode: Optional[str] = None
    unit: Optional[str] = None


class SageMakerSavingsPlansConfiguration(BaseValidatorModel):
    accountScope: Optional[str] = None
    term: Optional[str] = None
    paymentOption: Optional[str] = None
    hourlyCommitment: Optional[str] = None


class SavingsPlansPricing(BaseValidatorModel):
    monthlySavingsPlansEligibleCost: Optional[float] = None
    estimatedMonthlyCommitment: Optional[float] = None
    savingsPercentage: Optional[float] = None
    estimatedOnDemandCost: Optional[float] = None


# This class is the input for the 'update_enrollment_status' function.
class UpdateEnrollmentStatusRequest(BaseValidatorModel):
    status: EnrollmentStatusType
    includeMemberAccounts: Optional[bool] = None


# This class is the input for the 'update_preferences' function.
class UpdatePreferencesRequest(BaseValidatorModel):
    savingsEstimationMode: Optional[SavingsEstimationModeType] = None
    memberAccountDiscountVisibility: Optional[MemberAccountDiscountVisibilityType] = None


class EcsServiceConfiguration(BaseValidatorModel):
    compute: Optional[ComputeConfiguration] = None


class LambdaFunctionConfiguration(BaseValidatorModel):
    compute: Optional[ComputeConfiguration] = None


class RdsDbInstanceConfiguration(BaseValidatorModel):
    instance: Optional[DbInstanceConfiguration] = None


class EbsVolumeConfiguration(BaseValidatorModel):
    storage: Optional[StorageConfiguration] = None
    performance: Optional[BlockStoragePerformanceConfiguration] = None
    attachmentState: Optional[str] = None


class Ec2InstanceConfiguration(BaseValidatorModel):
    instance: Optional[InstanceConfiguration] = None


class Ec2AutoScalingGroupConfiguration(BaseValidatorModel):
    instance: Optional[InstanceConfiguration] = None
    mixedInstances: Optional[List[MixedInstanceConfiguration]] = None
    type: Optional[Ec2AutoScalingGroupTypeType] = None
    allocationStrategy: Optional[AllocationStrategyType] = None


class ResourcePricing(BaseValidatorModel):
    estimatedCostBeforeDiscounts: Optional[float] = None
    estimatedNetUnusedAmortizedCommitments: Optional[float] = None
    estimatedDiscounts: Optional[EstimatedDiscounts] = None
    estimatedCostAfterDiscounts: Optional[float] = None


class Filter(BaseValidatorModel):
    restartNeeded: Optional[bool] = None
    rollbackPossible: Optional[bool] = None
    implementationEfforts: Optional[List[ImplementationEffortType]] = None
    accountIds: Optional[List[str]] = None
    regions: Optional[List[str]] = None
    resourceTypes: Optional[List[ResourceTypeType]] = None
    actionTypes: Optional[List[ActionTypeType]] = None
    tags: Optional[List[Tag]] = None
    resourceIds: Optional[List[str]] = None
    resourceArns: Optional[List[str]] = None
    recommendationIds: Optional[List[str]] = None


class Recommendation(BaseValidatorModel):
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
    tags: Optional[List[Tag]] = None


class GetPreferencesResponse(BaseValidatorModel):
    savingsEstimationMode: SavingsEstimationModeType
    memberAccountDiscountVisibility: MemberAccountDiscountVisibilityType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_enrollment_statuses' function.
class ListEnrollmentStatusesResponse(BaseValidatorModel):
    items: List[AccountEnrollmentStatus]
    includeMemberAccounts: bool
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_enrollment_status' function.
class UpdateEnrollmentStatusResponse(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_preferences' function.
class UpdatePreferencesResponse(BaseValidatorModel):
    savingsEstimationMode: SavingsEstimationModeType
    memberAccountDiscountVisibility: MemberAccountDiscountVisibilityType
    ResponseMetadata: ResponseMetadata


class ListEnrollmentStatusesRequestPaginate(BaseValidatorModel):
    includeOrganizationInfo: Optional[bool] = None
    accountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_recommendation_summaries' function.
class ListRecommendationSummariesResponse(BaseValidatorModel):
    estimatedTotalDedupedSavings: float
    items: List[RecommendationSummary]
    groupBy: str
    currencyCode: str
    metrics: SummaryMetricsResult
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ReservedInstancesCostCalculation(BaseValidatorModel):
    pricing: Optional[ReservedInstancesPricing] = None


class SavingsPlansCostCalculation(BaseValidatorModel):
    pricing: Optional[SavingsPlansPricing] = None


class ResourceCostCalculation(BaseValidatorModel):
    usages: Optional[List[Usage]] = None
    pricing: Optional[ResourcePricing] = None


class ListRecommendationSummariesRequestPaginate(BaseValidatorModel):
    groupBy: str
    filter: Optional[Filter] = None
    metrics: Optional[List[Literal['SavingsPercentage']]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_recommendation_summaries' function.
class ListRecommendationSummariesRequest(BaseValidatorModel):
    groupBy: str
    filter: Optional[Filter] = None
    maxResults: Optional[int] = None
    metrics: Optional[List[Literal['SavingsPercentage']]] = None
    nextToken: Optional[str] = None


class ListRecommendationsRequestPaginate(BaseValidatorModel):
    filter: Optional[Filter] = None
    orderBy: Optional[OrderBy] = None
    includeAllRecommendations: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_recommendations' function.
class ListRecommendationsRequest(BaseValidatorModel):
    filter: Optional[Filter] = None
    orderBy: Optional[OrderBy] = None
    includeAllRecommendations: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_recommendations' function.
class ListRecommendationsResponse(BaseValidatorModel):
    items: List[Recommendation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Ec2ReservedInstances(BaseValidatorModel):
    configuration: Optional[Ec2ReservedInstancesConfiguration] = None
    costCalculation: Optional[ReservedInstancesCostCalculation] = None


class ElastiCacheReservedInstances(BaseValidatorModel):
    configuration: Optional[ElastiCacheReservedInstancesConfiguration] = None
    costCalculation: Optional[ReservedInstancesCostCalculation] = None


class OpenSearchReservedInstances(BaseValidatorModel):
    configuration: Optional[OpenSearchReservedInstancesConfiguration] = None
    costCalculation: Optional[ReservedInstancesCostCalculation] = None


class RdsReservedInstances(BaseValidatorModel):
    configuration: Optional[RdsReservedInstancesConfiguration] = None
    costCalculation: Optional[ReservedInstancesCostCalculation] = None


class RedshiftReservedInstances(BaseValidatorModel):
    configuration: Optional[RedshiftReservedInstancesConfiguration] = None
    costCalculation: Optional[ReservedInstancesCostCalculation] = None


class ComputeSavingsPlans(BaseValidatorModel):
    configuration: Optional[ComputeSavingsPlansConfiguration] = None
    costCalculation: Optional[SavingsPlansCostCalculation] = None


class Ec2InstanceSavingsPlans(BaseValidatorModel):
    configuration: Optional[Ec2InstanceSavingsPlansConfiguration] = None
    costCalculation: Optional[SavingsPlansCostCalculation] = None


class SageMakerSavingsPlans(BaseValidatorModel):
    configuration: Optional[SageMakerSavingsPlansConfiguration] = None
    costCalculation: Optional[SavingsPlansCostCalculation] = None


class EbsVolume(BaseValidatorModel):
    configuration: Optional[EbsVolumeConfiguration] = None
    costCalculation: Optional[ResourceCostCalculation] = None


class Ec2AutoScalingGroup(BaseValidatorModel):
    configuration: Optional[Ec2AutoScalingGroupConfiguration] = None
    costCalculation: Optional[ResourceCostCalculation] = None


class Ec2Instance(BaseValidatorModel):
    configuration: Optional[Ec2InstanceConfiguration] = None
    costCalculation: Optional[ResourceCostCalculation] = None


class EcsService(BaseValidatorModel):
    configuration: Optional[EcsServiceConfiguration] = None
    costCalculation: Optional[ResourceCostCalculation] = None


class LambdaFunction(BaseValidatorModel):
    configuration: Optional[LambdaFunctionConfiguration] = None
    costCalculation: Optional[ResourceCostCalculation] = None


class RdsDbInstanceStorage(BaseValidatorModel):
    configuration: Optional[RdsDbInstanceStorageConfiguration] = None
    costCalculation: Optional[ResourceCostCalculation] = None


class RdsDbInstance(BaseValidatorModel):
    configuration: Optional[RdsDbInstanceConfiguration] = None
    costCalculation: Optional[ResourceCostCalculation] = None


class ResourceDetails(BaseValidatorModel):
    lambdaFunction: Optional[LambdaFunction] = None
    ecsService: Optional[EcsService] = None
    ec2Instance: Optional[Ec2Instance] = None
    ebsVolume: Optional[EbsVolume] = None
    ec2AutoScalingGroup: Optional[Ec2AutoScalingGroup] = None
    ec2ReservedInstances: Optional[Ec2ReservedInstances] = None
    rdsReservedInstances: Optional[RdsReservedInstances] = None
    elastiCacheReservedInstances: Optional[ElastiCacheReservedInstances] = None
    openSearchReservedInstances: Optional[OpenSearchReservedInstances] = None
    redshiftReservedInstances: Optional[RedshiftReservedInstances] = None
    ec2InstanceSavingsPlans: Optional[Ec2InstanceSavingsPlans] = None
    computeSavingsPlans: Optional[ComputeSavingsPlans] = None
    sageMakerSavingsPlans: Optional[SageMakerSavingsPlans] = None
    rdsDbInstance: Optional[RdsDbInstance] = None
    rdsDbInstanceStorage: Optional[RdsDbInstanceStorage] = None


# This class is the output for the 'get_recommendation' function.
class GetRecommendationResponse(BaseValidatorModel):
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
    currentResourceDetails: ResourceDetails
    recommendedResourceDetails: ResourceDetails
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
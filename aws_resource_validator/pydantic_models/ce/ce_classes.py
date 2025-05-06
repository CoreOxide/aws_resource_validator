from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ce.ce_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AnomalyDateInterval(BaseValidatorModel):
    StartDate: str
    EndDate: Optional[str] = None


class AnomalyScore(BaseValidatorModel):
    MaxScore: float
    CurrentScore: float


class Subscriber(BaseValidatorModel):
    Address: Optional[str] = None
    Type: Optional[SubscriberTypeType] = None
    Status: Optional[SubscriberStatusType] = None


class Impact(BaseValidatorModel):
    MaxImpact: float
    TotalImpact: Optional[float] = None
    TotalActualSpend: Optional[float] = None
    TotalExpectedSpend: Optional[float] = None
    TotalImpactPercentage: Optional[float] = None


class CostAllocationTagBackfillRequest(BaseValidatorModel):
    BackfillFrom: Optional[str] = None
    RequestedAt: Optional[str] = None
    CompletedAt: Optional[str] = None
    BackfillStatus: Optional[CostAllocationTagBackfillStatusType] = None
    LastUpdatedAt: Optional[str] = None


class CostAllocationTagStatusEntry(BaseValidatorModel):
    TagKey: str
    Status: CostAllocationTagStatusType


class CostAllocationTag(BaseValidatorModel):
    TagKey: str
    Type: CostAllocationTagTypeType
    Status: CostAllocationTagStatusType
    LastUpdatedDate: Optional[str] = None
    LastUsedDate: Optional[str] = None


class CostCategoryInheritedValueDimension(BaseValidatorModel):
    DimensionName: Optional[CostCategoryInheritedValueDimensionNameType] = None
    DimensionKey: Optional[str] = None


class CostCategoryProcessingStatus(BaseValidatorModel):
    Component: Optional[Literal['COST_EXPLORER']] = None
    Status: Optional[CostCategoryStatusType] = None


class CostCategorySplitChargeRuleParameterOutput(BaseValidatorModel):
    Type: Literal['ALLOCATION_PERCENTAGES']
    Values: List[str]


class CostCategorySplitChargeRuleParameter(BaseValidatorModel):
    Type: Literal['ALLOCATION_PERCENTAGES']
    Values: List[str]


class CostCategoryValuesOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class CostCategoryValues(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class DateInterval(BaseValidatorModel):
    Start: str
    End: str


class CoverageCost(BaseValidatorModel):
    OnDemandCost: Optional[str] = None


class CoverageHours(BaseValidatorModel):
    OnDemandHours: Optional[str] = None
    ReservedHours: Optional[str] = None
    TotalRunningHours: Optional[str] = None
    CoverageHoursPercentage: Optional[str] = None


class CoverageNormalizedUnits(BaseValidatorModel):
    OnDemandNormalizedUnits: Optional[str] = None
    ReservedNormalizedUnits: Optional[str] = None
    TotalRunningNormalizedUnits: Optional[str] = None
    CoverageNormalizedUnitsPercentage: Optional[str] = None


class ResourceTag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagValuesOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class DeleteAnomalyMonitorRequest(BaseValidatorModel):
    MonitorArn: str


class DeleteAnomalySubscriptionRequest(BaseValidatorModel):
    SubscriptionArn: str


class DeleteCostCategoryDefinitionRequest(BaseValidatorModel):
    CostCategoryArn: str


class DescribeCostCategoryDefinitionRequest(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveOn: Optional[str] = None


class DimensionValuesOutput(BaseValidatorModel):
    Key: Optional[DimensionType] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class DimensionValues(BaseValidatorModel):
    Key: Optional[DimensionType] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class DimensionValuesWithAttributes(BaseValidatorModel):
    Value: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class DiskResourceUtilization(BaseValidatorModel):
    DiskReadOpsPerSecond: Optional[str] = None
    DiskWriteOpsPerSecond: Optional[str] = None
    DiskReadBytesPerSecond: Optional[str] = None
    DiskWriteBytesPerSecond: Optional[str] = None


class DynamoDBCapacityDetails(BaseValidatorModel):
    CapacityUnits: Optional[str] = None
    Region: Optional[str] = None


class EBSResourceUtilization(BaseValidatorModel):
    EbsReadOpsPerSecond: Optional[str] = None
    EbsWriteOpsPerSecond: Optional[str] = None
    EbsReadBytesPerSecond: Optional[str] = None
    EbsWriteBytesPerSecond: Optional[str] = None


class EC2InstanceDetails(BaseValidatorModel):
    Family: Optional[str] = None
    InstanceType: Optional[str] = None
    Region: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Platform: Optional[str] = None
    Tenancy: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class EC2ResourceDetails(BaseValidatorModel):
    HourlyOnDemandRate: Optional[str] = None
    InstanceType: Optional[str] = None
    Platform: Optional[str] = None
    Region: Optional[str] = None
    Sku: Optional[str] = None
    Memory: Optional[str] = None
    NetworkPerformance: Optional[str] = None
    Storage: Optional[str] = None
    Vcpu: Optional[str] = None


class NetworkResourceUtilization(BaseValidatorModel):
    NetworkInBytesPerSecond: Optional[str] = None
    NetworkOutBytesPerSecond: Optional[str] = None
    NetworkPacketsInPerSecond: Optional[str] = None
    NetworkPacketsOutPerSecond: Optional[str] = None


class EC2Specification(BaseValidatorModel):
    OfferingClass: Optional[OfferingClassType] = None


class ESInstanceDetails(BaseValidatorModel):
    InstanceClass: Optional[str] = None
    InstanceSize: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class ElastiCacheInstanceDetails(BaseValidatorModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    ProductDescription: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class GenerationSummary(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    GenerationStatus: Optional[GenerationStatusType] = None
    GenerationStartedTime: Optional[str] = None
    GenerationCompletionTime: Optional[str] = None
    EstimatedCompletionTime: Optional[str] = None


class TotalImpactFilter(BaseValidatorModel):
    NumericOperator: NumericOperatorType
    StartValue: float
    EndValue: Optional[float] = None


class GetAnomalyMonitorsRequest(BaseValidatorModel):
    MonitorArnList: Optional[List[str]] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetAnomalySubscriptionsRequest(BaseValidatorModel):
    SubscriptionArnList: Optional[List[str]] = None
    MonitorArn: Optional[str] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetApproximateUsageRecordsRequest(BaseValidatorModel):
    Granularity: GranularityType
    ApproximationDimension: ApproximationDimensionType
    Services: Optional[List[str]] = None


class GetCommitmentPurchaseAnalysisRequest(BaseValidatorModel):
    AnalysisId: str


class GroupDefinition(BaseValidatorModel):
    Type: Optional[GroupDefinitionTypeType] = None
    Key: Optional[str] = None


class SortDefinition(BaseValidatorModel):
    Key: str
    SortOrder: Optional[SortOrderType] = None


class MetricValue(BaseValidatorModel):
    Amount: Optional[str] = None
    Unit: Optional[str] = None


class ReservationPurchaseRecommendationMetadata(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    AdditionalMetadata: Optional[str] = None


class ReservationAggregates(BaseValidatorModel):
    UtilizationPercentage: Optional[str] = None
    UtilizationPercentageInUnits: Optional[str] = None
    PurchasedHours: Optional[str] = None
    PurchasedUnits: Optional[str] = None
    TotalActualHours: Optional[str] = None
    TotalActualUnits: Optional[str] = None
    UnusedHours: Optional[str] = None
    UnusedUnits: Optional[str] = None
    OnDemandCostOfRIHoursUsed: Optional[str] = None
    NetRISavings: Optional[str] = None
    TotalPotentialRISavings: Optional[str] = None
    AmortizedUpfrontFee: Optional[str] = None
    AmortizedRecurringFee: Optional[str] = None
    TotalAmortizedFee: Optional[str] = None
    RICostForUnusedHours: Optional[str] = None
    RealizedSavings: Optional[str] = None
    UnrealizedSavings: Optional[str] = None


class RightsizingRecommendationConfiguration(BaseValidatorModel):
    RecommendationTarget: RecommendationTargetType
    BenefitsConsidered: bool


class RightsizingRecommendationMetadata(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    AdditionalMetadata: Optional[str] = None


class RightsizingRecommendationSummary(BaseValidatorModel):
    TotalRecommendationCount: Optional[str] = None
    EstimatedTotalMonthlySavingsAmount: Optional[str] = None
    SavingsCurrencyCode: Optional[str] = None
    SavingsPercentage: Optional[str] = None


class GetSavingsPlanPurchaseRecommendationDetailsRequest(BaseValidatorModel):
    RecommendationDetailId: str


class SavingsPlansPurchaseRecommendationMetadata(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    AdditionalMetadata: Optional[str] = None


class MemoryDBInstanceDetails(BaseValidatorModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class RDSInstanceDetails(BaseValidatorModel):
    Family: Optional[str] = None
    InstanceType: Optional[str] = None
    Region: Optional[str] = None
    DatabaseEngine: Optional[str] = None
    DatabaseEdition: Optional[str] = None
    DeploymentOption: Optional[str] = None
    LicenseModel: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class RedshiftInstanceDetails(BaseValidatorModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class ListCommitmentPurchaseAnalysesRequest(BaseValidatorModel):
    AnalysisStatus: Optional[AnalysisStatusType] = None
    NextPageToken: Optional[str] = None
    PageSize: Optional[int] = None
    AnalysisIds: Optional[List[str]] = None


class ListCostAllocationTagBackfillHistoryRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCostAllocationTagsRequest(BaseValidatorModel):
    Status: Optional[CostAllocationTagStatusType] = None
    TagKeys: Optional[List[str]] = None
    Type: Optional[CostAllocationTagTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCostCategoryDefinitionsRequest(BaseValidatorModel):
    EffectiveOn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSavingsPlansPurchaseRecommendationGenerationRequest(BaseValidatorModel):
    GenerationStatus: Optional[GenerationStatusType] = None
    RecommendationIds: Optional[List[str]] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ProvideAnomalyFeedbackRequest(BaseValidatorModel):
    AnomalyId: str
    Feedback: AnomalyFeedbackTypeType


class RecommendationDetailHourlyMetrics(BaseValidatorModel):
    StartTime: Optional[str] = None
    EstimatedOnDemandCost: Optional[str] = None
    CurrentCoverage: Optional[str] = None
    EstimatedCoverage: Optional[str] = None
    EstimatedNewCommitmentUtilization: Optional[str] = None


class ReservationPurchaseRecommendationSummary(BaseValidatorModel):
    TotalEstimatedMonthlySavingsAmount: Optional[str] = None
    TotalEstimatedMonthlySavingsPercentage: Optional[str] = None
    CurrencyCode: Optional[str] = None


class TerminateRecommendationDetail(BaseValidatorModel):
    EstimatedMonthlySavings: Optional[str] = None
    CurrencyCode: Optional[str] = None


class RootCauseImpact(BaseValidatorModel):
    Contribution: float


class SavingsPlansAmortizedCommitment(BaseValidatorModel):
    AmortizedRecurringCommitment: Optional[str] = None
    AmortizedUpfrontCommitment: Optional[str] = None
    TotalAmortizedCommitment: Optional[str] = None


class SavingsPlansCoverageData(BaseValidatorModel):
    SpendCoveredBySavingsPlans: Optional[str] = None
    OnDemandCost: Optional[str] = None
    TotalCost: Optional[str] = None
    CoveragePercentage: Optional[str] = None


class SavingsPlansDetails(BaseValidatorModel):
    Region: Optional[str] = None
    InstanceFamily: Optional[str] = None
    OfferingId: Optional[str] = None


class SavingsPlans(BaseValidatorModel):
    PaymentOption: Optional[PaymentOptionType] = None
    SavingsPlansType: Optional[SupportedSavingsPlansTypeType] = None
    Region: Optional[str] = None
    InstanceFamily: Optional[str] = None
    TermInYears: Optional[TermInYearsType] = None
    SavingsPlansCommitment: Optional[float] = None
    OfferingId: Optional[str] = None


class SavingsPlansPurchaseRecommendationSummary(BaseValidatorModel):
    EstimatedROI: Optional[str] = None
    CurrencyCode: Optional[str] = None
    EstimatedTotalCost: Optional[str] = None
    CurrentOnDemandSpend: Optional[str] = None
    EstimatedSavingsAmount: Optional[str] = None
    TotalRecommendationCount: Optional[str] = None
    DailyCommitmentToPurchase: Optional[str] = None
    HourlyCommitmentToPurchase: Optional[str] = None
    EstimatedSavingsPercentage: Optional[str] = None
    EstimatedMonthlySavingsAmount: Optional[str] = None
    EstimatedOnDemandCostWithCurrentCommitment: Optional[str] = None


class SavingsPlansSavings(BaseValidatorModel):
    NetSavings: Optional[str] = None
    OnDemandCostEquivalent: Optional[str] = None


class SavingsPlansUtilization(BaseValidatorModel):
    TotalCommitment: Optional[str] = None
    UsedCommitment: Optional[str] = None
    UnusedCommitment: Optional[str] = None
    UtilizationPercentage: Optional[str] = None


class StartCostAllocationTagBackfillRequest(BaseValidatorModel):
    BackfillFrom: str


class TagValues(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    ResourceTagKeys: List[str]


class UpdateAnomalyMonitorRequest(BaseValidatorModel):
    MonitorArn: str
    MonitorName: Optional[str] = None


class UpdateCostAllocationTagsStatusError(BaseValidatorModel):
    TagKey: Optional[str] = None
    Code: Optional[str] = None
    Message: Optional[str] = None


class UpdateCostAllocationTagsStatusRequest(BaseValidatorModel):
    CostAllocationTagsStatus: List[CostAllocationTagStatusEntry]


class CostCategoryReference(BaseValidatorModel):
    CostCategoryArn: Optional[str] = None
    Name: Optional[str] = None
    EffectiveStart: Optional[str] = None
    EffectiveEnd: Optional[str] = None
    NumberOfRules: Optional[int] = None
    ProcessingStatus: Optional[List[CostCategoryProcessingStatus]] = None
    Values: Optional[List[str]] = None
    DefaultValue: Optional[str] = None


class CostCategorySplitChargeRuleOutput(BaseValidatorModel):
    Source: str
    Targets: List[str]
    Method: CostCategorySplitChargeMethodType
    Parameters: Optional[List[CostCategorySplitChargeRuleParameterOutput]] = None

CostCategorySplitChargeRuleParameterUnion = Union[CostCategorySplitChargeRuleParameter, CostCategorySplitChargeRuleParameterOutput]

CostCategoryValuesUnion = Union[CostCategoryValues, CostCategoryValuesOutput]


class ForecastResult(BaseValidatorModel):
    TimePeriod: Optional[DateInterval] = None
    MeanValue: Optional[str] = None
    PredictionIntervalLowerBound: Optional[str] = None
    PredictionIntervalUpperBound: Optional[str] = None


class Coverage(BaseValidatorModel):
    CoverageHours: Optional[CoverageHours] = None
    CoverageNormalizedUnits: Optional[CoverageNormalizedUnits] = None
    CoverageCost: Optional[CoverageCost] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: List[ResourceTag]


class CreateAnomalyMonitorResponse(BaseValidatorModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadata


class CreateAnomalySubscriptionResponse(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadata


class CreateCostCategoryDefinitionResponse(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveStart: str
    ResponseMetadata: ResponseMetadata


class DeleteCostCategoryDefinitionResponse(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveEnd: str
    ResponseMetadata: ResponseMetadata


class GetApproximateUsageRecordsResponse(BaseValidatorModel):
    Services: Dict[str, int]
    TotalRecords: int
    LookbackPeriod: DateInterval
    ResponseMetadata: ResponseMetadata


class GetCostCategoriesResponse(BaseValidatorModel):
    NextPageToken: str
    CostCategoryNames: List[str]
    CostCategoryValues: List[str]
    ReturnSize: int
    TotalSize: int
    ResponseMetadata: ResponseMetadata


class GetTagsResponse(BaseValidatorModel):
    NextPageToken: str
    Tags: List[str]
    ReturnSize: int
    TotalSize: int
    ResponseMetadata: ResponseMetadata


class ListCostAllocationTagBackfillHistoryResponse(BaseValidatorModel):
    BackfillRequests: List[CostAllocationTagBackfillRequest]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCostAllocationTagsResponse(BaseValidatorModel):
    CostAllocationTags: List[CostAllocationTag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


class ProvideAnomalyFeedbackResponse(BaseValidatorModel):
    AnomalyId: str
    ResponseMetadata: ResponseMetadata


class StartCommitmentPurchaseAnalysisResponse(BaseValidatorModel):
    AnalysisId: str
    AnalysisStartedTime: str
    EstimatedCompletionTime: str
    ResponseMetadata: ResponseMetadata


class StartCostAllocationTagBackfillResponse(BaseValidatorModel):
    BackfillRequest: CostAllocationTagBackfillRequest
    ResponseMetadata: ResponseMetadata


class StartSavingsPlansPurchaseRecommendationGenerationResponse(BaseValidatorModel):
    RecommendationId: str
    GenerationStartedTime: str
    EstimatedCompletionTime: str
    ResponseMetadata: ResponseMetadata


class UpdateAnomalyMonitorResponse(BaseValidatorModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadata


class UpdateAnomalySubscriptionResponse(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadata


class UpdateCostCategoryDefinitionResponse(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveStart: str
    ResponseMetadata: ResponseMetadata


class ExpressionOutput(BaseValidatorModel):
    or_: Optional[List[Dict[str, Any]]] = None
    And: Optional[List[Dict[str, Any]]] = None
    Not: Optional[Dict[str, Any]] = None
    Dimensions: Optional[DimensionValuesOutput] = None
    Tags: Optional[TagValuesOutput] = None
    CostCategories: Optional[CostCategoryValuesOutput] = None

DimensionValuesUnion = Union[DimensionValues, DimensionValuesOutput]


class GetDimensionValuesResponse(BaseValidatorModel):
    DimensionValues: List[DimensionValuesWithAttributes]
    ReturnSize: int
    TotalSize: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ReservedCapacityDetails(BaseValidatorModel):
    DynamoDBCapacityDetails: Optional[DynamoDBCapacityDetails] = None


class ResourceDetails(BaseValidatorModel):
    EC2ResourceDetails: Optional[EC2ResourceDetails] = None


class EC2ResourceUtilization(BaseValidatorModel):
    MaxCpuUtilizationPercentage: Optional[str] = None
    MaxMemoryUtilizationPercentage: Optional[str] = None
    MaxStorageUtilizationPercentage: Optional[str] = None
    EBSResourceUtilization: Optional[EBSResourceUtilization] = None
    DiskResourceUtilization: Optional[DiskResourceUtilization] = None
    NetworkResourceUtilization: Optional[NetworkResourceUtilization] = None


class ServiceSpecification(BaseValidatorModel):
    EC2Specification: Optional[EC2Specification] = None


class ListSavingsPlansPurchaseRecommendationGenerationResponse(BaseValidatorModel):
    GenerationSummaryList: List[GenerationSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetAnomaliesRequest(BaseValidatorModel):
    DateInterval: AnomalyDateInterval
    MonitorArn: Optional[str] = None
    Feedback: Optional[AnomalyFeedbackTypeType] = None
    TotalImpact: Optional[TotalImpactFilter] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Group(BaseValidatorModel):
    Keys: Optional[List[str]] = None
    Metrics: Optional[Dict[str, MetricValue]] = None


class ReservationUtilizationGroup(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    Utilization: Optional[ReservationAggregates] = None


class InstanceDetails(BaseValidatorModel):
    EC2InstanceDetails: Optional[EC2InstanceDetails] = None
    RDSInstanceDetails: Optional[RDSInstanceDetails] = None
    RedshiftInstanceDetails: Optional[RedshiftInstanceDetails] = None
    ElastiCacheInstanceDetails: Optional[ElastiCacheInstanceDetails] = None
    ESInstanceDetails: Optional[ESInstanceDetails] = None
    MemoryDBInstanceDetails: Optional[MemoryDBInstanceDetails] = None


class RecommendationDetailData(BaseValidatorModel):
    AccountScope: Optional[AccountScopeType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    SavingsPlansType: Optional[SupportedSavingsPlansTypeType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    AccountId: Optional[str] = None
    CurrencyCode: Optional[str] = None
    InstanceFamily: Optional[str] = None
    Region: Optional[str] = None
    OfferingId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    LatestUsageTimestamp: Optional[str] = None
    CurrentAverageHourlyOnDemandSpend: Optional[str] = None
    CurrentMaximumHourlyOnDemandSpend: Optional[str] = None
    CurrentMinimumHourlyOnDemandSpend: Optional[str] = None
    EstimatedAverageUtilization: Optional[str] = None
    EstimatedMonthlySavingsAmount: Optional[str] = None
    EstimatedOnDemandCost: Optional[str] = None
    EstimatedOnDemandCostWithCurrentCommitment: Optional[str] = None
    EstimatedROI: Optional[str] = None
    EstimatedSPCost: Optional[str] = None
    EstimatedSavingsAmount: Optional[str] = None
    EstimatedSavingsPercentage: Optional[str] = None
    ExistingHourlyCommitment: Optional[str] = None
    HourlyCommitmentToPurchase: Optional[str] = None
    UpfrontCost: Optional[str] = None
    CurrentAverageCoverage: Optional[str] = None
    EstimatedAverageCoverage: Optional[str] = None
    MetricsOverLookbackPeriod: Optional[List[RecommendationDetailHourlyMetrics]] = None


class SavingsPlansPurchaseAnalysisDetails(BaseValidatorModel):
    CurrencyCode: Optional[str] = None
    LookbackPeriodInHours: Optional[str] = None
    CurrentAverageCoverage: Optional[str] = None
    CurrentAverageHourlyOnDemandSpend: Optional[str] = None
    CurrentMaximumHourlyOnDemandSpend: Optional[str] = None
    CurrentMinimumHourlyOnDemandSpend: Optional[str] = None
    CurrentOnDemandSpend: Optional[str] = None
    ExistingHourlyCommitment: Optional[str] = None
    HourlyCommitmentToPurchase: Optional[str] = None
    EstimatedAverageCoverage: Optional[str] = None
    EstimatedAverageUtilization: Optional[str] = None
    EstimatedMonthlySavingsAmount: Optional[str] = None
    EstimatedOnDemandCost: Optional[str] = None
    EstimatedOnDemandCostWithCurrentCommitment: Optional[str] = None
    EstimatedROI: Optional[str] = None
    EstimatedSavingsAmount: Optional[str] = None
    EstimatedSavingsPercentage: Optional[str] = None
    EstimatedCommitmentCost: Optional[str] = None
    LatestUsageTimestamp: Optional[str] = None
    UpfrontCost: Optional[str] = None
    AdditionalMetadata: Optional[str] = None
    MetricsOverLookbackPeriod: Optional[List[RecommendationDetailHourlyMetrics]] = None


class RootCause(BaseValidatorModel):
    Service: Optional[str] = None
    Region: Optional[str] = None
    LinkedAccount: Optional[str] = None
    LinkedAccountName: Optional[str] = None
    UsageType: Optional[str] = None
    Impact: Optional[RootCauseImpact] = None


class SavingsPlansCoverage(BaseValidatorModel):
    Attributes: Optional[Dict[str, str]] = None
    Coverage: Optional[SavingsPlansCoverageData] = None
    TimePeriod: Optional[DateInterval] = None


class SavingsPlansPurchaseRecommendationDetail(BaseValidatorModel):
    SavingsPlansDetails: Optional[SavingsPlansDetails] = None
    AccountId: Optional[str] = None
    UpfrontCost: Optional[str] = None
    EstimatedROI: Optional[str] = None
    CurrencyCode: Optional[str] = None
    EstimatedSPCost: Optional[str] = None
    EstimatedOnDemandCost: Optional[str] = None
    EstimatedOnDemandCostWithCurrentCommitment: Optional[str] = None
    EstimatedSavingsAmount: Optional[str] = None
    EstimatedSavingsPercentage: Optional[str] = None
    HourlyCommitmentToPurchase: Optional[str] = None
    EstimatedAverageUtilization: Optional[str] = None
    EstimatedMonthlySavingsAmount: Optional[str] = None
    CurrentMinimumHourlyOnDemandSpend: Optional[str] = None
    CurrentMaximumHourlyOnDemandSpend: Optional[str] = None
    CurrentAverageHourlyOnDemandSpend: Optional[str] = None
    RecommendationDetailId: Optional[str] = None


class SavingsPlansPurchaseAnalysisConfigurationOutput(BaseValidatorModel):
    AnalysisType: AnalysisTypeType
    SavingsPlansToAdd: List[SavingsPlans]
    LookBackTimePeriod: DateInterval
    AccountScope: Optional[AccountScopeType] = None
    AccountId: Optional[str] = None
    SavingsPlansToExclude: Optional[List[str]] = None


class SavingsPlansPurchaseAnalysisConfiguration(BaseValidatorModel):
    AnalysisType: AnalysisTypeType
    SavingsPlansToAdd: List[SavingsPlans]
    LookBackTimePeriod: DateInterval
    AccountScope: Optional[AccountScopeType] = None
    AccountId: Optional[str] = None
    SavingsPlansToExclude: Optional[List[str]] = None


class SavingsPlansUtilizationAggregates(BaseValidatorModel):
    Utilization: SavingsPlansUtilization
    Savings: Optional[SavingsPlansSavings] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitment] = None


class SavingsPlansUtilizationByTime(BaseValidatorModel):
    TimePeriod: DateInterval
    Utilization: SavingsPlansUtilization
    Savings: Optional[SavingsPlansSavings] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitment] = None


class SavingsPlansUtilizationDetail(BaseValidatorModel):
    SavingsPlanArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    Utilization: Optional[SavingsPlansUtilization] = None
    Savings: Optional[SavingsPlansSavings] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitment] = None

TagValuesUnion = Union[TagValues, TagValuesOutput]


class UpdateCostAllocationTagsStatusResponse(BaseValidatorModel):
    Errors: List[UpdateCostAllocationTagsStatusError]
    ResponseMetadata: ResponseMetadata


class ListCostCategoryDefinitionsResponse(BaseValidatorModel):
    CostCategoryReferences: List[CostCategoryReference]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CostCategorySplitChargeRule(BaseValidatorModel):
    Source: str
    Targets: List[str]
    Method: CostCategorySplitChargeMethodType
    Parameters: Optional[List[CostCategorySplitChargeRuleParameterUnion]] = None


class GetCostForecastResponse(BaseValidatorModel):
    Total: MetricValue
    ForecastResultsByTime: List[ForecastResult]
    ResponseMetadata: ResponseMetadata


class GetUsageForecastResponse(BaseValidatorModel):
    Total: MetricValue
    ForecastResultsByTime: List[ForecastResult]
    ResponseMetadata: ResponseMetadata


class ReservationCoverageGroup(BaseValidatorModel):
    Attributes: Optional[Dict[str, str]] = None
    Coverage: Optional[Coverage] = None


class AnomalyMonitorOutput(BaseValidatorModel):
    MonitorName: str
    MonitorType: MonitorTypeType
    MonitorArn: Optional[str] = None
    CreationDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    LastEvaluatedDate: Optional[str] = None
    MonitorDimension: Optional[Literal['SERVICE']] = None
    MonitorSpecification: Optional[ExpressionOutput] = None
    DimensionalValueCount: Optional[int] = None


class AnomalySubscriptionOutput(BaseValidatorModel):
    MonitorArnList: List[str]
    Subscribers: List[Subscriber]
    Frequency: AnomalySubscriptionFrequencyType
    SubscriptionName: str
    SubscriptionArn: Optional[str] = None
    AccountId: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdExpression: Optional[ExpressionOutput] = None


class CostCategoryRuleOutput(BaseValidatorModel):
    Value: Optional[str] = None
    Rule: Optional[ExpressionOutput] = None
    InheritedValue: Optional[CostCategoryInheritedValueDimension] = None
    Type: Optional[CostCategoryRuleTypeType] = None


class ResourceUtilization(BaseValidatorModel):
    EC2ResourceUtilization: Optional[EC2ResourceUtilization] = None


class ResultByTime(BaseValidatorModel):
    TimePeriod: Optional[DateInterval] = None
    Total: Optional[Dict[str, MetricValue]] = None
    Groups: Optional[List[Group]] = None
    Estimated: Optional[bool] = None


class UtilizationByTime(BaseValidatorModel):
    TimePeriod: Optional[DateInterval] = None
    Groups: Optional[List[ReservationUtilizationGroup]] = None
    Total: Optional[ReservationAggregates] = None


class ReservationPurchaseRecommendationDetail(BaseValidatorModel):
    AccountId: Optional[str] = None
    InstanceDetails: Optional[InstanceDetails] = None
    RecommendedNumberOfInstancesToPurchase: Optional[str] = None
    RecommendedNormalizedUnitsToPurchase: Optional[str] = None
    MinimumNumberOfInstancesUsedPerHour: Optional[str] = None
    MinimumNormalizedUnitsUsedPerHour: Optional[str] = None
    MaximumNumberOfInstancesUsedPerHour: Optional[str] = None
    MaximumNormalizedUnitsUsedPerHour: Optional[str] = None
    AverageNumberOfInstancesUsedPerHour: Optional[str] = None
    AverageNormalizedUnitsUsedPerHour: Optional[str] = None
    AverageUtilization: Optional[str] = None
    EstimatedBreakEvenInMonths: Optional[str] = None
    CurrencyCode: Optional[str] = None
    EstimatedMonthlySavingsAmount: Optional[str] = None
    EstimatedMonthlySavingsPercentage: Optional[str] = None
    EstimatedMonthlyOnDemandCost: Optional[str] = None
    EstimatedReservationCostForLookbackPeriod: Optional[str] = None
    UpfrontCost: Optional[str] = None
    RecurringStandardMonthlyCost: Optional[str] = None
    ReservedCapacityDetails: Optional[ReservedCapacityDetails] = None
    RecommendedNumberOfCapacityUnitsToPurchase: Optional[str] = None
    MinimumNumberOfCapacityUnitsUsedPerHour: Optional[str] = None
    MaximumNumberOfCapacityUnitsUsedPerHour: Optional[str] = None
    AverageNumberOfCapacityUnitsUsedPerHour: Optional[str] = None


class GetSavingsPlanPurchaseRecommendationDetailsResponse(BaseValidatorModel):
    RecommendationDetailId: str
    RecommendationDetailData: RecommendationDetailData
    ResponseMetadata: ResponseMetadata


class AnalysisDetails(BaseValidatorModel):
    SavingsPlansPurchaseAnalysisDetails: Optional[SavingsPlansPurchaseAnalysisDetails] = None


class Anomaly(BaseValidatorModel):
    AnomalyId: str
    AnomalyScore: AnomalyScore
    Impact: Impact
    MonitorArn: str
    AnomalyStartDate: Optional[str] = None
    AnomalyEndDate: Optional[str] = None
    DimensionValue: Optional[str] = None
    RootCauses: Optional[List[RootCause]] = None
    Feedback: Optional[AnomalyFeedbackTypeType] = None


class GetSavingsPlansCoverageResponse(BaseValidatorModel):
    SavingsPlansCoverages: List[SavingsPlansCoverage]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SavingsPlansPurchaseRecommendation(BaseValidatorModel):
    AccountScope: Optional[AccountScopeType] = None
    SavingsPlansType: Optional[SupportedSavingsPlansTypeType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    SavingsPlansPurchaseRecommendationDetails: Optional[List[SavingsPlansPurchaseRecommendationDetail]] = None
    SavingsPlansPurchaseRecommendationSummary: Optional[SavingsPlansPurchaseRecommendationSummary] = None


class CommitmentPurchaseAnalysisConfigurationOutput(BaseValidatorModel):
    SavingsPlansPurchaseAnalysisConfiguration: Optional[SavingsPlansPurchaseAnalysisConfigurationOutput] = None


class CommitmentPurchaseAnalysisConfiguration(BaseValidatorModel):
    SavingsPlansPurchaseAnalysisConfiguration: Optional[SavingsPlansPurchaseAnalysisConfiguration] = None


class GetSavingsPlansUtilizationResponse(BaseValidatorModel):
    SavingsPlansUtilizationsByTime: List[SavingsPlansUtilizationByTime]
    Total: SavingsPlansUtilizationAggregates
    ResponseMetadata: ResponseMetadata


class GetSavingsPlansUtilizationDetailsResponse(BaseValidatorModel):
    SavingsPlansUtilizationDetails: List[SavingsPlansUtilizationDetail]
    Total: SavingsPlansUtilizationAggregates
    TimePeriod: DateInterval
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Expression(BaseValidatorModel):
    or_: Optional[List[Dict[str, Any]]] = None
    And: Optional[List[Dict[str, Any]]] = None
    Not: Optional[Dict[str, Any]] = None
    Dimensions: Optional[DimensionValuesUnion] = None
    Tags: Optional[TagValuesUnion] = None
    CostCategories: Optional[CostCategoryValuesUnion] = None

CostCategorySplitChargeRuleUnion = Union[CostCategorySplitChargeRule, CostCategorySplitChargeRuleOutput]


class CoverageByTime(BaseValidatorModel):
    TimePeriod: Optional[DateInterval] = None
    Groups: Optional[List[ReservationCoverageGroup]] = None
    Total: Optional[Coverage] = None


class GetAnomalyMonitorsResponse(BaseValidatorModel):
    AnomalyMonitors: List[AnomalyMonitorOutput]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetAnomalySubscriptionsResponse(BaseValidatorModel):
    AnomalySubscriptions: List[AnomalySubscriptionOutput]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class CostCategory(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveStart: str
    Name: str
    RuleVersion: Literal['CostCategoryExpression.v1']
    Rules: List[CostCategoryRuleOutput]
    EffectiveEnd: Optional[str] = None
    SplitChargeRules: Optional[List[CostCategorySplitChargeRuleOutput]] = None
    ProcessingStatus: Optional[List[CostCategoryProcessingStatus]] = None
    DefaultValue: Optional[str] = None


class CurrentInstance(BaseValidatorModel):
    ResourceId: Optional[str] = None
    InstanceName: Optional[str] = None
    Tags: Optional[List[TagValuesOutput]] = None
    ResourceDetails: Optional[ResourceDetails] = None
    ResourceUtilization: Optional[ResourceUtilization] = None
    ReservationCoveredHoursInLookbackPeriod: Optional[str] = None
    SavingsPlansCoveredHoursInLookbackPeriod: Optional[str] = None
    OnDemandHoursInLookbackPeriod: Optional[str] = None
    TotalRunningHoursInLookbackPeriod: Optional[str] = None
    MonthlyCost: Optional[str] = None
    CurrencyCode: Optional[str] = None


class TargetInstance(BaseValidatorModel):
    EstimatedMonthlyCost: Optional[str] = None
    EstimatedMonthlySavings: Optional[str] = None
    CurrencyCode: Optional[str] = None
    DefaultTargetInstance: Optional[bool] = None
    ResourceDetails: Optional[ResourceDetails] = None
    ExpectedResourceUtilization: Optional[ResourceUtilization] = None
    PlatformDifferences: Optional[List[PlatformDifferenceType]] = None


class GetCostAndUsageResponse(BaseValidatorModel):
    NextPageToken: str
    GroupDefinitions: List[GroupDefinition]
    ResultsByTime: List[ResultByTime]
    DimensionValueAttributes: List[DimensionValuesWithAttributes]
    ResponseMetadata: ResponseMetadata


class GetCostAndUsageWithResourcesResponse(BaseValidatorModel):
    NextPageToken: str
    GroupDefinitions: List[GroupDefinition]
    ResultsByTime: List[ResultByTime]
    DimensionValueAttributes: List[DimensionValuesWithAttributes]
    ResponseMetadata: ResponseMetadata


class GetReservationUtilizationResponse(BaseValidatorModel):
    UtilizationsByTime: List[UtilizationByTime]
    Total: ReservationAggregates
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ReservationPurchaseRecommendation(BaseValidatorModel):
    AccountScope: Optional[AccountScopeType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    ServiceSpecification: Optional[ServiceSpecification] = None
    RecommendationDetails: Optional[List[ReservationPurchaseRecommendationDetail]] = None
    RecommendationSummary: Optional[ReservationPurchaseRecommendationSummary] = None


class GetAnomaliesResponse(BaseValidatorModel):
    Anomalies: List[Anomaly]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetSavingsPlansPurchaseRecommendationResponse(BaseValidatorModel):
    Metadata: SavingsPlansPurchaseRecommendationMetadata
    SavingsPlansPurchaseRecommendation: SavingsPlansPurchaseRecommendation
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class AnalysisSummary(BaseValidatorModel):
    EstimatedCompletionTime: Optional[str] = None
    AnalysisCompletionTime: Optional[str] = None
    AnalysisStartedTime: Optional[str] = None
    AnalysisStatus: Optional[AnalysisStatusType] = None
    ErrorCode: Optional[ErrorCodeType] = None
    AnalysisId: Optional[str] = None
    CommitmentPurchaseAnalysisConfiguration: Optional[CommitmentPurchaseAnalysisConfigurationOutput] = None


class GetCommitmentPurchaseAnalysisResponse(BaseValidatorModel):
    EstimatedCompletionTime: str
    AnalysisCompletionTime: str
    AnalysisStartedTime: str
    AnalysisId: str
    AnalysisStatus: AnalysisStatusType
    ErrorCode: ErrorCodeType
    AnalysisDetails: AnalysisDetails
    CommitmentPurchaseAnalysisConfiguration: CommitmentPurchaseAnalysisConfigurationOutput
    ResponseMetadata: ResponseMetadata

CommitmentPurchaseAnalysisConfigurationUnion = Union[CommitmentPurchaseAnalysisConfiguration, CommitmentPurchaseAnalysisConfigurationOutput]


class AnomalyMonitor(BaseValidatorModel):
    MonitorName: str
    MonitorType: MonitorTypeType
    MonitorArn: Optional[str] = None
    CreationDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    LastEvaluatedDate: Optional[str] = None
    MonitorDimension: Optional[Literal['SERVICE']] = None
    MonitorSpecification: Optional[Expression] = None
    DimensionalValueCount: Optional[int] = None


class AnomalySubscription(BaseValidatorModel):
    MonitorArnList: List[str]
    Subscribers: List[Subscriber]
    Frequency: AnomalySubscriptionFrequencyType
    SubscriptionName: str
    SubscriptionArn: Optional[str] = None
    AccountId: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdExpression: Optional[Expression] = None

ExpressionUnion = Union[Expression, ExpressionOutput]


class GetReservationCoverageResponse(BaseValidatorModel):
    CoveragesByTime: List[CoverageByTime]
    Total: Coverage
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class DescribeCostCategoryDefinitionResponse(BaseValidatorModel):
    CostCategory: CostCategory
    ResponseMetadata: ResponseMetadata


class ModifyRecommendationDetail(BaseValidatorModel):
    TargetInstances: Optional[List[TargetInstance]] = None


class GetReservationPurchaseRecommendationResponse(BaseValidatorModel):
    Metadata: ReservationPurchaseRecommendationMetadata
    Recommendations: List[ReservationPurchaseRecommendation]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListCommitmentPurchaseAnalysesResponse(BaseValidatorModel):
    AnalysisSummaryList: List[AnalysisSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class StartCommitmentPurchaseAnalysisRequest(BaseValidatorModel):
    CommitmentPurchaseAnalysisConfiguration: CommitmentPurchaseAnalysisConfigurationUnion

AnomalyMonitorUnion = Union[AnomalyMonitor, AnomalyMonitorOutput]

AnomalySubscriptionUnion = Union[AnomalySubscription, AnomalySubscriptionOutput]


class CostCategoryRule(BaseValidatorModel):
    Value: Optional[str] = None
    Rule: Optional[ExpressionUnion] = None
    InheritedValue: Optional[CostCategoryInheritedValueDimension] = None
    Type: Optional[CostCategoryRuleTypeType] = None


class GetCostAndUsageRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    Granularity: GranularityType
    Metrics: List[str]
    Filter: Optional[ExpressionUnion] = None
    GroupBy: Optional[List[GroupDefinition]] = None
    BillingViewArn: Optional[str] = None
    NextPageToken: Optional[str] = None


class GetCostAndUsageWithResourcesRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    Granularity: GranularityType
    Filter: ExpressionUnion
    Metrics: Optional[List[str]] = None
    GroupBy: Optional[List[GroupDefinition]] = None
    BillingViewArn: Optional[str] = None
    NextPageToken: Optional[str] = None


class GetCostCategoriesRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    SearchString: Optional[str] = None
    CostCategoryName: Optional[str] = None
    Filter: Optional[ExpressionUnion] = None
    SortBy: Optional[List[SortDefinition]] = None
    BillingViewArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetCostForecastRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    Metric: MetricType
    Granularity: GranularityType
    Filter: Optional[ExpressionUnion] = None
    BillingViewArn: Optional[str] = None
    PredictionIntervalLevel: Optional[int] = None


class GetDimensionValuesRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    Dimension: DimensionType
    SearchString: Optional[str] = None
    Context: Optional[ContextType] = None
    Filter: Optional[ExpressionUnion] = None
    SortBy: Optional[List[SortDefinition]] = None
    BillingViewArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetReservationCoverageRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    GroupBy: Optional[List[GroupDefinition]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional[ExpressionUnion] = None
    Metrics: Optional[List[str]] = None
    NextPageToken: Optional[str] = None
    SortBy: Optional[SortDefinition] = None
    MaxResults: Optional[int] = None


class GetReservationPurchaseRecommendationRequest(BaseValidatorModel):
    Service: str
    AccountId: Optional[str] = None
    Filter: Optional[ExpressionUnion] = None
    AccountScope: Optional[AccountScopeType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    ServiceSpecification: Optional[ServiceSpecification] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetReservationUtilizationRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    GroupBy: Optional[List[GroupDefinition]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional[ExpressionUnion] = None
    SortBy: Optional[SortDefinition] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetRightsizingRecommendationRequest(BaseValidatorModel):
    Service: str
    Filter: Optional[ExpressionUnion] = None
    Configuration: Optional[RightsizingRecommendationConfiguration] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetSavingsPlansCoverageRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    GroupBy: Optional[List[GroupDefinition]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional[ExpressionUnion] = None
    Metrics: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[SortDefinition] = None


class GetSavingsPlansPurchaseRecommendationRequest(BaseValidatorModel):
    SavingsPlansType: SupportedSavingsPlansTypeType
    TermInYears: TermInYearsType
    PaymentOption: PaymentOptionType
    LookbackPeriodInDays: LookbackPeriodInDaysType
    AccountScope: Optional[AccountScopeType] = None
    NextPageToken: Optional[str] = None
    PageSize: Optional[int] = None
    Filter: Optional[ExpressionUnion] = None


class GetSavingsPlansUtilizationDetailsRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    Filter: Optional[ExpressionUnion] = None
    DataType: Optional[List[SavingsPlansDataTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[SortDefinition] = None


class GetSavingsPlansUtilizationRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    Granularity: Optional[GranularityType] = None
    Filter: Optional[ExpressionUnion] = None
    SortBy: Optional[SortDefinition] = None


class GetTagsRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    SearchString: Optional[str] = None
    TagKey: Optional[str] = None
    Filter: Optional[ExpressionUnion] = None
    SortBy: Optional[List[SortDefinition]] = None
    BillingViewArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetUsageForecastRequest(BaseValidatorModel):
    TimePeriod: DateInterval
    Metric: MetricType
    Granularity: GranularityType
    Filter: Optional[ExpressionUnion] = None
    BillingViewArn: Optional[str] = None
    PredictionIntervalLevel: Optional[int] = None


class UpdateAnomalySubscriptionRequest(BaseValidatorModel):
    SubscriptionArn: str
    Threshold: Optional[float] = None
    Frequency: Optional[AnomalySubscriptionFrequencyType] = None
    MonitorArnList: Optional[List[str]] = None
    Subscribers: Optional[List[Subscriber]] = None
    SubscriptionName: Optional[str] = None
    ThresholdExpression: Optional[ExpressionUnion] = None


class RightsizingRecommendation(BaseValidatorModel):
    AccountId: Optional[str] = None
    CurrentInstance: Optional[CurrentInstance] = None
    RightsizingType: Optional[RightsizingTypeType] = None
    ModifyRecommendationDetail: Optional[ModifyRecommendationDetail] = None
    TerminateRecommendationDetail: Optional[TerminateRecommendationDetail] = None
    FindingReasonCodes: Optional[List[FindingReasonCodeType]] = None


class CreateAnomalyMonitorRequest(BaseValidatorModel):
    AnomalyMonitor: AnomalyMonitorUnion
    ResourceTags: Optional[List[ResourceTag]] = None


class CreateAnomalySubscriptionRequest(BaseValidatorModel):
    AnomalySubscription: AnomalySubscriptionUnion
    ResourceTags: Optional[List[ResourceTag]] = None

CostCategoryRuleUnion = Union[CostCategoryRule, CostCategoryRuleOutput]


class GetRightsizingRecommendationResponse(BaseValidatorModel):
    Metadata: RightsizingRecommendationMetadata
    Summary: RightsizingRecommendationSummary
    RightsizingRecommendations: List[RightsizingRecommendation]
    NextPageToken: str
    Configuration: RightsizingRecommendationConfiguration
    ResponseMetadata: ResponseMetadata


class CreateCostCategoryDefinitionRequest(BaseValidatorModel):
    Name: str
    RuleVersion: Literal['CostCategoryExpression.v1']
    Rules: List[CostCategoryRuleUnion]
    EffectiveStart: Optional[str] = None
    DefaultValue: Optional[str] = None
    SplitChargeRules: Optional[List[CostCategorySplitChargeRuleUnion]] = None
    ResourceTags: Optional[List[ResourceTag]] = None


class UpdateCostCategoryDefinitionRequest(BaseValidatorModel):
    CostCategoryArn: str
    RuleVersion: Literal['CostCategoryExpression.v1']
    Rules: List[CostCategoryRuleUnion]
    EffectiveStart: Optional[str] = None
    DefaultValue: Optional[str] = None
    SplitChargeRules: Optional[List[CostCategorySplitChargeRuleUnion]] = None
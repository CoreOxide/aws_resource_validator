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
from aws_resource_validator.pydantic_models.ce_constants import *

class AnomalyDateIntervalTypeDef(BaseModel):
    StartDate: str
    EndDate: Optional[str] = None

class AnomalyMonitorTypeDef(BaseModel):
    MonitorName: str
    MonitorType: MonitorTypeType
    MonitorArn: Optional[str] = None
    CreationDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    LastEvaluatedDate: Optional[str] = None
    MonitorDimension: Optional[Literal["SERVICE"]] = None
    MonitorSpecification: Optional["ExpressionTypeDef"] = None
    DimensionalValueCount: Optional[int] = None

class AnomalyScoreTypeDef(BaseModel):
    MaxScore: float
    CurrentScore: float

class SubscriberTypeDef(BaseModel):
    Address: Optional[str] = None
    Type: Optional[SubscriberTypeType] = None
    Status: Optional[SubscriberStatusType] = None

class ImpactTypeDef(BaseModel):
    MaxImpact: float
    TotalImpact: Optional[float] = None
    TotalActualSpend: Optional[float] = None
    TotalExpectedSpend: Optional[float] = None
    TotalImpactPercentage: Optional[float] = None

class RootCauseTypeDef(BaseModel):
    Service: Optional[str] = None
    Region: Optional[str] = None
    LinkedAccount: Optional[str] = None
    UsageType: Optional[str] = None
    LinkedAccountName: Optional[str] = None

class CostAllocationTagBackfillRequestTypeDef(BaseModel):
    BackfillFrom: Optional[str] = None
    RequestedAt: Optional[str] = None
    CompletedAt: Optional[str] = None
    BackfillStatus: Optional[CostAllocationTagBackfillStatusType] = None
    LastUpdatedAt: Optional[str] = None

class CostAllocationTagStatusEntryTypeDef(BaseModel):
    TagKey: str
    Status: CostAllocationTagStatusType

class CostAllocationTagTypeDef(BaseModel):
    TagKey: str
    Type: CostAllocationTagTypeType
    Status: CostAllocationTagStatusType
    LastUpdatedDate: Optional[str] = None
    LastUsedDate: Optional[str] = None

class CostCategoryInheritedValueDimensionTypeDef(BaseModel):
    DimensionName: Optional[CostCategoryInheritedValueDimensionNameType] = None
    DimensionKey: Optional[str] = None

class CostCategoryProcessingStatusTypeDef(BaseModel):
    Component: Optional[Literal["COST_EXPLORER"]] = None
    Status: Optional[CostCategoryStatusType] = None

class CostCategorySplitChargeRuleParameterTypeDef(BaseModel):
    Type: Literal["ALLOCATION_PERCENTAGES"]
    Values: Sequence[str]

class CostCategoryValuesTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    MatchOptions: Optional[Sequence[MatchOptionType]] = None

class DateIntervalTypeDef(BaseModel):
    Start: str
    End: str

class CoverageCostTypeDef(BaseModel):
    OnDemandCost: Optional[str] = None

class CoverageHoursTypeDef(BaseModel):
    OnDemandHours: Optional[str] = None
    ReservedHours: Optional[str] = None
    TotalRunningHours: Optional[str] = None
    CoverageHoursPercentage: Optional[str] = None

class CoverageNormalizedUnitsTypeDef(BaseModel):
    OnDemandNormalizedUnits: Optional[str] = None
    ReservedNormalizedUnits: Optional[str] = None
    TotalRunningNormalizedUnits: Optional[str] = None
    CoverageNormalizedUnitsPercentage: Optional[str] = None

class ResourceTagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagValuesTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    MatchOptions: Optional[Sequence[MatchOptionType]] = None

class DeleteAnomalyMonitorRequestRequestTypeDef(BaseModel):
    MonitorArn: str

class DeleteAnomalySubscriptionRequestRequestTypeDef(BaseModel):
    SubscriptionArn: str

class DeleteCostCategoryDefinitionRequestRequestTypeDef(BaseModel):
    CostCategoryArn: str

class DescribeCostCategoryDefinitionRequestRequestTypeDef(BaseModel):
    CostCategoryArn: str
    EffectiveOn: Optional[str] = None

class DimensionValuesTypeDef(BaseModel):
    Key: Optional[DimensionType] = None
    Values: Optional[Sequence[str]] = None
    MatchOptions: Optional[Sequence[MatchOptionType]] = None

class DimensionValuesWithAttributesTypeDef(BaseModel):
    Value: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None

class DiskResourceUtilizationTypeDef(BaseModel):
    DiskReadOpsPerSecond: Optional[str] = None
    DiskWriteOpsPerSecond: Optional[str] = None
    DiskReadBytesPerSecond: Optional[str] = None
    DiskWriteBytesPerSecond: Optional[str] = None

class EBSResourceUtilizationTypeDef(BaseModel):
    EbsReadOpsPerSecond: Optional[str] = None
    EbsWriteOpsPerSecond: Optional[str] = None
    EbsReadBytesPerSecond: Optional[str] = None
    EbsWriteBytesPerSecond: Optional[str] = None

class EC2InstanceDetailsTypeDef(BaseModel):
    Family: Optional[str] = None
    InstanceType: Optional[str] = None
    Region: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Platform: Optional[str] = None
    Tenancy: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None

class EC2ResourceDetailsTypeDef(BaseModel):
    HourlyOnDemandRate: Optional[str] = None
    InstanceType: Optional[str] = None
    Platform: Optional[str] = None
    Region: Optional[str] = None
    Sku: Optional[str] = None
    Memory: Optional[str] = None
    NetworkPerformance: Optional[str] = None
    Storage: Optional[str] = None
    Vcpu: Optional[str] = None

class NetworkResourceUtilizationTypeDef(BaseModel):
    NetworkInBytesPerSecond: Optional[str] = None
    NetworkOutBytesPerSecond: Optional[str] = None
    NetworkPacketsInPerSecond: Optional[str] = None
    NetworkPacketsOutPerSecond: Optional[str] = None

class EC2SpecificationTypeDef(BaseModel):
    OfferingClass: Optional[OfferingClassType] = None

class ESInstanceDetailsTypeDef(BaseModel):
    InstanceClass: Optional[str] = None
    InstanceSize: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None

class ElastiCacheInstanceDetailsTypeDef(BaseModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    ProductDescription: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None

class GenerationSummaryTypeDef(BaseModel):
    RecommendationId: Optional[str] = None
    GenerationStatus: Optional[GenerationStatusType] = None
    GenerationStartedTime: Optional[str] = None
    GenerationCompletionTime: Optional[str] = None
    EstimatedCompletionTime: Optional[str] = None

class TotalImpactFilterTypeDef(BaseModel):
    NumericOperator: NumericOperatorType
    StartValue: float
    EndValue: Optional[float] = None

class GetAnomalyMonitorsRequestRequestTypeDef(BaseModel):
    MonitorArnList: Optional[Sequence[str]] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetAnomalySubscriptionsRequestRequestTypeDef(BaseModel):
    SubscriptionArnList: Optional[Sequence[str]] = None
    MonitorArn: Optional[str] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetApproximateUsageRecordsRequestRequestTypeDef(BaseModel):
    Granularity: GranularityType
    ApproximationDimension: ApproximationDimensionType
    Services: Optional[Sequence[str]] = None

class GroupDefinitionTypeDef(BaseModel):
    Type: Optional[GroupDefinitionTypeType] = None
    Key: Optional[str] = None

class SortDefinitionTypeDef(BaseModel):
    Key: str
    SortOrder: Optional[SortOrderType] = None

class MetricValueTypeDef(BaseModel):
    Amount: Optional[str] = None
    Unit: Optional[str] = None

class ReservationPurchaseRecommendationMetadataTypeDef(BaseModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    AdditionalMetadata: Optional[str] = None

class ReservationAggregatesTypeDef(BaseModel):
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

class RightsizingRecommendationConfigurationTypeDef(BaseModel):
    RecommendationTarget: RecommendationTargetType
    BenefitsConsidered: bool

class RightsizingRecommendationMetadataTypeDef(BaseModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    AdditionalMetadata: Optional[str] = None

class RightsizingRecommendationSummaryTypeDef(BaseModel):
    TotalRecommendationCount: Optional[str] = None
    EstimatedTotalMonthlySavingsAmount: Optional[str] = None
    SavingsCurrencyCode: Optional[str] = None
    SavingsPercentage: Optional[str] = None

class GetSavingsPlanPurchaseRecommendationDetailsRequestRequestTypeDef(BaseModel):
    RecommendationDetailId: str

class GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef(BaseModel):
    SavingsPlansType: SupportedSavingsPlansTypeType
    TermInYears: TermInYearsType
    PaymentOption: PaymentOptionType
    LookbackPeriodInDays: LookbackPeriodInDaysType
    AccountScope: Optional[AccountScopeType] = None
    NextPageToken: Optional[str] = None
    PageSize: Optional[int] = None
    Filter: Optional["ExpressionTypeDef"] = None

class SavingsPlansPurchaseRecommendationMetadataTypeDef(BaseModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    AdditionalMetadata: Optional[str] = None

class MemoryDBInstanceDetailsTypeDef(BaseModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None

class RDSInstanceDetailsTypeDef(BaseModel):
    Family: Optional[str] = None
    InstanceType: Optional[str] = None
    Region: Optional[str] = None
    DatabaseEngine: Optional[str] = None
    DatabaseEdition: Optional[str] = None
    DeploymentOption: Optional[str] = None
    LicenseModel: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None

class RedshiftInstanceDetailsTypeDef(BaseModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None

class ListCostAllocationTagBackfillHistoryRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCostAllocationTagsRequestRequestTypeDef(BaseModel):
    Status: Optional[CostAllocationTagStatusType] = None
    TagKeys: Optional[Sequence[str]] = None
    Type: Optional[CostAllocationTagTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCostCategoryDefinitionsRequestRequestTypeDef(BaseModel):
    EffectiveOn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSavingsPlansPurchaseRecommendationGenerationRequestRequestTypeDef(BaseModel):
    GenerationStatus: Optional[GenerationStatusType] = None
    RecommendationIds: Optional[Sequence[str]] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ProvideAnomalyFeedbackRequestRequestTypeDef(BaseModel):
    AnomalyId: str
    Feedback: AnomalyFeedbackTypeType

class RecommendationDetailHourlyMetricsTypeDef(BaseModel):
    StartTime: Optional[str] = None
    EstimatedOnDemandCost: Optional[str] = None
    CurrentCoverage: Optional[str] = None
    EstimatedCoverage: Optional[str] = None
    EstimatedNewCommitmentUtilization: Optional[str] = None

class ReservationPurchaseRecommendationSummaryTypeDef(BaseModel):
    TotalEstimatedMonthlySavingsAmount: Optional[str] = None
    TotalEstimatedMonthlySavingsPercentage: Optional[str] = None
    CurrencyCode: Optional[str] = None

class TerminateRecommendationDetailTypeDef(BaseModel):
    EstimatedMonthlySavings: Optional[str] = None
    CurrencyCode: Optional[str] = None

class SavingsPlansAmortizedCommitmentTypeDef(BaseModel):
    AmortizedRecurringCommitment: Optional[str] = None
    AmortizedUpfrontCommitment: Optional[str] = None
    TotalAmortizedCommitment: Optional[str] = None

class SavingsPlansCoverageDataTypeDef(BaseModel):
    SpendCoveredBySavingsPlans: Optional[str] = None
    OnDemandCost: Optional[str] = None
    TotalCost: Optional[str] = None
    CoveragePercentage: Optional[str] = None

class SavingsPlansDetailsTypeDef(BaseModel):
    Region: Optional[str] = None
    InstanceFamily: Optional[str] = None
    OfferingId: Optional[str] = None

class SavingsPlansPurchaseRecommendationSummaryTypeDef(BaseModel):
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

class SavingsPlansSavingsTypeDef(BaseModel):
    NetSavings: Optional[str] = None
    OnDemandCostEquivalent: Optional[str] = None

class SavingsPlansUtilizationTypeDef(BaseModel):
    TotalCommitment: Optional[str] = None
    UsedCommitment: Optional[str] = None
    UnusedCommitment: Optional[str] = None
    UtilizationPercentage: Optional[str] = None

class StartCostAllocationTagBackfillRequestRequestTypeDef(BaseModel):
    BackfillFrom: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]

class UpdateAnomalyMonitorRequestRequestTypeDef(BaseModel):
    MonitorArn: str
    MonitorName: Optional[str] = None

class UpdateCostAllocationTagsStatusErrorTypeDef(BaseModel):
    TagKey: Optional[str] = None
    Code: Optional[str] = None
    Message: Optional[str] = None

class AnomalySubscriptionTypeDef(BaseModel):
    MonitorArnList: Sequence[str]
    Subscribers: Sequence[SubscriberTypeDef]
    Frequency: AnomalySubscriptionFrequencyType
    SubscriptionName: str
    SubscriptionArn: Optional[str] = None
    AccountId: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdExpression: Optional["ExpressionTypeDef"] = None

class UpdateAnomalySubscriptionRequestRequestTypeDef(BaseModel):
    SubscriptionArn: str
    Threshold: Optional[float] = None
    Frequency: Optional[AnomalySubscriptionFrequencyType] = None
    MonitorArnList: Optional[Sequence[str]] = None
    Subscribers: Optional[Sequence[SubscriberTypeDef]] = None
    SubscriptionName: Optional[str] = None
    ThresholdExpression: Optional["ExpressionTypeDef"] = None

class AnomalyTypeDef(BaseModel):
    AnomalyId: str
    AnomalyScore: AnomalyScoreTypeDef
    Impact: ImpactTypeDef
    MonitorArn: str
    AnomalyStartDate: Optional[str] = None
    AnomalyEndDate: Optional[str] = None
    DimensionValue: Optional[str] = None
    RootCauses: Optional[List[RootCauseTypeDef]] = None
    Feedback: Optional[AnomalyFeedbackTypeType] = None

class UpdateCostAllocationTagsStatusRequestRequestTypeDef(BaseModel):
    CostAllocationTagsStatus: Sequence[CostAllocationTagStatusEntryTypeDef]

class CostCategoryRuleTypeDef(BaseModel):
    Value: Optional[str] = None
    Rule: Optional["ExpressionTypeDef"] = None
    InheritedValue: Optional[CostCategoryInheritedValueDimensionTypeDef] = None
    Type: Optional[CostCategoryRuleTypeType] = None

class CostCategoryReferenceTypeDef(BaseModel):
    CostCategoryArn: Optional[str] = None
    Name: Optional[str] = None
    EffectiveStart: Optional[str] = None
    EffectiveEnd: Optional[str] = None
    NumberOfRules: Optional[int] = None
    ProcessingStatus: Optional[List[CostCategoryProcessingStatusTypeDef]] = None
    Values: Optional[List[str]] = None
    DefaultValue: Optional[str] = None

class CostCategorySplitChargeRuleTypeDef(BaseModel):
    Source: str
    Targets: Sequence[str]
    Method: CostCategorySplitChargeMethodType
    Parameters: Optional[Sequence[CostCategorySplitChargeRuleParameterTypeDef]] = None

class ForecastResultTypeDef(BaseModel):
    TimePeriod: Optional[DateIntervalTypeDef] = None
    MeanValue: Optional[str] = None
    PredictionIntervalLowerBound: Optional[str] = None
    PredictionIntervalUpperBound: Optional[str] = None

class GetCostForecastRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    Metric: MetricType
    Granularity: GranularityType
    Filter: Optional["ExpressionTypeDef"] = None
    PredictionIntervalLevel: Optional[int] = None

class GetUsageForecastRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    Metric: MetricType
    Granularity: GranularityType
    Filter: Optional["ExpressionTypeDef"] = None
    PredictionIntervalLevel: Optional[int] = None

class CoverageTypeDef(BaseModel):
    CoverageHours: Optional[CoverageHoursTypeDef] = None
    CoverageNormalizedUnits: Optional[CoverageNormalizedUnitsTypeDef] = None
    CoverageCost: Optional[CoverageCostTypeDef] = None

class CreateAnomalyMonitorRequestRequestTypeDef(BaseModel):
    AnomalyMonitor: AnomalyMonitorTypeDef
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class CreateAnomalyMonitorResponseTypeDef(BaseModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnomalySubscriptionResponseTypeDef(BaseModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCostCategoryDefinitionResponseTypeDef(BaseModel):
    CostCategoryArn: str
    EffectiveStart: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCostCategoryDefinitionResponseTypeDef(BaseModel):
    CostCategoryArn: str
    EffectiveEnd: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnomalyMonitorsResponseTypeDef(BaseModel):
    AnomalyMonitors: List[AnomalyMonitorTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApproximateUsageRecordsResponseTypeDef(BaseModel):
    Services: Dict[str, int]
    TotalRecords: int
    LookbackPeriod: DateIntervalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCostCategoriesResponseTypeDef(BaseModel):
    NextPageToken: str
    CostCategoryNames: List[str]
    CostCategoryValues: List[str]
    ReturnSize: int
    TotalSize: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagsResponseTypeDef(BaseModel):
    NextPageToken: str
    Tags: List[str]
    ReturnSize: int
    TotalSize: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListCostAllocationTagBackfillHistoryResponseTypeDef(BaseModel):
    BackfillRequests: List[CostAllocationTagBackfillRequestTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCostAllocationTagsResponseTypeDef(BaseModel):
    CostAllocationTags: List[CostAllocationTagTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProvideAnomalyFeedbackResponseTypeDef(BaseModel):
    AnomalyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCostAllocationTagBackfillResponseTypeDef(BaseModel):
    BackfillRequest: CostAllocationTagBackfillRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef(BaseModel):
    RecommendationId: str
    GenerationStartedTime: str
    EstimatedCompletionTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnomalyMonitorResponseTypeDef(BaseModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnomalySubscriptionResponseTypeDef(BaseModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCostCategoryDefinitionResponseTypeDef(BaseModel):
    CostCategoryArn: str
    EffectiveStart: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExpressionTypeDef(BaseModel):
    Or: Optional[Sequence[Dict[str, Any]]] = None
    And: Optional[Sequence[Dict[str, Any]]] = None
    Not: Optional[Dict[str, Any]] = None
    Dimensions: Optional[DimensionValuesTypeDef] = None
    Tags: Optional[TagValuesTypeDef] = None
    CostCategories: Optional[CostCategoryValuesTypeDef] = None

class GetDimensionValuesResponseTypeDef(BaseModel):
    DimensionValues: List[DimensionValuesWithAttributesTypeDef]
    ReturnSize: int
    TotalSize: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceDetailsTypeDef(BaseModel):
    EC2ResourceDetails: Optional[EC2ResourceDetailsTypeDef] = None

class EC2ResourceUtilizationTypeDef(BaseModel):
    MaxCpuUtilizationPercentage: Optional[str] = None
    MaxMemoryUtilizationPercentage: Optional[str] = None
    MaxStorageUtilizationPercentage: Optional[str] = None
    EBSResourceUtilization: Optional[EBSResourceUtilizationTypeDef] = None
    DiskResourceUtilization: Optional[DiskResourceUtilizationTypeDef] = None
    NetworkResourceUtilization: Optional[NetworkResourceUtilizationTypeDef] = None

class ServiceSpecificationTypeDef(BaseModel):
    EC2Specification: Optional[EC2SpecificationTypeDef] = None

class ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef(BaseModel):
    GenerationSummaryList: List[GenerationSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnomaliesRequestRequestTypeDef(BaseModel):
    DateInterval: AnomalyDateIntervalTypeDef
    MonitorArn: Optional[str] = None
    Feedback: Optional[AnomalyFeedbackTypeType] = None
    TotalImpact: Optional[TotalImpactFilterTypeDef] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetCostAndUsageRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    Granularity: GranularityType
    Metrics: Sequence[str]
    Filter: Optional["ExpressionTypeDef"] = None
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    NextPageToken: Optional[str] = None

class GetCostAndUsageWithResourcesRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    Granularity: GranularityType
    Filter: "ExpressionTypeDef"
    Metrics: Optional[Sequence[str]] = None
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    NextPageToken: Optional[str] = None

class GetCostCategoriesRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    SearchString: Optional[str] = None
    CostCategoryName: Optional[str] = None
    Filter: Optional["ExpressionTypeDef"] = None
    SortBy: Optional[Sequence[SortDefinitionTypeDef]] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None

class GetDimensionValuesRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    Dimension: DimensionType
    SearchString: Optional[str] = None
    Context: Optional[ContextType] = None
    Filter: Optional["ExpressionTypeDef"] = None
    SortBy: Optional[Sequence[SortDefinitionTypeDef]] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None

class GetReservationCoverageRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional["ExpressionTypeDef"] = None
    Metrics: Optional[Sequence[str]] = None
    NextPageToken: Optional[str] = None
    SortBy: Optional[SortDefinitionTypeDef] = None
    MaxResults: Optional[int] = None

class GetReservationUtilizationRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional["ExpressionTypeDef"] = None
    SortBy: Optional[SortDefinitionTypeDef] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetSavingsPlansCoverageRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional["ExpressionTypeDef"] = None
    Metrics: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[SortDefinitionTypeDef] = None

class GetSavingsPlansUtilizationDetailsRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    Filter: Optional["ExpressionTypeDef"] = None
    DataType: Optional[Sequence[SavingsPlansDataTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[SortDefinitionTypeDef] = None

class GetSavingsPlansUtilizationRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    Granularity: Optional[GranularityType] = None
    Filter: Optional["ExpressionTypeDef"] = None
    SortBy: Optional[SortDefinitionTypeDef] = None

class GetTagsRequestRequestTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    SearchString: Optional[str] = None
    TagKey: Optional[str] = None
    Filter: Optional["ExpressionTypeDef"] = None
    SortBy: Optional[Sequence[SortDefinitionTypeDef]] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None

class GroupTypeDef(BaseModel):
    Keys: Optional[List[str]] = None
    Metrics: Optional[Dict[str, MetricValueTypeDef]] = None

class ReservationUtilizationGroupTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    Utilization: Optional[ReservationAggregatesTypeDef] = None

class GetRightsizingRecommendationRequestRequestTypeDef(BaseModel):
    Service: str
    Filter: Optional["ExpressionTypeDef"] = None
    Configuration: Optional[RightsizingRecommendationConfigurationTypeDef] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None

class InstanceDetailsTypeDef(BaseModel):
    EC2InstanceDetails: Optional[EC2InstanceDetailsTypeDef] = None
    RDSInstanceDetails: Optional[RDSInstanceDetailsTypeDef] = None
    RedshiftInstanceDetails: Optional[RedshiftInstanceDetailsTypeDef] = None
    ElastiCacheInstanceDetails: Optional[ElastiCacheInstanceDetailsTypeDef] = None
    ESInstanceDetails: Optional[ESInstanceDetailsTypeDef] = None
    MemoryDBInstanceDetails: Optional[MemoryDBInstanceDetailsTypeDef] = None

class RecommendationDetailDataTypeDef(BaseModel):
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
    MetricsOverLookbackPeriod: Optional[List[RecommendationDetailHourlyMetricsTypeDef]] = None

class SavingsPlansCoverageTypeDef(BaseModel):
    Attributes: Optional[Dict[str, str]] = None
    Coverage: Optional[SavingsPlansCoverageDataTypeDef] = None
    TimePeriod: Optional[DateIntervalTypeDef] = None

class SavingsPlansPurchaseRecommendationDetailTypeDef(BaseModel):
    SavingsPlansDetails: Optional[SavingsPlansDetailsTypeDef] = None
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

class SavingsPlansUtilizationAggregatesTypeDef(BaseModel):
    Utilization: SavingsPlansUtilizationTypeDef
    Savings: Optional[SavingsPlansSavingsTypeDef] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitmentTypeDef] = None

class SavingsPlansUtilizationByTimeTypeDef(BaseModel):
    TimePeriod: DateIntervalTypeDef
    Utilization: SavingsPlansUtilizationTypeDef
    Savings: Optional[SavingsPlansSavingsTypeDef] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitmentTypeDef] = None

class SavingsPlansUtilizationDetailTypeDef(BaseModel):
    SavingsPlanArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    Utilization: Optional[SavingsPlansUtilizationTypeDef] = None
    Savings: Optional[SavingsPlansSavingsTypeDef] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitmentTypeDef] = None

class UpdateCostAllocationTagsStatusResponseTypeDef(BaseModel):
    Errors: List[UpdateCostAllocationTagsStatusErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnomalySubscriptionRequestRequestTypeDef(BaseModel):
    AnomalySubscription: AnomalySubscriptionTypeDef
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class GetAnomalySubscriptionsResponseTypeDef(BaseModel):
    AnomalySubscriptions: List[AnomalySubscriptionTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnomaliesResponseTypeDef(BaseModel):
    Anomalies: List[AnomalyTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCostCategoryDefinitionsResponseTypeDef(BaseModel):
    CostCategoryReferences: List[CostCategoryReferenceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CostCategoryTypeDef(BaseModel):
    CostCategoryArn: str
    EffectiveStart: str
    Name: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: List[CostCategoryRuleTypeDef]
    EffectiveEnd: Optional[str] = None
    SplitChargeRules: Optional[List[CostCategorySplitChargeRuleTypeDef]] = None
    ProcessingStatus: Optional[List[CostCategoryProcessingStatusTypeDef]] = None
    DefaultValue: Optional[str] = None

class CreateCostCategoryDefinitionRequestRequestTypeDef(BaseModel):
    Name: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: Sequence[CostCategoryRuleTypeDef]
    EffectiveStart: Optional[str] = None
    DefaultValue: Optional[str] = None
    SplitChargeRules: Optional[Sequence[CostCategorySplitChargeRuleTypeDef]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class UpdateCostCategoryDefinitionRequestRequestTypeDef(BaseModel):
    CostCategoryArn: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: Sequence[CostCategoryRuleTypeDef]
    EffectiveStart: Optional[str] = None
    DefaultValue: Optional[str] = None
    SplitChargeRules: Optional[Sequence[CostCategorySplitChargeRuleTypeDef]] = None

class GetCostForecastResponseTypeDef(BaseModel):
    Total: MetricValueTypeDef
    ForecastResultsByTime: List[ForecastResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetUsageForecastResponseTypeDef(BaseModel):
    Total: MetricValueTypeDef
    ForecastResultsByTime: List[ForecastResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservationCoverageGroupTypeDef(BaseModel):
    Attributes: Optional[Dict[str, str]] = None
    Coverage: Optional[CoverageTypeDef] = None

class ResourceUtilizationTypeDef(BaseModel):
    EC2ResourceUtilization: Optional[EC2ResourceUtilizationTypeDef] = None

class GetReservationPurchaseRecommendationRequestRequestTypeDef(BaseModel):
    Service: str
    AccountId: Optional[str] = None
    Filter: Optional["ExpressionTypeDef"] = None
    AccountScope: Optional[AccountScopeType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    ServiceSpecification: Optional[ServiceSpecificationTypeDef] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None

class ResultByTimeTypeDef(BaseModel):
    TimePeriod: Optional[DateIntervalTypeDef] = None
    Total: Optional[Dict[str, MetricValueTypeDef]] = None
    Groups: Optional[List[GroupTypeDef]] = None
    Estimated: Optional[bool] = None

class UtilizationByTimeTypeDef(BaseModel):
    TimePeriod: Optional[DateIntervalTypeDef] = None
    Groups: Optional[List[ReservationUtilizationGroupTypeDef]] = None
    Total: Optional[ReservationAggregatesTypeDef] = None

class ReservationPurchaseRecommendationDetailTypeDef(BaseModel):
    AccountId: Optional[str] = None
    InstanceDetails: Optional[InstanceDetailsTypeDef] = None
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

class GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef(BaseModel):
    RecommendationDetailId: str
    RecommendationDetailData: RecommendationDetailDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSavingsPlansCoverageResponseTypeDef(BaseModel):
    SavingsPlansCoverages: List[SavingsPlansCoverageTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SavingsPlansPurchaseRecommendationTypeDef(BaseModel):
    AccountScope: Optional[AccountScopeType] = None
    SavingsPlansType: Optional[SupportedSavingsPlansTypeType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    SavingsPlansPurchaseRecommendationDetails: Optional[       List[SavingsPlansPurchaseRecommendationDetailTypeDef]     ] = None
    SavingsPlansPurchaseRecommendationSummary: Optional[       SavingsPlansPurchaseRecommendationSummaryTypeDef     ] = None

class GetSavingsPlansUtilizationResponseTypeDef(BaseModel):
    SavingsPlansUtilizationsByTime: List[SavingsPlansUtilizationByTimeTypeDef]
    Total: SavingsPlansUtilizationAggregatesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSavingsPlansUtilizationDetailsResponseTypeDef(BaseModel):
    SavingsPlansUtilizationDetails: List[SavingsPlansUtilizationDetailTypeDef]
    Total: SavingsPlansUtilizationAggregatesTypeDef
    TimePeriod: DateIntervalTypeDef
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCostCategoryDefinitionResponseTypeDef(BaseModel):
    CostCategory: CostCategoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CoverageByTimeTypeDef(BaseModel):
    TimePeriod: Optional[DateIntervalTypeDef] = None
    Groups: Optional[List[ReservationCoverageGroupTypeDef]] = None
    Total: Optional[CoverageTypeDef] = None

class CurrentInstanceTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    InstanceName: Optional[str] = None
    Tags: Optional[List[TagValuesTypeDef]] = None
    ResourceDetails: Optional[ResourceDetailsTypeDef] = None
    ResourceUtilization: Optional[ResourceUtilizationTypeDef] = None
    ReservationCoveredHoursInLookbackPeriod: Optional[str] = None
    SavingsPlansCoveredHoursInLookbackPeriod: Optional[str] = None
    OnDemandHoursInLookbackPeriod: Optional[str] = None
    TotalRunningHoursInLookbackPeriod: Optional[str] = None
    MonthlyCost: Optional[str] = None
    CurrencyCode: Optional[str] = None

class TargetInstanceTypeDef(BaseModel):
    EstimatedMonthlyCost: Optional[str] = None
    EstimatedMonthlySavings: Optional[str] = None
    CurrencyCode: Optional[str] = None
    DefaultTargetInstance: Optional[bool] = None
    ResourceDetails: Optional[ResourceDetailsTypeDef] = None
    ExpectedResourceUtilization: Optional[ResourceUtilizationTypeDef] = None
    PlatformDifferences: Optional[List[PlatformDifferenceType]] = None

class GetCostAndUsageResponseTypeDef(BaseModel):
    NextPageToken: str
    GroupDefinitions: List[GroupDefinitionTypeDef]
    ResultsByTime: List[ResultByTimeTypeDef]
    DimensionValueAttributes: List[DimensionValuesWithAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCostAndUsageWithResourcesResponseTypeDef(BaseModel):
    NextPageToken: str
    GroupDefinitions: List[GroupDefinitionTypeDef]
    ResultsByTime: List[ResultByTimeTypeDef]
    DimensionValueAttributes: List[DimensionValuesWithAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReservationUtilizationResponseTypeDef(BaseModel):
    UtilizationsByTime: List[UtilizationByTimeTypeDef]
    Total: ReservationAggregatesTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReservationPurchaseRecommendationTypeDef(BaseModel):
    AccountScope: Optional[AccountScopeType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    ServiceSpecification: Optional[ServiceSpecificationTypeDef] = None
    RecommendationDetails: Optional[List[ReservationPurchaseRecommendationDetailTypeDef]] = None
    RecommendationSummary: Optional[ReservationPurchaseRecommendationSummaryTypeDef] = None

class GetSavingsPlansPurchaseRecommendationResponseTypeDef(BaseModel):
    Metadata: SavingsPlansPurchaseRecommendationMetadataTypeDef
    SavingsPlansPurchaseRecommendation: SavingsPlansPurchaseRecommendationTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReservationCoverageResponseTypeDef(BaseModel):
    CoveragesByTime: List[CoverageByTimeTypeDef]
    Total: CoverageTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyRecommendationDetailTypeDef(BaseModel):
    TargetInstances: Optional[List[TargetInstanceTypeDef]] = None

class GetReservationPurchaseRecommendationResponseTypeDef(BaseModel):
    Metadata: ReservationPurchaseRecommendationMetadataTypeDef
    Recommendations: List[ReservationPurchaseRecommendationTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RightsizingRecommendationTypeDef(BaseModel):
    AccountId: Optional[str] = None
    CurrentInstance: Optional[CurrentInstanceTypeDef] = None
    RightsizingType: Optional[RightsizingTypeType] = None
    ModifyRecommendationDetail: Optional[ModifyRecommendationDetailTypeDef] = None
    TerminateRecommendationDetail: Optional[TerminateRecommendationDetailTypeDef] = None
    FindingReasonCodes: Optional[List[FindingReasonCodeType]] = None

class GetRightsizingRecommendationResponseTypeDef(BaseModel):
    Metadata: RightsizingRecommendationMetadataTypeDef
    Summary: RightsizingRecommendationSummaryTypeDef
    RightsizingRecommendations: List[RightsizingRecommendationTypeDef]
    NextPageToken: str
    Configuration: RightsizingRecommendationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.ce_constants import *

class AnomalyDateIntervalTypeDef(BaseValidatorModel):
    StartDate: str
    EndDate: Optional[str] = None


class AnomalyScoreTypeDef(BaseValidatorModel):
    MaxScore: float
    CurrentScore: float


class ImpactTypeDef(BaseValidatorModel):
    MaxImpact: float
    TotalImpact: Optional[float] = None
    TotalActualSpend: Optional[float] = None
    TotalExpectedSpend: Optional[float] = None
    TotalImpactPercentage: Optional[float] = None


class CostAllocationTagBackfillRequestTypeDef(BaseValidatorModel):
    BackfillFrom: Optional[str] = None
    RequestedAt: Optional[str] = None
    CompletedAt: Optional[str] = None
    BackfillStatus: Optional[CostAllocationTagBackfillStatusType] = None
    LastUpdatedAt: Optional[str] = None


class CostAllocationTagStatusEntryTypeDef(BaseValidatorModel):
    TagKey: str
    Status: CostAllocationTagStatusType


class CostCategoryInheritedValueDimensionTypeDef(BaseValidatorModel):
    DimensionName: Optional[CostCategoryInheritedValueDimensionNameType] = None
    DimensionKey: Optional[str] = None


class CostCategoryProcessingStatusTypeDef(BaseValidatorModel):
    Component: Optional[Literal["COST_EXPLORER"]] = None
    Status: Optional[CostCategoryStatusType] = None


class CostCategoryValuesOutputTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class CostCategoryValuesTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    MatchOptions: Optional[Sequence[MatchOptionType]] = None


class DateIntervalTypeDef(BaseValidatorModel):
    Start: str
    End: str


class CoverageCostTypeDef(BaseValidatorModel):
    OnDemandCost: Optional[str] = None


class CoverageHoursTypeDef(BaseValidatorModel):
    OnDemandHours: Optional[str] = None
    ReservedHours: Optional[str] = None
    TotalRunningHours: Optional[str] = None
    CoverageHoursPercentage: Optional[str] = None


class CoverageNormalizedUnitsTypeDef(BaseValidatorModel):
    OnDemandNormalizedUnits: Optional[str] = None
    ReservedNormalizedUnits: Optional[str] = None
    TotalRunningNormalizedUnits: Optional[str] = None
    CoverageNormalizedUnitsPercentage: Optional[str] = None


class ResourceTagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagValuesOutputTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class DeleteAnomalyMonitorRequestTypeDef(BaseValidatorModel):
    MonitorArn: str


class DeleteAnomalySubscriptionRequestTypeDef(BaseValidatorModel):
    SubscriptionArn: str


class DeleteCostCategoryDefinitionRequestTypeDef(BaseValidatorModel):
    CostCategoryArn: str


class DescribeCostCategoryDefinitionRequestTypeDef(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveOn: Optional[str] = None


class DimensionValuesOutputTypeDef(BaseValidatorModel):
    Key: Optional[DimensionType] = None
    Values: Optional[List[str]] = None
    MatchOptions: Optional[List[MatchOptionType]] = None


class DimensionValuesTypeDef(BaseValidatorModel):
    Key: Optional[DimensionType] = None
    Values: Optional[Sequence[str]] = None
    MatchOptions: Optional[Sequence[MatchOptionType]] = None


class DimensionValuesWithAttributesTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class DiskResourceUtilizationTypeDef(BaseValidatorModel):
    DiskReadOpsPerSecond: Optional[str] = None
    DiskWriteOpsPerSecond: Optional[str] = None
    DiskReadBytesPerSecond: Optional[str] = None
    DiskWriteBytesPerSecond: Optional[str] = None


class DynamoDBCapacityDetailsTypeDef(BaseValidatorModel):
    CapacityUnits: Optional[str] = None
    Region: Optional[str] = None


class EBSResourceUtilizationTypeDef(BaseValidatorModel):
    EbsReadOpsPerSecond: Optional[str] = None
    EbsWriteOpsPerSecond: Optional[str] = None
    EbsReadBytesPerSecond: Optional[str] = None
    EbsWriteBytesPerSecond: Optional[str] = None


class EC2InstanceDetailsTypeDef(BaseValidatorModel):
    Family: Optional[str] = None
    InstanceType: Optional[str] = None
    Region: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Platform: Optional[str] = None
    Tenancy: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class EC2ResourceDetailsTypeDef(BaseValidatorModel):
    HourlyOnDemandRate: Optional[str] = None
    InstanceType: Optional[str] = None
    Platform: Optional[str] = None
    Region: Optional[str] = None
    Sku: Optional[str] = None
    Memory: Optional[str] = None
    NetworkPerformance: Optional[str] = None
    Storage: Optional[str] = None
    Vcpu: Optional[str] = None


class NetworkResourceUtilizationTypeDef(BaseValidatorModel):
    NetworkInBytesPerSecond: Optional[str] = None
    NetworkOutBytesPerSecond: Optional[str] = None
    NetworkPacketsInPerSecond: Optional[str] = None
    NetworkPacketsOutPerSecond: Optional[str] = None


class EC2SpecificationTypeDef(BaseValidatorModel):
    OfferingClass: Optional[OfferingClassType] = None


class ESInstanceDetailsTypeDef(BaseValidatorModel):
    InstanceClass: Optional[str] = None
    InstanceSize: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class ElastiCacheInstanceDetailsTypeDef(BaseValidatorModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    ProductDescription: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class GenerationSummaryTypeDef(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    GenerationStatus: Optional[GenerationStatusType] = None
    GenerationStartedTime: Optional[str] = None
    GenerationCompletionTime: Optional[str] = None
    EstimatedCompletionTime: Optional[str] = None


class TotalImpactFilterTypeDef(BaseValidatorModel):
    NumericOperator: NumericOperatorType
    StartValue: float
    EndValue: Optional[float] = None


class GetAnomalyMonitorsRequestTypeDef(BaseValidatorModel):
    MonitorArnList: Optional[Sequence[str]] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetAnomalySubscriptionsRequestTypeDef(BaseValidatorModel):
    SubscriptionArnList: Optional[Sequence[str]] = None
    MonitorArn: Optional[str] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetApproximateUsageRecordsRequestTypeDef(BaseValidatorModel):
    Granularity: GranularityType
    ApproximationDimension: ApproximationDimensionType
    Services: Optional[Sequence[str]] = None


class GetCommitmentPurchaseAnalysisRequestTypeDef(BaseValidatorModel):
    AnalysisId: str


class SortDefinitionTypeDef(BaseValidatorModel):
    Key: str
    SortOrder: Optional[SortOrderType] = None


class MetricValueTypeDef(BaseValidatorModel):
    Amount: Optional[str] = None
    Unit: Optional[str] = None


class ReservationPurchaseRecommendationMetadataTypeDef(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    AdditionalMetadata: Optional[str] = None


class ReservationAggregatesTypeDef(BaseValidatorModel):
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


class RightsizingRecommendationConfigurationTypeDef(BaseValidatorModel):
    RecommendationTarget: RecommendationTargetType
    BenefitsConsidered: bool


class RightsizingRecommendationMetadataTypeDef(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    AdditionalMetadata: Optional[str] = None


class RightsizingRecommendationSummaryTypeDef(BaseValidatorModel):
    TotalRecommendationCount: Optional[str] = None
    EstimatedTotalMonthlySavingsAmount: Optional[str] = None
    SavingsCurrencyCode: Optional[str] = None
    SavingsPercentage: Optional[str] = None


class GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef(BaseValidatorModel):
    RecommendationDetailId: str


class SavingsPlansPurchaseRecommendationMetadataTypeDef(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    GenerationTimestamp: Optional[str] = None
    AdditionalMetadata: Optional[str] = None


class MemoryDBInstanceDetailsTypeDef(BaseValidatorModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class RDSInstanceDetailsTypeDef(BaseValidatorModel):
    Family: Optional[str] = None
    InstanceType: Optional[str] = None
    Region: Optional[str] = None
    DatabaseEngine: Optional[str] = None
    DatabaseEdition: Optional[str] = None
    DeploymentOption: Optional[str] = None
    LicenseModel: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class RedshiftInstanceDetailsTypeDef(BaseValidatorModel):
    Family: Optional[str] = None
    NodeType: Optional[str] = None
    Region: Optional[str] = None
    CurrentGeneration: Optional[bool] = None
    SizeFlexEligible: Optional[bool] = None


class ListCommitmentPurchaseAnalysesRequestTypeDef(BaseValidatorModel):
    AnalysisStatus: Optional[AnalysisStatusType] = None
    NextPageToken: Optional[str] = None
    PageSize: Optional[int] = None
    AnalysisIds: Optional[Sequence[str]] = None


class ListCostAllocationTagBackfillHistoryRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCostCategoryDefinitionsRequestTypeDef(BaseValidatorModel):
    EffectiveOn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef(BaseValidatorModel):
    GenerationStatus: Optional[GenerationStatusType] = None
    RecommendationIds: Optional[Sequence[str]] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ProvideAnomalyFeedbackRequestTypeDef(BaseValidatorModel):
    AnomalyId: str
    Feedback: AnomalyFeedbackTypeType


class RecommendationDetailHourlyMetricsTypeDef(BaseValidatorModel):
    StartTime: Optional[str] = None
    EstimatedOnDemandCost: Optional[str] = None
    CurrentCoverage: Optional[str] = None
    EstimatedCoverage: Optional[str] = None
    EstimatedNewCommitmentUtilization: Optional[str] = None


class ReservationPurchaseRecommendationSummaryTypeDef(BaseValidatorModel):
    TotalEstimatedMonthlySavingsAmount: Optional[str] = None
    TotalEstimatedMonthlySavingsPercentage: Optional[str] = None
    CurrencyCode: Optional[str] = None


class TerminateRecommendationDetailTypeDef(BaseValidatorModel):
    EstimatedMonthlySavings: Optional[str] = None
    CurrencyCode: Optional[str] = None


class RootCauseImpactTypeDef(BaseValidatorModel):
    Contribution: float


class SavingsPlansAmortizedCommitmentTypeDef(BaseValidatorModel):
    AmortizedRecurringCommitment: Optional[str] = None
    AmortizedUpfrontCommitment: Optional[str] = None
    TotalAmortizedCommitment: Optional[str] = None


class SavingsPlansCoverageDataTypeDef(BaseValidatorModel):
    SpendCoveredBySavingsPlans: Optional[str] = None
    OnDemandCost: Optional[str] = None
    TotalCost: Optional[str] = None
    CoveragePercentage: Optional[str] = None


class SavingsPlansDetailsTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    InstanceFamily: Optional[str] = None
    OfferingId: Optional[str] = None


class SavingsPlansTypeDef(BaseValidatorModel):
    PaymentOption: Optional[PaymentOptionType] = None
    SavingsPlansType: Optional[SupportedSavingsPlansTypeType] = None
    Region: Optional[str] = None
    InstanceFamily: Optional[str] = None
    TermInYears: Optional[TermInYearsType] = None
    SavingsPlansCommitment: Optional[float] = None
    OfferingId: Optional[str] = None


class SavingsPlansPurchaseRecommendationSummaryTypeDef(BaseValidatorModel):
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


class SavingsPlansSavingsTypeDef(BaseValidatorModel):
    NetSavings: Optional[str] = None
    OnDemandCostEquivalent: Optional[str] = None


class SavingsPlansUtilizationTypeDef(BaseValidatorModel):
    TotalCommitment: Optional[str] = None
    UsedCommitment: Optional[str] = None
    UnusedCommitment: Optional[str] = None
    UtilizationPercentage: Optional[str] = None


class StartCostAllocationTagBackfillRequestTypeDef(BaseValidatorModel):
    BackfillFrom: str


class TagValuesTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    MatchOptions: Optional[Sequence[MatchOptionType]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]


class UpdateAnomalyMonitorRequestTypeDef(BaseValidatorModel):
    MonitorArn: str
    MonitorName: Optional[str] = None


class UpdateCostAllocationTagsStatusErrorTypeDef(BaseValidatorModel):
    TagKey: Optional[str] = None
    Code: Optional[str] = None
    Message: Optional[str] = None


class UpdateCostAllocationTagsStatusRequestTypeDef(BaseValidatorModel):
    CostAllocationTagsStatus: Sequence[CostAllocationTagStatusEntryTypeDef]


class CostCategoryReferenceTypeDef(BaseValidatorModel):
    CostCategoryArn: Optional[str] = None
    Name: Optional[str] = None
    EffectiveStart: Optional[str] = None
    EffectiveEnd: Optional[str] = None
    NumberOfRules: Optional[int] = None
    ProcessingStatus: Optional[List[CostCategoryProcessingStatusTypeDef]] = None
    Values: Optional[List[str]] = None
    DefaultValue: Optional[str] = None


class CostCategorySplitChargeRuleParameterOutputTypeDef(BaseValidatorModel):
    pass


class CostCategorySplitChargeRuleOutputTypeDef(BaseValidatorModel):
    Source: str
    Targets: List[str]
    Method: CostCategorySplitChargeMethodType
    Parameters: Optional[List[CostCategorySplitChargeRuleParameterOutputTypeDef]] = None


class ForecastResultTypeDef(BaseValidatorModel):
    TimePeriod: Optional[DateIntervalTypeDef] = None
    MeanValue: Optional[str] = None
    PredictionIntervalLowerBound: Optional[str] = None
    PredictionIntervalUpperBound: Optional[str] = None


class CoverageTypeDef(BaseValidatorModel):
    CoverageHours: Optional[CoverageHoursTypeDef] = None
    CoverageNormalizedUnits: Optional[CoverageNormalizedUnitsTypeDef] = None
    CoverageCost: Optional[CoverageCostTypeDef] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]


class CreateAnomalyMonitorResponseTypeDef(BaseValidatorModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAnomalySubscriptionResponseTypeDef(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCostCategoryDefinitionResponseTypeDef(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveStart: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCostCategoryDefinitionResponseTypeDef(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveEnd: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetApproximateUsageRecordsResponseTypeDef(BaseValidatorModel):
    Services: Dict[str, int]
    TotalRecords: int
    LookbackPeriod: DateIntervalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCostCategoriesResponseTypeDef(BaseValidatorModel):
    NextPageToken: str
    CostCategoryNames: List[str]
    CostCategoryValues: List[str]
    ReturnSize: int
    TotalSize: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetTagsResponseTypeDef(BaseValidatorModel):
    NextPageToken: str
    Tags: List[str]
    ReturnSize: int
    TotalSize: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListCostAllocationTagBackfillHistoryResponseTypeDef(BaseValidatorModel):
    BackfillRequests: List[CostAllocationTagBackfillRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CostAllocationTagTypeDef(BaseValidatorModel):
    pass


class ListCostAllocationTagsResponseTypeDef(BaseValidatorModel):
    CostAllocationTags: List[CostAllocationTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ProvideAnomalyFeedbackResponseTypeDef(BaseValidatorModel):
    AnomalyId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartCommitmentPurchaseAnalysisResponseTypeDef(BaseValidatorModel):
    AnalysisId: str
    AnalysisStartedTime: str
    EstimatedCompletionTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartCostAllocationTagBackfillResponseTypeDef(BaseValidatorModel):
    BackfillRequest: CostAllocationTagBackfillRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef(BaseValidatorModel):
    RecommendationId: str
    GenerationStartedTime: str
    EstimatedCompletionTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAnomalyMonitorResponseTypeDef(BaseValidatorModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAnomalySubscriptionResponseTypeDef(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCostCategoryDefinitionResponseTypeDef(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveStart: str
    ResponseMetadata: ResponseMetadataTypeDef


class ExpressionOutputTypeDef(BaseValidatorModel):
    Or: Optional[List[Dict[str, Any]]] = None
    And: Optional[List[Dict[str, Any]]] = None
    Not: Optional[Dict[str, Any]] = None
    Dimensions: Optional[DimensionValuesOutputTypeDef] = None
    Tags: Optional[TagValuesOutputTypeDef] = None
    CostCategories: Optional[CostCategoryValuesOutputTypeDef] = None


class GetDimensionValuesResponseTypeDef(BaseValidatorModel):
    DimensionValues: List[DimensionValuesWithAttributesTypeDef]
    ReturnSize: int
    TotalSize: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ReservedCapacityDetailsTypeDef(BaseValidatorModel):
    DynamoDBCapacityDetails: Optional[DynamoDBCapacityDetailsTypeDef] = None


class ResourceDetailsTypeDef(BaseValidatorModel):
    EC2ResourceDetails: Optional[EC2ResourceDetailsTypeDef] = None


class EC2ResourceUtilizationTypeDef(BaseValidatorModel):
    MaxCpuUtilizationPercentage: Optional[str] = None
    MaxMemoryUtilizationPercentage: Optional[str] = None
    MaxStorageUtilizationPercentage: Optional[str] = None
    EBSResourceUtilization: Optional[EBSResourceUtilizationTypeDef] = None
    DiskResourceUtilization: Optional[DiskResourceUtilizationTypeDef] = None
    NetworkResourceUtilization: Optional[NetworkResourceUtilizationTypeDef] = None


class ServiceSpecificationTypeDef(BaseValidatorModel):
    EC2Specification: Optional[EC2SpecificationTypeDef] = None


class ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef(BaseValidatorModel):
    GenerationSummaryList: List[GenerationSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAnomaliesRequestTypeDef(BaseValidatorModel):
    DateInterval: AnomalyDateIntervalTypeDef
    MonitorArn: Optional[str] = None
    Feedback: Optional[AnomalyFeedbackTypeType] = None
    TotalImpact: Optional[TotalImpactFilterTypeDef] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GroupTypeDef(BaseValidatorModel):
    Keys: Optional[List[str]] = None
    Metrics: Optional[Dict[str, MetricValueTypeDef]] = None


class ReservationUtilizationGroupTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    Utilization: Optional[ReservationAggregatesTypeDef] = None


class InstanceDetailsTypeDef(BaseValidatorModel):
    EC2InstanceDetails: Optional[EC2InstanceDetailsTypeDef] = None
    RDSInstanceDetails: Optional[RDSInstanceDetailsTypeDef] = None
    RedshiftInstanceDetails: Optional[RedshiftInstanceDetailsTypeDef] = None
    ElastiCacheInstanceDetails: Optional[ElastiCacheInstanceDetailsTypeDef] = None
    ESInstanceDetails: Optional[ESInstanceDetailsTypeDef] = None
    MemoryDBInstanceDetails: Optional[MemoryDBInstanceDetailsTypeDef] = None


class RecommendationDetailDataTypeDef(BaseValidatorModel):
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


class SavingsPlansPurchaseAnalysisDetailsTypeDef(BaseValidatorModel):
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
    MetricsOverLookbackPeriod: Optional[List[RecommendationDetailHourlyMetricsTypeDef]] = None


class RootCauseTypeDef(BaseValidatorModel):
    Service: Optional[str] = None
    Region: Optional[str] = None
    LinkedAccount: Optional[str] = None
    LinkedAccountName: Optional[str] = None
    UsageType: Optional[str] = None
    Impact: Optional[RootCauseImpactTypeDef] = None


class SavingsPlansCoverageTypeDef(BaseValidatorModel):
    Attributes: Optional[Dict[str, str]] = None
    Coverage: Optional[SavingsPlansCoverageDataTypeDef] = None
    TimePeriod: Optional[DateIntervalTypeDef] = None


class SavingsPlansPurchaseRecommendationDetailTypeDef(BaseValidatorModel):
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


class SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef(BaseValidatorModel):
    AnalysisType: AnalysisTypeType
    SavingsPlansToAdd: List[SavingsPlansTypeDef]
    LookBackTimePeriod: DateIntervalTypeDef
    AccountScope: Optional[AccountScopeType] = None
    AccountId: Optional[str] = None
    SavingsPlansToExclude: Optional[List[str]] = None


class SavingsPlansPurchaseAnalysisConfigurationTypeDef(BaseValidatorModel):
    AnalysisType: AnalysisTypeType
    SavingsPlansToAdd: Sequence[SavingsPlansTypeDef]
    LookBackTimePeriod: DateIntervalTypeDef
    AccountScope: Optional[AccountScopeType] = None
    AccountId: Optional[str] = None
    SavingsPlansToExclude: Optional[Sequence[str]] = None


class SavingsPlansUtilizationAggregatesTypeDef(BaseValidatorModel):
    Utilization: SavingsPlansUtilizationTypeDef
    Savings: Optional[SavingsPlansSavingsTypeDef] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitmentTypeDef] = None


class SavingsPlansUtilizationByTimeTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    Utilization: SavingsPlansUtilizationTypeDef
    Savings: Optional[SavingsPlansSavingsTypeDef] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitmentTypeDef] = None


class SavingsPlansUtilizationDetailTypeDef(BaseValidatorModel):
    SavingsPlanArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    Utilization: Optional[SavingsPlansUtilizationTypeDef] = None
    Savings: Optional[SavingsPlansSavingsTypeDef] = None
    AmortizedCommitment: Optional[SavingsPlansAmortizedCommitmentTypeDef] = None


class UpdateCostAllocationTagsStatusResponseTypeDef(BaseValidatorModel):
    Errors: List[UpdateCostAllocationTagsStatusErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListCostCategoryDefinitionsResponseTypeDef(BaseValidatorModel):
    CostCategoryReferences: List[CostCategoryReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CostCategorySplitChargeRuleParameterUnionTypeDef(BaseValidatorModel):
    pass


class CostCategorySplitChargeRuleTypeDef(BaseValidatorModel):
    Source: str
    Targets: Sequence[str]
    Method: CostCategorySplitChargeMethodType
    Parameters: Optional[Sequence[CostCategorySplitChargeRuleParameterUnionTypeDef]] = None


class GetCostForecastResponseTypeDef(BaseValidatorModel):
    Total: MetricValueTypeDef
    ForecastResultsByTime: List[ForecastResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetUsageForecastResponseTypeDef(BaseValidatorModel):
    Total: MetricValueTypeDef
    ForecastResultsByTime: List[ForecastResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ReservationCoverageGroupTypeDef(BaseValidatorModel):
    Attributes: Optional[Dict[str, str]] = None
    Coverage: Optional[CoverageTypeDef] = None


class AnomalyMonitorOutputTypeDef(BaseValidatorModel):
    MonitorName: str
    MonitorType: MonitorTypeType
    MonitorArn: Optional[str] = None
    CreationDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    LastEvaluatedDate: Optional[str] = None
    MonitorDimension: Optional[Literal["SERVICE"]] = None
    MonitorSpecification: Optional[ExpressionOutputTypeDef] = None
    DimensionalValueCount: Optional[int] = None


class SubscriberTypeDef(BaseValidatorModel):
    pass


class AnomalySubscriptionOutputTypeDef(BaseValidatorModel):
    MonitorArnList: List[str]
    Subscribers: List[SubscriberTypeDef]
    Frequency: AnomalySubscriptionFrequencyType
    SubscriptionName: str
    SubscriptionArn: Optional[str] = None
    AccountId: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdExpression: Optional[ExpressionOutputTypeDef] = None


class ResourceUtilizationTypeDef(BaseValidatorModel):
    EC2ResourceUtilization: Optional[EC2ResourceUtilizationTypeDef] = None


class ResultByTimeTypeDef(BaseValidatorModel):
    TimePeriod: Optional[DateIntervalTypeDef] = None
    Total: Optional[Dict[str, MetricValueTypeDef]] = None
    Groups: Optional[List[GroupTypeDef]] = None
    Estimated: Optional[bool] = None


class UtilizationByTimeTypeDef(BaseValidatorModel):
    TimePeriod: Optional[DateIntervalTypeDef] = None
    Groups: Optional[List[ReservationUtilizationGroupTypeDef]] = None
    Total: Optional[ReservationAggregatesTypeDef] = None


class ReservationPurchaseRecommendationDetailTypeDef(BaseValidatorModel):
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
    ReservedCapacityDetails: Optional[ReservedCapacityDetailsTypeDef] = None
    RecommendedNumberOfCapacityUnitsToPurchase: Optional[str] = None
    MinimumNumberOfCapacityUnitsUsedPerHour: Optional[str] = None
    MaximumNumberOfCapacityUnitsUsedPerHour: Optional[str] = None
    AverageNumberOfCapacityUnitsUsedPerHour: Optional[str] = None


class GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef(BaseValidatorModel):
    RecommendationDetailId: str
    RecommendationDetailData: RecommendationDetailDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AnalysisDetailsTypeDef(BaseValidatorModel):
    SavingsPlansPurchaseAnalysisDetails: Optional[SavingsPlansPurchaseAnalysisDetailsTypeDef] = None


class AnomalyTypeDef(BaseValidatorModel):
    AnomalyId: str
    AnomalyScore: AnomalyScoreTypeDef
    Impact: ImpactTypeDef
    MonitorArn: str
    AnomalyStartDate: Optional[str] = None
    AnomalyEndDate: Optional[str] = None
    DimensionValue: Optional[str] = None
    RootCauses: Optional[List[RootCauseTypeDef]] = None
    Feedback: Optional[AnomalyFeedbackTypeType] = None


class GetSavingsPlansCoverageResponseTypeDef(BaseValidatorModel):
    SavingsPlansCoverages: List[SavingsPlansCoverageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SavingsPlansPurchaseRecommendationTypeDef(BaseValidatorModel):
    AccountScope: Optional[AccountScopeType] = None
    SavingsPlansType: Optional[SupportedSavingsPlansTypeType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    SavingsPlansPurchaseRecommendationDetails: Optional[ List[SavingsPlansPurchaseRecommendationDetailTypeDef] ] = None
    SavingsPlansPurchaseRecommendationSummary: Optional[ SavingsPlansPurchaseRecommendationSummaryTypeDef ] = None


class CommitmentPurchaseAnalysisConfigurationOutputTypeDef(BaseValidatorModel):
    SavingsPlansPurchaseAnalysisConfiguration: Optional[ SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef ] = None


class CommitmentPurchaseAnalysisConfigurationTypeDef(BaseValidatorModel):
    SavingsPlansPurchaseAnalysisConfiguration: Optional[ SavingsPlansPurchaseAnalysisConfigurationTypeDef ] = None


class GetSavingsPlansUtilizationResponseTypeDef(BaseValidatorModel):
    SavingsPlansUtilizationsByTime: List[SavingsPlansUtilizationByTimeTypeDef]
    Total: SavingsPlansUtilizationAggregatesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSavingsPlansUtilizationDetailsResponseTypeDef(BaseValidatorModel):
    SavingsPlansUtilizationDetails: List[SavingsPlansUtilizationDetailTypeDef]
    Total: SavingsPlansUtilizationAggregatesTypeDef
    TimePeriod: DateIntervalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CostCategoryValuesUnionTypeDef(BaseValidatorModel):
    pass


class DimensionValuesUnionTypeDef(BaseValidatorModel):
    pass


class TagValuesUnionTypeDef(BaseValidatorModel):
    pass


class ExpressionTypeDef(BaseValidatorModel):
    Or: Optional[Sequence[Mapping[str, Any]]] = None
    And: Optional[Sequence[Mapping[str, Any]]] = None
    Not: Optional[Mapping[str, Any]] = None
    Dimensions: Optional[DimensionValuesUnionTypeDef] = None
    Tags: Optional[TagValuesUnionTypeDef] = None
    CostCategories: Optional[CostCategoryValuesUnionTypeDef] = None


class CoverageByTimeTypeDef(BaseValidatorModel):
    TimePeriod: Optional[DateIntervalTypeDef] = None
    Groups: Optional[List[ReservationCoverageGroupTypeDef]] = None
    Total: Optional[CoverageTypeDef] = None


class GetAnomalyMonitorsResponseTypeDef(BaseValidatorModel):
    AnomalyMonitors: List[AnomalyMonitorOutputTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAnomalySubscriptionsResponseTypeDef(BaseValidatorModel):
    AnomalySubscriptions: List[AnomalySubscriptionOutputTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CostCategoryRuleOutputTypeDef(BaseValidatorModel):
    pass


class CostCategoryTypeDef(BaseValidatorModel):
    CostCategoryArn: str
    EffectiveStart: str
    Name: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: List[CostCategoryRuleOutputTypeDef]
    EffectiveEnd: Optional[str] = None
    SplitChargeRules: Optional[List[CostCategorySplitChargeRuleOutputTypeDef]] = None
    ProcessingStatus: Optional[List[CostCategoryProcessingStatusTypeDef]] = None
    DefaultValue: Optional[str] = None


class CurrentInstanceTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    InstanceName: Optional[str] = None
    Tags: Optional[List[TagValuesOutputTypeDef]] = None
    ResourceDetails: Optional[ResourceDetailsTypeDef] = None
    ResourceUtilization: Optional[ResourceUtilizationTypeDef] = None
    ReservationCoveredHoursInLookbackPeriod: Optional[str] = None
    SavingsPlansCoveredHoursInLookbackPeriod: Optional[str] = None
    OnDemandHoursInLookbackPeriod: Optional[str] = None
    TotalRunningHoursInLookbackPeriod: Optional[str] = None
    MonthlyCost: Optional[str] = None
    CurrencyCode: Optional[str] = None


class TargetInstanceTypeDef(BaseValidatorModel):
    EstimatedMonthlyCost: Optional[str] = None
    EstimatedMonthlySavings: Optional[str] = None
    CurrencyCode: Optional[str] = None
    DefaultTargetInstance: Optional[bool] = None
    ResourceDetails: Optional[ResourceDetailsTypeDef] = None
    ExpectedResourceUtilization: Optional[ResourceUtilizationTypeDef] = None
    PlatformDifferences: Optional[List[PlatformDifferenceType]] = None


class GroupDefinitionTypeDef(BaseValidatorModel):
    pass


class GetCostAndUsageResponseTypeDef(BaseValidatorModel):
    NextPageToken: str
    GroupDefinitions: List[GroupDefinitionTypeDef]
    ResultsByTime: List[ResultByTimeTypeDef]
    DimensionValueAttributes: List[DimensionValuesWithAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetCostAndUsageWithResourcesResponseTypeDef(BaseValidatorModel):
    NextPageToken: str
    GroupDefinitions: List[GroupDefinitionTypeDef]
    ResultsByTime: List[ResultByTimeTypeDef]
    DimensionValueAttributes: List[DimensionValuesWithAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetReservationUtilizationResponseTypeDef(BaseValidatorModel):
    UtilizationsByTime: List[UtilizationByTimeTypeDef]
    Total: ReservationAggregatesTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ReservationPurchaseRecommendationTypeDef(BaseValidatorModel):
    AccountScope: Optional[AccountScopeType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    ServiceSpecification: Optional[ServiceSpecificationTypeDef] = None
    RecommendationDetails: Optional[List[ReservationPurchaseRecommendationDetailTypeDef]] = None
    RecommendationSummary: Optional[ReservationPurchaseRecommendationSummaryTypeDef] = None


class GetAnomaliesResponseTypeDef(BaseValidatorModel):
    Anomalies: List[AnomalyTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSavingsPlansPurchaseRecommendationResponseTypeDef(BaseValidatorModel):
    Metadata: SavingsPlansPurchaseRecommendationMetadataTypeDef
    SavingsPlansPurchaseRecommendation: SavingsPlansPurchaseRecommendationTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class AnalysisSummaryTypeDef(BaseValidatorModel):
    EstimatedCompletionTime: Optional[str] = None
    AnalysisCompletionTime: Optional[str] = None
    AnalysisStartedTime: Optional[str] = None
    AnalysisStatus: Optional[AnalysisStatusType] = None
    ErrorCode: Optional[ErrorCodeType] = None
    AnalysisId: Optional[str] = None
    CommitmentPurchaseAnalysisConfiguration: Optional[ CommitmentPurchaseAnalysisConfigurationOutputTypeDef ] = None


class GetCommitmentPurchaseAnalysisResponseTypeDef(BaseValidatorModel):
    EstimatedCompletionTime: str
    AnalysisCompletionTime: str
    AnalysisStartedTime: str
    AnalysisId: str
    AnalysisStatus: AnalysisStatusType
    ErrorCode: ErrorCodeType
    AnalysisDetails: AnalysisDetailsTypeDef
    CommitmentPurchaseAnalysisConfiguration: CommitmentPurchaseAnalysisConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AnomalyMonitorTypeDef(BaseValidatorModel):
    MonitorName: str
    MonitorType: MonitorTypeType
    MonitorArn: Optional[str] = None
    CreationDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    LastEvaluatedDate: Optional[str] = None
    MonitorDimension: Optional[Literal["SERVICE"]] = None
    MonitorSpecification: Optional[ExpressionTypeDef] = None
    DimensionalValueCount: Optional[int] = None


class AnomalySubscriptionTypeDef(BaseValidatorModel):
    MonitorArnList: Sequence[str]
    Subscribers: Sequence[SubscriberTypeDef]
    Frequency: AnomalySubscriptionFrequencyType
    SubscriptionName: str
    SubscriptionArn: Optional[str] = None
    AccountId: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdExpression: Optional[ExpressionTypeDef] = None


class GetReservationCoverageResponseTypeDef(BaseValidatorModel):
    CoveragesByTime: List[CoverageByTimeTypeDef]
    Total: CoverageTypeDef
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCostCategoryDefinitionResponseTypeDef(BaseValidatorModel):
    CostCategory: CostCategoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyRecommendationDetailTypeDef(BaseValidatorModel):
    TargetInstances: Optional[List[TargetInstanceTypeDef]] = None


class GetReservationPurchaseRecommendationResponseTypeDef(BaseValidatorModel):
    Metadata: ReservationPurchaseRecommendationMetadataTypeDef
    Recommendations: List[ReservationPurchaseRecommendationTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListCommitmentPurchaseAnalysesResponseTypeDef(BaseValidatorModel):
    AnalysisSummaryList: List[AnalysisSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CommitmentPurchaseAnalysisConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class StartCommitmentPurchaseAnalysisRequestTypeDef(BaseValidatorModel):
    CommitmentPurchaseAnalysisConfiguration: CommitmentPurchaseAnalysisConfigurationUnionTypeDef


class ExpressionUnionTypeDef(BaseValidatorModel):
    pass


class GetCostAndUsageRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    Granularity: GranularityType
    Metrics: Sequence[str]
    Filter: Optional[ExpressionUnionTypeDef] = None
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    BillingViewArn: Optional[str] = None
    NextPageToken: Optional[str] = None


class GetCostAndUsageWithResourcesRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    Granularity: GranularityType
    Filter: ExpressionUnionTypeDef
    Metrics: Optional[Sequence[str]] = None
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    BillingViewArn: Optional[str] = None
    NextPageToken: Optional[str] = None


class GetCostCategoriesRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    SearchString: Optional[str] = None
    CostCategoryName: Optional[str] = None
    Filter: Optional[ExpressionUnionTypeDef] = None
    SortBy: Optional[Sequence[SortDefinitionTypeDef]] = None
    BillingViewArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetCostForecastRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    Metric: MetricType
    Granularity: GranularityType
    Filter: Optional[ExpressionUnionTypeDef] = None
    BillingViewArn: Optional[str] = None
    PredictionIntervalLevel: Optional[int] = None


class GetDimensionValuesRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    Dimension: DimensionType
    SearchString: Optional[str] = None
    Context: Optional[ContextType] = None
    Filter: Optional[ExpressionUnionTypeDef] = None
    SortBy: Optional[Sequence[SortDefinitionTypeDef]] = None
    BillingViewArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetReservationCoverageRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional[ExpressionUnionTypeDef] = None
    Metrics: Optional[Sequence[str]] = None
    NextPageToken: Optional[str] = None
    SortBy: Optional[SortDefinitionTypeDef] = None
    MaxResults: Optional[int] = None


class GetReservationPurchaseRecommendationRequestTypeDef(BaseValidatorModel):
    Service: str
    AccountId: Optional[str] = None
    Filter: Optional[ExpressionUnionTypeDef] = None
    AccountScope: Optional[AccountScopeType] = None
    LookbackPeriodInDays: Optional[LookbackPeriodInDaysType] = None
    TermInYears: Optional[TermInYearsType] = None
    PaymentOption: Optional[PaymentOptionType] = None
    ServiceSpecification: Optional[ServiceSpecificationTypeDef] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetReservationUtilizationRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional[ExpressionUnionTypeDef] = None
    SortBy: Optional[SortDefinitionTypeDef] = None
    NextPageToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetRightsizingRecommendationRequestTypeDef(BaseValidatorModel):
    Service: str
    Filter: Optional[ExpressionUnionTypeDef] = None
    Configuration: Optional[RightsizingRecommendationConfigurationTypeDef] = None
    PageSize: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetSavingsPlansCoverageRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    GroupBy: Optional[Sequence[GroupDefinitionTypeDef]] = None
    Granularity: Optional[GranularityType] = None
    Filter: Optional[ExpressionUnionTypeDef] = None
    Metrics: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[SortDefinitionTypeDef] = None


class GetSavingsPlansPurchaseRecommendationRequestTypeDef(BaseValidatorModel):
    SavingsPlansType: SupportedSavingsPlansTypeType
    TermInYears: TermInYearsType
    PaymentOption: PaymentOptionType
    LookbackPeriodInDays: LookbackPeriodInDaysType
    AccountScope: Optional[AccountScopeType] = None
    NextPageToken: Optional[str] = None
    PageSize: Optional[int] = None
    Filter: Optional[ExpressionUnionTypeDef] = None


class GetSavingsPlansUtilizationDetailsRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    Filter: Optional[ExpressionUnionTypeDef] = None
    DataType: Optional[Sequence[SavingsPlansDataTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[SortDefinitionTypeDef] = None


class GetSavingsPlansUtilizationRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    Granularity: Optional[GranularityType] = None
    Filter: Optional[ExpressionUnionTypeDef] = None
    SortBy: Optional[SortDefinitionTypeDef] = None


class GetTagsRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    SearchString: Optional[str] = None
    TagKey: Optional[str] = None
    Filter: Optional[ExpressionUnionTypeDef] = None
    SortBy: Optional[Sequence[SortDefinitionTypeDef]] = None
    BillingViewArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextPageToken: Optional[str] = None


class GetUsageForecastRequestTypeDef(BaseValidatorModel):
    TimePeriod: DateIntervalTypeDef
    Metric: MetricType
    Granularity: GranularityType
    Filter: Optional[ExpressionUnionTypeDef] = None
    BillingViewArn: Optional[str] = None
    PredictionIntervalLevel: Optional[int] = None


class UpdateAnomalySubscriptionRequestTypeDef(BaseValidatorModel):
    SubscriptionArn: str
    Threshold: Optional[float] = None
    Frequency: Optional[AnomalySubscriptionFrequencyType] = None
    MonitorArnList: Optional[Sequence[str]] = None
    Subscribers: Optional[Sequence[SubscriberTypeDef]] = None
    SubscriptionName: Optional[str] = None
    ThresholdExpression: Optional[ExpressionUnionTypeDef] = None


class RightsizingRecommendationTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    CurrentInstance: Optional[CurrentInstanceTypeDef] = None
    RightsizingType: Optional[RightsizingTypeType] = None
    ModifyRecommendationDetail: Optional[ModifyRecommendationDetailTypeDef] = None
    TerminateRecommendationDetail: Optional[TerminateRecommendationDetailTypeDef] = None
    FindingReasonCodes: Optional[List[FindingReasonCodeType]] = None


class AnomalyMonitorUnionTypeDef(BaseValidatorModel):
    pass


class CreateAnomalyMonitorRequestTypeDef(BaseValidatorModel):
    AnomalyMonitor: AnomalyMonitorUnionTypeDef
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class AnomalySubscriptionUnionTypeDef(BaseValidatorModel):
    pass


class CreateAnomalySubscriptionRequestTypeDef(BaseValidatorModel):
    AnomalySubscription: AnomalySubscriptionUnionTypeDef
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class GetRightsizingRecommendationResponseTypeDef(BaseValidatorModel):
    Metadata: RightsizingRecommendationMetadataTypeDef
    Summary: RightsizingRecommendationSummaryTypeDef
    RightsizingRecommendations: List[RightsizingRecommendationTypeDef]
    NextPageToken: str
    Configuration: RightsizingRecommendationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CostCategoryRuleUnionTypeDef(BaseValidatorModel):
    pass


class CostCategorySplitChargeRuleUnionTypeDef(BaseValidatorModel):
    pass


class CreateCostCategoryDefinitionRequestTypeDef(BaseValidatorModel):
    Name: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: Sequence[CostCategoryRuleUnionTypeDef]
    EffectiveStart: Optional[str] = None
    DefaultValue: Optional[str] = None
    SplitChargeRules: Optional[Sequence[CostCategorySplitChargeRuleUnionTypeDef]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class UpdateCostCategoryDefinitionRequestTypeDef(BaseValidatorModel):
    CostCategoryArn: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: Sequence[CostCategoryRuleUnionTypeDef]
    EffectiveStart: Optional[str] = None
    DefaultValue: Optional[str] = None
    SplitChargeRules: Optional[Sequence[CostCategorySplitChargeRuleUnionTypeDef]] = None



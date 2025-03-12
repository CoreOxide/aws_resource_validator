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
from aws_resource_validator.pydantic_models.compute_optimizer_constants import *

class AccountEnrollmentStatusTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[StatusType] = None
    statusReason: Optional[str] = None
    lastUpdatedTimestamp: Optional[datetime] = None


class AutoScalingGroupEstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class UtilizationMetricTypeDef(BaseValidatorModel):
    name: Optional[MetricNameType] = None
    statistic: Optional[MetricStatisticType] = None
    value: Optional[float] = None


class MemorySizeConfigurationTypeDef(BaseValidatorModel):
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None


class CurrentPerformanceRiskRatingsTypeDef(BaseValidatorModel):
    high: Optional[int] = None
    medium: Optional[int] = None
    low: Optional[int] = None
    veryLow: Optional[int] = None


class CustomizableMetricParametersTypeDef(BaseValidatorModel):
    threshold: Optional[CustomizableMetricThresholdType] = None
    headroom: Optional[CustomizableMetricHeadroomType] = None


class DBStorageConfigurationTypeDef(BaseValidatorModel):
    storageType: Optional[str] = None
    allocatedStorage: Optional[int] = None
    iops: Optional[int] = None
    maxAllocatedStorage: Optional[int] = None
    storageThroughput: Optional[int] = None


class ScopeTypeDef(BaseValidatorModel):
    name: Optional[ScopeNameType] = None
    value: Optional[str] = None


class JobFilterTypeDef(BaseValidatorModel):
    name: Optional[JobFilterNameType] = None
    values: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EBSSavingsEstimationModeTypeDef(BaseValidatorModel):
    source: Optional[EBSSavingsEstimationModeSourceType] = None


class EBSEstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class EBSFilterTypeDef(BaseValidatorModel):
    name: Optional[Literal["Finding"]] = None
    values: Optional[Sequence[str]] = None


class EBSUtilizationMetricTypeDef(BaseValidatorModel):
    name: Optional[EBSMetricNameType] = None
    statistic: Optional[MetricStatisticType] = None
    value: Optional[float] = None


class ECSSavingsEstimationModeTypeDef(BaseValidatorModel):
    source: Optional[ECSSavingsEstimationModeSourceType] = None


class ECSEstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class ECSServiceProjectedMetricTypeDef(BaseValidatorModel):
    name: Optional[ECSServiceMetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    upperBoundValues: Optional[List[float]] = None
    lowerBoundValues: Optional[List[float]] = None


class ECSServiceProjectedUtilizationMetricTypeDef(BaseValidatorModel):
    name: Optional[ECSServiceMetricNameType] = None
    statistic: Optional[ECSServiceMetricStatisticType] = None
    lowerBoundValue: Optional[float] = None
    upperBoundValue: Optional[float] = None


class ECSServiceRecommendationFilterTypeDef(BaseValidatorModel):
    name: Optional[ECSServiceRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None


class ECSServiceUtilizationMetricTypeDef(BaseValidatorModel):
    name: Optional[ECSServiceMetricNameType] = None
    statistic: Optional[ECSServiceMetricStatisticType] = None
    value: Optional[float] = None


class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class EffectivePreferredResourceTypeDef(BaseValidatorModel):
    name: Optional[Literal["Ec2InstanceTypes"]] = None
    includeList: Optional[List[str]] = None
    effectiveIncludeList: Optional[List[str]] = None
    excludeList: Optional[List[str]] = None


class ExternalMetricsPreferenceTypeDef(BaseValidatorModel):
    source: Optional[ExternalMetricsSourceType] = None


class InstanceSavingsEstimationModeTypeDef(BaseValidatorModel):
    source: Optional[InstanceSavingsEstimationModeSourceType] = None


class EnrollmentFilterTypeDef(BaseValidatorModel):
    name: Optional[Literal["Status"]] = None
    values: Optional[Sequence[str]] = None


class EstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class FilterTypeDef(BaseValidatorModel):
    name: Optional[FilterNameType] = None
    values: Optional[Sequence[str]] = None


class RecommendationPreferencesTypeDef(BaseValidatorModel):
    cpuVendorArchitectures: Optional[Sequence[CpuVendorArchitectureType]] = None


class S3DestinationConfigTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None


class S3DestinationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    metadataKey: Optional[str] = None


class IdleRecommendationFilterTypeDef(BaseValidatorModel):
    name: Optional[IdleRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None


class LambdaFunctionRecommendationFilterTypeDef(BaseValidatorModel):
    name: Optional[LambdaFunctionRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None


class LicenseRecommendationFilterTypeDef(BaseValidatorModel):
    name: Optional[LicenseRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None


class RDSDBRecommendationFilterTypeDef(BaseValidatorModel):
    name: Optional[RDSDBRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None


class ExternalMetricStatusTypeDef(BaseValidatorModel):
    statusCode: Optional[ExternalMetricStatusCodeType] = None
    statusReason: Optional[str] = None


class GetRecommendationErrorTypeDef(BaseValidatorModel):
    identifier: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None


class GetEffectiveRecommendationPreferencesRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class OrderByTypeDef(BaseValidatorModel):
    dimension: Optional[DimensionType] = None
    order: Optional[OrderType] = None


class IdleRecommendationErrorTypeDef(BaseValidatorModel):
    identifier: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None
    resourceType: Optional[IdleRecommendationResourceTypeType] = None


class GetRecommendationSummariesRequestTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GpuTypeDef(BaseValidatorModel):
    gpuCount: Optional[int] = None
    gpuMemorySizeInMiB: Optional[int] = None


class IdleEstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class IdleUtilizationMetricTypeDef(BaseValidatorModel):
    name: Optional[IdleMetricNameType] = None
    statistic: Optional[MetricStatisticType] = None
    value: Optional[float] = None


class IdleSummaryTypeDef(BaseValidatorModel):
    name: Optional[IdleFindingType] = None
    value: Optional[float] = None


class InstanceEstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class RecommendationSourceTypeDef(BaseValidatorModel):
    recommendationSourceArn: Optional[str] = None
    recommendationSourceType: Optional[RecommendationSourceTypeType] = None


class LambdaSavingsEstimationModeTypeDef(BaseValidatorModel):
    source: Optional[LambdaSavingsEstimationModeSourceType] = None


class LambdaEstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class LambdaFunctionMemoryProjectedMetricTypeDef(BaseValidatorModel):
    name: Optional[Literal["Duration"]] = None
    statistic: Optional[LambdaFunctionMemoryMetricStatisticType] = None
    value: Optional[float] = None


class LambdaFunctionUtilizationMetricTypeDef(BaseValidatorModel):
    name: Optional[LambdaFunctionMetricNameType] = None
    statistic: Optional[LambdaFunctionMetricStatisticType] = None
    value: Optional[float] = None


class MetricSourceTypeDef(BaseValidatorModel):
    provider: Optional[Literal["CloudWatchApplicationInsights"]] = None
    providerArn: Optional[str] = None


class PreferredResourceTypeDef(BaseValidatorModel):
    name: Optional[Literal["Ec2InstanceTypes"]] = None
    includeList: Optional[Sequence[str]] = None
    excludeList: Optional[Sequence[str]] = None


class ProjectedMetricTypeDef(BaseValidatorModel):
    name: Optional[MetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    values: Optional[List[float]] = None


class RDSDBUtilizationMetricTypeDef(BaseValidatorModel):
    name: Optional[RDSDBMetricNameType] = None
    statistic: Optional[RDSDBMetricStatisticType] = None
    value: Optional[float] = None


class RDSDatabaseProjectedMetricTypeDef(BaseValidatorModel):
    name: Optional[RDSDBMetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    values: Optional[List[float]] = None


class RDSSavingsEstimationModeTypeDef(BaseValidatorModel):
    source: Optional[RDSSavingsEstimationModeSourceType] = None


class RDSInstanceEstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class RDSStorageEstimatedMonthlySavingsTypeDef(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class ReasonCodeSummaryTypeDef(BaseValidatorModel):
    name: Optional[FindingReasonCodeType] = None
    value: Optional[float] = None


class UpdateEnrollmentStatusRequestTypeDef(BaseValidatorModel):
    status: StatusType
    includeMemberAccounts: Optional[bool] = None


class VolumeConfigurationTypeDef(BaseValidatorModel):
    volumeType: Optional[str] = None
    volumeSize: Optional[int] = None
    volumeBaselineIOPS: Optional[int] = None
    volumeBurstIOPS: Optional[int] = None
    volumeBaselineThroughput: Optional[int] = None
    volumeBurstThroughput: Optional[int] = None
    rootVolume: Optional[bool] = None


class AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[AutoScalingGroupEstimatedMonthlySavingsTypeDef] = None


class ContainerConfigurationTypeDef(BaseValidatorModel):
    containerName: Optional[str] = None
    memorySizeConfiguration: Optional[MemorySizeConfigurationTypeDef] = None
    cpu: Optional[int] = None


class ContainerRecommendationTypeDef(BaseValidatorModel):
    containerName: Optional[str] = None
    memorySizeConfiguration: Optional[MemorySizeConfigurationTypeDef] = None
    cpu: Optional[int] = None


class UtilizationPreferenceTypeDef(BaseValidatorModel):
    metricName: Optional[CustomizableMetricNameType] = None
    metricParameters: Optional[CustomizableMetricParametersTypeDef] = None


class DeleteRecommendationPreferencesRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    recommendationPreferenceNames: Sequence[RecommendationPreferenceNameType]
    scope: Optional[ScopeTypeDef] = None


class GetRecommendationPreferencesRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    scope: Optional[ScopeTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeRecommendationExportJobsRequestTypeDef(BaseValidatorModel):
    jobIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[JobFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeRecommendationExportJobsRequestPaginateTypeDef(BaseValidatorModel):
    jobIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[JobFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRecommendationPreferencesRequestPaginateTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    scope: Optional[ScopeTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRecommendationSummariesRequestPaginateTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetEnrollmentStatusResponseTypeDef(BaseValidatorModel):
    status: StatusType
    statusReason: str
    memberAccountsEnrolled: bool
    lastUpdatedTimestamp: datetime
    numberOfMemberAccountsOptedIn: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetEnrollmentStatusesForOrganizationResponseTypeDef(BaseValidatorModel):
    accountEnrollmentStatuses: List[AccountEnrollmentStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateEnrollmentStatusResponseTypeDef(BaseValidatorModel):
    status: StatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class EBSEffectiveRecommendationPreferencesTypeDef(BaseValidatorModel):
    savingsEstimationMode: Optional[EBSSavingsEstimationModeTypeDef] = None


class EBSSavingsOpportunityAfterDiscountsTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[EBSEstimatedMonthlySavingsTypeDef] = None


class GetEBSVolumeRecommendationsRequestTypeDef(BaseValidatorModel):
    volumeArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[EBSFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None


class ECSEffectiveRecommendationPreferencesTypeDef(BaseValidatorModel):
    savingsEstimationMode: Optional[ECSSavingsEstimationModeTypeDef] = None


class ECSSavingsOpportunityAfterDiscountsTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[ECSEstimatedMonthlySavingsTypeDef] = None


class ECSServiceRecommendedOptionProjectedMetricTypeDef(BaseValidatorModel):
    recommendedCpuUnits: Optional[int] = None
    recommendedMemorySize: Optional[int] = None
    projectedMetrics: Optional[List[ECSServiceProjectedMetricTypeDef]] = None


class GetECSServiceRecommendationsRequestTypeDef(BaseValidatorModel):
    serviceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[ECSServiceRecommendationFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None


class GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[EnrollmentFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetEnrollmentStatusesForOrganizationRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[EnrollmentFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class InferredWorkloadSavingTypeDef(BaseValidatorModel):
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None
    estimatedMonthlySavings: Optional[EstimatedMonthlySavingsTypeDef] = None


class SavingsOpportunityTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[EstimatedMonthlySavingsTypeDef] = None


class GetAutoScalingGroupRecommendationsRequestTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    autoScalingGroupArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None


class GetEC2InstanceRecommendationsRequestTypeDef(BaseValidatorModel):
    instanceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None


class ExportAutoScalingGroupRecommendationsRequestTypeDef(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableAutoScalingGroupFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None


class ExportEBSVolumeRecommendationsRequestTypeDef(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[EBSFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableVolumeFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None


class ExportEC2InstanceRecommendationsRequestTypeDef(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableInstanceFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None


class ExportECSServiceRecommendationsRequestTypeDef(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[ECSServiceRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableECSServiceFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None


class ExportAutoScalingGroupRecommendationsResponseTypeDef(BaseValidatorModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportDestinationTypeDef(BaseValidatorModel):
    s3: Optional[S3DestinationTypeDef] = None


class ExportEBSVolumeRecommendationsResponseTypeDef(BaseValidatorModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportEC2InstanceRecommendationsResponseTypeDef(BaseValidatorModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportECSServiceRecommendationsResponseTypeDef(BaseValidatorModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportIdleRecommendationsResponseTypeDef(BaseValidatorModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportLambdaFunctionRecommendationsResponseTypeDef(BaseValidatorModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportLicenseRecommendationsResponseTypeDef(BaseValidatorModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportRDSDatabaseRecommendationsResponseTypeDef(BaseValidatorModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportIdleRecommendationsRequestTypeDef(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[IdleRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableIdleFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None


class ExportLambdaFunctionRecommendationsRequestTypeDef(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableLambdaFunctionFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None


class GetLambdaFunctionRecommendationsRequestPaginateTypeDef(BaseValidatorModel):
    functionArns: Optional[Sequence[str]] = None
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetLambdaFunctionRecommendationsRequestTypeDef(BaseValidatorModel):
    functionArns: Optional[Sequence[str]] = None
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ExportLicenseRecommendationsRequestTypeDef(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[LicenseRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableLicenseFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None


class GetLicenseRecommendationsRequestTypeDef(BaseValidatorModel):
    resourceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[LicenseRecommendationFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None


class ExportRDSDatabaseRecommendationsRequestTypeDef(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[RDSDBRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableRDSDBFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None


class GetRDSDatabaseRecommendationsRequestTypeDef(BaseValidatorModel):
    resourceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[RDSDBRecommendationFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetEC2RecommendationProjectedMetricsRequestTypeDef(BaseValidatorModel):
    instanceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None


class GetECSServiceRecommendationProjectedMetricsRequestTypeDef(BaseValidatorModel):
    serviceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef


class GetRDSDatabaseRecommendationProjectedMetricsRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None


class GetIdleRecommendationsRequestTypeDef(BaseValidatorModel):
    resourceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[IdleRecommendationFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None
    orderBy: Optional[OrderByTypeDef] = None


class GpuInfoTypeDef(BaseValidatorModel):
    gpus: Optional[List[GpuTypeDef]] = None


class IdleSavingsOpportunityAfterDiscountsTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[IdleEstimatedMonthlySavingsTypeDef] = None


class IdleSavingsOpportunityTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[IdleEstimatedMonthlySavingsTypeDef] = None


class InstanceSavingsOpportunityAfterDiscountsTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[InstanceEstimatedMonthlySavingsTypeDef] = None


class LambdaEffectiveRecommendationPreferencesTypeDef(BaseValidatorModel):
    savingsEstimationMode: Optional[LambdaSavingsEstimationModeTypeDef] = None


class LambdaSavingsOpportunityAfterDiscountsTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[LambdaEstimatedMonthlySavingsTypeDef] = None


class LicenseConfigurationTypeDef(BaseValidatorModel):
    numberOfCores: Optional[int] = None
    instanceType: Optional[str] = None
    operatingSystem: Optional[str] = None
    licenseEdition: Optional[LicenseEditionType] = None
    licenseName: Optional[Literal["SQLServer"]] = None
    licenseModel: Optional[LicenseModelType] = None
    licenseVersion: Optional[str] = None
    metricsSource: Optional[List[MetricSourceTypeDef]] = None


class RecommendedOptionProjectedMetricTypeDef(BaseValidatorModel):
    recommendedInstanceType: Optional[str] = None
    rank: Optional[int] = None
    projectedMetrics: Optional[List[ProjectedMetricTypeDef]] = None


class RDSDatabaseRecommendedOptionProjectedMetricTypeDef(BaseValidatorModel):
    recommendedDBInstanceClass: Optional[str] = None
    rank: Optional[int] = None
    projectedMetrics: Optional[List[RDSDatabaseProjectedMetricTypeDef]] = None


class RDSEffectiveRecommendationPreferencesTypeDef(BaseValidatorModel):
    cpuVendorArchitectures: Optional[List[CpuVendorArchitectureType]] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    savingsEstimationMode: Optional[RDSSavingsEstimationModeTypeDef] = None


class RDSInstanceSavingsOpportunityAfterDiscountsTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[RDSInstanceEstimatedMonthlySavingsTypeDef] = None


class RDSStorageSavingsOpportunityAfterDiscountsTypeDef(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[RDSStorageEstimatedMonthlySavingsTypeDef] = None


class SummaryTypeDef(BaseValidatorModel):
    name: Optional[FindingType] = None
    value: Optional[float] = None
    reasonCodeSummaries: Optional[List[ReasonCodeSummaryTypeDef]] = None


class ServiceConfigurationTypeDef(BaseValidatorModel):
    memory: Optional[int] = None
    cpu: Optional[int] = None
    containerConfigurations: Optional[List[ContainerConfigurationTypeDef]] = None
    autoScalingConfiguration: Optional[AutoScalingConfigurationType] = None
    taskDefinitionArn: Optional[str] = None


class EffectiveRecommendationPreferencesTypeDef(BaseValidatorModel):
    cpuVendorArchitectures: Optional[List[CpuVendorArchitectureType]] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreferenceTypeDef] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[List[UtilizationPreferenceTypeDef]] = None
    preferredResources: Optional[List[EffectivePreferredResourceTypeDef]] = None
    savingsEstimationMode: Optional[InstanceSavingsEstimationModeTypeDef] = None


class GetEffectiveRecommendationPreferencesResponseTypeDef(BaseValidatorModel):
    enhancedInfrastructureMetrics: EnhancedInfrastructureMetricsType
    externalMetricsPreference: ExternalMetricsPreferenceTypeDef
    lookBackPeriod: LookBackPeriodPreferenceType
    utilizationPreferences: List[UtilizationPreferenceTypeDef]
    preferredResources: List[EffectivePreferredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutRecommendationPreferencesRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    scope: Optional[ScopeTypeDef] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreferenceTypeDef] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[Sequence[UtilizationPreferenceTypeDef]] = None
    preferredResources: Optional[Sequence[PreferredResourceTypeDef]] = None
    savingsEstimationMode: Optional[SavingsEstimationModeType] = None


class RecommendationPreferencesDetailTypeDef(BaseValidatorModel):
    scope: Optional[ScopeTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreferenceTypeDef] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[List[UtilizationPreferenceTypeDef]] = None
    preferredResources: Optional[List[EffectivePreferredResourceTypeDef]] = None
    savingsEstimationMode: Optional[SavingsEstimationModeType] = None


class GetECSServiceRecommendationProjectedMetricsResponseTypeDef(BaseValidatorModel):
    recommendedOptionProjectedMetrics: List[ECSServiceRecommendedOptionProjectedMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ECSServiceRecommendationOptionTypeDef(BaseValidatorModel):
    memory: Optional[int] = None
    cpu: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[ECSSavingsOpportunityAfterDiscountsTypeDef] = None
    projectedUtilizationMetrics: Optional[List[ECSServiceProjectedUtilizationMetricTypeDef]] = None
    containerRecommendations: Optional[List[ContainerRecommendationTypeDef]] = None


class LicenseRecommendationOptionTypeDef(BaseValidatorModel):
    rank: Optional[int] = None
    operatingSystem: Optional[str] = None
    licenseEdition: Optional[LicenseEditionType] = None
    licenseModel: Optional[LicenseModelType] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None


class VolumeRecommendationOptionTypeDef(BaseValidatorModel):
    configuration: Optional[VolumeConfigurationTypeDef] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[EBSSavingsOpportunityAfterDiscountsTypeDef] = None


class RecommendationExportJobTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    destination: Optional[ExportDestinationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    status: Optional[JobStatusType] = None
    creationTimestamp: Optional[datetime] = None
    lastUpdatedTimestamp: Optional[datetime] = None
    failureReason: Optional[str] = None


class AutoScalingGroupConfigurationTypeDef(BaseValidatorModel):
    pass


class AutoScalingGroupRecommendationOptionTypeDef(BaseValidatorModel):
    configuration: Optional[AutoScalingGroupConfigurationTypeDef] = None
    instanceGpuInfo: Optional[GpuInfoTypeDef] = None
    projectedUtilizationMetrics: Optional[List[UtilizationMetricTypeDef]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[ AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef ] = None
    migrationEffort: Optional[MigrationEffortType] = None


class IdleRecommendationTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    resourceId: Optional[str] = None
    resourceType: Optional[IdleRecommendationResourceTypeType] = None
    accountId: Optional[str] = None
    finding: Optional[IdleFindingType] = None
    findingDescription: Optional[str] = None
    savingsOpportunity: Optional[IdleSavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[IdleSavingsOpportunityAfterDiscountsTypeDef] = None
    utilizationMetrics: Optional[List[IdleUtilizationMetricTypeDef]] = None
    lookBackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None


class InstanceRecommendationOptionTypeDef(BaseValidatorModel):
    instanceType: Optional[str] = None
    instanceGpuInfo: Optional[GpuInfoTypeDef] = None
    projectedUtilizationMetrics: Optional[List[UtilizationMetricTypeDef]] = None
    platformDifferences: Optional[List[PlatformDifferenceType]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[InstanceSavingsOpportunityAfterDiscountsTypeDef] = None
    migrationEffort: Optional[MigrationEffortType] = None


class LambdaFunctionMemoryRecommendationOptionTypeDef(BaseValidatorModel):
    rank: Optional[int] = None
    memorySize: Optional[int] = None
    projectedUtilizationMetrics: Optional[List[LambdaFunctionMemoryProjectedMetricTypeDef]] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[LambdaSavingsOpportunityAfterDiscountsTypeDef] = None


class GetEC2RecommendationProjectedMetricsResponseTypeDef(BaseValidatorModel):
    recommendedOptionProjectedMetrics: List[RecommendedOptionProjectedMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef(BaseValidatorModel):
    recommendedOptionProjectedMetrics: List[RDSDatabaseRecommendedOptionProjectedMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RDSDBInstanceRecommendationOptionTypeDef(BaseValidatorModel):
    dbInstanceClass: Optional[str] = None
    projectedUtilizationMetrics: Optional[List[RDSDBUtilizationMetricTypeDef]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[ RDSInstanceSavingsOpportunityAfterDiscountsTypeDef ] = None


class RDSDBStorageRecommendationOptionTypeDef(BaseValidatorModel):
    storageConfiguration: Optional[DBStorageConfigurationTypeDef] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[RDSStorageSavingsOpportunityAfterDiscountsTypeDef] = None


class RecommendationSummaryTypeDef(BaseValidatorModel):
    summaries: Optional[List[SummaryTypeDef]] = None
    idleSummaries: Optional[List[IdleSummaryTypeDef]] = None
    recommendationResourceType: Optional[RecommendationSourceTypeType] = None
    accountId: Optional[str] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    idleSavingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    aggregatedSavingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    currentPerformanceRiskRatings: Optional[CurrentPerformanceRiskRatingsTypeDef] = None
    inferredWorkloadSavings: Optional[List[InferredWorkloadSavingTypeDef]] = None


class GetRecommendationPreferencesResponseTypeDef(BaseValidatorModel):
    recommendationPreferencesDetails: List[RecommendationPreferencesDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ECSServiceRecommendationTypeDef(BaseValidatorModel):
    serviceArn: Optional[str] = None
    accountId: Optional[str] = None
    currentServiceConfiguration: Optional[ServiceConfigurationTypeDef] = None
    utilizationMetrics: Optional[List[ECSServiceUtilizationMetricTypeDef]] = None
    lookbackPeriodInDays: Optional[float] = None
    launchType: Optional[ECSServiceLaunchTypeType] = None
    lastRefreshTimestamp: Optional[datetime] = None
    finding: Optional[ECSServiceRecommendationFindingType] = None
    findingReasonCodes: Optional[List[ECSServiceRecommendationFindingReasonCodeType]] = None
    serviceRecommendationOptions: Optional[List[ECSServiceRecommendationOptionTypeDef]] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[ECSEffectiveRecommendationPreferencesTypeDef] = None
    tags: Optional[List[TagTypeDef]] = None


class LicenseRecommendationTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    accountId: Optional[str] = None
    currentLicenseConfiguration: Optional[LicenseConfigurationTypeDef] = None
    lookbackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    finding: Optional[LicenseFindingType] = None
    findingReasonCodes: Optional[List[LicenseFindingReasonCodeType]] = None
    licenseRecommendationOptions: Optional[List[LicenseRecommendationOptionTypeDef]] = None
    tags: Optional[List[TagTypeDef]] = None


class VolumeRecommendationTypeDef(BaseValidatorModel):
    volumeArn: Optional[str] = None
    accountId: Optional[str] = None
    currentConfiguration: Optional[VolumeConfigurationTypeDef] = None
    finding: Optional[EBSFindingType] = None
    utilizationMetrics: Optional[List[EBSUtilizationMetricTypeDef]] = None
    lookBackPeriodInDays: Optional[float] = None
    volumeRecommendationOptions: Optional[List[VolumeRecommendationOptionTypeDef]] = None
    lastRefreshTimestamp: Optional[datetime] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[EBSEffectiveRecommendationPreferencesTypeDef] = None
    tags: Optional[List[TagTypeDef]] = None


class DescribeRecommendationExportJobsResponseTypeDef(BaseValidatorModel):
    recommendationExportJobs: List[RecommendationExportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AutoScalingGroupRecommendationTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    autoScalingGroupArn: Optional[str] = None
    autoScalingGroupName: Optional[str] = None
    finding: Optional[FindingType] = None
    utilizationMetrics: Optional[List[UtilizationMetricTypeDef]] = None
    lookBackPeriodInDays: Optional[float] = None
    currentConfiguration: Optional[AutoScalingGroupConfigurationTypeDef] = None
    currentInstanceGpuInfo: Optional[GpuInfoTypeDef] = None
    recommendationOptions: Optional[List[AutoScalingGroupRecommendationOptionTypeDef]] = None
    lastRefreshTimestamp: Optional[datetime] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[EffectiveRecommendationPreferencesTypeDef] = None
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None


class GetIdleRecommendationsResponseTypeDef(BaseValidatorModel):
    idleRecommendations: List[IdleRecommendationTypeDef]
    errors: List[IdleRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class InstanceRecommendationTypeDef(BaseValidatorModel):
    instanceArn: Optional[str] = None
    accountId: Optional[str] = None
    instanceName: Optional[str] = None
    currentInstanceType: Optional[str] = None
    finding: Optional[FindingType] = None
    findingReasonCodes: Optional[List[InstanceRecommendationFindingReasonCodeType]] = None
    utilizationMetrics: Optional[List[UtilizationMetricTypeDef]] = None
    lookBackPeriodInDays: Optional[float] = None
    recommendationOptions: Optional[List[InstanceRecommendationOptionTypeDef]] = None
    recommendationSources: Optional[List[RecommendationSourceTypeDef]] = None
    lastRefreshTimestamp: Optional[datetime] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[EffectiveRecommendationPreferencesTypeDef] = None
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None
    instanceState: Optional[InstanceStateType] = None
    tags: Optional[List[TagTypeDef]] = None
    externalMetricStatus: Optional[ExternalMetricStatusTypeDef] = None
    currentInstanceGpuInfo: Optional[GpuInfoTypeDef] = None
    idle: Optional[InstanceIdleType] = None


class LambdaFunctionRecommendationTypeDef(BaseValidatorModel):
    functionArn: Optional[str] = None
    functionVersion: Optional[str] = None
    accountId: Optional[str] = None
    currentMemorySize: Optional[int] = None
    numberOfInvocations: Optional[int] = None
    utilizationMetrics: Optional[List[LambdaFunctionUtilizationMetricTypeDef]] = None
    lookbackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    finding: Optional[LambdaFunctionRecommendationFindingType] = None
    findingReasonCodes: Optional[List[LambdaFunctionRecommendationFindingReasonCodeType]] = None
    memorySizeRecommendationOptions: Optional[ List[LambdaFunctionMemoryRecommendationOptionTypeDef] ] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[LambdaEffectiveRecommendationPreferencesTypeDef] = None
    tags: Optional[List[TagTypeDef]] = None


class RDSDBRecommendationTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    accountId: Optional[str] = None
    engine: Optional[str] = None
    engineVersion: Optional[str] = None
    promotionTier: Optional[int] = None
    currentDBInstanceClass: Optional[str] = None
    currentStorageConfiguration: Optional[DBStorageConfigurationTypeDef] = None
    dbClusterIdentifier: Optional[str] = None
    idle: Optional[IdleType] = None
    instanceFinding: Optional[RDSInstanceFindingType] = None
    storageFinding: Optional[RDSStorageFindingType] = None
    instanceFindingReasonCodes: Optional[List[RDSInstanceFindingReasonCodeType]] = None
    currentInstancePerformanceRisk: Optional[RDSCurrentInstancePerformanceRiskType] = None
    storageFindingReasonCodes: Optional[List[RDSStorageFindingReasonCodeType]] = None
    instanceRecommendationOptions: Optional[List[RDSDBInstanceRecommendationOptionTypeDef]] = None
    storageRecommendationOptions: Optional[List[RDSDBStorageRecommendationOptionTypeDef]] = None
    utilizationMetrics: Optional[List[RDSDBUtilizationMetricTypeDef]] = None
    effectiveRecommendationPreferences: Optional[RDSEffectiveRecommendationPreferencesTypeDef] = None
    lookbackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None


class GetRecommendationSummariesResponseTypeDef(BaseValidatorModel):
    recommendationSummaries: List[RecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetECSServiceRecommendationsResponseTypeDef(BaseValidatorModel):
    ecsServiceRecommendations: List[ECSServiceRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetLicenseRecommendationsResponseTypeDef(BaseValidatorModel):
    licenseRecommendations: List[LicenseRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetEBSVolumeRecommendationsResponseTypeDef(BaseValidatorModel):
    volumeRecommendations: List[VolumeRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetAutoScalingGroupRecommendationsResponseTypeDef(BaseValidatorModel):
    autoScalingGroupRecommendations: List[AutoScalingGroupRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetEC2InstanceRecommendationsResponseTypeDef(BaseValidatorModel):
    instanceRecommendations: List[InstanceRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetLambdaFunctionRecommendationsResponseTypeDef(BaseValidatorModel):
    lambdaFunctionRecommendations: List[LambdaFunctionRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetRDSDatabaseRecommendationsResponseTypeDef(BaseValidatorModel):
    rdsDBRecommendations: List[RDSDBRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None



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
from aws_resource_validator.pydantic_models.compute_optimizer_constants import *

class AccountEnrollmentStatusTypeDef(BaseModel):
    accountId: Optional[str] = None
    status: Optional[StatusType] = None
    statusReason: Optional[str] = None
    lastUpdatedTimestamp: Optional[datetime] = None

class AutoScalingGroupConfigurationTypeDef(BaseModel):
    desiredCapacity: Optional[int] = None
    minSize: Optional[int] = None
    maxSize: Optional[int] = None
    instanceType: Optional[str] = None

class AutoScalingGroupEstimatedMonthlySavingsTypeDef(BaseModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None

class UtilizationMetricTypeDef(BaseModel):
    name: Optional[MetricNameType] = None
    statistic: Optional[MetricStatisticType] = None
    value: Optional[float] = None

class MemorySizeConfigurationTypeDef(BaseModel):
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None

class CurrentPerformanceRiskRatingsTypeDef(BaseModel):
    high: Optional[int] = None
    medium: Optional[int] = None
    low: Optional[int] = None
    veryLow: Optional[int] = None

class CustomizableMetricParametersTypeDef(BaseModel):
    threshold: Optional[CustomizableMetricThresholdType] = None
    headroom: Optional[CustomizableMetricHeadroomType] = None

class DBStorageConfigurationTypeDef(BaseModel):
    storageType: Optional[str] = None
    allocatedStorage: Optional[int] = None
    iops: Optional[int] = None
    maxAllocatedStorage: Optional[int] = None
    storageThroughput: Optional[int] = None

class ScopeTypeDef(BaseModel):
    name: Optional[ScopeNameType] = None
    value: Optional[str] = None

class JobFilterTypeDef(BaseModel):
    name: Optional[JobFilterNameType] = None
    values: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class EBSSavingsEstimationModeTypeDef(BaseModel):
    source: Optional[EBSSavingsEstimationModeSourceType] = None

class EBSEstimatedMonthlySavingsTypeDef(BaseModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None

class EBSFilterTypeDef(BaseModel):
    name: Optional[Literal["Finding"]] = None
    values: Optional[Sequence[str]] = None

class EBSUtilizationMetricTypeDef(BaseModel):
    name: Optional[EBSMetricNameType] = None
    statistic: Optional[MetricStatisticType] = None
    value: Optional[float] = None

class ECSSavingsEstimationModeTypeDef(BaseModel):
    source: Optional[ECSSavingsEstimationModeSourceType] = None

class ECSEstimatedMonthlySavingsTypeDef(BaseModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None

class ECSServiceProjectedMetricTypeDef(BaseModel):
    name: Optional[ECSServiceMetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    upperBoundValues: Optional[List[float]] = None
    lowerBoundValues: Optional[List[float]] = None

class ECSServiceProjectedUtilizationMetricTypeDef(BaseModel):
    name: Optional[ECSServiceMetricNameType] = None
    statistic: Optional[ECSServiceMetricStatisticType] = None
    lowerBoundValue: Optional[float] = None
    upperBoundValue: Optional[float] = None

class ECSServiceRecommendationFilterTypeDef(BaseModel):
    name: Optional[ECSServiceRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None

class ECSServiceUtilizationMetricTypeDef(BaseModel):
    name: Optional[ECSServiceMetricNameType] = None
    statistic: Optional[ECSServiceMetricStatisticType] = None
    value: Optional[float] = None

class TagTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class EffectivePreferredResourceTypeDef(BaseModel):
    name: Optional[Literal["Ec2InstanceTypes"]] = None
    includeList: Optional[List[str]] = None
    effectiveIncludeList: Optional[List[str]] = None
    excludeList: Optional[List[str]] = None

class ExternalMetricsPreferenceTypeDef(BaseModel):
    source: Optional[ExternalMetricsSourceType] = None

class InstanceSavingsEstimationModeTypeDef(BaseModel):
    source: Optional[InstanceSavingsEstimationModeSourceType] = None

class EnrollmentFilterTypeDef(BaseModel):
    name: Optional[Literal["Status"]] = None
    values: Optional[Sequence[str]] = None

class EstimatedMonthlySavingsTypeDef(BaseModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None

class FilterTypeDef(BaseModel):
    name: Optional[FilterNameType] = None
    values: Optional[Sequence[str]] = None

class RecommendationPreferencesTypeDef(BaseModel):
    cpuVendorArchitectures: Optional[Sequence[CpuVendorArchitectureType]] = None

class S3DestinationConfigTypeDef(BaseModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None

class S3DestinationTypeDef(BaseModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    metadataKey: Optional[str] = None

class LambdaFunctionRecommendationFilterTypeDef(BaseModel):
    name: Optional[LambdaFunctionRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None

class LicenseRecommendationFilterTypeDef(BaseModel):
    name: Optional[LicenseRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None

class RDSDBRecommendationFilterTypeDef(BaseModel):
    name: Optional[RDSDBRecommendationFilterNameType] = None
    values: Optional[Sequence[str]] = None

class ExternalMetricStatusTypeDef(BaseModel):
    statusCode: Optional[ExternalMetricStatusCodeType] = None
    statusReason: Optional[str] = None

class GetRecommendationErrorTypeDef(BaseModel):
    identifier: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

class GetEffectiveRecommendationPreferencesRequestRequestTypeDef(BaseModel):
    resourceArn: str

class GetRecommendationSummariesRequestRequestTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GpuTypeDef(BaseModel):
    gpuCount: Optional[int] = None
    gpuMemorySizeInMiB: Optional[int] = None

class InstanceEstimatedMonthlySavingsTypeDef(BaseModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None

class RecommendationSourceTypeDef(BaseModel):
    recommendationSourceArn: Optional[str] = None
    recommendationSourceType: Optional[RecommendationSourceTypeType] = None

class LambdaSavingsEstimationModeTypeDef(BaseModel):
    source: Optional[LambdaSavingsEstimationModeSourceType] = None

class LambdaEstimatedMonthlySavingsTypeDef(BaseModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None

class LambdaFunctionMemoryProjectedMetricTypeDef(BaseModel):
    name: Optional[Literal["Duration"]] = None
    statistic: Optional[LambdaFunctionMemoryMetricStatisticType] = None
    value: Optional[float] = None

class LambdaFunctionUtilizationMetricTypeDef(BaseModel):
    name: Optional[LambdaFunctionMetricNameType] = None
    statistic: Optional[LambdaFunctionMetricStatisticType] = None
    value: Optional[float] = None

class MetricSourceTypeDef(BaseModel):
    provider: Optional[Literal["CloudWatchApplicationInsights"]] = None
    providerArn: Optional[str] = None

class PreferredResourceTypeDef(BaseModel):
    name: Optional[Literal["Ec2InstanceTypes"]] = None
    includeList: Optional[Sequence[str]] = None
    excludeList: Optional[Sequence[str]] = None

class ProjectedMetricTypeDef(BaseModel):
    name: Optional[MetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    values: Optional[List[float]] = None

class RDSDBUtilizationMetricTypeDef(BaseModel):
    name: Optional[RDSDBMetricNameType] = None
    statistic: Optional[RDSDBMetricStatisticType] = None
    value: Optional[float] = None

class RDSDatabaseProjectedMetricTypeDef(BaseModel):
    name: Optional[RDSDBMetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    values: Optional[List[float]] = None

class RDSSavingsEstimationModeTypeDef(BaseModel):
    source: Optional[RDSSavingsEstimationModeSourceType] = None

class RDSInstanceEstimatedMonthlySavingsTypeDef(BaseModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None

class RDSStorageEstimatedMonthlySavingsTypeDef(BaseModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None

class ReasonCodeSummaryTypeDef(BaseModel):
    name: Optional[FindingReasonCodeType] = None
    value: Optional[float] = None

class UpdateEnrollmentStatusRequestRequestTypeDef(BaseModel):
    status: StatusType
    includeMemberAccounts: Optional[bool] = None

class VolumeConfigurationTypeDef(BaseModel):
    volumeType: Optional[str] = None
    volumeSize: Optional[int] = None
    volumeBaselineIOPS: Optional[int] = None
    volumeBurstIOPS: Optional[int] = None
    volumeBaselineThroughput: Optional[int] = None
    volumeBurstThroughput: Optional[int] = None
    rootVolume: Optional[bool] = None

class AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef(BaseModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[AutoScalingGroupEstimatedMonthlySavingsTypeDef] = None

class ContainerConfigurationTypeDef(BaseModel):
    containerName: Optional[str] = None
    memorySizeConfiguration: Optional[MemorySizeConfigurationTypeDef] = None
    cpu: Optional[int] = None

class ContainerRecommendationTypeDef(BaseModel):
    containerName: Optional[str] = None
    memorySizeConfiguration: Optional[MemorySizeConfigurationTypeDef] = None
    cpu: Optional[int] = None

class UtilizationPreferenceTypeDef(BaseModel):
    metricName: Optional[CustomizableMetricNameType] = None
    metricParameters: Optional[CustomizableMetricParametersTypeDef] = None

class DeleteRecommendationPreferencesRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    recommendationPreferenceNames: Sequence[RecommendationPreferenceNameType]
    scope: Optional[ScopeTypeDef] = None

class GetRecommendationPreferencesRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    scope: Optional[ScopeTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeRecommendationExportJobsRequestRequestTypeDef(BaseModel):
    jobIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[JobFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeRecommendationExportJobsRequestDescribeRecommendationExportJobsPaginateTypeDef(BaseModel):
    jobIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[JobFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRecommendationPreferencesRequestGetRecommendationPreferencesPaginateTypeDef(BaseModel):
    resourceType: ResourceTypeType
    scope: Optional[ScopeTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRecommendationSummariesRequestGetRecommendationSummariesPaginateTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetEnrollmentStatusResponseTypeDef(BaseModel):
    status: StatusType
    statusReason: str
    memberAccountsEnrolled: bool
    lastUpdatedTimestamp: datetime
    numberOfMemberAccountsOptedIn: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnrollmentStatusesForOrganizationResponseTypeDef(BaseModel):
    accountEnrollmentStatuses: List[AccountEnrollmentStatusTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnrollmentStatusResponseTypeDef(BaseModel):
    status: StatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class EBSEffectiveRecommendationPreferencesTypeDef(BaseModel):
    savingsEstimationMode: Optional[EBSSavingsEstimationModeTypeDef] = None

class EBSSavingsOpportunityAfterDiscountsTypeDef(BaseModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[EBSEstimatedMonthlySavingsTypeDef] = None

class GetEBSVolumeRecommendationsRequestRequestTypeDef(BaseModel):
    volumeArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[EBSFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None

class ECSEffectiveRecommendationPreferencesTypeDef(BaseModel):
    savingsEstimationMode: Optional[ECSSavingsEstimationModeTypeDef] = None

class ECSSavingsOpportunityAfterDiscountsTypeDef(BaseModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[ECSEstimatedMonthlySavingsTypeDef] = None

class ECSServiceRecommendedOptionProjectedMetricTypeDef(BaseModel):
    recommendedCpuUnits: Optional[int] = None
    recommendedMemorySize: Optional[int] = None
    projectedMetrics: Optional[List[ECSServiceProjectedMetricTypeDef]] = None

class GetECSServiceRecommendationsRequestRequestTypeDef(BaseModel):
    serviceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[ECSServiceRecommendationFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None

class GetEnrollmentStatusesForOrganizationRequestGetEnrollmentStatusesForOrganizationPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[EnrollmentFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetEnrollmentStatusesForOrganizationRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[EnrollmentFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class InferredWorkloadSavingTypeDef(BaseModel):
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None
    estimatedMonthlySavings: Optional[EstimatedMonthlySavingsTypeDef] = None

class SavingsOpportunityTypeDef(BaseModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[EstimatedMonthlySavingsTypeDef] = None

class GetAutoScalingGroupRecommendationsRequestRequestTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    autoScalingGroupArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None

class GetEC2InstanceRecommendationsRequestRequestTypeDef(BaseModel):
    instanceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None

class ExportAutoScalingGroupRecommendationsRequestRequestTypeDef(BaseModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableAutoScalingGroupFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None

class ExportEBSVolumeRecommendationsRequestRequestTypeDef(BaseModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[EBSFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableVolumeFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None

class ExportEC2InstanceRecommendationsRequestRequestTypeDef(BaseModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableInstanceFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None

class ExportECSServiceRecommendationsRequestRequestTypeDef(BaseModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[ECSServiceRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableECSServiceFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None

class ExportAutoScalingGroupRecommendationsResponseTypeDef(BaseModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportDestinationTypeDef(BaseModel):
    s3: Optional[S3DestinationTypeDef] = None

class ExportEBSVolumeRecommendationsResponseTypeDef(BaseModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportEC2InstanceRecommendationsResponseTypeDef(BaseModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportECSServiceRecommendationsResponseTypeDef(BaseModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportLambdaFunctionRecommendationsResponseTypeDef(BaseModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportLicenseRecommendationsResponseTypeDef(BaseModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportRDSDatabaseRecommendationsResponseTypeDef(BaseModel):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportLambdaFunctionRecommendationsRequestRequestTypeDef(BaseModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableLambdaFunctionFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None

class GetLambdaFunctionRecommendationsRequestGetLambdaFunctionRecommendationsPaginateTypeDef(BaseModel):
    functionArns: Optional[Sequence[str]] = None
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetLambdaFunctionRecommendationsRequestRequestTypeDef(BaseModel):
    functionArns: Optional[Sequence[str]] = None
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ExportLicenseRecommendationsRequestRequestTypeDef(BaseModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[LicenseRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableLicenseFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None

class GetLicenseRecommendationsRequestRequestTypeDef(BaseModel):
    resourceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[LicenseRecommendationFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None

class ExportRDSDatabaseRecommendationsRequestRequestTypeDef(BaseModel):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[RDSDBRecommendationFilterTypeDef]] = None
    fieldsToExport: Optional[Sequence[ExportableRDSDBFieldType]] = None
    fileFormat: Optional[Literal["Csv"]] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None

class GetRDSDatabaseRecommendationsRequestRequestTypeDef(BaseModel):
    resourceArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[RDSDBRecommendationFilterTypeDef]] = None
    accountIds: Optional[Sequence[str]] = None
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None

class GetEC2RecommendationProjectedMetricsRequestRequestTypeDef(BaseModel):
    instanceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None

class GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef(BaseModel):
    serviceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef

class GetRDSDatabaseRecommendationProjectedMetricsRequestRequestTypeDef(BaseModel):
    resourceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    recommendationPreferences: Optional[RecommendationPreferencesTypeDef] = None

class GpuInfoTypeDef(BaseModel):
    gpus: Optional[List[GpuTypeDef]] = None

class InstanceSavingsOpportunityAfterDiscountsTypeDef(BaseModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[InstanceEstimatedMonthlySavingsTypeDef] = None

class LambdaEffectiveRecommendationPreferencesTypeDef(BaseModel):
    savingsEstimationMode: Optional[LambdaSavingsEstimationModeTypeDef] = None

class LambdaSavingsOpportunityAfterDiscountsTypeDef(BaseModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[LambdaEstimatedMonthlySavingsTypeDef] = None

class LicenseConfigurationTypeDef(BaseModel):
    numberOfCores: Optional[int] = None
    instanceType: Optional[str] = None
    operatingSystem: Optional[str] = None
    licenseEdition: Optional[LicenseEditionType] = None
    licenseName: Optional[Literal["SQLServer"]] = None
    licenseModel: Optional[LicenseModelType] = None
    licenseVersion: Optional[str] = None
    metricsSource: Optional[List[MetricSourceTypeDef]] = None

class RecommendedOptionProjectedMetricTypeDef(BaseModel):
    recommendedInstanceType: Optional[str] = None
    rank: Optional[int] = None
    projectedMetrics: Optional[List[ProjectedMetricTypeDef]] = None

class RDSDatabaseRecommendedOptionProjectedMetricTypeDef(BaseModel):
    recommendedDBInstanceClass: Optional[str] = None
    rank: Optional[int] = None
    projectedMetrics: Optional[List[RDSDatabaseProjectedMetricTypeDef]] = None

class RDSEffectiveRecommendationPreferencesTypeDef(BaseModel):
    cpuVendorArchitectures: Optional[List[CpuVendorArchitectureType]] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    savingsEstimationMode: Optional[RDSSavingsEstimationModeTypeDef] = None

class RDSInstanceSavingsOpportunityAfterDiscountsTypeDef(BaseModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[RDSInstanceEstimatedMonthlySavingsTypeDef] = None

class RDSStorageSavingsOpportunityAfterDiscountsTypeDef(BaseModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[RDSStorageEstimatedMonthlySavingsTypeDef] = None

class SummaryTypeDef(BaseModel):
    name: Optional[FindingType] = None
    value: Optional[float] = None
    reasonCodeSummaries: Optional[List[ReasonCodeSummaryTypeDef]] = None

class ServiceConfigurationTypeDef(BaseModel):
    memory: Optional[int] = None
    cpu: Optional[int] = None
    containerConfigurations: Optional[List[ContainerConfigurationTypeDef]] = None
    autoScalingConfiguration: Optional[AutoScalingConfigurationType] = None
    taskDefinitionArn: Optional[str] = None

class EffectiveRecommendationPreferencesTypeDef(BaseModel):
    cpuVendorArchitectures: Optional[List[CpuVendorArchitectureType]] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreferenceTypeDef] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[List[UtilizationPreferenceTypeDef]] = None
    preferredResources: Optional[List[EffectivePreferredResourceTypeDef]] = None
    savingsEstimationMode: Optional[InstanceSavingsEstimationModeTypeDef] = None

class GetEffectiveRecommendationPreferencesResponseTypeDef(BaseModel):
    enhancedInfrastructureMetrics: EnhancedInfrastructureMetricsType
    externalMetricsPreference: ExternalMetricsPreferenceTypeDef
    lookBackPeriod: LookBackPeriodPreferenceType
    utilizationPreferences: List[UtilizationPreferenceTypeDef]
    preferredResources: List[EffectivePreferredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecommendationPreferencesRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    scope: Optional[ScopeTypeDef] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreferenceTypeDef] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[Sequence[UtilizationPreferenceTypeDef]] = None
    preferredResources: Optional[Sequence[PreferredResourceTypeDef]] = None
    savingsEstimationMode: Optional[SavingsEstimationModeType] = None

class RecommendationPreferencesDetailTypeDef(BaseModel):
    scope: Optional[ScopeTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreferenceTypeDef] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[List[UtilizationPreferenceTypeDef]] = None
    preferredResources: Optional[List[EffectivePreferredResourceTypeDef]] = None
    savingsEstimationMode: Optional[SavingsEstimationModeType] = None

class GetECSServiceRecommendationProjectedMetricsResponseTypeDef(BaseModel):
    recommendedOptionProjectedMetrics: List[       ECSServiceRecommendedOptionProjectedMetricTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class ECSServiceRecommendationOptionTypeDef(BaseModel):
    memory: Optional[int] = None
    cpu: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[ECSSavingsOpportunityAfterDiscountsTypeDef] = None
    projectedUtilizationMetrics: Optional[       List[ECSServiceProjectedUtilizationMetricTypeDef]     ] = None
    containerRecommendations: Optional[List[ContainerRecommendationTypeDef]] = None

class LicenseRecommendationOptionTypeDef(BaseModel):
    rank: Optional[int] = None
    operatingSystem: Optional[str] = None
    licenseEdition: Optional[LicenseEditionType] = None
    licenseModel: Optional[LicenseModelType] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None

class VolumeRecommendationOptionTypeDef(BaseModel):
    configuration: Optional[VolumeConfigurationTypeDef] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[EBSSavingsOpportunityAfterDiscountsTypeDef] = None

class RecommendationExportJobTypeDef(BaseModel):
    jobId: Optional[str] = None
    destination: Optional[ExportDestinationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    status: Optional[JobStatusType] = None
    creationTimestamp: Optional[datetime] = None
    lastUpdatedTimestamp: Optional[datetime] = None
    failureReason: Optional[str] = None

class AutoScalingGroupRecommendationOptionTypeDef(BaseModel):
    configuration: Optional[AutoScalingGroupConfigurationTypeDef] = None
    instanceGpuInfo: Optional[GpuInfoTypeDef] = None
    projectedUtilizationMetrics: Optional[List[UtilizationMetricTypeDef]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[       AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef     ] = None
    migrationEffort: Optional[MigrationEffortType] = None

class InstanceRecommendationOptionTypeDef(BaseModel):
    instanceType: Optional[str] = None
    instanceGpuInfo: Optional[GpuInfoTypeDef] = None
    projectedUtilizationMetrics: Optional[List[UtilizationMetricTypeDef]] = None
    platformDifferences: Optional[List[PlatformDifferenceType]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[       InstanceSavingsOpportunityAfterDiscountsTypeDef     ] = None
    migrationEffort: Optional[MigrationEffortType] = None

class LambdaFunctionMemoryRecommendationOptionTypeDef(BaseModel):
    rank: Optional[int] = None
    memorySize: Optional[int] = None
    projectedUtilizationMetrics: Optional[       List[LambdaFunctionMemoryProjectedMetricTypeDef]     ] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[       LambdaSavingsOpportunityAfterDiscountsTypeDef     ] = None

class GetEC2RecommendationProjectedMetricsResponseTypeDef(BaseModel):
    recommendedOptionProjectedMetrics: List[RecommendedOptionProjectedMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef(BaseModel):
    recommendedOptionProjectedMetrics: List[       RDSDatabaseRecommendedOptionProjectedMetricTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class RDSDBInstanceRecommendationOptionTypeDef(BaseModel):
    dbInstanceClass: Optional[str] = None
    projectedUtilizationMetrics: Optional[List[RDSDBUtilizationMetricTypeDef]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[       RDSInstanceSavingsOpportunityAfterDiscountsTypeDef     ] = None

class RDSDBStorageRecommendationOptionTypeDef(BaseModel):
    storageConfiguration: Optional[DBStorageConfigurationTypeDef] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    savingsOpportunityAfterDiscounts: Optional[       RDSStorageSavingsOpportunityAfterDiscountsTypeDef     ] = None

class RecommendationSummaryTypeDef(BaseModel):
    summaries: Optional[List[SummaryTypeDef]] = None
    recommendationResourceType: Optional[RecommendationSourceTypeType] = None
    accountId: Optional[str] = None
    savingsOpportunity: Optional[SavingsOpportunityTypeDef] = None
    currentPerformanceRiskRatings: Optional[CurrentPerformanceRiskRatingsTypeDef] = None
    inferredWorkloadSavings: Optional[List[InferredWorkloadSavingTypeDef]] = None

class GetRecommendationPreferencesResponseTypeDef(BaseModel):
    nextToken: str
    recommendationPreferencesDetails: List[RecommendationPreferencesDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ECSServiceRecommendationTypeDef(BaseModel):
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
    effectiveRecommendationPreferences: Optional[       ECSEffectiveRecommendationPreferencesTypeDef     ] = None
    tags: Optional[List[TagTypeDef]] = None

class LicenseRecommendationTypeDef(BaseModel):
    resourceArn: Optional[str] = None
    accountId: Optional[str] = None
    currentLicenseConfiguration: Optional[LicenseConfigurationTypeDef] = None
    lookbackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    finding: Optional[LicenseFindingType] = None
    findingReasonCodes: Optional[List[LicenseFindingReasonCodeType]] = None
    licenseRecommendationOptions: Optional[List[LicenseRecommendationOptionTypeDef]] = None
    tags: Optional[List[TagTypeDef]] = None

class VolumeRecommendationTypeDef(BaseModel):
    volumeArn: Optional[str] = None
    accountId: Optional[str] = None
    currentConfiguration: Optional[VolumeConfigurationTypeDef] = None
    finding: Optional[EBSFindingType] = None
    utilizationMetrics: Optional[List[EBSUtilizationMetricTypeDef]] = None
    lookBackPeriodInDays: Optional[float] = None
    volumeRecommendationOptions: Optional[List[VolumeRecommendationOptionTypeDef]] = None
    lastRefreshTimestamp: Optional[datetime] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[       EBSEffectiveRecommendationPreferencesTypeDef     ] = None
    tags: Optional[List[TagTypeDef]] = None

class DescribeRecommendationExportJobsResponseTypeDef(BaseModel):
    recommendationExportJobs: List[RecommendationExportJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AutoScalingGroupRecommendationTypeDef(BaseModel):
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
    effectiveRecommendationPreferences: Optional[       EffectiveRecommendationPreferencesTypeDef     ] = None
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None

class InstanceRecommendationTypeDef(BaseModel):
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
    effectiveRecommendationPreferences: Optional[       EffectiveRecommendationPreferencesTypeDef     ] = None
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None
    instanceState: Optional[InstanceStateType] = None
    tags: Optional[List[TagTypeDef]] = None
    externalMetricStatus: Optional[ExternalMetricStatusTypeDef] = None
    currentInstanceGpuInfo: Optional[GpuInfoTypeDef] = None
    idle: Optional[InstanceIdleType] = None

class LambdaFunctionRecommendationTypeDef(BaseModel):
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
    memorySizeRecommendationOptions: Optional[       List[LambdaFunctionMemoryRecommendationOptionTypeDef]     ] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[       LambdaEffectiveRecommendationPreferencesTypeDef     ] = None
    tags: Optional[List[TagTypeDef]] = None

class RDSDBRecommendationTypeDef(BaseModel):
    resourceArn: Optional[str] = None
    accountId: Optional[str] = None
    engine: Optional[str] = None
    engineVersion: Optional[str] = None
    currentDBInstanceClass: Optional[str] = None
    currentStorageConfiguration: Optional[DBStorageConfigurationTypeDef] = None
    idle: Optional[IdleType] = None
    instanceFinding: Optional[RDSInstanceFindingType] = None
    storageFinding: Optional[RDSStorageFindingType] = None
    instanceFindingReasonCodes: Optional[List[RDSInstanceFindingReasonCodeType]] = None
    storageFindingReasonCodes: Optional[List[RDSStorageFindingReasonCodeType]] = None
    instanceRecommendationOptions: Optional[       List[RDSDBInstanceRecommendationOptionTypeDef]     ] = None
    storageRecommendationOptions: Optional[List[RDSDBStorageRecommendationOptionTypeDef]] = None
    utilizationMetrics: Optional[List[RDSDBUtilizationMetricTypeDef]] = None
    effectiveRecommendationPreferences: Optional[       RDSEffectiveRecommendationPreferencesTypeDef     ] = None
    lookbackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None

class GetRecommendationSummariesResponseTypeDef(BaseModel):
    nextToken: str
    recommendationSummaries: List[RecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetECSServiceRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    ecsServiceRecommendations: List[ECSServiceRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLicenseRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    licenseRecommendations: List[LicenseRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEBSVolumeRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    volumeRecommendations: List[VolumeRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAutoScalingGroupRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    autoScalingGroupRecommendations: List[AutoScalingGroupRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEC2InstanceRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    instanceRecommendations: List[InstanceRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLambdaFunctionRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    lambdaFunctionRecommendations: List[LambdaFunctionRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRDSDatabaseRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    rdsDBRecommendations: List[RDSDBRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


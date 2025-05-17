from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountEnrollmentStatus(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[StatusType] = None
    statusReason: Optional[str] = None
    lastUpdatedTimestamp: Optional[datetime] = None


class AutoScalingGroupConfiguration(BaseValidatorModel):
    desiredCapacity: Optional[int] = None
    minSize: Optional[int] = None
    maxSize: Optional[int] = None
    instanceType: Optional[str] = None
    allocationStrategy: Optional[AllocationStrategyType] = None
    estimatedInstanceHourReductionPercentage: Optional[float] = None
    type: Optional[AsgTypeType] = None
    mixedInstanceTypes: Optional[List[str]] = None


class AutoScalingGroupEstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class UtilizationMetric(BaseValidatorModel):
    name: Optional[MetricNameType] = None
    statistic: Optional[MetricStatisticType] = None
    value: Optional[float] = None


class MemorySizeConfiguration(BaseValidatorModel):
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None


class CurrentPerformanceRiskRatings(BaseValidatorModel):
    high: Optional[int] = None
    medium: Optional[int] = None
    low: Optional[int] = None
    veryLow: Optional[int] = None


class CustomizableMetricParameters(BaseValidatorModel):
    threshold: Optional[CustomizableMetricThresholdType] = None
    headroom: Optional[CustomizableMetricHeadroomType] = None


class DBStorageConfiguration(BaseValidatorModel):
    storageType: Optional[str] = None
    allocatedStorage: Optional[int] = None
    iops: Optional[int] = None
    maxAllocatedStorage: Optional[int] = None
    storageThroughput: Optional[int] = None


class Scope(BaseValidatorModel):
    name: Optional[ScopeNameType] = None
    value: Optional[str] = None


class JobFilter(BaseValidatorModel):
    name: Optional[JobFilterNameType] = None
    values: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EBSSavingsEstimationMode(BaseValidatorModel):
    source: Optional[EBSSavingsEstimationModeSourceType] = None


class EBSEstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class EBSFilter(BaseValidatorModel):
    name: Optional[Literal['Finding']] = None
    values: Optional[List[str]] = None


class EBSUtilizationMetric(BaseValidatorModel):
    name: Optional[EBSMetricNameType] = None
    statistic: Optional[MetricStatisticType] = None
    value: Optional[float] = None


class ECSSavingsEstimationMode(BaseValidatorModel):
    source: Optional[ECSSavingsEstimationModeSourceType] = None


class ECSEstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class ECSServiceProjectedMetric(BaseValidatorModel):
    name: Optional[ECSServiceMetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    upperBoundValues: Optional[List[float]] = None
    lowerBoundValues: Optional[List[float]] = None


class ECSServiceProjectedUtilizationMetric(BaseValidatorModel):
    name: Optional[ECSServiceMetricNameType] = None
    statistic: Optional[ECSServiceMetricStatisticType] = None
    lowerBoundValue: Optional[float] = None
    upperBoundValue: Optional[float] = None


class ECSServiceRecommendationFilter(BaseValidatorModel):
    name: Optional[ECSServiceRecommendationFilterNameType] = None
    values: Optional[List[str]] = None


class ECSServiceUtilizationMetric(BaseValidatorModel):
    name: Optional[ECSServiceMetricNameType] = None
    statistic: Optional[ECSServiceMetricStatisticType] = None
    value: Optional[float] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class EffectivePreferredResource(BaseValidatorModel):
    name: Optional[Literal['Ec2InstanceTypes']] = None
    includeList: Optional[List[str]] = None
    effectiveIncludeList: Optional[List[str]] = None
    excludeList: Optional[List[str]] = None


class ExternalMetricsPreference(BaseValidatorModel):
    source: Optional[ExternalMetricsSourceType] = None


class InstanceSavingsEstimationMode(BaseValidatorModel):
    source: Optional[InstanceSavingsEstimationModeSourceType] = None


class EnrollmentFilter(BaseValidatorModel):
    name: Optional[Literal['Status']] = None
    values: Optional[List[str]] = None


class EstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class Filter(BaseValidatorModel):
    name: Optional[FilterNameType] = None
    values: Optional[List[str]] = None


class RecommendationPreferences(BaseValidatorModel):
    cpuVendorArchitectures: Optional[List[CpuVendorArchitectureType]] = None


class S3DestinationConfig(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None


class S3Destination(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    metadataKey: Optional[str] = None


class IdleRecommendationFilter(BaseValidatorModel):
    name: Optional[IdleRecommendationFilterNameType] = None
    values: Optional[List[str]] = None


class LambdaFunctionRecommendationFilter(BaseValidatorModel):
    name: Optional[LambdaFunctionRecommendationFilterNameType] = None
    values: Optional[List[str]] = None


class LicenseRecommendationFilter(BaseValidatorModel):
    name: Optional[LicenseRecommendationFilterNameType] = None
    values: Optional[List[str]] = None


class RDSDBRecommendationFilter(BaseValidatorModel):
    name: Optional[RDSDBRecommendationFilterNameType] = None
    values: Optional[List[str]] = None


class ExternalMetricStatus(BaseValidatorModel):
    statusCode: Optional[ExternalMetricStatusCodeType] = None
    statusReason: Optional[str] = None


class GetRecommendationError(BaseValidatorModel):
    identifier: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'get_effective_recommendation_preferences' function.
class GetEffectiveRecommendationPreferencesRequest(BaseValidatorModel):
    resourceArn: str


class OrderBy(BaseValidatorModel):
    dimension: Optional[DimensionType] = None
    order: Optional[OrderType] = None


class IdleRecommendationError(BaseValidatorModel):
    identifier: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None
    resourceType: Optional[IdleRecommendationResourceTypeType] = None


# This class is the input for the 'get_recommendation_summaries' function.
class GetRecommendationSummariesRequest(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class Gpu(BaseValidatorModel):
    gpuCount: Optional[int] = None
    gpuMemorySizeInMiB: Optional[int] = None


class IdleEstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class IdleUtilizationMetric(BaseValidatorModel):
    name: Optional[IdleMetricNameType] = None
    statistic: Optional[MetricStatisticType] = None
    value: Optional[float] = None


class IdleSummary(BaseValidatorModel):
    name: Optional[IdleFindingType] = None
    value: Optional[float] = None


class InstanceEstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class RecommendationSource(BaseValidatorModel):
    recommendationSourceArn: Optional[str] = None
    recommendationSourceType: Optional[RecommendationSourceTypeType] = None


class LambdaSavingsEstimationMode(BaseValidatorModel):
    source: Optional[LambdaSavingsEstimationModeSourceType] = None


class LambdaEstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class LambdaFunctionMemoryProjectedMetric(BaseValidatorModel):
    name: Optional[Literal['Duration']] = None
    statistic: Optional[LambdaFunctionMemoryMetricStatisticType] = None
    value: Optional[float] = None


class LambdaFunctionUtilizationMetric(BaseValidatorModel):
    name: Optional[LambdaFunctionMetricNameType] = None
    statistic: Optional[LambdaFunctionMetricStatisticType] = None
    value: Optional[float] = None


class MetricSource(BaseValidatorModel):
    provider: Optional[Literal['CloudWatchApplicationInsights']] = None
    providerArn: Optional[str] = None


class PreferredResource(BaseValidatorModel):
    name: Optional[Literal['Ec2InstanceTypes']] = None
    includeList: Optional[List[str]] = None
    excludeList: Optional[List[str]] = None


class ProjectedMetric(BaseValidatorModel):
    name: Optional[MetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    values: Optional[List[float]] = None


class RDSDBUtilizationMetric(BaseValidatorModel):
    name: Optional[RDSDBMetricNameType] = None
    statistic: Optional[RDSDBMetricStatisticType] = None
    value: Optional[float] = None


class RDSDatabaseProjectedMetric(BaseValidatorModel):
    name: Optional[RDSDBMetricNameType] = None
    timestamps: Optional[List[datetime]] = None
    values: Optional[List[float]] = None


class RDSSavingsEstimationMode(BaseValidatorModel):
    source: Optional[RDSSavingsEstimationModeSourceType] = None


class RDSInstanceEstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class RDSStorageEstimatedMonthlySavings(BaseValidatorModel):
    currency: Optional[CurrencyType] = None
    value: Optional[float] = None


class ReasonCodeSummary(BaseValidatorModel):
    name: Optional[FindingReasonCodeType] = None
    value: Optional[float] = None


# This class is the input for the 'update_enrollment_status' function.
class UpdateEnrollmentStatusRequest(BaseValidatorModel):
    status: StatusType
    includeMemberAccounts: Optional[bool] = None


class VolumeConfiguration(BaseValidatorModel):
    volumeType: Optional[str] = None
    volumeSize: Optional[int] = None
    volumeBaselineIOPS: Optional[int] = None
    volumeBurstIOPS: Optional[int] = None
    volumeBaselineThroughput: Optional[int] = None
    volumeBurstThroughput: Optional[int] = None
    rootVolume: Optional[bool] = None


class AutoScalingGroupSavingsOpportunityAfterDiscounts(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[AutoScalingGroupEstimatedMonthlySavings] = None


class ContainerConfiguration(BaseValidatorModel):
    containerName: Optional[str] = None
    memorySizeConfiguration: Optional[MemorySizeConfiguration] = None
    cpu: Optional[int] = None


class ContainerRecommendation(BaseValidatorModel):
    containerName: Optional[str] = None
    memorySizeConfiguration: Optional[MemorySizeConfiguration] = None
    cpu: Optional[int] = None


class UtilizationPreference(BaseValidatorModel):
    metricName: Optional[CustomizableMetricNameType] = None
    metricParameters: Optional[CustomizableMetricParameters] = None


class DeleteRecommendationPreferencesRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    recommendationPreferenceNames: List[RecommendationPreferenceNameType]
    scope: Optional[Scope] = None


# This class is the input for the 'get_recommendation_preferences' function.
class GetRecommendationPreferencesRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    scope: Optional[Scope] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'describe_recommendation_export_jobs' function.
class DescribeRecommendationExportJobsRequest(BaseValidatorModel):
    jobIds: Optional[List[str]] = None
    filters: Optional[List[JobFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeRecommendationExportJobsRequestPaginate(BaseValidatorModel):
    jobIds: Optional[List[str]] = None
    filters: Optional[List[JobFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRecommendationPreferencesRequestPaginate(BaseValidatorModel):
    resourceType: ResourceTypeType
    scope: Optional[Scope] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRecommendationSummariesRequestPaginate(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetEnrollmentStatusResponse(BaseValidatorModel):
    status: StatusType
    statusReason: str
    memberAccountsEnrolled: bool
    lastUpdatedTimestamp: datetime
    numberOfMemberAccountsOptedIn: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_enrollment_statuses_for_organization' function.
class GetEnrollmentStatusesForOrganizationResponse(BaseValidatorModel):
    accountEnrollmentStatuses: List[AccountEnrollmentStatus]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_enrollment_status' function.
class UpdateEnrollmentStatusResponse(BaseValidatorModel):
    status: StatusType
    statusReason: str
    ResponseMetadata: ResponseMetadata


class EBSEffectiveRecommendationPreferences(BaseValidatorModel):
    savingsEstimationMode: Optional[EBSSavingsEstimationMode] = None


class EBSSavingsOpportunityAfterDiscounts(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[EBSEstimatedMonthlySavings] = None


# This class is the input for the 'get_ebs_volume_recommendations' function.
class GetEBSVolumeRecommendationsRequest(BaseValidatorModel):
    volumeArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[EBSFilter]] = None
    accountIds: Optional[List[str]] = None


class ECSEffectiveRecommendationPreferences(BaseValidatorModel):
    savingsEstimationMode: Optional[ECSSavingsEstimationMode] = None


class ECSSavingsOpportunityAfterDiscounts(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[ECSEstimatedMonthlySavings] = None


class ECSServiceRecommendedOptionProjectedMetric(BaseValidatorModel):
    recommendedCpuUnits: Optional[int] = None
    recommendedMemorySize: Optional[int] = None
    projectedMetrics: Optional[List[ECSServiceProjectedMetric]] = None


# This class is the input for the 'get_ecs_service_recommendations' function.
class GetECSServiceRecommendationsRequest(BaseValidatorModel):
    serviceArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[ECSServiceRecommendationFilter]] = None
    accountIds: Optional[List[str]] = None


class GetEnrollmentStatusesForOrganizationRequestPaginate(BaseValidatorModel):
    filters: Optional[List[EnrollmentFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_enrollment_statuses_for_organization' function.
class GetEnrollmentStatusesForOrganizationRequest(BaseValidatorModel):
    filters: Optional[List[EnrollmentFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class InferredWorkloadSaving(BaseValidatorModel):
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None
    estimatedMonthlySavings: Optional[EstimatedMonthlySavings] = None


class SavingsOpportunity(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[EstimatedMonthlySavings] = None


# This class is the input for the 'get_auto_scaling_group_recommendations' function.
class GetAutoScalingGroupRecommendationsRequest(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    autoScalingGroupArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None
    recommendationPreferences: Optional[RecommendationPreferences] = None


# This class is the input for the 'get_ec2_instance_recommendations' function.
class GetEC2InstanceRecommendationsRequest(BaseValidatorModel):
    instanceArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None
    accountIds: Optional[List[str]] = None
    recommendationPreferences: Optional[RecommendationPreferences] = None


# This class is the input for the 'export_auto_scaling_group_recommendations' function.
class ExportAutoScalingGroupRecommendationsRequest(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfig
    accountIds: Optional[List[str]] = None
    filters: Optional[List[Filter]] = None
    fieldsToExport: Optional[List[ExportableAutoScalingGroupFieldType]] = None
    fileFormat: Optional[Literal['Csv']] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferences] = None


# This class is the input for the 'export_ebs_volume_recommendations' function.
class ExportEBSVolumeRecommendationsRequest(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfig
    accountIds: Optional[List[str]] = None
    filters: Optional[List[EBSFilter]] = None
    fieldsToExport: Optional[List[ExportableVolumeFieldType]] = None
    fileFormat: Optional[Literal['Csv']] = None
    includeMemberAccounts: Optional[bool] = None


# This class is the input for the 'export_ec2_instance_recommendations' function.
class ExportEC2InstanceRecommendationsRequest(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfig
    accountIds: Optional[List[str]] = None
    filters: Optional[List[Filter]] = None
    fieldsToExport: Optional[List[ExportableInstanceFieldType]] = None
    fileFormat: Optional[Literal['Csv']] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferences] = None


# This class is the input for the 'export_ecs_service_recommendations' function.
class ExportECSServiceRecommendationsRequest(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfig
    accountIds: Optional[List[str]] = None
    filters: Optional[List[ECSServiceRecommendationFilter]] = None
    fieldsToExport: Optional[List[ExportableECSServiceFieldType]] = None
    fileFormat: Optional[Literal['Csv']] = None
    includeMemberAccounts: Optional[bool] = None


# This class is the output for the 'export_auto_scaling_group_recommendations' function.
class ExportAutoScalingGroupRecommendationsResponse(BaseValidatorModel):
    jobId: str
    s3Destination: S3Destination
    ResponseMetadata: ResponseMetadata


class ExportDestination(BaseValidatorModel):
    s3: Optional[S3Destination] = None


# This class is the output for the 'export_ebs_volume_recommendations' function.
class ExportEBSVolumeRecommendationsResponse(BaseValidatorModel):
    jobId: str
    s3Destination: S3Destination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_ec2_instance_recommendations' function.
class ExportEC2InstanceRecommendationsResponse(BaseValidatorModel):
    jobId: str
    s3Destination: S3Destination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_ecs_service_recommendations' function.
class ExportECSServiceRecommendationsResponse(BaseValidatorModel):
    jobId: str
    s3Destination: S3Destination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_idle_recommendations' function.
class ExportIdleRecommendationsResponse(BaseValidatorModel):
    jobId: str
    s3Destination: S3Destination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_lambda_function_recommendations' function.
class ExportLambdaFunctionRecommendationsResponse(BaseValidatorModel):
    jobId: str
    s3Destination: S3Destination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_license_recommendations' function.
class ExportLicenseRecommendationsResponse(BaseValidatorModel):
    jobId: str
    s3Destination: S3Destination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_rds_database_recommendations' function.
class ExportRDSDatabaseRecommendationsResponse(BaseValidatorModel):
    jobId: str
    s3Destination: S3Destination
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'export_idle_recommendations' function.
class ExportIdleRecommendationsRequest(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfig
    accountIds: Optional[List[str]] = None
    filters: Optional[List[IdleRecommendationFilter]] = None
    fieldsToExport: Optional[List[ExportableIdleFieldType]] = None
    fileFormat: Optional[Literal['Csv']] = None
    includeMemberAccounts: Optional[bool] = None


# This class is the input for the 'export_lambda_function_recommendations' function.
class ExportLambdaFunctionRecommendationsRequest(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfig
    accountIds: Optional[List[str]] = None
    filters: Optional[List[LambdaFunctionRecommendationFilter]] = None
    fieldsToExport: Optional[List[ExportableLambdaFunctionFieldType]] = None
    fileFormat: Optional[Literal['Csv']] = None
    includeMemberAccounts: Optional[bool] = None


class GetLambdaFunctionRecommendationsRequestPaginate(BaseValidatorModel):
    functionArns: Optional[List[str]] = None
    accountIds: Optional[List[str]] = None
    filters: Optional[List[LambdaFunctionRecommendationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_lambda_function_recommendations' function.
class GetLambdaFunctionRecommendationsRequest(BaseValidatorModel):
    functionArns: Optional[List[str]] = None
    accountIds: Optional[List[str]] = None
    filters: Optional[List[LambdaFunctionRecommendationFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'export_license_recommendations' function.
class ExportLicenseRecommendationsRequest(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfig
    accountIds: Optional[List[str]] = None
    filters: Optional[List[LicenseRecommendationFilter]] = None
    fieldsToExport: Optional[List[ExportableLicenseFieldType]] = None
    fileFormat: Optional[Literal['Csv']] = None
    includeMemberAccounts: Optional[bool] = None


# This class is the input for the 'get_license_recommendations' function.
class GetLicenseRecommendationsRequest(BaseValidatorModel):
    resourceArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[LicenseRecommendationFilter]] = None
    accountIds: Optional[List[str]] = None


# This class is the input for the 'export_rds_database_recommendations' function.
class ExportRDSDatabaseRecommendationsRequest(BaseValidatorModel):
    s3DestinationConfig: S3DestinationConfig
    accountIds: Optional[List[str]] = None
    filters: Optional[List[RDSDBRecommendationFilter]] = None
    fieldsToExport: Optional[List[ExportableRDSDBFieldType]] = None
    fileFormat: Optional[Literal['Csv']] = None
    includeMemberAccounts: Optional[bool] = None
    recommendationPreferences: Optional[RecommendationPreferences] = None


# This class is the input for the 'get_rds_database_recommendations' function.
class GetRDSDatabaseRecommendationsRequest(BaseValidatorModel):
    resourceArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[RDSDBRecommendationFilter]] = None
    accountIds: Optional[List[str]] = None
    recommendationPreferences: Optional[RecommendationPreferences] = None


# This class is the input for the 'get_ec2_recommendation_projected_metrics' function.
class GetEC2RecommendationProjectedMetricsRequest(BaseValidatorModel):
    instanceArn: str
    stat: MetricStatisticType
    period: int
    startTime: Timestamp
    endTime: Timestamp
    recommendationPreferences: Optional[RecommendationPreferences] = None


# This class is the input for the 'get_ecs_service_recommendation_projected_metrics' function.
class GetECSServiceRecommendationProjectedMetricsRequest(BaseValidatorModel):
    serviceArn: str
    stat: MetricStatisticType
    period: int
    startTime: Timestamp
    endTime: Timestamp


# This class is the input for the 'get_rds_database_recommendation_projected_metrics' function.
class GetRDSDatabaseRecommendationProjectedMetricsRequest(BaseValidatorModel):
    resourceArn: str
    stat: MetricStatisticType
    period: int
    startTime: Timestamp
    endTime: Timestamp
    recommendationPreferences: Optional[RecommendationPreferences] = None


# This class is the input for the 'get_idle_recommendations' function.
class GetIdleRecommendationsRequest(BaseValidatorModel):
    resourceArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[IdleRecommendationFilter]] = None
    accountIds: Optional[List[str]] = None
    orderBy: Optional[OrderBy] = None


class GpuInfo(BaseValidatorModel):
    gpus: Optional[List[Gpu]] = None


class IdleSavingsOpportunityAfterDiscounts(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[IdleEstimatedMonthlySavings] = None


class IdleSavingsOpportunity(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[IdleEstimatedMonthlySavings] = None


class InstanceSavingsOpportunityAfterDiscounts(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[InstanceEstimatedMonthlySavings] = None


class LambdaEffectiveRecommendationPreferences(BaseValidatorModel):
    savingsEstimationMode: Optional[LambdaSavingsEstimationMode] = None


class LambdaSavingsOpportunityAfterDiscounts(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[LambdaEstimatedMonthlySavings] = None


class LicenseConfiguration(BaseValidatorModel):
    numberOfCores: Optional[int] = None
    instanceType: Optional[str] = None
    operatingSystem: Optional[str] = None
    licenseEdition: Optional[LicenseEditionType] = None
    licenseName: Optional[Literal['SQLServer']] = None
    licenseModel: Optional[LicenseModelType] = None
    licenseVersion: Optional[str] = None
    metricsSource: Optional[List[MetricSource]] = None


class RecommendedOptionProjectedMetric(BaseValidatorModel):
    recommendedInstanceType: Optional[str] = None
    rank: Optional[int] = None
    projectedMetrics: Optional[List[ProjectedMetric]] = None


class RDSDatabaseRecommendedOptionProjectedMetric(BaseValidatorModel):
    recommendedDBInstanceClass: Optional[str] = None
    rank: Optional[int] = None
    projectedMetrics: Optional[List[RDSDatabaseProjectedMetric]] = None


class RDSEffectiveRecommendationPreferences(BaseValidatorModel):
    cpuVendorArchitectures: Optional[List[CpuVendorArchitectureType]] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    savingsEstimationMode: Optional[RDSSavingsEstimationMode] = None


class RDSInstanceSavingsOpportunityAfterDiscounts(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[RDSInstanceEstimatedMonthlySavings] = None


class RDSStorageSavingsOpportunityAfterDiscounts(BaseValidatorModel):
    savingsOpportunityPercentage: Optional[float] = None
    estimatedMonthlySavings: Optional[RDSStorageEstimatedMonthlySavings] = None


class Summary(BaseValidatorModel):
    name: Optional[FindingType] = None
    value: Optional[float] = None
    reasonCodeSummaries: Optional[List[ReasonCodeSummary]] = None


class ServiceConfiguration(BaseValidatorModel):
    memory: Optional[int] = None
    cpu: Optional[int] = None
    containerConfigurations: Optional[List[ContainerConfiguration]] = None
    autoScalingConfiguration: Optional[AutoScalingConfigurationType] = None
    taskDefinitionArn: Optional[str] = None


class EffectiveRecommendationPreferences(BaseValidatorModel):
    cpuVendorArchitectures: Optional[List[CpuVendorArchitectureType]] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreference] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[List[UtilizationPreference]] = None
    preferredResources: Optional[List[EffectivePreferredResource]] = None
    savingsEstimationMode: Optional[InstanceSavingsEstimationMode] = None


# This class is the output for the 'get_effective_recommendation_preferences' function.
class GetEffectiveRecommendationPreferencesResponse(BaseValidatorModel):
    enhancedInfrastructureMetrics: EnhancedInfrastructureMetricsType
    externalMetricsPreference: ExternalMetricsPreference
    lookBackPeriod: LookBackPeriodPreferenceType
    utilizationPreferences: List[UtilizationPreference]
    preferredResources: List[EffectivePreferredResource]
    ResponseMetadata: ResponseMetadata


class PutRecommendationPreferencesRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    scope: Optional[Scope] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreference] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[List[UtilizationPreference]] = None
    preferredResources: Optional[List[PreferredResource]] = None
    savingsEstimationMode: Optional[SavingsEstimationModeType] = None


class RecommendationPreferencesDetail(BaseValidatorModel):
    scope: Optional[Scope] = None
    resourceType: Optional[ResourceTypeType] = None
    enhancedInfrastructureMetrics: Optional[EnhancedInfrastructureMetricsType] = None
    inferredWorkloadTypes: Optional[InferredWorkloadTypesPreferenceType] = None
    externalMetricsPreference: Optional[ExternalMetricsPreference] = None
    lookBackPeriod: Optional[LookBackPeriodPreferenceType] = None
    utilizationPreferences: Optional[List[UtilizationPreference]] = None
    preferredResources: Optional[List[EffectivePreferredResource]] = None
    savingsEstimationMode: Optional[SavingsEstimationModeType] = None


# This class is the output for the 'get_ecs_service_recommendation_projected_metrics' function.
class GetECSServiceRecommendationProjectedMetricsResponse(BaseValidatorModel):
    recommendedOptionProjectedMetrics: List[ECSServiceRecommendedOptionProjectedMetric]
    ResponseMetadata: ResponseMetadata


class ECSServiceRecommendationOption(BaseValidatorModel):
    memory: Optional[int] = None
    cpu: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None
    savingsOpportunityAfterDiscounts: Optional[ECSSavingsOpportunityAfterDiscounts] = None
    projectedUtilizationMetrics: Optional[List[ECSServiceProjectedUtilizationMetric]] = None
    containerRecommendations: Optional[List[ContainerRecommendation]] = None


class LicenseRecommendationOption(BaseValidatorModel):
    rank: Optional[int] = None
    operatingSystem: Optional[str] = None
    licenseEdition: Optional[LicenseEditionType] = None
    licenseModel: Optional[LicenseModelType] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None


class VolumeRecommendationOption(BaseValidatorModel):
    configuration: Optional[VolumeConfiguration] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None
    savingsOpportunityAfterDiscounts: Optional[EBSSavingsOpportunityAfterDiscounts] = None


class RecommendationExportJob(BaseValidatorModel):
    jobId: Optional[str] = None
    destination: Optional[ExportDestination] = None
    resourceType: Optional[ResourceTypeType] = None
    status: Optional[JobStatusType] = None
    creationTimestamp: Optional[datetime] = None
    lastUpdatedTimestamp: Optional[datetime] = None
    failureReason: Optional[str] = None


class AutoScalingGroupRecommendationOption(BaseValidatorModel):
    configuration: Optional[AutoScalingGroupConfiguration] = None
    instanceGpuInfo: Optional[GpuInfo] = None
    projectedUtilizationMetrics: Optional[List[UtilizationMetric]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None
    savingsOpportunityAfterDiscounts: Optional[AutoScalingGroupSavingsOpportunityAfterDiscounts] = None
    migrationEffort: Optional[MigrationEffortType] = None


class IdleRecommendation(BaseValidatorModel):
    resourceArn: Optional[str] = None
    resourceId: Optional[str] = None
    resourceType: Optional[IdleRecommendationResourceTypeType] = None
    accountId: Optional[str] = None
    finding: Optional[IdleFindingType] = None
    findingDescription: Optional[str] = None
    savingsOpportunity: Optional[IdleSavingsOpportunity] = None
    savingsOpportunityAfterDiscounts: Optional[IdleSavingsOpportunityAfterDiscounts] = None
    utilizationMetrics: Optional[List[IdleUtilizationMetric]] = None
    lookBackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    tags: Optional[List[Tag]] = None


class InstanceRecommendationOption(BaseValidatorModel):
    instanceType: Optional[str] = None
    instanceGpuInfo: Optional[GpuInfo] = None
    projectedUtilizationMetrics: Optional[List[UtilizationMetric]] = None
    platformDifferences: Optional[List[PlatformDifferenceType]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None
    savingsOpportunityAfterDiscounts: Optional[InstanceSavingsOpportunityAfterDiscounts] = None
    migrationEffort: Optional[MigrationEffortType] = None


class LambdaFunctionMemoryRecommendationOption(BaseValidatorModel):
    rank: Optional[int] = None
    memorySize: Optional[int] = None
    projectedUtilizationMetrics: Optional[List[LambdaFunctionMemoryProjectedMetric]] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None
    savingsOpportunityAfterDiscounts: Optional[LambdaSavingsOpportunityAfterDiscounts] = None


# This class is the output for the 'get_ec2_recommendation_projected_metrics' function.
class GetEC2RecommendationProjectedMetricsResponse(BaseValidatorModel):
    recommendedOptionProjectedMetrics: List[RecommendedOptionProjectedMetric]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rds_database_recommendation_projected_metrics' function.
class GetRDSDatabaseRecommendationProjectedMetricsResponse(BaseValidatorModel):
    recommendedOptionProjectedMetrics: List[RDSDatabaseRecommendedOptionProjectedMetric]
    ResponseMetadata: ResponseMetadata


class RDSDBInstanceRecommendationOption(BaseValidatorModel):
    dbInstanceClass: Optional[str] = None
    projectedUtilizationMetrics: Optional[List[RDSDBUtilizationMetric]] = None
    performanceRisk: Optional[float] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None
    savingsOpportunityAfterDiscounts: Optional[RDSInstanceSavingsOpportunityAfterDiscounts] = None


class RDSDBStorageRecommendationOption(BaseValidatorModel):
    storageConfiguration: Optional[DBStorageConfiguration] = None
    rank: Optional[int] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None
    savingsOpportunityAfterDiscounts: Optional[RDSStorageSavingsOpportunityAfterDiscounts] = None


class RecommendationSummary(BaseValidatorModel):
    summaries: Optional[List[Summary]] = None
    idleSummaries: Optional[List[IdleSummary]] = None
    recommendationResourceType: Optional[RecommendationSourceTypeType] = None
    accountId: Optional[str] = None
    savingsOpportunity: Optional[SavingsOpportunity] = None
    idleSavingsOpportunity: Optional[SavingsOpportunity] = None
    aggregatedSavingsOpportunity: Optional[SavingsOpportunity] = None
    currentPerformanceRiskRatings: Optional[CurrentPerformanceRiskRatings] = None
    inferredWorkloadSavings: Optional[List[InferredWorkloadSaving]] = None


# This class is the output for the 'get_recommendation_preferences' function.
class GetRecommendationPreferencesResponse(BaseValidatorModel):
    recommendationPreferencesDetails: List[RecommendationPreferencesDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ECSServiceRecommendation(BaseValidatorModel):
    serviceArn: Optional[str] = None
    accountId: Optional[str] = None
    currentServiceConfiguration: Optional[ServiceConfiguration] = None
    utilizationMetrics: Optional[List[ECSServiceUtilizationMetric]] = None
    lookbackPeriodInDays: Optional[float] = None
    launchType: Optional[ECSServiceLaunchTypeType] = None
    lastRefreshTimestamp: Optional[datetime] = None
    finding: Optional[ECSServiceRecommendationFindingType] = None
    findingReasonCodes: Optional[List[ECSServiceRecommendationFindingReasonCodeType]] = None
    serviceRecommendationOptions: Optional[List[ECSServiceRecommendationOption]] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[ECSEffectiveRecommendationPreferences] = None
    tags: Optional[List[Tag]] = None


class LicenseRecommendation(BaseValidatorModel):
    resourceArn: Optional[str] = None
    accountId: Optional[str] = None
    currentLicenseConfiguration: Optional[LicenseConfiguration] = None
    lookbackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    finding: Optional[LicenseFindingType] = None
    findingReasonCodes: Optional[List[LicenseFindingReasonCodeType]] = None
    licenseRecommendationOptions: Optional[List[LicenseRecommendationOption]] = None
    tags: Optional[List[Tag]] = None


class VolumeRecommendation(BaseValidatorModel):
    volumeArn: Optional[str] = None
    accountId: Optional[str] = None
    currentConfiguration: Optional[VolumeConfiguration] = None
    finding: Optional[EBSFindingType] = None
    utilizationMetrics: Optional[List[EBSUtilizationMetric]] = None
    lookBackPeriodInDays: Optional[float] = None
    volumeRecommendationOptions: Optional[List[VolumeRecommendationOption]] = None
    lastRefreshTimestamp: Optional[datetime] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[EBSEffectiveRecommendationPreferences] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_recommendation_export_jobs' function.
class DescribeRecommendationExportJobsResponse(BaseValidatorModel):
    recommendationExportJobs: List[RecommendationExportJob]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AutoScalingGroupRecommendation(BaseValidatorModel):
    accountId: Optional[str] = None
    autoScalingGroupArn: Optional[str] = None
    autoScalingGroupName: Optional[str] = None
    finding: Optional[FindingType] = None
    utilizationMetrics: Optional[List[UtilizationMetric]] = None
    lookBackPeriodInDays: Optional[float] = None
    currentConfiguration: Optional[AutoScalingGroupConfiguration] = None
    currentInstanceGpuInfo: Optional[GpuInfo] = None
    recommendationOptions: Optional[List[AutoScalingGroupRecommendationOption]] = None
    lastRefreshTimestamp: Optional[datetime] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[EffectiveRecommendationPreferences] = None
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None


# This class is the output for the 'get_idle_recommendations' function.
class GetIdleRecommendationsResponse(BaseValidatorModel):
    idleRecommendations: List[IdleRecommendation]
    errors: List[IdleRecommendationError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class InstanceRecommendation(BaseValidatorModel):
    instanceArn: Optional[str] = None
    accountId: Optional[str] = None
    instanceName: Optional[str] = None
    currentInstanceType: Optional[str] = None
    finding: Optional[FindingType] = None
    findingReasonCodes: Optional[List[InstanceRecommendationFindingReasonCodeType]] = None
    utilizationMetrics: Optional[List[UtilizationMetric]] = None
    lookBackPeriodInDays: Optional[float] = None
    recommendationOptions: Optional[List[InstanceRecommendationOption]] = None
    recommendationSources: Optional[List[RecommendationSource]] = None
    lastRefreshTimestamp: Optional[datetime] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[EffectiveRecommendationPreferences] = None
    inferredWorkloadTypes: Optional[List[InferredWorkloadTypeType]] = None
    instanceState: Optional[InstanceStateType] = None
    tags: Optional[List[Tag]] = None
    externalMetricStatus: Optional[ExternalMetricStatus] = None
    currentInstanceGpuInfo: Optional[GpuInfo] = None
    idle: Optional[InstanceIdleType] = None


class LambdaFunctionRecommendation(BaseValidatorModel):
    functionArn: Optional[str] = None
    functionVersion: Optional[str] = None
    accountId: Optional[str] = None
    currentMemorySize: Optional[int] = None
    numberOfInvocations: Optional[int] = None
    utilizationMetrics: Optional[List[LambdaFunctionUtilizationMetric]] = None
    lookbackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    finding: Optional[LambdaFunctionRecommendationFindingType] = None
    findingReasonCodes: Optional[List[LambdaFunctionRecommendationFindingReasonCodeType]] = None
    memorySizeRecommendationOptions: Optional[List[LambdaFunctionMemoryRecommendationOption]] = None
    currentPerformanceRisk: Optional[CurrentPerformanceRiskType] = None
    effectiveRecommendationPreferences: Optional[LambdaEffectiveRecommendationPreferences] = None
    tags: Optional[List[Tag]] = None


class RDSDBRecommendation(BaseValidatorModel):
    resourceArn: Optional[str] = None
    accountId: Optional[str] = None
    engine: Optional[str] = None
    engineVersion: Optional[str] = None
    promotionTier: Optional[int] = None
    currentDBInstanceClass: Optional[str] = None
    currentStorageConfiguration: Optional[DBStorageConfiguration] = None
    dbClusterIdentifier: Optional[str] = None
    idle: Optional[IdleType] = None
    instanceFinding: Optional[RDSInstanceFindingType] = None
    storageFinding: Optional[RDSStorageFindingType] = None
    instanceFindingReasonCodes: Optional[List[RDSInstanceFindingReasonCodeType]] = None
    currentInstancePerformanceRisk: Optional[RDSCurrentInstancePerformanceRiskType] = None
    storageFindingReasonCodes: Optional[List[RDSStorageFindingReasonCodeType]] = None
    instanceRecommendationOptions: Optional[List[RDSDBInstanceRecommendationOption]] = None
    storageRecommendationOptions: Optional[List[RDSDBStorageRecommendationOption]] = None
    utilizationMetrics: Optional[List[RDSDBUtilizationMetric]] = None
    effectiveRecommendationPreferences: Optional[RDSEffectiveRecommendationPreferences] = None
    lookbackPeriodInDays: Optional[float] = None
    lastRefreshTimestamp: Optional[datetime] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'get_recommendation_summaries' function.
class GetRecommendationSummariesResponse(BaseValidatorModel):
    recommendationSummaries: List[RecommendationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_ecs_service_recommendations' function.
class GetECSServiceRecommendationsResponse(BaseValidatorModel):
    ecsServiceRecommendations: List[ECSServiceRecommendation]
    errors: List[GetRecommendationError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_license_recommendations' function.
class GetLicenseRecommendationsResponse(BaseValidatorModel):
    licenseRecommendations: List[LicenseRecommendation]
    errors: List[GetRecommendationError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_ebs_volume_recommendations' function.
class GetEBSVolumeRecommendationsResponse(BaseValidatorModel):
    volumeRecommendations: List[VolumeRecommendation]
    errors: List[GetRecommendationError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_auto_scaling_group_recommendations' function.
class GetAutoScalingGroupRecommendationsResponse(BaseValidatorModel):
    autoScalingGroupRecommendations: List[AutoScalingGroupRecommendation]
    errors: List[GetRecommendationError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_ec2_instance_recommendations' function.
class GetEC2InstanceRecommendationsResponse(BaseValidatorModel):
    instanceRecommendations: List[InstanceRecommendation]
    errors: List[GetRecommendationError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_lambda_function_recommendations' function.
class GetLambdaFunctionRecommendationsResponse(BaseValidatorModel):
    lambdaFunctionRecommendations: List[LambdaFunctionRecommendation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_rds_database_recommendations' function.
class GetRDSDatabaseRecommendationsResponse(BaseValidatorModel):
    rdsDBRecommendations: List[RDSDBRecommendation]
    errors: List[GetRecommendationError]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None
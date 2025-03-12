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
from aws_resource_validator.pydantic_models.resiliencehub_constants import *

class AcceptGroupingRecommendationEntryTypeDef(BaseValidatorModel):
    groupingRecommendationId: str


class FailedGroupingRecommendationEntryTypeDef(BaseValidatorModel):
    errorMessage: str
    groupingRecommendationId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AlarmTypeDef(BaseValidatorModel):
    alarmArn: Optional[str] = None
    source: Optional[str] = None


class CostTypeDef(BaseValidatorModel):
    amount: float
    currency: str
    frequency: CostFrequencyType


class DisruptionComplianceTypeDef(BaseValidatorModel):
    complianceStatus: ComplianceStatusType
    achievableRpoInSecs: Optional[int] = None
    achievableRtoInSecs: Optional[int] = None
    currentRpoInSecs: Optional[int] = None
    currentRtoInSecs: Optional[int] = None
    message: Optional[str] = None
    rpoDescription: Optional[str] = None
    rpoReferenceId: Optional[str] = None
    rtoDescription: Optional[str] = None
    rtoReferenceId: Optional[str] = None


class EksSourceClusterNamespaceTypeDef(BaseValidatorModel):
    eksClusterArn: str
    namespace: str


class TerraformSourceTypeDef(BaseValidatorModel):
    s3StateFileUrl: str


class AppSummaryTypeDef(BaseValidatorModel):
    appArn: str
    creationTime: datetime
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    awsApplicationArn: Optional[str] = None
    complianceStatus: Optional[AppComplianceStatusTypeType] = None
    description: Optional[str] = None
    driftStatus: Optional[AppDriftStatusTypeType] = None
    lastAppComplianceEvaluationTime: Optional[datetime] = None
    resiliencyScore: Optional[float] = None
    rpoInSecs: Optional[int] = None
    rtoInSecs: Optional[int] = None
    status: Optional[AppStatusTypeType] = None


class EventSubscriptionTypeDef(BaseValidatorModel):
    eventType: EventTypeType
    name: str
    snsTopicArn: Optional[str] = None


class AppVersionSummaryTypeDef(BaseValidatorModel):
    appVersion: str
    creationTime: Optional[datetime] = None
    identifier: Optional[int] = None
    versionName: Optional[str] = None


class AssessmentRiskRecommendationTypeDef(BaseValidatorModel):
    appComponents: Optional[List[str]] = None
    recommendation: Optional[str] = None
    risk: Optional[str] = None


class BatchUpdateRecommendationStatusFailedEntryTypeDef(BaseValidatorModel):
    entryId: str
    errorMessage: str


class UpdateRecommendationStatusItemTypeDef(BaseValidatorModel):
    resourceId: Optional[str] = None
    targetAccountId: Optional[str] = None
    targetRegion: Optional[str] = None


class RecommendationDisruptionComplianceTypeDef(BaseValidatorModel):
    expectedComplianceStatus: ComplianceStatusType
    expectedRpoDescription: Optional[str] = None
    expectedRpoInSecs: Optional[int] = None
    expectedRtoDescription: Optional[str] = None
    expectedRtoInSecs: Optional[int] = None


class LogicalResourceIdTypeDef(BaseValidatorModel):
    identifier: str
    eksSourceName: Optional[str] = None
    logicalStackName: Optional[str] = None
    resourceGroupName: Optional[str] = None
    terraformSourceName: Optional[str] = None


class FailurePolicyTypeDef(BaseValidatorModel):
    rpoInSecs: int
    rtoInSecs: int


class DeleteAppAssessmentRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    clientToken: Optional[str] = None


class DeleteAppRequestTypeDef(BaseValidatorModel):
    appArn: str
    clientToken: Optional[str] = None
    forceDelete: Optional[bool] = None


class DeleteRecommendationTemplateRequestTypeDef(BaseValidatorModel):
    recommendationTemplateArn: str
    clientToken: Optional[str] = None


class DeleteResiliencyPolicyRequestTypeDef(BaseValidatorModel):
    policyArn: str
    clientToken: Optional[str] = None


class DescribeAppAssessmentRequestTypeDef(BaseValidatorModel):
    assessmentArn: str


class DescribeAppRequestTypeDef(BaseValidatorModel):
    appArn: str


class DescribeAppVersionRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str


class DescribeAppVersionResourcesResolutionStatusRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    resolutionId: Optional[str] = None


class DescribeAppVersionTemplateRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str


class DescribeDraftAppVersionResourcesImportStatusRequestTypeDef(BaseValidatorModel):
    appArn: str


class ErrorDetailTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None


class DescribeMetricsExportRequestTypeDef(BaseValidatorModel):
    metricsExportId: str


class S3LocationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None


class DescribeResiliencyPolicyRequestTypeDef(BaseValidatorModel):
    policyArn: str


class DescribeResourceGroupingRecommendationTaskRequestTypeDef(BaseValidatorModel):
    appArn: str
    groupingId: Optional[str] = None


class EksSourceOutputTypeDef(BaseValidatorModel):
    eksClusterArn: str
    namespaces: List[str]


class EksSourceTypeDef(BaseValidatorModel):
    eksClusterArn: str
    namespaces: Sequence[str]


class ExperimentTypeDef(BaseValidatorModel):
    experimentArn: Optional[str] = None
    experimentTemplateId: Optional[str] = None


class FieldTypeDef(BaseValidatorModel):
    name: str
    aggregation: Optional[FieldAggregationTypeType] = None


class GroupingAppComponentTypeDef(BaseValidatorModel):
    appComponentId: str
    appComponentName: str
    appComponentType: str


class ListAlarmRecommendationsRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppAssessmentComplianceDriftsRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAppAssessmentResourceDriftsRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppAssessmentsRequestTypeDef(BaseValidatorModel):
    appArn: Optional[str] = None
    assessmentName: Optional[str] = None
    assessmentStatus: Optional[Sequence[AssessmentStatusType]] = None
    complianceStatus: Optional[ComplianceStatusType] = None
    invoker: Optional[AssessmentInvokerType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    reverseOrder: Optional[bool] = None


class ListAppComponentCompliancesRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppComponentRecommendationsRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppInputSourcesRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppVersionAppComponentsRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppVersionResourceMappingsRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppVersionResourcesRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resolutionId: Optional[str] = None


class SortTypeDef(BaseValidatorModel):
    field: str
    ascending: Optional[bool] = None


class ListRecommendationTemplatesRequestTypeDef(BaseValidatorModel):
    assessmentArn: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    recommendationTemplateArn: Optional[str] = None
    reverseOrder: Optional[bool] = None
    status: Optional[Sequence[RecommendationTemplateStatusType]] = None


class ListResiliencyPoliciesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    policyName: Optional[str] = None


class ListResourceGroupingRecommendationsRequestTypeDef(BaseValidatorModel):
    appArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSopRecommendationsRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSuggestedResiliencyPoliciesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTestRecommendationsRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListUnsupportedAppVersionResourcesRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resolutionId: Optional[str] = None


class PublishAppVersionRequestTypeDef(BaseValidatorModel):
    appArn: str
    versionName: Optional[str] = None


class PutDraftAppVersionTemplateRequestTypeDef(BaseValidatorModel):
    appArn: str
    appTemplateBody: str


class RejectGroupingRecommendationEntryTypeDef(BaseValidatorModel):
    groupingRecommendationId: str
    rejectionReason: Optional[GroupingRecommendationRejectionReasonType] = None


class RemoveDraftAppVersionResourceMappingsRequestTypeDef(BaseValidatorModel):
    appArn: str
    appRegistryAppNames: Optional[Sequence[str]] = None
    eksSourceNames: Optional[Sequence[str]] = None
    logicalStackNames: Optional[Sequence[str]] = None
    resourceGroupNames: Optional[Sequence[str]] = None
    resourceNames: Optional[Sequence[str]] = None
    terraformSourceNames: Optional[Sequence[str]] = None


class ScoringComponentResiliencyScoreTypeDef(BaseValidatorModel):
    excludedCount: Optional[int] = None
    outstandingCount: Optional[int] = None
    possibleScore: Optional[float] = None
    score: Optional[float] = None


class ResolveAppVersionResourcesRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str


class ResourceErrorTypeDef(BaseValidatorModel):
    logicalResourceId: Optional[str] = None
    physicalResourceId: Optional[str] = None
    reason: Optional[str] = None


class StartAppAssessmentRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    assessmentName: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class StartMetricsExportRequestTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    clientToken: Optional[str] = None


class StartResourceGroupingRecommendationTaskRequestTypeDef(BaseValidatorModel):
    appArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAppVersionRequestTypeDef(BaseValidatorModel):
    appArn: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None


class AcceptResourceGroupingRecommendationsRequestTypeDef(BaseValidatorModel):
    appArn: str
    entries: Sequence[AcceptGroupingRecommendationEntryTypeDef]


class AcceptResourceGroupingRecommendationsResponseTypeDef(BaseValidatorModel):
    appArn: str
    failedEntries: List[FailedGroupingRecommendationEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAppAssessmentResponseTypeDef(BaseValidatorModel):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAppResponseTypeDef(BaseValidatorModel):
    appArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRecommendationTemplateResponseTypeDef(BaseValidatorModel):
    recommendationTemplateArn: str
    status: RecommendationTemplateStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResiliencyPolicyResponseTypeDef(BaseValidatorModel):
    policyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAppVersionResourcesResolutionStatusResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    errorMessage: str
    resolutionId: str
    status: ResourceResolutionStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAppVersionResponseTypeDef(BaseValidatorModel):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAppVersionTemplateResponseTypeDef(BaseValidatorModel):
    appArn: str
    appTemplateBody: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeResourceGroupingRecommendationTaskResponseTypeDef(BaseValidatorModel):
    errorMessage: str
    groupingId: str
    status: ResourcesGroupingRecGenStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class ListMetricsResponseTypeDef(BaseValidatorModel):
    rows: List[List[str]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PublishAppVersionResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    identifier: int
    versionName: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutDraftAppVersionTemplateResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class RejectResourceGroupingRecommendationsResponseTypeDef(BaseValidatorModel):
    appArn: str
    failedEntries: List[FailedGroupingRecommendationEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveDraftAppVersionResourceMappingsResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResolveAppVersionResourcesResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    resolutionId: str
    status: ResourceResolutionStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class StartMetricsExportResponseTypeDef(BaseValidatorModel):
    metricsExportId: str
    status: MetricsExportStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class StartResourceGroupingRecommendationTaskResponseTypeDef(BaseValidatorModel):
    appArn: str
    errorMessage: str
    groupingId: str
    status: ResourcesGroupingRecGenStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAppVersionResponseTypeDef(BaseValidatorModel):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class AppAssessmentSummaryTypeDef(BaseValidatorModel):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    appArn: Optional[str] = None
    appVersion: Optional[str] = None
    assessmentName: Optional[str] = None
    complianceStatus: Optional[ComplianceStatusType] = None
    cost: Optional[CostTypeDef] = None
    driftStatus: Optional[DriftStatusType] = None
    endTime: Optional[datetime] = None
    invoker: Optional[AssessmentInvokerType] = None
    message: Optional[str] = None
    resiliencyScore: Optional[float] = None
    startTime: Optional[datetime] = None
    versionName: Optional[str] = None


class ComplianceDriftTypeDef(BaseValidatorModel):
    actualReferenceId: Optional[str] = None
    actualValue: Optional[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]] = None
    appId: Optional[str] = None
    appVersion: Optional[str] = None
    diffType: Optional[DifferenceTypeType] = None
    driftType: Optional[DriftTypeType] = None
    entityId: Optional[str] = None
    entityType: Optional[str] = None
    expectedReferenceId: Optional[str] = None
    expectedValue: Optional[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]] = None


class AppComponentTypeDef(BaseValidatorModel):
    pass


class CreateAppVersionAppComponentResponseTypeDef(BaseValidatorModel):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAppVersionAppComponentResponseTypeDef(BaseValidatorModel):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAppVersionAppComponentResponseTypeDef(BaseValidatorModel):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppVersionAppComponentsResponseTypeDef(BaseValidatorModel):
    appArn: str
    appComponents: List[AppComponentTypeDef]
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateAppVersionAppComponentResponseTypeDef(BaseValidatorModel):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class AppInputSourceTypeDef(BaseValidatorModel):
    importType: ResourceMappingTypeType
    eksSourceClusterNamespace: Optional[EksSourceClusterNamespaceTypeDef] = None
    resourceCount: Optional[int] = None
    sourceArn: Optional[str] = None
    sourceName: Optional[str] = None
    terraformSource: Optional[TerraformSourceTypeDef] = None


class DeleteAppInputSourceRequestTypeDef(BaseValidatorModel):
    appArn: str
    clientToken: Optional[str] = None
    eksSourceClusterNamespace: Optional[EksSourceClusterNamespaceTypeDef] = None
    sourceArn: Optional[str] = None
    terraformSource: Optional[TerraformSourceTypeDef] = None


class ListAppsResponseTypeDef(BaseValidatorModel):
    appSummaries: List[AppSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PermissionModelOutputTypeDef(BaseValidatorModel):
    pass


class AppTypeDef(BaseValidatorModel):
    appArn: str
    creationTime: datetime
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    awsApplicationArn: Optional[str] = None
    complianceStatus: Optional[AppComplianceStatusTypeType] = None
    description: Optional[str] = None
    driftStatus: Optional[AppDriftStatusTypeType] = None
    eventSubscriptions: Optional[List[EventSubscriptionTypeDef]] = None
    lastAppComplianceEvaluationTime: Optional[datetime] = None
    lastDriftEvaluationTime: Optional[datetime] = None
    lastResiliencyScoreEvaluationTime: Optional[datetime] = None
    permissionModel: Optional[PermissionModelOutputTypeDef] = None
    policyArn: Optional[str] = None
    resiliencyScore: Optional[float] = None
    rpoInSecs: Optional[int] = None
    rtoInSecs: Optional[int] = None
    status: Optional[AppStatusTypeType] = None
    tags: Optional[Dict[str, str]] = None


class ListAppVersionsResponseTypeDef(BaseValidatorModel):
    appVersions: List[AppVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssessmentSummaryTypeDef(BaseValidatorModel):
    riskRecommendations: Optional[List[AssessmentRiskRecommendationTypeDef]] = None
    summary: Optional[str] = None


class BatchUpdateRecommendationStatusSuccessfulEntryTypeDef(BaseValidatorModel):
    entryId: str
    excluded: bool
    referenceId: str
    appComponentId: Optional[str] = None
    excludeReason: Optional[ExcludeRecommendationReasonType] = None
    item: Optional[UpdateRecommendationStatusItemTypeDef] = None


class UpdateRecommendationStatusRequestEntryTypeDef(BaseValidatorModel):
    entryId: str
    excluded: bool
    referenceId: str
    appComponentId: Optional[str] = None
    excludeReason: Optional[ExcludeRecommendationReasonType] = None
    item: Optional[UpdateRecommendationStatusItemTypeDef] = None


class ConfigRecommendationTypeDef(BaseValidatorModel):
    name: str
    optimizationType: ConfigRecommendationOptimizationTypeType
    referenceId: str
    appComponentName: Optional[str] = None
    compliance: Optional[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]] = None
    cost: Optional[CostTypeDef] = None
    description: Optional[str] = None
    haArchitecture: Optional[HaArchitectureType] = None
    recommendationCompliance: Optional[ Dict[DisruptionTypeType, RecommendationDisruptionComplianceTypeDef] ] = None
    suggestedChanges: Optional[List[str]] = None


class CreateAppVersionResourceRequestTypeDef(BaseValidatorModel):
    appArn: str
    appComponents: Sequence[str]
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: str
    resourceType: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    clientToken: Optional[str] = None
    resourceName: Optional[str] = None


class DeleteAppVersionResourceRequestTypeDef(BaseValidatorModel):
    appArn: str
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    clientToken: Optional[str] = None
    logicalResourceId: Optional[LogicalResourceIdTypeDef] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None


class DescribeAppVersionResourceRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    logicalResourceId: Optional[LogicalResourceIdTypeDef] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None


class ResourceIdentifierTypeDef(BaseValidatorModel):
    logicalResourceId: Optional[LogicalResourceIdTypeDef] = None
    resourceType: Optional[str] = None


class UpdateAppVersionResourceRequestTypeDef(BaseValidatorModel):
    appArn: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None
    appComponents: Optional[Sequence[str]] = None
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    excluded: Optional[bool] = None
    logicalResourceId: Optional[LogicalResourceIdTypeDef] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None
    resourceType: Optional[str] = None


class CreateResiliencyPolicyRequestTypeDef(BaseValidatorModel):
    policy: Mapping[DisruptionTypeType, FailurePolicyTypeDef]
    policyName: str
    tier: ResiliencyPolicyTierType
    clientToken: Optional[str] = None
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    policyDescription: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ResiliencyPolicyTypeDef(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    estimatedCostTier: Optional[EstimatedCostTierType] = None
    policy: Optional[Dict[DisruptionTypeType, FailurePolicyTypeDef]] = None
    policyArn: Optional[str] = None
    policyDescription: Optional[str] = None
    policyName: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tier: Optional[ResiliencyPolicyTierType] = None


class UpdateResiliencyPolicyRequestTypeDef(BaseValidatorModel):
    policyArn: str
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    policy: Optional[Mapping[DisruptionTypeType, FailurePolicyTypeDef]] = None
    policyDescription: Optional[str] = None
    policyName: Optional[str] = None
    tier: Optional[ResiliencyPolicyTierType] = None


class DescribeDraftAppVersionResourcesImportStatusResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    errorDetails: List[ErrorDetailTypeDef]
    errorMessage: str
    status: ResourceImportStatusTypeType
    statusChangeTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMetricsExportResponseTypeDef(BaseValidatorModel):
    errorMessage: str
    exportLocation: S3LocationTypeDef
    metricsExportId: str
    status: MetricsExportStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class ImportResourcesToDraftAppVersionResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    eksSources: List[EksSourceOutputTypeDef]
    sourceArns: List[str]
    status: ResourceImportStatusTypeType
    terraformSources: List[TerraformSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RecommendationItemTypeDef(BaseValidatorModel):
    alreadyImplemented: Optional[bool] = None
    discoveredAlarm: Optional[AlarmTypeDef] = None
    excludeReason: Optional[ExcludeRecommendationReasonType] = None
    excluded: Optional[bool] = None
    latestDiscoveredExperiment: Optional[ExperimentTypeDef] = None
    resourceId: Optional[str] = None
    targetAccountId: Optional[str] = None
    targetRegion: Optional[str] = None


class PhysicalResourceIdTypeDef(BaseValidatorModel):
    pass


class GroupingResourceTypeDef(BaseValidatorModel):
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: PhysicalResourceIdTypeDef
    resourceName: str
    resourceType: str
    sourceAppComponentIds: List[str]


class PhysicalResourceTypeDef(BaseValidatorModel):
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: PhysicalResourceIdTypeDef
    resourceType: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    appComponents: Optional[List[AppComponentTypeDef]] = None
    excluded: Optional[bool] = None
    parentResourceName: Optional[str] = None
    resourceName: Optional[str] = None
    sourceType: Optional[ResourceSourceTypeType] = None


class ResourceMappingTypeDef(BaseValidatorModel):
    mappingType: ResourceMappingTypeType
    physicalResourceId: PhysicalResourceIdTypeDef
    appRegistryAppName: Optional[str] = None
    eksSourceName: Optional[str] = None
    logicalStackName: Optional[str] = None
    resourceGroupName: Optional[str] = None
    resourceName: Optional[str] = None
    terraformSourceName: Optional[str] = None


class UnsupportedResourceTypeDef(BaseValidatorModel):
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: PhysicalResourceIdTypeDef
    resourceType: str
    unsupportedResourceStatus: Optional[str] = None


class ListAppAssessmentResourceDriftsRequestPaginateTypeDef(BaseValidatorModel):
    assessmentArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceGroupingRecommendationsRequestPaginateTypeDef(BaseValidatorModel):
    appArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListAppVersionsRequestTypeDef(BaseValidatorModel):
    appArn: str
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None


class ListAppsRequestTypeDef(BaseValidatorModel):
    appArn: Optional[str] = None
    awsApplicationArn: Optional[str] = None
    fromLastAssessmentTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    reverseOrder: Optional[bool] = None
    toLastAssessmentTime: Optional[TimestampTypeDef] = None


class ConditionTypeDef(BaseValidatorModel):
    pass


class ListMetricsRequestPaginateTypeDef(BaseValidatorModel):
    conditions: Optional[Sequence[ConditionTypeDef]] = None
    dataSource: Optional[str] = None
    fields: Optional[Sequence[FieldTypeDef]] = None
    sorts: Optional[Sequence[SortTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMetricsRequestTypeDef(BaseValidatorModel):
    conditions: Optional[Sequence[ConditionTypeDef]] = None
    dataSource: Optional[str] = None
    fields: Optional[Sequence[FieldTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sorts: Optional[Sequence[SortTypeDef]] = None


class RejectResourceGroupingRecommendationsRequestTypeDef(BaseValidatorModel):
    appArn: str
    entries: Sequence[RejectGroupingRecommendationEntryTypeDef]


class ResiliencyScoreTypeDef(BaseValidatorModel):
    disruptionScore: Dict[DisruptionTypeType, float]
    score: float
    componentScore: Optional[ Dict[ResiliencyScoreTypeType, ScoringComponentResiliencyScoreTypeDef] ] = None


class ResourceErrorsDetailsTypeDef(BaseValidatorModel):
    hasMoreErrors: Optional[bool] = None
    resourceErrors: Optional[List[ResourceErrorTypeDef]] = None


class ListAppAssessmentsResponseTypeDef(BaseValidatorModel):
    assessmentSummaries: List[AppAssessmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAppAssessmentComplianceDriftsResponseTypeDef(BaseValidatorModel):
    complianceDrifts: List[ComplianceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DeleteAppInputSourceResponseTypeDef(BaseValidatorModel):
    appArn: str
    appInputSource: AppInputSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppInputSourcesResponseTypeDef(BaseValidatorModel):
    appInputSources: List[AppInputSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateAppResponseTypeDef(BaseValidatorModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAppResponseTypeDef(BaseValidatorModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAppResponseTypeDef(BaseValidatorModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdateRecommendationStatusResponseTypeDef(BaseValidatorModel):
    appArn: str
    failedEntries: List[BatchUpdateRecommendationStatusFailedEntryTypeDef]
    successfulEntries: List[BatchUpdateRecommendationStatusSuccessfulEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdateRecommendationStatusRequestTypeDef(BaseValidatorModel):
    appArn: str
    requestEntries: Sequence[UpdateRecommendationStatusRequestEntryTypeDef]


class ComponentRecommendationTypeDef(BaseValidatorModel):
    appComponentName: str
    configRecommendations: List[ConfigRecommendationTypeDef]
    recommendationStatus: RecommendationComplianceStatusType


class ResourceDriftTypeDef(BaseValidatorModel):
    appArn: Optional[str] = None
    appVersion: Optional[str] = None
    diffType: Optional[DifferenceTypeType] = None
    referenceId: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None


class CreateResiliencyPolicyResponseTypeDef(BaseValidatorModel):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeResiliencyPolicyResponseTypeDef(BaseValidatorModel):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResiliencyPoliciesResponseTypeDef(BaseValidatorModel):
    resiliencyPolicies: List[ResiliencyPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSuggestedResiliencyPoliciesResponseTypeDef(BaseValidatorModel):
    resiliencyPolicies: List[ResiliencyPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateResiliencyPolicyResponseTypeDef(BaseValidatorModel):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RecommendationTemplateTypeDef(BaseValidatorModel):
    pass


class CreateRecommendationTemplateResponseTypeDef(BaseValidatorModel):
    recommendationTemplate: RecommendationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRecommendationTemplatesResponseTypeDef(BaseValidatorModel):
    recommendationTemplates: List[RecommendationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EksSourceUnionTypeDef(BaseValidatorModel):
    pass


class ImportResourcesToDraftAppVersionRequestTypeDef(BaseValidatorModel):
    appArn: str
    eksSources: Optional[Sequence[EksSourceUnionTypeDef]] = None
    importStrategy: Optional[ResourceImportStrategyTypeType] = None
    sourceArns: Optional[Sequence[str]] = None
    terraformSources: Optional[Sequence[TerraformSourceTypeDef]] = None


class SopRecommendationTypeDef(BaseValidatorModel):
    recommendationId: str
    referenceId: str
    serviceType: Literal["SSM"]
    appComponentName: Optional[str] = None
    description: Optional[str] = None
    items: Optional[List[RecommendationItemTypeDef]] = None
    name: Optional[str] = None
    prerequisite: Optional[str] = None
    recommendationStatus: Optional[RecommendationStatusType] = None


class GroupingRecommendationTypeDef(BaseValidatorModel):
    confidenceLevel: GroupingRecommendationConfidenceLevelType
    creationTime: datetime
    groupingAppComponent: GroupingAppComponentTypeDef
    groupingRecommendationId: str
    recommendationReasons: List[str]
    resources: List[GroupingResourceTypeDef]
    score: float
    status: GroupingRecommendationStatusTypeType
    rejectionReason: Optional[GroupingRecommendationRejectionReasonType] = None


class CreateAppVersionResourceResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAppVersionResourceResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAppVersionResourceResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppVersionResourcesResponseTypeDef(BaseValidatorModel):
    physicalResources: List[PhysicalResourceTypeDef]
    resolutionId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateAppVersionResourceResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AddDraftAppVersionResourceMappingsRequestTypeDef(BaseValidatorModel):
    appArn: str
    resourceMappings: Sequence[ResourceMappingTypeDef]


class AddDraftAppVersionResourceMappingsResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    resourceMappings: List[ResourceMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppVersionResourceMappingsResponseTypeDef(BaseValidatorModel):
    resourceMappings: List[ResourceMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListUnsupportedAppVersionResourcesResponseTypeDef(BaseValidatorModel):
    resolutionId: str
    unsupportedResources: List[UnsupportedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PermissionModelUnionTypeDef(BaseValidatorModel):
    pass


class CreateAppRequestTypeDef(BaseValidatorModel):
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    awsApplicationArn: Optional[str] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    eventSubscriptions: Optional[Sequence[EventSubscriptionTypeDef]] = None
    permissionModel: Optional[PermissionModelUnionTypeDef] = None
    policyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateAppRequestTypeDef(BaseValidatorModel):
    appArn: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    clearResiliencyPolicyArn: Optional[bool] = None
    description: Optional[str] = None
    eventSubscriptions: Optional[Sequence[EventSubscriptionTypeDef]] = None
    permissionModel: Optional[PermissionModelUnionTypeDef] = None
    policyArn: Optional[str] = None


class AppComponentComplianceTypeDef(BaseValidatorModel):
    appComponentName: Optional[str] = None
    compliance: Optional[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]] = None
    cost: Optional[CostTypeDef] = None
    message: Optional[str] = None
    resiliencyScore: Optional[ResiliencyScoreTypeDef] = None
    status: Optional[ComplianceStatusType] = None


class AppAssessmentTypeDef(BaseValidatorModel):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    invoker: AssessmentInvokerType
    appArn: Optional[str] = None
    appVersion: Optional[str] = None
    assessmentName: Optional[str] = None
    compliance: Optional[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]] = None
    complianceStatus: Optional[ComplianceStatusType] = None
    cost: Optional[CostTypeDef] = None
    driftStatus: Optional[DriftStatusType] = None
    endTime: Optional[datetime] = None
    message: Optional[str] = None
    policy: Optional[ResiliencyPolicyTypeDef] = None
    resiliencyScore: Optional[ResiliencyScoreTypeDef] = None
    resourceErrorsDetails: Optional[ResourceErrorsDetailsTypeDef] = None
    startTime: Optional[datetime] = None
    summary: Optional[AssessmentSummaryTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    versionName: Optional[str] = None


class ListAppComponentRecommendationsResponseTypeDef(BaseValidatorModel):
    componentRecommendations: List[ComponentRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAppAssessmentResourceDriftsResponseTypeDef(BaseValidatorModel):
    resourceDrifts: List[ResourceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AlarmRecommendationTypeDef(BaseValidatorModel):
    pass


class ListAlarmRecommendationsResponseTypeDef(BaseValidatorModel):
    alarmRecommendations: List[AlarmRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSopRecommendationsResponseTypeDef(BaseValidatorModel):
    sopRecommendations: List[SopRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TestRecommendationTypeDef(BaseValidatorModel):
    pass


class ListTestRecommendationsResponseTypeDef(BaseValidatorModel):
    testRecommendations: List[TestRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListResourceGroupingRecommendationsResponseTypeDef(BaseValidatorModel):
    groupingRecommendations: List[GroupingRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAppComponentCompliancesResponseTypeDef(BaseValidatorModel):
    componentCompliances: List[AppComponentComplianceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeAppAssessmentResponseTypeDef(BaseValidatorModel):
    assessment: AppAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartAppAssessmentResponseTypeDef(BaseValidatorModel):
    assessment: AppAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



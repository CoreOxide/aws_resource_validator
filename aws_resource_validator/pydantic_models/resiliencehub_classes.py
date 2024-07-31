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
from aws_resource_validator.pydantic_models.resiliencehub_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class RecommendationItemTypeDef(BaseModel):
    alreadyImplemented: Optional[bool] = None
    excludeReason: Optional[ExcludeRecommendationReasonType] = None
    excluded: Optional[bool] = None
    resourceId: Optional[str] = None
    targetAccountId: Optional[str] = None
    targetRegion: Optional[str] = None

class CostTypeDef(BaseModel):
    amount: float
    currency: str
    frequency: CostFrequencyType

class DisruptionComplianceTypeDef(BaseModel):
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

class AppComponentTypeDef(BaseModel):
    name: str
    type: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    id: Optional[str] = None

class EksSourceClusterNamespaceTypeDef(BaseModel):
    eksClusterArn: str
    namespace: str

class TerraformSourceTypeDef(BaseModel):
    s3StateFileUrl: str

class AppSummaryTypeDef(BaseModel):
    appArn: str
    creationTime: datetime
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    complianceStatus: Optional[AppComplianceStatusTypeType] = None
    description: Optional[str] = None
    driftStatus: Optional[AppDriftStatusTypeType] = None
    lastAppComplianceEvaluationTime: Optional[datetime] = None
    resiliencyScore: Optional[float] = None
    rpoInSecs: Optional[int] = None
    rtoInSecs: Optional[int] = None
    status: Optional[AppStatusTypeType] = None

class EventSubscriptionTypeDef(BaseModel):
    eventType: EventTypeType
    name: str
    snsTopicArn: Optional[str] = None

class PermissionModelOutputTypeDef(BaseModel):
    type: PermissionModelTypeType
    crossAccountRoleArns: Optional[List[str]] = None
    invokerRoleName: Optional[str] = None

class AppVersionSummaryTypeDef(BaseModel):
    appVersion: str
    creationTime: Optional[datetime] = None
    identifier: Optional[int] = None
    versionName: Optional[str] = None

class BatchUpdateRecommendationStatusFailedEntryTypeDef(BaseModel):
    entryId: str
    errorMessage: str

class UpdateRecommendationStatusItemTypeDef(BaseModel):
    resourceId: Optional[str] = None
    targetAccountId: Optional[str] = None
    targetRegion: Optional[str] = None

class RecommendationDisruptionComplianceTypeDef(BaseModel):
    expectedComplianceStatus: ComplianceStatusType
    expectedRpoDescription: Optional[str] = None
    expectedRpoInSecs: Optional[int] = None
    expectedRtoDescription: Optional[str] = None
    expectedRtoInSecs: Optional[int] = None

class PermissionModelTypeDef(BaseModel):
    type: PermissionModelTypeType
    crossAccountRoleArns: Optional[Sequence[str]] = None
    invokerRoleName: Optional[str] = None

class CreateAppVersionAppComponentRequestRequestTypeDef(BaseModel):
    appArn: str
    name: str
    type: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None
    clientToken: Optional[str] = None
    id: Optional[str] = None

class LogicalResourceIdTypeDef(BaseModel):
    identifier: str
    eksSourceName: Optional[str] = None
    logicalStackName: Optional[str] = None
    resourceGroupName: Optional[str] = None
    terraformSourceName: Optional[str] = None

class CreateRecommendationTemplateRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    name: str
    bucketName: Optional[str] = None
    clientToken: Optional[str] = None
    format: Optional[TemplateFormatType] = None
    recommendationIds: Optional[Sequence[str]] = None
    recommendationTypes: Optional[Sequence[RenderRecommendationTypeType]] = None
    tags: Optional[Mapping[str, str]] = None

class FailurePolicyTypeDef(BaseModel):
    rpoInSecs: int
    rtoInSecs: int

class DeleteAppAssessmentRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    clientToken: Optional[str] = None

class DeleteAppRequestRequestTypeDef(BaseModel):
    appArn: str
    clientToken: Optional[str] = None
    forceDelete: Optional[bool] = None

class DeleteAppVersionAppComponentRequestRequestTypeDef(BaseModel):
    appArn: str
    id: str
    clientToken: Optional[str] = None

class DeleteRecommendationTemplateRequestRequestTypeDef(BaseModel):
    recommendationTemplateArn: str
    clientToken: Optional[str] = None

class DeleteResiliencyPolicyRequestRequestTypeDef(BaseModel):
    policyArn: str
    clientToken: Optional[str] = None

class DescribeAppAssessmentRequestRequestTypeDef(BaseModel):
    assessmentArn: str

class DescribeAppRequestRequestTypeDef(BaseModel):
    appArn: str

class DescribeAppVersionAppComponentRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    id: str

class DescribeAppVersionRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str

class DescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    resolutionId: Optional[str] = None

class DescribeAppVersionTemplateRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str

class DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef(BaseModel):
    appArn: str

class DescribeResiliencyPolicyRequestRequestTypeDef(BaseModel):
    policyArn: str

class EksSourceOutputTypeDef(BaseModel):
    eksClusterArn: str
    namespaces: List[str]

class EksSourceTypeDef(BaseModel):
    eksClusterArn: str
    namespaces: Sequence[str]

class ListAlarmRecommendationsRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppAssessmentComplianceDriftsRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAppAssessmentResourceDriftsRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppAssessmentsRequestRequestTypeDef(BaseModel):
    appArn: Optional[str] = None
    assessmentName: Optional[str] = None
    assessmentStatus: Optional[Sequence[AssessmentStatusType]] = None
    complianceStatus: Optional[ComplianceStatusType] = None
    invoker: Optional[AssessmentInvokerType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    reverseOrder: Optional[bool] = None

class ListAppComponentCompliancesRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppComponentRecommendationsRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppInputSourcesRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppVersionAppComponentsRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppVersionResourceMappingsRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppVersionResourcesRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resolutionId: Optional[str] = None

class ListRecommendationTemplatesRequestRequestTypeDef(BaseModel):
    assessmentArn: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    recommendationTemplateArn: Optional[str] = None
    reverseOrder: Optional[bool] = None
    status: Optional[Sequence[RecommendationTemplateStatusType]] = None

class ListResiliencyPoliciesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    policyName: Optional[str] = None

class ListSopRecommendationsRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSuggestedResiliencyPoliciesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTestRecommendationsRequestRequestTypeDef(BaseModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListUnsupportedAppVersionResourcesRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resolutionId: Optional[str] = None

class PhysicalResourceIdTypeDef(BaseModel):
    identifier: str
    type: PhysicalIdentifierTypeType
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None

class PublishAppVersionRequestRequestTypeDef(BaseModel):
    appArn: str
    versionName: Optional[str] = None

class PutDraftAppVersionTemplateRequestRequestTypeDef(BaseModel):
    appArn: str
    appTemplateBody: str

class S3LocationTypeDef(BaseModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None

class RemoveDraftAppVersionResourceMappingsRequestRequestTypeDef(BaseModel):
    appArn: str
    appRegistryAppNames: Optional[Sequence[str]] = None
    eksSourceNames: Optional[Sequence[str]] = None
    logicalStackNames: Optional[Sequence[str]] = None
    resourceGroupNames: Optional[Sequence[str]] = None
    resourceNames: Optional[Sequence[str]] = None
    terraformSourceNames: Optional[Sequence[str]] = None

class ScoringComponentResiliencyScoreTypeDef(BaseModel):
    excludedCount: Optional[int] = None
    outstandingCount: Optional[int] = None
    possibleScore: Optional[float] = None
    score: Optional[float] = None

class ResolveAppVersionResourcesRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str

class ResourceErrorTypeDef(BaseModel):
    logicalResourceId: Optional[str] = None
    physicalResourceId: Optional[str] = None
    reason: Optional[str] = None

class StartAppAssessmentRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    assessmentName: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAppVersionAppComponentRequestRequestTypeDef(BaseModel):
    appArn: str
    id: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None
    name: Optional[str] = None
    type: Optional[str] = None

class UpdateAppVersionRequestRequestTypeDef(BaseModel):
    appArn: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None

class DeleteAppAssessmentResponseTypeDef(BaseModel):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppResponseTypeDef(BaseModel):
    appArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRecommendationTemplateResponseTypeDef(BaseModel):
    recommendationTemplateArn: str
    status: RecommendationTemplateStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResiliencyPolicyResponseTypeDef(BaseModel):
    policyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionResourcesResolutionStatusResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    errorMessage: str
    resolutionId: str
    status: ResourceResolutionStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionResponseTypeDef(BaseModel):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionTemplateResponseTypeDef(BaseModel):
    appArn: str
    appTemplateBody: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDraftAppVersionResourcesImportStatusResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    errorMessage: str
    status: ResourceImportStatusTypeType
    statusChangeTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishAppVersionResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    identifier: int
    versionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutDraftAppVersionTemplateResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveDraftAppVersionResourceMappingsResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveAppVersionResourcesResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    resolutionId: str
    status: ResourceResolutionStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppVersionResponseTypeDef(BaseModel):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class AlarmRecommendationTypeDef(BaseModel):
    name: str
    recommendationId: str
    referenceId: str
    type: AlarmTypeType
    appComponentName: Optional[str] = None
    appComponentNames: Optional[List[str]] = None
    description: Optional[str] = None
    items: Optional[List[RecommendationItemTypeDef]] = None
    prerequisite: Optional[str] = None
    recommendationStatus: Optional[RecommendationStatusType] = None

class SopRecommendationTypeDef(BaseModel):
    recommendationId: str
    referenceId: str
    serviceType: Literal["SSM"]
    appComponentName: Optional[str] = None
    description: Optional[str] = None
    items: Optional[List[RecommendationItemTypeDef]] = None
    name: Optional[str] = None
    prerequisite: Optional[str] = None
    recommendationStatus: Optional[RecommendationStatusType] = None

class TestRecommendationTypeDef(BaseModel):
    referenceId: str
    appComponentName: Optional[str] = None
    dependsOnAlarms: Optional[List[str]] = None
    description: Optional[str] = None
    intent: Optional[str] = None
    items: Optional[List[RecommendationItemTypeDef]] = None
    name: Optional[str] = None
    prerequisite: Optional[str] = None
    recommendationId: Optional[str] = None
    recommendationStatus: Optional[RecommendationStatusType] = None
    risk: Optional[TestRiskType] = None
    type: Optional[TestTypeType] = None

class AppAssessmentSummaryTypeDef(BaseModel):
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

class ComplianceDriftTypeDef(BaseModel):
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

class CreateAppVersionAppComponentResponseTypeDef(BaseModel):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppVersionAppComponentResponseTypeDef(BaseModel):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionAppComponentResponseTypeDef(BaseModel):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppVersionAppComponentsResponseTypeDef(BaseModel):
    appArn: str
    appComponents: List[AppComponentTypeDef]
    appVersion: str
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppVersionAppComponentResponseTypeDef(BaseModel):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppInputSourceTypeDef(BaseModel):
    importType: ResourceMappingTypeType
    eksSourceClusterNamespace: Optional[EksSourceClusterNamespaceTypeDef] = None
    resourceCount: Optional[int] = None
    sourceArn: Optional[str] = None
    sourceName: Optional[str] = None
    terraformSource: Optional[TerraformSourceTypeDef] = None

class DeleteAppInputSourceRequestRequestTypeDef(BaseModel):
    appArn: str
    clientToken: Optional[str] = None
    eksSourceClusterNamespace: Optional[EksSourceClusterNamespaceTypeDef] = None
    sourceArn: Optional[str] = None
    terraformSource: Optional[TerraformSourceTypeDef] = None

class ListAppsResponseTypeDef(BaseModel):
    appSummaries: List[AppSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppTypeDef(BaseModel):
    appArn: str
    creationTime: datetime
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
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

class ListAppVersionsResponseTypeDef(BaseModel):
    appVersions: List[AppVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRecommendationStatusSuccessfulEntryTypeDef(BaseModel):
    entryId: str
    excluded: bool
    item: UpdateRecommendationStatusItemTypeDef
    referenceId: str
    excludeReason: Optional[ExcludeRecommendationReasonType] = None

class UpdateRecommendationStatusRequestEntryTypeDef(BaseModel):
    entryId: str
    excluded: bool
    item: UpdateRecommendationStatusItemTypeDef
    referenceId: str
    excludeReason: Optional[ExcludeRecommendationReasonType] = None

class ConfigRecommendationTypeDef(BaseModel):
    name: str
    optimizationType: ConfigRecommendationOptimizationTypeType
    referenceId: str
    appComponentName: Optional[str] = None
    compliance: Optional[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]] = None
    cost: Optional[CostTypeDef] = None
    description: Optional[str] = None
    haArchitecture: Optional[HaArchitectureType] = None
    recommendationCompliance: Optional[       Dict[DisruptionTypeType, RecommendationDisruptionComplianceTypeDef] = None
    suggestedChanges: Optional[List[str]] = None

class CreateAppRequestRequestTypeDef(BaseModel):
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    eventSubscriptions: Optional[Sequence[EventSubscriptionTypeDef]] = None
    permissionModel: Optional[PermissionModelTypeDef] = None
    policyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAppRequestRequestTypeDef(BaseModel):
    appArn: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    clearResiliencyPolicyArn: Optional[bool] = None
    description: Optional[str] = None
    eventSubscriptions: Optional[Sequence[EventSubscriptionTypeDef]] = None
    permissionModel: Optional[PermissionModelTypeDef] = None
    policyArn: Optional[str] = None

class CreateAppVersionResourceRequestRequestTypeDef(BaseModel):
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

class DeleteAppVersionResourceRequestRequestTypeDef(BaseModel):
    appArn: str
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    clientToken: Optional[str] = None
    logicalResourceId: Optional[LogicalResourceIdTypeDef] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None

class DescribeAppVersionResourceRequestRequestTypeDef(BaseModel):
    appArn: str
    appVersion: str
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    logicalResourceId: Optional[LogicalResourceIdTypeDef] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None

class ResourceIdentifierTypeDef(BaseModel):
    logicalResourceId: Optional[LogicalResourceIdTypeDef] = None
    resourceType: Optional[str] = None

class UpdateAppVersionResourceRequestRequestTypeDef(BaseModel):
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

class CreateResiliencyPolicyRequestRequestTypeDef(BaseModel):
    policy: Mapping[DisruptionTypeType, FailurePolicyTypeDef]
    policyName: str
    tier: ResiliencyPolicyTierType
    clientToken: Optional[str] = None
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    policyDescription: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ResiliencyPolicyTypeDef(BaseModel):
    creationTime: Optional[datetime] = None
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    estimatedCostTier: Optional[EstimatedCostTierType] = None
    policy: Optional[Dict[DisruptionTypeType, FailurePolicyTypeDef]] = None
    policyArn: Optional[str] = None
    policyDescription: Optional[str] = None
    policyName: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tier: Optional[ResiliencyPolicyTierType] = None

class UpdateResiliencyPolicyRequestRequestTypeDef(BaseModel):
    policyArn: str
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    policy: Optional[Mapping[DisruptionTypeType, FailurePolicyTypeDef]] = None
    policyDescription: Optional[str] = None
    policyName: Optional[str] = None
    tier: Optional[ResiliencyPolicyTierType] = None

class ImportResourcesToDraftAppVersionResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    eksSources: List[EksSourceOutputTypeDef]
    sourceArns: List[str]
    status: ResourceImportStatusTypeType
    terraformSources: List[TerraformSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAssessmentResourceDriftsRequestListAppAssessmentResourceDriftsPaginateTypeDef(BaseModel):
    assessmentArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppVersionsRequestRequestTypeDef(BaseModel):
    appArn: str
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class ListAppsRequestRequestTypeDef(BaseModel):
    appArn: Optional[str] = None
    fromLastAssessmentTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    reverseOrder: Optional[bool] = None
    toLastAssessmentTime: Optional[TimestampTypeDef] = None

class PhysicalResourceTypeDef(BaseModel):
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: PhysicalResourceIdTypeDef
    resourceType: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    appComponents: Optional[List[AppComponentTypeDef]] = None
    excluded: Optional[bool] = None
    parentResourceName: Optional[str] = None
    resourceName: Optional[str] = None
    sourceType: Optional[ResourceSourceTypeType] = None

class ResourceMappingTypeDef(BaseModel):
    mappingType: ResourceMappingTypeType
    physicalResourceId: PhysicalResourceIdTypeDef
    appRegistryAppName: Optional[str] = None
    eksSourceName: Optional[str] = None
    logicalStackName: Optional[str] = None
    resourceGroupName: Optional[str] = None
    resourceName: Optional[str] = None
    terraformSourceName: Optional[str] = None

class UnsupportedResourceTypeDef(BaseModel):
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: PhysicalResourceIdTypeDef
    resourceType: str
    unsupportedResourceStatus: Optional[str] = None

class RecommendationTemplateTypeDef(BaseModel):
    assessmentArn: str
    format: TemplateFormatType
    name: str
    recommendationTemplateArn: str
    recommendationTypes: List[RenderRecommendationTypeType]
    status: RecommendationTemplateStatusType
    appArn: Optional[str] = None
    endTime: Optional[datetime] = None
    message: Optional[str] = None
    needsReplacements: Optional[bool] = None
    recommendationIds: Optional[List[str]] = None
    startTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    templatesLocation: Optional[S3LocationTypeDef] = None

class ResiliencyScoreTypeDef(BaseModel):
    disruptionScore: Dict[DisruptionTypeType, float]
    score: float
    componentScore: Optional[       Dict[ResiliencyScoreTypeType, ScoringComponentResiliencyScoreTypeDef] = None

class ResourceErrorsDetailsTypeDef(BaseModel):
    hasMoreErrors: Optional[bool] = None
    resourceErrors: Optional[List[ResourceErrorTypeDef]] = None

class ListAlarmRecommendationsResponseTypeDef(BaseModel):
    alarmRecommendations: List[AlarmRecommendationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSopRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    sopRecommendations: List[SopRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestRecommendationsResponseTypeDef(BaseModel):
    nextToken: str
    testRecommendations: List[TestRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAssessmentsResponseTypeDef(BaseModel):
    assessmentSummaries: List[AppAssessmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAssessmentComplianceDriftsResponseTypeDef(BaseModel):
    complianceDrifts: List[ComplianceDriftTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppInputSourceResponseTypeDef(BaseModel):
    appArn: str
    appInputSource: AppInputSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInputSourcesResponseTypeDef(BaseModel):
    appInputSources: List[AppInputSourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppResponseTypeDef(BaseModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppResponseTypeDef(BaseModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppResponseTypeDef(BaseModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRecommendationStatusResponseTypeDef(BaseModel):
    appArn: str
    failedEntries: List[BatchUpdateRecommendationStatusFailedEntryTypeDef]
    successfulEntries: List[BatchUpdateRecommendationStatusSuccessfulEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRecommendationStatusRequestRequestTypeDef(BaseModel):
    appArn: str
    requestEntries: Sequence[UpdateRecommendationStatusRequestEntryTypeDef]

class ComponentRecommendationTypeDef(BaseModel):
    appComponentName: str
    configRecommendations: List[ConfigRecommendationTypeDef]
    recommendationStatus: RecommendationComplianceStatusType

class ResourceDriftTypeDef(BaseModel):
    appArn: Optional[str] = None
    appVersion: Optional[str] = None
    diffType: Optional[DifferenceTypeType] = None
    referenceId: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None

class CreateResiliencyPolicyResponseTypeDef(BaseModel):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResiliencyPolicyResponseTypeDef(BaseModel):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResiliencyPoliciesResponseTypeDef(BaseModel):
    nextToken: str
    resiliencyPolicies: List[ResiliencyPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSuggestedResiliencyPoliciesResponseTypeDef(BaseModel):
    nextToken: str
    resiliencyPolicies: List[ResiliencyPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResiliencyPolicyResponseTypeDef(BaseModel):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportResourcesToDraftAppVersionRequestRequestTypeDef(BaseModel):
    appArn: str
    eksSources: Optional[Sequence[EksSourceUnionTypeDef]] = None
    importStrategy: Optional[ResourceImportStrategyTypeType] = None
    sourceArns: Optional[Sequence[str]] = None
    terraformSources: Optional[Sequence[TerraformSourceTypeDef]] = None

class CreateAppVersionResourceResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppVersionResourceResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionResourceResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppVersionResourcesResponseTypeDef(BaseModel):
    nextToken: str
    physicalResources: List[PhysicalResourceTypeDef]
    resolutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppVersionResourceResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddDraftAppVersionResourceMappingsRequestRequestTypeDef(BaseModel):
    appArn: str
    resourceMappings: Sequence[ResourceMappingTypeDef]

class AddDraftAppVersionResourceMappingsResponseTypeDef(BaseModel):
    appArn: str
    appVersion: str
    resourceMappings: List[ResourceMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppVersionResourceMappingsResponseTypeDef(BaseModel):
    nextToken: str
    resourceMappings: List[ResourceMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListUnsupportedAppVersionResourcesResponseTypeDef(BaseModel):
    nextToken: str
    resolutionId: str
    unsupportedResources: List[UnsupportedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecommendationTemplateResponseTypeDef(BaseModel):
    recommendationTemplate: RecommendationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecommendationTemplatesResponseTypeDef(BaseModel):
    nextToken: str
    recommendationTemplates: List[RecommendationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AppComponentComplianceTypeDef(BaseModel):
    appComponentName: Optional[str] = None
    compliance: Optional[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]] = None
    cost: Optional[CostTypeDef] = None
    message: Optional[str] = None
    resiliencyScore: Optional[ResiliencyScoreTypeDef] = None
    status: Optional[ComplianceStatusType] = None

class AppAssessmentTypeDef(BaseModel):
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
    tags: Optional[Dict[str, str]] = None
    versionName: Optional[str] = None

class ListAppComponentRecommendationsResponseTypeDef(BaseModel):
    componentRecommendations: List[ComponentRecommendationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAssessmentResourceDriftsResponseTypeDef(BaseModel):
    nextToken: str
    resourceDrifts: List[ResourceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppComponentCompliancesResponseTypeDef(BaseModel):
    componentCompliances: List[AppComponentComplianceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppAssessmentResponseTypeDef(BaseModel):
    assessment: AppAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartAppAssessmentResponseTypeDef(BaseModel):
    assessment: AppAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


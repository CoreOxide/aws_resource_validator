from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class RecommendationItemTypeDef(BaseValidatorModel):
    alreadyImplemented: Optional[bool] = None
    excludeReason: Optional[ExcludeRecommendationReasonType] = None
    excluded: Optional[bool] = None
    resourceId: Optional[str] = None
    targetAccountId: Optional[str] = None
    targetRegion: Optional[str] = None

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

class AppComponentTypeDef(BaseValidatorModel):
    name: str
    type: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    id: Optional[str] = None

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

class PermissionModelOutputTypeDef(BaseValidatorModel):
    type: PermissionModelTypeType
    crossAccountRoleArns: Optional[List[str]] = None
    invokerRoleName: Optional[str] = None

class AppVersionSummaryTypeDef(BaseValidatorModel):
    appVersion: str
    creationTime: Optional[datetime] = None
    identifier: Optional[int] = None
    versionName: Optional[str] = None

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

class PermissionModelTypeDef(BaseValidatorModel):
    type: PermissionModelTypeType
    crossAccountRoleArns: Optional[Sequence[str]] = None
    invokerRoleName: Optional[str] = None

class CreateAppVersionAppComponentRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    name: str
    type: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None
    clientToken: Optional[str] = None
    id: Optional[str] = None

class LogicalResourceIdTypeDef(BaseValidatorModel):
    identifier: str
    eksSourceName: Optional[str] = None
    logicalStackName: Optional[str] = None
    resourceGroupName: Optional[str] = None
    terraformSourceName: Optional[str] = None

class CreateRecommendationTemplateRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    name: str
    bucketName: Optional[str] = None
    clientToken: Optional[str] = None
    format: Optional[TemplateFormatType] = None
    recommendationIds: Optional[Sequence[str]] = None
    recommendationTypes: Optional[Sequence[RenderRecommendationTypeType]] = None
    tags: Optional[Mapping[str, str]] = None

class FailurePolicyTypeDef(BaseValidatorModel):
    rpoInSecs: int
    rtoInSecs: int

class DeleteAppAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    clientToken: Optional[str] = None

class DeleteAppRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    clientToken: Optional[str] = None
    forceDelete: Optional[bool] = None

class DeleteAppVersionAppComponentRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    id: str
    clientToken: Optional[str] = None

class DeleteRecommendationTemplateRequestRequestTypeDef(BaseValidatorModel):
    recommendationTemplateArn: str
    clientToken: Optional[str] = None

class DeleteResiliencyPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyArn: str
    clientToken: Optional[str] = None

class DescribeAppAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str

class DescribeAppRequestRequestTypeDef(BaseValidatorModel):
    appArn: str

class DescribeAppVersionAppComponentRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    id: str

class DescribeAppVersionRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str

class DescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    resolutionId: Optional[str] = None

class DescribeAppVersionTemplateRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str

class DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef(BaseValidatorModel):
    appArn: str

class DescribeResiliencyPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyArn: str

class EksSourceOutputTypeDef(BaseValidatorModel):
    eksClusterArn: str
    namespaces: List[str]

class EksSourceTypeDef(BaseValidatorModel):
    eksClusterArn: str
    namespaces: Sequence[str]

class ListAlarmRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppAssessmentComplianceDriftsRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAppAssessmentResourceDriftsRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppAssessmentsRequestRequestTypeDef(BaseValidatorModel):
    appArn: Optional[str] = None
    assessmentName: Optional[str] = None
    assessmentStatus: Optional[Sequence[AssessmentStatusType]] = None
    complianceStatus: Optional[ComplianceStatusType] = None
    invoker: Optional[AssessmentInvokerType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    reverseOrder: Optional[bool] = None

class ListAppComponentCompliancesRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppComponentRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppInputSourcesRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppVersionAppComponentsRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppVersionResourceMappingsRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppVersionResourcesRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resolutionId: Optional[str] = None

class ListRecommendationTemplatesRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    recommendationTemplateArn: Optional[str] = None
    reverseOrder: Optional[bool] = None
    status: Optional[Sequence[RecommendationTemplateStatusType]] = None

class ListResiliencyPoliciesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    policyName: Optional[str] = None

class ListSopRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSuggestedResiliencyPoliciesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTestRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListUnsupportedAppVersionResourcesRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resolutionId: Optional[str] = None

class PhysicalResourceIdTypeDef(BaseValidatorModel):
    identifier: str
    type: PhysicalIdentifierTypeType
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None

class PublishAppVersionRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    versionName: Optional[str] = None

class PutDraftAppVersionTemplateRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appTemplateBody: str

class S3LocationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None

class RemoveDraftAppVersionResourceMappingsRequestRequestTypeDef(BaseValidatorModel):
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

class ResolveAppVersionResourcesRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str

class ResourceErrorTypeDef(BaseValidatorModel):
    logicalResourceId: Optional[str] = None
    physicalResourceId: Optional[str] = None
    reason: Optional[str] = None

class StartAppAssessmentRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    assessmentName: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAppVersionAppComponentRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    id: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None
    name: Optional[str] = None
    type: Optional[str] = None

class UpdateAppVersionRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    additionalInfo: Optional[Mapping[str, Sequence[str]]] = None

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

class DescribeDraftAppVersionResourcesImportStatusResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    errorMessage: str
    status: ResourceImportStatusTypeType
    statusChangeTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

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

class UpdateAppVersionResponseTypeDef(BaseValidatorModel):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class AlarmRecommendationTypeDef(BaseValidatorModel):
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

class TestRecommendationTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class DeleteAppInputSourceRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    clientToken: Optional[str] = None
    eksSourceClusterNamespace: Optional[EksSourceClusterNamespaceTypeDef] = None
    sourceArn: Optional[str] = None
    terraformSource: Optional[TerraformSourceTypeDef] = None

class ListAppsResponseTypeDef(BaseValidatorModel):
    appSummaries: List[AppSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppTypeDef(BaseValidatorModel):
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

class ListAppVersionsResponseTypeDef(BaseValidatorModel):
    appVersions: List[AppVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRecommendationStatusSuccessfulEntryTypeDef(BaseValidatorModel):
    entryId: str
    excluded: bool
    item: UpdateRecommendationStatusItemTypeDef
    referenceId: str
    excludeReason: Optional[ExcludeRecommendationReasonType] = None

class UpdateRecommendationStatusRequestEntryTypeDef(BaseValidatorModel):
    entryId: str
    excluded: bool
    item: UpdateRecommendationStatusItemTypeDef
    referenceId: str
    excludeReason: Optional[ExcludeRecommendationReasonType] = None

class ConfigRecommendationTypeDef(BaseValidatorModel):
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

class CreateAppRequestRequestTypeDef(BaseValidatorModel):
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    eventSubscriptions: Optional[Sequence[EventSubscriptionTypeDef]] = None
    permissionModel: Optional[PermissionModelTypeDef] = None
    policyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAppRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    clearResiliencyPolicyArn: Optional[bool] = None
    description: Optional[str] = None
    eventSubscriptions: Optional[Sequence[EventSubscriptionTypeDef]] = None
    permissionModel: Optional[PermissionModelTypeDef] = None
    policyArn: Optional[str] = None

class CreateAppVersionResourceRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteAppVersionResourceRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    clientToken: Optional[str] = None
    logicalResourceId: Optional[LogicalResourceIdTypeDef] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None

class DescribeAppVersionResourceRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateAppVersionResourceRequestRequestTypeDef(BaseValidatorModel):
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

class CreateResiliencyPolicyRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateResiliencyPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyArn: str
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    policy: Optional[Mapping[DisruptionTypeType, FailurePolicyTypeDef]] = None
    policyDescription: Optional[str] = None
    policyName: Optional[str] = None
    tier: Optional[ResiliencyPolicyTierType] = None

class ImportResourcesToDraftAppVersionResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    eksSources: List[EksSourceOutputTypeDef]
    sourceArns: List[str]
    status: ResourceImportStatusTypeType
    terraformSources: List[TerraformSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAssessmentResourceDriftsRequestListAppAssessmentResourceDriftsPaginateTypeDef(BaseValidatorModel):
    assessmentArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppVersionsRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class ListAppsRequestRequestTypeDef(BaseValidatorModel):
    appArn: Optional[str] = None
    fromLastAssessmentTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    reverseOrder: Optional[bool] = None
    toLastAssessmentTime: Optional[TimestampTypeDef] = None

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

class RecommendationTemplateTypeDef(BaseValidatorModel):
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

class ResiliencyScoreTypeDef(BaseValidatorModel):
    disruptionScore: Dict[DisruptionTypeType, float]
    score: float
    componentScore: Optional[       Dict[ResiliencyScoreTypeType, ScoringComponentResiliencyScoreTypeDef] = None

class ResourceErrorsDetailsTypeDef(BaseValidatorModel):
    hasMoreErrors: Optional[bool] = None
    resourceErrors: Optional[List[ResourceErrorTypeDef]] = None

class ListAlarmRecommendationsResponseTypeDef(BaseValidatorModel):
    alarmRecommendations: List[AlarmRecommendationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSopRecommendationsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    sopRecommendations: List[SopRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestRecommendationsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    testRecommendations: List[TestRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAssessmentsResponseTypeDef(BaseValidatorModel):
    assessmentSummaries: List[AppAssessmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAssessmentComplianceDriftsResponseTypeDef(BaseValidatorModel):
    complianceDrifts: List[ComplianceDriftTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppInputSourceResponseTypeDef(BaseValidatorModel):
    appArn: str
    appInputSource: AppInputSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInputSourcesResponseTypeDef(BaseValidatorModel):
    appInputSources: List[AppInputSourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class BatchUpdateRecommendationStatusRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    resiliencyPolicies: List[ResiliencyPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSuggestedResiliencyPoliciesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    resiliencyPolicies: List[ResiliencyPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResiliencyPolicyResponseTypeDef(BaseValidatorModel):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportResourcesToDraftAppVersionRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    eksSources: Optional[Sequence[EksSourceUnionTypeDef]] = None
    importStrategy: Optional[ResourceImportStrategyTypeType] = None
    sourceArns: Optional[Sequence[str]] = None
    terraformSources: Optional[Sequence[TerraformSourceTypeDef]] = None

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
    nextToken: str
    physicalResources: List[PhysicalResourceTypeDef]
    resolutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppVersionResourceResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddDraftAppVersionResourceMappingsRequestRequestTypeDef(BaseValidatorModel):
    appArn: str
    resourceMappings: Sequence[ResourceMappingTypeDef]

class AddDraftAppVersionResourceMappingsResponseTypeDef(BaseValidatorModel):
    appArn: str
    appVersion: str
    resourceMappings: List[ResourceMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppVersionResourceMappingsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    resourceMappings: List[ResourceMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListUnsupportedAppVersionResourcesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    resolutionId: str
    unsupportedResources: List[UnsupportedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecommendationTemplateResponseTypeDef(BaseValidatorModel):
    recommendationTemplate: RecommendationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecommendationTemplatesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    recommendationTemplates: List[RecommendationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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
    tags: Optional[Dict[str, str]] = None
    versionName: Optional[str] = None

class ListAppComponentRecommendationsResponseTypeDef(BaseValidatorModel):
    componentRecommendations: List[ComponentRecommendationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAssessmentResourceDriftsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    resourceDrifts: List[ResourceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppComponentCompliancesResponseTypeDef(BaseValidatorModel):
    componentCompliances: List[AppComponentComplianceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppAssessmentResponseTypeDef(BaseValidatorModel):
    assessment: AppAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartAppAssessmentResponseTypeDef(BaseValidatorModel):
    assessment: AppAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


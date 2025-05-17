from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.resiliencehub.resiliencehub_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptGroupingRecommendationEntry(BaseValidatorModel):
    groupingRecommendationId: str


class FailedGroupingRecommendationEntry(BaseValidatorModel):
    errorMessage: str
    groupingRecommendationId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Alarm(BaseValidatorModel):
    alarmArn: Optional[str] = None
    source: Optional[str] = None


class Cost(BaseValidatorModel):
    amount: float
    currency: str
    frequency: CostFrequencyType


class DisruptionCompliance(BaseValidatorModel):
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


class AppComponent(BaseValidatorModel):
    name: str
    type: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    id: Optional[str] = None


class EksSourceClusterNamespace(BaseValidatorModel):
    eksClusterArn: str
    namespace: str


class TerraformSource(BaseValidatorModel):
    s3StateFileUrl: str


class AppSummary(BaseValidatorModel):
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


class EventSubscription(BaseValidatorModel):
    eventType: EventTypeType
    name: str
    snsTopicArn: Optional[str] = None


class PermissionModelOutput(BaseValidatorModel):
    type: PermissionModelTypeType
    crossAccountRoleArns: Optional[List[str]] = None
    invokerRoleName: Optional[str] = None


class AppVersionSummary(BaseValidatorModel):
    appVersion: str
    creationTime: Optional[datetime] = None
    identifier: Optional[int] = None
    versionName: Optional[str] = None


class AssessmentRiskRecommendation(BaseValidatorModel):
    appComponents: Optional[List[str]] = None
    recommendation: Optional[str] = None
    risk: Optional[str] = None


class BatchUpdateRecommendationStatusFailedEntry(BaseValidatorModel):
    entryId: str
    errorMessage: str


class UpdateRecommendationStatusItem(BaseValidatorModel):
    resourceId: Optional[str] = None
    targetAccountId: Optional[str] = None
    targetRegion: Optional[str] = None


class Condition(BaseValidatorModel):
    field: str
    operator: ConditionOperatorTypeType
    value: Optional[str] = None


class RecommendationDisruptionCompliance(BaseValidatorModel):
    expectedComplianceStatus: ComplianceStatusType
    expectedRpoDescription: Optional[str] = None
    expectedRpoInSecs: Optional[int] = None
    expectedRtoDescription: Optional[str] = None
    expectedRtoInSecs: Optional[int] = None


# This class is the input for the 'create_app_version_app_component' function.
class CreateAppVersionAppComponentRequest(BaseValidatorModel):
    appArn: str
    name: str
    type: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    clientToken: Optional[str] = None
    id: Optional[str] = None


class LogicalResourceId(BaseValidatorModel):
    identifier: str
    eksSourceName: Optional[str] = None
    logicalStackName: Optional[str] = None
    resourceGroupName: Optional[str] = None
    terraformSourceName: Optional[str] = None


# This class is the input for the 'create_recommendation_template' function.
class CreateRecommendationTemplateRequest(BaseValidatorModel):
    assessmentArn: str
    name: str
    bucketName: Optional[str] = None
    clientToken: Optional[str] = None
    format: Optional[TemplateFormatType] = None
    recommendationIds: Optional[List[str]] = None
    recommendationTypes: Optional[List[RenderRecommendationTypeType]] = None
    tags: Optional[Dict[str, str]] = None


class FailurePolicy(BaseValidatorModel):
    rpoInSecs: int
    rtoInSecs: int


# This class is the input for the 'delete_app_assessment' function.
class DeleteAppAssessmentRequest(BaseValidatorModel):
    assessmentArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_app' function.
class DeleteAppRequest(BaseValidatorModel):
    appArn: str
    clientToken: Optional[str] = None
    forceDelete: Optional[bool] = None


# This class is the input for the 'delete_app_version_app_component' function.
class DeleteAppVersionAppComponentRequest(BaseValidatorModel):
    appArn: str
    id: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_recommendation_template' function.
class DeleteRecommendationTemplateRequest(BaseValidatorModel):
    recommendationTemplateArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_resiliency_policy' function.
class DeleteResiliencyPolicyRequest(BaseValidatorModel):
    policyArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'describe_app_assessment' function.
class DescribeAppAssessmentRequest(BaseValidatorModel):
    assessmentArn: str


# This class is the input for the 'describe_app' function.
class DescribeAppRequest(BaseValidatorModel):
    appArn: str


# This class is the input for the 'describe_app_version_app_component' function.
class DescribeAppVersionAppComponentRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    id: str


# This class is the input for the 'describe_app_version' function.
class DescribeAppVersionRequest(BaseValidatorModel):
    appArn: str
    appVersion: str


# This class is the input for the 'describe_app_version_resources_resolution_status' function.
class DescribeAppVersionResourcesResolutionStatusRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    resolutionId: Optional[str] = None


# This class is the input for the 'describe_app_version_template' function.
class DescribeAppVersionTemplateRequest(BaseValidatorModel):
    appArn: str
    appVersion: str


# This class is the input for the 'describe_draft_app_version_resources_import_status' function.
class DescribeDraftAppVersionResourcesImportStatusRequest(BaseValidatorModel):
    appArn: str


class ErrorDetail(BaseValidatorModel):
    errorMessage: Optional[str] = None


# This class is the input for the 'describe_metrics_export' function.
class DescribeMetricsExportRequest(BaseValidatorModel):
    metricsExportId: str


class S3Location(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None


# This class is the input for the 'describe_resiliency_policy' function.
class DescribeResiliencyPolicyRequest(BaseValidatorModel):
    policyArn: str


# This class is the input for the 'describe_resource_grouping_recommendation_task' function.
class DescribeResourceGroupingRecommendationTaskRequest(BaseValidatorModel):
    appArn: str
    groupingId: Optional[str] = None


class EksSourceOutput(BaseValidatorModel):
    eksClusterArn: str
    namespaces: List[str]


class EksSource(BaseValidatorModel):
    eksClusterArn: str
    namespaces: List[str]


class Experiment(BaseValidatorModel):
    experimentArn: Optional[str] = None
    experimentTemplateId: Optional[str] = None


class Field(BaseValidatorModel):
    name: str
    aggregation: Optional[FieldAggregationTypeType] = None


class GroupingAppComponent(BaseValidatorModel):
    appComponentId: str
    appComponentName: str
    appComponentType: str


class PhysicalResourceId(BaseValidatorModel):
    identifier: str
    type: PhysicalIdentifierTypeType
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None


# This class is the input for the 'list_alarm_recommendations' function.
class ListAlarmRecommendationsRequest(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_app_assessment_compliance_drifts' function.
class ListAppAssessmentComplianceDriftsRequest(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_app_assessment_resource_drifts' function.
class ListAppAssessmentResourceDriftsRequest(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_app_assessments' function.
class ListAppAssessmentsRequest(BaseValidatorModel):
    appArn: Optional[str] = None
    assessmentName: Optional[str] = None
    assessmentStatus: Optional[List[AssessmentStatusType]] = None
    complianceStatus: Optional[ComplianceStatusType] = None
    invoker: Optional[AssessmentInvokerType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    reverseOrder: Optional[bool] = None


# This class is the input for the 'list_app_component_compliances' function.
class ListAppComponentCompliancesRequest(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_app_component_recommendations' function.
class ListAppComponentRecommendationsRequest(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_app_input_sources' function.
class ListAppInputSourcesRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_app_version_app_components' function.
class ListAppVersionAppComponentsRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_app_version_resource_mappings' function.
class ListAppVersionResourceMappingsRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_app_version_resources' function.
class ListAppVersionResourcesRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resolutionId: Optional[str] = None

Timestamp = Union[datetime, str]


class Sort(BaseValidatorModel):
    field: str
    ascending: Optional[bool] = None


# This class is the input for the 'list_recommendation_templates' function.
class ListRecommendationTemplatesRequest(BaseValidatorModel):
    assessmentArn: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    recommendationTemplateArn: Optional[str] = None
    reverseOrder: Optional[bool] = None
    status: Optional[List[RecommendationTemplateStatusType]] = None


# This class is the input for the 'list_resiliency_policies' function.
class ListResiliencyPoliciesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    policyName: Optional[str] = None


# This class is the input for the 'list_resource_grouping_recommendations' function.
class ListResourceGroupingRecommendationsRequest(BaseValidatorModel):
    appArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_sop_recommendations' function.
class ListSopRecommendationsRequest(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_suggested_resiliency_policies' function.
class ListSuggestedResiliencyPoliciesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_test_recommendations' function.
class ListTestRecommendationsRequest(BaseValidatorModel):
    assessmentArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_unsupported_app_version_resources' function.
class ListUnsupportedAppVersionResourcesRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resolutionId: Optional[str] = None


class PermissionModel(BaseValidatorModel):
    type: PermissionModelTypeType
    crossAccountRoleArns: Optional[List[str]] = None
    invokerRoleName: Optional[str] = None


# This class is the input for the 'publish_app_version' function.
class PublishAppVersionRequest(BaseValidatorModel):
    appArn: str
    versionName: Optional[str] = None


# This class is the input for the 'put_draft_app_version_template' function.
class PutDraftAppVersionTemplateRequest(BaseValidatorModel):
    appArn: str
    appTemplateBody: str


class RejectGroupingRecommendationEntry(BaseValidatorModel):
    groupingRecommendationId: str
    rejectionReason: Optional[GroupingRecommendationRejectionReasonType] = None


# This class is the input for the 'remove_draft_app_version_resource_mappings' function.
class RemoveDraftAppVersionResourceMappingsRequest(BaseValidatorModel):
    appArn: str
    appRegistryAppNames: Optional[List[str]] = None
    eksSourceNames: Optional[List[str]] = None
    logicalStackNames: Optional[List[str]] = None
    resourceGroupNames: Optional[List[str]] = None
    resourceNames: Optional[List[str]] = None
    terraformSourceNames: Optional[List[str]] = None


class ScoringComponentResiliencyScore(BaseValidatorModel):
    excludedCount: Optional[int] = None
    outstandingCount: Optional[int] = None
    possibleScore: Optional[float] = None
    score: Optional[float] = None


# This class is the input for the 'resolve_app_version_resources' function.
class ResolveAppVersionResourcesRequest(BaseValidatorModel):
    appArn: str
    appVersion: str


class ResourceError(BaseValidatorModel):
    logicalResourceId: Optional[str] = None
    physicalResourceId: Optional[str] = None
    reason: Optional[str] = None


# This class is the input for the 'start_app_assessment' function.
class StartAppAssessmentRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    assessmentName: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'start_metrics_export' function.
class StartMetricsExportRequest(BaseValidatorModel):
    bucketName: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the input for the 'start_resource_grouping_recommendation_task' function.
class StartResourceGroupingRecommendationTaskRequest(BaseValidatorModel):
    appArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_app_version_app_component' function.
class UpdateAppVersionAppComponentRequest(BaseValidatorModel):
    appArn: str
    id: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    name: Optional[str] = None
    type: Optional[str] = None


# This class is the input for the 'update_app_version' function.
class UpdateAppVersionRequest(BaseValidatorModel):
    appArn: str
    additionalInfo: Optional[Dict[str, List[str]]] = None


# This class is the input for the 'accept_resource_grouping_recommendations' function.
class AcceptResourceGroupingRecommendationsRequest(BaseValidatorModel):
    appArn: str
    entries: List[AcceptGroupingRecommendationEntry]


# This class is the output for the 'accept_resource_grouping_recommendations' function.
class AcceptResourceGroupingRecommendationsResponse(BaseValidatorModel):
    appArn: str
    failedEntries: List[FailedGroupingRecommendationEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_app_assessment' function.
class DeleteAppAssessmentResponse(BaseValidatorModel):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_app' function.
class DeleteAppResponse(BaseValidatorModel):
    appArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_recommendation_template' function.
class DeleteRecommendationTemplateResponse(BaseValidatorModel):
    recommendationTemplateArn: str
    status: RecommendationTemplateStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resiliency_policy' function.
class DeleteResiliencyPolicyResponse(BaseValidatorModel):
    policyArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_version_resources_resolution_status' function.
class DescribeAppVersionResourcesResolutionStatusResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    errorMessage: str
    resolutionId: str
    status: ResourceResolutionStatusTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_version' function.
class DescribeAppVersionResponse(BaseValidatorModel):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_version_template' function.
class DescribeAppVersionTemplateResponse(BaseValidatorModel):
    appArn: str
    appTemplateBody: str
    appVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resource_grouping_recommendation_task' function.
class DescribeResourceGroupingRecommendationTaskResponse(BaseValidatorModel):
    errorMessage: str
    groupingId: str
    status: ResourcesGroupingRecGenStatusTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_metrics' function.
class ListMetricsResponse(BaseValidatorModel):
    rows: List[List[str]]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'publish_app_version' function.
class PublishAppVersionResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    identifier: int
    versionName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_draft_app_version_template' function.
class PutDraftAppVersionTemplateResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_resource_grouping_recommendations' function.
class RejectResourceGroupingRecommendationsResponse(BaseValidatorModel):
    appArn: str
    failedEntries: List[FailedGroupingRecommendationEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_draft_app_version_resource_mappings' function.
class RemoveDraftAppVersionResourceMappingsResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'resolve_app_version_resources' function.
class ResolveAppVersionResourcesResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    resolutionId: str
    status: ResourceResolutionStatusTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_metrics_export' function.
class StartMetricsExportResponse(BaseValidatorModel):
    metricsExportId: str
    status: MetricsExportStatusTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_resource_grouping_recommendation_task' function.
class StartResourceGroupingRecommendationTaskResponse(BaseValidatorModel):
    appArn: str
    errorMessage: str
    groupingId: str
    status: ResourcesGroupingRecGenStatusTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app_version' function.
class UpdateAppVersionResponse(BaseValidatorModel):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadata


class AppAssessmentSummary(BaseValidatorModel):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    appArn: Optional[str] = None
    appVersion: Optional[str] = None
    assessmentName: Optional[str] = None
    complianceStatus: Optional[ComplianceStatusType] = None
    cost: Optional[Cost] = None
    driftStatus: Optional[DriftStatusType] = None
    endTime: Optional[datetime] = None
    invoker: Optional[AssessmentInvokerType] = None
    message: Optional[str] = None
    resiliencyScore: Optional[float] = None
    startTime: Optional[datetime] = None
    versionName: Optional[str] = None


class ComplianceDrift(BaseValidatorModel):
    actualReferenceId: Optional[str] = None
    actualValue: Optional[Dict[DisruptionTypeType, DisruptionCompliance]] = None
    appId: Optional[str] = None
    appVersion: Optional[str] = None
    diffType: Optional[DifferenceTypeType] = None
    driftType: Optional[DriftTypeType] = None
    entityId: Optional[str] = None
    entityType: Optional[str] = None
    expectedReferenceId: Optional[str] = None
    expectedValue: Optional[Dict[DisruptionTypeType, DisruptionCompliance]] = None


# This class is the output for the 'create_app_version_app_component' function.
class CreateAppVersionAppComponentResponse(BaseValidatorModel):
    appArn: str
    appComponent: AppComponent
    appVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_app_version_app_component' function.
class DeleteAppVersionAppComponentResponse(BaseValidatorModel):
    appArn: str
    appComponent: AppComponent
    appVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_version_app_component' function.
class DescribeAppVersionAppComponentResponse(BaseValidatorModel):
    appArn: str
    appComponent: AppComponent
    appVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_version_app_components' function.
class ListAppVersionAppComponentsResponse(BaseValidatorModel):
    appArn: str
    appComponents: List[AppComponent]
    appVersion: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_app_version_app_component' function.
class UpdateAppVersionAppComponentResponse(BaseValidatorModel):
    appArn: str
    appComponent: AppComponent
    appVersion: str
    ResponseMetadata: ResponseMetadata


class AppInputSource(BaseValidatorModel):
    importType: ResourceMappingTypeType
    eksSourceClusterNamespace: Optional[EksSourceClusterNamespace] = None
    resourceCount: Optional[int] = None
    sourceArn: Optional[str] = None
    sourceName: Optional[str] = None
    terraformSource: Optional[TerraformSource] = None


# This class is the input for the 'delete_app_input_source' function.
class DeleteAppInputSourceRequest(BaseValidatorModel):
    appArn: str
    clientToken: Optional[str] = None
    eksSourceClusterNamespace: Optional[EksSourceClusterNamespace] = None
    sourceArn: Optional[str] = None
    terraformSource: Optional[TerraformSource] = None


# This class is the output for the 'list_apps' function.
class ListAppsResponse(BaseValidatorModel):
    appSummaries: List[AppSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class App(BaseValidatorModel):
    appArn: str
    creationTime: datetime
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    awsApplicationArn: Optional[str] = None
    complianceStatus: Optional[AppComplianceStatusTypeType] = None
    description: Optional[str] = None
    driftStatus: Optional[AppDriftStatusTypeType] = None
    eventSubscriptions: Optional[List[EventSubscription]] = None
    lastAppComplianceEvaluationTime: Optional[datetime] = None
    lastDriftEvaluationTime: Optional[datetime] = None
    lastResiliencyScoreEvaluationTime: Optional[datetime] = None
    permissionModel: Optional[PermissionModelOutput] = None
    policyArn: Optional[str] = None
    resiliencyScore: Optional[float] = None
    rpoInSecs: Optional[int] = None
    rtoInSecs: Optional[int] = None
    status: Optional[AppStatusTypeType] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'list_app_versions' function.
class ListAppVersionsResponse(BaseValidatorModel):
    appVersions: List[AppVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssessmentSummary(BaseValidatorModel):
    riskRecommendations: Optional[List[AssessmentRiskRecommendation]] = None
    summary: Optional[str] = None


class BatchUpdateRecommendationStatusSuccessfulEntry(BaseValidatorModel):
    entryId: str
    excluded: bool
    referenceId: str
    appComponentId: Optional[str] = None
    excludeReason: Optional[ExcludeRecommendationReasonType] = None
    item: Optional[UpdateRecommendationStatusItem] = None


class UpdateRecommendationStatusRequestEntry(BaseValidatorModel):
    entryId: str
    excluded: bool
    referenceId: str
    appComponentId: Optional[str] = None
    excludeReason: Optional[ExcludeRecommendationReasonType] = None
    item: Optional[UpdateRecommendationStatusItem] = None


class ConfigRecommendation(BaseValidatorModel):
    name: str
    optimizationType: ConfigRecommendationOptimizationTypeType
    referenceId: str
    appComponentName: Optional[str] = None
    compliance: Optional[Dict[DisruptionTypeType, DisruptionCompliance]] = None
    cost: Optional[Cost] = None
    description: Optional[str] = None
    haArchitecture: Optional[HaArchitectureType] = None
    recommendationCompliance: Optional[Dict[DisruptionTypeType, RecommendationDisruptionCompliance]] = None
    suggestedChanges: Optional[List[str]] = None


# This class is the input for the 'create_app_version_resource' function.
class CreateAppVersionResourceRequest(BaseValidatorModel):
    appArn: str
    appComponents: List[str]
    logicalResourceId: LogicalResourceId
    physicalResourceId: str
    resourceType: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    clientToken: Optional[str] = None
    resourceName: Optional[str] = None


# This class is the input for the 'delete_app_version_resource' function.
class DeleteAppVersionResourceRequest(BaseValidatorModel):
    appArn: str
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    clientToken: Optional[str] = None
    logicalResourceId: Optional[LogicalResourceId] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None


# This class is the input for the 'describe_app_version_resource' function.
class DescribeAppVersionResourceRequest(BaseValidatorModel):
    appArn: str
    appVersion: str
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    logicalResourceId: Optional[LogicalResourceId] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None


class ResourceIdentifier(BaseValidatorModel):
    logicalResourceId: Optional[LogicalResourceId] = None
    resourceType: Optional[str] = None


# This class is the input for the 'update_app_version_resource' function.
class UpdateAppVersionResourceRequest(BaseValidatorModel):
    appArn: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    appComponents: Optional[List[str]] = None
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    excluded: Optional[bool] = None
    logicalResourceId: Optional[LogicalResourceId] = None
    physicalResourceId: Optional[str] = None
    resourceName: Optional[str] = None
    resourceType: Optional[str] = None


# This class is the input for the 'create_resiliency_policy' function.
class CreateResiliencyPolicyRequest(BaseValidatorModel):
    policy: Dict[DisruptionTypeType, FailurePolicy]
    policyName: str
    tier: ResiliencyPolicyTierType
    clientToken: Optional[str] = None
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    policyDescription: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ResiliencyPolicy(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    estimatedCostTier: Optional[EstimatedCostTierType] = None
    policy: Optional[Dict[DisruptionTypeType, FailurePolicy]] = None
    policyArn: Optional[str] = None
    policyDescription: Optional[str] = None
    policyName: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tier: Optional[ResiliencyPolicyTierType] = None


# This class is the input for the 'update_resiliency_policy' function.
class UpdateResiliencyPolicyRequest(BaseValidatorModel):
    policyArn: str
    dataLocationConstraint: Optional[DataLocationConstraintType] = None
    policy: Optional[Dict[DisruptionTypeType, FailurePolicy]] = None
    policyDescription: Optional[str] = None
    policyName: Optional[str] = None
    tier: Optional[ResiliencyPolicyTierType] = None


# This class is the output for the 'describe_draft_app_version_resources_import_status' function.
class DescribeDraftAppVersionResourcesImportStatusResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    errorDetails: List[ErrorDetail]
    errorMessage: str
    status: ResourceImportStatusTypeType
    statusChangeTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_metrics_export' function.
class DescribeMetricsExportResponse(BaseValidatorModel):
    errorMessage: str
    exportLocation: S3Location
    metricsExportId: str
    status: MetricsExportStatusTypeType
    ResponseMetadata: ResponseMetadata


class RecommendationTemplate(BaseValidatorModel):
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
    templatesLocation: Optional[S3Location] = None


# This class is the output for the 'import_resources_to_draft_app_version' function.
class ImportResourcesToDraftAppVersionResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    eksSources: List[EksSourceOutput]
    sourceArns: List[str]
    status: ResourceImportStatusTypeType
    terraformSources: List[TerraformSource]
    ResponseMetadata: ResponseMetadata

EksSourceUnion = Union[EksSource, EksSourceOutput]


class RecommendationItem(BaseValidatorModel):
    alreadyImplemented: Optional[bool] = None
    discoveredAlarm: Optional[Alarm] = None
    excludeReason: Optional[ExcludeRecommendationReasonType] = None
    excluded: Optional[bool] = None
    latestDiscoveredExperiment: Optional[Experiment] = None
    resourceId: Optional[str] = None
    targetAccountId: Optional[str] = None
    targetRegion: Optional[str] = None


class GroupingResource(BaseValidatorModel):
    logicalResourceId: LogicalResourceId
    physicalResourceId: PhysicalResourceId
    resourceName: str
    resourceType: str
    sourceAppComponentIds: List[str]


class PhysicalResource(BaseValidatorModel):
    logicalResourceId: LogicalResourceId
    physicalResourceId: PhysicalResourceId
    resourceType: str
    additionalInfo: Optional[Dict[str, List[str]]] = None
    appComponents: Optional[List[AppComponent]] = None
    excluded: Optional[bool] = None
    parentResourceName: Optional[str] = None
    resourceName: Optional[str] = None
    sourceType: Optional[ResourceSourceTypeType] = None


class ResourceMapping(BaseValidatorModel):
    mappingType: ResourceMappingTypeType
    physicalResourceId: PhysicalResourceId
    appRegistryAppName: Optional[str] = None
    eksSourceName: Optional[str] = None
    logicalStackName: Optional[str] = None
    resourceGroupName: Optional[str] = None
    resourceName: Optional[str] = None
    terraformSourceName: Optional[str] = None


class UnsupportedResource(BaseValidatorModel):
    logicalResourceId: LogicalResourceId
    physicalResourceId: PhysicalResourceId
    resourceType: str
    unsupportedResourceStatus: Optional[str] = None


class ListAppAssessmentResourceDriftsRequestPaginate(BaseValidatorModel):
    assessmentArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceGroupingRecommendationsRequestPaginate(BaseValidatorModel):
    appArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_app_versions' function.
class ListAppVersionsRequest(BaseValidatorModel):
    appArn: str
    endTime: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startTime: Optional[Timestamp] = None


# This class is the input for the 'list_apps' function.
class ListAppsRequest(BaseValidatorModel):
    appArn: Optional[str] = None
    awsApplicationArn: Optional[str] = None
    fromLastAssessmentTime: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    reverseOrder: Optional[bool] = None
    toLastAssessmentTime: Optional[Timestamp] = None


class ListMetricsRequestPaginate(BaseValidatorModel):
    conditions: Optional[List[Condition]] = None
    dataSource: Optional[str] = None
    fields: Optional[List[Field]] = None
    sorts: Optional[List[Sort]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_metrics' function.
class ListMetricsRequest(BaseValidatorModel):
    conditions: Optional[List[Condition]] = None
    dataSource: Optional[str] = None
    fields: Optional[List[Field]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sorts: Optional[List[Sort]] = None

PermissionModelUnion = Union[PermissionModel, PermissionModelOutput]


# This class is the input for the 'reject_resource_grouping_recommendations' function.
class RejectResourceGroupingRecommendationsRequest(BaseValidatorModel):
    appArn: str
    entries: List[RejectGroupingRecommendationEntry]


class ResiliencyScore(BaseValidatorModel):
    disruptionScore: Dict[DisruptionTypeType, float]
    score: float
    componentScore: Optional[Dict[ResiliencyScoreTypeType, ScoringComponentResiliencyScore]] = None


class ResourceErrorsDetails(BaseValidatorModel):
    hasMoreErrors: Optional[bool] = None
    resourceErrors: Optional[List[ResourceError]] = None


# This class is the output for the 'list_app_assessments' function.
class ListAppAssessmentsResponse(BaseValidatorModel):
    assessmentSummaries: List[AppAssessmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_app_assessment_compliance_drifts' function.
class ListAppAssessmentComplianceDriftsResponse(BaseValidatorModel):
    complianceDrifts: List[ComplianceDrift]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'delete_app_input_source' function.
class DeleteAppInputSourceResponse(BaseValidatorModel):
    appArn: str
    appInputSource: AppInputSource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_input_sources' function.
class ListAppInputSourcesResponse(BaseValidatorModel):
    appInputSources: List[AppInputSource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_app' function.
class CreateAppResponse(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app' function.
class DescribeAppResponse(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app' function.
class UpdateAppResponse(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_update_recommendation_status' function.
class BatchUpdateRecommendationStatusResponse(BaseValidatorModel):
    appArn: str
    failedEntries: List[BatchUpdateRecommendationStatusFailedEntry]
    successfulEntries: List[BatchUpdateRecommendationStatusSuccessfulEntry]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_update_recommendation_status' function.
class BatchUpdateRecommendationStatusRequest(BaseValidatorModel):
    appArn: str
    requestEntries: List[UpdateRecommendationStatusRequestEntry]


class ComponentRecommendation(BaseValidatorModel):
    appComponentName: str
    configRecommendations: List[ConfigRecommendation]
    recommendationStatus: RecommendationComplianceStatusType


class ResourceDrift(BaseValidatorModel):
    appArn: Optional[str] = None
    appVersion: Optional[str] = None
    diffType: Optional[DifferenceTypeType] = None
    referenceId: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifier] = None


# This class is the output for the 'create_resiliency_policy' function.
class CreateResiliencyPolicyResponse(BaseValidatorModel):
    policy: ResiliencyPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resiliency_policy' function.
class DescribeResiliencyPolicyResponse(BaseValidatorModel):
    policy: ResiliencyPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resiliency_policies' function.
class ListResiliencyPoliciesResponse(BaseValidatorModel):
    resiliencyPolicies: List[ResiliencyPolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_suggested_resiliency_policies' function.
class ListSuggestedResiliencyPoliciesResponse(BaseValidatorModel):
    resiliencyPolicies: List[ResiliencyPolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_resiliency_policy' function.
class UpdateResiliencyPolicyResponse(BaseValidatorModel):
    policy: ResiliencyPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_recommendation_template' function.
class CreateRecommendationTemplateResponse(BaseValidatorModel):
    recommendationTemplate: RecommendationTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_recommendation_templates' function.
class ListRecommendationTemplatesResponse(BaseValidatorModel):
    recommendationTemplates: List[RecommendationTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'import_resources_to_draft_app_version' function.
class ImportResourcesToDraftAppVersionRequest(BaseValidatorModel):
    appArn: str
    eksSources: Optional[List[EksSourceUnion]] = None
    importStrategy: Optional[ResourceImportStrategyTypeType] = None
    sourceArns: Optional[List[str]] = None
    terraformSources: Optional[List[TerraformSource]] = None


class AlarmRecommendation(BaseValidatorModel):
    name: str
    recommendationId: str
    referenceId: str
    type: AlarmTypeType
    appComponentName: Optional[str] = None
    appComponentNames: Optional[List[str]] = None
    description: Optional[str] = None
    items: Optional[List[RecommendationItem]] = None
    prerequisite: Optional[str] = None
    recommendationStatus: Optional[RecommendationStatusType] = None


class SopRecommendation(BaseValidatorModel):
    recommendationId: str
    referenceId: str
    serviceType: Literal['SSM']
    appComponentName: Optional[str] = None
    description: Optional[str] = None
    items: Optional[List[RecommendationItem]] = None
    name: Optional[str] = None
    prerequisite: Optional[str] = None
    recommendationStatus: Optional[RecommendationStatusType] = None


class TestRecommendation(BaseValidatorModel):
    referenceId: str
    appComponentId: Optional[str] = None
    appComponentName: Optional[str] = None
    dependsOnAlarms: Optional[List[str]] = None
    description: Optional[str] = None
    intent: Optional[str] = None
    items: Optional[List[RecommendationItem]] = None
    name: Optional[str] = None
    prerequisite: Optional[str] = None
    recommendationId: Optional[str] = None
    recommendationStatus: Optional[RecommendationStatusType] = None
    risk: Optional[TestRiskType] = None
    type: Optional[TestTypeType] = None


class GroupingRecommendation(BaseValidatorModel):
    confidenceLevel: GroupingRecommendationConfidenceLevelType
    creationTime: datetime
    groupingAppComponent: GroupingAppComponent
    groupingRecommendationId: str
    recommendationReasons: List[str]
    resources: List[GroupingResource]
    score: float
    status: GroupingRecommendationStatusTypeType
    rejectionReason: Optional[GroupingRecommendationRejectionReasonType] = None


# This class is the output for the 'create_app_version_resource' function.
class CreateAppVersionResourceResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_app_version_resource' function.
class DeleteAppVersionResourceResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_version_resource' function.
class DescribeAppVersionResourceResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_version_resources' function.
class ListAppVersionResourcesResponse(BaseValidatorModel):
    physicalResources: List[PhysicalResource]
    resolutionId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_app_version_resource' function.
class UpdateAppVersionResourceResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResource
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'add_draft_app_version_resource_mappings' function.
class AddDraftAppVersionResourceMappingsRequest(BaseValidatorModel):
    appArn: str
    resourceMappings: List[ResourceMapping]


# This class is the output for the 'add_draft_app_version_resource_mappings' function.
class AddDraftAppVersionResourceMappingsResponse(BaseValidatorModel):
    appArn: str
    appVersion: str
    resourceMappings: List[ResourceMapping]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_version_resource_mappings' function.
class ListAppVersionResourceMappingsResponse(BaseValidatorModel):
    resourceMappings: List[ResourceMapping]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_unsupported_app_version_resources' function.
class ListUnsupportedAppVersionResourcesResponse(BaseValidatorModel):
    resolutionId: str
    unsupportedResources: List[UnsupportedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_app' function.
class CreateAppRequest(BaseValidatorModel):
    name: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    awsApplicationArn: Optional[str] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    eventSubscriptions: Optional[List[EventSubscription]] = None
    permissionModel: Optional[PermissionModelUnion] = None
    policyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_app' function.
class UpdateAppRequest(BaseValidatorModel):
    appArn: str
    assessmentSchedule: Optional[AppAssessmentScheduleTypeType] = None
    clearResiliencyPolicyArn: Optional[bool] = None
    description: Optional[str] = None
    eventSubscriptions: Optional[List[EventSubscription]] = None
    permissionModel: Optional[PermissionModelUnion] = None
    policyArn: Optional[str] = None


class AppComponentCompliance(BaseValidatorModel):
    appComponentName: Optional[str] = None
    compliance: Optional[Dict[DisruptionTypeType, DisruptionCompliance]] = None
    cost: Optional[Cost] = None
    message: Optional[str] = None
    resiliencyScore: Optional[ResiliencyScore] = None
    status: Optional[ComplianceStatusType] = None


class AppAssessment(BaseValidatorModel):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    invoker: AssessmentInvokerType
    appArn: Optional[str] = None
    appVersion: Optional[str] = None
    assessmentName: Optional[str] = None
    compliance: Optional[Dict[DisruptionTypeType, DisruptionCompliance]] = None
    complianceStatus: Optional[ComplianceStatusType] = None
    cost: Optional[Cost] = None
    driftStatus: Optional[DriftStatusType] = None
    endTime: Optional[datetime] = None
    message: Optional[str] = None
    policy: Optional[ResiliencyPolicy] = None
    resiliencyScore: Optional[ResiliencyScore] = None
    resourceErrorsDetails: Optional[ResourceErrorsDetails] = None
    startTime: Optional[datetime] = None
    summary: Optional[AssessmentSummary] = None
    tags: Optional[Dict[str, str]] = None
    versionName: Optional[str] = None


# This class is the output for the 'list_app_component_recommendations' function.
class ListAppComponentRecommendationsResponse(BaseValidatorModel):
    componentRecommendations: List[ComponentRecommendation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_app_assessment_resource_drifts' function.
class ListAppAssessmentResourceDriftsResponse(BaseValidatorModel):
    resourceDrifts: List[ResourceDrift]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_alarm_recommendations' function.
class ListAlarmRecommendationsResponse(BaseValidatorModel):
    alarmRecommendations: List[AlarmRecommendation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sop_recommendations' function.
class ListSopRecommendationsResponse(BaseValidatorModel):
    sopRecommendations: List[SopRecommendation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_test_recommendations' function.
class ListTestRecommendationsResponse(BaseValidatorModel):
    testRecommendations: List[TestRecommendation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_resource_grouping_recommendations' function.
class ListResourceGroupingRecommendationsResponse(BaseValidatorModel):
    groupingRecommendations: List[GroupingRecommendation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_app_component_compliances' function.
class ListAppComponentCompliancesResponse(BaseValidatorModel):
    componentCompliances: List[AppComponentCompliance]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_app_assessment' function.
class DescribeAppAssessmentResponse(BaseValidatorModel):
    assessment: AppAssessment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_app_assessment' function.
class StartAppAssessmentResponse(BaseValidatorModel):
    assessment: AppAssessment
    ResponseMetadata: ResponseMetadata
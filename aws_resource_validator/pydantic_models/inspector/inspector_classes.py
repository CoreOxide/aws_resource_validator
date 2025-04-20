from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.inspector.inspector_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Attribute(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class FailedItemDetails(BaseValidatorModel):
    failureCode: FailedItemErrorCodeType
    retryable: bool


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AgentFilter(BaseValidatorModel):
    agentHealths: List[AgentHealthType]
    agentHealthCodes: List[AgentHealthCodeType]


class AgentPreview(BaseValidatorModel):
    agentId: str
    hostname: Optional[str] = None
    autoScalingGroup: Optional[str] = None
    agentHealth: Optional[AgentHealthType] = None
    agentVersion: Optional[str] = None
    operatingSystem: Optional[str] = None
    kernelVersion: Optional[str] = None
    ipv4Address: Optional[str] = None


class TelemetryMetadata(BaseValidatorModel):
    messageType: str
    count: int
    dataSize: Optional[int] = None


class DurationRange(BaseValidatorModel):
    minSeconds: Optional[int] = None
    maxSeconds: Optional[int] = None


class AssessmentRunNotification(BaseValidatorModel):
    date: datetime
    event: InspectorEventType
    error: bool
    message: Optional[str] = None
    snsTopicArn: Optional[str] = None
    snsPublishStatusCode: Optional[AssessmentRunNotificationSnsStatusCodeType] = None


class AssessmentRunStateChange(BaseValidatorModel):
    stateChangedAt: datetime
    state: AssessmentRunStateType


class AssessmentTargetFilter(BaseValidatorModel):
    assessmentTargetNamePattern: Optional[str] = None


class AssessmentTarget(BaseValidatorModel):
    arn: str
    name: str
    createdAt: datetime
    updatedAt: datetime
    resourceGroupArn: Optional[str] = None


class Tag(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class CreateAssessmentTargetRequest(BaseValidatorModel):
    assessmentTargetName: str
    resourceGroupArn: Optional[str] = None


class CreateExclusionsPreviewRequest(BaseValidatorModel):
    assessmentTemplateArn: str


class ResourceGroupTag(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class DeleteAssessmentRunRequest(BaseValidatorModel):
    assessmentRunArn: str


class DeleteAssessmentTargetRequest(BaseValidatorModel):
    assessmentTargetArn: str


class DeleteAssessmentTemplateRequest(BaseValidatorModel):
    assessmentTemplateArn: str


class DescribeAssessmentRunsRequest(BaseValidatorModel):
    assessmentRunArns: List[str]


class DescribeAssessmentTargetsRequest(BaseValidatorModel):
    assessmentTargetArns: List[str]


class DescribeAssessmentTemplatesRequest(BaseValidatorModel):
    assessmentTemplateArns: List[str]


class DescribeExclusionsRequest(BaseValidatorModel):
    exclusionArns: List[str]
    locale: Optional[Literal['EN_US']] = None


class DescribeFindingsRequest(BaseValidatorModel):
    findingArns: List[str]
    locale: Optional[Literal['EN_US']] = None


class DescribeResourceGroupsRequest(BaseValidatorModel):
    resourceGroupArns: List[str]


class DescribeRulesPackagesRequest(BaseValidatorModel):
    rulesPackageArns: List[str]
    locale: Optional[Literal['EN_US']] = None


class RulesPackage(BaseValidatorModel):
    arn: str
    name: str
    version: str
    provider: str
    description: Optional[str] = None


class EventSubscription(BaseValidatorModel):
    event: InspectorEventType
    subscribedAt: datetime


class Scope(BaseValidatorModel):
    key: Optional[ScopeTypeType] = None
    value: Optional[str] = None


class InspectorServiceAttributes(BaseValidatorModel):
    schemaVersion: int
    assessmentRunArn: Optional[str] = None
    rulesPackageArn: Optional[str] = None


class GetAssessmentReportRequest(BaseValidatorModel):
    assessmentRunArn: str
    reportFileFormat: ReportFileFormatType
    reportType: ReportTypeType


class GetExclusionsPreviewRequest(BaseValidatorModel):
    assessmentTemplateArn: str
    previewToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[Literal['EN_US']] = None


class GetTelemetryMetadataRequest(BaseValidatorModel):
    assessmentRunArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEventSubscriptionsRequest(BaseValidatorModel):
    resourceArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListExclusionsRequest(BaseValidatorModel):
    assessmentRunArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRulesPackagesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PrivateIp(BaseValidatorModel):
    privateDnsName: Optional[str] = None
    privateIpAddress: Optional[str] = None


class SecurityGroup(BaseValidatorModel):
    groupName: Optional[str] = None
    groupId: Optional[str] = None


class PreviewAgentsRequest(BaseValidatorModel):
    previewAgentsArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RegisterCrossAccountAccessRoleRequest(BaseValidatorModel):
    roleArn: str


class RemoveAttributesFromFindingsRequest(BaseValidatorModel):
    findingArns: List[str]
    attributeKeys: List[str]


class StartAssessmentRunRequest(BaseValidatorModel):
    assessmentTemplateArn: str
    assessmentRunName: Optional[str] = None


class StopAssessmentRunRequest(BaseValidatorModel):
    assessmentRunArn: str
    stopAction: Optional[StopActionType] = None


class SubscribeToEventRequest(BaseValidatorModel):
    resourceArn: str
    event: InspectorEventType
    topicArn: str

Timestamp = Union[datetime, str]


class UnsubscribeFromEventRequest(BaseValidatorModel):
    resourceArn: str
    event: InspectorEventType
    topicArn: str


class UpdateAssessmentTargetRequest(BaseValidatorModel):
    assessmentTargetArn: str
    assessmentTargetName: str
    resourceGroupArn: Optional[str] = None


class AddAttributesToFindingsRequest(BaseValidatorModel):
    findingArns: List[str]
    attributes: List[Attribute]


class AssessmentTemplate(BaseValidatorModel):
    arn: str
    name: str
    assessmentTargetArn: str
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List[Attribute]
    assessmentRunCount: int
    createdAt: datetime
    lastAssessmentRunArn: Optional[str] = None


class CreateAssessmentTemplateRequest(BaseValidatorModel):
    assessmentTargetArn: str
    assessmentTemplateName: str
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: Optional[List[Attribute]] = None


class AddAttributesToFindingsResponse(BaseValidatorModel):
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata


class CreateAssessmentTargetResponse(BaseValidatorModel):
    assessmentTargetArn: str
    ResponseMetadata: ResponseMetadata


class CreateAssessmentTemplateResponse(BaseValidatorModel):
    assessmentTemplateArn: str
    ResponseMetadata: ResponseMetadata


class CreateExclusionsPreviewResponse(BaseValidatorModel):
    previewToken: str
    ResponseMetadata: ResponseMetadata


class CreateResourceGroupResponse(BaseValidatorModel):
    resourceGroupArn: str
    ResponseMetadata: ResponseMetadata


class DescribeCrossAccountAccessRoleResponse(BaseValidatorModel):
    roleArn: str
    valid: bool
    registeredAt: datetime
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAssessmentReportResponse(BaseValidatorModel):
    status: ReportStatusType
    url: str
    ResponseMetadata: ResponseMetadata


class ListAssessmentRunsResponse(BaseValidatorModel):
    assessmentRunArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssessmentTargetsResponse(BaseValidatorModel):
    assessmentTargetArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssessmentTemplatesResponse(BaseValidatorModel):
    assessmentTemplateArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListExclusionsResponse(BaseValidatorModel):
    exclusionArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFindingsResponse(BaseValidatorModel):
    findingArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRulesPackagesResponse(BaseValidatorModel):
    rulesPackageArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RemoveAttributesFromFindingsResponse(BaseValidatorModel):
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata


class StartAssessmentRunResponse(BaseValidatorModel):
    assessmentRunArn: str
    ResponseMetadata: ResponseMetadata


class ListAssessmentRunAgentsRequest(BaseValidatorModel):
    assessmentRunArn: str
    filter: Optional[AgentFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PreviewAgentsResponse(BaseValidatorModel):
    agentPreviews: List[AgentPreview]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssessmentRunAgent(BaseValidatorModel):
    agentId: str
    assessmentRunArn: str
    agentHealth: AgentHealthType
    agentHealthCode: AgentHealthCodeType
    telemetryMetadata: List[TelemetryMetadata]
    agentHealthDetails: Optional[str] = None
    autoScalingGroup: Optional[str] = None


class GetTelemetryMetadataResponse(BaseValidatorModel):
    telemetryMetadata: List[TelemetryMetadata]
    ResponseMetadata: ResponseMetadata


class AssessmentTemplateFilter(BaseValidatorModel):
    namePattern: Optional[str] = None
    durationRange: Optional[DurationRange] = None
    rulesPackageArns: Optional[List[str]] = None


class AssessmentRun(BaseValidatorModel):
    arn: str
    name: str
    assessmentTemplateArn: str
    state: AssessmentRunStateType
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List[Attribute]
    createdAt: datetime
    stateChangedAt: datetime
    dataCollected: bool
    stateChanges: List[AssessmentRunStateChange]
    notifications: List[AssessmentRunNotification]
    findingCounts: Dict[SeverityType, int]
    startedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None


class ListAssessmentTargetsRequest(BaseValidatorModel):
    filter: Optional[AssessmentTargetFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeAssessmentTargetsResponse(BaseValidatorModel):
    assessmentTargets: List[AssessmentTarget]
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class SetTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Optional[List[Tag]] = None


class CreateResourceGroupRequest(BaseValidatorModel):
    resourceGroupTags: List[ResourceGroupTag]


class ResourceGroup(BaseValidatorModel):
    arn: str
    tags: List[ResourceGroupTag]
    createdAt: datetime


class DescribeRulesPackagesResponse(BaseValidatorModel):
    rulesPackages: List[RulesPackage]
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata


class Subscription(BaseValidatorModel):
    resourceArn: str
    topicArn: str
    eventSubscriptions: List[EventSubscription]


class ExclusionPreview(BaseValidatorModel):
    title: str
    description: str
    recommendation: str
    scopes: List[Scope]
    attributes: Optional[List[Attribute]] = None


class Exclusion(BaseValidatorModel):
    arn: str
    title: str
    description: str
    recommendation: str
    scopes: List[Scope]
    attributes: Optional[List[Attribute]] = None


class ListAssessmentRunAgentsRequestPaginate(BaseValidatorModel):
    assessmentRunArn: str
    filter: Optional[AgentFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssessmentTargetsRequestPaginate(BaseValidatorModel):
    filter: Optional[AssessmentTargetFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventSubscriptionsRequestPaginate(BaseValidatorModel):
    resourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExclusionsRequestPaginate(BaseValidatorModel):
    assessmentRunArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRulesPackagesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class PreviewAgentsRequestPaginate(BaseValidatorModel):
    previewAgentsArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class NetworkInterface(BaseValidatorModel):
    networkInterfaceId: Optional[str] = None
    subnetId: Optional[str] = None
    vpcId: Optional[str] = None
    privateDnsName: Optional[str] = None
    privateIpAddress: Optional[str] = None
    privateIpAddresses: Optional[List[PrivateIp]] = None
    publicDnsName: Optional[str] = None
    publicIp: Optional[str] = None
    ipv6Addresses: Optional[List[str]] = None
    securityGroups: Optional[List[SecurityGroup]] = None


class TimestampRange(BaseValidatorModel):
    beginDate: Optional[Timestamp] = None
    endDate: Optional[Timestamp] = None


class DescribeAssessmentTemplatesResponse(BaseValidatorModel):
    assessmentTemplates: List[AssessmentTemplate]
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata


class ListAssessmentRunAgentsResponse(BaseValidatorModel):
    assessmentRunAgents: List[AssessmentRunAgent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssessmentTemplatesRequestPaginate(BaseValidatorModel):
    assessmentTargetArns: Optional[List[str]] = None
    filter: Optional[AssessmentTemplateFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssessmentTemplatesRequest(BaseValidatorModel):
    assessmentTargetArns: Optional[List[str]] = None
    filter: Optional[AssessmentTemplateFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeAssessmentRunsResponse(BaseValidatorModel):
    assessmentRuns: List[AssessmentRun]
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata


class DescribeResourceGroupsResponse(BaseValidatorModel):
    resourceGroups: List[ResourceGroup]
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata


class ListEventSubscriptionsResponse(BaseValidatorModel):
    subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetExclusionsPreviewResponse(BaseValidatorModel):
    previewStatus: PreviewStatusType
    exclusionPreviews: List[ExclusionPreview]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeExclusionsResponse(BaseValidatorModel):
    exclusions: Dict[str, Exclusion]
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata


class AssetAttributes(BaseValidatorModel):
    schemaVersion: int
    agentId: Optional[str] = None
    autoScalingGroup: Optional[str] = None
    amiId: Optional[str] = None
    hostname: Optional[str] = None
    ipv4Addresses: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None


class AssessmentRunFilter(BaseValidatorModel):
    namePattern: Optional[str] = None
    states: Optional[List[AssessmentRunStateType]] = None
    durationRange: Optional[DurationRange] = None
    rulesPackageArns: Optional[List[str]] = None
    startTimeRange: Optional[TimestampRange] = None
    completionTimeRange: Optional[TimestampRange] = None
    stateChangeTimeRange: Optional[TimestampRange] = None


class FindingFilter(BaseValidatorModel):
    agentIds: Optional[List[str]] = None
    autoScalingGroups: Optional[List[str]] = None
    ruleNames: Optional[List[str]] = None
    severities: Optional[List[SeverityType]] = None
    rulesPackageArns: Optional[List[str]] = None
    attributes: Optional[List[Attribute]] = None
    userAttributes: Optional[List[Attribute]] = None
    creationTimeRange: Optional[TimestampRange] = None


class Finding(BaseValidatorModel):
    arn: str
    attributes: List[Attribute]
    userAttributes: List[Attribute]
    createdAt: datetime
    updatedAt: datetime
    schemaVersion: Optional[int] = None
    service: Optional[str] = None
    serviceAttributes: Optional[InspectorServiceAttributes] = None
    assetType: Optional[Literal['ec2-instance']] = None
    assetAttributes: Optional[AssetAttributes] = None
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    recommendation: Optional[str] = None
    severity: Optional[SeverityType] = None
    numericSeverity: Optional[float] = None
    confidence: Optional[int] = None
    indicatorOfCompromise: Optional[bool] = None


class ListAssessmentRunsRequestPaginate(BaseValidatorModel):
    assessmentTemplateArns: Optional[List[str]] = None
    filter: Optional[AssessmentRunFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssessmentRunsRequest(BaseValidatorModel):
    assessmentTemplateArns: Optional[List[str]] = None
    filter: Optional[AssessmentRunFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFindingsRequestPaginate(BaseValidatorModel):
    assessmentRunArns: Optional[List[str]] = None
    filter: Optional[FindingFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingsRequest(BaseValidatorModel):
    assessmentRunArns: Optional[List[str]] = None
    filter: Optional[FindingFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeFindingsResponse(BaseValidatorModel):
    findings: List[Finding]
    failedItems: Dict[str, FailedItemDetails]
    ResponseMetadata: ResponseMetadata
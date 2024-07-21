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
from aws_resource_validator.pydantic_models.inspector_constants import *

class AttributeTypeDef(BaseModel):
    key: str
    value: Optional[str] = None

class FailedItemDetailsTypeDef(BaseModel):
    failureCode: FailedItemErrorCodeType
    retryable: bool

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AgentFilterTypeDef(BaseModel):
    agentHealths: Sequence[AgentHealthType]
    agentHealthCodes: Sequence[AgentHealthCodeType]

class AgentPreviewTypeDef(BaseModel):
    agentId: str
    hostname: Optional[str] = None
    autoScalingGroup: Optional[str] = None
    agentHealth: Optional[AgentHealthType] = None
    agentVersion: Optional[str] = None
    operatingSystem: Optional[str] = None
    kernelVersion: Optional[str] = None
    ipv4Address: Optional[str] = None

class TelemetryMetadataTypeDef(BaseModel):
    messageType: str
    count: int
    dataSize: Optional[int] = None

class DurationRangeTypeDef(BaseModel):
    minSeconds: Optional[int] = None
    maxSeconds: Optional[int] = None

class AssessmentRunNotificationTypeDef(BaseModel):
    date: datetime
    event: InspectorEventType
    error: bool
    message: Optional[str] = None
    snsTopicArn: Optional[str] = None
    snsPublishStatusCode: Optional[AssessmentRunNotificationSnsStatusCodeType] = None

class AssessmentRunStateChangeTypeDef(BaseModel):
    stateChangedAt: datetime
    state: AssessmentRunStateType

class AssessmentTargetFilterTypeDef(BaseModel):
    assessmentTargetNamePattern: Optional[str] = None

class AssessmentTargetTypeDef(BaseModel):
    arn: str
    name: str
    createdAt: datetime
    updatedAt: datetime
    resourceGroupArn: Optional[str] = None

class TagTypeDef(BaseModel):
    key: str
    value: Optional[str] = None

class CreateAssessmentTargetRequestRequestTypeDef(BaseModel):
    assessmentTargetName: str
    resourceGroupArn: Optional[str] = None

class CreateExclusionsPreviewRequestRequestTypeDef(BaseModel):
    assessmentTemplateArn: str

class ResourceGroupTagTypeDef(BaseModel):
    key: str
    value: Optional[str] = None

class DeleteAssessmentRunRequestRequestTypeDef(BaseModel):
    assessmentRunArn: str

class DeleteAssessmentTargetRequestRequestTypeDef(BaseModel):
    assessmentTargetArn: str

class DeleteAssessmentTemplateRequestRequestTypeDef(BaseModel):
    assessmentTemplateArn: str

class DescribeAssessmentRunsRequestRequestTypeDef(BaseModel):
    assessmentRunArns: Sequence[str]

class DescribeAssessmentTargetsRequestRequestTypeDef(BaseModel):
    assessmentTargetArns: Sequence[str]

class DescribeAssessmentTemplatesRequestRequestTypeDef(BaseModel):
    assessmentTemplateArns: Sequence[str]

class DescribeExclusionsRequestRequestTypeDef(BaseModel):
    exclusionArns: Sequence[str]
    locale: Optional[Literal["EN_US"]] = None

class DescribeFindingsRequestRequestTypeDef(BaseModel):
    findingArns: Sequence[str]
    locale: Optional[Literal["EN_US"]] = None

class DescribeResourceGroupsRequestRequestTypeDef(BaseModel):
    resourceGroupArns: Sequence[str]

class DescribeRulesPackagesRequestRequestTypeDef(BaseModel):
    rulesPackageArns: Sequence[str]
    locale: Optional[Literal["EN_US"]] = None

class RulesPackageTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    provider: str
    description: Optional[str] = None

class EventSubscriptionTypeDef(BaseModel):
    event: InspectorEventType
    subscribedAt: datetime

class ScopeTypeDef(BaseModel):
    key: Optional[ScopeTypeType] = None
    value: Optional[str] = None

class InspectorServiceAttributesTypeDef(BaseModel):
    schemaVersion: int
    assessmentRunArn: Optional[str] = None
    rulesPackageArn: Optional[str] = None

class GetAssessmentReportRequestRequestTypeDef(BaseModel):
    assessmentRunArn: str
    reportFileFormat: ReportFileFormatType
    reportType: ReportTypeType

class GetExclusionsPreviewRequestRequestTypeDef(BaseModel):
    assessmentTemplateArn: str
    previewToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[Literal["EN_US"]] = None

class GetTelemetryMetadataRequestRequestTypeDef(BaseModel):
    assessmentRunArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEventSubscriptionsRequestRequestTypeDef(BaseModel):
    resourceArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListExclusionsRequestRequestTypeDef(BaseModel):
    assessmentRunArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListRulesPackagesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PrivateIpTypeDef(BaseModel):
    privateDnsName: Optional[str] = None
    privateIpAddress: Optional[str] = None

class SecurityGroupTypeDef(BaseModel):
    groupName: Optional[str] = None
    groupId: Optional[str] = None

class PreviewAgentsRequestRequestTypeDef(BaseModel):
    previewAgentsArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RegisterCrossAccountAccessRoleRequestRequestTypeDef(BaseModel):
    roleArn: str

class RemoveAttributesFromFindingsRequestRequestTypeDef(BaseModel):
    findingArns: Sequence[str]
    attributeKeys: Sequence[str]

class StartAssessmentRunRequestRequestTypeDef(BaseModel):
    assessmentTemplateArn: str
    assessmentRunName: Optional[str] = None

class StopAssessmentRunRequestRequestTypeDef(BaseModel):
    assessmentRunArn: str
    stopAction: Optional[StopActionType] = None

class SubscribeToEventRequestRequestTypeDef(BaseModel):
    resourceArn: str
    event: InspectorEventType
    topicArn: str

class UnsubscribeFromEventRequestRequestTypeDef(BaseModel):
    resourceArn: str
    event: InspectorEventType
    topicArn: str

class UpdateAssessmentTargetRequestRequestTypeDef(BaseModel):
    assessmentTargetArn: str
    assessmentTargetName: str
    resourceGroupArn: Optional[str] = None

class AddAttributesToFindingsRequestRequestTypeDef(BaseModel):
    findingArns: Sequence[str]
    attributes: Sequence[AttributeTypeDef]

class AssessmentTemplateTypeDef(BaseModel):
    arn: str
    name: str
    assessmentTargetArn: str
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List[AttributeTypeDef]
    assessmentRunCount: int
    createdAt: datetime
    lastAssessmentRunArn: Optional[str] = None

class CreateAssessmentTemplateRequestRequestTypeDef(BaseModel):
    assessmentTargetArn: str
    assessmentTemplateName: str
    durationInSeconds: int
    rulesPackageArns: Sequence[str]
    userAttributesForFindings: Optional[Sequence[AttributeTypeDef]] = None

class AddAttributesToFindingsResponseTypeDef(BaseModel):
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentTargetResponseTypeDef(BaseModel):
    assessmentTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentTemplateResponseTypeDef(BaseModel):
    assessmentTemplateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExclusionsPreviewResponseTypeDef(BaseModel):
    previewToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceGroupResponseTypeDef(BaseModel):
    resourceGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCrossAccountAccessRoleResponseTypeDef(BaseModel):
    roleArn: str
    valid: bool
    registeredAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentReportResponseTypeDef(BaseModel):
    status: ReportStatusType
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentRunsResponseTypeDef(BaseModel):
    assessmentRunArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentTargetsResponseTypeDef(BaseModel):
    assessmentTargetArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentTemplatesResponseTypeDef(BaseModel):
    assessmentTemplateArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListExclusionsResponseTypeDef(BaseModel):
    exclusionArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsResponseTypeDef(BaseModel):
    findingArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesPackagesResponseTypeDef(BaseModel):
    rulesPackageArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveAttributesFromFindingsResponseTypeDef(BaseModel):
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentRunResponseTypeDef(BaseModel):
    assessmentRunArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentRunAgentsRequestRequestTypeDef(BaseModel):
    assessmentRunArn: str
    filter: Optional[AgentFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PreviewAgentsResponseTypeDef(BaseModel):
    agentPreviews: List[AgentPreviewTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentRunAgentTypeDef(BaseModel):
    agentId: str
    assessmentRunArn: str
    agentHealth: AgentHealthType
    agentHealthCode: AgentHealthCodeType
    telemetryMetadata: List[TelemetryMetadataTypeDef]
    agentHealthDetails: Optional[str] = None
    autoScalingGroup: Optional[str] = None

class GetTelemetryMetadataResponseTypeDef(BaseModel):
    telemetryMetadata: List[TelemetryMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentTemplateFilterTypeDef(BaseModel):
    namePattern: Optional[str] = None
    durationRange: Optional[DurationRangeTypeDef] = None
    rulesPackageArns: Optional[Sequence[str]] = None

class AssessmentRunTypeDef(BaseModel):
    arn: str
    name: str
    assessmentTemplateArn: str
    state: AssessmentRunStateType
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List[AttributeTypeDef]
    createdAt: datetime
    stateChangedAt: datetime
    dataCollected: bool
    stateChanges: List[AssessmentRunStateChangeTypeDef]
    notifications: List[AssessmentRunNotificationTypeDef]
    findingCounts: Dict[SeverityType, int]
    startedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None

class ListAssessmentTargetsRequestRequestTypeDef(BaseModel):
    filter: Optional[AssessmentTargetFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeAssessmentTargetsResponseTypeDef(BaseModel):
    assessmentTargets: List[AssessmentTargetTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateResourceGroupRequestRequestTypeDef(BaseModel):
    resourceGroupTags: Sequence[ResourceGroupTagTypeDef]

class ResourceGroupTypeDef(BaseModel):
    arn: str
    tags: List[ResourceGroupTagTypeDef]
    createdAt: datetime

class DescribeRulesPackagesResponseTypeDef(BaseModel):
    rulesPackages: List[RulesPackageTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionTypeDef(BaseModel):
    resourceArn: str
    topicArn: str
    eventSubscriptions: List[EventSubscriptionTypeDef]

class ExclusionPreviewTypeDef(BaseModel):
    title: str
    description: str
    recommendation: str
    scopes: List[ScopeTypeDef]
    attributes: Optional[List[AttributeTypeDef]] = None

class ExclusionTypeDef(BaseModel):
    arn: str
    title: str
    description: str
    recommendation: str
    scopes: List[ScopeTypeDef]
    attributes: Optional[List[AttributeTypeDef]] = None

class ListAssessmentRunAgentsRequestListAssessmentRunAgentsPaginateTypeDef(BaseModel):
    assessmentRunArn: str
    filter: Optional[AgentFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssessmentTargetsRequestListAssessmentTargetsPaginateTypeDef(BaseModel):
    filter: Optional[AssessmentTargetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventSubscriptionsRequestListEventSubscriptionsPaginateTypeDef(BaseModel):
    resourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExclusionsRequestListExclusionsPaginateTypeDef(BaseModel):
    assessmentRunArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesPackagesRequestListRulesPackagesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PreviewAgentsRequestPreviewAgentsPaginateTypeDef(BaseModel):
    previewAgentsArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class NetworkInterfaceTypeDef(BaseModel):
    networkInterfaceId: Optional[str] = None
    subnetId: Optional[str] = None
    vpcId: Optional[str] = None
    privateDnsName: Optional[str] = None
    privateIpAddress: Optional[str] = None
    privateIpAddresses: Optional[List[PrivateIpTypeDef]] = None
    publicDnsName: Optional[str] = None
    publicIp: Optional[str] = None
    ipv6Addresses: Optional[List[str]] = None
    securityGroups: Optional[List[SecurityGroupTypeDef]] = None

class TimestampRangeTypeDef(BaseModel):
    beginDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None

class DescribeAssessmentTemplatesResponseTypeDef(BaseModel):
    assessmentTemplates: List[AssessmentTemplateTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentRunAgentsResponseTypeDef(BaseModel):
    assessmentRunAgents: List[AssessmentRunAgentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentTemplatesRequestListAssessmentTemplatesPaginateTypeDef(BaseModel):
    assessmentTargetArns: Optional[Sequence[str]] = None
    filter: Optional[AssessmentTemplateFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssessmentTemplatesRequestRequestTypeDef(BaseModel):
    assessmentTargetArns: Optional[Sequence[str]] = None
    filter: Optional[AssessmentTemplateFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeAssessmentRunsResponseTypeDef(BaseModel):
    assessmentRuns: List[AssessmentRunTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceGroupsResponseTypeDef(BaseModel):
    resourceGroups: List[ResourceGroupTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventSubscriptionsResponseTypeDef(BaseModel):
    subscriptions: List[SubscriptionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetExclusionsPreviewResponseTypeDef(BaseModel):
    previewStatus: PreviewStatusType
    exclusionPreviews: List[ExclusionPreviewTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExclusionsResponseTypeDef(BaseModel):
    exclusions: Dict[str, ExclusionTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssetAttributesTypeDef(BaseModel):
    schemaVersion: int
    agentId: Optional[str] = None
    autoScalingGroup: Optional[str] = None
    amiId: Optional[str] = None
    hostname: Optional[str] = None
    ipv4Addresses: Optional[List[str]] = None
    tags: Optional[List[TagTypeDef]] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None

class AssessmentRunFilterTypeDef(BaseModel):
    namePattern: Optional[str] = None
    states: Optional[Sequence[AssessmentRunStateType]] = None
    durationRange: Optional[DurationRangeTypeDef] = None
    rulesPackageArns: Optional[Sequence[str]] = None
    startTimeRange: Optional[TimestampRangeTypeDef] = None
    completionTimeRange: Optional[TimestampRangeTypeDef] = None
    stateChangeTimeRange: Optional[TimestampRangeTypeDef] = None

class FindingFilterTypeDef(BaseModel):
    agentIds: Optional[Sequence[str]] = None
    autoScalingGroups: Optional[Sequence[str]] = None
    ruleNames: Optional[Sequence[str]] = None
    severities: Optional[Sequence[SeverityType]] = None
    rulesPackageArns: Optional[Sequence[str]] = None
    attributes: Optional[Sequence[AttributeTypeDef]] = None
    userAttributes: Optional[Sequence[AttributeTypeDef]] = None
    creationTimeRange: Optional[TimestampRangeTypeDef] = None

class FindingTypeDef(BaseModel):
    arn: str
    attributes: List[AttributeTypeDef]
    userAttributes: List[AttributeTypeDef]
    createdAt: datetime
    updatedAt: datetime
    schemaVersion: Optional[int] = None
    service: Optional[str] = None
    serviceAttributes: Optional[InspectorServiceAttributesTypeDef] = None
    assetType: Optional[Literal["ec2-instance"]] = None
    assetAttributes: Optional[AssetAttributesTypeDef] = None
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    recommendation: Optional[str] = None
    severity: Optional[SeverityType] = None
    numericSeverity: Optional[float] = None
    confidence: Optional[int] = None
    indicatorOfCompromise: Optional[bool] = None

class ListAssessmentRunsRequestListAssessmentRunsPaginateTypeDef(BaseModel):
    assessmentTemplateArns: Optional[Sequence[str]] = None
    filter: Optional[AssessmentRunFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssessmentRunsRequestRequestTypeDef(BaseModel):
    assessmentTemplateArns: Optional[Sequence[str]] = None
    filter: Optional[AssessmentRunFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFindingsRequestListFindingsPaginateTypeDef(BaseModel):
    assessmentRunArns: Optional[Sequence[str]] = None
    filter: Optional[FindingFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsRequestRequestTypeDef(BaseModel):
    assessmentRunArns: Optional[Sequence[str]] = None
    filter: Optional[FindingFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeFindingsResponseTypeDef(BaseModel):
    findings: List[FindingTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


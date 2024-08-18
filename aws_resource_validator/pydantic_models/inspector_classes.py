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
from aws_resource_validator.pydantic_models.inspector_constants import *

class AttributeTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None

class FailedItemDetailsTypeDef(BaseValidatorModel):
    failureCode: FailedItemErrorCodeType
    retryable: bool

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AgentFilterTypeDef(BaseValidatorModel):
    agentHealths: Sequence[AgentHealthType]
    agentHealthCodes: Sequence[AgentHealthCodeType]

class AgentPreviewTypeDef(BaseValidatorModel):
    agentId: str
    hostname: Optional[str] = None
    autoScalingGroup: Optional[str] = None
    agentHealth: Optional[AgentHealthType] = None
    agentVersion: Optional[str] = None
    operatingSystem: Optional[str] = None
    kernelVersion: Optional[str] = None
    ipv4Address: Optional[str] = None

class TelemetryMetadataTypeDef(BaseValidatorModel):
    messageType: str
    count: int
    dataSize: Optional[int] = None

class DurationRangeTypeDef(BaseValidatorModel):
    minSeconds: Optional[int] = None
    maxSeconds: Optional[int] = None

class AssessmentRunNotificationTypeDef(BaseValidatorModel):
    date: datetime
    event: InspectorEventType
    error: bool
    message: Optional[str] = None
    snsTopicArn: Optional[str] = None
    snsPublishStatusCode: Optional[AssessmentRunNotificationSnsStatusCodeType] = None

class AssessmentRunStateChangeTypeDef(BaseValidatorModel):
    stateChangedAt: datetime
    state: AssessmentRunStateType

class AssessmentTargetFilterTypeDef(BaseValidatorModel):
    assessmentTargetNamePattern: Optional[str] = None

class AssessmentTargetTypeDef(BaseValidatorModel):
    arn: str
    name: str
    createdAt: datetime
    updatedAt: datetime
    resourceGroupArn: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None

class CreateAssessmentTargetRequestRequestTypeDef(BaseValidatorModel):
    assessmentTargetName: str
    resourceGroupArn: Optional[str] = None

class CreateExclusionsPreviewRequestRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str

class ResourceGroupTagTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None

class DeleteAssessmentRunRequestRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str

class DeleteAssessmentTargetRequestRequestTypeDef(BaseValidatorModel):
    assessmentTargetArn: str

class DeleteAssessmentTemplateRequestRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str

class DescribeAssessmentRunsRequestRequestTypeDef(BaseValidatorModel):
    assessmentRunArns: Sequence[str]

class DescribeAssessmentTargetsRequestRequestTypeDef(BaseValidatorModel):
    assessmentTargetArns: Sequence[str]

class DescribeAssessmentTemplatesRequestRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArns: Sequence[str]

class DescribeExclusionsRequestRequestTypeDef(BaseValidatorModel):
    exclusionArns: Sequence[str]
    locale: Optional[Literal["EN_US"]] = None

class DescribeFindingsRequestRequestTypeDef(BaseValidatorModel):
    findingArns: Sequence[str]
    locale: Optional[Literal["EN_US"]] = None

class DescribeResourceGroupsRequestRequestTypeDef(BaseValidatorModel):
    resourceGroupArns: Sequence[str]

class DescribeRulesPackagesRequestRequestTypeDef(BaseValidatorModel):
    rulesPackageArns: Sequence[str]
    locale: Optional[Literal["EN_US"]] = None

class RulesPackageTypeDef(BaseValidatorModel):
    arn: str
    name: str
    version: str
    provider: str
    description: Optional[str] = None

class EventSubscriptionTypeDef(BaseValidatorModel):
    event: InspectorEventType
    subscribedAt: datetime

class ScopeTypeDef(BaseValidatorModel):
    key: Optional[ScopeTypeType] = None
    value: Optional[str] = None

class InspectorServiceAttributesTypeDef(BaseValidatorModel):
    schemaVersion: int
    assessmentRunArn: Optional[str] = None
    rulesPackageArn: Optional[str] = None

class GetAssessmentReportRequestRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    reportFileFormat: ReportFileFormatType
    reportType: ReportTypeType

class GetExclusionsPreviewRequestRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str
    previewToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[Literal["EN_US"]] = None

class GetTelemetryMetadataRequestRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEventSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListExclusionsRequestRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListRulesPackagesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class PrivateIpTypeDef(BaseValidatorModel):
    privateDnsName: Optional[str] = None
    privateIpAddress: Optional[str] = None

class SecurityGroupTypeDef(BaseValidatorModel):
    groupName: Optional[str] = None
    groupId: Optional[str] = None

class PreviewAgentsRequestRequestTypeDef(BaseValidatorModel):
    previewAgentsArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RegisterCrossAccountAccessRoleRequestRequestTypeDef(BaseValidatorModel):
    roleArn: str

class RemoveAttributesFromFindingsRequestRequestTypeDef(BaseValidatorModel):
    findingArns: Sequence[str]
    attributeKeys: Sequence[str]

class StartAssessmentRunRequestRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str
    assessmentRunName: Optional[str] = None

class StopAssessmentRunRequestRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    stopAction: Optional[StopActionType] = None

class SubscribeToEventRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    event: InspectorEventType
    topicArn: str

class UnsubscribeFromEventRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    event: InspectorEventType
    topicArn: str

class UpdateAssessmentTargetRequestRequestTypeDef(BaseValidatorModel):
    assessmentTargetArn: str
    assessmentTargetName: str
    resourceGroupArn: Optional[str] = None

class AddAttributesToFindingsRequestRequestTypeDef(BaseValidatorModel):
    findingArns: Sequence[str]
    attributes: Sequence[AttributeTypeDef]

class AssessmentTemplateTypeDef(BaseValidatorModel):
    arn: str
    name: str
    assessmentTargetArn: str
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List[AttributeTypeDef]
    assessmentRunCount: int
    createdAt: datetime
    lastAssessmentRunArn: Optional[str] = None

class CreateAssessmentTemplateRequestRequestTypeDef(BaseValidatorModel):
    assessmentTargetArn: str
    assessmentTemplateName: str
    durationInSeconds: int
    rulesPackageArns: Sequence[str]
    userAttributesForFindings: Optional[Sequence[AttributeTypeDef]] = None

class AddAttributesToFindingsResponseTypeDef(BaseValidatorModel):
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentTargetResponseTypeDef(BaseValidatorModel):
    assessmentTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentTemplateResponseTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExclusionsPreviewResponseTypeDef(BaseValidatorModel):
    previewToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceGroupResponseTypeDef(BaseValidatorModel):
    resourceGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCrossAccountAccessRoleResponseTypeDef(BaseValidatorModel):
    roleArn: str
    valid: bool
    registeredAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentReportResponseTypeDef(BaseValidatorModel):
    status: ReportStatusType
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentRunsResponseTypeDef(BaseValidatorModel):
    assessmentRunArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentTargetsResponseTypeDef(BaseValidatorModel):
    assessmentTargetArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentTemplatesResponseTypeDef(BaseValidatorModel):
    assessmentTemplateArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListExclusionsResponseTypeDef(BaseValidatorModel):
    exclusionArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsResponseTypeDef(BaseValidatorModel):
    findingArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesPackagesResponseTypeDef(BaseValidatorModel):
    rulesPackageArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveAttributesFromFindingsResponseTypeDef(BaseValidatorModel):
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentRunResponseTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentRunAgentsRequestRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    filter: Optional[AgentFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PreviewAgentsResponseTypeDef(BaseValidatorModel):
    agentPreviews: List[AgentPreviewTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentRunAgentTypeDef(BaseValidatorModel):
    agentId: str
    assessmentRunArn: str
    agentHealth: AgentHealthType
    agentHealthCode: AgentHealthCodeType
    telemetryMetadata: List[TelemetryMetadataTypeDef]
    agentHealthDetails: Optional[str] = None
    autoScalingGroup: Optional[str] = None

class GetTelemetryMetadataResponseTypeDef(BaseValidatorModel):
    telemetryMetadata: List[TelemetryMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentTemplateFilterTypeDef(BaseValidatorModel):
    namePattern: Optional[str] = None
    durationRange: Optional[DurationRangeTypeDef] = None
    rulesPackageArns: Optional[Sequence[str]] = None

class AssessmentRunTypeDef(BaseValidatorModel):
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

class ListAssessmentTargetsRequestRequestTypeDef(BaseValidatorModel):
    filter: Optional[AssessmentTargetFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeAssessmentTargetsResponseTypeDef(BaseValidatorModel):
    assessmentTargets: List[AssessmentTargetTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateResourceGroupRequestRequestTypeDef(BaseValidatorModel):
    resourceGroupTags: Sequence[ResourceGroupTagTypeDef]

class ResourceGroupTypeDef(BaseValidatorModel):
    arn: str
    tags: List[ResourceGroupTagTypeDef]
    createdAt: datetime

class DescribeRulesPackagesResponseTypeDef(BaseValidatorModel):
    rulesPackages: List[RulesPackageTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionTypeDef(BaseValidatorModel):
    resourceArn: str
    topicArn: str
    eventSubscriptions: List[EventSubscriptionTypeDef]

class ExclusionPreviewTypeDef(BaseValidatorModel):
    title: str
    description: str
    recommendation: str
    scopes: List[ScopeTypeDef]
    attributes: Optional[List[AttributeTypeDef]] = None

class ExclusionTypeDef(BaseValidatorModel):
    arn: str
    title: str
    description: str
    recommendation: str
    scopes: List[ScopeTypeDef]
    attributes: Optional[List[AttributeTypeDef]] = None

class ListAssessmentRunAgentsRequestListAssessmentRunAgentsPaginateTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    filter: Optional[AgentFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssessmentTargetsRequestListAssessmentTargetsPaginateTypeDef(BaseValidatorModel):
    filter: Optional[AssessmentTargetFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventSubscriptionsRequestListEventSubscriptionsPaginateTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExclusionsRequestListExclusionsPaginateTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesPackagesRequestListRulesPackagesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PreviewAgentsRequestPreviewAgentsPaginateTypeDef(BaseValidatorModel):
    previewAgentsArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class NetworkInterfaceTypeDef(BaseValidatorModel):
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

class TimestampRangeTypeDef(BaseValidatorModel):
    beginDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None

class DescribeAssessmentTemplatesResponseTypeDef(BaseValidatorModel):
    assessmentTemplates: List[AssessmentTemplateTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentRunAgentsResponseTypeDef(BaseValidatorModel):
    assessmentRunAgents: List[AssessmentRunAgentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentTemplatesRequestListAssessmentTemplatesPaginateTypeDef(BaseValidatorModel):
    assessmentTargetArns: Optional[Sequence[str]] = None
    filter: Optional[AssessmentTemplateFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssessmentTemplatesRequestRequestTypeDef(BaseValidatorModel):
    assessmentTargetArns: Optional[Sequence[str]] = None
    filter: Optional[AssessmentTemplateFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeAssessmentRunsResponseTypeDef(BaseValidatorModel):
    assessmentRuns: List[AssessmentRunTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceGroupsResponseTypeDef(BaseValidatorModel):
    resourceGroups: List[ResourceGroupTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventSubscriptionsResponseTypeDef(BaseValidatorModel):
    subscriptions: List[SubscriptionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetExclusionsPreviewResponseTypeDef(BaseValidatorModel):
    previewStatus: PreviewStatusType
    exclusionPreviews: List[ExclusionPreviewTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExclusionsResponseTypeDef(BaseValidatorModel):
    exclusions: Dict[str, ExclusionTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssetAttributesTypeDef(BaseValidatorModel):
    schemaVersion: int
    agentId: Optional[str] = None
    autoScalingGroup: Optional[str] = None
    amiId: Optional[str] = None
    hostname: Optional[str] = None
    ipv4Addresses: Optional[List[str]] = None
    tags: Optional[List[TagTypeDef]] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None

class AssessmentRunFilterTypeDef(BaseValidatorModel):
    namePattern: Optional[str] = None
    states: Optional[Sequence[AssessmentRunStateType]] = None
    durationRange: Optional[DurationRangeTypeDef] = None
    rulesPackageArns: Optional[Sequence[str]] = None
    startTimeRange: Optional[TimestampRangeTypeDef] = None
    completionTimeRange: Optional[TimestampRangeTypeDef] = None
    stateChangeTimeRange: Optional[TimestampRangeTypeDef] = None

class FindingFilterTypeDef(BaseValidatorModel):
    agentIds: Optional[Sequence[str]] = None
    autoScalingGroups: Optional[Sequence[str]] = None
    ruleNames: Optional[Sequence[str]] = None
    severities: Optional[Sequence[SeverityType]] = None
    rulesPackageArns: Optional[Sequence[str]] = None
    attributes: Optional[Sequence[AttributeTypeDef]] = None
    userAttributes: Optional[Sequence[AttributeTypeDef]] = None
    creationTimeRange: Optional[TimestampRangeTypeDef] = None

class FindingTypeDef(BaseValidatorModel):
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

class ListAssessmentRunsRequestListAssessmentRunsPaginateTypeDef(BaseValidatorModel):
    assessmentTemplateArns: Optional[Sequence[str]] = None
    filter: Optional[AssessmentRunFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssessmentRunsRequestRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArns: Optional[Sequence[str]] = None
    filter: Optional[AssessmentRunFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFindingsRequestListFindingsPaginateTypeDef(BaseValidatorModel):
    assessmentRunArns: Optional[Sequence[str]] = None
    filter: Optional[FindingFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsRequestRequestTypeDef(BaseValidatorModel):
    assessmentRunArns: Optional[Sequence[str]] = None
    filter: Optional[FindingFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[FindingTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.inspector_constants import *

class AttributeTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class FailedItemDetailsTypeDef(BaseValidatorModel):
    failureCode: FailedItemErrorCodeType
    retryable: bool


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class CreateAssessmentTargetRequestTypeDef(BaseValidatorModel):
    assessmentTargetName: str
    resourceGroupArn: Optional[str] = None


class CreateExclusionsPreviewRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str


class ResourceGroupTagTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class DeleteAssessmentRunRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str


class DeleteAssessmentTargetRequestTypeDef(BaseValidatorModel):
    assessmentTargetArn: str


class DeleteAssessmentTemplateRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str


class DescribeAssessmentRunsRequestTypeDef(BaseValidatorModel):
    assessmentRunArns: Sequence[str]


class DescribeAssessmentTargetsRequestTypeDef(BaseValidatorModel):
    assessmentTargetArns: Sequence[str]


class DescribeAssessmentTemplatesRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArns: Sequence[str]


class DescribeExclusionsRequestTypeDef(BaseValidatorModel):
    exclusionArns: Sequence[str]
    locale: Optional[Literal["EN_US"]] = None


class DescribeFindingsRequestTypeDef(BaseValidatorModel):
    findingArns: Sequence[str]
    locale: Optional[Literal["EN_US"]] = None


class DescribeResourceGroupsRequestTypeDef(BaseValidatorModel):
    resourceGroupArns: Sequence[str]


class DescribeRulesPackagesRequestTypeDef(BaseValidatorModel):
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


class GetAssessmentReportRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    reportFileFormat: ReportFileFormatType
    reportType: ReportTypeType


class GetExclusionsPreviewRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str
    previewToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[Literal["EN_US"]] = None


class GetTelemetryMetadataRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEventSubscriptionsRequestTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListExclusionsRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRulesPackagesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PrivateIpTypeDef(BaseValidatorModel):
    privateDnsName: Optional[str] = None
    privateIpAddress: Optional[str] = None


class SecurityGroupTypeDef(BaseValidatorModel):
    groupName: Optional[str] = None
    groupId: Optional[str] = None


class PreviewAgentsRequestTypeDef(BaseValidatorModel):
    previewAgentsArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RegisterCrossAccountAccessRoleRequestTypeDef(BaseValidatorModel):
    roleArn: str


class RemoveAttributesFromFindingsRequestTypeDef(BaseValidatorModel):
    findingArns: Sequence[str]
    attributeKeys: Sequence[str]


class StartAssessmentRunRequestTypeDef(BaseValidatorModel):
    assessmentTemplateArn: str
    assessmentRunName: Optional[str] = None


class StopAssessmentRunRequestTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    stopAction: Optional[StopActionType] = None


class SubscribeToEventRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    event: InspectorEventType
    topicArn: str


class UnsubscribeFromEventRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    event: InspectorEventType
    topicArn: str


class UpdateAssessmentTargetRequestTypeDef(BaseValidatorModel):
    assessmentTargetArn: str
    assessmentTargetName: str
    resourceGroupArn: Optional[str] = None


class AddAttributesToFindingsRequestTypeDef(BaseValidatorModel):
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


class CreateAssessmentTemplateRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAssessmentTargetsResponseTypeDef(BaseValidatorModel):
    assessmentTargetArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAssessmentTemplatesResponseTypeDef(BaseValidatorModel):
    assessmentTemplateArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListExclusionsResponseTypeDef(BaseValidatorModel):
    exclusionArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListFindingsResponseTypeDef(BaseValidatorModel):
    findingArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRulesPackagesResponseTypeDef(BaseValidatorModel):
    rulesPackageArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RemoveAttributesFromFindingsResponseTypeDef(BaseValidatorModel):
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartAssessmentRunResponseTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PreviewAgentsResponseTypeDef(BaseValidatorModel):
    agentPreviews: List[AgentPreviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class DescribeAssessmentTargetsResponseTypeDef(BaseValidatorModel):
    assessmentTargets: List[AssessmentTargetTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SetTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateResourceGroupRequestTypeDef(BaseValidatorModel):
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


class ListEventSubscriptionsRequestPaginateTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExclusionsRequestPaginateTypeDef(BaseValidatorModel):
    assessmentRunArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRulesPackagesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PreviewAgentsRequestPaginateTypeDef(BaseValidatorModel):
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


class TimestampTypeDef(BaseValidatorModel):
    pass


class TimestampRangeTypeDef(BaseValidatorModel):
    beginDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None


class DescribeAssessmentTemplatesResponseTypeDef(BaseValidatorModel):
    assessmentTemplates: List[AssessmentTemplateTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAssessmentRunAgentsResponseTypeDef(BaseValidatorModel):
    assessmentRunAgents: List[AssessmentRunAgentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetExclusionsPreviewResponseTypeDef(BaseValidatorModel):
    previewStatus: PreviewStatusType
    exclusionPreviews: List[ExclusionPreviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    pass


class DescribeFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[FindingTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef



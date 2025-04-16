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
from aws_resource_validator.pydantic_models.ssm_incidents_constants import *

class AddRegionAction(BaseValidatorModel):
    regionName: str
    sseKmsKeyId: Optional[str] = None


class AttributeValueList(BaseValidatorModel):
    integerValues: Optional[Sequence[int]] = None
    stringValues: Optional[Sequence[str]] = None


class AutomationExecution(BaseValidatorModel):
    ssmExecutionArn: Optional[str] = None


class BatchGetIncidentFindingsError(BaseValidatorModel):
    code: str
    findingId: str
    message: str


class BatchGetIncidentFindingsInput(BaseValidatorModel):
    findingIds: Sequence[str]
    incidentRecordArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ChatChannelOutput(BaseValidatorModel):
    chatbotSns: Optional[List[str]] = None
    empty: Optional[Dict[str, Any]] = None


class ChatChannel(BaseValidatorModel):
    chatbotSns: Optional[Sequence[str]] = None
    empty: Optional[Mapping[str, Any]] = None


class CloudFormationStackUpdate(BaseValidatorModel):
    stackArn: str
    startTime: datetime
    endTime: Optional[datetime] = None


class CodeDeployDeployment(BaseValidatorModel):
    deploymentGroupArn: str
    deploymentId: str
    startTime: datetime
    endTime: Optional[datetime] = None


class RegionMapInputValue(BaseValidatorModel):
    sseKmsKeyId: Optional[str] = None


class EventReference(BaseValidatorModel):
    relatedItemId: Optional[str] = None
    resource: Optional[str] = None


class DeleteIncidentRecordInput(BaseValidatorModel):
    arn: str


class DeleteRegionAction(BaseValidatorModel):
    regionName: str


class DeleteReplicationSetInput(BaseValidatorModel):
    arn: str


class DeleteResourcePolicyInput(BaseValidatorModel):
    policyId: str
    resourceArn: str


class DeleteResponsePlanInput(BaseValidatorModel):
    arn: str


class DeleteTimelineEventInput(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str


class DynamicSsmParameterValue(BaseValidatorModel):
    variable: Optional[VariableTypeType] = None


class GetIncidentRecordInput(BaseValidatorModel):
    arn: str


class GetReplicationSetInput(BaseValidatorModel):
    arn: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetResourcePoliciesInput(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ResourcePolicy(BaseValidatorModel):
    policyDocument: str
    policyId: str
    ramResourceShareRegion: str


class GetResponsePlanInput(BaseValidatorModel):
    arn: str


class GetTimelineEventInput(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str


class IncidentRecordSource(BaseValidatorModel):
    createdBy: str
    source: str
    invokedBy: Optional[str] = None
    resourceArn: Optional[str] = None


class NotificationTargetItem(BaseValidatorModel):
    snsTopicArn: Optional[str] = None


class ListIncidentFindingsInput(BaseValidatorModel):
    incidentRecordArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListRelatedItemsInput(BaseValidatorModel):
    incidentRecordArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListReplicationSetsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListResponsePlansInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ResponsePlanSummary(BaseValidatorModel):
    arn: str
    name: str
    displayName: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PagerDutyIncidentConfiguration(BaseValidatorModel):
    serviceId: str


class PutResourcePolicyInput(BaseValidatorModel):
    policy: str
    resourceArn: str


class RegionInfo(BaseValidatorModel):
    status: RegionStatusType
    statusUpdateDateTime: datetime
    sseKmsKeyId: Optional[str] = None
    statusMessage: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDeletionProtectionInput(BaseValidatorModel):
    arn: str
    deletionProtected: bool
    clientToken: Optional[str] = None


class CreateReplicationSetOutput(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class CreateResponsePlanOutput(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class CreateTimelineEventOutput(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str
    ResponseMetadata: ResponseMetadata


class ListReplicationSetsOutput(BaseValidatorModel):
    replicationSetArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyOutput(BaseValidatorModel):
    policyId: str
    ResponseMetadata: ResponseMetadata


class StartIncidentOutput(BaseValidatorModel):
    incidentRecordArn: str
    ResponseMetadata: ResponseMetadata


class FindingDetails(BaseValidatorModel):
    cloudFormationStackUpdate: Optional[CloudFormationStackUpdate] = None
    codeDeployDeployment: Optional[CodeDeployDeployment] = None


class Timestamp(BaseValidatorModel):
    pass


class Condition(BaseValidatorModel):
    after: Optional[Timestamp] = None
    before: Optional[Timestamp] = None
    equals: Optional[AttributeValueList] = None


class TriggerDetails(BaseValidatorModel):
    source: str
    timestamp: Timestamp
    rawData: Optional[str] = None
    triggerArn: Optional[str] = None


class CreateReplicationSetInput(BaseValidatorModel):
    regions: Mapping[str, RegionMapInputValue]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateTimelineEventInput(BaseValidatorModel):
    eventData: str
    eventTime: Timestamp
    eventType: str
    incidentRecordArn: str
    clientToken: Optional[str] = None
    eventReferences: Optional[Sequence[EventReference]] = None


class EventSummary(BaseValidatorModel):
    eventId: str
    eventTime: datetime
    eventType: str
    eventUpdatedTime: datetime
    incidentRecordArn: str
    eventReferences: Optional[List[EventReference]] = None


class TimelineEvent(BaseValidatorModel):
    eventData: str
    eventId: str
    eventTime: datetime
    eventType: str
    eventUpdatedTime: datetime
    incidentRecordArn: str
    eventReferences: Optional[List[EventReference]] = None


class UpdateTimelineEventInput(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str
    clientToken: Optional[str] = None
    eventData: Optional[str] = None
    eventReferences: Optional[Sequence[EventReference]] = None
    eventTime: Optional[Timestamp] = None
    eventType: Optional[str] = None


class UpdateReplicationSetAction(BaseValidatorModel):
    addRegionAction: Optional[AddRegionAction] = None
    deleteRegionAction: Optional[DeleteRegionAction] = None


class SsmAutomationOutput(BaseValidatorModel):
    documentName: str
    roleArn: str
    documentVersion: Optional[str] = None
    dynamicParameters: Optional[Dict[str, DynamicSsmParameterValue]] = None
    parameters: Optional[Dict[str, List[str]]] = None
    targetAccount: Optional[SsmTargetAccountType] = None


class SsmAutomation(BaseValidatorModel):
    documentName: str
    roleArn: str
    documentVersion: Optional[str] = None
    dynamicParameters: Optional[Mapping[str, DynamicSsmParameterValue]] = None
    parameters: Optional[Mapping[str, Sequence[str]]] = None
    targetAccount: Optional[SsmTargetAccountType] = None


class FindingSummary(BaseValidatorModel):
    pass


class ListIncidentFindingsOutput(BaseValidatorModel):
    findings: List[FindingSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetReplicationSetInputWaitExtra(BaseValidatorModel):
    arn: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetReplicationSetInputWait(BaseValidatorModel):
    arn: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetResourcePoliciesInputPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIncidentFindingsInputPaginate(BaseValidatorModel):
    incidentRecordArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRelatedItemsInputPaginate(BaseValidatorModel):
    incidentRecordArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReplicationSetsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResponsePlansInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourcePoliciesOutput(BaseValidatorModel):
    resourcePolicies: List[ResourcePolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IncidentRecordSummary(BaseValidatorModel):
    arn: str
    creationTime: datetime
    impact: int
    incidentRecordSource: IncidentRecordSource
    status: IncidentRecordStatusType
    title: str
    resolvedTime: Optional[datetime] = None


class IncidentRecord(BaseValidatorModel):
    arn: str
    creationTime: datetime
    dedupeString: str
    impact: int
    incidentRecordSource: IncidentRecordSource
    lastModifiedBy: str
    lastModifiedTime: datetime
    status: IncidentRecordStatusType
    title: str
    automationExecutions: Optional[List[AutomationExecution]] = None
    chatChannel: Optional[ChatChannelOutput] = None
    notificationTargets: Optional[List[NotificationTargetItem]] = None
    resolvedTime: Optional[datetime] = None
    summary: Optional[str] = None


class IncidentTemplateOutput(BaseValidatorModel):
    impact: int
    title: str
    dedupeString: Optional[str] = None
    incidentTags: Optional[Dict[str, str]] = None
    notificationTargets: Optional[List[NotificationTargetItem]] = None
    summary: Optional[str] = None


class IncidentTemplate(BaseValidatorModel):
    impact: int
    title: str
    dedupeString: Optional[str] = None
    incidentTags: Optional[Mapping[str, str]] = None
    notificationTargets: Optional[Sequence[NotificationTargetItem]] = None
    summary: Optional[str] = None


class PagerDutyIncidentDetail(BaseValidatorModel):
    pass


class ItemValue(BaseValidatorModel):
    arn: Optional[str] = None
    metricDefinition: Optional[str] = None
    pagerDutyIncidentDetail: Optional[PagerDutyIncidentDetail] = None
    url: Optional[str] = None


class ListResponsePlansOutput(BaseValidatorModel):
    responsePlanSummaries: List[ResponsePlanSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PagerDutyConfiguration(BaseValidatorModel):
    name: str
    pagerDutyIncidentConfiguration: PagerDutyIncidentConfiguration
    secretId: str


class ReplicationSet(BaseValidatorModel):
    createdBy: str
    createdTime: datetime
    deletionProtected: bool
    lastModifiedBy: str
    lastModifiedTime: datetime
    regionMap: Dict[str, RegionInfo]
    status: ReplicationSetStatusType
    arn: Optional[str] = None


class ChatChannelUnion(BaseValidatorModel):
    pass


class UpdateIncidentRecordInput(BaseValidatorModel):
    arn: str
    chatChannel: Optional[ChatChannelUnion] = None
    clientToken: Optional[str] = None
    impact: Optional[int] = None
    notificationTargets: Optional[Sequence[NotificationTargetItem]] = None
    status: Optional[IncidentRecordStatusType] = None
    summary: Optional[str] = None
    title: Optional[str] = None


class Filter(BaseValidatorModel):
    condition: Condition
    key: str


class ListTimelineEventsOutput(BaseValidatorModel):
    eventSummaries: List[EventSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetTimelineEventOutput(BaseValidatorModel):
    event: TimelineEvent
    ResponseMetadata: ResponseMetadata


class UpdateReplicationSetInput(BaseValidatorModel):
    actions: Sequence[UpdateReplicationSetAction]
    arn: str
    clientToken: Optional[str] = None


class ActionOutput(BaseValidatorModel):
    ssmAutomation: Optional[SsmAutomationOutput] = None


class ListIncidentRecordsOutput(BaseValidatorModel):
    incidentRecordSummaries: List[IncidentRecordSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetIncidentRecordOutput(BaseValidatorModel):
    incidentRecord: IncidentRecord
    ResponseMetadata: ResponseMetadata


class Integration(BaseValidatorModel):
    pagerDutyConfiguration: Optional[PagerDutyConfiguration] = None


class GetReplicationSetOutput(BaseValidatorModel):
    replicationSet: ReplicationSet
    ResponseMetadata: ResponseMetadata


class Finding(BaseValidatorModel):
    pass


class BatchGetIncidentFindingsOutput(BaseValidatorModel):
    errors: List[BatchGetIncidentFindingsError]
    findings: List[Finding]
    ResponseMetadata: ResponseMetadata


class ListIncidentRecordsInputPaginate(BaseValidatorModel):
    filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIncidentRecordsInput(BaseValidatorModel):
    filters: Optional[Sequence[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTimelineEventsInputPaginate(BaseValidatorModel):
    incidentRecordArn: str
    filters: Optional[Sequence[Filter]] = None
    sortBy: Optional[Literal["EVENT_TIME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTimelineEventsInput(BaseValidatorModel):
    incidentRecordArn: str
    filters: Optional[Sequence[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["EVENT_TIME"]] = None
    sortOrder: Optional[SortOrderType] = None


class SsmAutomationUnion(BaseValidatorModel):
    pass


class Action(BaseValidatorModel):
    ssmAutomation: Optional[SsmAutomationUnion] = None


class ItemIdentifier(BaseValidatorModel):
    pass


class RelatedItem(BaseValidatorModel):
    identifier: ItemIdentifier
    generatedId: Optional[str] = None
    title: Optional[str] = None


class GetResponsePlanOutput(BaseValidatorModel):
    actions: List[ActionOutput]
    arn: str
    chatChannel: ChatChannelOutput
    displayName: str
    engagements: List[str]
    incidentTemplate: IncidentTemplateOutput
    integrations: List[Integration]
    name: str
    ResponseMetadata: ResponseMetadata


class ListRelatedItemsOutput(BaseValidatorModel):
    relatedItems: List[RelatedItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RelatedItemsUpdate(BaseValidatorModel):
    itemToAdd: Optional[RelatedItem] = None
    itemToRemove: Optional[ItemIdentifier] = None


class StartIncidentInput(BaseValidatorModel):
    responsePlanArn: str
    clientToken: Optional[str] = None
    impact: Optional[int] = None
    relatedItems: Optional[Sequence[RelatedItem]] = None
    title: Optional[str] = None
    triggerDetails: Optional[TriggerDetails] = None


class ActionUnion(BaseValidatorModel):
    pass


class IncidentTemplateUnion(BaseValidatorModel):
    pass


class CreateResponsePlanInput(BaseValidatorModel):
    incidentTemplate: IncidentTemplateUnion
    name: str
    actions: Optional[Sequence[ActionUnion]] = None
    chatChannel: Optional[ChatChannelUnion] = None
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    engagements: Optional[Sequence[str]] = None
    integrations: Optional[Sequence[Integration]] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateResponsePlanInput(BaseValidatorModel):
    arn: str
    actions: Optional[Sequence[ActionUnion]] = None
    chatChannel: Optional[ChatChannelUnion] = None
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    engagements: Optional[Sequence[str]] = None
    incidentTemplateDedupeString: Optional[str] = None
    incidentTemplateImpact: Optional[int] = None
    incidentTemplateNotificationTargets: Optional[Sequence[NotificationTargetItem]] = None
    incidentTemplateSummary: Optional[str] = None
    incidentTemplateTags: Optional[Mapping[str, str]] = None
    incidentTemplateTitle: Optional[str] = None
    integrations: Optional[Sequence[Integration]] = None


class UpdateRelatedItemsInput(BaseValidatorModel):
    incidentRecordArn: str
    relatedItemsUpdate: RelatedItemsUpdate
    clientToken: Optional[str] = None



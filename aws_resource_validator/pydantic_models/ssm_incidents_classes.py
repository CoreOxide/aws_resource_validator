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

class AddRegionActionTypeDef(BaseValidatorModel):
    regionName: str
    sseKmsKeyId: Optional[str] = None


class AttributeValueListTypeDef(BaseValidatorModel):
    integerValues: Optional[Sequence[int]] = None
    stringValues: Optional[Sequence[str]] = None


class AutomationExecutionTypeDef(BaseValidatorModel):
    ssmExecutionArn: Optional[str] = None


class BatchGetIncidentFindingsErrorTypeDef(BaseValidatorModel):
    code: str
    findingId: str
    message: str


class BatchGetIncidentFindingsInputTypeDef(BaseValidatorModel):
    findingIds: Sequence[str]
    incidentRecordArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ChatChannelOutputTypeDef(BaseValidatorModel):
    chatbotSns: Optional[List[str]] = None
    empty: Optional[Dict[str, Any]] = None


class ChatChannelTypeDef(BaseValidatorModel):
    chatbotSns: Optional[Sequence[str]] = None
    empty: Optional[Mapping[str, Any]] = None


class CloudFormationStackUpdateTypeDef(BaseValidatorModel):
    stackArn: str
    startTime: datetime
    endTime: Optional[datetime] = None


class CodeDeployDeploymentTypeDef(BaseValidatorModel):
    deploymentGroupArn: str
    deploymentId: str
    startTime: datetime
    endTime: Optional[datetime] = None


class RegionMapInputValueTypeDef(BaseValidatorModel):
    sseKmsKeyId: Optional[str] = None


class EventReferenceTypeDef(BaseValidatorModel):
    relatedItemId: Optional[str] = None
    resource: Optional[str] = None


class DeleteIncidentRecordInputTypeDef(BaseValidatorModel):
    arn: str


class DeleteRegionActionTypeDef(BaseValidatorModel):
    regionName: str


class DeleteReplicationSetInputTypeDef(BaseValidatorModel):
    arn: str


class DeleteResourcePolicyInputTypeDef(BaseValidatorModel):
    policyId: str
    resourceArn: str


class DeleteResponsePlanInputTypeDef(BaseValidatorModel):
    arn: str


class DeleteTimelineEventInputTypeDef(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str


class DynamicSsmParameterValueTypeDef(BaseValidatorModel):
    variable: Optional[VariableTypeType] = None


class GetIncidentRecordInputTypeDef(BaseValidatorModel):
    arn: str


class GetReplicationSetInputTypeDef(BaseValidatorModel):
    arn: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetResourcePoliciesInputTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ResourcePolicyTypeDef(BaseValidatorModel):
    policyDocument: str
    policyId: str
    ramResourceShareRegion: str


class GetResponsePlanInputTypeDef(BaseValidatorModel):
    arn: str


class GetTimelineEventInputTypeDef(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str


class IncidentRecordSourceTypeDef(BaseValidatorModel):
    createdBy: str
    source: str
    invokedBy: Optional[str] = None
    resourceArn: Optional[str] = None


class NotificationTargetItemTypeDef(BaseValidatorModel):
    snsTopicArn: Optional[str] = None


class ListIncidentFindingsInputTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListRelatedItemsInputTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListReplicationSetsInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListResponsePlansInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ResponsePlanSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: str
    displayName: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PagerDutyIncidentConfigurationTypeDef(BaseValidatorModel):
    serviceId: str


class PutResourcePolicyInputTypeDef(BaseValidatorModel):
    policy: str
    resourceArn: str


class RegionInfoTypeDef(BaseValidatorModel):
    status: RegionStatusType
    statusUpdateDateTime: datetime
    sseKmsKeyId: Optional[str] = None
    statusMessage: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDeletionProtectionInputTypeDef(BaseValidatorModel):
    arn: str
    deletionProtected: bool
    clientToken: Optional[str] = None


class CreateReplicationSetOutputTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResponsePlanOutputTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTimelineEventOutputTypeDef(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListReplicationSetsOutputTypeDef(BaseValidatorModel):
    replicationSetArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourcePolicyOutputTypeDef(BaseValidatorModel):
    policyId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartIncidentOutputTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class FindingDetailsTypeDef(BaseValidatorModel):
    cloudFormationStackUpdate: Optional[CloudFormationStackUpdateTypeDef] = None
    codeDeployDeployment: Optional[CodeDeployDeploymentTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ConditionTypeDef(BaseValidatorModel):
    after: Optional[TimestampTypeDef] = None
    before: Optional[TimestampTypeDef] = None
    equals: Optional[AttributeValueListTypeDef] = None


class TriggerDetailsTypeDef(BaseValidatorModel):
    source: str
    timestamp: TimestampTypeDef
    rawData: Optional[str] = None
    triggerArn: Optional[str] = None


class CreateReplicationSetInputTypeDef(BaseValidatorModel):
    regions: Mapping[str, RegionMapInputValueTypeDef]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateTimelineEventInputTypeDef(BaseValidatorModel):
    eventData: str
    eventTime: TimestampTypeDef
    eventType: str
    incidentRecordArn: str
    clientToken: Optional[str] = None
    eventReferences: Optional[Sequence[EventReferenceTypeDef]] = None


class EventSummaryTypeDef(BaseValidatorModel):
    eventId: str
    eventTime: datetime
    eventType: str
    eventUpdatedTime: datetime
    incidentRecordArn: str
    eventReferences: Optional[List[EventReferenceTypeDef]] = None


class TimelineEventTypeDef(BaseValidatorModel):
    eventData: str
    eventId: str
    eventTime: datetime
    eventType: str
    eventUpdatedTime: datetime
    incidentRecordArn: str
    eventReferences: Optional[List[EventReferenceTypeDef]] = None


class UpdateTimelineEventInputTypeDef(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str
    clientToken: Optional[str] = None
    eventData: Optional[str] = None
    eventReferences: Optional[Sequence[EventReferenceTypeDef]] = None
    eventTime: Optional[TimestampTypeDef] = None
    eventType: Optional[str] = None


class UpdateReplicationSetActionTypeDef(BaseValidatorModel):
    addRegionAction: Optional[AddRegionActionTypeDef] = None
    deleteRegionAction: Optional[DeleteRegionActionTypeDef] = None


class SsmAutomationOutputTypeDef(BaseValidatorModel):
    documentName: str
    roleArn: str
    documentVersion: Optional[str] = None
    dynamicParameters: Optional[Dict[str, DynamicSsmParameterValueTypeDef]] = None
    parameters: Optional[Dict[str, List[str]]] = None
    targetAccount: Optional[SsmTargetAccountType] = None


class SsmAutomationTypeDef(BaseValidatorModel):
    documentName: str
    roleArn: str
    documentVersion: Optional[str] = None
    dynamicParameters: Optional[Mapping[str, DynamicSsmParameterValueTypeDef]] = None
    parameters: Optional[Mapping[str, Sequence[str]]] = None
    targetAccount: Optional[SsmTargetAccountType] = None


class FindingSummaryTypeDef(BaseValidatorModel):
    pass


class ListIncidentFindingsOutputTypeDef(BaseValidatorModel):
    findings: List[FindingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetReplicationSetInputWaitExtraTypeDef(BaseValidatorModel):
    arn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetReplicationSetInputWaitTypeDef(BaseValidatorModel):
    arn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetResourcePoliciesInputPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIncidentFindingsInputPaginateTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRelatedItemsInputPaginateTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListReplicationSetsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResponsePlansInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourcePoliciesOutputTypeDef(BaseValidatorModel):
    resourcePolicies: List[ResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IncidentRecordSummaryTypeDef(BaseValidatorModel):
    arn: str
    creationTime: datetime
    impact: int
    incidentRecordSource: IncidentRecordSourceTypeDef
    status: IncidentRecordStatusType
    title: str
    resolvedTime: Optional[datetime] = None


class IncidentRecordTypeDef(BaseValidatorModel):
    arn: str
    creationTime: datetime
    dedupeString: str
    impact: int
    incidentRecordSource: IncidentRecordSourceTypeDef
    lastModifiedBy: str
    lastModifiedTime: datetime
    status: IncidentRecordStatusType
    title: str
    automationExecutions: Optional[List[AutomationExecutionTypeDef]] = None
    chatChannel: Optional[ChatChannelOutputTypeDef] = None
    notificationTargets: Optional[List[NotificationTargetItemTypeDef]] = None
    resolvedTime: Optional[datetime] = None
    summary: Optional[str] = None


class IncidentTemplateOutputTypeDef(BaseValidatorModel):
    impact: int
    title: str
    dedupeString: Optional[str] = None
    incidentTags: Optional[Dict[str, str]] = None
    notificationTargets: Optional[List[NotificationTargetItemTypeDef]] = None
    summary: Optional[str] = None


class IncidentTemplateTypeDef(BaseValidatorModel):
    impact: int
    title: str
    dedupeString: Optional[str] = None
    incidentTags: Optional[Mapping[str, str]] = None
    notificationTargets: Optional[Sequence[NotificationTargetItemTypeDef]] = None
    summary: Optional[str] = None


class PagerDutyIncidentDetailTypeDef(BaseValidatorModel):
    pass


class ItemValueTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    metricDefinition: Optional[str] = None
    pagerDutyIncidentDetail: Optional[PagerDutyIncidentDetailTypeDef] = None
    url: Optional[str] = None


class ListResponsePlansOutputTypeDef(BaseValidatorModel):
    responsePlanSummaries: List[ResponsePlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PagerDutyConfigurationTypeDef(BaseValidatorModel):
    name: str
    pagerDutyIncidentConfiguration: PagerDutyIncidentConfigurationTypeDef
    secretId: str


class ReplicationSetTypeDef(BaseValidatorModel):
    createdBy: str
    createdTime: datetime
    deletionProtected: bool
    lastModifiedBy: str
    lastModifiedTime: datetime
    regionMap: Dict[str, RegionInfoTypeDef]
    status: ReplicationSetStatusType
    arn: Optional[str] = None


class ChatChannelUnionTypeDef(BaseValidatorModel):
    pass


class UpdateIncidentRecordInputTypeDef(BaseValidatorModel):
    arn: str
    chatChannel: Optional[ChatChannelUnionTypeDef] = None
    clientToken: Optional[str] = None
    impact: Optional[int] = None
    notificationTargets: Optional[Sequence[NotificationTargetItemTypeDef]] = None
    status: Optional[IncidentRecordStatusType] = None
    summary: Optional[str] = None
    title: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    condition: ConditionTypeDef
    key: str


class ListTimelineEventsOutputTypeDef(BaseValidatorModel):
    eventSummaries: List[EventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetTimelineEventOutputTypeDef(BaseValidatorModel):
    event: TimelineEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateReplicationSetInputTypeDef(BaseValidatorModel):
    actions: Sequence[UpdateReplicationSetActionTypeDef]
    arn: str
    clientToken: Optional[str] = None


class ActionOutputTypeDef(BaseValidatorModel):
    ssmAutomation: Optional[SsmAutomationOutputTypeDef] = None


class ListIncidentRecordsOutputTypeDef(BaseValidatorModel):
    incidentRecordSummaries: List[IncidentRecordSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetIncidentRecordOutputTypeDef(BaseValidatorModel):
    incidentRecord: IncidentRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IntegrationTypeDef(BaseValidatorModel):
    pagerDutyConfiguration: Optional[PagerDutyConfigurationTypeDef] = None


class GetReplicationSetOutputTypeDef(BaseValidatorModel):
    replicationSet: ReplicationSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FindingTypeDef(BaseValidatorModel):
    pass


class BatchGetIncidentFindingsOutputTypeDef(BaseValidatorModel):
    errors: List[BatchGetIncidentFindingsErrorTypeDef]
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListIncidentRecordsInputPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIncidentRecordsInputTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTimelineEventsInputPaginateTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    sortBy: Optional[Literal["EVENT_TIME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTimelineEventsInputTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["EVENT_TIME"]] = None
    sortOrder: Optional[SortOrderType] = None


class SsmAutomationUnionTypeDef(BaseValidatorModel):
    pass


class ActionTypeDef(BaseValidatorModel):
    ssmAutomation: Optional[SsmAutomationUnionTypeDef] = None


class ItemIdentifierTypeDef(BaseValidatorModel):
    pass


class RelatedItemTypeDef(BaseValidatorModel):
    identifier: ItemIdentifierTypeDef
    generatedId: Optional[str] = None
    title: Optional[str] = None


class GetResponsePlanOutputTypeDef(BaseValidatorModel):
    actions: List[ActionOutputTypeDef]
    arn: str
    chatChannel: ChatChannelOutputTypeDef
    displayName: str
    engagements: List[str]
    incidentTemplate: IncidentTemplateOutputTypeDef
    integrations: List[IntegrationTypeDef]
    name: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListRelatedItemsOutputTypeDef(BaseValidatorModel):
    relatedItems: List[RelatedItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RelatedItemsUpdateTypeDef(BaseValidatorModel):
    itemToAdd: Optional[RelatedItemTypeDef] = None
    itemToRemove: Optional[ItemIdentifierTypeDef] = None


class StartIncidentInputTypeDef(BaseValidatorModel):
    responsePlanArn: str
    clientToken: Optional[str] = None
    impact: Optional[int] = None
    relatedItems: Optional[Sequence[RelatedItemTypeDef]] = None
    title: Optional[str] = None
    triggerDetails: Optional[TriggerDetailsTypeDef] = None


class ActionUnionTypeDef(BaseValidatorModel):
    pass


class IncidentTemplateUnionTypeDef(BaseValidatorModel):
    pass


class CreateResponsePlanInputTypeDef(BaseValidatorModel):
    incidentTemplate: IncidentTemplateUnionTypeDef
    name: str
    actions: Optional[Sequence[ActionUnionTypeDef]] = None
    chatChannel: Optional[ChatChannelUnionTypeDef] = None
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    engagements: Optional[Sequence[str]] = None
    integrations: Optional[Sequence[IntegrationTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateResponsePlanInputTypeDef(BaseValidatorModel):
    arn: str
    actions: Optional[Sequence[ActionUnionTypeDef]] = None
    chatChannel: Optional[ChatChannelUnionTypeDef] = None
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    engagements: Optional[Sequence[str]] = None
    incidentTemplateDedupeString: Optional[str] = None
    incidentTemplateImpact: Optional[int] = None
    incidentTemplateNotificationTargets: Optional[Sequence[NotificationTargetItemTypeDef]] = None
    incidentTemplateSummary: Optional[str] = None
    incidentTemplateTags: Optional[Mapping[str, str]] = None
    incidentTemplateTitle: Optional[str] = None
    integrations: Optional[Sequence[IntegrationTypeDef]] = None


class UpdateRelatedItemsInputTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    relatedItemsUpdate: RelatedItemsUpdateTypeDef
    clientToken: Optional[str] = None



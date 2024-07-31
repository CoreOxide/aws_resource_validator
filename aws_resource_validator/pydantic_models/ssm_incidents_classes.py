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
from aws_resource_validator.pydantic_models.ssm_incidents_constants import *

class AddRegionActionTypeDef(BaseModel):
    regionName: str
    sseKmsKeyId: Optional[str] = None

class AttributeValueListTypeDef(BaseModel):
    integerValues: Optional[Sequence[int]] = None
    stringValues: Optional[Sequence[str]] = None

class AutomationExecutionTypeDef(BaseModel):
    ssmExecutionArn: Optional[str] = None

class BatchGetIncidentFindingsErrorTypeDef(BaseModel):
    code: str
    findingId: str
    message: str

class BatchGetIncidentFindingsInputRequestTypeDef(BaseModel):
    findingIds: Sequence[str]
    incidentRecordArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ChatChannelTypeDef(BaseModel):
    chatbotSns: Optional[Sequence[str]] = None
    empty: Optional[Mapping[str, Any]] = None

class CloudFormationStackUpdateTypeDef(BaseModel):
    stackArn: str
    startTime: datetime
    endTime: Optional[datetime] = None

class CodeDeployDeploymentTypeDef(BaseModel):
    deploymentGroupArn: str
    deploymentId: str
    startTime: datetime
    endTime: Optional[datetime] = None

class RegionMapInputValueTypeDef(BaseModel):
    sseKmsKeyId: Optional[str] = None

class EventReferenceTypeDef(BaseModel):
    relatedItemId: Optional[str] = None
    resource: Optional[str] = None

class DeleteIncidentRecordInputRequestTypeDef(BaseModel):
    arn: str

class DeleteRegionActionTypeDef(BaseModel):
    regionName: str

class DeleteReplicationSetInputRequestTypeDef(BaseModel):
    arn: str

class DeleteResourcePolicyInputRequestTypeDef(BaseModel):
    policyId: str
    resourceArn: str

class DeleteResponsePlanInputRequestTypeDef(BaseModel):
    arn: str

class DeleteTimelineEventInputRequestTypeDef(BaseModel):
    eventId: str
    incidentRecordArn: str

class DynamicSsmParameterValueTypeDef(BaseModel):
    variable: Optional[VariableTypeType] = None

class FindingSummaryTypeDef(BaseModel):
    id: str
    lastModifiedTime: datetime

class GetIncidentRecordInputRequestTypeDef(BaseModel):
    arn: str

class GetReplicationSetInputRequestTypeDef(BaseModel):
    arn: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetResourcePoliciesInputRequestTypeDef(BaseModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ResourcePolicyTypeDef(BaseModel):
    policyDocument: str
    policyId: str
    ramResourceShareRegion: str

class GetResponsePlanInputRequestTypeDef(BaseModel):
    arn: str

class GetTimelineEventInputRequestTypeDef(BaseModel):
    eventId: str
    incidentRecordArn: str

class IncidentRecordSourceTypeDef(BaseModel):
    createdBy: str
    source: str
    invokedBy: Optional[str] = None
    resourceArn: Optional[str] = None

class NotificationTargetItemTypeDef(BaseModel):
    snsTopicArn: Optional[str] = None

class PagerDutyIncidentDetailTypeDef(BaseModel):
    id: str
    autoResolve: Optional[bool] = None
    secretId: Optional[str] = None

class ListIncidentFindingsInputRequestTypeDef(BaseModel):
    incidentRecordArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRelatedItemsInputRequestTypeDef(BaseModel):
    incidentRecordArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListReplicationSetsInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListResponsePlansInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ResponsePlanSummaryTypeDef(BaseModel):
    arn: str
    name: str
    displayName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PagerDutyIncidentConfigurationTypeDef(BaseModel):
    serviceId: str

class PutResourcePolicyInputRequestTypeDef(BaseModel):
    policy: str
    resourceArn: str

class RegionInfoTypeDef(BaseModel):
    status: RegionStatusType
    statusUpdateDateTime: datetime
    sseKmsKeyId: Optional[str] = None
    statusMessage: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDeletionProtectionInputRequestTypeDef(BaseModel):
    arn: str
    deletionProtected: bool
    clientToken: Optional[str] = None

class CreateReplicationSetOutputTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResponsePlanOutputTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTimelineEventOutputTypeDef(BaseModel):
    eventId: str
    incidentRecordArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReplicationSetsOutputTypeDef(BaseModel):
    nextToken: str
    replicationSetArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyOutputTypeDef(BaseModel):
    policyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartIncidentOutputTypeDef(BaseModel):
    incidentRecordArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class FindingDetailsTypeDef(BaseModel):
    cloudFormationStackUpdate: Optional[CloudFormationStackUpdateTypeDef] = None
    codeDeployDeployment: Optional[CodeDeployDeploymentTypeDef] = None

class ConditionTypeDef(BaseModel):
    after: Optional[TimestampTypeDef] = None
    before: Optional[TimestampTypeDef] = None
    equals: Optional[AttributeValueListTypeDef] = None

class TriggerDetailsTypeDef(BaseModel):
    source: str
    timestamp: TimestampTypeDef
    rawData: Optional[str] = None
    triggerArn: Optional[str] = None

class CreateReplicationSetInputRequestTypeDef(BaseModel):
    regions: Mapping[str, RegionMapInputValueTypeDef]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateTimelineEventInputRequestTypeDef(BaseModel):
    eventData: str
    eventTime: TimestampTypeDef
    eventType: str
    incidentRecordArn: str
    clientToken: Optional[str] = None
    eventReferences: Optional[Sequence[EventReferenceTypeDef]] = None

class EventSummaryTypeDef(BaseModel):
    eventId: str
    eventTime: datetime
    eventType: str
    eventUpdatedTime: datetime
    incidentRecordArn: str
    eventReferences: Optional[List[EventReferenceTypeDef]] = None

class TimelineEventTypeDef(BaseModel):
    eventData: str
    eventId: str
    eventTime: datetime
    eventType: str
    eventUpdatedTime: datetime
    incidentRecordArn: str
    eventReferences: Optional[List[EventReferenceTypeDef]] = None

class UpdateTimelineEventInputRequestTypeDef(BaseModel):
    eventId: str
    incidentRecordArn: str
    clientToken: Optional[str] = None
    eventData: Optional[str] = None
    eventReferences: Optional[Sequence[EventReferenceTypeDef]] = None
    eventTime: Optional[TimestampTypeDef] = None
    eventType: Optional[str] = None

class UpdateReplicationSetActionTypeDef(BaseModel):
    addRegionAction: Optional[AddRegionActionTypeDef] = None
    deleteRegionAction: Optional[DeleteRegionActionTypeDef] = None

class SsmAutomationTypeDef(BaseModel):
    documentName: str
    roleArn: str
    documentVersion: Optional[str] = None
    dynamicParameters: Optional[Mapping[str, DynamicSsmParameterValueTypeDef]] = None
    parameters: Optional[Mapping[str, Sequence[str]]] = None
    targetAccount: Optional[SsmTargetAccountType] = None

class ListIncidentFindingsOutputTypeDef(BaseModel):
    findings: List[FindingSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef(BaseModel):
    arn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef(BaseModel):
    arn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIncidentFindingsInputListIncidentFindingsPaginateTypeDef(BaseModel):
    incidentRecordArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRelatedItemsInputListRelatedItemsPaginateTypeDef(BaseModel):
    incidentRecordArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReplicationSetsInputListReplicationSetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResponsePlansInputListResponsePlansPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourcePoliciesOutputTypeDef(BaseModel):
    nextToken: str
    resourcePolicies: List[ResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IncidentRecordSummaryTypeDef(BaseModel):
    arn: str
    creationTime: datetime
    impact: int
    incidentRecordSource: IncidentRecordSourceTypeDef
    status: IncidentRecordStatusType
    title: str
    resolvedTime: Optional[datetime] = None

class IncidentRecordTypeDef(BaseModel):
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
    chatChannel: Optional[ChatChannelTypeDef] = None
    notificationTargets: Optional[List[NotificationTargetItemTypeDef]] = None
    resolvedTime: Optional[datetime] = None
    summary: Optional[str] = None

class IncidentTemplateTypeDef(BaseModel):
    impact: int
    title: str
    dedupeString: Optional[str] = None
    incidentTags: Optional[Mapping[str, str]] = None
    notificationTargets: Optional[Sequence[NotificationTargetItemTypeDef]] = None
    summary: Optional[str] = None

class UpdateIncidentRecordInputRequestTypeDef(BaseModel):
    arn: str
    chatChannel: Optional[ChatChannelTypeDef] = None
    clientToken: Optional[str] = None
    impact: Optional[int] = None
    notificationTargets: Optional[Sequence[NotificationTargetItemTypeDef]] = None
    status: Optional[IncidentRecordStatusType] = None
    summary: Optional[str] = None
    title: Optional[str] = None

class ItemValueTypeDef(BaseModel):
    arn: Optional[str] = None
    metricDefinition: Optional[str] = None
    pagerDutyIncidentDetail: Optional[PagerDutyIncidentDetailTypeDef] = None
    url: Optional[str] = None

class ListResponsePlansOutputTypeDef(BaseModel):
    nextToken: str
    responsePlanSummaries: List[ResponsePlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PagerDutyConfigurationTypeDef(BaseModel):
    name: str
    pagerDutyIncidentConfiguration: PagerDutyIncidentConfigurationTypeDef
    secretId: str

class ReplicationSetTypeDef(BaseModel):
    createdBy: str
    createdTime: datetime
    deletionProtected: bool
    lastModifiedBy: str
    lastModifiedTime: datetime
    regionMap: Dict[str, RegionInfoTypeDef]
    status: ReplicationSetStatusType
    arn: Optional[str] = None

class FindingTypeDef(BaseModel):
    creationTime: datetime
    id: str
    lastModifiedTime: datetime
    details: Optional[FindingDetailsTypeDef] = None

class FilterTypeDef(BaseModel):
    condition: ConditionTypeDef
    key: str

class ListTimelineEventsOutputTypeDef(BaseModel):
    eventSummaries: List[EventSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTimelineEventOutputTypeDef(BaseModel):
    event: TimelineEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReplicationSetInputRequestTypeDef(BaseModel):
    actions: Sequence[UpdateReplicationSetActionTypeDef]
    arn: str
    clientToken: Optional[str] = None

class ActionTypeDef(BaseModel):
    ssmAutomation: Optional[SsmAutomationTypeDef] = None

class ListIncidentRecordsOutputTypeDef(BaseModel):
    incidentRecordSummaries: List[IncidentRecordSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIncidentRecordOutputTypeDef(BaseModel):
    incidentRecord: IncidentRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ItemIdentifierTypeDef(BaseModel):
    type: ItemTypeType
    value: ItemValueTypeDef

class IntegrationTypeDef(BaseModel):
    pagerDutyConfiguration: Optional[PagerDutyConfigurationTypeDef] = None

class GetReplicationSetOutputTypeDef(BaseModel):
    replicationSet: ReplicationSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetIncidentFindingsOutputTypeDef(BaseModel):
    errors: List[BatchGetIncidentFindingsErrorTypeDef]
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIncidentRecordsInputRequestTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTimelineEventsInputListTimelineEventsPaginateTypeDef(BaseModel):
    incidentRecordArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    sortBy: Optional[Literal["EVENT_TIME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTimelineEventsInputRequestTypeDef(BaseModel):
    incidentRecordArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["EVENT_TIME"]] = None
    sortOrder: Optional[SortOrderType] = None

class RelatedItemTypeDef(BaseModel):
    identifier: ItemIdentifierTypeDef
    generatedId: Optional[str] = None
    title: Optional[str] = None

class CreateResponsePlanInputRequestTypeDef(BaseModel):
    incidentTemplate: IncidentTemplateTypeDef
    name: str
    actions: Optional[Sequence[ActionTypeDef]] = None
    chatChannel: Optional[ChatChannelTypeDef] = None
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    engagements: Optional[Sequence[str]] = None
    integrations: Optional[Sequence[IntegrationTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class GetResponsePlanOutputTypeDef(BaseModel):
    actions: List[ActionTypeDef]
    arn: str
    chatChannel: ChatChannelTypeDef
    displayName: str
    engagements: List[str]
    incidentTemplate: IncidentTemplateTypeDef
    integrations: List[IntegrationTypeDef]
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResponsePlanInputRequestTypeDef(BaseModel):
    arn: str
    actions: Optional[Sequence[ActionTypeDef]] = None
    chatChannel: Optional[ChatChannelTypeDef] = None
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

class ListRelatedItemsOutputTypeDef(BaseModel):
    nextToken: str
    relatedItems: List[RelatedItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RelatedItemsUpdateTypeDef(BaseModel):
    itemToAdd: Optional[RelatedItemTypeDef] = None
    itemToRemove: Optional[ItemIdentifierTypeDef] = None

class StartIncidentInputRequestTypeDef(BaseModel):
    responsePlanArn: str
    clientToken: Optional[str] = None
    impact: Optional[int] = None
    relatedItems: Optional[Sequence[RelatedItemTypeDef]] = None
    title: Optional[str] = None
    triggerDetails: Optional[TriggerDetailsTypeDef] = None

class UpdateRelatedItemsInputRequestTypeDef(BaseModel):
    incidentRecordArn: str
    relatedItemsUpdate: RelatedItemsUpdateTypeDef
    clientToken: Optional[str] = None


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

class BatchGetIncidentFindingsInputRequestTypeDef(BaseValidatorModel):
    findingIds: Sequence[str]
    incidentRecordArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class DeleteIncidentRecordInputRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteRegionActionTypeDef(BaseValidatorModel):
    regionName: str

class DeleteReplicationSetInputRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    policyId: str
    resourceArn: str

class DeleteResponsePlanInputRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteTimelineEventInputRequestTypeDef(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str

class DynamicSsmParameterValueTypeDef(BaseValidatorModel):
    variable: Optional[VariableTypeType] = None

class FindingSummaryTypeDef(BaseValidatorModel):
    id: str
    lastModifiedTime: datetime

class GetIncidentRecordInputRequestTypeDef(BaseValidatorModel):
    arn: str

class GetReplicationSetInputRequestTypeDef(BaseValidatorModel):
    arn: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetResourcePoliciesInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ResourcePolicyTypeDef(BaseValidatorModel):
    policyDocument: str
    policyId: str
    ramResourceShareRegion: str

class GetResponsePlanInputRequestTypeDef(BaseValidatorModel):
    arn: str

class GetTimelineEventInputRequestTypeDef(BaseValidatorModel):
    eventId: str
    incidentRecordArn: str

class IncidentRecordSourceTypeDef(BaseValidatorModel):
    createdBy: str
    source: str
    invokedBy: Optional[str] = None
    resourceArn: Optional[str] = None

class NotificationTargetItemTypeDef(BaseValidatorModel):
    snsTopicArn: Optional[str] = None

class PagerDutyIncidentDetailTypeDef(BaseValidatorModel):
    id: str
    autoResolve: Optional[bool] = None
    secretId: Optional[str] = None

class ListIncidentFindingsInputRequestTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRelatedItemsInputRequestTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListReplicationSetsInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListResponsePlansInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ResponsePlanSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: str
    displayName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class PagerDutyIncidentConfigurationTypeDef(BaseValidatorModel):
    serviceId: str

class PutResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    policy: str
    resourceArn: str

class RegionInfoTypeDef(BaseValidatorModel):
    status: RegionStatusType
    statusUpdateDateTime: datetime
    sseKmsKeyId: Optional[str] = None
    statusMessage: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDeletionProtectionInputRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    replicationSetArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

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

class ConditionTypeDef(BaseValidatorModel):
    after: Optional[TimestampTypeDef] = None
    before: Optional[TimestampTypeDef] = None
    equals: Optional[AttributeValueListTypeDef] = None

class TriggerDetailsTypeDef(BaseValidatorModel):
    source: str
    timestamp: TimestampTypeDef
    rawData: Optional[str] = None
    triggerArn: Optional[str] = None

class CreateReplicationSetInputRequestTypeDef(BaseValidatorModel):
    regions: Mapping[str, RegionMapInputValueTypeDef]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateTimelineEventInputRequestTypeDef(BaseValidatorModel):
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

class UpdateTimelineEventInputRequestTypeDef(BaseValidatorModel):
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

class SsmAutomationTypeDef(BaseValidatorModel):
    documentName: str
    roleArn: str
    documentVersion: Optional[str] = None
    dynamicParameters: Optional[Mapping[str, DynamicSsmParameterValueTypeDef]] = None
    parameters: Optional[Mapping[str, Sequence[str]]] = None
    targetAccount: Optional[SsmTargetAccountType] = None

class ListIncidentFindingsOutputTypeDef(BaseValidatorModel):
    findings: List[FindingSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef(BaseValidatorModel):
    arn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef(BaseValidatorModel):
    arn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIncidentFindingsInputListIncidentFindingsPaginateTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRelatedItemsInputListRelatedItemsPaginateTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReplicationSetsInputListReplicationSetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResponsePlansInputListResponsePlansPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourcePoliciesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    resourcePolicies: List[ResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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
    chatChannel: Optional[ChatChannelTypeDef] = None
    notificationTargets: Optional[List[NotificationTargetItemTypeDef]] = None
    resolvedTime: Optional[datetime] = None
    summary: Optional[str] = None

class IncidentTemplateTypeDef(BaseValidatorModel):
    impact: int
    title: str
    dedupeString: Optional[str] = None
    incidentTags: Optional[Mapping[str, str]] = None
    notificationTargets: Optional[Sequence[NotificationTargetItemTypeDef]] = None
    summary: Optional[str] = None

class UpdateIncidentRecordInputRequestTypeDef(BaseValidatorModel):
    arn: str
    chatChannel: Optional[ChatChannelTypeDef] = None
    clientToken: Optional[str] = None
    impact: Optional[int] = None
    notificationTargets: Optional[Sequence[NotificationTargetItemTypeDef]] = None
    status: Optional[IncidentRecordStatusType] = None
    summary: Optional[str] = None
    title: Optional[str] = None

class ItemValueTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    metricDefinition: Optional[str] = None
    pagerDutyIncidentDetail: Optional[PagerDutyIncidentDetailTypeDef] = None
    url: Optional[str] = None

class ListResponsePlansOutputTypeDef(BaseValidatorModel):
    nextToken: str
    responsePlanSummaries: List[ResponsePlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class FindingTypeDef(BaseValidatorModel):
    creationTime: datetime
    id: str
    lastModifiedTime: datetime
    details: Optional[FindingDetailsTypeDef] = None

class FilterTypeDef(BaseValidatorModel):
    condition: ConditionTypeDef
    key: str

class ListTimelineEventsOutputTypeDef(BaseValidatorModel):
    eventSummaries: List[EventSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTimelineEventOutputTypeDef(BaseValidatorModel):
    event: TimelineEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReplicationSetInputRequestTypeDef(BaseValidatorModel):
    actions: Sequence[UpdateReplicationSetActionTypeDef]
    arn: str
    clientToken: Optional[str] = None

class ActionTypeDef(BaseValidatorModel):
    ssmAutomation: Optional[SsmAutomationTypeDef] = None

class ListIncidentRecordsOutputTypeDef(BaseValidatorModel):
    incidentRecordSummaries: List[IncidentRecordSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIncidentRecordOutputTypeDef(BaseValidatorModel):
    incidentRecord: IncidentRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ItemIdentifierTypeDef(BaseValidatorModel):
    type: ItemTypeType
    value: ItemValueTypeDef

class IntegrationTypeDef(BaseValidatorModel):
    pagerDutyConfiguration: Optional[PagerDutyConfigurationTypeDef] = None

class GetReplicationSetOutputTypeDef(BaseValidatorModel):
    replicationSet: ReplicationSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetIncidentFindingsOutputTypeDef(BaseValidatorModel):
    errors: List[BatchGetIncidentFindingsErrorTypeDef]
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIncidentRecordsInputRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTimelineEventsInputListTimelineEventsPaginateTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    sortBy: Optional[Literal["EVENT_TIME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTimelineEventsInputRequestTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["EVENT_TIME"]] = None
    sortOrder: Optional[SortOrderType] = None

class RelatedItemTypeDef(BaseValidatorModel):
    identifier: ItemIdentifierTypeDef
    generatedId: Optional[str] = None
    title: Optional[str] = None

class CreateResponsePlanInputRequestTypeDef(BaseValidatorModel):
    incidentTemplate: IncidentTemplateTypeDef
    name: str
    actions: Optional[Sequence[ActionTypeDef]] = None
    chatChannel: Optional[ChatChannelTypeDef] = None
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    engagements: Optional[Sequence[str]] = None
    integrations: Optional[Sequence[IntegrationTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class GetResponsePlanOutputTypeDef(BaseValidatorModel):
    actions: List[ActionTypeDef]
    arn: str
    chatChannel: ChatChannelTypeDef
    displayName: str
    engagements: List[str]
    incidentTemplate: IncidentTemplateTypeDef
    integrations: List[IntegrationTypeDef]
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResponsePlanInputRequestTypeDef(BaseValidatorModel):
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

class ListRelatedItemsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    relatedItems: List[RelatedItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RelatedItemsUpdateTypeDef(BaseValidatorModel):
    itemToAdd: Optional[RelatedItemTypeDef] = None
    itemToRemove: Optional[ItemIdentifierTypeDef] = None

class StartIncidentInputRequestTypeDef(BaseValidatorModel):
    responsePlanArn: str
    clientToken: Optional[str] = None
    impact: Optional[int] = None
    relatedItems: Optional[Sequence[RelatedItemTypeDef]] = None
    title: Optional[str] = None
    triggerDetails: Optional[TriggerDetailsTypeDef] = None

class UpdateRelatedItemsInputRequestTypeDef(BaseValidatorModel):
    incidentRecordArn: str
    relatedItemsUpdate: RelatedItemsUpdateTypeDef
    clientToken: Optional[str] = None


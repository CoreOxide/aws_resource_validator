from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AnswerMachineDetectionConfig(BaseValidatorModel):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: Optional[bool] = None


class InstanceIdFilter(BaseValidatorModel):
    value: str
    operator: Literal['Eq']


class ScheduleOutput(BaseValidatorModel):
    startTime: datetime
    endTime: datetime
    refreshFrequency: Optional[str] = None


class EmailChannelSubtypeParameters(BaseValidatorModel):
    destinationEmailAddress: str
    templateParameters: Dict[str, str]
    connectSourceEmailAddress: Optional[str] = None
    templateArn: Optional[str] = None


class SmsChannelSubtypeParameters(BaseValidatorModel):
    destinationPhoneNumber: str
    templateParameters: Dict[str, str]
    connectSourcePhoneNumberArn: Optional[str] = None
    templateArn: Optional[str] = None


class CommunicationLimit(BaseValidatorModel):
    maxCountPerRecipient: int
    frequency: int
    unit: Literal['DAY']


class LocalTimeZoneConfigOutput(BaseValidatorModel):
    defaultTimeZone: Optional[str] = None
    localTimeZoneDetection: Optional[List[LocalTimeZoneDetectionTypeType]] = None


class LocalTimeZoneConfig(BaseValidatorModel):
    defaultTimeZone: Optional[str] = None
    localTimeZoneDetection: Optional[List[LocalTimeZoneDetectionTypeType]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CustomerProfilesIntegrationConfig(BaseValidatorModel):
    domainArn: str
    objectTypeNames: Dict[EventTypeType, str]


class CustomerProfilesIntegrationIdentifier(BaseValidatorModel):
    domainArn: str


class CustomerProfilesIntegrationSummary(BaseValidatorModel):
    domainArn: str
    objectTypeNames: Dict[EventTypeType, str]


class DeleteCampaignChannelSubtypeConfigRequest(BaseValidatorModel):
    id: str
    channelSubtype: ChannelSubtypeType


class DeleteCampaignCommunicationLimitsRequest(BaseValidatorModel):
    id: str
    config: Literal['ALL_CHANNEL_SUBTYPES']


class DeleteCampaignCommunicationTimeRequest(BaseValidatorModel):
    id: str
    config: CommunicationTimeConfigTypeType


class DeleteCampaignRequest(BaseValidatorModel):
    id: str


class DeleteConnectInstanceConfigRequest(BaseValidatorModel):
    connectInstanceId: str
    campaignDeletionPolicy: Optional[CampaignDeletionPolicyType] = None


class DeleteInstanceOnboardingJobRequest(BaseValidatorModel):
    connectInstanceId: str


class DescribeCampaignRequest(BaseValidatorModel):
    id: str


class EmailOutboundConfig(BaseValidatorModel):
    connectSourceEmailAddress: str
    wisdomTemplateArn: str
    sourceEmailAddressDisplayName: Optional[str] = None


class EmailOutboundModeOutput(BaseValidatorModel):
    agentless: Optional[Dict[str, Any]] = None


class EmailOutboundMode(BaseValidatorModel):
    agentless: Optional[Dict[str, Any]] = None


class EncryptionConfig(BaseValidatorModel):
    enabled: bool
    encryptionType: Optional[Literal['KMS']] = None
    keyArn: Optional[str] = None


class EventTrigger(BaseValidatorModel):
    customerProfilesDomainArn: Optional[str] = None


class FailedCampaignStateResponse(BaseValidatorModel):
    campaignId: Optional[str] = None
    failureCode: Optional[GetCampaignStateBatchFailureCodeType] = None


class FailedProfileOutboundRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None
    failureCode: Optional[ProfileOutboundRequestFailureCodeType] = None


class FailedRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None
    failureCode: Optional[FailureCodeType] = None


class GetCampaignStateBatchRequest(BaseValidatorModel):
    campaignIds: List[str]


class SuccessfulCampaignStateResponse(BaseValidatorModel):
    campaignId: Optional[str] = None
    state: Optional[CampaignStateType] = None


class GetCampaignStateRequest(BaseValidatorModel):
    id: str


class GetConnectInstanceConfigRequest(BaseValidatorModel):
    connectInstanceId: str


class GetInstanceOnboardingJobStatusRequest(BaseValidatorModel):
    connectInstanceId: str


class InstanceOnboardingJobStatus(BaseValidatorModel):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: Optional[InstanceOnboardingJobFailureCodeType] = None


class QConnectIntegrationConfig(BaseValidatorModel):
    knowledgeBaseArn: str


class QConnectIntegrationIdentifier(BaseValidatorModel):
    knowledgeBaseArn: str


class QConnectIntegrationSummary(BaseValidatorModel):
    knowledgeBaseArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListConnectInstanceIntegrationsRequest(BaseValidatorModel):
    connectInstanceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


class TimeRange(BaseValidatorModel):
    startTime: str
    endTime: str

Timestamp = Union[datetime, str]


class PauseCampaignRequest(BaseValidatorModel):
    id: str


class PredictiveConfig(BaseValidatorModel):
    bandwidthAllocation: float


class ProgressiveConfig(BaseValidatorModel):
    bandwidthAllocation: float


class SuccessfulRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None


class SuccessfulProfileOutboundRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None


class RestrictedPeriod(BaseValidatorModel):
    startDate: str
    endDate: str
    name: Optional[str] = None


class ResumeCampaignRequest(BaseValidatorModel):
    id: str


class SmsOutboundConfig(BaseValidatorModel):
    connectSourcePhoneNumberArn: str
    wisdomTemplateArn: str


class SmsOutboundModeOutput(BaseValidatorModel):
    agentless: Optional[Dict[str, Any]] = None


class SmsOutboundMode(BaseValidatorModel):
    agentless: Optional[Dict[str, Any]] = None


class StartCampaignRequest(BaseValidatorModel):
    id: str


class StopCampaignRequest(BaseValidatorModel):
    id: str


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: List[str]


class UpdateCampaignFlowAssociationRequest(BaseValidatorModel):
    id: str
    connectCampaignFlowArn: str


class UpdateCampaignNameRequest(BaseValidatorModel):
    id: str
    name: str


class TelephonyChannelSubtypeParameters(BaseValidatorModel):
    destinationPhoneNumber: str
    attributes: Dict[str, str]
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None


class TelephonyOutboundConfig(BaseValidatorModel):
    connectContactFlowId: str
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None


class CampaignFilters(BaseValidatorModel):
    instanceIdFilter: Optional[InstanceIdFilter] = None


class CampaignSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str
    channelSubtypes: List[ChannelSubtypeType]
    schedule: Optional[ScheduleOutput] = None
    connectCampaignFlowArn: Optional[str] = None


class CommunicationLimitsOutput(BaseValidatorModel):
    communicationLimitsList: Optional[List[CommunicationLimit]] = None


class CommunicationLimits(BaseValidatorModel):
    communicationLimitsList: Optional[List[CommunicationLimit]] = None


class CreateCampaignResponse(BaseValidatorModel):
    id: str
    arn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCampaignStateResponse(BaseValidatorModel):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmailChannelSubtypeConfigOutput(BaseValidatorModel):
    outboundMode: EmailOutboundModeOutput
    defaultOutboundConfig: EmailOutboundConfig
    capacity: Optional[float] = None


class EmailChannelSubtypeConfig(BaseValidatorModel):
    outboundMode: EmailOutboundMode
    defaultOutboundConfig: EmailOutboundConfig
    capacity: Optional[float] = None


class InstanceConfig(BaseValidatorModel):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfig


class StartInstanceOnboardingJobRequest(BaseValidatorModel):
    connectInstanceId: str
    encryptionConfig: EncryptionConfig


class Source(BaseValidatorModel):
    customerProfilesSegmentArn: Optional[str] = None
    eventTrigger: Optional[EventTrigger] = None


class GetCampaignStateBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulCampaignStateResponse]
    failedRequests: List[FailedCampaignStateResponse]
    ResponseMetadata: ResponseMetadata


class GetInstanceOnboardingJobStatusResponse(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatus
    ResponseMetadata: ResponseMetadata


class StartInstanceOnboardingJobResponse(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatus
    ResponseMetadata: ResponseMetadata


class IntegrationConfig(BaseValidatorModel):
    customerProfiles: Optional[CustomerProfilesIntegrationConfig] = None
    qConnect: Optional[QConnectIntegrationConfig] = None


class IntegrationIdentifier(BaseValidatorModel):
    customerProfiles: Optional[CustomerProfilesIntegrationIdentifier] = None
    qConnect: Optional[QConnectIntegrationIdentifier] = None


class IntegrationSummary(BaseValidatorModel):
    customerProfiles: Optional[CustomerProfilesIntegrationSummary] = None
    qConnect: Optional[QConnectIntegrationSummary] = None


class ListConnectInstanceIntegrationsRequestPaginate(BaseValidatorModel):
    connectInstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class OpenHoursOutput(BaseValidatorModel):
    dailyHours: Optional[Dict[DayOfWeekType, List[TimeRange]]] = None


class OpenHours(BaseValidatorModel):
    dailyHours: Optional[Dict[DayOfWeekType, List[TimeRange]]] = None


class ProfileOutboundRequest(BaseValidatorModel):
    clientToken: str
    profileId: str
    expirationTime: Optional[Timestamp] = None


class Schedule(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    refreshFrequency: Optional[str] = None


class TelephonyOutboundModeOutput(BaseValidatorModel):
    progressive: Optional[ProgressiveConfig] = None
    predictive: Optional[PredictiveConfig] = None
    agentless: Optional[Dict[str, Any]] = None


class TelephonyOutboundMode(BaseValidatorModel):
    progressive: Optional[ProgressiveConfig] = None
    predictive: Optional[PredictiveConfig] = None
    agentless: Optional[Dict[str, Any]] = None


class PutOutboundRequestBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulRequest]
    failedRequests: List[FailedRequest]
    ResponseMetadata: ResponseMetadata


class PutProfileOutboundRequestBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulProfileOutboundRequest]
    failedRequests: List[FailedProfileOutboundRequest]
    ResponseMetadata: ResponseMetadata


class RestrictedPeriodsOutput(BaseValidatorModel):
    restrictedPeriodList: Optional[List[RestrictedPeriod]] = None


class RestrictedPeriods(BaseValidatorModel):
    restrictedPeriodList: Optional[List[RestrictedPeriod]] = None


class SmsChannelSubtypeConfigOutput(BaseValidatorModel):
    outboundMode: SmsOutboundModeOutput
    defaultOutboundConfig: SmsOutboundConfig
    capacity: Optional[float] = None


class SmsChannelSubtypeConfig(BaseValidatorModel):
    outboundMode: SmsOutboundMode
    defaultOutboundConfig: SmsOutboundConfig
    capacity: Optional[float] = None


class ChannelSubtypeParameters(BaseValidatorModel):
    telephony: Optional[TelephonyChannelSubtypeParameters] = None
    sms: Optional[SmsChannelSubtypeParameters] = None
    email: Optional[EmailChannelSubtypeParameters] = None


class ListCampaignsRequestPaginate(BaseValidatorModel):
    filters: Optional[CampaignFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCampaignsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[CampaignFilters] = None


class ListCampaignsResponse(BaseValidatorModel):
    campaignSummaryList: List[CampaignSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CommunicationLimitsConfigOutput(BaseValidatorModel):
    allChannelSubtypes: Optional[CommunicationLimitsOutput] = None


class CommunicationLimitsConfig(BaseValidatorModel):
    allChannelSubtypes: Optional[CommunicationLimits] = None


class GetConnectInstanceConfigResponse(BaseValidatorModel):
    connectInstanceConfig: InstanceConfig
    ResponseMetadata: ResponseMetadata


class UpdateCampaignSourceRequest(BaseValidatorModel):
    id: str
    source: Source


class PutConnectInstanceIntegrationRequest(BaseValidatorModel):
    connectInstanceId: str
    integrationConfig: IntegrationConfig


class DeleteConnectInstanceIntegrationRequest(BaseValidatorModel):
    connectInstanceId: str
    integrationIdentifier: IntegrationIdentifier


class ListConnectInstanceIntegrationsResponse(BaseValidatorModel):
    integrationSummaryList: List[IntegrationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PutProfileOutboundRequestBatchRequest(BaseValidatorModel):
    id: str
    profileOutboundRequests: List[ProfileOutboundRequest]

ScheduleUnion = Union[Schedule, ScheduleOutput]


class TelephonyChannelSubtypeConfigOutput(BaseValidatorModel):
    outboundMode: TelephonyOutboundModeOutput
    defaultOutboundConfig: TelephonyOutboundConfig
    capacity: Optional[float] = None
    connectQueueId: Optional[str] = None


class TelephonyChannelSubtypeConfig(BaseValidatorModel):
    outboundMode: TelephonyOutboundMode
    defaultOutboundConfig: TelephonyOutboundConfig
    capacity: Optional[float] = None
    connectQueueId: Optional[str] = None


class TimeWindowOutput(BaseValidatorModel):
    openHours: OpenHoursOutput
    restrictedPeriods: Optional[RestrictedPeriodsOutput] = None


class TimeWindow(BaseValidatorModel):
    openHours: OpenHours
    restrictedPeriods: Optional[RestrictedPeriods] = None


class OutboundRequest(BaseValidatorModel):
    clientToken: str
    expirationTime: Timestamp
    channelSubtypeParameters: ChannelSubtypeParameters

CommunicationLimitsConfigUnion = Union[CommunicationLimitsConfig, CommunicationLimitsConfigOutput]


class UpdateCampaignScheduleRequest(BaseValidatorModel):
    id: str
    schedule: ScheduleUnion


class ChannelSubtypeConfigOutput(BaseValidatorModel):
    telephony: Optional[TelephonyChannelSubtypeConfigOutput] = None
    sms: Optional[SmsChannelSubtypeConfigOutput] = None
    email: Optional[EmailChannelSubtypeConfigOutput] = None


class ChannelSubtypeConfig(BaseValidatorModel):
    telephony: Optional[TelephonyChannelSubtypeConfig] = None
    sms: Optional[SmsChannelSubtypeConfig] = None
    email: Optional[EmailChannelSubtypeConfig] = None


class CommunicationTimeConfigOutput(BaseValidatorModel):
    localTimeZoneConfig: LocalTimeZoneConfigOutput
    telephony: Optional[TimeWindowOutput] = None
    sms: Optional[TimeWindowOutput] = None
    email: Optional[TimeWindowOutput] = None


class CommunicationTimeConfig(BaseValidatorModel):
    localTimeZoneConfig: LocalTimeZoneConfig
    telephony: Optional[TimeWindow] = None
    sms: Optional[TimeWindow] = None
    email: Optional[TimeWindow] = None


class PutOutboundRequestBatchRequest(BaseValidatorModel):
    id: str
    outboundRequests: List[OutboundRequest]


class UpdateCampaignCommunicationLimitsRequest(BaseValidatorModel):
    id: str
    communicationLimitsOverride: CommunicationLimitsConfigUnion

ChannelSubtypeConfigUnion = Union[ChannelSubtypeConfig, ChannelSubtypeConfigOutput]


class Campaign(BaseValidatorModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str
    channelSubtypeConfig: ChannelSubtypeConfigOutput
    source: Optional[Source] = None
    connectCampaignFlowArn: Optional[str] = None
    schedule: Optional[ScheduleOutput] = None
    communicationTimeConfig: Optional[CommunicationTimeConfigOutput] = None
    communicationLimitsOverride: Optional[CommunicationLimitsConfigOutput] = None
    tags: Optional[Dict[str, str]] = None

CommunicationTimeConfigUnion = Union[CommunicationTimeConfig, CommunicationTimeConfigOutput]


class UpdateCampaignChannelSubtypeConfigRequest(BaseValidatorModel):
    id: str
    channelSubtypeConfig: ChannelSubtypeConfigUnion


class DescribeCampaignResponse(BaseValidatorModel):
    campaign: Campaign
    ResponseMetadata: ResponseMetadata


class CreateCampaignRequest(BaseValidatorModel):
    name: str
    connectInstanceId: str
    channelSubtypeConfig: ChannelSubtypeConfigUnion
    source: Optional[Source] = None
    connectCampaignFlowArn: Optional[str] = None
    schedule: Optional[ScheduleUnion] = None
    communicationTimeConfig: Optional[CommunicationTimeConfigUnion] = None
    communicationLimitsOverride: Optional[CommunicationLimitsConfigUnion] = None
    tags: Optional[Dict[str, str]] = None


class UpdateCampaignCommunicationTimeRequest(BaseValidatorModel):
    id: str
    communicationTimeConfig: CommunicationTimeConfigUnion
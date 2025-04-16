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
from aws_resource_validator.pydantic_models.connectcampaignsv2_constants import *

class AnswerMachineDetectionConfig(BaseValidatorModel):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: Optional[bool] = None


class ScheduleOutput(BaseValidatorModel):
    startTime: datetime
    endTime: datetime
    refreshFrequency: Optional[str] = None


class EmailChannelSubtypeParameters(BaseValidatorModel):
    destinationEmailAddress: str
    templateParameters: Mapping[str, str]
    connectSourceEmailAddress: Optional[str] = None
    templateArn: Optional[str] = None


class SmsChannelSubtypeParameters(BaseValidatorModel):
    destinationPhoneNumber: str
    templateParameters: Mapping[str, str]
    connectSourcePhoneNumberArn: Optional[str] = None
    templateArn: Optional[str] = None


class CommunicationLimit(BaseValidatorModel):
    maxCountPerRecipient: int
    frequency: int
    unit: Literal["DAY"]


class LocalTimeZoneConfigOutput(BaseValidatorModel):
    defaultTimeZone: Optional[str] = None
    localTimeZoneDetection: Optional[List[LocalTimeZoneDetectionTypeType]] = None


class LocalTimeZoneConfig(BaseValidatorModel):
    defaultTimeZone: Optional[str] = None
    localTimeZoneDetection: Optional[Sequence[LocalTimeZoneDetectionTypeType]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CustomerProfilesIntegrationConfig(BaseValidatorModel):
    domainArn: str
    objectTypeNames: Mapping[EventTypeType, str]


class CustomerProfilesIntegrationIdentifier(BaseValidatorModel):
    domainArn: str


class CustomerProfilesIntegrationSummary(BaseValidatorModel):
    domainArn: str
    objectTypeNames: Dict[EventTypeType, str]


class DeleteConnectInstanceConfigRequest(BaseValidatorModel):
    connectInstanceId: str
    campaignDeletionPolicy: Optional[CampaignDeletionPolicyType] = None


class DeleteInstanceOnboardingJobRequest(BaseValidatorModel):
    connectInstanceId: str


class EmailOutboundConfig(BaseValidatorModel):
    connectSourceEmailAddress: str
    wisdomTemplateArn: str
    sourceEmailAddressDisplayName: Optional[str] = None


class EmailOutboundModeOutput(BaseValidatorModel):
    agentless: Optional[Dict[str, Any]] = None


class EmailOutboundMode(BaseValidatorModel):
    agentless: Optional[Mapping[str, Any]] = None


class EncryptionConfig(BaseValidatorModel):
    enabled: bool
    encryptionType: Optional[Literal["KMS"]] = None
    keyArn: Optional[str] = None


class EventTrigger(BaseValidatorModel):
    customerProfilesDomainArn: Optional[str] = None


class FailedCampaignStateResponse(BaseValidatorModel):
    campaignId: Optional[str] = None
    failureCode: Optional[GetCampaignStateBatchFailureCodeType] = None


class GetCampaignStateBatchRequest(BaseValidatorModel):
    campaignIds: Sequence[str]


class SuccessfulCampaignStateResponse(BaseValidatorModel):
    campaignId: Optional[str] = None
    state: Optional[CampaignStateType] = None


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


class PredictiveConfig(BaseValidatorModel):
    bandwidthAllocation: float


class ProgressiveConfig(BaseValidatorModel):
    bandwidthAllocation: float


class RestrictedPeriod(BaseValidatorModel):
    startDate: str
    endDate: str
    name: Optional[str] = None


class SmsOutboundConfig(BaseValidatorModel):
    connectSourcePhoneNumberArn: str
    wisdomTemplateArn: str


class SmsOutboundModeOutput(BaseValidatorModel):
    agentless: Optional[Dict[str, Any]] = None


class SmsOutboundMode(BaseValidatorModel):
    agentless: Optional[Mapping[str, Any]] = None


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class TelephonyChannelSubtypeParameters(BaseValidatorModel):
    destinationPhoneNumber: str
    attributes: Mapping[str, str]
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None


class TelephonyOutboundConfig(BaseValidatorModel):
    connectContactFlowId: str
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None


class InstanceIdFilter(BaseValidatorModel):
    pass


class CampaignFilters(BaseValidatorModel):
    instanceIdFilter: Optional[InstanceIdFilter] = None


class CommunicationLimitsOutput(BaseValidatorModel):
    communicationLimitsList: Optional[List[CommunicationLimit]] = None


class CommunicationLimits(BaseValidatorModel):
    communicationLimitsList: Optional[Sequence[CommunicationLimit]] = None


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
    dailyHours: Optional[Mapping[DayOfWeekType, Sequence[TimeRange]]] = None


class Timestamp(BaseValidatorModel):
    pass


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
    agentless: Optional[Mapping[str, Any]] = None


class FailedRequest(BaseValidatorModel):
    pass


class SuccessfulRequest(BaseValidatorModel):
    pass


class PutOutboundRequestBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulRequest]
    failedRequests: List[FailedRequest]
    ResponseMetadata: ResponseMetadata


class FailedProfileOutboundRequest(BaseValidatorModel):
    pass


class SuccessfulProfileOutboundRequest(BaseValidatorModel):
    pass


class PutProfileOutboundRequestBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulProfileOutboundRequest]
    failedRequests: List[FailedProfileOutboundRequest]
    ResponseMetadata: ResponseMetadata


class RestrictedPeriodsOutput(BaseValidatorModel):
    restrictedPeriodList: Optional[List[RestrictedPeriod]] = None


class RestrictedPeriods(BaseValidatorModel):
    restrictedPeriodList: Optional[Sequence[RestrictedPeriod]] = None


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


class CampaignSummary(BaseValidatorModel):
    pass


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


class Campaign(BaseValidatorModel):
    pass


class DescribeCampaignResponse(BaseValidatorModel):
    campaign: Campaign
    ResponseMetadata: ResponseMetadata


class ChannelSubtypeConfigUnion(BaseValidatorModel):
    pass


class ScheduleUnion(BaseValidatorModel):
    pass


class CommunicationTimeConfigUnion(BaseValidatorModel):
    pass


class CommunicationLimitsConfigUnion(BaseValidatorModel):
    pass


class CreateCampaignRequest(BaseValidatorModel):
    name: str
    connectInstanceId: str
    channelSubtypeConfig: ChannelSubtypeConfigUnion
    source: Optional[Source] = None
    connectCampaignFlowArn: Optional[str] = None
    schedule: Optional[ScheduleUnion] = None
    communicationTimeConfig: Optional[CommunicationTimeConfigUnion] = None
    communicationLimitsOverride: Optional[CommunicationLimitsConfigUnion] = None
    tags: Optional[Mapping[str, str]] = None



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

class AnswerMachineDetectionConfigTypeDef(BaseValidatorModel):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: Optional[bool] = None


class ScheduleOutputTypeDef(BaseValidatorModel):
    startTime: datetime
    endTime: datetime
    refreshFrequency: Optional[str] = None


class EmailChannelSubtypeParametersTypeDef(BaseValidatorModel):
    destinationEmailAddress: str
    templateParameters: Mapping[str, str]
    connectSourceEmailAddress: Optional[str] = None
    templateArn: Optional[str] = None


class SmsChannelSubtypeParametersTypeDef(BaseValidatorModel):
    destinationPhoneNumber: str
    templateParameters: Mapping[str, str]
    connectSourcePhoneNumberArn: Optional[str] = None
    templateArn: Optional[str] = None


class CommunicationLimitTypeDef(BaseValidatorModel):
    maxCountPerRecipient: int
    frequency: int
    unit: Literal["DAY"]


class LocalTimeZoneConfigOutputTypeDef(BaseValidatorModel):
    defaultTimeZone: Optional[str] = None
    localTimeZoneDetection: Optional[List[LocalTimeZoneDetectionTypeType]] = None


class LocalTimeZoneConfigTypeDef(BaseValidatorModel):
    defaultTimeZone: Optional[str] = None
    localTimeZoneDetection: Optional[Sequence[LocalTimeZoneDetectionTypeType]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CustomerProfilesIntegrationConfigTypeDef(BaseValidatorModel):
    domainArn: str
    objectTypeNames: Mapping[EventTypeType, str]


class CustomerProfilesIntegrationIdentifierTypeDef(BaseValidatorModel):
    domainArn: str


class CustomerProfilesIntegrationSummaryTypeDef(BaseValidatorModel):
    domainArn: str
    objectTypeNames: Dict[EventTypeType, str]


class DeleteConnectInstanceConfigRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str
    campaignDeletionPolicy: Optional[CampaignDeletionPolicyType] = None


class DeleteInstanceOnboardingJobRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str


class EmailOutboundConfigTypeDef(BaseValidatorModel):
    connectSourceEmailAddress: str
    wisdomTemplateArn: str
    sourceEmailAddressDisplayName: Optional[str] = None


class EmailOutboundModeOutputTypeDef(BaseValidatorModel):
    agentless: Optional[Dict[str, Any]] = None


class EmailOutboundModeTypeDef(BaseValidatorModel):
    agentless: Optional[Mapping[str, Any]] = None


class EncryptionConfigTypeDef(BaseValidatorModel):
    enabled: bool
    encryptionType: Optional[Literal["KMS"]] = None
    keyArn: Optional[str] = None


class EventTriggerTypeDef(BaseValidatorModel):
    customerProfilesDomainArn: Optional[str] = None


class FailedCampaignStateResponseTypeDef(BaseValidatorModel):
    campaignId: Optional[str] = None
    failureCode: Optional[GetCampaignStateBatchFailureCodeType] = None


class GetCampaignStateBatchRequestTypeDef(BaseValidatorModel):
    campaignIds: Sequence[str]


class SuccessfulCampaignStateResponseTypeDef(BaseValidatorModel):
    campaignId: Optional[str] = None
    state: Optional[CampaignStateType] = None


class GetConnectInstanceConfigRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str


class GetInstanceOnboardingJobStatusRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str


class InstanceOnboardingJobStatusTypeDef(BaseValidatorModel):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: Optional[InstanceOnboardingJobFailureCodeType] = None


class QConnectIntegrationConfigTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str


class QConnectIntegrationIdentifierTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str


class QConnectIntegrationSummaryTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListConnectInstanceIntegrationsRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    arn: str


class TimeRangeTypeDef(BaseValidatorModel):
    startTime: str
    endTime: str


class PredictiveConfigTypeDef(BaseValidatorModel):
    bandwidthAllocation: float


class ProgressiveConfigTypeDef(BaseValidatorModel):
    bandwidthAllocation: float


class RestrictedPeriodTypeDef(BaseValidatorModel):
    startDate: str
    endDate: str
    name: Optional[str] = None


class SmsOutboundConfigTypeDef(BaseValidatorModel):
    connectSourcePhoneNumberArn: str
    wisdomTemplateArn: str


class SmsOutboundModeOutputTypeDef(BaseValidatorModel):
    agentless: Optional[Dict[str, Any]] = None


class SmsOutboundModeTypeDef(BaseValidatorModel):
    agentless: Optional[Mapping[str, Any]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class TelephonyChannelSubtypeParametersTypeDef(BaseValidatorModel):
    destinationPhoneNumber: str
    attributes: Mapping[str, str]
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfigTypeDef] = None


class TelephonyOutboundConfigTypeDef(BaseValidatorModel):
    connectContactFlowId: str
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfigTypeDef] = None


class InstanceIdFilterTypeDef(BaseValidatorModel):
    pass


class CampaignFiltersTypeDef(BaseValidatorModel):
    instanceIdFilter: Optional[InstanceIdFilterTypeDef] = None


class CommunicationLimitsOutputTypeDef(BaseValidatorModel):
    communicationLimitsList: Optional[List[CommunicationLimitTypeDef]] = None


class CommunicationLimitsTypeDef(BaseValidatorModel):
    communicationLimitsList: Optional[Sequence[CommunicationLimitTypeDef]] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetCampaignStateResponseTypeDef(BaseValidatorModel):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class EmailChannelSubtypeConfigOutputTypeDef(BaseValidatorModel):
    outboundMode: EmailOutboundModeOutputTypeDef
    defaultOutboundConfig: EmailOutboundConfigTypeDef
    capacity: Optional[float] = None


class EmailChannelSubtypeConfigTypeDef(BaseValidatorModel):
    outboundMode: EmailOutboundModeTypeDef
    defaultOutboundConfig: EmailOutboundConfigTypeDef
    capacity: Optional[float] = None


class InstanceConfigTypeDef(BaseValidatorModel):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfigTypeDef


class StartInstanceOnboardingJobRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str
    encryptionConfig: EncryptionConfigTypeDef


class SourceTypeDef(BaseValidatorModel):
    customerProfilesSegmentArn: Optional[str] = None
    eventTrigger: Optional[EventTriggerTypeDef] = None


class GetCampaignStateBatchResponseTypeDef(BaseValidatorModel):
    successfulRequests: List[SuccessfulCampaignStateResponseTypeDef]
    failedRequests: List[FailedCampaignStateResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstanceOnboardingJobStatusResponseTypeDef(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartInstanceOnboardingJobResponseTypeDef(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IntegrationConfigTypeDef(BaseValidatorModel):
    customerProfiles: Optional[CustomerProfilesIntegrationConfigTypeDef] = None
    qConnect: Optional[QConnectIntegrationConfigTypeDef] = None


class IntegrationIdentifierTypeDef(BaseValidatorModel):
    customerProfiles: Optional[CustomerProfilesIntegrationIdentifierTypeDef] = None
    qConnect: Optional[QConnectIntegrationIdentifierTypeDef] = None


class IntegrationSummaryTypeDef(BaseValidatorModel):
    customerProfiles: Optional[CustomerProfilesIntegrationSummaryTypeDef] = None
    qConnect: Optional[QConnectIntegrationSummaryTypeDef] = None


class ListConnectInstanceIntegrationsRequestPaginateTypeDef(BaseValidatorModel):
    connectInstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class OpenHoursOutputTypeDef(BaseValidatorModel):
    dailyHours: Optional[Dict[DayOfWeekType, List[TimeRangeTypeDef]]] = None


class OpenHoursTypeDef(BaseValidatorModel):
    dailyHours: Optional[Mapping[DayOfWeekType, Sequence[TimeRangeTypeDef]]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ProfileOutboundRequestTypeDef(BaseValidatorModel):
    clientToken: str
    profileId: str
    expirationTime: Optional[TimestampTypeDef] = None


class ScheduleTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    refreshFrequency: Optional[str] = None


class TelephonyOutboundModeOutputTypeDef(BaseValidatorModel):
    progressive: Optional[ProgressiveConfigTypeDef] = None
    predictive: Optional[PredictiveConfigTypeDef] = None
    agentless: Optional[Dict[str, Any]] = None


class TelephonyOutboundModeTypeDef(BaseValidatorModel):
    progressive: Optional[ProgressiveConfigTypeDef] = None
    predictive: Optional[PredictiveConfigTypeDef] = None
    agentless: Optional[Mapping[str, Any]] = None


class FailedRequestTypeDef(BaseValidatorModel):
    pass


class SuccessfulRequestTypeDef(BaseValidatorModel):
    pass


class PutOutboundRequestBatchResponseTypeDef(BaseValidatorModel):
    successfulRequests: List[SuccessfulRequestTypeDef]
    failedRequests: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FailedProfileOutboundRequestTypeDef(BaseValidatorModel):
    pass


class SuccessfulProfileOutboundRequestTypeDef(BaseValidatorModel):
    pass


class PutProfileOutboundRequestBatchResponseTypeDef(BaseValidatorModel):
    successfulRequests: List[SuccessfulProfileOutboundRequestTypeDef]
    failedRequests: List[FailedProfileOutboundRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RestrictedPeriodsOutputTypeDef(BaseValidatorModel):
    restrictedPeriodList: Optional[List[RestrictedPeriodTypeDef]] = None


class RestrictedPeriodsTypeDef(BaseValidatorModel):
    restrictedPeriodList: Optional[Sequence[RestrictedPeriodTypeDef]] = None


class SmsChannelSubtypeConfigOutputTypeDef(BaseValidatorModel):
    outboundMode: SmsOutboundModeOutputTypeDef
    defaultOutboundConfig: SmsOutboundConfigTypeDef
    capacity: Optional[float] = None


class SmsChannelSubtypeConfigTypeDef(BaseValidatorModel):
    outboundMode: SmsOutboundModeTypeDef
    defaultOutboundConfig: SmsOutboundConfigTypeDef
    capacity: Optional[float] = None


class ChannelSubtypeParametersTypeDef(BaseValidatorModel):
    telephony: Optional[TelephonyChannelSubtypeParametersTypeDef] = None
    sms: Optional[SmsChannelSubtypeParametersTypeDef] = None
    email: Optional[EmailChannelSubtypeParametersTypeDef] = None


class ListCampaignsRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[CampaignFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCampaignsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[CampaignFiltersTypeDef] = None


class CampaignSummaryTypeDef(BaseValidatorModel):
    pass


class ListCampaignsResponseTypeDef(BaseValidatorModel):
    campaignSummaryList: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CommunicationLimitsConfigOutputTypeDef(BaseValidatorModel):
    allChannelSubtypes: Optional[CommunicationLimitsOutputTypeDef] = None


class CommunicationLimitsConfigTypeDef(BaseValidatorModel):
    allChannelSubtypes: Optional[CommunicationLimitsTypeDef] = None


class GetConnectInstanceConfigResponseTypeDef(BaseValidatorModel):
    connectInstanceConfig: InstanceConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutConnectInstanceIntegrationRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str
    integrationConfig: IntegrationConfigTypeDef


class DeleteConnectInstanceIntegrationRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str
    integrationIdentifier: IntegrationIdentifierTypeDef


class ListConnectInstanceIntegrationsResponseTypeDef(BaseValidatorModel):
    integrationSummaryList: List[IntegrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TelephonyChannelSubtypeConfigOutputTypeDef(BaseValidatorModel):
    outboundMode: TelephonyOutboundModeOutputTypeDef
    defaultOutboundConfig: TelephonyOutboundConfigTypeDef
    capacity: Optional[float] = None
    connectQueueId: Optional[str] = None


class TelephonyChannelSubtypeConfigTypeDef(BaseValidatorModel):
    outboundMode: TelephonyOutboundModeTypeDef
    defaultOutboundConfig: TelephonyOutboundConfigTypeDef
    capacity: Optional[float] = None
    connectQueueId: Optional[str] = None


class TimeWindowOutputTypeDef(BaseValidatorModel):
    openHours: OpenHoursOutputTypeDef
    restrictedPeriods: Optional[RestrictedPeriodsOutputTypeDef] = None


class TimeWindowTypeDef(BaseValidatorModel):
    openHours: OpenHoursTypeDef
    restrictedPeriods: Optional[RestrictedPeriodsTypeDef] = None


class OutboundRequestTypeDef(BaseValidatorModel):
    clientToken: str
    expirationTime: TimestampTypeDef
    channelSubtypeParameters: ChannelSubtypeParametersTypeDef


class ChannelSubtypeConfigOutputTypeDef(BaseValidatorModel):
    telephony: Optional[TelephonyChannelSubtypeConfigOutputTypeDef] = None
    sms: Optional[SmsChannelSubtypeConfigOutputTypeDef] = None
    email: Optional[EmailChannelSubtypeConfigOutputTypeDef] = None


class ChannelSubtypeConfigTypeDef(BaseValidatorModel):
    telephony: Optional[TelephonyChannelSubtypeConfigTypeDef] = None
    sms: Optional[SmsChannelSubtypeConfigTypeDef] = None
    email: Optional[EmailChannelSubtypeConfigTypeDef] = None


class CommunicationTimeConfigOutputTypeDef(BaseValidatorModel):
    localTimeZoneConfig: LocalTimeZoneConfigOutputTypeDef
    telephony: Optional[TimeWindowOutputTypeDef] = None
    sms: Optional[TimeWindowOutputTypeDef] = None
    email: Optional[TimeWindowOutputTypeDef] = None


class CommunicationTimeConfigTypeDef(BaseValidatorModel):
    localTimeZoneConfig: LocalTimeZoneConfigTypeDef
    telephony: Optional[TimeWindowTypeDef] = None
    sms: Optional[TimeWindowTypeDef] = None
    email: Optional[TimeWindowTypeDef] = None


class CampaignTypeDef(BaseValidatorModel):
    pass


class DescribeCampaignResponseTypeDef(BaseValidatorModel):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ChannelSubtypeConfigUnionTypeDef(BaseValidatorModel):
    pass


class ScheduleUnionTypeDef(BaseValidatorModel):
    pass


class CommunicationTimeConfigUnionTypeDef(BaseValidatorModel):
    pass


class CommunicationLimitsConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateCampaignRequestTypeDef(BaseValidatorModel):
    name: str
    connectInstanceId: str
    channelSubtypeConfig: ChannelSubtypeConfigUnionTypeDef
    source: Optional[SourceTypeDef] = None
    connectCampaignFlowArn: Optional[str] = None
    schedule: Optional[ScheduleUnionTypeDef] = None
    communicationTimeConfig: Optional[CommunicationTimeConfigUnionTypeDef] = None
    communicationLimitsOverride: Optional[CommunicationLimitsConfigUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None



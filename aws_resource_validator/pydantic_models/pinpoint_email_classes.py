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
from aws_resource_validator.pydantic_models.pinpoint_email_constants import *

class BlacklistEntry(BaseValidatorModel):
    RblName: Optional[str] = None
    ListingTime: Optional[datetime] = None
    Description: Optional[str] = None


class Content(BaseValidatorModel):
    Data: str
    Charset: Optional[str] = None


class CloudWatchDimensionConfiguration(BaseValidatorModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str


class DeliveryOptions(BaseValidatorModel):
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None


class SendingOptions(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class TrackingOptions(BaseValidatorModel):
    CustomRedirectDomain: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DkimAttributes(BaseValidatorModel):
    SigningEnabled: Optional[bool] = None
    Status: Optional[DkimStatusType] = None
    Tokens: Optional[List[str]] = None


class DomainIspPlacement(BaseValidatorModel):
    IspName: Optional[str] = None
    InboxRawCount: Optional[int] = None
    SpamRawCount: Optional[int] = None
    InboxPercentage: Optional[float] = None
    SpamPercentage: Optional[float] = None


class VolumeStatistics(BaseValidatorModel):
    InboxRawCount: Optional[int] = None
    SpamRawCount: Optional[int] = None
    ProjectedInbox: Optional[int] = None
    ProjectedSpam: Optional[int] = None


class DedicatedIp(BaseValidatorModel):
    Ip: str
    WarmupStatus: WarmupStatusType
    WarmupPercentage: int
    PoolName: Optional[str] = None


class DeleteConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str


class DeleteConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteDedicatedIpPoolRequest(BaseValidatorModel):
    PoolName: str


class DeleteEmailIdentityRequest(BaseValidatorModel):
    EmailIdentity: str


class DeliverabilityTestReport(BaseValidatorModel):
    ReportId: Optional[str] = None
    ReportName: Optional[str] = None
    Subject: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    CreateDate: Optional[datetime] = None
    DeliverabilityTestStatus: Optional[DeliverabilityTestStatusType] = None


class Destination(BaseValidatorModel):
    ToAddresses: Optional[Sequence[str]] = None
    CcAddresses: Optional[Sequence[str]] = None
    BccAddresses: Optional[Sequence[str]] = None


class DomainDeliverabilityCampaign(BaseValidatorModel):
    CampaignId: Optional[str] = None
    ImageUrl: Optional[str] = None
    Subject: Optional[str] = None
    FromAddress: Optional[str] = None
    SendingIps: Optional[List[str]] = None
    FirstSeenDateTime: Optional[datetime] = None
    LastSeenDateTime: Optional[datetime] = None
    InboxCount: Optional[int] = None
    SpamCount: Optional[int] = None
    ReadRate: Optional[float] = None
    DeleteRate: Optional[float] = None
    ReadDeleteRate: Optional[float] = None
    ProjectedVolume: Optional[int] = None
    Esps: Optional[List[str]] = None


class InboxPlacementTrackingOptionOutput(BaseValidatorModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[List[str]] = None


class Template(BaseValidatorModel):
    TemplateArn: Optional[str] = None
    TemplateData: Optional[str] = None


class KinesisFirehoseDestination(BaseValidatorModel):
    IamRoleArn: str
    DeliveryStreamArn: str


class PinpointDestination(BaseValidatorModel):
    ApplicationArn: Optional[str] = None


class SnsDestination(BaseValidatorModel):
    TopicArn: str


class SendQuota(BaseValidatorModel):
    Max24HourSend: Optional[float] = None
    MaxSendRate: Optional[float] = None
    SentLast24Hours: Optional[float] = None


class GetBlacklistReportsRequest(BaseValidatorModel):
    BlacklistItemNames: Sequence[str]


class GetConfigurationSetEventDestinationsRequest(BaseValidatorModel):
    ConfigurationSetName: str


class GetConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str


class ReputationOptionsOutput(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None


class GetDedicatedIpRequest(BaseValidatorModel):
    Ip: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetDedicatedIpsRequest(BaseValidatorModel):
    PoolName: Optional[str] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class GetDeliverabilityTestReportRequest(BaseValidatorModel):
    ReportId: str


class PlacementStatistics(BaseValidatorModel):
    InboxPercentage: Optional[float] = None
    SpamPercentage: Optional[float] = None
    MissingPercentage: Optional[float] = None
    SpfPercentage: Optional[float] = None
    DkimPercentage: Optional[float] = None


class GetDomainDeliverabilityCampaignRequest(BaseValidatorModel):
    CampaignId: str


class GetEmailIdentityRequest(BaseValidatorModel):
    EmailIdentity: str


class MailFromAttributes(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType


class IdentityInfo(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    IdentityName: Optional[str] = None
    SendingEnabled: Optional[bool] = None


class InboxPlacementTrackingOption(BaseValidatorModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[Sequence[str]] = None


class ListConfigurationSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListDedicatedIpPoolsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListDeliverabilityTestReportsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListEmailIdentitiesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class MessageTag(BaseValidatorModel):
    Name: str
    Value: str


class PutAccountDedicatedIpWarmupAttributesRequest(BaseValidatorModel):
    AutoWarmupEnabled: Optional[bool] = None


class PutAccountSendingAttributesRequest(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None


class PutConfigurationSetDeliveryOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None


class PutConfigurationSetReputationOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    ReputationMetricsEnabled: Optional[bool] = None


class PutConfigurationSetSendingOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    SendingEnabled: Optional[bool] = None


class PutConfigurationSetTrackingOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    CustomRedirectDomain: Optional[str] = None


class PutDedicatedIpInPoolRequest(BaseValidatorModel):
    Ip: str
    DestinationPoolName: str


class PutDedicatedIpWarmupAttributesRequest(BaseValidatorModel):
    Ip: str
    WarmupPercentage: int


class PutEmailIdentityDkimAttributesRequest(BaseValidatorModel):
    EmailIdentity: str
    SigningEnabled: Optional[bool] = None


class PutEmailIdentityFeedbackAttributesRequest(BaseValidatorModel):
    EmailIdentity: str
    EmailForwardingEnabled: Optional[bool] = None


class PutEmailIdentityMailFromAttributesRequest(BaseValidatorModel):
    EmailIdentity: str
    MailFromDomain: Optional[str] = None
    BehaviorOnMxFailure: Optional[BehaviorOnMxFailureType] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class Blob(BaseValidatorModel):
    pass


class RawMessage(BaseValidatorModel):
    Data: Blob


class CloudWatchDestinationOutput(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfiguration]


class CloudWatchDestination(BaseValidatorModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfiguration]


class CreateDedicatedIpPoolRequest(BaseValidatorModel):
    PoolName: str
    Tags: Optional[Sequence[Tag]] = None


class CreateEmailIdentityRequest(BaseValidatorModel):
    EmailIdentity: str
    Tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class CreateDeliverabilityTestReportResponse(BaseValidatorModel):
    ReportId: str
    DeliverabilityTestStatus: DeliverabilityTestStatusType
    ResponseMetadata: ResponseMetadata


class GetBlacklistReportsResponse(BaseValidatorModel):
    BlacklistReport: Dict[str, List[BlacklistEntry]]
    ResponseMetadata: ResponseMetadata


class ListConfigurationSetsResponse(BaseValidatorModel):
    ConfigurationSets: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDedicatedIpPoolsResponse(BaseValidatorModel):
    DedicatedIpPools: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class SendEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class CreateEmailIdentityResponse(BaseValidatorModel):
    IdentityType: IdentityTypeType
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributes
    ResponseMetadata: ResponseMetadata


class DailyVolume(BaseValidatorModel):
    StartDate: Optional[datetime] = None
    VolumeStatistics: Optional[VolumeStatistics] = None
    DomainIspPlacements: Optional[List[DomainIspPlacement]] = None


class OverallVolume(BaseValidatorModel):
    VolumeStatistics: Optional[VolumeStatistics] = None
    ReadRatePercent: Optional[float] = None
    DomainIspPlacements: Optional[List[DomainIspPlacement]] = None


class GetDedicatedIpResponse(BaseValidatorModel):
    DedicatedIp: DedicatedIp
    ResponseMetadata: ResponseMetadata


class GetDedicatedIpsResponse(BaseValidatorModel):
    DedicatedIps: List[DedicatedIp]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDeliverabilityTestReportsResponse(BaseValidatorModel):
    DeliverabilityTestReports: List[DeliverabilityTestReport]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDomainDeliverabilityCampaignResponse(BaseValidatorModel):
    DomainDeliverabilityCampaign: DomainDeliverabilityCampaign
    ResponseMetadata: ResponseMetadata


class ListDomainDeliverabilityCampaignsResponse(BaseValidatorModel):
    DomainDeliverabilityCampaigns: List[DomainDeliverabilityCampaign]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DomainDeliverabilityTrackingOptionOutput(BaseValidatorModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[datetime] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionOutput] = None


class Timestamp(BaseValidatorModel):
    pass


class GetDomainStatisticsReportRequest(BaseValidatorModel):
    Domain: str
    StartDate: Timestamp
    EndDate: Timestamp


class ListDomainDeliverabilityCampaignsRequest(BaseValidatorModel):
    StartDate: Timestamp
    EndDate: Timestamp
    SubscribedDomain: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ReputationOptions(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[Timestamp] = None


class GetAccountResponse(BaseValidatorModel):
    SendQuota: SendQuota
    SendingEnabled: bool
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    ResponseMetadata: ResponseMetadata


class GetConfigurationSetResponse(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptions
    DeliveryOptions: DeliveryOptions
    ReputationOptions: ReputationOptionsOutput
    SendingOptions: SendingOptions
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class GetDedicatedIpsRequestPaginate(BaseValidatorModel):
    PoolName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDedicatedIpPoolsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeliverabilityTestReportsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEmailIdentitiesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class IspPlacement(BaseValidatorModel):
    IspName: Optional[str] = None
    PlacementStatistics: Optional[PlacementStatistics] = None


class GetEmailIdentityResponse(BaseValidatorModel):
    IdentityType: IdentityTypeType
    FeedbackForwardingStatus: bool
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributes
    MailFromAttributes: MailFromAttributes
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ListEmailIdentitiesResponse(BaseValidatorModel):
    EmailIdentities: List[IdentityInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Body(BaseValidatorModel):
    pass


class Message(BaseValidatorModel):
    Subject: Content
    Body: Body


class EventDestination(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutput] = None
    SnsDestination: Optional[SnsDestination] = None
    PinpointDestination: Optional[PinpointDestination] = None


class GetDomainStatisticsReportResponse(BaseValidatorModel):
    OverallVolume: OverallVolume
    DailyVolumes: List[DailyVolume]
    ResponseMetadata: ResponseMetadata


class GetDeliverabilityDashboardOptionsResponse(BaseValidatorModel):
    DashboardEnabled: bool
    SubscriptionExpiryDate: datetime
    AccountStatus: DeliverabilityDashboardAccountStatusType
    ActiveSubscribedDomains: List[DomainDeliverabilityTrackingOptionOutput]
    PendingExpirationSubscribedDomains: List[DomainDeliverabilityTrackingOptionOutput]
    ResponseMetadata: ResponseMetadata


class GetDeliverabilityTestReportResponse(BaseValidatorModel):
    DeliverabilityTestReport: DeliverabilityTestReport
    OverallPlacement: PlacementStatistics
    IspPlacements: List[IspPlacement]
    Message: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class InboxPlacementTrackingOptionUnion(BaseValidatorModel):
    pass


class DomainDeliverabilityTrackingOption(BaseValidatorModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[Timestamp] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionUnion] = None


class EmailContent(BaseValidatorModel):
    Simple: Optional[Message] = None
    Raw: Optional[RawMessage] = None
    Template: Optional[Template] = None


class GetConfigurationSetEventDestinationsResponse(BaseValidatorModel):
    EventDestinations: List[EventDestination]
    ResponseMetadata: ResponseMetadata


class CloudWatchDestinationUnion(BaseValidatorModel):
    pass


class EventDestinationDefinition(BaseValidatorModel):
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    CloudWatchDestination: Optional[CloudWatchDestinationUnion] = None
    SnsDestination: Optional[SnsDestination] = None
    PinpointDestination: Optional[PinpointDestination] = None


class ReputationOptionsUnion(BaseValidatorModel):
    pass


class CreateConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: Optional[TrackingOptions] = None
    DeliveryOptions: Optional[DeliveryOptions] = None
    ReputationOptions: Optional[ReputationOptionsUnion] = None
    SendingOptions: Optional[SendingOptions] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateDeliverabilityTestReportRequest(BaseValidatorModel):
    FromEmailAddress: str
    Content: EmailContent
    ReportName: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class SendEmailRequest(BaseValidatorModel):
    Destination: Destination
    Content: EmailContent
    FromEmailAddress: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    EmailTags: Optional[Sequence[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None


class CreateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinition


class UpdateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinition


class DomainDeliverabilityTrackingOptionUnion(BaseValidatorModel):
    pass


class PutDeliverabilityDashboardOptionRequest(BaseValidatorModel):
    DashboardEnabled: bool
    SubscribedDomains: Optional[Sequence[DomainDeliverabilityTrackingOptionUnion]] = None



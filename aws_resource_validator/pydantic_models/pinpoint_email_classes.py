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

class BlacklistEntryTypeDef(BaseValidatorModel):
    RblName: Optional[str] = None
    ListingTime: Optional[datetime] = None
    Description: Optional[str] = None


class ContentTypeDef(BaseValidatorModel):
    Data: str
    Charset: Optional[str] = None


class CloudWatchDimensionConfigurationTypeDef(BaseValidatorModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str


class DeliveryOptionsTypeDef(BaseValidatorModel):
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None


class SendingOptionsTypeDef(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class TrackingOptionsTypeDef(BaseValidatorModel):
    CustomRedirectDomain: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DkimAttributesTypeDef(BaseValidatorModel):
    SigningEnabled: Optional[bool] = None
    Status: Optional[DkimStatusType] = None
    Tokens: Optional[List[str]] = None


class DomainIspPlacementTypeDef(BaseValidatorModel):
    IspName: Optional[str] = None
    InboxRawCount: Optional[int] = None
    SpamRawCount: Optional[int] = None
    InboxPercentage: Optional[float] = None
    SpamPercentage: Optional[float] = None


class VolumeStatisticsTypeDef(BaseValidatorModel):
    InboxRawCount: Optional[int] = None
    SpamRawCount: Optional[int] = None
    ProjectedInbox: Optional[int] = None
    ProjectedSpam: Optional[int] = None


class DedicatedIpTypeDef(BaseValidatorModel):
    Ip: str
    WarmupStatus: WarmupStatusType
    WarmupPercentage: int
    PoolName: Optional[str] = None


class DeleteConfigurationSetEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str


class DeleteConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteDedicatedIpPoolRequestTypeDef(BaseValidatorModel):
    PoolName: str


class DeleteEmailIdentityRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str


class DeliverabilityTestReportTypeDef(BaseValidatorModel):
    ReportId: Optional[str] = None
    ReportName: Optional[str] = None
    Subject: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    CreateDate: Optional[datetime] = None
    DeliverabilityTestStatus: Optional[DeliverabilityTestStatusType] = None


class DestinationTypeDef(BaseValidatorModel):
    ToAddresses: Optional[Sequence[str]] = None
    CcAddresses: Optional[Sequence[str]] = None
    BccAddresses: Optional[Sequence[str]] = None


class DomainDeliverabilityCampaignTypeDef(BaseValidatorModel):
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


class InboxPlacementTrackingOptionOutputTypeDef(BaseValidatorModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[List[str]] = None


class TemplateTypeDef(BaseValidatorModel):
    TemplateArn: Optional[str] = None
    TemplateData: Optional[str] = None


class KinesisFirehoseDestinationTypeDef(BaseValidatorModel):
    IamRoleArn: str
    DeliveryStreamArn: str


class PinpointDestinationTypeDef(BaseValidatorModel):
    ApplicationArn: Optional[str] = None


class SnsDestinationTypeDef(BaseValidatorModel):
    TopicArn: str


class SendQuotaTypeDef(BaseValidatorModel):
    Max24HourSend: Optional[float] = None
    MaxSendRate: Optional[float] = None
    SentLast24Hours: Optional[float] = None


class GetBlacklistReportsRequestTypeDef(BaseValidatorModel):
    BlacklistItemNames: Sequence[str]


class GetConfigurationSetEventDestinationsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class GetConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class ReputationOptionsOutputTypeDef(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None


class GetDedicatedIpRequestTypeDef(BaseValidatorModel):
    Ip: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetDedicatedIpsRequestTypeDef(BaseValidatorModel):
    PoolName: Optional[str] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class GetDeliverabilityTestReportRequestTypeDef(BaseValidatorModel):
    ReportId: str


class PlacementStatisticsTypeDef(BaseValidatorModel):
    InboxPercentage: Optional[float] = None
    SpamPercentage: Optional[float] = None
    MissingPercentage: Optional[float] = None
    SpfPercentage: Optional[float] = None
    DkimPercentage: Optional[float] = None


class GetDomainDeliverabilityCampaignRequestTypeDef(BaseValidatorModel):
    CampaignId: str


class GetEmailIdentityRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str


class MailFromAttributesTypeDef(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType


class IdentityInfoTypeDef(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    IdentityName: Optional[str] = None
    SendingEnabled: Optional[bool] = None


class InboxPlacementTrackingOptionTypeDef(BaseValidatorModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[Sequence[str]] = None


class ListConfigurationSetsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListDedicatedIpPoolsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListDeliverabilityTestReportsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListEmailIdentitiesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class MessageTagTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class PutAccountDedicatedIpWarmupAttributesRequestTypeDef(BaseValidatorModel):
    AutoWarmupEnabled: Optional[bool] = None


class PutAccountSendingAttributesRequestTypeDef(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None


class PutConfigurationSetDeliveryOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None


class PutConfigurationSetReputationOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    ReputationMetricsEnabled: Optional[bool] = None


class PutConfigurationSetSendingOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    SendingEnabled: Optional[bool] = None


class PutConfigurationSetTrackingOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    CustomRedirectDomain: Optional[str] = None


class PutDedicatedIpInPoolRequestTypeDef(BaseValidatorModel):
    Ip: str
    DestinationPoolName: str


class PutDedicatedIpWarmupAttributesRequestTypeDef(BaseValidatorModel):
    Ip: str
    WarmupPercentage: int


class PutEmailIdentityDkimAttributesRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    SigningEnabled: Optional[bool] = None


class PutEmailIdentityFeedbackAttributesRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    EmailForwardingEnabled: Optional[bool] = None


class PutEmailIdentityMailFromAttributesRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    MailFromDomain: Optional[str] = None
    BehaviorOnMxFailure: Optional[BehaviorOnMxFailureType] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class BlobTypeDef(BaseValidatorModel):
    pass


class RawMessageTypeDef(BaseValidatorModel):
    Data: BlobTypeDef


class CloudWatchDestinationOutputTypeDef(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfigurationTypeDef]


class CloudWatchDestinationTypeDef(BaseValidatorModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]


class CreateDedicatedIpPoolRequestTypeDef(BaseValidatorModel):
    PoolName: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateEmailIdentityRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateDeliverabilityTestReportResponseTypeDef(BaseValidatorModel):
    ReportId: str
    DeliverabilityTestStatus: DeliverabilityTestStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetBlacklistReportsResponseTypeDef(BaseValidatorModel):
    BlacklistReport: Dict[str, List[BlacklistEntryTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigurationSetsResponseTypeDef(BaseValidatorModel):
    ConfigurationSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDedicatedIpPoolsResponseTypeDef(BaseValidatorModel):
    DedicatedIpPools: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SendEmailResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEmailIdentityResponseTypeDef(BaseValidatorModel):
    IdentityType: IdentityTypeType
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DailyVolumeTypeDef(BaseValidatorModel):
    StartDate: Optional[datetime] = None
    VolumeStatistics: Optional[VolumeStatisticsTypeDef] = None
    DomainIspPlacements: Optional[List[DomainIspPlacementTypeDef]] = None


class OverallVolumeTypeDef(BaseValidatorModel):
    VolumeStatistics: Optional[VolumeStatisticsTypeDef] = None
    ReadRatePercent: Optional[float] = None
    DomainIspPlacements: Optional[List[DomainIspPlacementTypeDef]] = None


class GetDedicatedIpResponseTypeDef(BaseValidatorModel):
    DedicatedIp: DedicatedIpTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDedicatedIpsResponseTypeDef(BaseValidatorModel):
    DedicatedIps: List[DedicatedIpTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDeliverabilityTestReportsResponseTypeDef(BaseValidatorModel):
    DeliverabilityTestReports: List[DeliverabilityTestReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetDomainDeliverabilityCampaignResponseTypeDef(BaseValidatorModel):
    DomainDeliverabilityCampaign: DomainDeliverabilityCampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDomainDeliverabilityCampaignsResponseTypeDef(BaseValidatorModel):
    DomainDeliverabilityCampaigns: List[DomainDeliverabilityCampaignTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DomainDeliverabilityTrackingOptionOutputTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[datetime] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionOutputTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetDomainStatisticsReportRequestTypeDef(BaseValidatorModel):
    Domain: str
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef


class ListDomainDeliverabilityCampaignsRequestTypeDef(BaseValidatorModel):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    SubscribedDomain: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ReputationOptionsTypeDef(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[TimestampTypeDef] = None


class GetAccountResponseTypeDef(BaseValidatorModel):
    SendQuota: SendQuotaTypeDef
    SendingEnabled: bool
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfigurationSetResponseTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsOutputTypeDef
    SendingOptions: SendingOptionsTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDedicatedIpsRequestPaginateTypeDef(BaseValidatorModel):
    PoolName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfigurationSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDedicatedIpPoolsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeliverabilityTestReportsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEmailIdentitiesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class IspPlacementTypeDef(BaseValidatorModel):
    IspName: Optional[str] = None
    PlacementStatistics: Optional[PlacementStatisticsTypeDef] = None


class GetEmailIdentityResponseTypeDef(BaseValidatorModel):
    IdentityType: IdentityTypeType
    FeedbackForwardingStatus: bool
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    MailFromAttributes: MailFromAttributesTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListEmailIdentitiesResponseTypeDef(BaseValidatorModel):
    EmailIdentities: List[IdentityInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BodyTypeDef(BaseValidatorModel):
    pass


class MessageTypeDef(BaseValidatorModel):
    Subject: ContentTypeDef
    Body: BodyTypeDef


class EventDestinationTypeDef(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutputTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None


class GetDomainStatisticsReportResponseTypeDef(BaseValidatorModel):
    OverallVolume: OverallVolumeTypeDef
    DailyVolumes: List[DailyVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeliverabilityDashboardOptionsResponseTypeDef(BaseValidatorModel):
    DashboardEnabled: bool
    SubscriptionExpiryDate: datetime
    AccountStatus: DeliverabilityDashboardAccountStatusType
    ActiveSubscribedDomains: List[DomainDeliverabilityTrackingOptionOutputTypeDef]
    PendingExpirationSubscribedDomains: List[DomainDeliverabilityTrackingOptionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeliverabilityTestReportResponseTypeDef(BaseValidatorModel):
    DeliverabilityTestReport: DeliverabilityTestReportTypeDef
    OverallPlacement: PlacementStatisticsTypeDef
    IspPlacements: List[IspPlacementTypeDef]
    Message: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class InboxPlacementTrackingOptionUnionTypeDef(BaseValidatorModel):
    pass


class DomainDeliverabilityTrackingOptionTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[TimestampTypeDef] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionUnionTypeDef] = None


class EmailContentTypeDef(BaseValidatorModel):
    Simple: Optional[MessageTypeDef] = None
    Raw: Optional[RawMessageTypeDef] = None
    Template: Optional[TemplateTypeDef] = None


class GetConfigurationSetEventDestinationsResponseTypeDef(BaseValidatorModel):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CloudWatchDestinationUnionTypeDef(BaseValidatorModel):
    pass


class EventDestinationDefinitionTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationUnionTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None


class ReputationOptionsUnionTypeDef(BaseValidatorModel):
    pass


class CreateConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: Optional[TrackingOptionsTypeDef] = None
    DeliveryOptions: Optional[DeliveryOptionsTypeDef] = None
    ReputationOptions: Optional[ReputationOptionsUnionTypeDef] = None
    SendingOptions: Optional[SendingOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateDeliverabilityTestReportRequestTypeDef(BaseValidatorModel):
    FromEmailAddress: str
    Content: EmailContentTypeDef
    ReportName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class SendEmailRequestTypeDef(BaseValidatorModel):
    Destination: DestinationTypeDef
    Content: EmailContentTypeDef
    FromEmailAddress: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    EmailTags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None


class CreateConfigurationSetEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef


class UpdateConfigurationSetEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef


class DomainDeliverabilityTrackingOptionUnionTypeDef(BaseValidatorModel):
    pass


class PutDeliverabilityDashboardOptionRequestTypeDef(BaseValidatorModel):
    DashboardEnabled: bool
    SubscribedDomains: Optional[Sequence[DomainDeliverabilityTrackingOptionUnionTypeDef]] = None



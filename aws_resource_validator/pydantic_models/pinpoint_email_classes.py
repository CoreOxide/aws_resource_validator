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
from aws_resource_validator.pydantic_models.pinpoint_email_constants import *

class BlacklistEntryTypeDef(BaseModel):
    RblName: Optional[str] = None
    ListingTime: Optional[datetime] = None
    Description: Optional[str] = None

class ContentTypeDef(BaseModel):
    Data: str
    Charset: Optional[str] = None

class CloudWatchDimensionConfigurationTypeDef(BaseModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str

class DeliveryOptionsTypeDef(BaseModel):
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None

class SendingOptionsTypeDef(BaseModel):
    SendingEnabled: Optional[bool] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class TrackingOptionsTypeDef(BaseModel):
    CustomRedirectDomain: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DkimAttributesTypeDef(BaseModel):
    SigningEnabled: Optional[bool] = None
    Status: Optional[DkimStatusType] = None
    Tokens: Optional[List[str]] = None

class DomainIspPlacementTypeDef(BaseModel):
    IspName: Optional[str] = None
    InboxRawCount: Optional[int] = None
    SpamRawCount: Optional[int] = None
    InboxPercentage: Optional[float] = None
    SpamPercentage: Optional[float] = None

class VolumeStatisticsTypeDef(BaseModel):
    InboxRawCount: Optional[int] = None
    SpamRawCount: Optional[int] = None
    ProjectedInbox: Optional[int] = None
    ProjectedSpam: Optional[int] = None

class DedicatedIpTypeDef(BaseModel):
    Ip: str
    WarmupStatus: WarmupStatusType
    WarmupPercentage: int
    PoolName: Optional[str] = None

class DeleteConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class DeleteDedicatedIpPoolRequestRequestTypeDef(BaseModel):
    PoolName: str

class DeleteEmailIdentityRequestRequestTypeDef(BaseModel):
    EmailIdentity: str

class DeliverabilityTestReportTypeDef(BaseModel):
    ReportId: Optional[str] = None
    ReportName: Optional[str] = None
    Subject: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    CreateDate: Optional[datetime] = None
    DeliverabilityTestStatus: Optional[DeliverabilityTestStatusType] = None

class DestinationTypeDef(BaseModel):
    ToAddresses: Optional[Sequence[str]] = None
    CcAddresses: Optional[Sequence[str]] = None
    BccAddresses: Optional[Sequence[str]] = None

class DomainDeliverabilityCampaignTypeDef(BaseModel):
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

class InboxPlacementTrackingOptionTypeDef(BaseModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[List[str]] = None

class TemplateTypeDef(BaseModel):
    TemplateArn: Optional[str] = None
    TemplateData: Optional[str] = None

class KinesisFirehoseDestinationTypeDef(BaseModel):
    IamRoleArn: str
    DeliveryStreamArn: str

class PinpointDestinationTypeDef(BaseModel):
    ApplicationArn: Optional[str] = None

class SnsDestinationTypeDef(BaseModel):
    TopicArn: str

class SendQuotaTypeDef(BaseModel):
    Max24HourSend: Optional[float] = None
    MaxSendRate: Optional[float] = None
    SentLast24Hours: Optional[float] = None

class GetBlacklistReportsRequestRequestTypeDef(BaseModel):
    BlacklistItemNames: Sequence[str]

class GetConfigurationSetEventDestinationsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class GetConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class GetDedicatedIpRequestRequestTypeDef(BaseModel):
    Ip: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetDedicatedIpsRequestRequestTypeDef(BaseModel):
    PoolName: Optional[str] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class GetDeliverabilityTestReportRequestRequestTypeDef(BaseModel):
    ReportId: str

class PlacementStatisticsTypeDef(BaseModel):
    InboxPercentage: Optional[float] = None
    SpamPercentage: Optional[float] = None
    MissingPercentage: Optional[float] = None
    SpfPercentage: Optional[float] = None
    DkimPercentage: Optional[float] = None

class GetDomainDeliverabilityCampaignRequestRequestTypeDef(BaseModel):
    CampaignId: str

class GetEmailIdentityRequestRequestTypeDef(BaseModel):
    EmailIdentity: str

class MailFromAttributesTypeDef(BaseModel):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType

class IdentityInfoTypeDef(BaseModel):
    IdentityType: Optional[IdentityTypeType] = None
    IdentityName: Optional[str] = None
    SendingEnabled: Optional[bool] = None

class ListConfigurationSetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListDedicatedIpPoolsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListDeliverabilityTestReportsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListEmailIdentitiesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class MessageTagTypeDef(BaseModel):
    Name: str
    Value: str

class PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef(BaseModel):
    AutoWarmupEnabled: Optional[bool] = None

class PutAccountSendingAttributesRequestRequestTypeDef(BaseModel):
    SendingEnabled: Optional[bool] = None

class PutConfigurationSetDeliveryOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None

class PutConfigurationSetReputationOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    ReputationMetricsEnabled: Optional[bool] = None

class PutConfigurationSetSendingOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    SendingEnabled: Optional[bool] = None

class PutConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    CustomRedirectDomain: Optional[str] = None

class PutDedicatedIpInPoolRequestRequestTypeDef(BaseModel):
    Ip: str
    DestinationPoolName: str

class PutDedicatedIpWarmupAttributesRequestRequestTypeDef(BaseModel):
    Ip: str
    WarmupPercentage: int

class PutEmailIdentityDkimAttributesRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    SigningEnabled: Optional[bool] = None

class PutEmailIdentityFeedbackAttributesRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    EmailForwardingEnabled: Optional[bool] = None

class PutEmailIdentityMailFromAttributesRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    MailFromDomain: Optional[str] = None
    BehaviorOnMxFailure: Optional[BehaviorOnMxFailureType] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class RawMessageTypeDef(BaseModel):
    Data: BlobTypeDef

class BodyTypeDef(BaseModel):
    Text: Optional[ContentTypeDef] = None
    Html: Optional[ContentTypeDef] = None

class CloudWatchDestinationTypeDef(BaseModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]

class CreateDedicatedIpPoolRequestRequestTypeDef(BaseModel):
    PoolName: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEmailIdentityRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateDeliverabilityTestReportResponseTypeDef(BaseModel):
    ReportId: str
    DeliverabilityTestStatus: DeliverabilityTestStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlacklistReportsResponseTypeDef(BaseModel):
    BlacklistReport: Dict[str, List[BlacklistEntryTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsResponseTypeDef(BaseModel):
    ConfigurationSets: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDedicatedIpPoolsResponseTypeDef(BaseModel):
    DedicatedIpPools: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEmailIdentityResponseTypeDef(BaseModel):
    IdentityType: IdentityTypeType
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DailyVolumeTypeDef(BaseModel):
    StartDate: Optional[datetime] = None
    VolumeStatistics: Optional[VolumeStatisticsTypeDef] = None
    DomainIspPlacements: Optional[List[DomainIspPlacementTypeDef]] = None

class OverallVolumeTypeDef(BaseModel):
    VolumeStatistics: Optional[VolumeStatisticsTypeDef] = None
    ReadRatePercent: Optional[float] = None
    DomainIspPlacements: Optional[List[DomainIspPlacementTypeDef]] = None

class GetDedicatedIpResponseTypeDef(BaseModel):
    DedicatedIp: DedicatedIpTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDedicatedIpsResponseTypeDef(BaseModel):
    DedicatedIps: List[DedicatedIpTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeliverabilityTestReportsResponseTypeDef(BaseModel):
    DeliverabilityTestReports: List[DeliverabilityTestReportTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainDeliverabilityCampaignResponseTypeDef(BaseModel):
    DomainDeliverabilityCampaign: DomainDeliverabilityCampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainDeliverabilityCampaignsResponseTypeDef(BaseModel):
    DomainDeliverabilityCampaigns: List[DomainDeliverabilityCampaignTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DomainDeliverabilityTrackingOptionTypeDef(BaseModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[datetime] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionTypeDef] = None

class GetAccountResponseTypeDef(BaseModel):
    SendQuota: SendQuotaTypeDef
    SendingEnabled: bool
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef(BaseModel):
    PoolName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class IspPlacementTypeDef(BaseModel):
    IspName: Optional[str] = None
    PlacementStatistics: Optional[PlacementStatisticsTypeDef] = None

class GetDomainStatisticsReportRequestRequestTypeDef(BaseModel):
    Domain: str
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef

class ListDomainDeliverabilityCampaignsRequestRequestTypeDef(BaseModel):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    SubscribedDomain: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ReputationOptionsTypeDef(BaseModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[TimestampTypeDef] = None

class GetEmailIdentityResponseTypeDef(BaseModel):
    IdentityType: IdentityTypeType
    FeedbackForwardingStatus: bool
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    MailFromAttributes: MailFromAttributesTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEmailIdentitiesResponseTypeDef(BaseModel):
    EmailIdentities: List[IdentityInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MessageTypeDef(BaseModel):
    Subject: ContentTypeDef
    Body: BodyTypeDef

class EventDestinationDefinitionTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None

class EventDestinationTypeDef(BaseModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None

class GetDomainStatisticsReportResponseTypeDef(BaseModel):
    OverallVolume: OverallVolumeTypeDef
    DailyVolumes: List[DailyVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliverabilityDashboardOptionsResponseTypeDef(BaseModel):
    DashboardEnabled: bool
    SubscriptionExpiryDate: datetime
    AccountStatus: DeliverabilityDashboardAccountStatusType
    ActiveSubscribedDomains: List[DomainDeliverabilityTrackingOptionTypeDef]
    PendingExpirationSubscribedDomains: List[DomainDeliverabilityTrackingOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliverabilityDashboardOptionRequestRequestTypeDef(BaseModel):
    DashboardEnabled: bool
    SubscribedDomains: Optional[Sequence[DomainDeliverabilityTrackingOptionTypeDef]] = None

class GetDeliverabilityTestReportResponseTypeDef(BaseModel):
    DeliverabilityTestReport: DeliverabilityTestReportTypeDef
    OverallPlacement: PlacementStatisticsTypeDef
    IspPlacements: List[IspPlacementTypeDef]
    Message: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    TrackingOptions: Optional[TrackingOptionsTypeDef] = None
    DeliveryOptions: Optional[DeliveryOptionsTypeDef] = None
    ReputationOptions: Optional[ReputationOptionsTypeDef] = None
    SendingOptions: Optional[SendingOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetConfigurationSetResponseTypeDef(BaseModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsTypeDef
    SendingOptions: SendingOptionsTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmailContentTypeDef(BaseModel):
    Simple: Optional[MessageTypeDef] = None
    Raw: Optional[RawMessageTypeDef] = None
    Template: Optional[TemplateTypeDef] = None

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class GetConfigurationSetEventDestinationsResponseTypeDef(BaseModel):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeliverabilityTestReportRequestRequestTypeDef(BaseModel):
    FromEmailAddress: str
    Content: EmailContentTypeDef
    ReportName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class SendEmailRequestRequestTypeDef(BaseModel):
    Destination: DestinationTypeDef
    Content: EmailContentTypeDef
    FromEmailAddress: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    EmailTags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None


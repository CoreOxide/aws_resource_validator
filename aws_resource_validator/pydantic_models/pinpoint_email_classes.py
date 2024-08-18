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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class DeleteConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class DeleteDedicatedIpPoolRequestRequestTypeDef(BaseValidatorModel):
    PoolName: str

class DeleteEmailIdentityRequestRequestTypeDef(BaseValidatorModel):
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

class InboxPlacementTrackingOptionTypeDef(BaseValidatorModel):
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

class GetBlacklistReportsRequestRequestTypeDef(BaseValidatorModel):
    BlacklistItemNames: Sequence[str]

class GetConfigurationSetEventDestinationsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class GetConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class GetDedicatedIpRequestRequestTypeDef(BaseValidatorModel):
    Ip: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetDedicatedIpsRequestRequestTypeDef(BaseValidatorModel):
    PoolName: Optional[str] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class GetDeliverabilityTestReportRequestRequestTypeDef(BaseValidatorModel):
    ReportId: str

class PlacementStatisticsTypeDef(BaseValidatorModel):
    InboxPercentage: Optional[float] = None
    SpamPercentage: Optional[float] = None
    MissingPercentage: Optional[float] = None
    SpfPercentage: Optional[float] = None
    DkimPercentage: Optional[float] = None

class GetDomainDeliverabilityCampaignRequestRequestTypeDef(BaseValidatorModel):
    CampaignId: str

class GetEmailIdentityRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str

class MailFromAttributesTypeDef(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType

class IdentityInfoTypeDef(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    IdentityName: Optional[str] = None
    SendingEnabled: Optional[bool] = None

class ListConfigurationSetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListDedicatedIpPoolsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListDeliverabilityTestReportsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListEmailIdentitiesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class MessageTagTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef(BaseValidatorModel):
    AutoWarmupEnabled: Optional[bool] = None

class PutAccountSendingAttributesRequestRequestTypeDef(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None

class PutConfigurationSetDeliveryOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None

class PutConfigurationSetReputationOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    ReputationMetricsEnabled: Optional[bool] = None

class PutConfigurationSetSendingOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    SendingEnabled: Optional[bool] = None

class PutConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    CustomRedirectDomain: Optional[str] = None

class PutDedicatedIpInPoolRequestRequestTypeDef(BaseValidatorModel):
    Ip: str
    DestinationPoolName: str

class PutDedicatedIpWarmupAttributesRequestRequestTypeDef(BaseValidatorModel):
    Ip: str
    WarmupPercentage: int

class PutEmailIdentityDkimAttributesRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    SigningEnabled: Optional[bool] = None

class PutEmailIdentityFeedbackAttributesRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    EmailForwardingEnabled: Optional[bool] = None

class PutEmailIdentityMailFromAttributesRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    MailFromDomain: Optional[str] = None
    BehaviorOnMxFailure: Optional[BehaviorOnMxFailureType] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class RawMessageTypeDef(BaseValidatorModel):
    Data: BlobTypeDef

class BodyTypeDef(BaseValidatorModel):
    Text: Optional[ContentTypeDef] = None
    Html: Optional[ContentTypeDef] = None

class CloudWatchDestinationTypeDef(BaseValidatorModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]

class CreateDedicatedIpPoolRequestRequestTypeDef(BaseValidatorModel):
    PoolName: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEmailIdentityRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDedicatedIpPoolsResponseTypeDef(BaseValidatorModel):
    DedicatedIpPools: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeliverabilityTestReportsResponseTypeDef(BaseValidatorModel):
    DeliverabilityTestReports: List[DeliverabilityTestReportTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainDeliverabilityCampaignResponseTypeDef(BaseValidatorModel):
    DomainDeliverabilityCampaign: DomainDeliverabilityCampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainDeliverabilityCampaignsResponseTypeDef(BaseValidatorModel):
    DomainDeliverabilityCampaigns: List[DomainDeliverabilityCampaignTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DomainDeliverabilityTrackingOptionTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[datetime] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionTypeDef] = None

class GetAccountResponseTypeDef(BaseValidatorModel):
    SendQuota: SendQuotaTypeDef
    SendingEnabled: bool
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef(BaseValidatorModel):
    PoolName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class IspPlacementTypeDef(BaseValidatorModel):
    IspName: Optional[str] = None
    PlacementStatistics: Optional[PlacementStatisticsTypeDef] = None

class GetDomainStatisticsReportRequestRequestTypeDef(BaseValidatorModel):
    Domain: str
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef

class ListDomainDeliverabilityCampaignsRequestRequestTypeDef(BaseValidatorModel):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    SubscribedDomain: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ReputationOptionsTypeDef(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[TimestampTypeDef] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MessageTypeDef(BaseValidatorModel):
    Subject: ContentTypeDef
    Body: BodyTypeDef

class EventDestinationDefinitionTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None

class EventDestinationTypeDef(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationTypeDef] = None
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
    ActiveSubscribedDomains: List[DomainDeliverabilityTrackingOptionTypeDef]
    PendingExpirationSubscribedDomains: List[DomainDeliverabilityTrackingOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliverabilityDashboardOptionRequestRequestTypeDef(BaseValidatorModel):
    DashboardEnabled: bool
    SubscribedDomains: Optional[Sequence[DomainDeliverabilityTrackingOptionTypeDef]] = None

class GetDeliverabilityTestReportResponseTypeDef(BaseValidatorModel):
    DeliverabilityTestReport: DeliverabilityTestReportTypeDef
    OverallPlacement: PlacementStatisticsTypeDef
    IspPlacements: List[IspPlacementTypeDef]
    Message: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: Optional[TrackingOptionsTypeDef] = None
    DeliveryOptions: Optional[DeliveryOptionsTypeDef] = None
    ReputationOptions: Optional[ReputationOptionsTypeDef] = None
    SendingOptions: Optional[SendingOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetConfigurationSetResponseTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsTypeDef
    SendingOptions: SendingOptionsTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmailContentTypeDef(BaseValidatorModel):
    Simple: Optional[MessageTypeDef] = None
    Raw: Optional[RawMessageTypeDef] = None
    Template: Optional[TemplateTypeDef] = None

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class GetConfigurationSetEventDestinationsResponseTypeDef(BaseValidatorModel):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeliverabilityTestReportRequestRequestTypeDef(BaseValidatorModel):
    FromEmailAddress: str
    Content: EmailContentTypeDef
    ReportName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class SendEmailRequestRequestTypeDef(BaseValidatorModel):
    Destination: DestinationTypeDef
    Content: EmailContentTypeDef
    FromEmailAddress: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    EmailTags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None


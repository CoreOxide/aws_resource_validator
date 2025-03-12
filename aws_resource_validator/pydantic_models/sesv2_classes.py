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
from aws_resource_validator.pydantic_models.sesv2_constants import *

class ReviewDetailsTypeDef(BaseValidatorModel):
    Status: Optional[ReviewStatusType] = None
    CaseId: Optional[str] = None


class ArchivingOptionsTypeDef(BaseValidatorModel):
    ArchiveArn: Optional[str] = None


class MetricDataErrorTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Code: Optional[QueryErrorCodeType] = None
    Message: Optional[str] = None


class MetricDataResultTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Timestamps: Optional[List[datetime]] = None
    Values: Optional[List[int]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BlacklistEntryTypeDef(BaseValidatorModel):
    RblName: Optional[str] = None
    ListingTime: Optional[datetime] = None
    Description: Optional[str] = None


class ContentTypeDef(BaseValidatorModel):
    Data: str
    Charset: Optional[str] = None


class BounceTypeDef(BaseValidatorModel):
    BounceType: Optional[BounceTypeType] = None
    BounceSubType: Optional[str] = None
    DiagnosticCode: Optional[str] = None


class BulkEmailEntryResultTypeDef(BaseValidatorModel):
    Status: Optional[BulkEmailStatusType] = None
    Error: Optional[str] = None
    MessageId: Optional[str] = None


class DestinationTypeDef(BaseValidatorModel):
    ToAddresses: Optional[Sequence[str]] = None
    CcAddresses: Optional[Sequence[str]] = None
    BccAddresses: Optional[Sequence[str]] = None


class MessageHeaderTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class MessageTagTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class CancelExportJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class CloudWatchDimensionConfigurationTypeDef(BaseValidatorModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str


class ComplaintTypeDef(BaseValidatorModel):
    ComplaintSubType: Optional[str] = None
    ComplaintFeedbackType: Optional[str] = None


class ContactListDestinationTypeDef(BaseValidatorModel):
    ContactListName: str
    ContactListImportAction: ContactListImportActionType


class ContactListTypeDef(BaseValidatorModel):
    ContactListName: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class TopicPreferenceTypeDef(BaseValidatorModel):
    TopicName: str
    SubscriptionStatus: SubscriptionStatusType


class DeliveryOptionsTypeDef(BaseValidatorModel):
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None
    MaxDeliverySeconds: Optional[int] = None


class SendingOptionsTypeDef(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class TrackingOptionsTypeDef(BaseValidatorModel):
    CustomRedirectDomain: str
    HttpsPolicy: Optional[HttpsPolicyType] = None


class TopicTypeDef(BaseValidatorModel):
    TopicName: str
    DisplayName: str
    DefaultSubscriptionStatus: SubscriptionStatusType
    Description: Optional[str] = None


class CreateCustomVerificationEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class CreateEmailIdentityPolicyRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    PolicyName: str
    Policy: str


class DkimSigningAttributesTypeDef(BaseValidatorModel):
    DomainSigningSelector: Optional[str] = None
    DomainSigningPrivateKey: Optional[str] = None
    NextSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    DomainSigningAttributesOrigin: Optional[DkimSigningAttributesOriginType] = None


class DkimAttributesTypeDef(BaseValidatorModel):
    SigningEnabled: Optional[bool] = None
    Status: Optional[DkimStatusType] = None
    Tokens: Optional[List[str]] = None
    SigningAttributesOrigin: Optional[DkimSigningAttributesOriginType] = None
    NextSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    CurrentSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    LastKeyGenerationTimestamp: Optional[datetime] = None


class ExportDestinationTypeDef(BaseValidatorModel):
    DataFormat: DataFormatType
    S3Url: Optional[str] = None


class ImportDataSourceTypeDef(BaseValidatorModel):
    S3Url: str
    DataFormat: DataFormatType


class CustomVerificationEmailTemplateMetadataTypeDef(BaseValidatorModel):
    TemplateName: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None


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


class DashboardAttributesTypeDef(BaseValidatorModel):
    EngagementMetrics: Optional[FeatureStatusType] = None


class DashboardOptionsTypeDef(BaseValidatorModel):
    EngagementMetrics: Optional[FeatureStatusType] = None


class DedicatedIpPoolTypeDef(BaseValidatorModel):
    PoolName: str
    ScalingMode: ScalingModeType


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


class DeleteContactListRequestTypeDef(BaseValidatorModel):
    ContactListName: str


class DeleteContactRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str


class DeleteCustomVerificationEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str


class DeleteDedicatedIpPoolRequestTypeDef(BaseValidatorModel):
    PoolName: str


class DeleteEmailIdentityPolicyRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    PolicyName: str


class DeleteEmailIdentityRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str


class DeleteEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str


class DeleteMultiRegionEndpointRequestTypeDef(BaseValidatorModel):
    EndpointName: str


class DeleteSuppressedDestinationRequestTypeDef(BaseValidatorModel):
    EmailAddress: str


class DeliverabilityTestReportTypeDef(BaseValidatorModel):
    ReportId: Optional[str] = None
    ReportName: Optional[str] = None
    Subject: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    CreateDate: Optional[datetime] = None
    DeliverabilityTestStatus: Optional[DeliverabilityTestStatusType] = None


class RouteDetailsTypeDef(BaseValidatorModel):
    Region: str


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


class EmailTemplateMetadataTypeDef(BaseValidatorModel):
    TemplateName: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class EventBridgeDestinationTypeDef(BaseValidatorModel):
    EventBusArn: str


class KinesisFirehoseDestinationTypeDef(BaseValidatorModel):
    IamRoleArn: str
    DeliveryStreamArn: str


class PinpointDestinationTypeDef(BaseValidatorModel):
    ApplicationArn: Optional[str] = None


class SnsDestinationTypeDef(BaseValidatorModel):
    TopicArn: str


class ExportJobSummaryTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    ExportSourceType: Optional[ExportSourceTypeType] = None
    JobStatus: Optional[JobStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    CompletedTimestamp: Optional[datetime] = None


class ExportMetricTypeDef(BaseValidatorModel):
    Name: Optional[MetricType] = None
    Aggregation: Optional[MetricAggregationType] = None


class ExportStatisticsTypeDef(BaseValidatorModel):
    ProcessedRecordsCount: Optional[int] = None
    ExportedRecordsCount: Optional[int] = None


class FailureInfoTypeDef(BaseValidatorModel):
    FailedRecordsS3Url: Optional[str] = None
    ErrorMessage: Optional[str] = None


class SendQuotaTypeDef(BaseValidatorModel):
    Max24HourSend: Optional[float] = None
    MaxSendRate: Optional[float] = None
    SentLast24Hours: Optional[float] = None


class SuppressionAttributesTypeDef(BaseValidatorModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None


class GetBlacklistReportsRequestTypeDef(BaseValidatorModel):
    BlacklistItemNames: Sequence[str]


class GetConfigurationSetEventDestinationsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class GetConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class ReputationOptionsOutputTypeDef(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None


class SuppressionOptionsOutputTypeDef(BaseValidatorModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None


class GetContactListRequestTypeDef(BaseValidatorModel):
    ContactListName: str


class GetContactRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str


class GetCustomVerificationEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str


class GetDedicatedIpPoolRequestTypeDef(BaseValidatorModel):
    PoolName: str


class GetDedicatedIpRequestTypeDef(BaseValidatorModel):
    Ip: str


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


class GetEmailIdentityPoliciesRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str


class GetEmailIdentityRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str


class MailFromAttributesTypeDef(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType


class GetEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str


class GetExportJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class GetImportJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class GetMessageInsightsRequestTypeDef(BaseValidatorModel):
    MessageId: str


class GetMultiRegionEndpointRequestTypeDef(BaseValidatorModel):
    EndpointName: str


class RouteTypeDef(BaseValidatorModel):
    Region: str


class GetSuppressedDestinationRequestTypeDef(BaseValidatorModel):
    EmailAddress: str


class GuardianAttributesTypeDef(BaseValidatorModel):
    OptimizedSharedDelivery: Optional[FeatureStatusType] = None


class GuardianOptionsTypeDef(BaseValidatorModel):
    OptimizedSharedDelivery: Optional[FeatureStatusType] = None


class IdentityInfoTypeDef(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    IdentityName: Optional[str] = None
    SendingEnabled: Optional[bool] = None
    VerificationStatus: Optional[VerificationStatusType] = None


class SuppressionListDestinationTypeDef(BaseValidatorModel):
    SuppressionListImportAction: SuppressionListImportActionType


class InboxPlacementTrackingOptionTypeDef(BaseValidatorModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[Sequence[str]] = None


class ListConfigurationSetsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListContactListsRequestTypeDef(BaseValidatorModel):
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None


class TopicFilterTypeDef(BaseValidatorModel):
    TopicName: Optional[str] = None
    UseDefaultIfPreferenceUnavailable: Optional[bool] = None


class ListCustomVerificationEmailTemplatesRequestTypeDef(BaseValidatorModel):
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


class ListEmailTemplatesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListExportJobsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None
    ExportSourceType: Optional[ExportSourceTypeType] = None
    JobStatus: Optional[JobStatusType] = None


class ListImportJobsRequestTypeDef(BaseValidatorModel):
    ImportDestinationType: Optional[ImportDestinationTypeType] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListManagementOptionsTypeDef(BaseValidatorModel):
    ContactListName: str
    TopicName: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListMultiRegionEndpointsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class MultiRegionEndpointTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    Status: Optional[StatusType] = None
    EndpointId: Optional[str] = None
    Regions: Optional[List[str]] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class ListRecommendationsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[Mapping[ListRecommendationsFilterKeyType, str]] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class SuppressedDestinationSummaryTypeDef(BaseValidatorModel):
    EmailAddress: str
    Reason: SuppressionListReasonType
    LastUpdateTime: datetime


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class MessageInsightsFiltersOutputTypeDef(BaseValidatorModel):
    FromEmailAddress: Optional[List[str]] = None
    Destination: Optional[List[str]] = None
    Subject: Optional[List[str]] = None
    Isp: Optional[List[str]] = None
    LastDeliveryEvent: Optional[List[DeliveryEventTypeType]] = None
    LastEngagementEvent: Optional[List[EngagementEventTypeType]] = None


class MessageInsightsFiltersTypeDef(BaseValidatorModel):
    FromEmailAddress: Optional[Sequence[str]] = None
    Destination: Optional[Sequence[str]] = None
    Subject: Optional[Sequence[str]] = None
    Isp: Optional[Sequence[str]] = None
    LastDeliveryEvent: Optional[Sequence[DeliveryEventTypeType]] = None
    LastEngagementEvent: Optional[Sequence[EngagementEventTypeType]] = None


class PutAccountDedicatedIpWarmupAttributesRequestTypeDef(BaseValidatorModel):
    AutoWarmupEnabled: Optional[bool] = None


class PutAccountDetailsRequestTypeDef(BaseValidatorModel):
    MailType: MailTypeType
    WebsiteURL: str
    ContactLanguage: Optional[ContactLanguageType] = None
    UseCaseDescription: Optional[str] = None
    AdditionalContactEmailAddresses: Optional[Sequence[str]] = None
    ProductionAccessEnabled: Optional[bool] = None


class PutAccountSendingAttributesRequestTypeDef(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None


class PutAccountSuppressionAttributesRequestTypeDef(BaseValidatorModel):
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None


class PutConfigurationSetArchivingOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    ArchiveArn: Optional[str] = None


class PutConfigurationSetDeliveryOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None
    MaxDeliverySeconds: Optional[int] = None


class PutConfigurationSetReputationOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    ReputationMetricsEnabled: Optional[bool] = None


class PutConfigurationSetSendingOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    SendingEnabled: Optional[bool] = None


class PutConfigurationSetSuppressionOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None


class PutConfigurationSetTrackingOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    CustomRedirectDomain: Optional[str] = None
    HttpsPolicy: Optional[HttpsPolicyType] = None


class PutDedicatedIpInPoolRequestTypeDef(BaseValidatorModel):
    Ip: str
    DestinationPoolName: str


class PutDedicatedIpPoolScalingAttributesRequestTypeDef(BaseValidatorModel):
    PoolName: str
    ScalingMode: ScalingModeType


class PutDedicatedIpWarmupAttributesRequestTypeDef(BaseValidatorModel):
    Ip: str
    WarmupPercentage: int


class PutEmailIdentityConfigurationSetAttributesRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    ConfigurationSetName: Optional[str] = None


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


class PutSuppressedDestinationRequestTypeDef(BaseValidatorModel):
    EmailAddress: str
    Reason: SuppressionListReasonType


class ReplacementTemplateTypeDef(BaseValidatorModel):
    ReplacementTemplateData: Optional[str] = None


class SOARecordTypeDef(BaseValidatorModel):
    PrimaryNameServer: Optional[str] = None
    AdminEmail: Optional[str] = None
    SerialNumber: Optional[int] = None


class SendCustomVerificationEmailRequestTypeDef(BaseValidatorModel):
    EmailAddress: str
    TemplateName: str
    ConfigurationSetName: Optional[str] = None


class SuppressedDestinationAttributesTypeDef(BaseValidatorModel):
    MessageId: Optional[str] = None
    FeedbackId: Optional[str] = None


class SuppressionOptionsTypeDef(BaseValidatorModel):
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None


class TestRenderEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateData: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateCustomVerificationEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class UpdateEmailIdentityPolicyRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    PolicyName: str
    Policy: str


class AccountDetailsTypeDef(BaseValidatorModel):
    MailType: Optional[MailTypeType] = None
    WebsiteURL: Optional[str] = None
    ContactLanguage: Optional[ContactLanguageType] = None
    UseCaseDescription: Optional[str] = None
    AdditionalContactEmailAddresses: Optional[List[str]] = None
    ReviewDetails: Optional[ReviewDetailsTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class BatchGetMetricDataQueryTypeDef(BaseValidatorModel):
    Id: str
    Namespace: Literal["VDM"]
    Metric: MetricType
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    Dimensions: Optional[Mapping[MetricDimensionNameType, str]] = None


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


class ListSuppressedDestinationsRequestTypeDef(BaseValidatorModel):
    Reasons: Optional[Sequence[SuppressionListReasonType]] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ReputationOptionsTypeDef(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[TimestampTypeDef] = None


class BatchGetMetricDataResponseTypeDef(BaseValidatorModel):
    Results: List[MetricDataResultTypeDef]
    Errors: List[MetricDataErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDeliverabilityTestReportResponseTypeDef(BaseValidatorModel):
    ReportId: str
    DeliverabilityTestStatus: DeliverabilityTestStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateExportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateImportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMultiRegionEndpointResponseTypeDef(BaseValidatorModel):
    Status: StatusType
    EndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMultiRegionEndpointResponseTypeDef(BaseValidatorModel):
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetCustomVerificationEmailTemplateResponseTypeDef(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetEmailIdentityPoliciesResponseTypeDef(BaseValidatorModel):
    Policies: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigurationSetsResponseTypeDef(BaseValidatorModel):
    ConfigurationSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDedicatedIpPoolsResponseTypeDef(BaseValidatorModel):
    DedicatedIpPools: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutEmailIdentityDkimSigningAttributesResponseTypeDef(BaseValidatorModel):
    DkimStatus: DkimStatusType
    DkimTokens: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class SendCustomVerificationEmailResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendEmailResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TestRenderEmailTemplateResponseTypeDef(BaseValidatorModel):
    RenderedTemplate: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBlacklistReportsResponseTypeDef(BaseValidatorModel):
    BlacklistReport: Dict[str, List[BlacklistEntryTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class RawMessageTypeDef(BaseValidatorModel):
    Data: BlobTypeDef


class SendBulkEmailResponseTypeDef(BaseValidatorModel):
    BulkEmailEntryResults: List[BulkEmailEntryResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CloudWatchDestinationOutputTypeDef(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfigurationTypeDef]


class CloudWatchDestinationTypeDef(BaseValidatorModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]


class EventDetailsTypeDef(BaseValidatorModel):
    Bounce: Optional[BounceTypeDef] = None
    Complaint: Optional[ComplaintTypeDef] = None


class ListContactListsResponseTypeDef(BaseValidatorModel):
    ContactLists: List[ContactListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ContactTypeDef(BaseValidatorModel):
    EmailAddress: Optional[str] = None
    TopicPreferences: Optional[List[TopicPreferenceTypeDef]] = None
    TopicDefaultPreferences: Optional[List[TopicPreferenceTypeDef]] = None
    UnsubscribeAll: Optional[bool] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class CreateContactRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: Optional[Sequence[TopicPreferenceTypeDef]] = None
    UnsubscribeAll: Optional[bool] = None
    AttributesData: Optional[str] = None


class GetContactResponseTypeDef(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: List[TopicPreferenceTypeDef]
    TopicDefaultPreferences: List[TopicPreferenceTypeDef]
    UnsubscribeAll: bool
    AttributesData: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContactRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: Optional[Sequence[TopicPreferenceTypeDef]] = None
    UnsubscribeAll: Optional[bool] = None
    AttributesData: Optional[str] = None


class CreateDedicatedIpPoolRequestTypeDef(BaseValidatorModel):
    PoolName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ScalingMode: Optional[ScalingModeType] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateContactListRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    Topics: Optional[Sequence[TopicTypeDef]] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class GetContactListResponseTypeDef(BaseValidatorModel):
    ContactListName: str
    Topics: List[TopicTypeDef]
    Description: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContactListRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    Topics: Optional[Sequence[TopicTypeDef]] = None
    Description: Optional[str] = None


class CreateEmailIdentityRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    DkimSigningAttributes: Optional[DkimSigningAttributesTypeDef] = None
    ConfigurationSetName: Optional[str] = None


class PutEmailIdentityDkimSigningAttributesRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    SigningAttributesOrigin: DkimSigningAttributesOriginType
    SigningAttributes: Optional[DkimSigningAttributesTypeDef] = None


class CreateEmailIdentityResponseTypeDef(BaseValidatorModel):
    IdentityType: IdentityTypeType
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmailTemplateContentTypeDef(BaseValidatorModel):
    pass


class CreateEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateContent: EmailTemplateContentTypeDef


class GetEmailTemplateResponseTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateContent: EmailTemplateContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TemplateTypeDef(BaseValidatorModel):
    TemplateName: Optional[str] = None
    TemplateArn: Optional[str] = None
    TemplateContent: Optional[EmailTemplateContentTypeDef] = None
    TemplateData: Optional[str] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None


class UpdateEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateContent: EmailTemplateContentTypeDef


class ListCustomVerificationEmailTemplatesResponseTypeDef(BaseValidatorModel):
    CustomVerificationEmailTemplates: List[CustomVerificationEmailTemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DailyVolumeTypeDef(BaseValidatorModel):
    StartDate: Optional[datetime] = None
    VolumeStatistics: Optional[VolumeStatisticsTypeDef] = None
    DomainIspPlacements: Optional[List[DomainIspPlacementTypeDef]] = None


class OverallVolumeTypeDef(BaseValidatorModel):
    VolumeStatistics: Optional[VolumeStatisticsTypeDef] = None
    ReadRatePercent: Optional[float] = None
    DomainIspPlacements: Optional[List[DomainIspPlacementTypeDef]] = None


class GetDedicatedIpPoolResponseTypeDef(BaseValidatorModel):
    DedicatedIpPool: DedicatedIpPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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


class DetailsTypeDef(BaseValidatorModel):
    RoutesDetails: Sequence[RouteDetailsTypeDef]


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


class ListEmailTemplatesResponseTypeDef(BaseValidatorModel):
    TemplatesMetadata: List[EmailTemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListExportJobsResponseTypeDef(BaseValidatorModel):
    ExportJobs: List[ExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MetricsDataSourceOutputTypeDef(BaseValidatorModel):
    Dimensions: Dict[MetricDimensionNameType, List[str]]
    Namespace: Literal["VDM"]
    Metrics: List[ExportMetricTypeDef]
    StartDate: datetime
    EndDate: datetime


class MetricsDataSourceTypeDef(BaseValidatorModel):
    Dimensions: Mapping[MetricDimensionNameType, Sequence[str]]
    Namespace: Literal["VDM"]
    Metrics: Sequence[ExportMetricTypeDef]
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef


class IspPlacementTypeDef(BaseValidatorModel):
    IspName: Optional[str] = None
    PlacementStatistics: Optional[PlacementStatisticsTypeDef] = None


class GetMultiRegionEndpointResponseTypeDef(BaseValidatorModel):
    EndpointName: str
    EndpointId: str
    Routes: List[RouteTypeDef]
    Status: StatusType
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class VdmAttributesTypeDef(BaseValidatorModel):
    VdmEnabled: FeatureStatusType
    DashboardAttributes: Optional[DashboardAttributesTypeDef] = None
    GuardianAttributes: Optional[GuardianAttributesTypeDef] = None


class VdmOptionsTypeDef(BaseValidatorModel):
    DashboardOptions: Optional[DashboardOptionsTypeDef] = None
    GuardianOptions: Optional[GuardianOptionsTypeDef] = None


class ListEmailIdentitiesResponseTypeDef(BaseValidatorModel):
    EmailIdentities: List[IdentityInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ImportDestinationTypeDef(BaseValidatorModel):
    SuppressionListDestination: Optional[SuppressionListDestinationTypeDef] = None
    ContactListDestination: Optional[ContactListDestinationTypeDef] = None


class ListContactsFilterTypeDef(BaseValidatorModel):
    FilteredStatus: Optional[SubscriptionStatusType] = None
    TopicFilter: Optional[TopicFilterTypeDef] = None


class ListMultiRegionEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMultiRegionEndpointsResponseTypeDef(BaseValidatorModel):
    MultiRegionEndpoints: List[MultiRegionEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RecommendationTypeDef(BaseValidatorModel):
    pass


class ListRecommendationsResponseTypeDef(BaseValidatorModel):
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSuppressedDestinationsResponseTypeDef(BaseValidatorModel):
    SuppressedDestinationSummaries: List[SuppressedDestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MessageInsightsDataSourceOutputTypeDef(BaseValidatorModel):
    StartDate: datetime
    EndDate: datetime
    Include: Optional[MessageInsightsFiltersOutputTypeDef] = None
    Exclude: Optional[MessageInsightsFiltersOutputTypeDef] = None
    MaxResults: Optional[int] = None


class MessageInsightsDataSourceTypeDef(BaseValidatorModel):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    Include: Optional[MessageInsightsFiltersTypeDef] = None
    Exclude: Optional[MessageInsightsFiltersTypeDef] = None
    MaxResults: Optional[int] = None


class ReplacementEmailContentTypeDef(BaseValidatorModel):
    ReplacementTemplate: Optional[ReplacementTemplateTypeDef] = None


class VerificationInfoTypeDef(BaseValidatorModel):
    LastCheckedTimestamp: Optional[datetime] = None
    LastSuccessTimestamp: Optional[datetime] = None
    ErrorType: Optional[VerificationErrorType] = None
    SOARecord: Optional[SOARecordTypeDef] = None


class SuppressedDestinationTypeDef(BaseValidatorModel):
    EmailAddress: str
    Reason: SuppressionListReasonType
    LastUpdateTime: datetime
    Attributes: Optional[SuppressedDestinationAttributesTypeDef] = None


class BatchGetMetricDataRequestTypeDef(BaseValidatorModel):
    Queries: Sequence[BatchGetMetricDataQueryTypeDef]


class BodyTypeDef(BaseValidatorModel):
    pass


class MessageTypeDef(BaseValidatorModel):
    Subject: ContentTypeDef
    Body: BodyTypeDef
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None


class EventDestinationTypeDef(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutputTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    EventBridgeDestination: Optional[EventBridgeDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None


class ListContactsResponseTypeDef(BaseValidatorModel):
    Contacts: List[ContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BulkEmailContentTypeDef(BaseValidatorModel):
    Template: Optional[TemplateTypeDef] = None


class GetDomainStatisticsReportResponseTypeDef(BaseValidatorModel):
    OverallVolume: OverallVolumeTypeDef
    DailyVolumes: List[DailyVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMultiRegionEndpointRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    Details: DetailsTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


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


class GetAccountResponseTypeDef(BaseValidatorModel):
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    SendQuota: SendQuotaTypeDef
    SendingEnabled: bool
    SuppressionAttributes: SuppressionAttributesTypeDef
    Details: AccountDetailsTypeDef
    VdmAttributes: VdmAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutAccountVdmAttributesRequestTypeDef(BaseValidatorModel):
    VdmAttributes: VdmAttributesTypeDef


class GetConfigurationSetResponseTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsOutputTypeDef
    SendingOptions: SendingOptionsTypeDef
    Tags: List[TagTypeDef]
    SuppressionOptions: SuppressionOptionsOutputTypeDef
    VdmOptions: VdmOptionsTypeDef
    ArchivingOptions: ArchivingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutConfigurationSetVdmOptionsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    VdmOptions: Optional[VdmOptionsTypeDef] = None


class CreateImportJobRequestTypeDef(BaseValidatorModel):
    ImportDestination: ImportDestinationTypeDef
    ImportDataSource: ImportDataSourceTypeDef


class GetImportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ImportDestination: ImportDestinationTypeDef
    ImportDataSource: ImportDataSourceTypeDef
    FailureInfo: FailureInfoTypeDef
    JobStatus: JobStatusType
    CreatedTimestamp: datetime
    CompletedTimestamp: datetime
    ProcessedRecordsCount: int
    FailedRecordsCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class ImportJobSummaryTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    ImportDestination: Optional[ImportDestinationTypeDef] = None
    JobStatus: Optional[JobStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    ProcessedRecordsCount: Optional[int] = None
    FailedRecordsCount: Optional[int] = None


class InboxPlacementTrackingOptionUnionTypeDef(BaseValidatorModel):
    pass


class DomainDeliverabilityTrackingOptionTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[TimestampTypeDef] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionUnionTypeDef] = None


class ListContactsRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    Filter: Optional[ListContactsFilterTypeDef] = None
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None


class ExportDataSourceOutputTypeDef(BaseValidatorModel):
    MetricsDataSource: Optional[MetricsDataSourceOutputTypeDef] = None
    MessageInsightsDataSource: Optional[MessageInsightsDataSourceOutputTypeDef] = None


class ExportDataSourceTypeDef(BaseValidatorModel):
    MetricsDataSource: Optional[MetricsDataSourceTypeDef] = None
    MessageInsightsDataSource: Optional[MessageInsightsDataSourceTypeDef] = None


class BulkEmailEntryTypeDef(BaseValidatorModel):
    Destination: DestinationTypeDef
    ReplacementTags: Optional[Sequence[MessageTagTypeDef]] = None
    ReplacementEmailContent: Optional[ReplacementEmailContentTypeDef] = None
    ReplacementHeaders: Optional[Sequence[MessageHeaderTypeDef]] = None


class GetEmailIdentityResponseTypeDef(BaseValidatorModel):
    IdentityType: IdentityTypeType
    FeedbackForwardingStatus: bool
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    MailFromAttributes: MailFromAttributesTypeDef
    Policies: Dict[str, str]
    Tags: List[TagTypeDef]
    ConfigurationSetName: str
    VerificationStatus: VerificationStatusType
    VerificationInfo: VerificationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSuppressedDestinationResponseTypeDef(BaseValidatorModel):
    SuppressedDestination: SuppressedDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReputationOptionsUnionTypeDef(BaseValidatorModel):
    pass


class SuppressionOptionsUnionTypeDef(BaseValidatorModel):
    pass


class CreateConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: Optional[TrackingOptionsTypeDef] = None
    DeliveryOptions: Optional[DeliveryOptionsTypeDef] = None
    ReputationOptions: Optional[ReputationOptionsUnionTypeDef] = None
    SendingOptions: Optional[SendingOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SuppressionOptions: Optional[SuppressionOptionsUnionTypeDef] = None
    VdmOptions: Optional[VdmOptionsTypeDef] = None
    ArchivingOptions: Optional[ArchivingOptionsTypeDef] = None


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
    EventBridgeDestination: Optional[EventBridgeDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None


class InsightsEventTypeDef(BaseValidatorModel):
    pass


class EmailInsightsTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None
    Isp: Optional[str] = None
    Events: Optional[List[InsightsEventTypeDef]] = None


class ListImportJobsResponseTypeDef(BaseValidatorModel):
    ImportJobs: List[ImportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetExportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ExportSourceType: ExportSourceTypeType
    JobStatus: JobStatusType
    ExportDestination: ExportDestinationTypeDef
    ExportDataSource: ExportDataSourceOutputTypeDef
    CreatedTimestamp: datetime
    CompletedTimestamp: datetime
    FailureInfo: FailureInfoTypeDef
    Statistics: ExportStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SendBulkEmailRequestTypeDef(BaseValidatorModel):
    DefaultContent: BulkEmailContentTypeDef
    BulkEmailEntries: Sequence[BulkEmailEntryTypeDef]
    FromEmailAddress: Optional[str] = None
    FromEmailAddressIdentityArn: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    FeedbackForwardingEmailAddressIdentityArn: Optional[str] = None
    DefaultEmailTags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None
    EndpointId: Optional[str] = None


class CreateDeliverabilityTestReportRequestTypeDef(BaseValidatorModel):
    FromEmailAddress: str
    Content: EmailContentTypeDef
    ReportName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class SendEmailRequestTypeDef(BaseValidatorModel):
    Content: EmailContentTypeDef
    FromEmailAddress: Optional[str] = None
    FromEmailAddressIdentityArn: Optional[str] = None
    Destination: Optional[DestinationTypeDef] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    FeedbackForwardingEmailAddressIdentityArn: Optional[str] = None
    EmailTags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None
    EndpointId: Optional[str] = None
    ListManagementOptions: Optional[ListManagementOptionsTypeDef] = None


class CreateConfigurationSetEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef


class UpdateConfigurationSetEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef


class GetMessageInsightsResponseTypeDef(BaseValidatorModel):
    MessageId: str
    FromEmailAddress: str
    Subject: str
    EmailTags: List[MessageTagTypeDef]
    Insights: List[EmailInsightsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DomainDeliverabilityTrackingOptionUnionTypeDef(BaseValidatorModel):
    pass


class PutDeliverabilityDashboardOptionRequestTypeDef(BaseValidatorModel):
    DashboardEnabled: bool
    SubscribedDomains: Optional[Sequence[DomainDeliverabilityTrackingOptionUnionTypeDef]] = None


class ExportDataSourceUnionTypeDef(BaseValidatorModel):
    pass


class CreateExportJobRequestTypeDef(BaseValidatorModel):
    ExportDataSource: ExportDataSourceUnionTypeDef
    ExportDestination: ExportDestinationTypeDef



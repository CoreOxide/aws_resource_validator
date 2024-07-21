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
from aws_resource_validator.pydantic_models.sesv2_constants import *

class ReviewDetailsTypeDef(BaseModel):
    Status: Optional[ReviewStatusType] = None
    CaseId: Optional[str] = None

class MetricDataErrorTypeDef(BaseModel):
    Id: Optional[str] = None
    Code: Optional[QueryErrorCodeType] = None
    Message: Optional[str] = None

class MetricDataResultTypeDef(BaseModel):
    Id: Optional[str] = None
    Timestamps: Optional[List[datetime]] = None
    Values: Optional[List[int]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BlacklistEntryTypeDef(BaseModel):
    RblName: Optional[str] = None
    ListingTime: Optional[datetime] = None
    Description: Optional[str] = None

class ContentTypeDef(BaseModel):
    Data: str
    Charset: Optional[str] = None

class BounceTypeDef(BaseModel):
    BounceType: Optional[BounceTypeType] = None
    BounceSubType: Optional[str] = None
    DiagnosticCode: Optional[str] = None

class BulkEmailEntryResultTypeDef(BaseModel):
    Status: Optional[BulkEmailStatusType] = None
    Error: Optional[str] = None
    MessageId: Optional[str] = None

class DestinationTypeDef(BaseModel):
    ToAddresses: Optional[Sequence[str]] = None
    CcAddresses: Optional[Sequence[str]] = None
    BccAddresses: Optional[Sequence[str]] = None

class MessageHeaderTypeDef(BaseModel):
    Name: str
    Value: str

class MessageTagTypeDef(BaseModel):
    Name: str
    Value: str

class CancelExportJobRequestRequestTypeDef(BaseModel):
    JobId: str

class CloudWatchDimensionConfigurationTypeDef(BaseModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str

class ComplaintTypeDef(BaseModel):
    ComplaintSubType: Optional[str] = None
    ComplaintFeedbackType: Optional[str] = None

class ContactListDestinationTypeDef(BaseModel):
    ContactListName: str
    ContactListImportAction: ContactListImportActionType

class ContactListTypeDef(BaseModel):
    ContactListName: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class TopicPreferenceTypeDef(BaseModel):
    TopicName: str
    SubscriptionStatus: SubscriptionStatusType

class DeliveryOptionsTypeDef(BaseModel):
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None

class SendingOptionsTypeDef(BaseModel):
    SendingEnabled: Optional[bool] = None

class SuppressionOptionsTypeDef(BaseModel):
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class TrackingOptionsTypeDef(BaseModel):
    CustomRedirectDomain: str

class TopicTypeDef(BaseModel):
    TopicName: str
    DisplayName: str
    DefaultSubscriptionStatus: SubscriptionStatusType
    Description: Optional[str] = None

class CreateCustomVerificationEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str

class CreateEmailIdentityPolicyRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    PolicyName: str
    Policy: str

class DkimSigningAttributesTypeDef(BaseModel):
    DomainSigningSelector: Optional[str] = None
    DomainSigningPrivateKey: Optional[str] = None
    NextSigningKeyLength: Optional[DkimSigningKeyLengthType] = None

class DkimAttributesTypeDef(BaseModel):
    SigningEnabled: Optional[bool] = None
    Status: Optional[DkimStatusType] = None
    Tokens: Optional[List[str]] = None
    SigningAttributesOrigin: Optional[DkimSigningAttributesOriginType] = None
    NextSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    CurrentSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    LastKeyGenerationTimestamp: Optional[datetime] = None

class EmailTemplateContentTypeDef(BaseModel):
    Subject: Optional[str] = None
    Text: Optional[str] = None
    Html: Optional[str] = None

class ExportDestinationTypeDef(BaseModel):
    DataFormat: DataFormatType
    S3Url: Optional[str] = None

class ImportDataSourceTypeDef(BaseModel):
    S3Url: str
    DataFormat: DataFormatType

class CustomVerificationEmailTemplateMetadataTypeDef(BaseModel):
    TemplateName: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None

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

class DashboardAttributesTypeDef(BaseModel):
    EngagementMetrics: Optional[FeatureStatusType] = None

class DashboardOptionsTypeDef(BaseModel):
    EngagementMetrics: Optional[FeatureStatusType] = None

class DedicatedIpPoolTypeDef(BaseModel):
    PoolName: str
    ScalingMode: ScalingModeType

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

class DeleteContactListRequestRequestTypeDef(BaseModel):
    ContactListName: str

class DeleteContactRequestRequestTypeDef(BaseModel):
    ContactListName: str
    EmailAddress: str

class DeleteCustomVerificationEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str

class DeleteDedicatedIpPoolRequestRequestTypeDef(BaseModel):
    PoolName: str

class DeleteEmailIdentityPolicyRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    PolicyName: str

class DeleteEmailIdentityRequestRequestTypeDef(BaseModel):
    EmailIdentity: str

class DeleteEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str

class DeleteSuppressedDestinationRequestRequestTypeDef(BaseModel):
    EmailAddress: str

class DeliverabilityTestReportTypeDef(BaseModel):
    ReportId: Optional[str] = None
    ReportName: Optional[str] = None
    Subject: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    CreateDate: Optional[datetime] = None
    DeliverabilityTestStatus: Optional[DeliverabilityTestStatusType] = None

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

class InboxPlacementTrackingOptionOutputTypeDef(BaseModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[List[str]] = None

class InboxPlacementTrackingOptionTypeDef(BaseModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[Sequence[str]] = None

class EmailTemplateMetadataTypeDef(BaseModel):
    TemplateName: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class EventBridgeDestinationTypeDef(BaseModel):
    EventBusArn: str

class KinesisFirehoseDestinationTypeDef(BaseModel):
    IamRoleArn: str
    DeliveryStreamArn: str

class PinpointDestinationTypeDef(BaseModel):
    ApplicationArn: Optional[str] = None

class SnsDestinationTypeDef(BaseModel):
    TopicArn: str

class ExportJobSummaryTypeDef(BaseModel):
    JobId: Optional[str] = None
    ExportSourceType: Optional[ExportSourceTypeType] = None
    JobStatus: Optional[JobStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    CompletedTimestamp: Optional[datetime] = None

class ExportMetricTypeDef(BaseModel):
    Name: Optional[MetricType] = None
    Aggregation: Optional[MetricAggregationType] = None

class ExportStatisticsTypeDef(BaseModel):
    ProcessedRecordsCount: Optional[int] = None
    ExportedRecordsCount: Optional[int] = None

class FailureInfoTypeDef(BaseModel):
    FailedRecordsS3Url: Optional[str] = None
    ErrorMessage: Optional[str] = None

class SendQuotaTypeDef(BaseModel):
    Max24HourSend: Optional[float] = None
    MaxSendRate: Optional[float] = None
    SentLast24Hours: Optional[float] = None

class SuppressionAttributesTypeDef(BaseModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None

class GetBlacklistReportsRequestRequestTypeDef(BaseModel):
    BlacklistItemNames: Sequence[str]

class GetConfigurationSetEventDestinationsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class GetConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class ReputationOptionsOutputTypeDef(BaseModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None

class SuppressionOptionsOutputTypeDef(BaseModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None

class GetContactListRequestRequestTypeDef(BaseModel):
    ContactListName: str

class GetContactRequestRequestTypeDef(BaseModel):
    ContactListName: str
    EmailAddress: str

class GetCustomVerificationEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str

class GetDedicatedIpPoolRequestRequestTypeDef(BaseModel):
    PoolName: str

class GetDedicatedIpRequestRequestTypeDef(BaseModel):
    Ip: str

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

class GetEmailIdentityPoliciesRequestRequestTypeDef(BaseModel):
    EmailIdentity: str

class GetEmailIdentityRequestRequestTypeDef(BaseModel):
    EmailIdentity: str

class MailFromAttributesTypeDef(BaseModel):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType

class GetEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str

class GetExportJobRequestRequestTypeDef(BaseModel):
    JobId: str

class GetImportJobRequestRequestTypeDef(BaseModel):
    JobId: str

class GetMessageInsightsRequestRequestTypeDef(BaseModel):
    MessageId: str

class GetSuppressedDestinationRequestRequestTypeDef(BaseModel):
    EmailAddress: str

class GuardianAttributesTypeDef(BaseModel):
    OptimizedSharedDelivery: Optional[FeatureStatusType] = None

class GuardianOptionsTypeDef(BaseModel):
    OptimizedSharedDelivery: Optional[FeatureStatusType] = None

class IdentityInfoTypeDef(BaseModel):
    IdentityType: Optional[IdentityTypeType] = None
    IdentityName: Optional[str] = None
    SendingEnabled: Optional[bool] = None
    VerificationStatus: Optional[VerificationStatusType] = None

class SuppressionListDestinationTypeDef(BaseModel):
    SuppressionListImportAction: SuppressionListImportActionType

class ListConfigurationSetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListContactListsRequestRequestTypeDef(BaseModel):
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None

class TopicFilterTypeDef(BaseModel):
    TopicName: Optional[str] = None
    UseDefaultIfPreferenceUnavailable: Optional[bool] = None

class ListCustomVerificationEmailTemplatesRequestRequestTypeDef(BaseModel):
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

class ListEmailTemplatesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListExportJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None
    ExportSourceType: Optional[ExportSourceTypeType] = None
    JobStatus: Optional[JobStatusType] = None

class ListImportJobsRequestRequestTypeDef(BaseModel):
    ImportDestinationType: Optional[ImportDestinationTypeType] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListManagementOptionsTypeDef(BaseModel):
    ContactListName: str
    TopicName: Optional[str] = None

class ListRecommendationsRequestRequestTypeDef(BaseModel):
    Filter: Optional[Mapping[ListRecommendationsFilterKeyType, str]] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class RecommendationTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    Type: Optional[RecommendationTypeType] = None
    Description: Optional[str] = None
    Status: Optional[RecommendationStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Impact: Optional[RecommendationImpactType] = None

class SuppressedDestinationSummaryTypeDef(BaseModel):
    EmailAddress: str
    Reason: SuppressionListReasonType
    LastUpdateTime: datetime

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class MessageInsightsFiltersOutputTypeDef(BaseModel):
    FromEmailAddress: Optional[List[str]] = None
    Destination: Optional[List[str]] = None
    Subject: Optional[List[str]] = None
    Isp: Optional[List[str]] = None
    LastDeliveryEvent: Optional[List[DeliveryEventTypeType]] = None
    LastEngagementEvent: Optional[List[EngagementEventTypeType]] = None

class MessageInsightsFiltersTypeDef(BaseModel):
    FromEmailAddress: Optional[Sequence[str]] = None
    Destination: Optional[Sequence[str]] = None
    Subject: Optional[Sequence[str]] = None
    Isp: Optional[Sequence[str]] = None
    LastDeliveryEvent: Optional[Sequence[DeliveryEventTypeType]] = None
    LastEngagementEvent: Optional[Sequence[EngagementEventTypeType]] = None

class PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef(BaseModel):
    AutoWarmupEnabled: Optional[bool] = None

class PutAccountDetailsRequestRequestTypeDef(BaseModel):
    MailType: MailTypeType
    WebsiteURL: str
    UseCaseDescription: str
    ContactLanguage: Optional[ContactLanguageType] = None
    AdditionalContactEmailAddresses: Optional[Sequence[str]] = None
    ProductionAccessEnabled: Optional[bool] = None

class PutAccountSendingAttributesRequestRequestTypeDef(BaseModel):
    SendingEnabled: Optional[bool] = None

class PutAccountSuppressionAttributesRequestRequestTypeDef(BaseModel):
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None

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

class PutConfigurationSetSuppressionOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None

class PutConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    CustomRedirectDomain: Optional[str] = None

class PutDedicatedIpInPoolRequestRequestTypeDef(BaseModel):
    Ip: str
    DestinationPoolName: str

class PutDedicatedIpPoolScalingAttributesRequestRequestTypeDef(BaseModel):
    PoolName: str
    ScalingMode: ScalingModeType

class PutDedicatedIpWarmupAttributesRequestRequestTypeDef(BaseModel):
    Ip: str
    WarmupPercentage: int

class PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    ConfigurationSetName: Optional[str] = None

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

class PutSuppressedDestinationRequestRequestTypeDef(BaseModel):
    EmailAddress: str
    Reason: SuppressionListReasonType

class ReplacementTemplateTypeDef(BaseModel):
    ReplacementTemplateData: Optional[str] = None

class SOARecordTypeDef(BaseModel):
    PrimaryNameServer: Optional[str] = None
    AdminEmail: Optional[str] = None
    SerialNumber: Optional[int] = None

class SendCustomVerificationEmailRequestRequestTypeDef(BaseModel):
    EmailAddress: str
    TemplateName: str
    ConfigurationSetName: Optional[str] = None

class SuppressedDestinationAttributesTypeDef(BaseModel):
    MessageId: Optional[str] = None
    FeedbackId: Optional[str] = None

class TestRenderEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    TemplateData: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateCustomVerificationEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str

class UpdateEmailIdentityPolicyRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    PolicyName: str
    Policy: str

class AccountDetailsTypeDef(BaseModel):
    MailType: Optional[MailTypeType] = None
    WebsiteURL: Optional[str] = None
    ContactLanguage: Optional[ContactLanguageType] = None
    UseCaseDescription: Optional[str] = None
    AdditionalContactEmailAddresses: Optional[List[str]] = None
    ReviewDetails: Optional[ReviewDetailsTypeDef] = None

class BatchGetMetricDataQueryTypeDef(BaseModel):
    Id: str
    Namespace: Literal["VDM"]
    Metric: MetricType
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    Dimensions: Optional[Mapping[MetricDimensionNameType, str]] = None

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

class ListSuppressedDestinationsRequestRequestTypeDef(BaseModel):
    Reasons: Optional[Sequence[SuppressionListReasonType]] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ReputationOptionsTypeDef(BaseModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[TimestampTypeDef] = None

class BatchGetMetricDataResponseTypeDef(BaseModel):
    Results: List[MetricDataResultTypeDef]
    Errors: List[MetricDataErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeliverabilityTestReportResponseTypeDef(BaseModel):
    ReportId: str
    DeliverabilityTestStatus: DeliverabilityTestStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExportJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImportJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomVerificationEmailTemplateResponseTypeDef(BaseModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEmailIdentityPoliciesResponseTypeDef(BaseModel):
    Policies: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsResponseTypeDef(BaseModel):
    ConfigurationSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDedicatedIpPoolsResponseTypeDef(BaseModel):
    DedicatedIpPools: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutEmailIdentityDkimSigningAttributesResponseTypeDef(BaseModel):
    DkimStatus: DkimStatusType
    DkimTokens: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SendCustomVerificationEmailResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestRenderEmailTemplateResponseTypeDef(BaseModel):
    RenderedTemplate: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlacklistReportsResponseTypeDef(BaseModel):
    BlacklistReport: Dict[str, List[BlacklistEntryTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class RawMessageTypeDef(BaseModel):
    Data: BlobTypeDef

class BodyTypeDef(BaseModel):
    Text: Optional[ContentTypeDef] = None
    Html: Optional[ContentTypeDef] = None

class SendBulkEmailResponseTypeDef(BaseModel):
    BulkEmailEntryResults: List[BulkEmailEntryResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TemplateTypeDef(BaseModel):
    TemplateName: Optional[str] = None
    TemplateArn: Optional[str] = None
    TemplateData: Optional[str] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None

class CloudWatchDestinationOutputTypeDef(BaseModel):
    DimensionConfigurations: List[CloudWatchDimensionConfigurationTypeDef]

class CloudWatchDestinationTypeDef(BaseModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]

class EventDetailsTypeDef(BaseModel):
    Bounce: Optional[BounceTypeDef] = None
    Complaint: Optional[ComplaintTypeDef] = None

class ListContactListsResponseTypeDef(BaseModel):
    ContactLists: List[ContactListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContactTypeDef(BaseModel):
    EmailAddress: Optional[str] = None
    TopicPreferences: Optional[List[TopicPreferenceTypeDef]] = None
    TopicDefaultPreferences: Optional[List[TopicPreferenceTypeDef]] = None
    UnsubscribeAll: Optional[bool] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class CreateContactRequestRequestTypeDef(BaseModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: Optional[Sequence[TopicPreferenceTypeDef]] = None
    UnsubscribeAll: Optional[bool] = None
    AttributesData: Optional[str] = None

class GetContactResponseTypeDef(BaseModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: List[TopicPreferenceTypeDef]
    TopicDefaultPreferences: List[TopicPreferenceTypeDef]
    UnsubscribeAll: bool
    AttributesData: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContactRequestRequestTypeDef(BaseModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: Optional[Sequence[TopicPreferenceTypeDef]] = None
    UnsubscribeAll: Optional[bool] = None
    AttributesData: Optional[str] = None

class CreateDedicatedIpPoolRequestRequestTypeDef(BaseModel):
    PoolName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ScalingMode: Optional[ScalingModeType] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateContactListRequestRequestTypeDef(BaseModel):
    ContactListName: str
    Topics: Optional[Sequence[TopicTypeDef]] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetContactListResponseTypeDef(BaseModel):
    ContactListName: str
    Topics: List[TopicTypeDef]
    Description: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContactListRequestRequestTypeDef(BaseModel):
    ContactListName: str
    Topics: Optional[Sequence[TopicTypeDef]] = None
    Description: Optional[str] = None

class CreateEmailIdentityRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    DkimSigningAttributes: Optional[DkimSigningAttributesTypeDef] = None
    ConfigurationSetName: Optional[str] = None

class PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef(BaseModel):
    EmailIdentity: str
    SigningAttributesOrigin: DkimSigningAttributesOriginType
    SigningAttributes: Optional[DkimSigningAttributesTypeDef] = None

class CreateEmailIdentityResponseTypeDef(BaseModel):
    IdentityType: IdentityTypeType
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    TemplateContent: EmailTemplateContentTypeDef

class GetEmailTemplateResponseTypeDef(BaseModel):
    TemplateName: str
    TemplateContent: EmailTemplateContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    TemplateContent: EmailTemplateContentTypeDef

class ListCustomVerificationEmailTemplatesResponseTypeDef(BaseModel):
    CustomVerificationEmailTemplates: List[CustomVerificationEmailTemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DailyVolumeTypeDef(BaseModel):
    StartDate: Optional[datetime] = None
    VolumeStatistics: Optional[VolumeStatisticsTypeDef] = None
    DomainIspPlacements: Optional[List[DomainIspPlacementTypeDef]] = None

class OverallVolumeTypeDef(BaseModel):
    VolumeStatistics: Optional[VolumeStatisticsTypeDef] = None
    ReadRatePercent: Optional[float] = None
    DomainIspPlacements: Optional[List[DomainIspPlacementTypeDef]] = None

class GetDedicatedIpPoolResponseTypeDef(BaseModel):
    DedicatedIpPool: DedicatedIpPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDedicatedIpResponseTypeDef(BaseModel):
    DedicatedIp: DedicatedIpTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDedicatedIpsResponseTypeDef(BaseModel):
    DedicatedIps: List[DedicatedIpTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDeliverabilityTestReportsResponseTypeDef(BaseModel):
    DeliverabilityTestReports: List[DeliverabilityTestReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDomainDeliverabilityCampaignResponseTypeDef(BaseModel):
    DomainDeliverabilityCampaign: DomainDeliverabilityCampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainDeliverabilityCampaignsResponseTypeDef(BaseModel):
    DomainDeliverabilityCampaigns: List[DomainDeliverabilityCampaignTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DomainDeliverabilityTrackingOptionOutputTypeDef(BaseModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[datetime] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionOutputTypeDef] = None

class DomainDeliverabilityTrackingOptionTypeDef(BaseModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[TimestampTypeDef] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionTypeDef] = None

class ListEmailTemplatesResponseTypeDef(BaseModel):
    TemplatesMetadata: List[EmailTemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListExportJobsResponseTypeDef(BaseModel):
    ExportJobs: List[ExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MetricsDataSourceOutputTypeDef(BaseModel):
    Dimensions: Dict[MetricDimensionNameType, List[str]]
    Namespace: Literal["VDM"]
    Metrics: List[ExportMetricTypeDef]
    StartDate: datetime
    EndDate: datetime

class MetricsDataSourceTypeDef(BaseModel):
    Dimensions: Mapping[MetricDimensionNameType, Sequence[str]]
    Namespace: Literal["VDM"]
    Metrics: Sequence[ExportMetricTypeDef]
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef

class IspPlacementTypeDef(BaseModel):
    IspName: Optional[str] = None
    PlacementStatistics: Optional[PlacementStatisticsTypeDef] = None

class VdmAttributesTypeDef(BaseModel):
    VdmEnabled: FeatureStatusType
    DashboardAttributes: Optional[DashboardAttributesTypeDef] = None
    GuardianAttributes: Optional[GuardianAttributesTypeDef] = None

class VdmOptionsTypeDef(BaseModel):
    DashboardOptions: Optional[DashboardOptionsTypeDef] = None
    GuardianOptions: Optional[GuardianOptionsTypeDef] = None

class ListEmailIdentitiesResponseTypeDef(BaseModel):
    EmailIdentities: List[IdentityInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ImportDestinationTypeDef(BaseModel):
    SuppressionListDestination: Optional[SuppressionListDestinationTypeDef] = None
    ContactListDestination: Optional[ContactListDestinationTypeDef] = None

class ListContactsFilterTypeDef(BaseModel):
    FilteredStatus: Optional[SubscriptionStatusType] = None
    TopicFilter: Optional[TopicFilterTypeDef] = None

class ListRecommendationsResponseTypeDef(BaseModel):
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSuppressedDestinationsResponseTypeDef(BaseModel):
    SuppressedDestinationSummaries: List[SuppressedDestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MessageInsightsDataSourceOutputTypeDef(BaseModel):
    StartDate: datetime
    EndDate: datetime
    Include: Optional[MessageInsightsFiltersOutputTypeDef] = None
    Exclude: Optional[MessageInsightsFiltersOutputTypeDef] = None
    MaxResults: Optional[int] = None

class MessageInsightsDataSourceTypeDef(BaseModel):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    Include: Optional[MessageInsightsFiltersTypeDef] = None
    Exclude: Optional[MessageInsightsFiltersTypeDef] = None
    MaxResults: Optional[int] = None

class ReplacementEmailContentTypeDef(BaseModel):
    ReplacementTemplate: Optional[ReplacementTemplateTypeDef] = None

class VerificationInfoTypeDef(BaseModel):
    LastCheckedTimestamp: Optional[datetime] = None
    LastSuccessTimestamp: Optional[datetime] = None
    ErrorType: Optional[VerificationErrorType] = None
    SOARecord: Optional[SOARecordTypeDef] = None

class SuppressedDestinationTypeDef(BaseModel):
    EmailAddress: str
    Reason: SuppressionListReasonType
    LastUpdateTime: datetime
    Attributes: Optional[SuppressedDestinationAttributesTypeDef] = None

class BatchGetMetricDataRequestRequestTypeDef(BaseModel):
    Queries: Sequence[BatchGetMetricDataQueryTypeDef]

class MessageTypeDef(BaseModel):
    Subject: ContentTypeDef
    Body: BodyTypeDef
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None

class BulkEmailContentTypeDef(BaseModel):
    Template: Optional[TemplateTypeDef] = None

class EventDestinationTypeDef(BaseModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutputTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    EventBridgeDestination: Optional[EventBridgeDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None

class EventDestinationDefinitionTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    EventBridgeDestination: Optional[EventBridgeDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None

class InsightsEventTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    Type: Optional[EventTypeType] = None
    Details: Optional[EventDetailsTypeDef] = None

class ListContactsResponseTypeDef(BaseModel):
    Contacts: List[ContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDomainStatisticsReportResponseTypeDef(BaseModel):
    OverallVolume: OverallVolumeTypeDef
    DailyVolumes: List[DailyVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliverabilityDashboardOptionsResponseTypeDef(BaseModel):
    DashboardEnabled: bool
    SubscriptionExpiryDate: datetime
    AccountStatus: DeliverabilityDashboardAccountStatusType
    ActiveSubscribedDomains: List[DomainDeliverabilityTrackingOptionOutputTypeDef]
    PendingExpirationSubscribedDomains: List[DomainDeliverabilityTrackingOptionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliverabilityTestReportResponseTypeDef(BaseModel):
    DeliverabilityTestReport: DeliverabilityTestReportTypeDef
    OverallPlacement: PlacementStatisticsTypeDef
    IspPlacements: List[IspPlacementTypeDef]
    Message: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountResponseTypeDef(BaseModel):
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    SendQuota: SendQuotaTypeDef
    SendingEnabled: bool
    SuppressionAttributes: SuppressionAttributesTypeDef
    Details: AccountDetailsTypeDef
    VdmAttributes: VdmAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountVdmAttributesRequestRequestTypeDef(BaseModel):
    VdmAttributes: VdmAttributesTypeDef

class CreateConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    TrackingOptions: Optional[TrackingOptionsTypeDef] = None
    DeliveryOptions: Optional[DeliveryOptionsTypeDef] = None
    ReputationOptions: Optional[ReputationOptionsTypeDef] = None
    SendingOptions: Optional[SendingOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SuppressionOptions: Optional[SuppressionOptionsTypeDef] = None
    VdmOptions: Optional[VdmOptionsTypeDef] = None

class GetConfigurationSetResponseTypeDef(BaseModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsOutputTypeDef
    SendingOptions: SendingOptionsTypeDef
    Tags: List[TagTypeDef]
    SuppressionOptions: SuppressionOptionsOutputTypeDef
    VdmOptions: VdmOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfigurationSetVdmOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    VdmOptions: Optional[VdmOptionsTypeDef] = None

class CreateImportJobRequestRequestTypeDef(BaseModel):
    ImportDestination: ImportDestinationTypeDef
    ImportDataSource: ImportDataSourceTypeDef

class GetImportJobResponseTypeDef(BaseModel):
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

class ImportJobSummaryTypeDef(BaseModel):
    JobId: Optional[str] = None
    ImportDestination: Optional[ImportDestinationTypeDef] = None
    JobStatus: Optional[JobStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    ProcessedRecordsCount: Optional[int] = None
    FailedRecordsCount: Optional[int] = None

class ListContactsRequestRequestTypeDef(BaseModel):
    ContactListName: str
    Filter: Optional[ListContactsFilterTypeDef] = None
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None

class ExportDataSourceOutputTypeDef(BaseModel):
    MetricsDataSource: Optional[MetricsDataSourceOutputTypeDef] = None
    MessageInsightsDataSource: Optional[MessageInsightsDataSourceOutputTypeDef] = None

class ExportDataSourceTypeDef(BaseModel):
    MetricsDataSource: Optional[MetricsDataSourceTypeDef] = None
    MessageInsightsDataSource: Optional[MessageInsightsDataSourceTypeDef] = None

class BulkEmailEntryTypeDef(BaseModel):
    Destination: DestinationTypeDef
    ReplacementTags: Optional[Sequence[MessageTagTypeDef]] = None
    ReplacementEmailContent: Optional[ReplacementEmailContentTypeDef] = None
    ReplacementHeaders: Optional[Sequence[MessageHeaderTypeDef]] = None

class GetEmailIdentityResponseTypeDef(BaseModel):
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

class GetSuppressedDestinationResponseTypeDef(BaseModel):
    SuppressedDestination: SuppressedDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmailContentTypeDef(BaseModel):
    Simple: Optional[MessageTypeDef] = None
    Raw: Optional[RawMessageTypeDef] = None
    Template: Optional[TemplateTypeDef] = None

class GetConfigurationSetEventDestinationsResponseTypeDef(BaseModel):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class EmailInsightsTypeDef(BaseModel):
    Destination: Optional[str] = None
    Isp: Optional[str] = None
    Events: Optional[List[InsightsEventTypeDef]] = None

class PutDeliverabilityDashboardOptionRequestRequestTypeDef(BaseModel):
    DashboardEnabled: bool
    SubscribedDomains: Optional[Sequence[DomainDeliverabilityTrackingOptionUnionTypeDef]] = None

class ListImportJobsResponseTypeDef(BaseModel):
    ImportJobs: List[ImportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetExportJobResponseTypeDef(BaseModel):
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

class CreateExportJobRequestRequestTypeDef(BaseModel):
    ExportDataSource: ExportDataSourceTypeDef
    ExportDestination: ExportDestinationTypeDef

class SendBulkEmailRequestRequestTypeDef(BaseModel):
    DefaultContent: BulkEmailContentTypeDef
    BulkEmailEntries: Sequence[BulkEmailEntryTypeDef]
    FromEmailAddress: Optional[str] = None
    FromEmailAddressIdentityArn: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    FeedbackForwardingEmailAddressIdentityArn: Optional[str] = None
    DefaultEmailTags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None

class CreateDeliverabilityTestReportRequestRequestTypeDef(BaseModel):
    FromEmailAddress: str
    Content: EmailContentTypeDef
    ReportName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class SendEmailRequestRequestTypeDef(BaseModel):
    Content: EmailContentTypeDef
    FromEmailAddress: Optional[str] = None
    FromEmailAddressIdentityArn: Optional[str] = None
    Destination: Optional[DestinationTypeDef] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    FeedbackForwardingEmailAddressIdentityArn: Optional[str] = None
    EmailTags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None
    ListManagementOptions: Optional[ListManagementOptionsTypeDef] = None

class GetMessageInsightsResponseTypeDef(BaseModel):
    MessageId: str
    FromEmailAddress: str
    Subject: str
    EmailTags: List[MessageTagTypeDef]
    Insights: List[EmailInsightsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


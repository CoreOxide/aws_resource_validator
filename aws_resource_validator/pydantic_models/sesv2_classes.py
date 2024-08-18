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
from aws_resource_validator.pydantic_models.sesv2_constants import *

class ReviewDetailsTypeDef(BaseValidatorModel):
    Status: Optional[ReviewStatusType] = None
    CaseId: Optional[str] = None

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

class CancelExportJobRequestRequestTypeDef(BaseValidatorModel):
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

class SendingOptionsTypeDef(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None

class SuppressionOptionsTypeDef(BaseValidatorModel):
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class TrackingOptionsTypeDef(BaseValidatorModel):
    CustomRedirectDomain: str

class TopicTypeDef(BaseValidatorModel):
    TopicName: str
    DisplayName: str
    DefaultSubscriptionStatus: SubscriptionStatusType
    Description: Optional[str] = None

class CreateCustomVerificationEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str

class CreateEmailIdentityPolicyRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    PolicyName: str
    Policy: str

class DkimSigningAttributesTypeDef(BaseValidatorModel):
    DomainSigningSelector: Optional[str] = None
    DomainSigningPrivateKey: Optional[str] = None
    NextSigningKeyLength: Optional[DkimSigningKeyLengthType] = None

class DkimAttributesTypeDef(BaseValidatorModel):
    SigningEnabled: Optional[bool] = None
    Status: Optional[DkimStatusType] = None
    Tokens: Optional[List[str]] = None
    SigningAttributesOrigin: Optional[DkimSigningAttributesOriginType] = None
    NextSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    CurrentSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    LastKeyGenerationTimestamp: Optional[datetime] = None

class EmailTemplateContentTypeDef(BaseValidatorModel):
    Subject: Optional[str] = None
    Text: Optional[str] = None
    Html: Optional[str] = None

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

class DeleteConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class DeleteContactListRequestRequestTypeDef(BaseValidatorModel):
    ContactListName: str

class DeleteContactRequestRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str

class DeleteCustomVerificationEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str

class DeleteDedicatedIpPoolRequestRequestTypeDef(BaseValidatorModel):
    PoolName: str

class DeleteEmailIdentityPolicyRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    PolicyName: str

class DeleteEmailIdentityRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str

class DeleteEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str

class DeleteSuppressedDestinationRequestRequestTypeDef(BaseValidatorModel):
    EmailAddress: str

class DeliverabilityTestReportTypeDef(BaseValidatorModel):
    ReportId: Optional[str] = None
    ReportName: Optional[str] = None
    Subject: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    CreateDate: Optional[datetime] = None
    DeliverabilityTestStatus: Optional[DeliverabilityTestStatusType] = None

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

class InboxPlacementTrackingOptionTypeDef(BaseValidatorModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[Sequence[str]] = None

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

class GetBlacklistReportsRequestRequestTypeDef(BaseValidatorModel):
    BlacklistItemNames: Sequence[str]

class GetConfigurationSetEventDestinationsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class GetConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class ReputationOptionsOutputTypeDef(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None

class SuppressionOptionsOutputTypeDef(BaseValidatorModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None

class GetContactListRequestRequestTypeDef(BaseValidatorModel):
    ContactListName: str

class GetContactRequestRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str

class GetCustomVerificationEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str

class GetDedicatedIpPoolRequestRequestTypeDef(BaseValidatorModel):
    PoolName: str

class GetDedicatedIpRequestRequestTypeDef(BaseValidatorModel):
    Ip: str

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

class GetEmailIdentityPoliciesRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str

class GetEmailIdentityRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str

class MailFromAttributesTypeDef(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType

class GetEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str

class GetExportJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class GetImportJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class GetMessageInsightsRequestRequestTypeDef(BaseValidatorModel):
    MessageId: str

class GetSuppressedDestinationRequestRequestTypeDef(BaseValidatorModel):
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

class ListConfigurationSetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListContactListsRequestRequestTypeDef(BaseValidatorModel):
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None

class TopicFilterTypeDef(BaseValidatorModel):
    TopicName: Optional[str] = None
    UseDefaultIfPreferenceUnavailable: Optional[bool] = None

class ListCustomVerificationEmailTemplatesRequestRequestTypeDef(BaseValidatorModel):
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

class ListEmailTemplatesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListExportJobsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None
    ExportSourceType: Optional[ExportSourceTypeType] = None
    JobStatus: Optional[JobStatusType] = None

class ListImportJobsRequestRequestTypeDef(BaseValidatorModel):
    ImportDestinationType: Optional[ImportDestinationTypeType] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListManagementOptionsTypeDef(BaseValidatorModel):
    ContactListName: str
    TopicName: Optional[str] = None

class ListRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[Mapping[ListRecommendationsFilterKeyType, str]] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class RecommendationTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Type: Optional[RecommendationTypeType] = None
    Description: Optional[str] = None
    Status: Optional[RecommendationStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Impact: Optional[RecommendationImpactType] = None

class SuppressedDestinationSummaryTypeDef(BaseValidatorModel):
    EmailAddress: str
    Reason: SuppressionListReasonType
    LastUpdateTime: datetime

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef(BaseValidatorModel):
    AutoWarmupEnabled: Optional[bool] = None

class PutAccountDetailsRequestRequestTypeDef(BaseValidatorModel):
    MailType: MailTypeType
    WebsiteURL: str
    UseCaseDescription: str
    ContactLanguage: Optional[ContactLanguageType] = None
    AdditionalContactEmailAddresses: Optional[Sequence[str]] = None
    ProductionAccessEnabled: Optional[bool] = None

class PutAccountSendingAttributesRequestRequestTypeDef(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None

class PutAccountSuppressionAttributesRequestRequestTypeDef(BaseValidatorModel):
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None

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

class PutConfigurationSetSuppressionOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    SuppressedReasons: Optional[Sequence[SuppressionListReasonType]] = None

class PutConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    CustomRedirectDomain: Optional[str] = None

class PutDedicatedIpInPoolRequestRequestTypeDef(BaseValidatorModel):
    Ip: str
    DestinationPoolName: str

class PutDedicatedIpPoolScalingAttributesRequestRequestTypeDef(BaseValidatorModel):
    PoolName: str
    ScalingMode: ScalingModeType

class PutDedicatedIpWarmupAttributesRequestRequestTypeDef(BaseValidatorModel):
    Ip: str
    WarmupPercentage: int

class PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    ConfigurationSetName: Optional[str] = None

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

class PutSuppressedDestinationRequestRequestTypeDef(BaseValidatorModel):
    EmailAddress: str
    Reason: SuppressionListReasonType

class ReplacementTemplateTypeDef(BaseValidatorModel):
    ReplacementTemplateData: Optional[str] = None

class SOARecordTypeDef(BaseValidatorModel):
    PrimaryNameServer: Optional[str] = None
    AdminEmail: Optional[str] = None
    SerialNumber: Optional[int] = None

class SendCustomVerificationEmailRequestRequestTypeDef(BaseValidatorModel):
    EmailAddress: str
    TemplateName: str
    ConfigurationSetName: Optional[str] = None

class SuppressedDestinationAttributesTypeDef(BaseValidatorModel):
    MessageId: Optional[str] = None
    FeedbackId: Optional[str] = None

class TestRenderEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateData: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateCustomVerificationEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str

class UpdateEmailIdentityPolicyRequestRequestTypeDef(BaseValidatorModel):
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

class BatchGetMetricDataQueryTypeDef(BaseValidatorModel):
    Id: str
    Namespace: Literal["VDM"]
    Metric: MetricType
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    Dimensions: Optional[Mapping[MetricDimensionNameType, str]] = None

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

class ListSuppressedDestinationsRequestRequestTypeDef(BaseValidatorModel):
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

class RawMessageTypeDef(BaseValidatorModel):
    Data: BlobTypeDef

class BodyTypeDef(BaseValidatorModel):
    Text: Optional[ContentTypeDef] = None
    Html: Optional[ContentTypeDef] = None

class SendBulkEmailResponseTypeDef(BaseValidatorModel):
    BulkEmailEntryResults: List[BulkEmailEntryResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TemplateTypeDef(BaseValidatorModel):
    TemplateName: Optional[str] = None
    TemplateArn: Optional[str] = None
    TemplateData: Optional[str] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None

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

class CreateContactRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateContactRequestRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: Optional[Sequence[TopicPreferenceTypeDef]] = None
    UnsubscribeAll: Optional[bool] = None
    AttributesData: Optional[str] = None

class CreateDedicatedIpPoolRequestRequestTypeDef(BaseValidatorModel):
    PoolName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ScalingMode: Optional[ScalingModeType] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateContactListRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateContactListRequestRequestTypeDef(BaseValidatorModel):
    ContactListName: str
    Topics: Optional[Sequence[TopicTypeDef]] = None
    Description: Optional[str] = None

class CreateEmailIdentityRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    DkimSigningAttributes: Optional[DkimSigningAttributesTypeDef] = None
    ConfigurationSetName: Optional[str] = None

class PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef(BaseValidatorModel):
    EmailIdentity: str
    SigningAttributesOrigin: DkimSigningAttributesOriginType
    SigningAttributes: Optional[DkimSigningAttributesTypeDef] = None

class CreateEmailIdentityResponseTypeDef(BaseValidatorModel):
    IdentityType: IdentityTypeType
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateContent: EmailTemplateContentTypeDef

class GetEmailTemplateResponseTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateContent: EmailTemplateContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class DomainDeliverabilityTrackingOptionTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[TimestampTypeDef] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionTypeDef] = None

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

class BatchGetMetricDataRequestRequestTypeDef(BaseValidatorModel):
    Queries: Sequence[BatchGetMetricDataQueryTypeDef]

class MessageTypeDef(BaseValidatorModel):
    Subject: ContentTypeDef
    Body: BodyTypeDef
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None

class BulkEmailContentTypeDef(BaseValidatorModel):
    Template: Optional[TemplateTypeDef] = None

class EventDestinationTypeDef(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutputTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    EventBridgeDestination: Optional[EventBridgeDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None

class EventDestinationDefinitionTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    EventBridgeDestination: Optional[EventBridgeDestinationTypeDef] = None
    PinpointDestination: Optional[PinpointDestinationTypeDef] = None

class InsightsEventTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Type: Optional[EventTypeType] = None
    Details: Optional[EventDetailsTypeDef] = None

class ListContactsResponseTypeDef(BaseValidatorModel):
    Contacts: List[ContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

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

class PutAccountVdmAttributesRequestRequestTypeDef(BaseValidatorModel):
    VdmAttributes: VdmAttributesTypeDef

class CreateConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: Optional[TrackingOptionsTypeDef] = None
    DeliveryOptions: Optional[DeliveryOptionsTypeDef] = None
    ReputationOptions: Optional[ReputationOptionsTypeDef] = None
    SendingOptions: Optional[SendingOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SuppressionOptions: Optional[SuppressionOptionsTypeDef] = None
    VdmOptions: Optional[VdmOptionsTypeDef] = None

class GetConfigurationSetResponseTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsOutputTypeDef
    SendingOptions: SendingOptionsTypeDef
    Tags: List[TagTypeDef]
    SuppressionOptions: SuppressionOptionsOutputTypeDef
    VdmOptions: VdmOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfigurationSetVdmOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    VdmOptions: Optional[VdmOptionsTypeDef] = None

class CreateImportJobRequestRequestTypeDef(BaseValidatorModel):
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

class ListContactsRequestRequestTypeDef(BaseValidatorModel):
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

class EmailContentTypeDef(BaseValidatorModel):
    Simple: Optional[MessageTypeDef] = None
    Raw: Optional[RawMessageTypeDef] = None
    Template: Optional[TemplateTypeDef] = None

class GetConfigurationSetEventDestinationsResponseTypeDef(BaseValidatorModel):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class EmailInsightsTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None
    Isp: Optional[str] = None
    Events: Optional[List[InsightsEventTypeDef]] = None

class PutDeliverabilityDashboardOptionRequestRequestTypeDef(BaseValidatorModel):
    DashboardEnabled: bool
    SubscribedDomains: Optional[Sequence[DomainDeliverabilityTrackingOptionUnionTypeDef]] = None

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

class CreateExportJobRequestRequestTypeDef(BaseValidatorModel):
    ExportDataSource: ExportDataSourceTypeDef
    ExportDestination: ExportDestinationTypeDef

class SendBulkEmailRequestRequestTypeDef(BaseValidatorModel):
    DefaultContent: BulkEmailContentTypeDef
    BulkEmailEntries: Sequence[BulkEmailEntryTypeDef]
    FromEmailAddress: Optional[str] = None
    FromEmailAddressIdentityArn: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    FeedbackForwardingEmailAddressIdentityArn: Optional[str] = None
    DefaultEmailTags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None

class CreateDeliverabilityTestReportRequestRequestTypeDef(BaseValidatorModel):
    FromEmailAddress: str
    Content: EmailContentTypeDef
    ReportName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class SendEmailRequestRequestTypeDef(BaseValidatorModel):
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

class GetMessageInsightsResponseTypeDef(BaseValidatorModel):
    MessageId: str
    FromEmailAddress: str
    Subject: str
    EmailTags: List[MessageTagTypeDef]
    Insights: List[EmailInsightsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


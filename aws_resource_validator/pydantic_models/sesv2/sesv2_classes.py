from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sesv2.sesv2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ReviewDetails(BaseValidatorModel):
    Status: Optional[ReviewStatusType] = None
    CaseId: Optional[str] = None


class ArchivingOptions(BaseValidatorModel):
    ArchiveArn: Optional[str] = None

Timestamp = Union[datetime, str]


class MetricDataError(BaseValidatorModel):
    Id: Optional[str] = None
    Code: Optional[QueryErrorCodeType] = None
    Message: Optional[str] = None


class MetricDataResult(BaseValidatorModel):
    Id: Optional[str] = None
    Timestamps: Optional[List[datetime]] = None
    Values: Optional[List[int]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BlacklistEntry(BaseValidatorModel):
    RblName: Optional[str] = None
    ListingTime: Optional[datetime] = None
    Description: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class Content(BaseValidatorModel):
    Data: str
    Charset: Optional[str] = None


class Bounce(BaseValidatorModel):
    BounceType: Optional[BounceTypeType] = None
    BounceSubType: Optional[str] = None
    DiagnosticCode: Optional[str] = None


class BulkEmailEntryResult(BaseValidatorModel):
    Status: Optional[BulkEmailStatusType] = None
    Error: Optional[str] = None
    MessageId: Optional[str] = None


class Destination(BaseValidatorModel):
    ToAddresses: Optional[List[str]] = None
    CcAddresses: Optional[List[str]] = None
    BccAddresses: Optional[List[str]] = None


class MessageHeader(BaseValidatorModel):
    Name: str
    Value: str


class MessageTag(BaseValidatorModel):
    Name: str
    Value: str


class CancelExportJobRequest(BaseValidatorModel):
    JobId: str


class CloudWatchDimensionConfiguration(BaseValidatorModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str


class Complaint(BaseValidatorModel):
    ComplaintSubType: Optional[str] = None
    ComplaintFeedbackType: Optional[str] = None


class ContactListDestination(BaseValidatorModel):
    ContactListName: str
    ContactListImportAction: ContactListImportActionType


class ContactList(BaseValidatorModel):
    ContactListName: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class TopicPreference(BaseValidatorModel):
    TopicName: str
    SubscriptionStatus: SubscriptionStatusType


class DeliveryOptions(BaseValidatorModel):
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None
    MaxDeliverySeconds: Optional[int] = None


class SendingOptions(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class TrackingOptions(BaseValidatorModel):
    CustomRedirectDomain: str
    HttpsPolicy: Optional[HttpsPolicyType] = None


class Topic(BaseValidatorModel):
    TopicName: str
    DisplayName: str
    DefaultSubscriptionStatus: SubscriptionStatusType
    Description: Optional[str] = None


class CreateCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class CreateEmailIdentityPolicyRequest(BaseValidatorModel):
    EmailIdentity: str
    PolicyName: str
    Policy: str


class DkimSigningAttributes(BaseValidatorModel):
    DomainSigningSelector: Optional[str] = None
    DomainSigningPrivateKey: Optional[str] = None
    NextSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    DomainSigningAttributesOrigin: Optional[DkimSigningAttributesOriginType] = None


class DkimAttributes(BaseValidatorModel):
    SigningEnabled: Optional[bool] = None
    Status: Optional[DkimStatusType] = None
    Tokens: Optional[List[str]] = None
    SigningAttributesOrigin: Optional[DkimSigningAttributesOriginType] = None
    NextSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    CurrentSigningKeyLength: Optional[DkimSigningKeyLengthType] = None
    LastKeyGenerationTimestamp: Optional[datetime] = None


class EmailTemplateContent(BaseValidatorModel):
    Subject: Optional[str] = None
    Text: Optional[str] = None
    Html: Optional[str] = None


class ExportDestination(BaseValidatorModel):
    DataFormat: DataFormatType
    S3Url: Optional[str] = None


class ImportDataSource(BaseValidatorModel):
    S3Url: str
    DataFormat: DataFormatType


class CustomVerificationEmailTemplateMetadata(BaseValidatorModel):
    TemplateName: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None


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


class DashboardAttributes(BaseValidatorModel):
    EngagementMetrics: Optional[FeatureStatusType] = None


class DashboardOptions(BaseValidatorModel):
    EngagementMetrics: Optional[FeatureStatusType] = None


class DedicatedIpPool(BaseValidatorModel):
    PoolName: str
    ScalingMode: ScalingModeType


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


class DeleteContactListRequest(BaseValidatorModel):
    ContactListName: str


class DeleteContactRequest(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str


class DeleteCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str


class DeleteDedicatedIpPoolRequest(BaseValidatorModel):
    PoolName: str


class DeleteEmailIdentityPolicyRequest(BaseValidatorModel):
    EmailIdentity: str
    PolicyName: str


class DeleteEmailIdentityRequest(BaseValidatorModel):
    EmailIdentity: str


class DeleteEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str


class DeleteMultiRegionEndpointRequest(BaseValidatorModel):
    EndpointName: str


class DeleteSuppressedDestinationRequest(BaseValidatorModel):
    EmailAddress: str


class DeliverabilityTestReport(BaseValidatorModel):
    ReportId: Optional[str] = None
    ReportName: Optional[str] = None
    Subject: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    CreateDate: Optional[datetime] = None
    DeliverabilityTestStatus: Optional[DeliverabilityTestStatusType] = None


class RouteDetails(BaseValidatorModel):
    Region: str


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


class EmailTemplateMetadata(BaseValidatorModel):
    TemplateName: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class EventBridgeDestination(BaseValidatorModel):
    EventBusArn: str


class KinesisFirehoseDestination(BaseValidatorModel):
    IamRoleArn: str
    DeliveryStreamArn: str


class PinpointDestination(BaseValidatorModel):
    ApplicationArn: Optional[str] = None


class SnsDestination(BaseValidatorModel):
    TopicArn: str


class ExportJobSummary(BaseValidatorModel):
    JobId: Optional[str] = None
    ExportSourceType: Optional[ExportSourceTypeType] = None
    JobStatus: Optional[JobStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    CompletedTimestamp: Optional[datetime] = None


class ExportMetric(BaseValidatorModel):
    Name: Optional[MetricType] = None
    Aggregation: Optional[MetricAggregationType] = None


class ExportStatistics(BaseValidatorModel):
    ProcessedRecordsCount: Optional[int] = None
    ExportedRecordsCount: Optional[int] = None


class FailureInfo(BaseValidatorModel):
    FailedRecordsS3Url: Optional[str] = None
    ErrorMessage: Optional[str] = None


class SendQuota(BaseValidatorModel):
    Max24HourSend: Optional[float] = None
    MaxSendRate: Optional[float] = None
    SentLast24Hours: Optional[float] = None


class SuppressionAttributes(BaseValidatorModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None


class GetBlacklistReportsRequest(BaseValidatorModel):
    BlacklistItemNames: List[str]


class GetConfigurationSetEventDestinationsRequest(BaseValidatorModel):
    ConfigurationSetName: str


class GetConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str


class ReputationOptionsOutput(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None


class SuppressionOptionsOutput(BaseValidatorModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None


class GetContactListRequest(BaseValidatorModel):
    ContactListName: str


class GetContactRequest(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str


class GetCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str


class GetDedicatedIpPoolRequest(BaseValidatorModel):
    PoolName: str


class GetDedicatedIpRequest(BaseValidatorModel):
    Ip: str


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


class GetEmailIdentityPoliciesRequest(BaseValidatorModel):
    EmailIdentity: str


class GetEmailIdentityRequest(BaseValidatorModel):
    EmailIdentity: str


class MailFromAttributes(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType


class GetEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str


class GetExportJobRequest(BaseValidatorModel):
    JobId: str


class GetImportJobRequest(BaseValidatorModel):
    JobId: str


class GetMessageInsightsRequest(BaseValidatorModel):
    MessageId: str


class GetMultiRegionEndpointRequest(BaseValidatorModel):
    EndpointName: str


class Route(BaseValidatorModel):
    Region: str


class GetSuppressedDestinationRequest(BaseValidatorModel):
    EmailAddress: str


class GuardianAttributes(BaseValidatorModel):
    OptimizedSharedDelivery: Optional[FeatureStatusType] = None


class GuardianOptions(BaseValidatorModel):
    OptimizedSharedDelivery: Optional[FeatureStatusType] = None


class IdentityInfo(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    IdentityName: Optional[str] = None
    SendingEnabled: Optional[bool] = None
    VerificationStatus: Optional[VerificationStatusType] = None


class SuppressionListDestination(BaseValidatorModel):
    SuppressionListImportAction: SuppressionListImportActionType


class InboxPlacementTrackingOption(BaseValidatorModel):
    Global: Optional[bool] = None
    TrackedIsps: Optional[List[str]] = None


class ListConfigurationSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListContactListsRequest(BaseValidatorModel):
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None


class TopicFilter(BaseValidatorModel):
    TopicName: Optional[str] = None
    UseDefaultIfPreferenceUnavailable: Optional[bool] = None


class ListCustomVerificationEmailTemplatesRequest(BaseValidatorModel):
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


class ListEmailTemplatesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListExportJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None
    ExportSourceType: Optional[ExportSourceTypeType] = None
    JobStatus: Optional[JobStatusType] = None


class ListImportJobsRequest(BaseValidatorModel):
    ImportDestinationType: Optional[ImportDestinationTypeType] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListManagementOptions(BaseValidatorModel):
    ContactListName: str
    TopicName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListMultiRegionEndpointsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class MultiRegionEndpoint(BaseValidatorModel):
    EndpointName: Optional[str] = None
    Status: Optional[StatusType] = None
    EndpointId: Optional[str] = None
    Regions: Optional[List[str]] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class ListRecommendationsRequest(BaseValidatorModel):
    Filter: Optional[Dict[ListRecommendationsFilterKeyType, str]] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class Recommendation(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Type: Optional[RecommendationTypeType] = None
    Description: Optional[str] = None
    Status: Optional[RecommendationStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Impact: Optional[RecommendationImpactType] = None


class SuppressedDestinationSummary(BaseValidatorModel):
    EmailAddress: str
    Reason: SuppressionListReasonType
    LastUpdateTime: datetime


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class MessageInsightsFiltersOutput(BaseValidatorModel):
    FromEmailAddress: Optional[List[str]] = None
    Destination: Optional[List[str]] = None
    Subject: Optional[List[str]] = None
    Isp: Optional[List[str]] = None
    LastDeliveryEvent: Optional[List[DeliveryEventTypeType]] = None
    LastEngagementEvent: Optional[List[EngagementEventTypeType]] = None


class MessageInsightsFilters(BaseValidatorModel):
    FromEmailAddress: Optional[List[str]] = None
    Destination: Optional[List[str]] = None
    Subject: Optional[List[str]] = None
    Isp: Optional[List[str]] = None
    LastDeliveryEvent: Optional[List[DeliveryEventTypeType]] = None
    LastEngagementEvent: Optional[List[EngagementEventTypeType]] = None


class PutAccountDedicatedIpWarmupAttributesRequest(BaseValidatorModel):
    AutoWarmupEnabled: Optional[bool] = None


class PutAccountDetailsRequest(BaseValidatorModel):
    MailType: MailTypeType
    WebsiteURL: str
    ContactLanguage: Optional[ContactLanguageType] = None
    UseCaseDescription: Optional[str] = None
    AdditionalContactEmailAddresses: Optional[List[str]] = None
    ProductionAccessEnabled: Optional[bool] = None


class PutAccountSendingAttributesRequest(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None


class PutAccountSuppressionAttributesRequest(BaseValidatorModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None


class PutConfigurationSetArchivingOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    ArchiveArn: Optional[str] = None


class PutConfigurationSetDeliveryOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    TlsPolicy: Optional[TlsPolicyType] = None
    SendingPoolName: Optional[str] = None
    MaxDeliverySeconds: Optional[int] = None


class PutConfigurationSetReputationOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    ReputationMetricsEnabled: Optional[bool] = None


class PutConfigurationSetSendingOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    SendingEnabled: Optional[bool] = None


class PutConfigurationSetSuppressionOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None


class PutConfigurationSetTrackingOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    CustomRedirectDomain: Optional[str] = None
    HttpsPolicy: Optional[HttpsPolicyType] = None


class PutDedicatedIpInPoolRequest(BaseValidatorModel):
    Ip: str
    DestinationPoolName: str


class PutDedicatedIpPoolScalingAttributesRequest(BaseValidatorModel):
    PoolName: str
    ScalingMode: ScalingModeType


class PutDedicatedIpWarmupAttributesRequest(BaseValidatorModel):
    Ip: str
    WarmupPercentage: int


class PutEmailIdentityConfigurationSetAttributesRequest(BaseValidatorModel):
    EmailIdentity: str
    ConfigurationSetName: Optional[str] = None


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


class PutSuppressedDestinationRequest(BaseValidatorModel):
    EmailAddress: str
    Reason: SuppressionListReasonType


class ReplacementTemplate(BaseValidatorModel):
    ReplacementTemplateData: Optional[str] = None


class SOARecord(BaseValidatorModel):
    PrimaryNameServer: Optional[str] = None
    AdminEmail: Optional[str] = None
    SerialNumber: Optional[int] = None


class SendCustomVerificationEmailRequest(BaseValidatorModel):
    EmailAddress: str
    TemplateName: str
    ConfigurationSetName: Optional[str] = None


class SuppressedDestinationAttributes(BaseValidatorModel):
    MessageId: Optional[str] = None
    FeedbackId: Optional[str] = None


class SuppressionOptions(BaseValidatorModel):
    SuppressedReasons: Optional[List[SuppressionListReasonType]] = None


class TestRenderEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    TemplateData: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class UpdateEmailIdentityPolicyRequest(BaseValidatorModel):
    EmailIdentity: str
    PolicyName: str
    Policy: str


class AccountDetails(BaseValidatorModel):
    MailType: Optional[MailTypeType] = None
    WebsiteURL: Optional[str] = None
    ContactLanguage: Optional[ContactLanguageType] = None
    UseCaseDescription: Optional[str] = None
    AdditionalContactEmailAddresses: Optional[List[str]] = None
    ReviewDetails: Optional[ReviewDetails] = None


class BatchGetMetricDataQuery(BaseValidatorModel):
    Id: str
    Namespace: Literal['VDM']
    Metric: MetricType
    StartDate: Timestamp
    EndDate: Timestamp
    Dimensions: Optional[Dict[MetricDimensionNameType, str]] = None


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


class ListSuppressedDestinationsRequest(BaseValidatorModel):
    Reasons: Optional[List[SuppressionListReasonType]] = None
    StartDate: Optional[Timestamp] = None
    EndDate: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ReputationOptions(BaseValidatorModel):
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[Timestamp] = None


class BatchGetMetricDataResponse(BaseValidatorModel):
    Results: List[MetricDataResult]
    Errors: List[MetricDataError]
    ResponseMetadata: ResponseMetadata


class CreateDeliverabilityTestReportResponse(BaseValidatorModel):
    ReportId: str
    DeliverabilityTestStatus: DeliverabilityTestStatusType
    ResponseMetadata: ResponseMetadata


class CreateExportJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class CreateImportJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class CreateMultiRegionEndpointResponse(BaseValidatorModel):
    Status: StatusType
    EndpointId: str
    ResponseMetadata: ResponseMetadata


class DeleteMultiRegionEndpointResponse(BaseValidatorModel):
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class GetCustomVerificationEmailTemplateResponse(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str
    ResponseMetadata: ResponseMetadata


class GetEmailIdentityPoliciesResponse(BaseValidatorModel):
    Policies: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListConfigurationSetsResponse(BaseValidatorModel):
    ConfigurationSets: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDedicatedIpPoolsResponse(BaseValidatorModel):
    DedicatedIpPools: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutEmailIdentityDkimSigningAttributesResponse(BaseValidatorModel):
    DkimStatus: DkimStatusType
    DkimTokens: List[str]
    ResponseMetadata: ResponseMetadata


class SendCustomVerificationEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class TestRenderEmailTemplateResponse(BaseValidatorModel):
    RenderedTemplate: str
    ResponseMetadata: ResponseMetadata


class GetBlacklistReportsResponse(BaseValidatorModel):
    BlacklistReport: Dict[str, List[BlacklistEntry]]
    ResponseMetadata: ResponseMetadata


class RawMessage(BaseValidatorModel):
    Data: Blob


class Body(BaseValidatorModel):
    Text: Optional[Content] = None
    Html: Optional[Content] = None


class SendBulkEmailResponse(BaseValidatorModel):
    BulkEmailEntryResults: List[BulkEmailEntryResult]
    ResponseMetadata: ResponseMetadata


class CloudWatchDestinationOutput(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfiguration]


class CloudWatchDestination(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfiguration]


class EventDetails(BaseValidatorModel):
    Bounce: Optional[Bounce] = None
    Complaint: Optional[Complaint] = None


class ListContactListsResponse(BaseValidatorModel):
    ContactLists: List[ContactList]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Contact(BaseValidatorModel):
    EmailAddress: Optional[str] = None
    TopicPreferences: Optional[List[TopicPreference]] = None
    TopicDefaultPreferences: Optional[List[TopicPreference]] = None
    UnsubscribeAll: Optional[bool] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class CreateContactRequest(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: Optional[List[TopicPreference]] = None
    UnsubscribeAll: Optional[bool] = None
    AttributesData: Optional[str] = None


class GetContactResponse(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: List[TopicPreference]
    TopicDefaultPreferences: List[TopicPreference]
    UnsubscribeAll: bool
    AttributesData: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class UpdateContactRequest(BaseValidatorModel):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: Optional[List[TopicPreference]] = None
    UnsubscribeAll: Optional[bool] = None
    AttributesData: Optional[str] = None


class CreateDedicatedIpPoolRequest(BaseValidatorModel):
    PoolName: str
    Tags: Optional[List[Tag]] = None
    ScalingMode: Optional[ScalingModeType] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CreateContactListRequest(BaseValidatorModel):
    ContactListName: str
    Topics: Optional[List[Topic]] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class GetContactListResponse(BaseValidatorModel):
    ContactListName: str
    Topics: List[Topic]
    Description: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateContactListRequest(BaseValidatorModel):
    ContactListName: str
    Topics: Optional[List[Topic]] = None
    Description: Optional[str] = None


class CreateEmailIdentityRequest(BaseValidatorModel):
    EmailIdentity: str
    Tags: Optional[List[Tag]] = None
    DkimSigningAttributes: Optional[DkimSigningAttributes] = None
    ConfigurationSetName: Optional[str] = None


class PutEmailIdentityDkimSigningAttributesRequest(BaseValidatorModel):
    EmailIdentity: str
    SigningAttributesOrigin: DkimSigningAttributesOriginType
    SigningAttributes: Optional[DkimSigningAttributes] = None


class CreateEmailIdentityResponse(BaseValidatorModel):
    IdentityType: IdentityTypeType
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributes
    ResponseMetadata: ResponseMetadata


class CreateEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    TemplateContent: EmailTemplateContent


class GetEmailTemplateResponse(BaseValidatorModel):
    TemplateName: str
    TemplateContent: EmailTemplateContent
    ResponseMetadata: ResponseMetadata


class Template(BaseValidatorModel):
    TemplateName: Optional[str] = None
    TemplateArn: Optional[str] = None
    TemplateContent: Optional[EmailTemplateContent] = None
    TemplateData: Optional[str] = None
    Headers: Optional[List[MessageHeader]] = None


class UpdateEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    TemplateContent: EmailTemplateContent


class ListCustomVerificationEmailTemplatesResponse(BaseValidatorModel):
    CustomVerificationEmailTemplates: List[CustomVerificationEmailTemplateMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DailyVolume(BaseValidatorModel):
    StartDate: Optional[datetime] = None
    VolumeStatistics: Optional[VolumeStatistics] = None
    DomainIspPlacements: Optional[List[DomainIspPlacement]] = None


class OverallVolume(BaseValidatorModel):
    VolumeStatistics: Optional[VolumeStatistics] = None
    ReadRatePercent: Optional[float] = None
    DomainIspPlacements: Optional[List[DomainIspPlacement]] = None


class GetDedicatedIpPoolResponse(BaseValidatorModel):
    DedicatedIpPool: DedicatedIpPool
    ResponseMetadata: ResponseMetadata


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


class Details(BaseValidatorModel):
    RoutesDetails: List[RouteDetails]


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


class ListEmailTemplatesResponse(BaseValidatorModel):
    TemplatesMetadata: List[EmailTemplateMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListExportJobsResponse(BaseValidatorModel):
    ExportJobs: List[ExportJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MetricsDataSourceOutput(BaseValidatorModel):
    Dimensions: Dict[MetricDimensionNameType, List[str]]
    Namespace: Literal['VDM']
    Metrics: List[ExportMetric]
    StartDate: datetime
    EndDate: datetime


class MetricsDataSource(BaseValidatorModel):
    Dimensions: Dict[MetricDimensionNameType, List[str]]
    Namespace: Literal['VDM']
    Metrics: List[ExportMetric]
    StartDate: Timestamp
    EndDate: Timestamp


class IspPlacement(BaseValidatorModel):
    IspName: Optional[str] = None
    PlacementStatistics: Optional[PlacementStatistics] = None


class GetMultiRegionEndpointResponse(BaseValidatorModel):
    EndpointName: str
    EndpointId: str
    Routes: List[Route]
    Status: StatusType
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class VdmAttributes(BaseValidatorModel):
    VdmEnabled: FeatureStatusType
    DashboardAttributes: Optional[DashboardAttributes] = None
    GuardianAttributes: Optional[GuardianAttributes] = None


class VdmOptions(BaseValidatorModel):
    DashboardOptions: Optional[DashboardOptions] = None
    GuardianOptions: Optional[GuardianOptions] = None


class ListEmailIdentitiesResponse(BaseValidatorModel):
    EmailIdentities: List[IdentityInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ImportDestination(BaseValidatorModel):
    SuppressionListDestination: Optional[SuppressionListDestination] = None
    ContactListDestination: Optional[ContactListDestination] = None

InboxPlacementTrackingOptionUnion = Union[InboxPlacementTrackingOption, InboxPlacementTrackingOptionOutput]


class ListContactsFilter(BaseValidatorModel):
    FilteredStatus: Optional[SubscriptionStatusType] = None
    TopicFilter: Optional[TopicFilter] = None


class ListMultiRegionEndpointsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMultiRegionEndpointsResponse(BaseValidatorModel):
    MultiRegionEndpoints: List[MultiRegionEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRecommendationsResponse(BaseValidatorModel):
    Recommendations: List[Recommendation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSuppressedDestinationsResponse(BaseValidatorModel):
    SuppressedDestinationSummaries: List[SuppressedDestinationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MessageInsightsDataSourceOutput(BaseValidatorModel):
    StartDate: datetime
    EndDate: datetime
    Include: Optional[MessageInsightsFiltersOutput] = None
    Exclude: Optional[MessageInsightsFiltersOutput] = None
    MaxResults: Optional[int] = None


class MessageInsightsDataSource(BaseValidatorModel):
    StartDate: Timestamp
    EndDate: Timestamp
    Include: Optional[MessageInsightsFilters] = None
    Exclude: Optional[MessageInsightsFilters] = None
    MaxResults: Optional[int] = None


class ReplacementEmailContent(BaseValidatorModel):
    ReplacementTemplate: Optional[ReplacementTemplate] = None


class VerificationInfo(BaseValidatorModel):
    LastCheckedTimestamp: Optional[datetime] = None
    LastSuccessTimestamp: Optional[datetime] = None
    ErrorType: Optional[VerificationErrorType] = None
    SOARecord: Optional[SOARecord] = None


class SuppressedDestination(BaseValidatorModel):
    EmailAddress: str
    Reason: SuppressionListReasonType
    LastUpdateTime: datetime
    Attributes: Optional[SuppressedDestinationAttributes] = None

SuppressionOptionsUnion = Union[SuppressionOptions, SuppressionOptionsOutput]


class BatchGetMetricDataRequest(BaseValidatorModel):
    Queries: List[BatchGetMetricDataQuery]

ReputationOptionsUnion = Union[ReputationOptions, ReputationOptionsOutput]


class Message(BaseValidatorModel):
    Subject: Content
    Body: Body
    Headers: Optional[List[MessageHeader]] = None


class EventDestination(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutput] = None
    SnsDestination: Optional[SnsDestination] = None
    EventBridgeDestination: Optional[EventBridgeDestination] = None
    PinpointDestination: Optional[PinpointDestination] = None

CloudWatchDestinationUnion = Union[CloudWatchDestination, CloudWatchDestinationOutput]


class InsightsEvent(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Type: Optional[EventTypeType] = None
    Details: Optional[EventDetails] = None


class ListContactsResponse(BaseValidatorModel):
    Contacts: List[Contact]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BulkEmailContent(BaseValidatorModel):
    Template: Optional[Template] = None


class GetDomainStatisticsReportResponse(BaseValidatorModel):
    OverallVolume: OverallVolume
    DailyVolumes: List[DailyVolume]
    ResponseMetadata: ResponseMetadata


class CreateMultiRegionEndpointRequest(BaseValidatorModel):
    EndpointName: str
    Details: Details
    Tags: Optional[List[Tag]] = None


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


class GetAccountResponse(BaseValidatorModel):
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    SendQuota: SendQuota
    SendingEnabled: bool
    SuppressionAttributes: SuppressionAttributes
    Details: AccountDetails
    VdmAttributes: VdmAttributes
    ResponseMetadata: ResponseMetadata


class PutAccountVdmAttributesRequest(BaseValidatorModel):
    VdmAttributes: VdmAttributes


class GetConfigurationSetResponse(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptions
    DeliveryOptions: DeliveryOptions
    ReputationOptions: ReputationOptionsOutput
    SendingOptions: SendingOptions
    Tags: List[Tag]
    SuppressionOptions: SuppressionOptionsOutput
    VdmOptions: VdmOptions
    ArchivingOptions: ArchivingOptions
    ResponseMetadata: ResponseMetadata


class PutConfigurationSetVdmOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    VdmOptions: Optional[VdmOptions] = None


class CreateImportJobRequest(BaseValidatorModel):
    ImportDestination: ImportDestination
    ImportDataSource: ImportDataSource


class GetImportJobResponse(BaseValidatorModel):
    JobId: str
    ImportDestination: ImportDestination
    ImportDataSource: ImportDataSource
    FailureInfo: FailureInfo
    JobStatus: JobStatusType
    CreatedTimestamp: datetime
    CompletedTimestamp: datetime
    ProcessedRecordsCount: int
    FailedRecordsCount: int
    ResponseMetadata: ResponseMetadata


class ImportJobSummary(BaseValidatorModel):
    JobId: Optional[str] = None
    ImportDestination: Optional[ImportDestination] = None
    JobStatus: Optional[JobStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    ProcessedRecordsCount: Optional[int] = None
    FailedRecordsCount: Optional[int] = None


class DomainDeliverabilityTrackingOption(BaseValidatorModel):
    Domain: Optional[str] = None
    SubscriptionStartDate: Optional[Timestamp] = None
    InboxPlacementTrackingOption: Optional[InboxPlacementTrackingOptionUnion] = None


class ListContactsRequest(BaseValidatorModel):
    ContactListName: str
    Filter: Optional[ListContactsFilter] = None
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None


class ExportDataSourceOutput(BaseValidatorModel):
    MetricsDataSource: Optional[MetricsDataSourceOutput] = None
    MessageInsightsDataSource: Optional[MessageInsightsDataSourceOutput] = None


class ExportDataSource(BaseValidatorModel):
    MetricsDataSource: Optional[MetricsDataSource] = None
    MessageInsightsDataSource: Optional[MessageInsightsDataSource] = None


class BulkEmailEntry(BaseValidatorModel):
    Destination: Destination
    ReplacementTags: Optional[List[MessageTag]] = None
    ReplacementEmailContent: Optional[ReplacementEmailContent] = None
    ReplacementHeaders: Optional[List[MessageHeader]] = None


class GetEmailIdentityResponse(BaseValidatorModel):
    IdentityType: IdentityTypeType
    FeedbackForwardingStatus: bool
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributes
    MailFromAttributes: MailFromAttributes
    Policies: Dict[str, str]
    Tags: List[Tag]
    ConfigurationSetName: str
    VerificationStatus: VerificationStatusType
    VerificationInfo: VerificationInfo
    ResponseMetadata: ResponseMetadata


class GetSuppressedDestinationResponse(BaseValidatorModel):
    SuppressedDestination: SuppressedDestination
    ResponseMetadata: ResponseMetadata


class CreateConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: Optional[TrackingOptions] = None
    DeliveryOptions: Optional[DeliveryOptions] = None
    ReputationOptions: Optional[ReputationOptionsUnion] = None
    SendingOptions: Optional[SendingOptions] = None
    Tags: Optional[List[Tag]] = None
    SuppressionOptions: Optional[SuppressionOptionsUnion] = None
    VdmOptions: Optional[VdmOptions] = None
    ArchivingOptions: Optional[ArchivingOptions] = None


class EmailContent(BaseValidatorModel):
    Simple: Optional[Message] = None
    Raw: Optional[RawMessage] = None
    Template: Optional[Template] = None


class GetConfigurationSetEventDestinationsResponse(BaseValidatorModel):
    EventDestinations: List[EventDestination]
    ResponseMetadata: ResponseMetadata


class EventDestinationDefinition(BaseValidatorModel):
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[List[EventTypeType]] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    CloudWatchDestination: Optional[CloudWatchDestinationUnion] = None
    SnsDestination: Optional[SnsDestination] = None
    EventBridgeDestination: Optional[EventBridgeDestination] = None
    PinpointDestination: Optional[PinpointDestination] = None


class EmailInsights(BaseValidatorModel):
    Destination: Optional[str] = None
    Isp: Optional[str] = None
    Events: Optional[List[InsightsEvent]] = None


class ListImportJobsResponse(BaseValidatorModel):
    ImportJobs: List[ImportJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

DomainDeliverabilityTrackingOptionUnion = Union[DomainDeliverabilityTrackingOption, DomainDeliverabilityTrackingOptionOutput]


class GetExportJobResponse(BaseValidatorModel):
    JobId: str
    ExportSourceType: ExportSourceTypeType
    JobStatus: JobStatusType
    ExportDestination: ExportDestination
    ExportDataSource: ExportDataSourceOutput
    CreatedTimestamp: datetime
    CompletedTimestamp: datetime
    FailureInfo: FailureInfo
    Statistics: ExportStatistics
    ResponseMetadata: ResponseMetadata

ExportDataSourceUnion = Union[ExportDataSource, ExportDataSourceOutput]


class SendBulkEmailRequest(BaseValidatorModel):
    DefaultContent: BulkEmailContent
    BulkEmailEntries: List[BulkEmailEntry]
    FromEmailAddress: Optional[str] = None
    FromEmailAddressIdentityArn: Optional[str] = None
    ReplyToAddresses: Optional[List[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    FeedbackForwardingEmailAddressIdentityArn: Optional[str] = None
    DefaultEmailTags: Optional[List[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None
    EndpointId: Optional[str] = None


class CreateDeliverabilityTestReportRequest(BaseValidatorModel):
    FromEmailAddress: str
    Content: EmailContent
    ReportName: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class SendEmailRequest(BaseValidatorModel):
    Content: EmailContent
    FromEmailAddress: Optional[str] = None
    FromEmailAddressIdentityArn: Optional[str] = None
    Destination: Optional[Destination] = None
    ReplyToAddresses: Optional[List[str]] = None
    FeedbackForwardingEmailAddress: Optional[str] = None
    FeedbackForwardingEmailAddressIdentityArn: Optional[str] = None
    EmailTags: Optional[List[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None
    EndpointId: Optional[str] = None
    ListManagementOptions: Optional[ListManagementOptions] = None


class CreateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinition


class UpdateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinition


class GetMessageInsightsResponse(BaseValidatorModel):
    MessageId: str
    FromEmailAddress: str
    Subject: str
    EmailTags: List[MessageTag]
    Insights: List[EmailInsights]
    ResponseMetadata: ResponseMetadata


class PutDeliverabilityDashboardOptionRequest(BaseValidatorModel):
    DashboardEnabled: bool
    SubscribedDomains: Optional[List[DomainDeliverabilityTrackingOptionUnion]] = None


class CreateExportJobRequest(BaseValidatorModel):
    ExportDataSource: ExportDataSourceUnion
    ExportDestination: ExportDestination
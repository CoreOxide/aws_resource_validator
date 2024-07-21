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
from aws_resource_validator.pydantic_models.ses_constants import *

class AddHeaderActionTypeDef(BaseModel):
    HeaderName: str
    HeaderValue: str

class ContentTypeDef(BaseModel):
    Data: str
    Charset: Optional[str] = None

class BounceActionTypeDef(BaseModel):
    SmtpReplyCode: str
    Message: str
    Sender: str
    TopicArn: Optional[str] = None
    StatusCode: Optional[str] = None

class BulkEmailDestinationStatusTypeDef(BaseModel):
    Status: Optional[BulkEmailStatusType] = None
    Error: Optional[str] = None
    MessageId: Optional[str] = None

class DestinationTypeDef(BaseModel):
    ToAddresses: Optional[Sequence[str]] = None
    CcAddresses: Optional[Sequence[str]] = None
    BccAddresses: Optional[Sequence[str]] = None

class MessageTagTypeDef(BaseModel):
    Name: str
    Value: str

class CloneReceiptRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetName: str
    OriginalRuleSetName: str

class CloudWatchDimensionConfigurationTypeDef(BaseModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str

class ConfigurationSetTypeDef(BaseModel):
    Name: str

class TrackingOptionsTypeDef(BaseModel):
    CustomRedirectDomain: Optional[str] = None

class CreateCustomVerificationEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str

class CreateReceiptRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetName: str

class TemplateTypeDef(BaseModel):
    TemplateName: str
    SubjectPart: Optional[str] = None
    TextPart: Optional[str] = None
    HtmlPart: Optional[str] = None

class CustomVerificationEmailTemplateTypeDef(BaseModel):
    TemplateName: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None

class DeleteConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class DeleteCustomVerificationEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str

class DeleteIdentityPolicyRequestRequestTypeDef(BaseModel):
    Identity: str
    PolicyName: str

class DeleteIdentityRequestRequestTypeDef(BaseModel):
    Identity: str

class DeleteReceiptFilterRequestRequestTypeDef(BaseModel):
    FilterName: str

class DeleteReceiptRuleRequestRequestTypeDef(BaseModel):
    RuleSetName: str
    RuleName: str

class DeleteReceiptRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetName: str

class DeleteTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str

class DeleteVerifiedEmailAddressRequestRequestTypeDef(BaseModel):
    EmailAddress: str

class DeliveryOptionsTypeDef(BaseModel):
    TlsPolicy: Optional[TlsPolicyType] = None

class ReceiptRuleSetMetadataTypeDef(BaseModel):
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DescribeConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    ConfigurationSetAttributeNames: Optional[Sequence[ConfigurationSetAttributeType]] = None

class ReputationOptionsTypeDef(BaseModel):
    SendingEnabled: Optional[bool] = None
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None

class DescribeReceiptRuleRequestRequestTypeDef(BaseModel):
    RuleSetName: str
    RuleName: str

class DescribeReceiptRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetName: str

class KinesisFirehoseDestinationTypeDef(BaseModel):
    IAMRoleARN: str
    DeliveryStreamARN: str

class SNSDestinationTypeDef(BaseModel):
    TopicARN: str

class ExtensionFieldTypeDef(BaseModel):
    Name: str
    Value: str

class GetCustomVerificationEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str

class GetIdentityDkimAttributesRequestRequestTypeDef(BaseModel):
    Identities: Sequence[str]

class IdentityDkimAttributesTypeDef(BaseModel):
    DkimEnabled: bool
    DkimVerificationStatus: VerificationStatusType
    DkimTokens: Optional[List[str]] = None

class GetIdentityMailFromDomainAttributesRequestRequestTypeDef(BaseModel):
    Identities: Sequence[str]

class IdentityMailFromDomainAttributesTypeDef(BaseModel):
    MailFromDomain: str
    MailFromDomainStatus: CustomMailFromStatusType
    BehaviorOnMXFailure: BehaviorOnMXFailureType

class GetIdentityNotificationAttributesRequestRequestTypeDef(BaseModel):
    Identities: Sequence[str]

class IdentityNotificationAttributesTypeDef(BaseModel):
    BounceTopic: str
    ComplaintTopic: str
    DeliveryTopic: str
    ForwardingEnabled: bool
    HeadersInBounceNotificationsEnabled: Optional[bool] = None
    HeadersInComplaintNotificationsEnabled: Optional[bool] = None
    HeadersInDeliveryNotificationsEnabled: Optional[bool] = None

class GetIdentityPoliciesRequestRequestTypeDef(BaseModel):
    Identity: str
    PolicyNames: Sequence[str]

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetIdentityVerificationAttributesRequestRequestTypeDef(BaseModel):
    Identities: Sequence[str]

class IdentityVerificationAttributesTypeDef(BaseModel):
    VerificationStatus: VerificationStatusType
    VerificationToken: Optional[str] = None

class SendDataPointTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    DeliveryAttempts: Optional[int] = None
    Bounces: Optional[int] = None
    Complaints: Optional[int] = None
    Rejects: Optional[int] = None

class GetTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str

class LambdaActionTypeDef(BaseModel):
    FunctionArn: str
    TopicArn: Optional[str] = None
    InvocationType: Optional[InvocationTypeType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListConfigurationSetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None

class ListCustomVerificationEmailTemplatesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIdentitiesRequestRequestTypeDef(BaseModel):
    IdentityType: Optional[IdentityTypeType] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None

class ListIdentityPoliciesRequestRequestTypeDef(BaseModel):
    Identity: str

class ListReceiptRuleSetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ListTemplatesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None

class TemplateMetadataTypeDef(BaseModel):
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class PutIdentityPolicyRequestRequestTypeDef(BaseModel):
    Identity: str
    PolicyName: str
    Policy: str

class S3ActionTypeDef(BaseModel):
    BucketName: str
    TopicArn: Optional[str] = None
    ObjectKeyPrefix: Optional[str] = None
    KmsKeyArn: Optional[str] = None

class SNSActionTypeDef(BaseModel):
    TopicArn: str
    Encoding: Optional[SNSActionEncodingType] = None

class StopActionTypeDef(BaseModel):
    Scope: Literal["RuleSet"]
    TopicArn: Optional[str] = None

class WorkmailActionTypeDef(BaseModel):
    OrganizationArn: str
    TopicArn: Optional[str] = None

class ReceiptIpFilterTypeDef(BaseModel):
    Policy: ReceiptFilterPolicyType
    Cidr: str

class ReorderReceiptRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetName: str
    RuleNames: Sequence[str]

class SendCustomVerificationEmailRequestRequestTypeDef(BaseModel):
    EmailAddress: str
    TemplateName: str
    ConfigurationSetName: Optional[str] = None

class SetActiveReceiptRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetName: Optional[str] = None

class SetIdentityDkimEnabledRequestRequestTypeDef(BaseModel):
    Identity: str
    DkimEnabled: bool

class SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef(BaseModel):
    Identity: str
    ForwardingEnabled: bool

class SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef(BaseModel):
    Identity: str
    NotificationType: NotificationTypeType
    Enabled: bool

class SetIdentityMailFromDomainRequestRequestTypeDef(BaseModel):
    Identity: str
    MailFromDomain: Optional[str] = None
    BehaviorOnMXFailure: Optional[BehaviorOnMXFailureType] = None

class SetIdentityNotificationTopicRequestRequestTypeDef(BaseModel):
    Identity: str
    NotificationType: NotificationTypeType
    SnsTopic: Optional[str] = None

class SetReceiptRulePositionRequestRequestTypeDef(BaseModel):
    RuleSetName: str
    RuleName: str
    After: Optional[str] = None

class TestRenderTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    TemplateData: str

class UpdateAccountSendingEnabledRequestRequestTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    Enabled: bool

class UpdateConfigurationSetSendingEnabledRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    Enabled: bool

class UpdateCustomVerificationEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    TemplateContent: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None

class VerifyDomainDkimRequestRequestTypeDef(BaseModel):
    Domain: str

class VerifyDomainIdentityRequestRequestTypeDef(BaseModel):
    Domain: str

class VerifyEmailAddressRequestRequestTypeDef(BaseModel):
    EmailAddress: str

class VerifyEmailIdentityRequestRequestTypeDef(BaseModel):
    EmailAddress: str

class RawMessageTypeDef(BaseModel):
    Data: BlobTypeDef

class BodyTypeDef(BaseModel):
    Text: Optional[ContentTypeDef] = None
    Html: Optional[ContentTypeDef] = None

class BulkEmailDestinationTypeDef(BaseModel):
    Destination: DestinationTypeDef
    ReplacementTags: Optional[Sequence[MessageTagTypeDef]] = None
    ReplacementTemplateData: Optional[str] = None

class SendTemplatedEmailRequestRequestTypeDef(BaseModel):
    Source: str
    Destination: DestinationTypeDef
    Template: str
    TemplateData: str
    ReplyToAddresses: Optional[Sequence[str]] = None
    ReturnPath: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None
    TemplateArn: Optional[str] = None

class CloudWatchDestinationOutputTypeDef(BaseModel):
    DimensionConfigurations: List[CloudWatchDimensionConfigurationTypeDef]

class CloudWatchDestinationTypeDef(BaseModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]

class CreateConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSet: ConfigurationSetTypeDef

class CreateConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef

class UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef

class CreateTemplateRequestRequestTypeDef(BaseModel):
    Template: TemplateTypeDef

class UpdateTemplateRequestRequestTypeDef(BaseModel):
    Template: TemplateTypeDef

class PutConfigurationSetDeliveryOptionsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    DeliveryOptions: Optional[DeliveryOptionsTypeDef] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSendingEnabledResponseTypeDef(BaseModel):
    Enabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomVerificationEmailTemplateResponseTypeDef(BaseModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityPoliciesResponseTypeDef(BaseModel):
    Policies: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSendQuotaResponseTypeDef(BaseModel):
    Max24HourSend: float
    MaxSendRate: float
    SentLast24Hours: float
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateResponseTypeDef(BaseModel):
    Template: TemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsResponseTypeDef(BaseModel):
    ConfigurationSets: List[ConfigurationSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCustomVerificationEmailTemplatesResponseTypeDef(BaseModel):
    CustomVerificationEmailTemplates: List[CustomVerificationEmailTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIdentitiesResponseTypeDef(BaseModel):
    Identities: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIdentityPoliciesResponseTypeDef(BaseModel):
    PolicyNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReceiptRuleSetsResponseTypeDef(BaseModel):
    RuleSets: List[ReceiptRuleSetMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListVerifiedEmailAddressesResponseTypeDef(BaseModel):
    VerifiedEmailAddresses: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SendBounceResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendBulkTemplatedEmailResponseTypeDef(BaseModel):
    Status: List[BulkEmailDestinationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendCustomVerificationEmailResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendRawEmailResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendTemplatedEmailResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestRenderTemplateResponseTypeDef(BaseModel):
    RenderedTemplate: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDomainDkimResponseTypeDef(BaseModel):
    DkimTokens: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDomainIdentityResponseTypeDef(BaseModel):
    VerificationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityDkimAttributesResponseTypeDef(BaseModel):
    DkimAttributes: Dict[str, IdentityDkimAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityMailFromDomainAttributesResponseTypeDef(BaseModel):
    MailFromDomainAttributes: Dict[str, IdentityMailFromDomainAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityNotificationAttributesResponseTypeDef(BaseModel):
    NotificationAttributes: Dict[str, IdentityNotificationAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityVerificationAttributesRequestIdentityExistsWaitTypeDef(BaseModel):
    Identities: Sequence[str]
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetIdentityVerificationAttributesResponseTypeDef(BaseModel):
    VerificationAttributes: Dict[str, IdentityVerificationAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSendStatisticsResponseTypeDef(BaseModel):
    SendDataPoints: List[SendDataPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomVerificationEmailTemplatesRequestListCustomVerificationEmailTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdentitiesRequestListIdentitiesPaginateTypeDef(BaseModel):
    IdentityType: Optional[IdentityTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReceiptRuleSetsRequestListReceiptRuleSetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplatesRequestListTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplatesResponseTypeDef(BaseModel):
    TemplatesMetadata: List[TemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MessageDsnTypeDef(BaseModel):
    ReportingMta: str
    ArrivalDate: Optional[TimestampTypeDef] = None
    ExtensionFields: Optional[Sequence[ExtensionFieldTypeDef]] = None

class RecipientDsnFieldsTypeDef(BaseModel):
    Action: DsnActionType
    Status: str
    FinalRecipient: Optional[str] = None
    RemoteMta: Optional[str] = None
    DiagnosticCode: Optional[str] = None
    LastAttemptDate: Optional[TimestampTypeDef] = None
    ExtensionFields: Optional[Sequence[ExtensionFieldTypeDef]] = None

class ReceiptActionTypeDef(BaseModel):
    S3Action: Optional[S3ActionTypeDef] = None
    BounceAction: Optional[BounceActionTypeDef] = None
    WorkmailAction: Optional[WorkmailActionTypeDef] = None
    LambdaAction: Optional[LambdaActionTypeDef] = None
    StopAction: Optional[StopActionTypeDef] = None
    AddHeaderAction: Optional[AddHeaderActionTypeDef] = None
    SNSAction: Optional[SNSActionTypeDef] = None

class ReceiptFilterTypeDef(BaseModel):
    Name: str
    IpFilter: ReceiptIpFilterTypeDef

class SendRawEmailRequestRequestTypeDef(BaseModel):
    RawMessage: RawMessageTypeDef
    Source: Optional[str] = None
    Destinations: Optional[Sequence[str]] = None
    FromArn: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None

class MessageTypeDef(BaseModel):
    Subject: ContentTypeDef
    Body: BodyTypeDef

class SendBulkTemplatedEmailRequestRequestTypeDef(BaseModel):
    Source: str
    Template: str
    Destinations: Sequence[BulkEmailDestinationTypeDef]
    SourceArn: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    ReturnPath: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    DefaultTags: Optional[Sequence[MessageTagTypeDef]] = None
    TemplateArn: Optional[str] = None
    DefaultTemplateData: Optional[str] = None

class EventDestinationOutputTypeDef(BaseModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutputTypeDef] = None
    SNSDestination: Optional[SNSDestinationTypeDef] = None

class EventDestinationTypeDef(BaseModel):
    Name: str
    MatchingEventTypes: Sequence[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationTypeDef] = None
    SNSDestination: Optional[SNSDestinationTypeDef] = None

class BouncedRecipientInfoTypeDef(BaseModel):
    Recipient: str
    RecipientArn: Optional[str] = None
    BounceType: Optional[BounceTypeType] = None
    RecipientDsnFields: Optional[RecipientDsnFieldsTypeDef] = None

class ReceiptRuleOutputTypeDef(BaseModel):
    Name: str
    Enabled: Optional[bool] = None
    TlsPolicy: Optional[TlsPolicyType] = None
    Recipients: Optional[List[str]] = None
    Actions: Optional[List[ReceiptActionTypeDef]] = None
    ScanEnabled: Optional[bool] = None

class ReceiptRuleTypeDef(BaseModel):
    Name: str
    Enabled: Optional[bool] = None
    TlsPolicy: Optional[TlsPolicyType] = None
    Recipients: Optional[Sequence[str]] = None
    Actions: Optional[Sequence[ReceiptActionTypeDef]] = None
    ScanEnabled: Optional[bool] = None

class CreateReceiptFilterRequestRequestTypeDef(BaseModel):
    Filter: ReceiptFilterTypeDef

class ListReceiptFiltersResponseTypeDef(BaseModel):
    Filters: List[ReceiptFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailRequestRequestTypeDef(BaseModel):
    Source: str
    Destination: DestinationTypeDef
    Message: MessageTypeDef
    ReplyToAddresses: Optional[Sequence[str]] = None
    ReturnPath: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None

class DescribeConfigurationSetResponseTypeDef(BaseModel):
    ConfigurationSet: ConfigurationSetTypeDef
    EventDestinations: List[EventDestinationOutputTypeDef]
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef

class SendBounceRequestRequestTypeDef(BaseModel):
    OriginalMessageId: str
    BounceSender: str
    BouncedRecipientInfoList: Sequence[BouncedRecipientInfoTypeDef]
    Explanation: Optional[str] = None
    MessageDsn: Optional[MessageDsnTypeDef] = None
    BounceSenderArn: Optional[str] = None

class DescribeActiveReceiptRuleSetResponseTypeDef(BaseModel):
    Metadata: ReceiptRuleSetMetadataTypeDef
    Rules: List[ReceiptRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReceiptRuleResponseTypeDef(BaseModel):
    Rule: ReceiptRuleOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReceiptRuleSetResponseTypeDef(BaseModel):
    Metadata: ReceiptRuleSetMetadataTypeDef
    Rules: List[ReceiptRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReceiptRuleRequestRequestTypeDef(BaseModel):
    RuleSetName: str
    Rule: ReceiptRuleTypeDef
    After: Optional[str] = None

class UpdateReceiptRuleRequestRequestTypeDef(BaseModel):
    RuleSetName: str
    Rule: ReceiptRuleTypeDef


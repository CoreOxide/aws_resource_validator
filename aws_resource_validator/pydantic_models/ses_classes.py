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
from aws_resource_validator.pydantic_models.ses_constants import *

class AddHeaderActionTypeDef(BaseValidatorModel):
    HeaderName: str
    HeaderValue: str

class ContentTypeDef(BaseValidatorModel):
    Data: str
    Charset: Optional[str] = None

class BounceActionTypeDef(BaseValidatorModel):
    SmtpReplyCode: str
    Message: str
    Sender: str
    TopicArn: Optional[str] = None
    StatusCode: Optional[str] = None

class BulkEmailDestinationStatusTypeDef(BaseValidatorModel):
    Status: Optional[BulkEmailStatusType] = None
    Error: Optional[str] = None
    MessageId: Optional[str] = None

class DestinationTypeDef(BaseValidatorModel):
    ToAddresses: Optional[Sequence[str]] = None
    CcAddresses: Optional[Sequence[str]] = None
    BccAddresses: Optional[Sequence[str]] = None

class MessageTagTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class CloneReceiptRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    OriginalRuleSetName: str

class CloudWatchDimensionConfigurationTypeDef(BaseValidatorModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str

class ConfigurationSetTypeDef(BaseValidatorModel):
    Name: str

class TrackingOptionsTypeDef(BaseValidatorModel):
    CustomRedirectDomain: Optional[str] = None

class CreateCustomVerificationEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str

class CreateReceiptRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str

class TemplateTypeDef(BaseValidatorModel):
    TemplateName: str
    SubjectPart: Optional[str] = None
    TextPart: Optional[str] = None
    HtmlPart: Optional[str] = None

class CustomVerificationEmailTemplateTypeDef(BaseValidatorModel):
    TemplateName: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None

class DeleteConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class DeleteCustomVerificationEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str

class DeleteIdentityPolicyRequestRequestTypeDef(BaseValidatorModel):
    Identity: str
    PolicyName: str

class DeleteIdentityRequestRequestTypeDef(BaseValidatorModel):
    Identity: str

class DeleteReceiptFilterRequestRequestTypeDef(BaseValidatorModel):
    FilterName: str

class DeleteReceiptRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    RuleName: str

class DeleteReceiptRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str

class DeleteTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str

class DeleteVerifiedEmailAddressRequestRequestTypeDef(BaseValidatorModel):
    EmailAddress: str

class DeliveryOptionsTypeDef(BaseValidatorModel):
    TlsPolicy: Optional[TlsPolicyType] = None

class ReceiptRuleSetMetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DescribeConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    ConfigurationSetAttributeNames: Optional[Sequence[ConfigurationSetAttributeType]] = None

class ReputationOptionsTypeDef(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None

class DescribeReceiptRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    RuleName: str

class DescribeReceiptRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str

class KinesisFirehoseDestinationTypeDef(BaseValidatorModel):
    IAMRoleARN: str
    DeliveryStreamARN: str

class SNSDestinationTypeDef(BaseValidatorModel):
    TopicARN: str

class ExtensionFieldTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class GetCustomVerificationEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str

class GetIdentityDkimAttributesRequestRequestTypeDef(BaseValidatorModel):
    Identities: Sequence[str]

class IdentityDkimAttributesTypeDef(BaseValidatorModel):
    DkimEnabled: bool
    DkimVerificationStatus: VerificationStatusType
    DkimTokens: Optional[List[str]] = None

class GetIdentityMailFromDomainAttributesRequestRequestTypeDef(BaseValidatorModel):
    Identities: Sequence[str]

class IdentityMailFromDomainAttributesTypeDef(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: CustomMailFromStatusType
    BehaviorOnMXFailure: BehaviorOnMXFailureType

class GetIdentityNotificationAttributesRequestRequestTypeDef(BaseValidatorModel):
    Identities: Sequence[str]

class IdentityNotificationAttributesTypeDef(BaseValidatorModel):
    BounceTopic: str
    ComplaintTopic: str
    DeliveryTopic: str
    ForwardingEnabled: bool
    HeadersInBounceNotificationsEnabled: Optional[bool] = None
    HeadersInComplaintNotificationsEnabled: Optional[bool] = None
    HeadersInDeliveryNotificationsEnabled: Optional[bool] = None

class GetIdentityPoliciesRequestRequestTypeDef(BaseValidatorModel):
    Identity: str
    PolicyNames: Sequence[str]

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetIdentityVerificationAttributesRequestRequestTypeDef(BaseValidatorModel):
    Identities: Sequence[str]

class IdentityVerificationAttributesTypeDef(BaseValidatorModel):
    VerificationStatus: VerificationStatusType
    VerificationToken: Optional[str] = None

class SendDataPointTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    DeliveryAttempts: Optional[int] = None
    Bounces: Optional[int] = None
    Complaints: Optional[int] = None
    Rejects: Optional[int] = None

class GetTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str

class LambdaActionTypeDef(BaseValidatorModel):
    FunctionArn: str
    TopicArn: Optional[str] = None
    InvocationType: Optional[InvocationTypeType] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListConfigurationSetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None

class ListCustomVerificationEmailTemplatesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIdentitiesRequestRequestTypeDef(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None

class ListIdentityPoliciesRequestRequestTypeDef(BaseValidatorModel):
    Identity: str

class ListReceiptRuleSetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class ListTemplatesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None

class TemplateMetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class PutIdentityPolicyRequestRequestTypeDef(BaseValidatorModel):
    Identity: str
    PolicyName: str
    Policy: str

class S3ActionTypeDef(BaseValidatorModel):
    BucketName: str
    TopicArn: Optional[str] = None
    ObjectKeyPrefix: Optional[str] = None
    KmsKeyArn: Optional[str] = None

class SNSActionTypeDef(BaseValidatorModel):
    TopicArn: str
    Encoding: Optional[SNSActionEncodingType] = None

class StopActionTypeDef(BaseValidatorModel):
    Scope: Literal["RuleSet"]
    TopicArn: Optional[str] = None

class WorkmailActionTypeDef(BaseValidatorModel):
    OrganizationArn: str
    TopicArn: Optional[str] = None

class ReceiptIpFilterTypeDef(BaseValidatorModel):
    Policy: ReceiptFilterPolicyType
    Cidr: str

class ReorderReceiptRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    RuleNames: Sequence[str]

class SendCustomVerificationEmailRequestRequestTypeDef(BaseValidatorModel):
    EmailAddress: str
    TemplateName: str
    ConfigurationSetName: Optional[str] = None

class SetActiveReceiptRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: Optional[str] = None

class SetIdentityDkimEnabledRequestRequestTypeDef(BaseValidatorModel):
    Identity: str
    DkimEnabled: bool

class SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef(BaseValidatorModel):
    Identity: str
    ForwardingEnabled: bool

class SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef(BaseValidatorModel):
    Identity: str
    NotificationType: NotificationTypeType
    Enabled: bool

class SetIdentityMailFromDomainRequestRequestTypeDef(BaseValidatorModel):
    Identity: str
    MailFromDomain: Optional[str] = None
    BehaviorOnMXFailure: Optional[BehaviorOnMXFailureType] = None

class SetIdentityNotificationTopicRequestRequestTypeDef(BaseValidatorModel):
    Identity: str
    NotificationType: NotificationTypeType
    SnsTopic: Optional[str] = None

class SetReceiptRulePositionRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    RuleName: str
    After: Optional[str] = None

class TestRenderTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateData: str

class UpdateAccountSendingEnabledRequestRequestTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    Enabled: bool

class UpdateConfigurationSetSendingEnabledRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    Enabled: bool

class UpdateCustomVerificationEmailTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    TemplateContent: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None

class VerifyDomainDkimRequestRequestTypeDef(BaseValidatorModel):
    Domain: str

class VerifyDomainIdentityRequestRequestTypeDef(BaseValidatorModel):
    Domain: str

class VerifyEmailAddressRequestRequestTypeDef(BaseValidatorModel):
    EmailAddress: str

class VerifyEmailIdentityRequestRequestTypeDef(BaseValidatorModel):
    EmailAddress: str

class RawMessageTypeDef(BaseValidatorModel):
    Data: BlobTypeDef

class BodyTypeDef(BaseValidatorModel):
    Text: Optional[ContentTypeDef] = None
    Html: Optional[ContentTypeDef] = None

class BulkEmailDestinationTypeDef(BaseValidatorModel):
    Destination: DestinationTypeDef
    ReplacementTags: Optional[Sequence[MessageTagTypeDef]] = None
    ReplacementTemplateData: Optional[str] = None

class SendTemplatedEmailRequestRequestTypeDef(BaseValidatorModel):
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

class CloudWatchDestinationOutputTypeDef(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfigurationTypeDef]

class CloudWatchDestinationTypeDef(BaseValidatorModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]

class CreateConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSet: ConfigurationSetTypeDef

class CreateConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef

class UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef

class CreateTemplateRequestRequestTypeDef(BaseValidatorModel):
    Template: TemplateTypeDef

class UpdateTemplateRequestRequestTypeDef(BaseValidatorModel):
    Template: TemplateTypeDef

class PutConfigurationSetDeliveryOptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    DeliveryOptions: Optional[DeliveryOptionsTypeDef] = None

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSendingEnabledResponseTypeDef(BaseValidatorModel):
    Enabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomVerificationEmailTemplateResponseTypeDef(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityPoliciesResponseTypeDef(BaseValidatorModel):
    Policies: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSendQuotaResponseTypeDef(BaseValidatorModel):
    Max24HourSend: float
    MaxSendRate: float
    SentLast24Hours: float
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateResponseTypeDef(BaseValidatorModel):
    Template: TemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsResponseTypeDef(BaseValidatorModel):
    ConfigurationSets: List[ConfigurationSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCustomVerificationEmailTemplatesResponseTypeDef(BaseValidatorModel):
    CustomVerificationEmailTemplates: List[CustomVerificationEmailTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIdentitiesResponseTypeDef(BaseValidatorModel):
    Identities: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIdentityPoliciesResponseTypeDef(BaseValidatorModel):
    PolicyNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReceiptRuleSetsResponseTypeDef(BaseValidatorModel):
    RuleSets: List[ReceiptRuleSetMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListVerifiedEmailAddressesResponseTypeDef(BaseValidatorModel):
    VerifiedEmailAddresses: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SendBounceResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendBulkTemplatedEmailResponseTypeDef(BaseValidatorModel):
    Status: List[BulkEmailDestinationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendCustomVerificationEmailResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendRawEmailResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendTemplatedEmailResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestRenderTemplateResponseTypeDef(BaseValidatorModel):
    RenderedTemplate: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDomainDkimResponseTypeDef(BaseValidatorModel):
    DkimTokens: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDomainIdentityResponseTypeDef(BaseValidatorModel):
    VerificationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityDkimAttributesResponseTypeDef(BaseValidatorModel):
    DkimAttributes: Dict[str, IdentityDkimAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityMailFromDomainAttributesResponseTypeDef(BaseValidatorModel):
    MailFromDomainAttributes: Dict[str, IdentityMailFromDomainAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityNotificationAttributesResponseTypeDef(BaseValidatorModel):
    NotificationAttributes: Dict[str, IdentityNotificationAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityVerificationAttributesRequestIdentityExistsWaitTypeDef(BaseValidatorModel):
    Identities: Sequence[str]
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetIdentityVerificationAttributesResponseTypeDef(BaseValidatorModel):
    VerificationAttributes: Dict[str, IdentityVerificationAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSendStatisticsResponseTypeDef(BaseValidatorModel):
    SendDataPoints: List[SendDataPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomVerificationEmailTemplatesRequestListCustomVerificationEmailTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdentitiesRequestListIdentitiesPaginateTypeDef(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReceiptRuleSetsRequestListReceiptRuleSetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplatesRequestListTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplatesResponseTypeDef(BaseValidatorModel):
    TemplatesMetadata: List[TemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MessageDsnTypeDef(BaseValidatorModel):
    ReportingMta: str
    ArrivalDate: Optional[TimestampTypeDef] = None
    ExtensionFields: Optional[Sequence[ExtensionFieldTypeDef]] = None

class RecipientDsnFieldsTypeDef(BaseValidatorModel):
    Action: DsnActionType
    Status: str
    FinalRecipient: Optional[str] = None
    RemoteMta: Optional[str] = None
    DiagnosticCode: Optional[str] = None
    LastAttemptDate: Optional[TimestampTypeDef] = None
    ExtensionFields: Optional[Sequence[ExtensionFieldTypeDef]] = None

class ReceiptActionTypeDef(BaseValidatorModel):
    S3Action: Optional[S3ActionTypeDef] = None
    BounceAction: Optional[BounceActionTypeDef] = None
    WorkmailAction: Optional[WorkmailActionTypeDef] = None
    LambdaAction: Optional[LambdaActionTypeDef] = None
    StopAction: Optional[StopActionTypeDef] = None
    AddHeaderAction: Optional[AddHeaderActionTypeDef] = None
    SNSAction: Optional[SNSActionTypeDef] = None

class ReceiptFilterTypeDef(BaseValidatorModel):
    Name: str
    IpFilter: ReceiptIpFilterTypeDef

class SendRawEmailRequestRequestTypeDef(BaseValidatorModel):
    RawMessage: RawMessageTypeDef
    Source: Optional[str] = None
    Destinations: Optional[Sequence[str]] = None
    FromArn: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None

class MessageTypeDef(BaseValidatorModel):
    Subject: ContentTypeDef
    Body: BodyTypeDef

class SendBulkTemplatedEmailRequestRequestTypeDef(BaseValidatorModel):
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

class EventDestinationOutputTypeDef(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutputTypeDef] = None
    SNSDestination: Optional[SNSDestinationTypeDef] = None

class EventDestinationTypeDef(BaseValidatorModel):
    Name: str
    MatchingEventTypes: Sequence[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    CloudWatchDestination: Optional[CloudWatchDestinationTypeDef] = None
    SNSDestination: Optional[SNSDestinationTypeDef] = None

class BouncedRecipientInfoTypeDef(BaseValidatorModel):
    Recipient: str
    RecipientArn: Optional[str] = None
    BounceType: Optional[BounceTypeType] = None
    RecipientDsnFields: Optional[RecipientDsnFieldsTypeDef] = None

class ReceiptRuleOutputTypeDef(BaseValidatorModel):
    Name: str
    Enabled: Optional[bool] = None
    TlsPolicy: Optional[TlsPolicyType] = None
    Recipients: Optional[List[str]] = None
    Actions: Optional[List[ReceiptActionTypeDef]] = None
    ScanEnabled: Optional[bool] = None

class ReceiptRuleTypeDef(BaseValidatorModel):
    Name: str
    Enabled: Optional[bool] = None
    TlsPolicy: Optional[TlsPolicyType] = None
    Recipients: Optional[Sequence[str]] = None
    Actions: Optional[Sequence[ReceiptActionTypeDef]] = None
    ScanEnabled: Optional[bool] = None

class CreateReceiptFilterRequestRequestTypeDef(BaseValidatorModel):
    Filter: ReceiptFilterTypeDef

class ListReceiptFiltersResponseTypeDef(BaseValidatorModel):
    Filters: List[ReceiptFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailRequestRequestTypeDef(BaseValidatorModel):
    Source: str
    Destination: DestinationTypeDef
    Message: MessageTypeDef
    ReplyToAddresses: Optional[Sequence[str]] = None
    ReturnPath: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[Sequence[MessageTagTypeDef]] = None
    ConfigurationSetName: Optional[str] = None

class DescribeConfigurationSetResponseTypeDef(BaseValidatorModel):
    ConfigurationSet: ConfigurationSetTypeDef
    EventDestinations: List[EventDestinationOutputTypeDef]
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef

class SendBounceRequestRequestTypeDef(BaseValidatorModel):
    OriginalMessageId: str
    BounceSender: str
    BouncedRecipientInfoList: Sequence[BouncedRecipientInfoTypeDef]
    Explanation: Optional[str] = None
    MessageDsn: Optional[MessageDsnTypeDef] = None
    BounceSenderArn: Optional[str] = None

class DescribeActiveReceiptRuleSetResponseTypeDef(BaseValidatorModel):
    Metadata: ReceiptRuleSetMetadataTypeDef
    Rules: List[ReceiptRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReceiptRuleResponseTypeDef(BaseValidatorModel):
    Rule: ReceiptRuleOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReceiptRuleSetResponseTypeDef(BaseValidatorModel):
    Metadata: ReceiptRuleSetMetadataTypeDef
    Rules: List[ReceiptRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReceiptRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    Rule: ReceiptRuleTypeDef
    After: Optional[str] = None

class UpdateReceiptRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    Rule: ReceiptRuleTypeDef


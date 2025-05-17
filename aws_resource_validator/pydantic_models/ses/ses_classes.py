from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ses.ses_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddHeaderAction(BaseValidatorModel):
    HeaderName: str
    HeaderValue: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class Content(BaseValidatorModel):
    Data: str
    Charset: Optional[str] = None


class BounceAction(BaseValidatorModel):
    SmtpReplyCode: str
    Message: str
    Sender: str
    TopicArn: Optional[str] = None
    StatusCode: Optional[str] = None


class BulkEmailDestinationStatus(BaseValidatorModel):
    Status: Optional[BulkEmailStatusType] = None
    Error: Optional[str] = None
    MessageId: Optional[str] = None


class Destination(BaseValidatorModel):
    ToAddresses: Optional[List[str]] = None
    CcAddresses: Optional[List[str]] = None
    BccAddresses: Optional[List[str]] = None


class MessageTag(BaseValidatorModel):
    Name: str
    Value: str


class CloneReceiptRuleSetRequest(BaseValidatorModel):
    RuleSetName: str
    OriginalRuleSetName: str


class CloudWatchDimensionConfiguration(BaseValidatorModel):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str


class ConfigurationSet(BaseValidatorModel):
    Name: str


class ConnectAction(BaseValidatorModel):
    InstanceARN: str
    IAMRoleARN: str


class TrackingOptions(BaseValidatorModel):
    CustomRedirectDomain: Optional[str] = None


# This class is the input for the 'create_custom_verification_email_template' function.
class CreateCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class CreateReceiptRuleSetRequest(BaseValidatorModel):
    RuleSetName: str


class Template(BaseValidatorModel):
    TemplateName: str
    SubjectPart: Optional[str] = None
    TextPart: Optional[str] = None
    HtmlPart: Optional[str] = None


class CustomVerificationEmailTemplate(BaseValidatorModel):
    TemplateName: Optional[str] = None
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None


class DeleteConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str


class DeleteConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteConfigurationSetTrackingOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str


# This class is the input for the 'delete_custom_verification_email_template' function.
class DeleteCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str


class DeleteIdentityPolicyRequest(BaseValidatorModel):
    Identity: str
    PolicyName: str


class DeleteIdentityRequest(BaseValidatorModel):
    Identity: str


class DeleteReceiptFilterRequest(BaseValidatorModel):
    FilterName: str


class DeleteReceiptRuleRequest(BaseValidatorModel):
    RuleSetName: str
    RuleName: str


class DeleteReceiptRuleSetRequest(BaseValidatorModel):
    RuleSetName: str


class DeleteTemplateRequest(BaseValidatorModel):
    TemplateName: str


# This class is the input for the 'delete_verified_email_address' function.
class DeleteVerifiedEmailAddressRequest(BaseValidatorModel):
    EmailAddress: str


class DeliveryOptions(BaseValidatorModel):
    TlsPolicy: Optional[TlsPolicyType] = None


class ReceiptRuleSetMetadata(BaseValidatorModel):
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'describe_configuration_set' function.
class DescribeConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str
    ConfigurationSetAttributeNames: Optional[List[ConfigurationSetAttributeType]] = None


class ReputationOptions(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None


# This class is the input for the 'describe_receipt_rule' function.
class DescribeReceiptRuleRequest(BaseValidatorModel):
    RuleSetName: str
    RuleName: str


# This class is the input for the 'describe_receipt_rule_set' function.
class DescribeReceiptRuleSetRequest(BaseValidatorModel):
    RuleSetName: str


class KinesisFirehoseDestination(BaseValidatorModel):
    IAMRoleARN: str
    DeliveryStreamARN: str


class SNSDestination(BaseValidatorModel):
    TopicARN: str


class ExtensionField(BaseValidatorModel):
    Name: str
    Value: str


# This class is the input for the 'get_custom_verification_email_template' function.
class GetCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str


# This class is the input for the 'get_identity_dkim_attributes' function.
class GetIdentityDkimAttributesRequest(BaseValidatorModel):
    Identities: List[str]


class IdentityDkimAttributes(BaseValidatorModel):
    DkimEnabled: bool
    DkimVerificationStatus: VerificationStatusType
    DkimTokens: Optional[List[str]] = None


# This class is the input for the 'get_identity_mail_from_domain_attributes' function.
class GetIdentityMailFromDomainAttributesRequest(BaseValidatorModel):
    Identities: List[str]


class IdentityMailFromDomainAttributes(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: CustomMailFromStatusType
    BehaviorOnMXFailure: BehaviorOnMXFailureType


# This class is the input for the 'get_identity_notification_attributes' function.
class GetIdentityNotificationAttributesRequest(BaseValidatorModel):
    Identities: List[str]


class IdentityNotificationAttributes(BaseValidatorModel):
    BounceTopic: str
    ComplaintTopic: str
    DeliveryTopic: str
    ForwardingEnabled: bool
    HeadersInBounceNotificationsEnabled: Optional[bool] = None
    HeadersInComplaintNotificationsEnabled: Optional[bool] = None
    HeadersInDeliveryNotificationsEnabled: Optional[bool] = None


# This class is the input for the 'get_identity_policies' function.
class GetIdentityPoliciesRequest(BaseValidatorModel):
    Identity: str
    PolicyNames: List[str]


# This class is the input for the 'get_identity_verification_attributes' function.
class GetIdentityVerificationAttributesRequest(BaseValidatorModel):
    Identities: List[str]


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class IdentityVerificationAttributes(BaseValidatorModel):
    VerificationStatus: VerificationStatusType
    VerificationToken: Optional[str] = None


class SendDataPoint(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    DeliveryAttempts: Optional[int] = None
    Bounces: Optional[int] = None
    Complaints: Optional[int] = None
    Rejects: Optional[int] = None


# This class is the input for the 'get_template' function.
class GetTemplateRequest(BaseValidatorModel):
    TemplateName: str


class LambdaAction(BaseValidatorModel):
    FunctionArn: str
    TopicArn: Optional[str] = None
    InvocationType: Optional[InvocationTypeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_configuration_sets' function.
class ListConfigurationSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_custom_verification_email_templates' function.
class ListCustomVerificationEmailTemplatesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_identities' function.
class ListIdentitiesRequest(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_identity_policies' function.
class ListIdentityPoliciesRequest(BaseValidatorModel):
    Identity: str


# This class is the input for the 'list_receipt_rule_sets' function.
class ListReceiptRuleSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'list_templates' function.
class ListTemplatesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None


class TemplateMetadata(BaseValidatorModel):
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

Timestamp = Union[datetime, str]


class PutIdentityPolicyRequest(BaseValidatorModel):
    Identity: str
    PolicyName: str
    Policy: str


class S3Action(BaseValidatorModel):
    BucketName: str
    TopicArn: Optional[str] = None
    ObjectKeyPrefix: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    IamRoleArn: Optional[str] = None


class SNSAction(BaseValidatorModel):
    TopicArn: str
    Encoding: Optional[SNSActionEncodingType] = None


class StopAction(BaseValidatorModel):
    Scope: Literal['RuleSet']
    TopicArn: Optional[str] = None


class WorkmailAction(BaseValidatorModel):
    OrganizationArn: str
    TopicArn: Optional[str] = None


class ReceiptIpFilter(BaseValidatorModel):
    Policy: ReceiptFilterPolicyType
    Cidr: str


class ReorderReceiptRuleSetRequest(BaseValidatorModel):
    RuleSetName: str
    RuleNames: List[str]


# This class is the input for the 'send_custom_verification_email' function.
class SendCustomVerificationEmailRequest(BaseValidatorModel):
    EmailAddress: str
    TemplateName: str
    ConfigurationSetName: Optional[str] = None


class SetActiveReceiptRuleSetRequest(BaseValidatorModel):
    RuleSetName: Optional[str] = None


class SetIdentityDkimEnabledRequest(BaseValidatorModel):
    Identity: str
    DkimEnabled: bool


class SetIdentityFeedbackForwardingEnabledRequest(BaseValidatorModel):
    Identity: str
    ForwardingEnabled: bool


class SetIdentityHeadersInNotificationsEnabledRequest(BaseValidatorModel):
    Identity: str
    NotificationType: NotificationTypeType
    Enabled: bool


class SetIdentityMailFromDomainRequest(BaseValidatorModel):
    Identity: str
    MailFromDomain: Optional[str] = None
    BehaviorOnMXFailure: Optional[BehaviorOnMXFailureType] = None


class SetIdentityNotificationTopicRequest(BaseValidatorModel):
    Identity: str
    NotificationType: NotificationTypeType
    SnsTopic: Optional[str] = None


class SetReceiptRulePositionRequest(BaseValidatorModel):
    RuleSetName: str
    RuleName: str
    After: Optional[str] = None


# This class is the input for the 'test_render_template' function.
class TestRenderTemplateRequest(BaseValidatorModel):
    TemplateName: str
    TemplateData: str


# This class is the input for the 'update_account_sending_enabled' function.
class UpdateAccountSendingEnabledRequest(BaseValidatorModel):
    Enabled: Optional[bool] = None


# This class is the input for the 'update_configuration_set_reputation_metrics_enabled' function.
class UpdateConfigurationSetReputationMetricsEnabledRequest(BaseValidatorModel):
    ConfigurationSetName: str
    Enabled: bool


# This class is the input for the 'update_configuration_set_sending_enabled' function.
class UpdateConfigurationSetSendingEnabledRequest(BaseValidatorModel):
    ConfigurationSetName: str
    Enabled: bool


# This class is the input for the 'update_custom_verification_email_template' function.
class UpdateCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    TemplateContent: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None


# This class is the input for the 'verify_domain_dkim' function.
class VerifyDomainDkimRequest(BaseValidatorModel):
    Domain: str


# This class is the input for the 'verify_domain_identity' function.
class VerifyDomainIdentityRequest(BaseValidatorModel):
    Domain: str


# This class is the input for the 'verify_email_address' function.
class VerifyEmailAddressRequest(BaseValidatorModel):
    EmailAddress: str


class VerifyEmailIdentityRequest(BaseValidatorModel):
    EmailAddress: str


class RawMessage(BaseValidatorModel):
    Data: Blob


class Body(BaseValidatorModel):
    Text: Optional[Content] = None
    Html: Optional[Content] = None


class BulkEmailDestination(BaseValidatorModel):
    Destination: Destination
    ReplacementTags: Optional[List[MessageTag]] = None
    ReplacementTemplateData: Optional[str] = None


# This class is the input for the 'send_templated_email' function.
class SendTemplatedEmailRequest(BaseValidatorModel):
    Source: str
    Destination: Destination
    Template: str
    TemplateData: str
    ReplyToAddresses: Optional[List[str]] = None
    ReturnPath: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[List[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None
    TemplateArn: Optional[str] = None


class CloudWatchDestinationOutput(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfiguration]


class CloudWatchDestination(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfiguration]


class CreateConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSet: ConfigurationSet


class CreateConfigurationSetTrackingOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptions


class UpdateConfigurationSetTrackingOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptions


class CreateTemplateRequest(BaseValidatorModel):
    Template: Template


class UpdateTemplateRequest(BaseValidatorModel):
    Template: Template


class PutConfigurationSetDeliveryOptionsRequest(BaseValidatorModel):
    ConfigurationSetName: str
    DeliveryOptions: Optional[DeliveryOptions] = None


# This class is the output for the 'verify_email_address' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAccountSendingEnabledResponse(BaseValidatorModel):
    Enabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_custom_verification_email_template' function.
class GetCustomVerificationEmailTemplateResponse(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_identity_policies' function.
class GetIdentityPoliciesResponse(BaseValidatorModel):
    Policies: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSendQuotaResponse(BaseValidatorModel):
    Max24HourSend: float
    MaxSendRate: float
    SentLast24Hours: float
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_template' function.
class GetTemplateResponse(BaseValidatorModel):
    Template: Template
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_configuration_sets' function.
class ListConfigurationSetsResponse(BaseValidatorModel):
    ConfigurationSets: List[ConfigurationSet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_custom_verification_email_templates' function.
class ListCustomVerificationEmailTemplatesResponse(BaseValidatorModel):
    CustomVerificationEmailTemplates: List[CustomVerificationEmailTemplate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_identities' function.
class ListIdentitiesResponse(BaseValidatorModel):
    Identities: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_identity_policies' function.
class ListIdentityPoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_receipt_rule_sets' function.
class ListReceiptRuleSetsResponse(BaseValidatorModel):
    RuleSets: List[ReceiptRuleSetMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListVerifiedEmailAddressesResponse(BaseValidatorModel):
    VerifiedEmailAddresses: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_bounce' function.
class SendBounceResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_bulk_templated_email' function.
class SendBulkTemplatedEmailResponse(BaseValidatorModel):
    Status: List[BulkEmailDestinationStatus]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_custom_verification_email' function.
class SendCustomVerificationEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_email' function.
class SendEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_raw_email' function.
class SendRawEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_templated_email' function.
class SendTemplatedEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_render_template' function.
class TestRenderTemplateResponse(BaseValidatorModel):
    RenderedTemplate: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'verify_domain_dkim' function.
class VerifyDomainDkimResponse(BaseValidatorModel):
    DkimTokens: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'verify_domain_identity' function.
class VerifyDomainIdentityResponse(BaseValidatorModel):
    VerificationToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_identity_dkim_attributes' function.
class GetIdentityDkimAttributesResponse(BaseValidatorModel):
    DkimAttributes: Dict[str, IdentityDkimAttributes]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_identity_mail_from_domain_attributes' function.
class GetIdentityMailFromDomainAttributesResponse(BaseValidatorModel):
    MailFromDomainAttributes: Dict[str, IdentityMailFromDomainAttributes]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_identity_notification_attributes' function.
class GetIdentityNotificationAttributesResponse(BaseValidatorModel):
    NotificationAttributes: Dict[str, IdentityNotificationAttributes]
    ResponseMetadata: ResponseMetadata


class GetIdentityVerificationAttributesRequestWait(BaseValidatorModel):
    Identities: List[str]
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'get_identity_verification_attributes' function.
class GetIdentityVerificationAttributesResponse(BaseValidatorModel):
    VerificationAttributes: Dict[str, IdentityVerificationAttributes]
    ResponseMetadata: ResponseMetadata


class GetSendStatisticsResponse(BaseValidatorModel):
    SendDataPoints: List[SendDataPoint]
    ResponseMetadata: ResponseMetadata


class ListConfigurationSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomVerificationEmailTemplatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIdentitiesRequestPaginate(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReceiptRuleSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_templates' function.
class ListTemplatesResponse(BaseValidatorModel):
    TemplatesMetadata: List[TemplateMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MessageDsn(BaseValidatorModel):
    ReportingMta: str
    ArrivalDate: Optional[Timestamp] = None
    ExtensionFields: Optional[List[ExtensionField]] = None


class RecipientDsnFields(BaseValidatorModel):
    Action: DsnActionType
    Status: str
    FinalRecipient: Optional[str] = None
    RemoteMta: Optional[str] = None
    DiagnosticCode: Optional[str] = None
    LastAttemptDate: Optional[Timestamp] = None
    ExtensionFields: Optional[List[ExtensionField]] = None


class ReceiptAction(BaseValidatorModel):
    S3Action: Optional[S3Action] = None
    BounceAction: Optional[BounceAction] = None
    WorkmailAction: Optional[WorkmailAction] = None
    LambdaAction: Optional[LambdaAction] = None
    StopAction: Optional[StopAction] = None
    AddHeaderAction: Optional[AddHeaderAction] = None
    SNSAction: Optional[SNSAction] = None
    ConnectAction: Optional[ConnectAction] = None


class ReceiptFilter(BaseValidatorModel):
    Name: str
    IpFilter: ReceiptIpFilter


# This class is the input for the 'send_raw_email' function.
class SendRawEmailRequest(BaseValidatorModel):
    RawMessage: RawMessage
    Source: Optional[str] = None
    Destinations: Optional[List[str]] = None
    FromArn: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[List[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None


class Message(BaseValidatorModel):
    Subject: Content
    Body: Body


# This class is the input for the 'send_bulk_templated_email' function.
class SendBulkTemplatedEmailRequest(BaseValidatorModel):
    Source: str
    Template: str
    DefaultTemplateData: str
    Destinations: List[BulkEmailDestination]
    SourceArn: Optional[str] = None
    ReplyToAddresses: Optional[List[str]] = None
    ReturnPath: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    DefaultTags: Optional[List[MessageTag]] = None
    TemplateArn: Optional[str] = None


class EventDestinationOutput(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    CloudWatchDestination: Optional[CloudWatchDestinationOutput] = None
    SNSDestination: Optional[SNSDestination] = None


class EventDestination(BaseValidatorModel):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    CloudWatchDestination: Optional[CloudWatchDestination] = None
    SNSDestination: Optional[SNSDestination] = None


class BouncedRecipientInfo(BaseValidatorModel):
    Recipient: str
    RecipientArn: Optional[str] = None
    BounceType: Optional[BounceTypeType] = None
    RecipientDsnFields: Optional[RecipientDsnFields] = None


class ReceiptRuleOutput(BaseValidatorModel):
    Name: str
    Enabled: Optional[bool] = None
    TlsPolicy: Optional[TlsPolicyType] = None
    Recipients: Optional[List[str]] = None
    Actions: Optional[List[ReceiptAction]] = None
    ScanEnabled: Optional[bool] = None


class ReceiptRule(BaseValidatorModel):
    Name: str
    Enabled: Optional[bool] = None
    TlsPolicy: Optional[TlsPolicyType] = None
    Recipients: Optional[List[str]] = None
    Actions: Optional[List[ReceiptAction]] = None
    ScanEnabled: Optional[bool] = None


class CreateReceiptFilterRequest(BaseValidatorModel):
    Filter: ReceiptFilter


class ListReceiptFiltersResponse(BaseValidatorModel):
    Filters: List[ReceiptFilter]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'send_email' function.
class SendEmailRequest(BaseValidatorModel):
    Source: str
    Destination: Destination
    Message: Message
    ReplyToAddresses: Optional[List[str]] = None
    ReturnPath: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[List[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None


# This class is the output for the 'describe_configuration_set' function.
class DescribeConfigurationSetResponse(BaseValidatorModel):
    ConfigurationSet: ConfigurationSet
    EventDestinations: List[EventDestinationOutput]
    TrackingOptions: TrackingOptions
    DeliveryOptions: DeliveryOptions
    ReputationOptions: ReputationOptions
    ResponseMetadata: ResponseMetadata

EventDestinationUnion = Union[EventDestination, EventDestinationOutput]


# This class is the input for the 'send_bounce' function.
class SendBounceRequest(BaseValidatorModel):
    OriginalMessageId: str
    BounceSender: str
    BouncedRecipientInfoList: List[BouncedRecipientInfo]
    Explanation: Optional[str] = None
    MessageDsn: Optional[MessageDsn] = None
    BounceSenderArn: Optional[str] = None


class DescribeActiveReceiptRuleSetResponse(BaseValidatorModel):
    Metadata: ReceiptRuleSetMetadata
    Rules: List[ReceiptRuleOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_receipt_rule' function.
class DescribeReceiptRuleResponse(BaseValidatorModel):
    Rule: ReceiptRuleOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_receipt_rule_set' function.
class DescribeReceiptRuleSetResponse(BaseValidatorModel):
    Metadata: ReceiptRuleSetMetadata
    Rules: List[ReceiptRuleOutput]
    ResponseMetadata: ResponseMetadata

ReceiptRuleUnion = Union[ReceiptRule, ReceiptRuleOutput]


class CreateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: EventDestinationUnion


class UpdateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: EventDestinationUnion


class CreateReceiptRuleRequest(BaseValidatorModel):
    RuleSetName: str
    Rule: ReceiptRuleUnion
    After: Optional[str] = None


class UpdateReceiptRuleRequest(BaseValidatorModel):
    RuleSetName: str
    Rule: ReceiptRuleUnion
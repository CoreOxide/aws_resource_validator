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
from aws_resource_validator.pydantic_models.ses_constants import *

class AddHeaderAction(BaseValidatorModel):
    HeaderName: str
    HeaderValue: str


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
    ToAddresses: Optional[Sequence[str]] = None
    CcAddresses: Optional[Sequence[str]] = None
    BccAddresses: Optional[Sequence[str]] = None


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


class DescribeConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str
    ConfigurationSetAttributeNames: Optional[Sequence[ConfigurationSetAttributeType]] = None


class ReputationOptions(BaseValidatorModel):
    SendingEnabled: Optional[bool] = None
    ReputationMetricsEnabled: Optional[bool] = None
    LastFreshStart: Optional[datetime] = None


class DescribeReceiptRuleRequest(BaseValidatorModel):
    RuleSetName: str
    RuleName: str


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


class GetCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str


class GetIdentityDkimAttributesRequest(BaseValidatorModel):
    Identities: Sequence[str]


class IdentityDkimAttributes(BaseValidatorModel):
    DkimEnabled: bool
    DkimVerificationStatus: VerificationStatusType
    DkimTokens: Optional[List[str]] = None


class GetIdentityMailFromDomainAttributesRequest(BaseValidatorModel):
    Identities: Sequence[str]


class IdentityMailFromDomainAttributes(BaseValidatorModel):
    MailFromDomain: str
    MailFromDomainStatus: CustomMailFromStatusType
    BehaviorOnMXFailure: BehaviorOnMXFailureType


class GetIdentityNotificationAttributesRequest(BaseValidatorModel):
    Identities: Sequence[str]


class IdentityNotificationAttributes(BaseValidatorModel):
    BounceTopic: str
    ComplaintTopic: str
    DeliveryTopic: str
    ForwardingEnabled: bool
    HeadersInBounceNotificationsEnabled: Optional[bool] = None
    HeadersInComplaintNotificationsEnabled: Optional[bool] = None
    HeadersInDeliveryNotificationsEnabled: Optional[bool] = None


class GetIdentityPoliciesRequest(BaseValidatorModel):
    Identity: str
    PolicyNames: Sequence[str]


class GetIdentityVerificationAttributesRequest(BaseValidatorModel):
    Identities: Sequence[str]


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


class ListConfigurationSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None


class ListCustomVerificationEmailTemplatesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIdentitiesRequest(BaseValidatorModel):
    IdentityType: Optional[IdentityTypeType] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None


class ListIdentityPoliciesRequest(BaseValidatorModel):
    Identity: str


class ListReceiptRuleSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListTemplatesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None


class TemplateMetadata(BaseValidatorModel):
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


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
    Scope: Literal["RuleSet"]
    TopicArn: Optional[str] = None


class WorkmailAction(BaseValidatorModel):
    OrganizationArn: str
    TopicArn: Optional[str] = None


class ReceiptIpFilter(BaseValidatorModel):
    Policy: ReceiptFilterPolicyType
    Cidr: str


class ReorderReceiptRuleSetRequest(BaseValidatorModel):
    RuleSetName: str
    RuleNames: Sequence[str]


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


class TestRenderTemplateRequest(BaseValidatorModel):
    TemplateName: str
    TemplateData: str


class UpdateAccountSendingEnabledRequest(BaseValidatorModel):
    Enabled: Optional[bool] = None


class UpdateConfigurationSetReputationMetricsEnabledRequest(BaseValidatorModel):
    ConfigurationSetName: str
    Enabled: bool


class UpdateConfigurationSetSendingEnabledRequest(BaseValidatorModel):
    ConfigurationSetName: str
    Enabled: bool


class UpdateCustomVerificationEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: Optional[str] = None
    TemplateSubject: Optional[str] = None
    TemplateContent: Optional[str] = None
    SuccessRedirectionURL: Optional[str] = None
    FailureRedirectionURL: Optional[str] = None


class VerifyDomainDkimRequest(BaseValidatorModel):
    Domain: str


class VerifyDomainIdentityRequest(BaseValidatorModel):
    Domain: str


class VerifyEmailAddressRequest(BaseValidatorModel):
    EmailAddress: str


class VerifyEmailIdentityRequest(BaseValidatorModel):
    EmailAddress: str


class Blob(BaseValidatorModel):
    pass


class RawMessage(BaseValidatorModel):
    Data: Blob


class BulkEmailDestination(BaseValidatorModel):
    Destination: Destination
    ReplacementTags: Optional[Sequence[MessageTag]] = None
    ReplacementTemplateData: Optional[str] = None


class SendTemplatedEmailRequest(BaseValidatorModel):
    Source: str
    Destination: Destination
    Template: str
    TemplateData: str
    ReplyToAddresses: Optional[Sequence[str]] = None
    ReturnPath: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[Sequence[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None
    TemplateArn: Optional[str] = None


class CloudWatchDestinationOutput(BaseValidatorModel):
    DimensionConfigurations: List[CloudWatchDimensionConfiguration]


class CloudWatchDestination(BaseValidatorModel):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfiguration]


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


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAccountSendingEnabledResponse(BaseValidatorModel):
    Enabled: bool
    ResponseMetadata: ResponseMetadata


class GetCustomVerificationEmailTemplateResponse(BaseValidatorModel):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str
    ResponseMetadata: ResponseMetadata


class GetIdentityPoliciesResponse(BaseValidatorModel):
    Policies: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSendQuotaResponse(BaseValidatorModel):
    Max24HourSend: float
    MaxSendRate: float
    SentLast24Hours: float
    ResponseMetadata: ResponseMetadata


class GetTemplateResponse(BaseValidatorModel):
    Template: Template
    ResponseMetadata: ResponseMetadata


class ListConfigurationSetsResponse(BaseValidatorModel):
    ConfigurationSets: List[ConfigurationSet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCustomVerificationEmailTemplatesResponse(BaseValidatorModel):
    CustomVerificationEmailTemplates: List[CustomVerificationEmailTemplate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIdentitiesResponse(BaseValidatorModel):
    Identities: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIdentityPoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    ResponseMetadata: ResponseMetadata


class ListReceiptRuleSetsResponse(BaseValidatorModel):
    RuleSets: List[ReceiptRuleSetMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListVerifiedEmailAddressesResponse(BaseValidatorModel):
    VerifiedEmailAddresses: List[str]
    ResponseMetadata: ResponseMetadata


class SendBounceResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendBulkTemplatedEmailResponse(BaseValidatorModel):
    Status: List[BulkEmailDestinationStatus]
    ResponseMetadata: ResponseMetadata


class SendCustomVerificationEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendRawEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendTemplatedEmailResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class TestRenderTemplateResponse(BaseValidatorModel):
    RenderedTemplate: str
    ResponseMetadata: ResponseMetadata


class VerifyDomainDkimResponse(BaseValidatorModel):
    DkimTokens: List[str]
    ResponseMetadata: ResponseMetadata


class VerifyDomainIdentityResponse(BaseValidatorModel):
    VerificationToken: str
    ResponseMetadata: ResponseMetadata


class GetIdentityDkimAttributesResponse(BaseValidatorModel):
    DkimAttributes: Dict[str, IdentityDkimAttributes]
    ResponseMetadata: ResponseMetadata


class GetIdentityMailFromDomainAttributesResponse(BaseValidatorModel):
    MailFromDomainAttributes: Dict[str, IdentityMailFromDomainAttributes]
    ResponseMetadata: ResponseMetadata


class GetIdentityNotificationAttributesResponse(BaseValidatorModel):
    NotificationAttributes: Dict[str, IdentityNotificationAttributes]
    ResponseMetadata: ResponseMetadata


class GetIdentityVerificationAttributesRequestWait(BaseValidatorModel):
    Identities: Sequence[str]
    WaiterConfig: Optional[WaiterConfig] = None


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


class ListTemplatesResponse(BaseValidatorModel):
    TemplatesMetadata: List[TemplateMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class MessageDsn(BaseValidatorModel):
    ReportingMta: str
    ArrivalDate: Optional[Timestamp] = None
    ExtensionFields: Optional[Sequence[ExtensionField]] = None


class RecipientDsnFields(BaseValidatorModel):
    Action: DsnActionType
    Status: str
    FinalRecipient: Optional[str] = None
    RemoteMta: Optional[str] = None
    DiagnosticCode: Optional[str] = None
    LastAttemptDate: Optional[Timestamp] = None
    ExtensionFields: Optional[Sequence[ExtensionField]] = None


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


class SendRawEmailRequest(BaseValidatorModel):
    RawMessage: RawMessage
    Source: Optional[str] = None
    Destinations: Optional[Sequence[str]] = None
    FromArn: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[Sequence[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None


class Body(BaseValidatorModel):
    pass


class Message(BaseValidatorModel):
    Subject: Content
    Body: Body


class SendBulkTemplatedEmailRequest(BaseValidatorModel):
    Source: str
    Template: str
    DefaultTemplateData: str
    Destinations: Sequence[BulkEmailDestination]
    SourceArn: Optional[str] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    ReturnPath: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    DefaultTags: Optional[Sequence[MessageTag]] = None
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
    MatchingEventTypes: Sequence[EventTypeType]
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
    Recipients: Optional[Sequence[str]] = None
    Actions: Optional[Sequence[ReceiptAction]] = None
    ScanEnabled: Optional[bool] = None


class CreateReceiptFilterRequest(BaseValidatorModel):
    Filter: ReceiptFilter


class ListReceiptFiltersResponse(BaseValidatorModel):
    Filters: List[ReceiptFilter]
    ResponseMetadata: ResponseMetadata


class SendEmailRequest(BaseValidatorModel):
    Source: str
    Destination: Destination
    Message: Message
    ReplyToAddresses: Optional[Sequence[str]] = None
    ReturnPath: Optional[str] = None
    SourceArn: Optional[str] = None
    ReturnPathArn: Optional[str] = None
    Tags: Optional[Sequence[MessageTag]] = None
    ConfigurationSetName: Optional[str] = None


class DescribeConfigurationSetResponse(BaseValidatorModel):
    ConfigurationSet: ConfigurationSet
    EventDestinations: List[EventDestinationOutput]
    TrackingOptions: TrackingOptions
    DeliveryOptions: DeliveryOptions
    ReputationOptions: ReputationOptions
    ResponseMetadata: ResponseMetadata


class SendBounceRequest(BaseValidatorModel):
    OriginalMessageId: str
    BounceSender: str
    BouncedRecipientInfoList: Sequence[BouncedRecipientInfo]
    Explanation: Optional[str] = None
    MessageDsn: Optional[MessageDsn] = None
    BounceSenderArn: Optional[str] = None


class DescribeActiveReceiptRuleSetResponse(BaseValidatorModel):
    Metadata: ReceiptRuleSetMetadata
    Rules: List[ReceiptRuleOutput]
    ResponseMetadata: ResponseMetadata


class DescribeReceiptRuleResponse(BaseValidatorModel):
    Rule: ReceiptRuleOutput
    ResponseMetadata: ResponseMetadata


class DescribeReceiptRuleSetResponse(BaseValidatorModel):
    Metadata: ReceiptRuleSetMetadata
    Rules: List[ReceiptRuleOutput]
    ResponseMetadata: ResponseMetadata


class EventDestinationUnion(BaseValidatorModel):
    pass


class CreateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: EventDestinationUnion


class UpdateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: EventDestinationUnion


class ReceiptRuleUnion(BaseValidatorModel):
    pass


class CreateReceiptRuleRequest(BaseValidatorModel):
    RuleSetName: str
    Rule: ReceiptRuleUnion
    After: Optional[str] = None


class UpdateReceiptRuleRequest(BaseValidatorModel):
    RuleSetName: str
    Rule: ReceiptRuleUnion



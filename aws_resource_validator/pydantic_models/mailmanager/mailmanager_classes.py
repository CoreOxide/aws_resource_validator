from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mailmanager.mailmanager_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddHeaderAction(BaseValidatorModel):
    HeaderName: str
    HeaderValue: str


class AddonInstance(BaseValidatorModel):
    AddonInstanceArn: Optional[str] = None
    AddonInstanceId: Optional[str] = None
    AddonName: Optional[str] = None
    AddonSubscriptionId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class AddonSubscription(BaseValidatorModel):
    AddonName: Optional[str] = None
    AddonSubscriptionArn: Optional[str] = None
    AddonSubscriptionId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class AddressFilter(BaseValidatorModel):
    AddressPrefix: Optional[str] = None


class AddressList(BaseValidatorModel):
    AddressListArn: str
    AddressListId: str
    AddressListName: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime


class Analysis(BaseValidatorModel):
    Analyzer: str
    ResultField: str


class ArchiveAction(BaseValidatorModel):
    TargetArchive: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None


class ArchiveBooleanToEvaluate(BaseValidatorModel):
    Attribute: Optional[Literal['HAS_ATTACHMENTS']] = None


class ArchiveRetention(BaseValidatorModel):
    RetentionPeriod: Optional[RetentionPeriodType] = None


class ArchiveStringToEvaluate(BaseValidatorModel):
    Attribute: Optional[ArchiveStringEmailAttributeType] = None


class Archive(BaseValidatorModel):
    ArchiveId: str
    ArchiveName: Optional[str] = None
    ArchiveState: Optional[ArchiveStateType] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ImportDataFormat(BaseValidatorModel):
    ImportDataType: ImportDataTypeType


class IngressPointConfiguration(BaseValidatorModel):
    SecretArn: Optional[str] = None
    SmtpPassword: Optional[str] = None


class DeleteAddonInstanceRequest(BaseValidatorModel):
    AddonInstanceId: str


class DeleteAddonSubscriptionRequest(BaseValidatorModel):
    AddonSubscriptionId: str


class DeleteAddressListRequest(BaseValidatorModel):
    AddressListId: str


class DeleteArchiveRequest(BaseValidatorModel):
    ArchiveId: str


class DeleteIngressPointRequest(BaseValidatorModel):
    IngressPointId: str


class DeleteRelayRequest(BaseValidatorModel):
    RelayId: str


class DeleteRuleSetRequest(BaseValidatorModel):
    RuleSetId: str


class DeleteTrafficPolicyRequest(BaseValidatorModel):
    TrafficPolicyId: str


class DeliverToMailboxAction(BaseValidatorModel):
    MailboxArn: str
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None


class DeliverToQBusinessAction(BaseValidatorModel):
    ApplicationId: str
    IndexId: str
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None


class DeregisterMemberFromAddressListRequest(BaseValidatorModel):
    Address: str
    AddressListId: str


class Envelope(BaseValidatorModel):
    From: Optional[str] = None
    Helo: Optional[str] = None
    To: Optional[List[str]] = None


class S3ExportDestinationConfiguration(BaseValidatorModel):
    S3Location: Optional[str] = None


class ExportStatus(BaseValidatorModel):
    CompletionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    State: Optional[ExportStateType] = None
    SubmissionTimestamp: Optional[datetime] = None


class GetAddonInstanceRequest(BaseValidatorModel):
    AddonInstanceId: str


class GetAddonSubscriptionRequest(BaseValidatorModel):
    AddonSubscriptionId: str


class GetAddressListImportJobRequest(BaseValidatorModel):
    JobId: str


class GetAddressListRequest(BaseValidatorModel):
    AddressListId: str


class GetArchiveExportRequest(BaseValidatorModel):
    ExportId: str


class GetArchiveMessageContentRequest(BaseValidatorModel):
    ArchivedMessageId: str


class MessageBody(BaseValidatorModel):
    Html: Optional[str] = None
    MessageMalformed: Optional[bool] = None
    Text: Optional[str] = None


class GetArchiveMessageRequest(BaseValidatorModel):
    ArchivedMessageId: str


class Metadata(BaseValidatorModel):
    ConfigurationSet: Optional[str] = None
    IngressPointId: Optional[str] = None
    RuleSetId: Optional[str] = None
    SenderHostname: Optional[str] = None
    SenderIpAddress: Optional[str] = None
    SendingMethod: Optional[str] = None
    SendingPool: Optional[str] = None
    SourceArn: Optional[str] = None
    SourceIdentity: Optional[str] = None
    Timestamp: Optional[datetime] = None
    TlsCipherSuite: Optional[str] = None
    TlsProtocol: Optional[str] = None
    TrafficPolicyId: Optional[str] = None


class GetArchiveRequest(BaseValidatorModel):
    ArchiveId: str


class GetArchiveSearchRequest(BaseValidatorModel):
    SearchId: str


class SearchStatus(BaseValidatorModel):
    CompletionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    State: Optional[SearchStateType] = None
    SubmissionTimestamp: Optional[datetime] = None


class GetArchiveSearchResultsRequest(BaseValidatorModel):
    SearchId: str


class GetIngressPointRequest(BaseValidatorModel):
    IngressPointId: str


class GetMemberOfAddressListRequest(BaseValidatorModel):
    Address: str
    AddressListId: str


class GetRelayRequest(BaseValidatorModel):
    RelayId: str


class RelayAuthenticationOutput(BaseValidatorModel):
    NoAuthentication: Optional[Dict[str, Any]] = None
    SecretArn: Optional[str] = None


class GetRuleSetRequest(BaseValidatorModel):
    RuleSetId: str


class GetTrafficPolicyRequest(BaseValidatorModel):
    TrafficPolicyId: str


class IngressAnalysis(BaseValidatorModel):
    Analyzer: str
    ResultField: str


class IngressIsInAddressListOutput(BaseValidatorModel):
    AddressLists: List[str]
    Attribute: Literal['RECIPIENT']


class IngressIpToEvaluate(BaseValidatorModel):
    Attribute: Optional[Literal['SENDER_IP']] = None


class IngressIsInAddressList(BaseValidatorModel):
    AddressLists: List[str]
    Attribute: Literal['RECIPIENT']


class IngressPointPasswordConfiguration(BaseValidatorModel):
    PreviousSmtpPasswordExpiryTimestamp: Optional[datetime] = None
    PreviousSmtpPasswordVersion: Optional[str] = None
    SmtpPasswordVersion: Optional[str] = None


class IngressPoint(BaseValidatorModel):
    IngressPointId: str
    IngressPointName: str
    Status: IngressPointStatusType
    Type: IngressPointTypeType
    ARecord: Optional[str] = None


class IngressStringToEvaluate(BaseValidatorModel):
    Attribute: Optional[Literal['RECIPIENT']] = None


class IngressTlsProtocolToEvaluate(BaseValidatorModel):
    Attribute: Optional[Literal['TLS_PROTOCOL']] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAddonInstancesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListAddonSubscriptionsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListAddressListImportJobsRequest(BaseValidatorModel):
    AddressListId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListAddressListsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListArchiveExportsRequest(BaseValidatorModel):
    ArchiveId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListArchiveSearchesRequest(BaseValidatorModel):
    ArchiveId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListArchivesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListIngressPointsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class SavedAddress(BaseValidatorModel):
    Address: str
    CreatedTimestamp: datetime


class ListRelaysRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class Relay(BaseValidatorModel):
    LastModifiedTimestamp: Optional[datetime] = None
    RelayId: Optional[str] = None
    RelayName: Optional[str] = None


class ListRuleSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class RuleSet(BaseValidatorModel):
    LastModificationDate: Optional[datetime] = None
    RuleSetId: Optional[str] = None
    RuleSetName: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListTrafficPoliciesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class TrafficPolicy(BaseValidatorModel):
    DefaultAction: AcceptActionType
    TrafficPolicyId: str
    TrafficPolicyName: str


class RegisterMemberToAddressListRequest(BaseValidatorModel):
    Address: str
    AddressListId: str


class RelayAction(BaseValidatorModel):
    Relay: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None
    MailFrom: Optional[MailFromType] = None


class RelayAuthentication(BaseValidatorModel):
    NoAuthentication: Optional[Dict[str, Any]] = None
    SecretArn: Optional[str] = None


class ReplaceRecipientActionOutput(BaseValidatorModel):
    ReplaceWith: Optional[List[str]] = None


class ReplaceRecipientAction(BaseValidatorModel):
    ReplaceWith: Optional[List[str]] = None


class S3Action(BaseValidatorModel):
    RoleArn: str
    S3Bucket: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None
    S3Prefix: Optional[str] = None
    S3SseKmsKeyId: Optional[str] = None


class SendAction(BaseValidatorModel):
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None


class RuleIsInAddressListOutput(BaseValidatorModel):
    AddressLists: List[str]
    Attribute: RuleAddressListEmailAttributeType


class RuleDmarcExpressionOutput(BaseValidatorModel):
    Operator: RuleDmarcOperatorType
    Values: List[RuleDmarcPolicyType]


class RuleDmarcExpression(BaseValidatorModel):
    Operator: RuleDmarcOperatorType
    Values: List[RuleDmarcPolicyType]


class RuleIpToEvaluate(BaseValidatorModel):
    Attribute: Optional[Literal['SOURCE_IP']] = None


class RuleIsInAddressList(BaseValidatorModel):
    AddressLists: List[str]
    Attribute: RuleAddressListEmailAttributeType


class RuleNumberToEvaluate(BaseValidatorModel):
    Attribute: Optional[Literal['MESSAGE_SIZE']] = None


class RuleStringToEvaluate(BaseValidatorModel):
    Attribute: Optional[RuleStringEmailAttributeType] = None
    MimeHeaderAttribute: Optional[str] = None


class StartAddressListImportJobRequest(BaseValidatorModel):
    JobId: str

Timestamp = Union[datetime, str]


class StopAddressListImportJobRequest(BaseValidatorModel):
    JobId: str


class StopArchiveExportRequest(BaseValidatorModel):
    ExportId: str


class StopArchiveSearchRequest(BaseValidatorModel):
    SearchId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class ListMembersOfAddressListRequest(BaseValidatorModel):
    AddressListId: str
    Filter: Optional[AddressFilter] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class RuleVerdictToEvaluate(BaseValidatorModel):
    Analysis: Optional[Analysis] = None
    Attribute: Optional[RuleVerdictAttributeType] = None


class ArchiveBooleanExpression(BaseValidatorModel):
    Evaluate: ArchiveBooleanToEvaluate
    Operator: ArchiveBooleanOperatorType


class UpdateArchiveRequest(BaseValidatorModel):
    ArchiveId: str
    ArchiveName: Optional[str] = None
    Retention: Optional[ArchiveRetention] = None


class ArchiveStringExpressionOutput(BaseValidatorModel):
    Evaluate: ArchiveStringToEvaluate
    Operator: Literal['CONTAINS']
    Values: List[str]


class ArchiveStringExpression(BaseValidatorModel):
    Evaluate: ArchiveStringToEvaluate
    Operator: Literal['CONTAINS']
    Values: List[str]


class CreateAddonInstanceRequest(BaseValidatorModel):
    AddonSubscriptionId: str
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateAddonSubscriptionRequest(BaseValidatorModel):
    AddonName: str
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateAddressListRequest(BaseValidatorModel):
    AddressListName: str
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateArchiveRequest(BaseValidatorModel):
    ArchiveName: str
    ClientToken: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Retention: Optional[ArchiveRetention] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CreateAddonInstanceResponse(BaseValidatorModel):
    AddonInstanceId: str
    ResponseMetadata: ResponseMetadata


class CreateAddonSubscriptionResponse(BaseValidatorModel):
    AddonSubscriptionId: str
    ResponseMetadata: ResponseMetadata


class CreateAddressListImportJobResponse(BaseValidatorModel):
    JobId: str
    PreSignedUrl: str
    ResponseMetadata: ResponseMetadata


class CreateAddressListResponse(BaseValidatorModel):
    AddressListId: str
    ResponseMetadata: ResponseMetadata


class CreateArchiveResponse(BaseValidatorModel):
    ArchiveId: str
    ResponseMetadata: ResponseMetadata


class CreateIngressPointResponse(BaseValidatorModel):
    IngressPointId: str
    ResponseMetadata: ResponseMetadata


class CreateRelayResponse(BaseValidatorModel):
    RelayId: str
    ResponseMetadata: ResponseMetadata


class CreateRuleSetResponse(BaseValidatorModel):
    RuleSetId: str
    ResponseMetadata: ResponseMetadata


class CreateTrafficPolicyResponse(BaseValidatorModel):
    TrafficPolicyId: str
    ResponseMetadata: ResponseMetadata


class GetAddonInstanceResponse(BaseValidatorModel):
    AddonInstanceArn: str
    AddonName: str
    AddonSubscriptionId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetAddonSubscriptionResponse(BaseValidatorModel):
    AddonName: str
    AddonSubscriptionArn: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetAddressListResponse(BaseValidatorModel):
    AddressListArn: str
    AddressListId: str
    AddressListName: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetArchiveResponse(BaseValidatorModel):
    ArchiveArn: str
    ArchiveId: str
    ArchiveName: str
    ArchiveState: ArchiveStateType
    CreatedTimestamp: datetime
    KmsKeyArn: str
    LastUpdatedTimestamp: datetime
    Retention: ArchiveRetention
    ResponseMetadata: ResponseMetadata


class GetMemberOfAddressListResponse(BaseValidatorModel):
    Address: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class ListAddonInstancesResponse(BaseValidatorModel):
    AddonInstances: List[AddonInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAddonSubscriptionsResponse(BaseValidatorModel):
    AddonSubscriptions: List[AddonSubscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAddressListsResponse(BaseValidatorModel):
    AddressLists: List[AddressList]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListArchivesResponse(BaseValidatorModel):
    Archives: List[Archive]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class StartArchiveExportResponse(BaseValidatorModel):
    ExportId: str
    ResponseMetadata: ResponseMetadata


class StartArchiveSearchResponse(BaseValidatorModel):
    SearchId: str
    ResponseMetadata: ResponseMetadata


class CreateAddressListImportJobRequest(BaseValidatorModel):
    AddressListId: str
    ImportDataFormat: ImportDataFormat
    Name: str
    ClientToken: Optional[str] = None


class GetAddressListImportJobResponse(BaseValidatorModel):
    AddressListId: str
    CompletedTimestamp: datetime
    CreatedTimestamp: datetime
    Error: str
    FailedItemsCount: int
    ImportDataFormat: ImportDataFormat
    ImportedItemsCount: int
    JobId: str
    Name: str
    PreSignedUrl: str
    StartTimestamp: datetime
    Status: ImportJobStatusType
    ResponseMetadata: ResponseMetadata


class ImportJob(BaseValidatorModel):
    AddressListId: str
    CreatedTimestamp: datetime
    ImportDataFormat: ImportDataFormat
    JobId: str
    Name: str
    PreSignedUrl: str
    Status: ImportJobStatusType
    CompletedTimestamp: Optional[datetime] = None
    Error: Optional[str] = None
    FailedItemsCount: Optional[int] = None
    ImportedItemsCount: Optional[int] = None
    StartTimestamp: Optional[datetime] = None


class CreateIngressPointRequest(BaseValidatorModel):
    IngressPointName: str
    RuleSetId: str
    TrafficPolicyId: str
    Type: IngressPointTypeType
    ClientToken: Optional[str] = None
    IngressPointConfiguration: Optional[IngressPointConfiguration] = None
    Tags: Optional[List[Tag]] = None


class UpdateIngressPointRequest(BaseValidatorModel):
    IngressPointId: str
    IngressPointConfiguration: Optional[IngressPointConfiguration] = None
    IngressPointName: Optional[str] = None
    RuleSetId: Optional[str] = None
    StatusToUpdate: Optional[IngressPointStatusToUpdateType] = None
    TrafficPolicyId: Optional[str] = None


class Row(BaseValidatorModel):
    ArchivedMessageId: Optional[str] = None
    Cc: Optional[str] = None
    Date: Optional[str] = None
    Envelope: Optional[Envelope] = None
    From: Optional[str] = None
    HasAttachments: Optional[bool] = None
    InReplyTo: Optional[str] = None
    IngressPointId: Optional[str] = None
    MessageId: Optional[str] = None
    ReceivedHeaders: Optional[List[str]] = None
    ReceivedTimestamp: Optional[datetime] = None
    SenderHostname: Optional[str] = None
    SenderIpAddress: Optional[str] = None
    SourceArn: Optional[str] = None
    Subject: Optional[str] = None
    To: Optional[str] = None
    XMailer: Optional[str] = None
    XOriginalMailer: Optional[str] = None
    XPriority: Optional[str] = None


class ExportDestinationConfiguration(BaseValidatorModel):
    S3: Optional[S3ExportDestinationConfiguration] = None


class ExportSummary(BaseValidatorModel):
    ExportId: Optional[str] = None
    Status: Optional[ExportStatus] = None


class GetArchiveMessageContentResponse(BaseValidatorModel):
    Body: MessageBody
    ResponseMetadata: ResponseMetadata


class GetArchiveMessageResponse(BaseValidatorModel):
    Envelope: Envelope
    MessageDownloadLink: str
    Metadata: Metadata
    ResponseMetadata: ResponseMetadata


class SearchSummary(BaseValidatorModel):
    SearchId: Optional[str] = None
    Status: Optional[SearchStatus] = None


class GetRelayResponse(BaseValidatorModel):
    Authentication: RelayAuthenticationOutput
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    RelayArn: str
    RelayId: str
    RelayName: str
    ServerName: str
    ServerPort: int
    ResponseMetadata: ResponseMetadata


class IngressBooleanToEvaluateOutput(BaseValidatorModel):
    Analysis: Optional[IngressAnalysis] = None
    IsInAddressList: Optional[IngressIsInAddressListOutput] = None


class IngressIpv4ExpressionOutput(BaseValidatorModel):
    Evaluate: IngressIpToEvaluate
    Operator: IngressIpOperatorType
    Values: List[str]


class IngressIpv4Expression(BaseValidatorModel):
    Evaluate: IngressIpToEvaluate
    Operator: IngressIpOperatorType
    Values: List[str]

IngressIsInAddressListUnion = Union[IngressIsInAddressList, IngressIsInAddressListOutput]


class IngressPointAuthConfiguration(BaseValidatorModel):
    IngressPointPasswordConfiguration: Optional[IngressPointPasswordConfiguration] = None
    SecretArn: Optional[str] = None


class ListIngressPointsResponse(BaseValidatorModel):
    IngressPoints: List[IngressPoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IngressStringExpressionOutput(BaseValidatorModel):
    Evaluate: IngressStringToEvaluate
    Operator: IngressStringOperatorType
    Values: List[str]


class IngressStringExpression(BaseValidatorModel):
    Evaluate: IngressStringToEvaluate
    Operator: IngressStringOperatorType
    Values: List[str]


class IngressTlsProtocolExpression(BaseValidatorModel):
    Evaluate: IngressTlsProtocolToEvaluate
    Operator: IngressTlsProtocolOperatorType
    Value: IngressTlsProtocolAttributeType


class ListAddonInstancesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAddonSubscriptionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAddressListImportJobsRequestPaginate(BaseValidatorModel):
    AddressListId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAddressListsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListArchiveExportsRequestPaginate(BaseValidatorModel):
    ArchiveId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListArchiveSearchesRequestPaginate(BaseValidatorModel):
    ArchiveId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListArchivesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIngressPointsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersOfAddressListRequestPaginate(BaseValidatorModel):
    AddressListId: str
    Filter: Optional[AddressFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRelaysRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRuleSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrafficPoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersOfAddressListResponse(BaseValidatorModel):
    Addresses: List[SavedAddress]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRelaysResponse(BaseValidatorModel):
    Relays: List[Relay]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRuleSetsResponse(BaseValidatorModel):
    RuleSets: List[RuleSet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrafficPoliciesResponse(BaseValidatorModel):
    TrafficPolicies: List[TrafficPolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

RelayAuthenticationUnion = Union[RelayAuthentication, RelayAuthenticationOutput]

ReplaceRecipientActionUnion = Union[ReplaceRecipientAction, ReplaceRecipientActionOutput]


class RuleActionOutput(BaseValidatorModel):
    AddHeader: Optional[AddHeaderAction] = None
    Archive: Optional[ArchiveAction] = None
    DeliverToMailbox: Optional[DeliverToMailboxAction] = None
    DeliverToQBusiness: Optional[DeliverToQBusinessAction] = None
    Drop: Optional[Dict[str, Any]] = None
    Relay: Optional[RelayAction] = None
    ReplaceRecipient: Optional[ReplaceRecipientActionOutput] = None
    Send: Optional[SendAction] = None
    WriteToS3: Optional[S3Action] = None


class RuleBooleanToEvaluateOutput(BaseValidatorModel):
    Attribute: Optional[RuleBooleanEmailAttributeType] = None
    IsInAddressList: Optional[RuleIsInAddressListOutput] = None

RuleDmarcExpressionUnion = Union[RuleDmarcExpression, RuleDmarcExpressionOutput]


class RuleIpExpressionOutput(BaseValidatorModel):
    Evaluate: RuleIpToEvaluate
    Operator: RuleIpOperatorType
    Values: List[str]


class RuleIpExpression(BaseValidatorModel):
    Evaluate: RuleIpToEvaluate
    Operator: RuleIpOperatorType
    Values: List[str]

RuleIsInAddressListUnion = Union[RuleIsInAddressList, RuleIsInAddressListOutput]


class RuleNumberExpression(BaseValidatorModel):
    Evaluate: RuleNumberToEvaluate
    Operator: RuleNumberOperatorType
    Value: float


class RuleStringExpressionOutput(BaseValidatorModel):
    Evaluate: RuleStringToEvaluate
    Operator: RuleStringOperatorType
    Values: List[str]


class RuleStringExpression(BaseValidatorModel):
    Evaluate: RuleStringToEvaluate
    Operator: RuleStringOperatorType
    Values: List[str]


class RuleVerdictExpressionOutput(BaseValidatorModel):
    Evaluate: RuleVerdictToEvaluate
    Operator: RuleVerdictOperatorType
    Values: List[RuleVerdictType]


class RuleVerdictExpression(BaseValidatorModel):
    Evaluate: RuleVerdictToEvaluate
    Operator: RuleVerdictOperatorType
    Values: List[RuleVerdictType]


class ArchiveFilterConditionOutput(BaseValidatorModel):
    BooleanExpression: Optional[ArchiveBooleanExpression] = None
    StringExpression: Optional[ArchiveStringExpressionOutput] = None


class ArchiveFilterCondition(BaseValidatorModel):
    BooleanExpression: Optional[ArchiveBooleanExpression] = None
    StringExpression: Optional[ArchiveStringExpression] = None


class ListAddressListImportJobsResponse(BaseValidatorModel):
    ImportJobs: List[ImportJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetArchiveSearchResultsResponse(BaseValidatorModel):
    Rows: List[Row]
    ResponseMetadata: ResponseMetadata


class ListArchiveExportsResponse(BaseValidatorModel):
    Exports: List[ExportSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListArchiveSearchesResponse(BaseValidatorModel):
    Searches: List[SearchSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IngressBooleanExpressionOutput(BaseValidatorModel):
    Evaluate: IngressBooleanToEvaluateOutput
    Operator: IngressBooleanOperatorType

IngressIpv4ExpressionUnion = Union[IngressIpv4Expression, IngressIpv4ExpressionOutput]


class IngressBooleanToEvaluate(BaseValidatorModel):
    Analysis: Optional[IngressAnalysis] = None
    IsInAddressList: Optional[IngressIsInAddressListUnion] = None


class GetIngressPointResponse(BaseValidatorModel):
    ARecord: str
    CreatedTimestamp: datetime
    IngressPointArn: str
    IngressPointAuthConfiguration: IngressPointAuthConfiguration
    IngressPointId: str
    IngressPointName: str
    LastUpdatedTimestamp: datetime
    RuleSetId: str
    Status: IngressPointStatusType
    TrafficPolicyId: str
    Type: IngressPointTypeType
    ResponseMetadata: ResponseMetadata

IngressStringExpressionUnion = Union[IngressStringExpression, IngressStringExpressionOutput]


class CreateRelayRequest(BaseValidatorModel):
    Authentication: RelayAuthenticationUnion
    RelayName: str
    ServerName: str
    ServerPort: int
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateRelayRequest(BaseValidatorModel):
    RelayId: str
    Authentication: Optional[RelayAuthenticationUnion] = None
    RelayName: Optional[str] = None
    ServerName: Optional[str] = None
    ServerPort: Optional[int] = None


class RuleAction(BaseValidatorModel):
    AddHeader: Optional[AddHeaderAction] = None
    Archive: Optional[ArchiveAction] = None
    DeliverToMailbox: Optional[DeliverToMailboxAction] = None
    DeliverToQBusiness: Optional[DeliverToQBusinessAction] = None
    Drop: Optional[Dict[str, Any]] = None
    Relay: Optional[RelayAction] = None
    ReplaceRecipient: Optional[ReplaceRecipientActionUnion] = None
    Send: Optional[SendAction] = None
    WriteToS3: Optional[S3Action] = None


class RuleBooleanExpressionOutput(BaseValidatorModel):
    Evaluate: RuleBooleanToEvaluateOutput
    Operator: RuleBooleanOperatorType

RuleIpExpressionUnion = Union[RuleIpExpression, RuleIpExpressionOutput]


class RuleBooleanToEvaluate(BaseValidatorModel):
    Attribute: Optional[RuleBooleanEmailAttributeType] = None
    IsInAddressList: Optional[RuleIsInAddressListUnion] = None

RuleStringExpressionUnion = Union[RuleStringExpression, RuleStringExpressionOutput]

RuleVerdictExpressionUnion = Union[RuleVerdictExpression, RuleVerdictExpressionOutput]


class ArchiveFiltersOutput(BaseValidatorModel):
    Include: Optional[List[ArchiveFilterConditionOutput]] = None
    Unless: Optional[List[ArchiveFilterConditionOutput]] = None


class ArchiveFilters(BaseValidatorModel):
    Include: Optional[List[ArchiveFilterCondition]] = None
    Unless: Optional[List[ArchiveFilterCondition]] = None


class PolicyConditionOutput(BaseValidatorModel):
    BooleanExpression: Optional[IngressBooleanExpressionOutput] = None
    IpExpression: Optional[IngressIpv4ExpressionOutput] = None
    StringExpression: Optional[IngressStringExpressionOutput] = None
    TlsExpression: Optional[IngressTlsProtocolExpression] = None

IngressBooleanToEvaluateUnion = Union[IngressBooleanToEvaluate, IngressBooleanToEvaluateOutput]

RuleActionUnion = Union[RuleAction, RuleActionOutput]


class RuleConditionOutput(BaseValidatorModel):
    BooleanExpression: Optional[RuleBooleanExpressionOutput] = None
    DmarcExpression: Optional[RuleDmarcExpressionOutput] = None
    IpExpression: Optional[RuleIpExpressionOutput] = None
    NumberExpression: Optional[RuleNumberExpression] = None
    StringExpression: Optional[RuleStringExpressionOutput] = None
    VerdictExpression: Optional[RuleVerdictExpressionOutput] = None

RuleBooleanToEvaluateUnion = Union[RuleBooleanToEvaluate, RuleBooleanToEvaluateOutput]


class GetArchiveExportResponse(BaseValidatorModel):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfiguration
    Filters: ArchiveFiltersOutput
    FromTimestamp: datetime
    MaxResults: int
    Status: ExportStatus
    ToTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetArchiveSearchResponse(BaseValidatorModel):
    ArchiveId: str
    Filters: ArchiveFiltersOutput
    FromTimestamp: datetime
    MaxResults: int
    Status: SearchStatus
    ToTimestamp: datetime
    ResponseMetadata: ResponseMetadata

ArchiveFiltersUnion = Union[ArchiveFilters, ArchiveFiltersOutput]


class PolicyStatementOutput(BaseValidatorModel):
    Action: AcceptActionType
    Conditions: List[PolicyConditionOutput]


class IngressBooleanExpression(BaseValidatorModel):
    Evaluate: IngressBooleanToEvaluateUnion
    Operator: IngressBooleanOperatorType


class RuleOutput(BaseValidatorModel):
    Actions: List[RuleActionOutput]
    Conditions: Optional[List[RuleConditionOutput]] = None
    Name: Optional[str] = None
    Unless: Optional[List[RuleConditionOutput]] = None


class RuleBooleanExpression(BaseValidatorModel):
    Evaluate: RuleBooleanToEvaluateUnion
    Operator: RuleBooleanOperatorType


class StartArchiveExportRequest(BaseValidatorModel):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfiguration
    FromTimestamp: Timestamp
    ToTimestamp: Timestamp
    Filters: Optional[ArchiveFiltersUnion] = None
    IncludeMetadata: Optional[bool] = None
    MaxResults: Optional[int] = None


class StartArchiveSearchRequest(BaseValidatorModel):
    ArchiveId: str
    FromTimestamp: Timestamp
    MaxResults: int
    ToTimestamp: Timestamp
    Filters: Optional[ArchiveFiltersUnion] = None


class GetTrafficPolicyResponse(BaseValidatorModel):
    CreatedTimestamp: datetime
    DefaultAction: AcceptActionType
    LastUpdatedTimestamp: datetime
    MaxMessageSizeBytes: int
    PolicyStatements: List[PolicyStatementOutput]
    TrafficPolicyArn: str
    TrafficPolicyId: str
    TrafficPolicyName: str
    ResponseMetadata: ResponseMetadata

IngressBooleanExpressionUnion = Union[IngressBooleanExpression, IngressBooleanExpressionOutput]


class GetRuleSetResponse(BaseValidatorModel):
    CreatedDate: datetime
    LastModificationDate: datetime
    RuleSetArn: str
    RuleSetId: str
    RuleSetName: str
    Rules: List[RuleOutput]
    ResponseMetadata: ResponseMetadata

RuleBooleanExpressionUnion = Union[RuleBooleanExpression, RuleBooleanExpressionOutput]


class PolicyCondition(BaseValidatorModel):
    BooleanExpression: Optional[IngressBooleanExpressionUnion] = None
    IpExpression: Optional[IngressIpv4ExpressionUnion] = None
    StringExpression: Optional[IngressStringExpressionUnion] = None
    TlsExpression: Optional[IngressTlsProtocolExpression] = None


class RuleCondition(BaseValidatorModel):
    BooleanExpression: Optional[RuleBooleanExpressionUnion] = None
    DmarcExpression: Optional[RuleDmarcExpressionUnion] = None
    IpExpression: Optional[RuleIpExpressionUnion] = None
    NumberExpression: Optional[RuleNumberExpression] = None
    StringExpression: Optional[RuleStringExpressionUnion] = None
    VerdictExpression: Optional[RuleVerdictExpressionUnion] = None

PolicyConditionUnion = Union[PolicyCondition, PolicyConditionOutput]

RuleConditionUnion = Union[RuleCondition, RuleConditionOutput]


class PolicyStatement(BaseValidatorModel):
    Action: AcceptActionType
    Conditions: List[PolicyConditionUnion]


class Rule(BaseValidatorModel):
    Actions: List[RuleActionUnion]
    Conditions: Optional[List[RuleConditionUnion]] = None
    Name: Optional[str] = None
    Unless: Optional[List[RuleConditionUnion]] = None

PolicyStatementUnion = Union[PolicyStatement, PolicyStatementOutput]

RuleUnion = Union[Rule, RuleOutput]


class CreateTrafficPolicyRequest(BaseValidatorModel):
    DefaultAction: AcceptActionType
    PolicyStatements: List[PolicyStatementUnion]
    TrafficPolicyName: str
    ClientToken: Optional[str] = None
    MaxMessageSizeBytes: Optional[int] = None
    Tags: Optional[List[Tag]] = None


class UpdateTrafficPolicyRequest(BaseValidatorModel):
    TrafficPolicyId: str
    DefaultAction: Optional[AcceptActionType] = None
    MaxMessageSizeBytes: Optional[int] = None
    PolicyStatements: Optional[List[PolicyStatementUnion]] = None
    TrafficPolicyName: Optional[str] = None


class CreateRuleSetRequest(BaseValidatorModel):
    RuleSetName: str
    Rules: List[RuleUnion]
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateRuleSetRequest(BaseValidatorModel):
    RuleSetId: str
    RuleSetName: Optional[str] = None
    Rules: Optional[List[RuleUnion]] = None
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
from aws_resource_validator.pydantic_models.mailmanager_constants import *

class AddHeaderActionTypeDef(BaseValidatorModel):
    HeaderName: str
    HeaderValue: str


class AddonInstanceTypeDef(BaseValidatorModel):
    AddonInstanceArn: Optional[str] = None
    AddonInstanceId: Optional[str] = None
    AddonName: Optional[str] = None
    AddonSubscriptionId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class AddonSubscriptionTypeDef(BaseValidatorModel):
    AddonName: Optional[str] = None
    AddonSubscriptionArn: Optional[str] = None
    AddonSubscriptionId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None


class AddressFilterTypeDef(BaseValidatorModel):
    AddressPrefix: Optional[str] = None


class AddressListTypeDef(BaseValidatorModel):
    AddressListArn: str
    AddressListId: str
    AddressListName: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime


class AnalysisTypeDef(BaseValidatorModel):
    Analyzer: str
    ResultField: str


class ArchiveActionTypeDef(BaseValidatorModel):
    TargetArchive: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None


class ArchiveBooleanToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["HAS_ATTACHMENTS"]] = None


class ArchiveRetentionTypeDef(BaseValidatorModel):
    RetentionPeriod: Optional[RetentionPeriodType] = None


class ArchiveStringToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[ArchiveStringEmailAttributeType] = None


class ArchiveTypeDef(BaseValidatorModel):
    ArchiveId: str
    ArchiveName: Optional[str] = None
    ArchiveState: Optional[ArchiveStateType] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ImportDataFormatTypeDef(BaseValidatorModel):
    ImportDataType: ImportDataTypeType


class IngressPointConfigurationTypeDef(BaseValidatorModel):
    SecretArn: Optional[str] = None
    SmtpPassword: Optional[str] = None


class DeleteAddonInstanceRequestTypeDef(BaseValidatorModel):
    AddonInstanceId: str


class DeleteAddonSubscriptionRequestTypeDef(BaseValidatorModel):
    AddonSubscriptionId: str


class DeleteAddressListRequestTypeDef(BaseValidatorModel):
    AddressListId: str


class DeleteArchiveRequestTypeDef(BaseValidatorModel):
    ArchiveId: str


class DeleteIngressPointRequestTypeDef(BaseValidatorModel):
    IngressPointId: str


class DeleteRelayRequestTypeDef(BaseValidatorModel):
    RelayId: str


class DeleteRuleSetRequestTypeDef(BaseValidatorModel):
    RuleSetId: str


class DeleteTrafficPolicyRequestTypeDef(BaseValidatorModel):
    TrafficPolicyId: str


class DeliverToMailboxActionTypeDef(BaseValidatorModel):
    MailboxArn: str
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None


class DeliverToQBusinessActionTypeDef(BaseValidatorModel):
    ApplicationId: str
    IndexId: str
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None


class DeregisterMemberFromAddressListRequestTypeDef(BaseValidatorModel):
    Address: str
    AddressListId: str


class EnvelopeTypeDef(BaseValidatorModel):
    From: Optional[str] = None
    Helo: Optional[str] = None
    To: Optional[List[str]] = None


class S3ExportDestinationConfigurationTypeDef(BaseValidatorModel):
    S3Location: Optional[str] = None


class ExportStatusTypeDef(BaseValidatorModel):
    CompletionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    State: Optional[ExportStateType] = None
    SubmissionTimestamp: Optional[datetime] = None


class GetAddonInstanceRequestTypeDef(BaseValidatorModel):
    AddonInstanceId: str


class GetAddonSubscriptionRequestTypeDef(BaseValidatorModel):
    AddonSubscriptionId: str


class GetAddressListImportJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class GetAddressListRequestTypeDef(BaseValidatorModel):
    AddressListId: str


class GetArchiveExportRequestTypeDef(BaseValidatorModel):
    ExportId: str


class GetArchiveMessageContentRequestTypeDef(BaseValidatorModel):
    ArchivedMessageId: str


class GetArchiveMessageRequestTypeDef(BaseValidatorModel):
    ArchivedMessageId: str


class MetadataTypeDef(BaseValidatorModel):
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


class GetArchiveRequestTypeDef(BaseValidatorModel):
    ArchiveId: str


class GetArchiveSearchRequestTypeDef(BaseValidatorModel):
    SearchId: str


class SearchStatusTypeDef(BaseValidatorModel):
    CompletionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    State: Optional[SearchStateType] = None
    SubmissionTimestamp: Optional[datetime] = None


class GetArchiveSearchResultsRequestTypeDef(BaseValidatorModel):
    SearchId: str


class GetIngressPointRequestTypeDef(BaseValidatorModel):
    IngressPointId: str


class GetMemberOfAddressListRequestTypeDef(BaseValidatorModel):
    Address: str
    AddressListId: str


class GetRelayRequestTypeDef(BaseValidatorModel):
    RelayId: str


class RelayAuthenticationOutputTypeDef(BaseValidatorModel):
    NoAuthentication: Optional[Dict[str, Any]] = None
    SecretArn: Optional[str] = None


class GetRuleSetRequestTypeDef(BaseValidatorModel):
    RuleSetId: str


class GetTrafficPolicyRequestTypeDef(BaseValidatorModel):
    TrafficPolicyId: str


class IngressAnalysisTypeDef(BaseValidatorModel):
    Analyzer: str
    ResultField: str


class IngressIsInAddressListOutputTypeDef(BaseValidatorModel):
    AddressLists: List[str]
    Attribute: Literal["RECIPIENT"]


class IngressIpToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["SENDER_IP"]] = None


class IngressIsInAddressListTypeDef(BaseValidatorModel):
    AddressLists: Sequence[str]
    Attribute: Literal["RECIPIENT"]


class IngressPointPasswordConfigurationTypeDef(BaseValidatorModel):
    PreviousSmtpPasswordExpiryTimestamp: Optional[datetime] = None
    PreviousSmtpPasswordVersion: Optional[str] = None
    SmtpPasswordVersion: Optional[str] = None


class IngressStringToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["RECIPIENT"]] = None


class IngressTlsProtocolToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["TLS_PROTOCOL"]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAddonInstancesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListAddonSubscriptionsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListAddressListImportJobsRequestTypeDef(BaseValidatorModel):
    AddressListId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListAddressListsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListArchiveExportsRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListArchiveSearchesRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListArchivesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListIngressPointsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class SavedAddressTypeDef(BaseValidatorModel):
    Address: str
    CreatedTimestamp: datetime


class ListRelaysRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class RelayTypeDef(BaseValidatorModel):
    LastModifiedTimestamp: Optional[datetime] = None
    RelayId: Optional[str] = None
    RelayName: Optional[str] = None


class ListRuleSetsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class RuleSetTypeDef(BaseValidatorModel):
    LastModificationDate: Optional[datetime] = None
    RuleSetId: Optional[str] = None
    RuleSetName: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListTrafficPoliciesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class TrafficPolicyTypeDef(BaseValidatorModel):
    DefaultAction: AcceptActionType
    TrafficPolicyId: str
    TrafficPolicyName: str


class RegisterMemberToAddressListRequestTypeDef(BaseValidatorModel):
    Address: str
    AddressListId: str


class RelayActionTypeDef(BaseValidatorModel):
    Relay: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None
    MailFrom: Optional[MailFromType] = None


class RelayAuthenticationTypeDef(BaseValidatorModel):
    NoAuthentication: Optional[Mapping[str, Any]] = None
    SecretArn: Optional[str] = None


class ReplaceRecipientActionOutputTypeDef(BaseValidatorModel):
    ReplaceWith: Optional[List[str]] = None


class ReplaceRecipientActionTypeDef(BaseValidatorModel):
    ReplaceWith: Optional[Sequence[str]] = None


class S3ActionTypeDef(BaseValidatorModel):
    RoleArn: str
    S3Bucket: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None
    S3Prefix: Optional[str] = None
    S3SseKmsKeyId: Optional[str] = None


class SendActionTypeDef(BaseValidatorModel):
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None


class RuleIsInAddressListOutputTypeDef(BaseValidatorModel):
    AddressLists: List[str]
    Attribute: RuleAddressListEmailAttributeType


class RuleDmarcExpressionOutputTypeDef(BaseValidatorModel):
    Operator: RuleDmarcOperatorType
    Values: List[RuleDmarcPolicyType]


class RuleDmarcExpressionTypeDef(BaseValidatorModel):
    Operator: RuleDmarcOperatorType
    Values: Sequence[RuleDmarcPolicyType]


class RuleIpToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["SOURCE_IP"]] = None


class RuleIsInAddressListTypeDef(BaseValidatorModel):
    AddressLists: Sequence[str]
    Attribute: RuleAddressListEmailAttributeType


class RuleNumberToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["MESSAGE_SIZE"]] = None


class RuleStringToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[RuleStringEmailAttributeType] = None
    MimeHeaderAttribute: Optional[str] = None


class StartAddressListImportJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopAddressListImportJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopArchiveExportRequestTypeDef(BaseValidatorModel):
    ExportId: str


class StopArchiveSearchRequestTypeDef(BaseValidatorModel):
    SearchId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class ListMembersOfAddressListRequestTypeDef(BaseValidatorModel):
    AddressListId: str
    Filter: Optional[AddressFilterTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class RuleVerdictToEvaluateTypeDef(BaseValidatorModel):
    Analysis: Optional[AnalysisTypeDef] = None
    Attribute: Optional[RuleVerdictAttributeType] = None


class ArchiveBooleanExpressionTypeDef(BaseValidatorModel):
    Evaluate: ArchiveBooleanToEvaluateTypeDef
    Operator: ArchiveBooleanOperatorType


class UpdateArchiveRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    ArchiveName: Optional[str] = None
    Retention: Optional[ArchiveRetentionTypeDef] = None


class ArchiveStringExpressionOutputTypeDef(BaseValidatorModel):
    Evaluate: ArchiveStringToEvaluateTypeDef
    Operator: Literal["CONTAINS"]
    Values: List[str]


class ArchiveStringExpressionTypeDef(BaseValidatorModel):
    Evaluate: ArchiveStringToEvaluateTypeDef
    Operator: Literal["CONTAINS"]
    Values: Sequence[str]


class CreateAddonInstanceRequestTypeDef(BaseValidatorModel):
    AddonSubscriptionId: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateAddonSubscriptionRequestTypeDef(BaseValidatorModel):
    AddonName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateAddressListRequestTypeDef(BaseValidatorModel):
    AddressListName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateArchiveRequestTypeDef(BaseValidatorModel):
    ArchiveName: str
    ClientToken: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Retention: Optional[ArchiveRetentionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateAddonInstanceResponseTypeDef(BaseValidatorModel):
    AddonInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAddonSubscriptionResponseTypeDef(BaseValidatorModel):
    AddonSubscriptionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAddressListImportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    PreSignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAddressListResponseTypeDef(BaseValidatorModel):
    AddressListId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateArchiveResponseTypeDef(BaseValidatorModel):
    ArchiveId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIngressPointResponseTypeDef(BaseValidatorModel):
    IngressPointId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRelayResponseTypeDef(BaseValidatorModel):
    RelayId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRuleSetResponseTypeDef(BaseValidatorModel):
    RuleSetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTrafficPolicyResponseTypeDef(BaseValidatorModel):
    TrafficPolicyId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAddonInstanceResponseTypeDef(BaseValidatorModel):
    AddonInstanceArn: str
    AddonName: str
    AddonSubscriptionId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetAddonSubscriptionResponseTypeDef(BaseValidatorModel):
    AddonName: str
    AddonSubscriptionArn: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetAddressListResponseTypeDef(BaseValidatorModel):
    AddressListArn: str
    AddressListId: str
    AddressListName: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetArchiveResponseTypeDef(BaseValidatorModel):
    ArchiveArn: str
    ArchiveId: str
    ArchiveName: str
    ArchiveState: ArchiveStateType
    CreatedTimestamp: datetime
    KmsKeyArn: str
    LastUpdatedTimestamp: datetime
    Retention: ArchiveRetentionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMemberOfAddressListResponseTypeDef(BaseValidatorModel):
    Address: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListAddonInstancesResponseTypeDef(BaseValidatorModel):
    AddonInstances: List[AddonInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAddonSubscriptionsResponseTypeDef(BaseValidatorModel):
    AddonSubscriptions: List[AddonSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAddressListsResponseTypeDef(BaseValidatorModel):
    AddressLists: List[AddressListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListArchivesResponseTypeDef(BaseValidatorModel):
    Archives: List[ArchiveTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartArchiveExportResponseTypeDef(BaseValidatorModel):
    ExportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartArchiveSearchResponseTypeDef(BaseValidatorModel):
    SearchId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAddressListImportJobRequestTypeDef(BaseValidatorModel):
    AddressListId: str
    ImportDataFormat: ImportDataFormatTypeDef
    Name: str
    ClientToken: Optional[str] = None


class GetAddressListImportJobResponseTypeDef(BaseValidatorModel):
    AddressListId: str
    CompletedTimestamp: datetime
    CreatedTimestamp: datetime
    Error: str
    FailedItemsCount: int
    ImportDataFormat: ImportDataFormatTypeDef
    ImportedItemsCount: int
    JobId: str
    Name: str
    PreSignedUrl: str
    StartTimestamp: datetime
    Status: ImportJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ImportJobTypeDef(BaseValidatorModel):
    AddressListId: str
    CreatedTimestamp: datetime
    ImportDataFormat: ImportDataFormatTypeDef
    JobId: str
    Name: str
    PreSignedUrl: str
    Status: ImportJobStatusType
    CompletedTimestamp: Optional[datetime] = None
    Error: Optional[str] = None
    FailedItemsCount: Optional[int] = None
    ImportedItemsCount: Optional[int] = None
    StartTimestamp: Optional[datetime] = None


class UpdateIngressPointRequestTypeDef(BaseValidatorModel):
    IngressPointId: str
    IngressPointConfiguration: Optional[IngressPointConfigurationTypeDef] = None
    IngressPointName: Optional[str] = None
    RuleSetId: Optional[str] = None
    StatusToUpdate: Optional[IngressPointStatusToUpdateType] = None
    TrafficPolicyId: Optional[str] = None


class RowTypeDef(BaseValidatorModel):
    ArchivedMessageId: Optional[str] = None
    Cc: Optional[str] = None
    Date: Optional[str] = None
    Envelope: Optional[EnvelopeTypeDef] = None
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


class ExportDestinationConfigurationTypeDef(BaseValidatorModel):
    S3: Optional[S3ExportDestinationConfigurationTypeDef] = None


class ExportSummaryTypeDef(BaseValidatorModel):
    ExportId: Optional[str] = None
    Status: Optional[ExportStatusTypeDef] = None


class MessageBodyTypeDef(BaseValidatorModel):
    pass


class GetArchiveMessageContentResponseTypeDef(BaseValidatorModel):
    Body: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetArchiveMessageResponseTypeDef(BaseValidatorModel):
    Envelope: EnvelopeTypeDef
    MessageDownloadLink: str
    Metadata: MetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SearchSummaryTypeDef(BaseValidatorModel):
    SearchId: Optional[str] = None
    Status: Optional[SearchStatusTypeDef] = None


class GetRelayResponseTypeDef(BaseValidatorModel):
    Authentication: RelayAuthenticationOutputTypeDef
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    RelayArn: str
    RelayId: str
    RelayName: str
    ServerName: str
    ServerPort: int
    ResponseMetadata: ResponseMetadataTypeDef


class IngressBooleanToEvaluateOutputTypeDef(BaseValidatorModel):
    Analysis: Optional[IngressAnalysisTypeDef] = None
    IsInAddressList: Optional[IngressIsInAddressListOutputTypeDef] = None


class IngressIpv4ExpressionOutputTypeDef(BaseValidatorModel):
    Evaluate: IngressIpToEvaluateTypeDef
    Operator: IngressIpOperatorType
    Values: List[str]


class IngressIpv4ExpressionTypeDef(BaseValidatorModel):
    Evaluate: IngressIpToEvaluateTypeDef
    Operator: IngressIpOperatorType
    Values: Sequence[str]


class IngressPointAuthConfigurationTypeDef(BaseValidatorModel):
    IngressPointPasswordConfiguration: Optional[IngressPointPasswordConfigurationTypeDef] = None
    SecretArn: Optional[str] = None


class IngressPointTypeDef(BaseValidatorModel):
    pass


class ListIngressPointsResponseTypeDef(BaseValidatorModel):
    IngressPoints: List[IngressPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IngressStringExpressionOutputTypeDef(BaseValidatorModel):
    Evaluate: IngressStringToEvaluateTypeDef
    Operator: IngressStringOperatorType
    Values: List[str]


class IngressStringExpressionTypeDef(BaseValidatorModel):
    Evaluate: IngressStringToEvaluateTypeDef
    Operator: IngressStringOperatorType
    Values: Sequence[str]


class IngressTlsProtocolExpressionTypeDef(BaseValidatorModel):
    Evaluate: IngressTlsProtocolToEvaluateTypeDef
    Operator: IngressTlsProtocolOperatorType
    Value: IngressTlsProtocolAttributeType


class ListAddonInstancesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAddonSubscriptionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAddressListImportJobsRequestPaginateTypeDef(BaseValidatorModel):
    AddressListId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAddressListsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListArchiveExportsRequestPaginateTypeDef(BaseValidatorModel):
    ArchiveId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListArchiveSearchesRequestPaginateTypeDef(BaseValidatorModel):
    ArchiveId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListArchivesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIngressPointsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMembersOfAddressListRequestPaginateTypeDef(BaseValidatorModel):
    AddressListId: str
    Filter: Optional[AddressFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRelaysRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRuleSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrafficPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMembersOfAddressListResponseTypeDef(BaseValidatorModel):
    Addresses: List[SavedAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRelaysResponseTypeDef(BaseValidatorModel):
    Relays: List[RelayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRuleSetsResponseTypeDef(BaseValidatorModel):
    RuleSets: List[RuleSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTrafficPoliciesResponseTypeDef(BaseValidatorModel):
    TrafficPolicies: List[TrafficPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RuleActionOutputTypeDef(BaseValidatorModel):
    AddHeader: Optional[AddHeaderActionTypeDef] = None
    Archive: Optional[ArchiveActionTypeDef] = None
    DeliverToMailbox: Optional[DeliverToMailboxActionTypeDef] = None
    DeliverToQBusiness: Optional[DeliverToQBusinessActionTypeDef] = None
    Drop: Optional[Dict[str, Any]] = None
    Relay: Optional[RelayActionTypeDef] = None
    ReplaceRecipient: Optional[ReplaceRecipientActionOutputTypeDef] = None
    Send: Optional[SendActionTypeDef] = None
    WriteToS3: Optional[S3ActionTypeDef] = None


class RuleBooleanToEvaluateOutputTypeDef(BaseValidatorModel):
    Attribute: Optional[RuleBooleanEmailAttributeType] = None
    IsInAddressList: Optional[RuleIsInAddressListOutputTypeDef] = None


class RuleIpExpressionOutputTypeDef(BaseValidatorModel):
    Evaluate: RuleIpToEvaluateTypeDef
    Operator: RuleIpOperatorType
    Values: List[str]


class RuleIpExpressionTypeDef(BaseValidatorModel):
    Evaluate: RuleIpToEvaluateTypeDef
    Operator: RuleIpOperatorType
    Values: Sequence[str]


class RuleNumberExpressionTypeDef(BaseValidatorModel):
    Evaluate: RuleNumberToEvaluateTypeDef
    Operator: RuleNumberOperatorType
    Value: float


class RuleStringExpressionOutputTypeDef(BaseValidatorModel):
    Evaluate: RuleStringToEvaluateTypeDef
    Operator: RuleStringOperatorType
    Values: List[str]


class RuleStringExpressionTypeDef(BaseValidatorModel):
    Evaluate: RuleStringToEvaluateTypeDef
    Operator: RuleStringOperatorType
    Values: Sequence[str]


class RuleVerdictExpressionOutputTypeDef(BaseValidatorModel):
    Evaluate: RuleVerdictToEvaluateTypeDef
    Operator: RuleVerdictOperatorType
    Values: List[RuleVerdictType]


class RuleVerdictExpressionTypeDef(BaseValidatorModel):
    Evaluate: RuleVerdictToEvaluateTypeDef
    Operator: RuleVerdictOperatorType
    Values: Sequence[RuleVerdictType]


class ArchiveFilterConditionOutputTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[ArchiveBooleanExpressionTypeDef] = None
    StringExpression: Optional[ArchiveStringExpressionOutputTypeDef] = None


class ArchiveFilterConditionTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[ArchiveBooleanExpressionTypeDef] = None
    StringExpression: Optional[ArchiveStringExpressionTypeDef] = None


class ListAddressListImportJobsResponseTypeDef(BaseValidatorModel):
    ImportJobs: List[ImportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetArchiveSearchResultsResponseTypeDef(BaseValidatorModel):
    Rows: List[RowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListArchiveExportsResponseTypeDef(BaseValidatorModel):
    Exports: List[ExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListArchiveSearchesResponseTypeDef(BaseValidatorModel):
    Searches: List[SearchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IngressBooleanExpressionOutputTypeDef(BaseValidatorModel):
    Evaluate: IngressBooleanToEvaluateOutputTypeDef
    Operator: IngressBooleanOperatorType


class IngressIsInAddressListUnionTypeDef(BaseValidatorModel):
    pass


class IngressBooleanToEvaluateTypeDef(BaseValidatorModel):
    Analysis: Optional[IngressAnalysisTypeDef] = None
    IsInAddressList: Optional[IngressIsInAddressListUnionTypeDef] = None


class RelayAuthenticationUnionTypeDef(BaseValidatorModel):
    pass


class CreateRelayRequestTypeDef(BaseValidatorModel):
    Authentication: RelayAuthenticationUnionTypeDef
    RelayName: str
    ServerName: str
    ServerPort: int
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateRelayRequestTypeDef(BaseValidatorModel):
    RelayId: str
    Authentication: Optional[RelayAuthenticationUnionTypeDef] = None
    RelayName: Optional[str] = None
    ServerName: Optional[str] = None
    ServerPort: Optional[int] = None


class ReplaceRecipientActionUnionTypeDef(BaseValidatorModel):
    pass


class RuleActionTypeDef(BaseValidatorModel):
    AddHeader: Optional[AddHeaderActionTypeDef] = None
    Archive: Optional[ArchiveActionTypeDef] = None
    DeliverToMailbox: Optional[DeliverToMailboxActionTypeDef] = None
    DeliverToQBusiness: Optional[DeliverToQBusinessActionTypeDef] = None
    Drop: Optional[Mapping[str, Any]] = None
    Relay: Optional[RelayActionTypeDef] = None
    ReplaceRecipient: Optional[ReplaceRecipientActionUnionTypeDef] = None
    Send: Optional[SendActionTypeDef] = None
    WriteToS3: Optional[S3ActionTypeDef] = None


class RuleBooleanExpressionOutputTypeDef(BaseValidatorModel):
    Evaluate: RuleBooleanToEvaluateOutputTypeDef
    Operator: RuleBooleanOperatorType


class RuleIsInAddressListUnionTypeDef(BaseValidatorModel):
    pass


class RuleBooleanToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[RuleBooleanEmailAttributeType] = None
    IsInAddressList: Optional[RuleIsInAddressListUnionTypeDef] = None


class ArchiveFiltersOutputTypeDef(BaseValidatorModel):
    Include: Optional[List[ArchiveFilterConditionOutputTypeDef]] = None
    Unless: Optional[List[ArchiveFilterConditionOutputTypeDef]] = None


class ArchiveFiltersTypeDef(BaseValidatorModel):
    Include: Optional[Sequence[ArchiveFilterConditionTypeDef]] = None
    Unless: Optional[Sequence[ArchiveFilterConditionTypeDef]] = None


class PolicyConditionOutputTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[IngressBooleanExpressionOutputTypeDef] = None
    IpExpression: Optional[IngressIpv4ExpressionOutputTypeDef] = None
    StringExpression: Optional[IngressStringExpressionOutputTypeDef] = None
    TlsExpression: Optional[IngressTlsProtocolExpressionTypeDef] = None


class RuleConditionOutputTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[RuleBooleanExpressionOutputTypeDef] = None
    DmarcExpression: Optional[RuleDmarcExpressionOutputTypeDef] = None
    IpExpression: Optional[RuleIpExpressionOutputTypeDef] = None
    NumberExpression: Optional[RuleNumberExpressionTypeDef] = None
    StringExpression: Optional[RuleStringExpressionOutputTypeDef] = None
    VerdictExpression: Optional[RuleVerdictExpressionOutputTypeDef] = None


class GetArchiveExportResponseTypeDef(BaseValidatorModel):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    Filters: ArchiveFiltersOutputTypeDef
    FromTimestamp: datetime
    MaxResults: int
    Status: ExportStatusTypeDef
    ToTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetArchiveSearchResponseTypeDef(BaseValidatorModel):
    ArchiveId: str
    Filters: ArchiveFiltersOutputTypeDef
    FromTimestamp: datetime
    MaxResults: int
    Status: SearchStatusTypeDef
    ToTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PolicyStatementOutputTypeDef(BaseValidatorModel):
    Action: AcceptActionType
    Conditions: List[PolicyConditionOutputTypeDef]


class IngressBooleanToEvaluateUnionTypeDef(BaseValidatorModel):
    pass


class IngressBooleanExpressionTypeDef(BaseValidatorModel):
    Evaluate: IngressBooleanToEvaluateUnionTypeDef
    Operator: IngressBooleanOperatorType


class RuleOutputTypeDef(BaseValidatorModel):
    Actions: List[RuleActionOutputTypeDef]
    Conditions: Optional[List[RuleConditionOutputTypeDef]] = None
    Name: Optional[str] = None
    Unless: Optional[List[RuleConditionOutputTypeDef]] = None


class RuleBooleanToEvaluateUnionTypeDef(BaseValidatorModel):
    pass


class RuleBooleanExpressionTypeDef(BaseValidatorModel):
    Evaluate: RuleBooleanToEvaluateUnionTypeDef
    Operator: RuleBooleanOperatorType


class TimestampTypeDef(BaseValidatorModel):
    pass


class ArchiveFiltersUnionTypeDef(BaseValidatorModel):
    pass


class StartArchiveExportRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    FromTimestamp: TimestampTypeDef
    ToTimestamp: TimestampTypeDef
    Filters: Optional[ArchiveFiltersUnionTypeDef] = None
    IncludeMetadata: Optional[bool] = None
    MaxResults: Optional[int] = None


class StartArchiveSearchRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    FromTimestamp: TimestampTypeDef
    MaxResults: int
    ToTimestamp: TimestampTypeDef
    Filters: Optional[ArchiveFiltersUnionTypeDef] = None


class GetTrafficPolicyResponseTypeDef(BaseValidatorModel):
    CreatedTimestamp: datetime
    DefaultAction: AcceptActionType
    LastUpdatedTimestamp: datetime
    MaxMessageSizeBytes: int
    PolicyStatements: List[PolicyStatementOutputTypeDef]
    TrafficPolicyArn: str
    TrafficPolicyId: str
    TrafficPolicyName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRuleSetResponseTypeDef(BaseValidatorModel):
    CreatedDate: datetime
    LastModificationDate: datetime
    RuleSetArn: str
    RuleSetId: str
    RuleSetName: str
    Rules: List[RuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class IngressBooleanExpressionUnionTypeDef(BaseValidatorModel):
    pass


class IngressStringExpressionUnionTypeDef(BaseValidatorModel):
    pass


class IngressIpv4ExpressionUnionTypeDef(BaseValidatorModel):
    pass


class PolicyConditionTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[IngressBooleanExpressionUnionTypeDef] = None
    IpExpression: Optional[IngressIpv4ExpressionUnionTypeDef] = None
    StringExpression: Optional[IngressStringExpressionUnionTypeDef] = None
    TlsExpression: Optional[IngressTlsProtocolExpressionTypeDef] = None


class RuleStringExpressionUnionTypeDef(BaseValidatorModel):
    pass


class RuleDmarcExpressionUnionTypeDef(BaseValidatorModel):
    pass


class RuleVerdictExpressionUnionTypeDef(BaseValidatorModel):
    pass


class RuleBooleanExpressionUnionTypeDef(BaseValidatorModel):
    pass


class RuleIpExpressionUnionTypeDef(BaseValidatorModel):
    pass


class RuleConditionTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[RuleBooleanExpressionUnionTypeDef] = None
    DmarcExpression: Optional[RuleDmarcExpressionUnionTypeDef] = None
    IpExpression: Optional[RuleIpExpressionUnionTypeDef] = None
    NumberExpression: Optional[RuleNumberExpressionTypeDef] = None
    StringExpression: Optional[RuleStringExpressionUnionTypeDef] = None
    VerdictExpression: Optional[RuleVerdictExpressionUnionTypeDef] = None


class PolicyConditionUnionTypeDef(BaseValidatorModel):
    pass


class PolicyStatementTypeDef(BaseValidatorModel):
    Action: AcceptActionType
    Conditions: Sequence[PolicyConditionUnionTypeDef]


class RuleConditionUnionTypeDef(BaseValidatorModel):
    pass


class RuleActionUnionTypeDef(BaseValidatorModel):
    pass


class RuleTypeDef(BaseValidatorModel):
    Actions: Sequence[RuleActionUnionTypeDef]
    Conditions: Optional[Sequence[RuleConditionUnionTypeDef]] = None
    Name: Optional[str] = None
    Unless: Optional[Sequence[RuleConditionUnionTypeDef]] = None


class PolicyStatementUnionTypeDef(BaseValidatorModel):
    pass


class CreateTrafficPolicyRequestTypeDef(BaseValidatorModel):
    DefaultAction: AcceptActionType
    PolicyStatements: Sequence[PolicyStatementUnionTypeDef]
    TrafficPolicyName: str
    ClientToken: Optional[str] = None
    MaxMessageSizeBytes: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateTrafficPolicyRequestTypeDef(BaseValidatorModel):
    TrafficPolicyId: str
    DefaultAction: Optional[AcceptActionType] = None
    MaxMessageSizeBytes: Optional[int] = None
    PolicyStatements: Optional[Sequence[PolicyStatementUnionTypeDef]] = None
    TrafficPolicyName: Optional[str] = None


class RuleUnionTypeDef(BaseValidatorModel):
    pass


class CreateRuleSetRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    Rules: Sequence[RuleUnionTypeDef]
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateRuleSetRequestTypeDef(BaseValidatorModel):
    RuleSetId: str
    RuleSetName: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None



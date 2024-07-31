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
from aws_resource_validator.pydantic_models.mailmanager_constants import *

class AddHeaderActionTypeDef(BaseModel):
    HeaderName: str
    HeaderValue: str

class AddonInstanceTypeDef(BaseModel):
    AddonInstanceArn: Optional[str] = None
    AddonInstanceId: Optional[str] = None
    AddonName: Optional[str] = None
    AddonSubscriptionId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class AddonSubscriptionTypeDef(BaseModel):
    AddonName: Optional[str] = None
    AddonSubscriptionArn: Optional[str] = None
    AddonSubscriptionId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class AnalysisTypeDef(BaseModel):
    Analyzer: str
    ResultField: str

class ArchiveActionTypeDef(BaseModel):
    TargetArchive: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None

class ArchiveBooleanToEvaluateTypeDef(BaseModel):
    Attribute: Optional[Literal["HAS_ATTACHMENTS"]] = None

class ArchiveRetentionTypeDef(BaseModel):
    RetentionPeriod: Optional[RetentionPeriodType] = None

class ArchiveStringToEvaluateTypeDef(BaseModel):
    Attribute: Optional[ArchiveStringEmailAttributeType] = None

class ArchiveTypeDef(BaseModel):
    ArchiveId: str
    ArchiveName: Optional[str] = None
    ArchiveState: Optional[ArchiveStateType] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class IngressPointConfigurationTypeDef(BaseModel):
    SecretArn: Optional[str] = None
    SmtpPassword: Optional[str] = None

class RelayAuthenticationTypeDef(BaseModel):
    NoAuthentication: Optional[Mapping[str, Any]] = None
    SecretArn: Optional[str] = None

class DeleteAddonInstanceRequestRequestTypeDef(BaseModel):
    AddonInstanceId: str

class DeleteAddonSubscriptionRequestRequestTypeDef(BaseModel):
    AddonSubscriptionId: str

class DeleteArchiveRequestRequestTypeDef(BaseModel):
    ArchiveId: str

class DeleteIngressPointRequestRequestTypeDef(BaseModel):
    IngressPointId: str

class DeleteRelayRequestRequestTypeDef(BaseModel):
    RelayId: str

class DeleteRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetId: str

class DeleteTrafficPolicyRequestRequestTypeDef(BaseModel):
    TrafficPolicyId: str

class DeliverToMailboxActionTypeDef(BaseModel):
    MailboxArn: str
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None

class S3ExportDestinationConfigurationTypeDef(BaseModel):
    S3Location: Optional[str] = None

class ExportStatusTypeDef(BaseModel):
    CompletionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    State: Optional[ExportStateType] = None
    SubmissionTimestamp: Optional[datetime] = None

class GetAddonInstanceRequestRequestTypeDef(BaseModel):
    AddonInstanceId: str

class GetAddonSubscriptionRequestRequestTypeDef(BaseModel):
    AddonSubscriptionId: str

class GetArchiveExportRequestRequestTypeDef(BaseModel):
    ExportId: str

class GetArchiveMessageContentRequestRequestTypeDef(BaseModel):
    ArchivedMessageId: str

class MessageBodyTypeDef(BaseModel):
    Html: Optional[str] = None
    MessageMalformed: Optional[bool] = None
    Text: Optional[str] = None

class GetArchiveMessageRequestRequestTypeDef(BaseModel):
    ArchivedMessageId: str

class GetArchiveRequestRequestTypeDef(BaseModel):
    ArchiveId: str

class GetArchiveSearchRequestRequestTypeDef(BaseModel):
    SearchId: str

class SearchStatusTypeDef(BaseModel):
    CompletionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    State: Optional[SearchStateType] = None
    SubmissionTimestamp: Optional[datetime] = None

class GetArchiveSearchResultsRequestRequestTypeDef(BaseModel):
    SearchId: str

class RowTypeDef(BaseModel):
    ArchivedMessageId: Optional[str] = None
    Cc: Optional[str] = None
    Date: Optional[str] = None
    From: Optional[str] = None
    HasAttachments: Optional[bool] = None
    InReplyTo: Optional[str] = None
    MessageId: Optional[str] = None
    ReceivedHeaders: Optional[List[str]] = None
    ReceivedTimestamp: Optional[datetime] = None
    Subject: Optional[str] = None
    To: Optional[str] = None
    XMailer: Optional[str] = None
    XOriginalMailer: Optional[str] = None
    XPriority: Optional[str] = None

class GetIngressPointRequestRequestTypeDef(BaseModel):
    IngressPointId: str

class GetRelayRequestRequestTypeDef(BaseModel):
    RelayId: str

class RelayAuthenticationOutputTypeDef(BaseModel):
    NoAuthentication: Optional[Dict[str, Any]] = None
    SecretArn: Optional[str] = None

class GetRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetId: str

class GetTrafficPolicyRequestRequestTypeDef(BaseModel):
    TrafficPolicyId: str

class IngressAnalysisTypeDef(BaseModel):
    Analyzer: str
    ResultField: str

class IngressIpToEvaluateTypeDef(BaseModel):
    Attribute: Optional[Literal["SENDER_IP"]] = None

class IngressPointPasswordConfigurationTypeDef(BaseModel):
    PreviousSmtpPasswordExpiryTimestamp: Optional[datetime] = None
    PreviousSmtpPasswordVersion: Optional[str] = None
    SmtpPasswordVersion: Optional[str] = None

class IngressPointTypeDef(BaseModel):
    IngressPointId: str
    IngressPointName: str
    Status: IngressPointStatusType
    Type: IngressPointTypeType
    ARecord: Optional[str] = None

class IngressStringToEvaluateTypeDef(BaseModel):
    Attribute: Optional[Literal["RECIPIENT"]] = None

class IngressTlsProtocolToEvaluateTypeDef(BaseModel):
    Attribute: Optional[Literal["TLS_PROTOCOL"]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAddonInstancesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListAddonSubscriptionsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListArchiveExportsRequestRequestTypeDef(BaseModel):
    ArchiveId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListArchiveSearchesRequestRequestTypeDef(BaseModel):
    ArchiveId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListArchivesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListIngressPointsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListRelaysRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class RelayTypeDef(BaseModel):
    LastModifiedTimestamp: Optional[datetime] = None
    RelayId: Optional[str] = None
    RelayName: Optional[str] = None

class ListRuleSetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class RuleSetTypeDef(BaseModel):
    LastModificationDate: Optional[datetime] = None
    RuleSetId: Optional[str] = None
    RuleSetName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListTrafficPoliciesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class TrafficPolicyTypeDef(BaseModel):
    DefaultAction: AcceptActionType
    TrafficPolicyId: str
    TrafficPolicyName: str

class RelayActionTypeDef(BaseModel):
    Relay: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None
    MailFrom: Optional[MailFromType] = None

class ReplaceRecipientActionOutputTypeDef(BaseModel):
    ReplaceWith: Optional[List[str]] = None

class ReplaceRecipientActionTypeDef(BaseModel):
    ReplaceWith: Optional[Sequence[str]] = None

class S3ActionTypeDef(BaseModel):
    RoleArn: str
    S3Bucket: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None
    S3Prefix: Optional[str] = None
    S3SseKmsKeyId: Optional[str] = None

class SendActionTypeDef(BaseModel):
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None

class RuleBooleanToEvaluateTypeDef(BaseModel):
    Attribute: Optional[RuleBooleanEmailAttributeType] = None

class RuleDmarcExpressionOutputTypeDef(BaseModel):
    Operator: RuleDmarcOperatorType
    Values: List[RuleDmarcPolicyType]

class RuleDmarcExpressionTypeDef(BaseModel):
    Operator: RuleDmarcOperatorType
    Values: Sequence[RuleDmarcPolicyType]

class RuleIpToEvaluateTypeDef(BaseModel):
    Attribute: Optional[Literal["SOURCE_IP"]] = None

class RuleNumberToEvaluateTypeDef(BaseModel):
    Attribute: Optional[Literal["MESSAGE_SIZE"]] = None

class RuleStringToEvaluateTypeDef(BaseModel):
    Attribute: Optional[RuleStringEmailAttributeType] = None

class StopArchiveExportRequestRequestTypeDef(BaseModel):
    ExportId: str

class StopArchiveSearchRequestRequestTypeDef(BaseModel):
    SearchId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class RuleVerdictToEvaluateTypeDef(BaseModel):
    Analysis: Optional[AnalysisTypeDef] = None
    Attribute: Optional[RuleVerdictAttributeType] = None

class ArchiveBooleanExpressionTypeDef(BaseModel):
    Evaluate: ArchiveBooleanToEvaluateTypeDef
    Operator: ArchiveBooleanOperatorType

class UpdateArchiveRequestRequestTypeDef(BaseModel):
    ArchiveId: str
    ArchiveName: Optional[str] = None
    Retention: Optional[ArchiveRetentionTypeDef] = None

class ArchiveStringExpressionOutputTypeDef(BaseModel):
    Evaluate: ArchiveStringToEvaluateTypeDef
    Operator: Literal["CONTAINS"]
    Values: List[str]

class ArchiveStringExpressionTypeDef(BaseModel):
    Evaluate: ArchiveStringToEvaluateTypeDef
    Operator: Literal["CONTAINS"]
    Values: Sequence[str]

class CreateAddonInstanceRequestRequestTypeDef(BaseModel):
    AddonSubscriptionId: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAddonSubscriptionRequestRequestTypeDef(BaseModel):
    AddonName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateArchiveRequestRequestTypeDef(BaseModel):
    ArchiveName: str
    ClientToken: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Retention: Optional[ArchiveRetentionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateAddonInstanceResponseTypeDef(BaseModel):
    AddonInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAddonSubscriptionResponseTypeDef(BaseModel):
    AddonSubscriptionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateArchiveResponseTypeDef(BaseModel):
    ArchiveId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIngressPointResponseTypeDef(BaseModel):
    IngressPointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelayResponseTypeDef(BaseModel):
    RelayId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleSetResponseTypeDef(BaseModel):
    RuleSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficPolicyResponseTypeDef(BaseModel):
    TrafficPolicyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAddonInstanceResponseTypeDef(BaseModel):
    AddonInstanceArn: str
    AddonName: str
    AddonSubscriptionId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAddonSubscriptionResponseTypeDef(BaseModel):
    AddonName: str
    AddonSubscriptionArn: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveMessageResponseTypeDef(BaseModel):
    MessageDownloadLink: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveResponseTypeDef(BaseModel):
    ArchiveArn: str
    ArchiveId: str
    ArchiveName: str
    ArchiveState: ArchiveStateType
    CreatedTimestamp: datetime
    KmsKeyArn: str
    LastUpdatedTimestamp: datetime
    Retention: ArchiveRetentionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAddonInstancesResponseTypeDef(BaseModel):
    AddonInstances: List[AddonInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAddonSubscriptionsResponseTypeDef(BaseModel):
    AddonSubscriptions: List[AddonSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListArchivesResponseTypeDef(BaseModel):
    Archives: List[ArchiveTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartArchiveExportResponseTypeDef(BaseModel):
    ExportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartArchiveSearchResponseTypeDef(BaseModel):
    SearchId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIngressPointRequestRequestTypeDef(BaseModel):
    IngressPointName: str
    RuleSetId: str
    TrafficPolicyId: str
    Type: IngressPointTypeType
    ClientToken: Optional[str] = None
    IngressPointConfiguration: Optional[IngressPointConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateIngressPointRequestRequestTypeDef(BaseModel):
    IngressPointId: str
    IngressPointConfiguration: Optional[IngressPointConfigurationTypeDef] = None
    IngressPointName: Optional[str] = None
    RuleSetId: Optional[str] = None
    StatusToUpdate: Optional[IngressPointStatusToUpdateType] = None
    TrafficPolicyId: Optional[str] = None

class CreateRelayRequestRequestTypeDef(BaseModel):
    Authentication: RelayAuthenticationTypeDef
    RelayName: str
    ServerName: str
    ServerPort: int
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRelayRequestRequestTypeDef(BaseModel):
    RelayId: str
    Authentication: Optional[RelayAuthenticationTypeDef] = None
    RelayName: Optional[str] = None
    ServerName: Optional[str] = None
    ServerPort: Optional[int] = None

class ExportDestinationConfigurationTypeDef(BaseModel):
    S3: Optional[S3ExportDestinationConfigurationTypeDef] = None

class ExportSummaryTypeDef(BaseModel):
    ExportId: Optional[str] = None
    Status: Optional[ExportStatusTypeDef] = None

class GetArchiveMessageContentResponseTypeDef(BaseModel):
    Body: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSummaryTypeDef(BaseModel):
    SearchId: Optional[str] = None
    Status: Optional[SearchStatusTypeDef] = None

class GetArchiveSearchResultsResponseTypeDef(BaseModel):
    Rows: List[RowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelayResponseTypeDef(BaseModel):
    Authentication: RelayAuthenticationOutputTypeDef
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    RelayArn: str
    RelayId: str
    RelayName: str
    ServerName: str
    ServerPort: int
    ResponseMetadata: ResponseMetadataTypeDef

class IngressBooleanToEvaluateTypeDef(BaseModel):
    Analysis: Optional[IngressAnalysisTypeDef] = None

class IngressIpv4ExpressionOutputTypeDef(BaseModel):
    Evaluate: IngressIpToEvaluateTypeDef
    Operator: IngressIpOperatorType
    Values: List[str]

class IngressIpv4ExpressionTypeDef(BaseModel):
    Evaluate: IngressIpToEvaluateTypeDef
    Operator: IngressIpOperatorType
    Values: Sequence[str]

class IngressPointAuthConfigurationTypeDef(BaseModel):
    IngressPointPasswordConfiguration: Optional[IngressPointPasswordConfigurationTypeDef] = None
    SecretArn: Optional[str] = None

class ListIngressPointsResponseTypeDef(BaseModel):
    IngressPoints: List[IngressPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class IngressStringExpressionOutputTypeDef(BaseModel):
    Evaluate: IngressStringToEvaluateTypeDef
    Operator: IngressStringOperatorType
    Values: List[str]

class IngressStringExpressionTypeDef(BaseModel):
    Evaluate: IngressStringToEvaluateTypeDef
    Operator: IngressStringOperatorType
    Values: Sequence[str]

class IngressTlsProtocolExpressionTypeDef(BaseModel):
    Evaluate: IngressTlsProtocolToEvaluateTypeDef
    Operator: IngressTlsProtocolOperatorType
    Value: IngressTlsProtocolAttributeType

class ListAddonInstancesRequestListAddonInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAddonSubscriptionsRequestListAddonSubscriptionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArchiveExportsRequestListArchiveExportsPaginateTypeDef(BaseModel):
    ArchiveId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArchiveSearchesRequestListArchiveSearchesPaginateTypeDef(BaseModel):
    ArchiveId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArchivesRequestListArchivesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIngressPointsRequestListIngressPointsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRelaysRequestListRelaysPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRuleSetsRequestListRuleSetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrafficPoliciesRequestListTrafficPoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRelaysResponseTypeDef(BaseModel):
    Relays: List[RelayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRuleSetsResponseTypeDef(BaseModel):
    RuleSets: List[RuleSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrafficPoliciesResponseTypeDef(BaseModel):
    TrafficPolicies: List[TrafficPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RuleActionOutputTypeDef(BaseModel):
    AddHeader: Optional[AddHeaderActionTypeDef] = None
    Archive: Optional[ArchiveActionTypeDef] = None
    DeliverToMailbox: Optional[DeliverToMailboxActionTypeDef] = None
    Drop: Optional[Dict[str, Any]] = None
    Relay: Optional[RelayActionTypeDef] = None
    ReplaceRecipient: Optional[ReplaceRecipientActionOutputTypeDef] = None
    Send: Optional[SendActionTypeDef] = None
    WriteToS3: Optional[S3ActionTypeDef] = None

class RuleActionTypeDef(BaseModel):
    AddHeader: Optional[AddHeaderActionTypeDef] = None
    Archive: Optional[ArchiveActionTypeDef] = None
    DeliverToMailbox: Optional[DeliverToMailboxActionTypeDef] = None
    Drop: Optional[Mapping[str, Any]] = None
    Relay: Optional[RelayActionTypeDef] = None
    ReplaceRecipient: Optional[ReplaceRecipientActionTypeDef] = None
    Send: Optional[SendActionTypeDef] = None
    WriteToS3: Optional[S3ActionTypeDef] = None

class RuleBooleanExpressionTypeDef(BaseModel):
    Evaluate: RuleBooleanToEvaluateTypeDef
    Operator: RuleBooleanOperatorType

class RuleIpExpressionOutputTypeDef(BaseModel):
    Evaluate: RuleIpToEvaluateTypeDef
    Operator: RuleIpOperatorType
    Values: List[str]

class RuleIpExpressionTypeDef(BaseModel):
    Evaluate: RuleIpToEvaluateTypeDef
    Operator: RuleIpOperatorType
    Values: Sequence[str]

class RuleNumberExpressionTypeDef(BaseModel):
    Evaluate: RuleNumberToEvaluateTypeDef
    Operator: RuleNumberOperatorType
    Value: float

class RuleStringExpressionOutputTypeDef(BaseModel):
    Evaluate: RuleStringToEvaluateTypeDef
    Operator: RuleStringOperatorType
    Values: List[str]

class RuleStringExpressionTypeDef(BaseModel):
    Evaluate: RuleStringToEvaluateTypeDef
    Operator: RuleStringOperatorType
    Values: Sequence[str]

class RuleVerdictExpressionOutputTypeDef(BaseModel):
    Evaluate: RuleVerdictToEvaluateTypeDef
    Operator: RuleVerdictOperatorType
    Values: List[RuleVerdictType]

class RuleVerdictExpressionTypeDef(BaseModel):
    Evaluate: RuleVerdictToEvaluateTypeDef
    Operator: RuleVerdictOperatorType
    Values: Sequence[RuleVerdictType]

class ArchiveFilterConditionOutputTypeDef(BaseModel):
    BooleanExpression: Optional[ArchiveBooleanExpressionTypeDef] = None
    StringExpression: Optional[ArchiveStringExpressionOutputTypeDef] = None

class ArchiveFilterConditionTypeDef(BaseModel):
    BooleanExpression: Optional[ArchiveBooleanExpressionTypeDef] = None
    StringExpression: Optional[ArchiveStringExpressionTypeDef] = None

class ListArchiveExportsResponseTypeDef(BaseModel):
    Exports: List[ExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListArchiveSearchesResponseTypeDef(BaseModel):
    Searches: List[SearchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class IngressBooleanExpressionTypeDef(BaseModel):
    Evaluate: IngressBooleanToEvaluateTypeDef
    Operator: IngressBooleanOperatorType

class GetIngressPointResponseTypeDef(BaseModel):
    ARecord: str
    CreatedTimestamp: datetime
    IngressPointArn: str
    IngressPointAuthConfiguration: IngressPointAuthConfigurationTypeDef
    IngressPointId: str
    IngressPointName: str
    LastUpdatedTimestamp: datetime
    RuleSetId: str
    Status: IngressPointStatusType
    TrafficPolicyId: str
    Type: IngressPointTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class RuleConditionOutputTypeDef(BaseModel):
    BooleanExpression: Optional[RuleBooleanExpressionTypeDef] = None
    DmarcExpression: Optional[RuleDmarcExpressionOutputTypeDef] = None
    IpExpression: Optional[RuleIpExpressionOutputTypeDef] = None
    NumberExpression: Optional[RuleNumberExpressionTypeDef] = None
    StringExpression: Optional[RuleStringExpressionOutputTypeDef] = None
    VerdictExpression: Optional[RuleVerdictExpressionOutputTypeDef] = None

class RuleConditionTypeDef(BaseModel):
    BooleanExpression: Optional[RuleBooleanExpressionTypeDef] = None
    DmarcExpression: Optional[RuleDmarcExpressionTypeDef] = None
    IpExpression: Optional[RuleIpExpressionTypeDef] = None
    NumberExpression: Optional[RuleNumberExpressionTypeDef] = None
    StringExpression: Optional[RuleStringExpressionTypeDef] = None
    VerdictExpression: Optional[RuleVerdictExpressionTypeDef] = None

class ArchiveFiltersOutputTypeDef(BaseModel):
    Include: Optional[List[ArchiveFilterConditionOutputTypeDef]] = None
    Unless: Optional[List[ArchiveFilterConditionOutputTypeDef]] = None

class ArchiveFiltersTypeDef(BaseModel):
    Include: Optional[Sequence[ArchiveFilterConditionTypeDef]] = None
    Unless: Optional[Sequence[ArchiveFilterConditionTypeDef]] = None

class PolicyConditionOutputTypeDef(BaseModel):
    BooleanExpression: Optional[IngressBooleanExpressionTypeDef] = None
    IpExpression: Optional[IngressIpv4ExpressionOutputTypeDef] = None
    StringExpression: Optional[IngressStringExpressionOutputTypeDef] = None
    TlsExpression: Optional[IngressTlsProtocolExpressionTypeDef] = None

class PolicyConditionTypeDef(BaseModel):
    BooleanExpression: Optional[IngressBooleanExpressionTypeDef] = None
    IpExpression: Optional[IngressIpv4ExpressionTypeDef] = None
    StringExpression: Optional[IngressStringExpressionTypeDef] = None
    TlsExpression: Optional[IngressTlsProtocolExpressionTypeDef] = None

class RuleOutputTypeDef(BaseModel):
    Actions: List[RuleActionOutputTypeDef]
    Conditions: Optional[List[RuleConditionOutputTypeDef]] = None
    Name: Optional[str] = None
    Unless: Optional[List[RuleConditionOutputTypeDef]] = None

class RuleTypeDef(BaseModel):
    Actions: Sequence[RuleActionTypeDef]
    Conditions: Optional[Sequence[RuleConditionTypeDef]] = None
    Name: Optional[str] = None
    Unless: Optional[Sequence[RuleConditionTypeDef]] = None

class GetArchiveExportResponseTypeDef(BaseModel):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    Filters: ArchiveFiltersOutputTypeDef
    FromTimestamp: datetime
    MaxResults: int
    Status: ExportStatusTypeDef
    ToTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveSearchResponseTypeDef(BaseModel):
    ArchiveId: str
    Filters: ArchiveFiltersOutputTypeDef
    FromTimestamp: datetime
    MaxResults: int
    Status: SearchStatusTypeDef
    ToTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartArchiveExportRequestRequestTypeDef(BaseModel):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    FromTimestamp: TimestampTypeDef
    ToTimestamp: TimestampTypeDef
    Filters: Optional[ArchiveFiltersTypeDef] = None
    MaxResults: Optional[int] = None

class StartArchiveSearchRequestRequestTypeDef(BaseModel):
    ArchiveId: str
    FromTimestamp: TimestampTypeDef
    MaxResults: int
    ToTimestamp: TimestampTypeDef
    Filters: Optional[ArchiveFiltersTypeDef] = None

class PolicyStatementOutputTypeDef(BaseModel):
    Action: AcceptActionType
    Conditions: List[PolicyConditionOutputTypeDef]

class PolicyStatementTypeDef(BaseModel):
    Action: AcceptActionType
    Conditions: Sequence[PolicyConditionTypeDef]

class GetRuleSetResponseTypeDef(BaseModel):
    CreatedDate: datetime
    LastModificationDate: datetime
    RuleSetArn: str
    RuleSetId: str
    RuleSetName: str
    Rules: List[RuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrafficPolicyResponseTypeDef(BaseModel):
    CreatedTimestamp: datetime
    DefaultAction: AcceptActionType
    LastUpdatedTimestamp: datetime
    MaxMessageSizeBytes: int
    PolicyStatements: List[PolicyStatementOutputTypeDef]
    TrafficPolicyArn: str
    TrafficPolicyId: str
    TrafficPolicyName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetName: str
    Rules: Sequence[RuleUnionTypeDef]
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRuleSetRequestRequestTypeDef(BaseModel):
    RuleSetId: str
    RuleSetName: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None

class CreateTrafficPolicyRequestRequestTypeDef(BaseModel):
    DefaultAction: AcceptActionType
    PolicyStatements: Sequence[PolicyStatementUnionTypeDef]
    TrafficPolicyName: str
    ClientToken: Optional[str] = None
    MaxMessageSizeBytes: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateTrafficPolicyRequestRequestTypeDef(BaseModel):
    TrafficPolicyId: str
    DefaultAction: Optional[AcceptActionType] = None
    MaxMessageSizeBytes: Optional[int] = None
    PolicyStatements: Optional[Sequence[PolicyStatementUnionTypeDef]] = None
    TrafficPolicyName: Optional[str] = None


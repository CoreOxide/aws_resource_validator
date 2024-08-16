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

class IngressPointConfigurationTypeDef(BaseValidatorModel):
    SecretArn: Optional[str] = None
    SmtpPassword: Optional[str] = None

class RelayAuthenticationTypeDef(BaseValidatorModel):
    NoAuthentication: Optional[Mapping[str, Any]] = None
    SecretArn: Optional[str] = None

class DeleteAddonInstanceRequestRequestTypeDef(BaseValidatorModel):
    AddonInstanceId: str

class DeleteAddonSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    AddonSubscriptionId: str

class DeleteArchiveRequestRequestTypeDef(BaseValidatorModel):
    ArchiveId: str

class DeleteIngressPointRequestRequestTypeDef(BaseValidatorModel):
    IngressPointId: str

class DeleteRelayRequestRequestTypeDef(BaseValidatorModel):
    RelayId: str

class DeleteRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetId: str

class DeleteTrafficPolicyRequestRequestTypeDef(BaseValidatorModel):
    TrafficPolicyId: str

class DeliverToMailboxActionTypeDef(BaseValidatorModel):
    MailboxArn: str
    RoleArn: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None

class S3ExportDestinationConfigurationTypeDef(BaseValidatorModel):
    S3Location: Optional[str] = None

class ExportStatusTypeDef(BaseValidatorModel):
    CompletionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    State: Optional[ExportStateType] = None
    SubmissionTimestamp: Optional[datetime] = None

class GetAddonInstanceRequestRequestTypeDef(BaseValidatorModel):
    AddonInstanceId: str

class GetAddonSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    AddonSubscriptionId: str

class GetArchiveExportRequestRequestTypeDef(BaseValidatorModel):
    ExportId: str

class GetArchiveMessageContentRequestRequestTypeDef(BaseValidatorModel):
    ArchivedMessageId: str

class MessageBodyTypeDef(BaseValidatorModel):
    Html: Optional[str] = None
    MessageMalformed: Optional[bool] = None
    Text: Optional[str] = None

class GetArchiveMessageRequestRequestTypeDef(BaseValidatorModel):
    ArchivedMessageId: str

class GetArchiveRequestRequestTypeDef(BaseValidatorModel):
    ArchiveId: str

class GetArchiveSearchRequestRequestTypeDef(BaseValidatorModel):
    SearchId: str

class SearchStatusTypeDef(BaseValidatorModel):
    CompletionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    State: Optional[SearchStateType] = None
    SubmissionTimestamp: Optional[datetime] = None

class GetArchiveSearchResultsRequestRequestTypeDef(BaseValidatorModel):
    SearchId: str

class RowTypeDef(BaseValidatorModel):
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

class GetIngressPointRequestRequestTypeDef(BaseValidatorModel):
    IngressPointId: str

class GetRelayRequestRequestTypeDef(BaseValidatorModel):
    RelayId: str

class RelayAuthenticationOutputTypeDef(BaseValidatorModel):
    NoAuthentication: Optional[Dict[str, Any]] = None
    SecretArn: Optional[str] = None

class GetRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetId: str

class GetTrafficPolicyRequestRequestTypeDef(BaseValidatorModel):
    TrafficPolicyId: str

class IngressAnalysisTypeDef(BaseValidatorModel):
    Analyzer: str
    ResultField: str

class IngressIpToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["SENDER_IP"]] = None

class IngressPointPasswordConfigurationTypeDef(BaseValidatorModel):
    PreviousSmtpPasswordExpiryTimestamp: Optional[datetime] = None
    PreviousSmtpPasswordVersion: Optional[str] = None
    SmtpPasswordVersion: Optional[str] = None

class IngressPointTypeDef(BaseValidatorModel):
    IngressPointId: str
    IngressPointName: str
    Status: IngressPointStatusType
    Type: IngressPointTypeType
    ARecord: Optional[str] = None

class IngressStringToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["RECIPIENT"]] = None

class IngressTlsProtocolToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["TLS_PROTOCOL"]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAddonInstancesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListAddonSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListArchiveExportsRequestRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListArchiveSearchesRequestRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListArchivesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListIngressPointsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListRelaysRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class RelayTypeDef(BaseValidatorModel):
    LastModifiedTimestamp: Optional[datetime] = None
    RelayId: Optional[str] = None
    RelayName: Optional[str] = None

class ListRuleSetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class RuleSetTypeDef(BaseValidatorModel):
    LastModificationDate: Optional[datetime] = None
    RuleSetId: Optional[str] = None
    RuleSetName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListTrafficPoliciesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class TrafficPolicyTypeDef(BaseValidatorModel):
    DefaultAction: AcceptActionType
    TrafficPolicyId: str
    TrafficPolicyName: str

class RelayActionTypeDef(BaseValidatorModel):
    Relay: str
    ActionFailurePolicy: Optional[ActionFailurePolicyType] = None
    MailFrom: Optional[MailFromType] = None

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

class RuleBooleanToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[RuleBooleanEmailAttributeType] = None

class RuleDmarcExpressionOutputTypeDef(BaseValidatorModel):
    Operator: RuleDmarcOperatorType
    Values: List[RuleDmarcPolicyType]

class RuleDmarcExpressionTypeDef(BaseValidatorModel):
    Operator: RuleDmarcOperatorType
    Values: Sequence[RuleDmarcPolicyType]

class RuleIpToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["SOURCE_IP"]] = None

class RuleNumberToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[Literal["MESSAGE_SIZE"]] = None

class RuleStringToEvaluateTypeDef(BaseValidatorModel):
    Attribute: Optional[RuleStringEmailAttributeType] = None

class StopArchiveExportRequestRequestTypeDef(BaseValidatorModel):
    ExportId: str

class StopArchiveSearchRequestRequestTypeDef(BaseValidatorModel):
    SearchId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class RuleVerdictToEvaluateTypeDef(BaseValidatorModel):
    Analysis: Optional[AnalysisTypeDef] = None
    Attribute: Optional[RuleVerdictAttributeType] = None

class ArchiveBooleanExpressionTypeDef(BaseValidatorModel):
    Evaluate: ArchiveBooleanToEvaluateTypeDef
    Operator: ArchiveBooleanOperatorType

class UpdateArchiveRequestRequestTypeDef(BaseValidatorModel):
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

class CreateAddonInstanceRequestRequestTypeDef(BaseValidatorModel):
    AddonSubscriptionId: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAddonSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    AddonName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateArchiveRequestRequestTypeDef(BaseValidatorModel):
    ArchiveName: str
    ClientToken: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Retention: Optional[ArchiveRetentionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateAddonInstanceResponseTypeDef(BaseValidatorModel):
    AddonInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAddonSubscriptionResponseTypeDef(BaseValidatorModel):
    AddonSubscriptionId: str
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

class GetArchiveMessageResponseTypeDef(BaseValidatorModel):
    MessageDownloadLink: str
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

class ListAddonInstancesResponseTypeDef(BaseValidatorModel):
    AddonInstances: List[AddonInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAddonSubscriptionsResponseTypeDef(BaseValidatorModel):
    AddonSubscriptions: List[AddonSubscriptionTypeDef]
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

class CreateIngressPointRequestRequestTypeDef(BaseValidatorModel):
    IngressPointName: str
    RuleSetId: str
    TrafficPolicyId: str
    Type: IngressPointTypeType
    ClientToken: Optional[str] = None
    IngressPointConfiguration: Optional[IngressPointConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateIngressPointRequestRequestTypeDef(BaseValidatorModel):
    IngressPointId: str
    IngressPointConfiguration: Optional[IngressPointConfigurationTypeDef] = None
    IngressPointName: Optional[str] = None
    RuleSetId: Optional[str] = None
    StatusToUpdate: Optional[IngressPointStatusToUpdateType] = None
    TrafficPolicyId: Optional[str] = None

class CreateRelayRequestRequestTypeDef(BaseValidatorModel):
    Authentication: RelayAuthenticationTypeDef
    RelayName: str
    ServerName: str
    ServerPort: int
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRelayRequestRequestTypeDef(BaseValidatorModel):
    RelayId: str
    Authentication: Optional[RelayAuthenticationTypeDef] = None
    RelayName: Optional[str] = None
    ServerName: Optional[str] = None
    ServerPort: Optional[int] = None

class ExportDestinationConfigurationTypeDef(BaseValidatorModel):
    S3: Optional[S3ExportDestinationConfigurationTypeDef] = None

class ExportSummaryTypeDef(BaseValidatorModel):
    ExportId: Optional[str] = None
    Status: Optional[ExportStatusTypeDef] = None

class GetArchiveMessageContentResponseTypeDef(BaseValidatorModel):
    Body: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSummaryTypeDef(BaseValidatorModel):
    SearchId: Optional[str] = None
    Status: Optional[SearchStatusTypeDef] = None

class GetArchiveSearchResultsResponseTypeDef(BaseValidatorModel):
    Rows: List[RowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class IngressBooleanToEvaluateTypeDef(BaseValidatorModel):
    Analysis: Optional[IngressAnalysisTypeDef] = None

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

class ListAddonInstancesRequestListAddonInstancesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAddonSubscriptionsRequestListAddonSubscriptionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArchiveExportsRequestListArchiveExportsPaginateTypeDef(BaseValidatorModel):
    ArchiveId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArchiveSearchesRequestListArchiveSearchesPaginateTypeDef(BaseValidatorModel):
    ArchiveId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArchivesRequestListArchivesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIngressPointsRequestListIngressPointsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRelaysRequestListRelaysPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRuleSetsRequestListRuleSetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrafficPoliciesRequestListTrafficPoliciesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

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
    Drop: Optional[Dict[str, Any]] = None
    Relay: Optional[RelayActionTypeDef] = None
    ReplaceRecipient: Optional[ReplaceRecipientActionOutputTypeDef] = None
    Send: Optional[SendActionTypeDef] = None
    WriteToS3: Optional[S3ActionTypeDef] = None

class RuleActionTypeDef(BaseValidatorModel):
    AddHeader: Optional[AddHeaderActionTypeDef] = None
    Archive: Optional[ArchiveActionTypeDef] = None
    DeliverToMailbox: Optional[DeliverToMailboxActionTypeDef] = None
    Drop: Optional[Mapping[str, Any]] = None
    Relay: Optional[RelayActionTypeDef] = None
    ReplaceRecipient: Optional[ReplaceRecipientActionTypeDef] = None
    Send: Optional[SendActionTypeDef] = None
    WriteToS3: Optional[S3ActionTypeDef] = None

class RuleBooleanExpressionTypeDef(BaseValidatorModel):
    Evaluate: RuleBooleanToEvaluateTypeDef
    Operator: RuleBooleanOperatorType

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

class ListArchiveExportsResponseTypeDef(BaseValidatorModel):
    Exports: List[ExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListArchiveSearchesResponseTypeDef(BaseValidatorModel):
    Searches: List[SearchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class IngressBooleanExpressionTypeDef(BaseValidatorModel):
    Evaluate: IngressBooleanToEvaluateTypeDef
    Operator: IngressBooleanOperatorType

class GetIngressPointResponseTypeDef(BaseValidatorModel):
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

class RuleConditionOutputTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[RuleBooleanExpressionTypeDef] = None
    DmarcExpression: Optional[RuleDmarcExpressionOutputTypeDef] = None
    IpExpression: Optional[RuleIpExpressionOutputTypeDef] = None
    NumberExpression: Optional[RuleNumberExpressionTypeDef] = None
    StringExpression: Optional[RuleStringExpressionOutputTypeDef] = None
    VerdictExpression: Optional[RuleVerdictExpressionOutputTypeDef] = None

class RuleConditionTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[RuleBooleanExpressionTypeDef] = None
    DmarcExpression: Optional[RuleDmarcExpressionTypeDef] = None
    IpExpression: Optional[RuleIpExpressionTypeDef] = None
    NumberExpression: Optional[RuleNumberExpressionTypeDef] = None
    StringExpression: Optional[RuleStringExpressionTypeDef] = None
    VerdictExpression: Optional[RuleVerdictExpressionTypeDef] = None

class ArchiveFiltersOutputTypeDef(BaseValidatorModel):
    Include: Optional[List[ArchiveFilterConditionOutputTypeDef]] = None
    Unless: Optional[List[ArchiveFilterConditionOutputTypeDef]] = None

class ArchiveFiltersTypeDef(BaseValidatorModel):
    Include: Optional[Sequence[ArchiveFilterConditionTypeDef]] = None
    Unless: Optional[Sequence[ArchiveFilterConditionTypeDef]] = None

class PolicyConditionOutputTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[IngressBooleanExpressionTypeDef] = None
    IpExpression: Optional[IngressIpv4ExpressionOutputTypeDef] = None
    StringExpression: Optional[IngressStringExpressionOutputTypeDef] = None
    TlsExpression: Optional[IngressTlsProtocolExpressionTypeDef] = None

class PolicyConditionTypeDef(BaseValidatorModel):
    BooleanExpression: Optional[IngressBooleanExpressionTypeDef] = None
    IpExpression: Optional[IngressIpv4ExpressionTypeDef] = None
    StringExpression: Optional[IngressStringExpressionTypeDef] = None
    TlsExpression: Optional[IngressTlsProtocolExpressionTypeDef] = None

class RuleOutputTypeDef(BaseValidatorModel):
    Actions: List[RuleActionOutputTypeDef]
    Conditions: Optional[List[RuleConditionOutputTypeDef]] = None
    Name: Optional[str] = None
    Unless: Optional[List[RuleConditionOutputTypeDef]] = None

class RuleTypeDef(BaseValidatorModel):
    Actions: Sequence[RuleActionTypeDef]
    Conditions: Optional[Sequence[RuleConditionTypeDef]] = None
    Name: Optional[str] = None
    Unless: Optional[Sequence[RuleConditionTypeDef]] = None

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

class StartArchiveExportRequestRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    FromTimestamp: TimestampTypeDef
    ToTimestamp: TimestampTypeDef
    Filters: Optional[ArchiveFiltersTypeDef] = None
    MaxResults: Optional[int] = None

class StartArchiveSearchRequestRequestTypeDef(BaseValidatorModel):
    ArchiveId: str
    FromTimestamp: TimestampTypeDef
    MaxResults: int
    ToTimestamp: TimestampTypeDef
    Filters: Optional[ArchiveFiltersTypeDef] = None

class PolicyStatementOutputTypeDef(BaseValidatorModel):
    Action: AcceptActionType
    Conditions: List[PolicyConditionOutputTypeDef]

class PolicyStatementTypeDef(BaseValidatorModel):
    Action: AcceptActionType
    Conditions: Sequence[PolicyConditionTypeDef]

class GetRuleSetResponseTypeDef(BaseValidatorModel):
    CreatedDate: datetime
    LastModificationDate: datetime
    RuleSetArn: str
    RuleSetId: str
    RuleSetName: str
    Rules: List[RuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class CreateRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetName: str
    Rules: Sequence[RuleUnionTypeDef]
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRuleSetRequestRequestTypeDef(BaseValidatorModel):
    RuleSetId: str
    RuleSetName: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None

class CreateTrafficPolicyRequestRequestTypeDef(BaseValidatorModel):
    DefaultAction: AcceptActionType
    PolicyStatements: Sequence[PolicyStatementUnionTypeDef]
    TrafficPolicyName: str
    ClientToken: Optional[str] = None
    MaxMessageSizeBytes: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateTrafficPolicyRequestRequestTypeDef(BaseValidatorModel):
    TrafficPolicyId: str
    DefaultAction: Optional[AcceptActionType] = None
    MaxMessageSizeBytes: Optional[int] = None
    PolicyStatements: Optional[Sequence[PolicyStatementUnionTypeDef]] = None
    TrafficPolicyName: Optional[str] = None


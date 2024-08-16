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
from aws_resource_validator.pydantic_models.waf_regional_constants import *

class ExcludedRuleTypeDef(BaseValidatorModel):
    RuleId: str

class WafActionTypeDef(BaseValidatorModel):
    Type: WafActionTypeType

class WafOverrideActionTypeDef(BaseValidatorModel):
    Type: WafOverrideActionTypeType

class AssociateWebACLRequestRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    ResourceArn: str

class ByteMatchSetSummaryTypeDef(BaseValidatorModel):
    ByteMatchSetId: str
    Name: str

class FieldToMatchTypeDef(BaseValidatorModel):
    Type: MatchFieldTypeType
    Data: Optional[str] = None

class CreateByteMatchSetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateGeoMatchSetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str

class CreateIPSetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CreateRegexMatchSetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str

class CreateRegexPatternSetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str

class RegexPatternSetTypeDef(BaseValidatorModel):
    RegexPatternSetId: str
    RegexPatternStrings: List[str]
    Name: Optional[str] = None

class RuleGroupTypeDef(BaseValidatorModel):
    RuleGroupId: str
    Name: Optional[str] = None
    MetricName: Optional[str] = None

class CreateSizeConstraintSetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str

class CreateSqlInjectionMatchSetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str

class CreateWebACLMigrationStackRequestRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    S3BucketName: str
    IgnoreUnsupportedType: bool

class CreateXssMatchSetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str

class DeleteByteMatchSetRequestRequestTypeDef(BaseValidatorModel):
    ByteMatchSetId: str
    ChangeToken: str

class DeleteGeoMatchSetRequestRequestTypeDef(BaseValidatorModel):
    GeoMatchSetId: str
    ChangeToken: str

class DeleteIPSetRequestRequestTypeDef(BaseValidatorModel):
    IPSetId: str
    ChangeToken: str

class DeleteLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DeletePermissionPolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DeleteRateBasedRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleId: str
    ChangeToken: str

class DeleteRegexMatchSetRequestRequestTypeDef(BaseValidatorModel):
    RegexMatchSetId: str
    ChangeToken: str

class DeleteRegexPatternSetRequestRequestTypeDef(BaseValidatorModel):
    RegexPatternSetId: str
    ChangeToken: str

class DeleteRuleGroupRequestRequestTypeDef(BaseValidatorModel):
    RuleGroupId: str
    ChangeToken: str

class DeleteRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleId: str
    ChangeToken: str

class DeleteSizeConstraintSetRequestRequestTypeDef(BaseValidatorModel):
    SizeConstraintSetId: str
    ChangeToken: str

class DeleteSqlInjectionMatchSetRequestRequestTypeDef(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str

class DeleteWebACLRequestRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    ChangeToken: str

class DeleteXssMatchSetRequestRequestTypeDef(BaseValidatorModel):
    XssMatchSetId: str
    ChangeToken: str

class DisassociateWebACLRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class GeoMatchConstraintTypeDef(BaseValidatorModel):
    Type: Literal["Country"]
    Value: GeoMatchConstraintValueType

class GeoMatchSetSummaryTypeDef(BaseValidatorModel):
    GeoMatchSetId: str
    Name: str

class GetByteMatchSetRequestRequestTypeDef(BaseValidatorModel):
    ByteMatchSetId: str

class GetChangeTokenStatusRequestRequestTypeDef(BaseValidatorModel):
    ChangeToken: str

class GetGeoMatchSetRequestRequestTypeDef(BaseValidatorModel):
    GeoMatchSetId: str

class GetIPSetRequestRequestTypeDef(BaseValidatorModel):
    IPSetId: str

class GetLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class GetPermissionPolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class GetRateBasedRuleManagedKeysRequestRequestTypeDef(BaseValidatorModel):
    RuleId: str
    NextMarker: Optional[str] = None

class GetRateBasedRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleId: str

class GetRegexMatchSetRequestRequestTypeDef(BaseValidatorModel):
    RegexMatchSetId: str

class GetRegexPatternSetRequestRequestTypeDef(BaseValidatorModel):
    RegexPatternSetId: str

class GetRuleGroupRequestRequestTypeDef(BaseValidatorModel):
    RuleGroupId: str

class GetRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleId: str

class GetSizeConstraintSetRequestRequestTypeDef(BaseValidatorModel):
    SizeConstraintSetId: str

class GetSqlInjectionMatchSetRequestRequestTypeDef(BaseValidatorModel):
    SqlInjectionMatchSetId: str

class GetWebACLForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class WebACLSummaryTypeDef(BaseValidatorModel):
    WebACLId: str
    Name: str

class GetWebACLRequestRequestTypeDef(BaseValidatorModel):
    WebACLId: str

class GetXssMatchSetRequestRequestTypeDef(BaseValidatorModel):
    XssMatchSetId: str

class HTTPHeaderTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class IPSetDescriptorTypeDef(BaseValidatorModel):
    Type: IPSetDescriptorTypeType
    Value: str

class IPSetSummaryTypeDef(BaseValidatorModel):
    IPSetId: str
    Name: str

class ListActivatedRulesInRuleGroupRequestRequestTypeDef(BaseValidatorModel):
    RuleGroupId: Optional[str] = None
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListByteMatchSetsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListGeoMatchSetsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListIPSetsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListLoggingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListRateBasedRulesRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class RuleSummaryTypeDef(BaseValidatorModel):
    RuleId: str
    Name: str

class ListRegexMatchSetsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class RegexMatchSetSummaryTypeDef(BaseValidatorModel):
    RegexMatchSetId: str
    Name: str

class ListRegexPatternSetsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class RegexPatternSetSummaryTypeDef(BaseValidatorModel):
    RegexPatternSetId: str
    Name: str

class ListResourcesForWebACLRequestRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    ResourceType: Optional[ResourceTypeType] = None

class ListRuleGroupsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class RuleGroupSummaryTypeDef(BaseValidatorModel):
    RuleGroupId: str
    Name: str

class ListRulesRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListSizeConstraintSetsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class SizeConstraintSetSummaryTypeDef(BaseValidatorModel):
    SizeConstraintSetId: str
    Name: str

class ListSqlInjectionMatchSetsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class SqlInjectionMatchSetSummaryTypeDef(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    Name: str

class ListSubscribedRuleGroupsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class SubscribedRuleGroupSummaryTypeDef(BaseValidatorModel):
    RuleGroupId: str
    Name: str
    MetricName: str

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListWebACLsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListXssMatchSetsRequestRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class XssMatchSetSummaryTypeDef(BaseValidatorModel):
    XssMatchSetId: str
    Name: str

class PredicateTypeDef(BaseValidatorModel):
    Negated: bool
    Type: PredicateTypeType
    DataId: str

class PutPermissionPolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str

class RegexPatternSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    RegexPatternString: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ActivatedRuleTypeDef(BaseValidatorModel):
    Priority: int
    RuleId: str
    Action: Optional[WafActionTypeDef] = None
    OverrideAction: Optional[WafOverrideActionTypeDef] = None
    Type: Optional[WafRuleTypeType] = None
    ExcludedRules: Optional[List[ExcludedRuleTypeDef]] = None

class ByteMatchTupleTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchTypeDef
    TargetString: bytes
    TextTransformation: TextTransformationType
    PositionalConstraint: PositionalConstraintType

class LoggingConfigurationTypeDef(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatchTypeDef]] = None

class RegexMatchTupleTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType
    RegexPatternSetId: str

class SizeConstraintTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType
    ComparisonOperator: ComparisonOperatorType
    Size: int

class SqlInjectionMatchTupleTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType

class XssMatchTupleTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType

class CreateWebACLMigrationStackResponseTypeDef(BaseValidatorModel):
    S3ObjectUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteByteMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGeoMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIPSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRateBasedRuleResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegexMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegexPatternSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleGroupResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSizeConstraintSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSqlInjectionMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWebACLResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteXssMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeTokenResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeTokenStatusResponseTypeDef(BaseValidatorModel):
    ChangeTokenStatus: ChangeTokenStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionPolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedRuleManagedKeysResponseTypeDef(BaseValidatorModel):
    ManagedKeys: List[str]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListByteMatchSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    ByteMatchSets: List[ByteMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesForWebACLResponseTypeDef(BaseValidatorModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateByteMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeoMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIPSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRateBasedRuleResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexPatternSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSizeConstraintSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSqlInjectionMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebACLResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateXssMatchSetResponseTypeDef(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRateBasedRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    MetricName: str
    RateKey: Literal["IP"]
    RateLimit: int
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateRuleGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateWebACLRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    MetricName: str
    DefaultAction: WafActionTypeDef
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagInfoForResourceTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    TagList: Optional[List[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateRegexPatternSetResponseTypeDef(BaseValidatorModel):
    RegexPatternSet: RegexPatternSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegexPatternSetResponseTypeDef(BaseValidatorModel):
    RegexPatternSet: RegexPatternSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupResponseTypeDef(BaseValidatorModel):
    RuleGroup: RuleGroupTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleGroupResponseTypeDef(BaseValidatorModel):
    RuleGroup: RuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GeoMatchSetTypeDef(BaseValidatorModel):
    GeoMatchSetId: str
    GeoMatchConstraints: List[GeoMatchConstraintTypeDef]
    Name: Optional[str] = None

class GeoMatchSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    GeoMatchConstraint: GeoMatchConstraintTypeDef

class ListGeoMatchSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    GeoMatchSets: List[GeoMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebACLForResourceResponseTypeDef(BaseValidatorModel):
    WebACLSummary: WebACLSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebACLsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    WebACLs: List[WebACLSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class HTTPRequestTypeDef(BaseValidatorModel):
    ClientIP: Optional[str] = None
    Country: Optional[str] = None
    URI: Optional[str] = None
    Method: Optional[str] = None
    HTTPVersion: Optional[str] = None
    Headers: Optional[List[HTTPHeaderTypeDef]] = None

class IPSetTypeDef(BaseValidatorModel):
    IPSetId: str
    IPSetDescriptors: List[IPSetDescriptorTypeDef]
    Name: Optional[str] = None

class IPSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    IPSetDescriptor: IPSetDescriptorTypeDef

class ListIPSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    IPSets: List[IPSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRateBasedRulesResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Rules: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Rules: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRegexMatchSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    RegexMatchSets: List[RegexMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRegexPatternSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRuleGroupsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[RuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSizeConstraintSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    SizeConstraintSets: List[SizeConstraintSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSqlInjectionMatchSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    SqlInjectionMatchSets: List[SqlInjectionMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscribedRuleGroupsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[SubscribedRuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListXssMatchSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    XssMatchSets: List[XssMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RateBasedRuleTypeDef(BaseValidatorModel):
    RuleId: str
    MatchPredicates: List[PredicateTypeDef]
    RateKey: Literal["IP"]
    RateLimit: int
    Name: Optional[str] = None
    MetricName: Optional[str] = None

class RuleTypeDef(BaseValidatorModel):
    RuleId: str
    Predicates: List[PredicateTypeDef]
    Name: Optional[str] = None
    MetricName: Optional[str] = None

class RuleUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    Predicate: PredicateTypeDef

class UpdateRegexPatternSetRequestRequestTypeDef(BaseValidatorModel):
    RegexPatternSetId: str
    Updates: Sequence[RegexPatternSetUpdateTypeDef]
    ChangeToken: str

class TimeWindowTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class ListActivatedRulesInRuleGroupResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    ActivatedRules: List[ActivatedRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleGroupUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleTypeDef

class WebACLTypeDef(BaseValidatorModel):
    WebACLId: str
    DefaultAction: WafActionTypeDef
    Rules: List[ActivatedRuleTypeDef]
    Name: Optional[str] = None
    MetricName: Optional[str] = None
    WebACLArn: Optional[str] = None

class WebACLUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleTypeDef

class ByteMatchSetTypeDef(BaseValidatorModel):
    ByteMatchSetId: str
    ByteMatchTuples: List[ByteMatchTupleTypeDef]
    Name: Optional[str] = None

class ByteMatchSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    ByteMatchTuple: ByteMatchTupleTypeDef

class GetLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggingConfigurationsResponseTypeDef(BaseValidatorModel):
    LoggingConfigurations: List[LoggingConfigurationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationTypeDef

class PutLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegexMatchSetTypeDef(BaseValidatorModel):
    RegexMatchSetId: Optional[str] = None
    Name: Optional[str] = None
    RegexMatchTuples: Optional[List[RegexMatchTupleTypeDef]] = None

class RegexMatchSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    RegexMatchTuple: RegexMatchTupleTypeDef

class SizeConstraintSetTypeDef(BaseValidatorModel):
    SizeConstraintSetId: str
    SizeConstraints: List[SizeConstraintTypeDef]
    Name: Optional[str] = None

class SizeConstraintSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    SizeConstraint: SizeConstraintTypeDef

class SqlInjectionMatchSetTypeDef(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    SqlInjectionMatchTuples: List[SqlInjectionMatchTupleTypeDef]
    Name: Optional[str] = None

class SqlInjectionMatchSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    SqlInjectionMatchTuple: SqlInjectionMatchTupleTypeDef

class XssMatchSetTypeDef(BaseValidatorModel):
    XssMatchSetId: str
    XssMatchTuples: List[XssMatchTupleTypeDef]
    Name: Optional[str] = None

class XssMatchSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    XssMatchTuple: XssMatchTupleTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    TagInfoForResource: TagInfoForResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGeoMatchSetResponseTypeDef(BaseValidatorModel):
    GeoMatchSet: GeoMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGeoMatchSetResponseTypeDef(BaseValidatorModel):
    GeoMatchSet: GeoMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeoMatchSetRequestRequestTypeDef(BaseValidatorModel):
    GeoMatchSetId: str
    ChangeToken: str
    Updates: Sequence[GeoMatchSetUpdateTypeDef]

class SampledHTTPRequestTypeDef(BaseValidatorModel):
    Request: HTTPRequestTypeDef
    Weight: int
    Timestamp: Optional[datetime] = None
    Action: Optional[str] = None
    RuleWithinRuleGroup: Optional[str] = None

class CreateIPSetResponseTypeDef(BaseValidatorModel):
    IPSet: IPSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIPSetResponseTypeDef(BaseValidatorModel):
    IPSet: IPSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIPSetRequestRequestTypeDef(BaseValidatorModel):
    IPSetId: str
    ChangeToken: str
    Updates: Sequence[IPSetUpdateTypeDef]

class CreateRateBasedRuleResponseTypeDef(BaseValidatorModel):
    Rule: RateBasedRuleTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedRuleResponseTypeDef(BaseValidatorModel):
    Rule: RateBasedRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleResponseTypeDef(BaseValidatorModel):
    Rule: RuleTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleResponseTypeDef(BaseValidatorModel):
    Rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRateBasedRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleId: str
    ChangeToken: str
    Updates: Sequence[RuleUpdateTypeDef]
    RateLimit: int

class UpdateRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleId: str
    ChangeToken: str
    Updates: Sequence[RuleUpdateTypeDef]

class GetSampledRequestsRequestRequestTypeDef(BaseValidatorModel):
    WebAclId: str
    RuleId: str
    TimeWindow: TimeWindowTypeDef
    MaxItems: int

class UpdateRuleGroupRequestRequestTypeDef(BaseValidatorModel):
    RuleGroupId: str
    Updates: Sequence[RuleGroupUpdateTypeDef]
    ChangeToken: str

class CreateWebACLResponseTypeDef(BaseValidatorModel):
    WebACL: WebACLTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebACLResponseTypeDef(BaseValidatorModel):
    WebACL: WebACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebACLRequestRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    ChangeToken: str
    Updates: Optional[Sequence[WebACLUpdateTypeDef]] = None
    DefaultAction: Optional[WafActionTypeDef] = None

class CreateByteMatchSetResponseTypeDef(BaseValidatorModel):
    ByteMatchSet: ByteMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetByteMatchSetResponseTypeDef(BaseValidatorModel):
    ByteMatchSet: ByteMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateByteMatchSetRequestRequestTypeDef(BaseValidatorModel):
    ByteMatchSetId: str
    ChangeToken: str
    Updates: Sequence[ByteMatchSetUpdateTypeDef]

class CreateRegexMatchSetResponseTypeDef(BaseValidatorModel):
    RegexMatchSet: RegexMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegexMatchSetResponseTypeDef(BaseValidatorModel):
    RegexMatchSet: RegexMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexMatchSetRequestRequestTypeDef(BaseValidatorModel):
    RegexMatchSetId: str
    Updates: Sequence[RegexMatchSetUpdateTypeDef]
    ChangeToken: str

class CreateSizeConstraintSetResponseTypeDef(BaseValidatorModel):
    SizeConstraintSet: SizeConstraintSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSizeConstraintSetResponseTypeDef(BaseValidatorModel):
    SizeConstraintSet: SizeConstraintSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSizeConstraintSetRequestRequestTypeDef(BaseValidatorModel):
    SizeConstraintSetId: str
    ChangeToken: str
    Updates: Sequence[SizeConstraintSetUpdateTypeDef]

class CreateSqlInjectionMatchSetResponseTypeDef(BaseValidatorModel):
    SqlInjectionMatchSet: SqlInjectionMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSqlInjectionMatchSetResponseTypeDef(BaseValidatorModel):
    SqlInjectionMatchSet: SqlInjectionMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSqlInjectionMatchSetRequestRequestTypeDef(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str
    Updates: Sequence[SqlInjectionMatchSetUpdateTypeDef]

class CreateXssMatchSetResponseTypeDef(BaseValidatorModel):
    XssMatchSet: XssMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetXssMatchSetResponseTypeDef(BaseValidatorModel):
    XssMatchSet: XssMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateXssMatchSetRequestRequestTypeDef(BaseValidatorModel):
    XssMatchSetId: str
    ChangeToken: str
    Updates: Sequence[XssMatchSetUpdateTypeDef]

class GetSampledRequestsResponseTypeDef(BaseValidatorModel):
    SampledRequests: List[SampledHTTPRequestTypeDef]
    PopulationSize: int
    TimeWindow: TimeWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.waf_regional_constants import *

class ExcludedRuleTypeDef(BaseModel):
    RuleId: str

class WafActionTypeDef(BaseModel):
    Type: WafActionTypeType

class WafOverrideActionTypeDef(BaseModel):
    Type: WafOverrideActionTypeType

class AssociateWebACLRequestRequestTypeDef(BaseModel):
    WebACLId: str
    ResourceArn: str

class ByteMatchSetSummaryTypeDef(BaseModel):
    ByteMatchSetId: str
    Name: str

class FieldToMatchTypeDef(BaseModel):
    Type: MatchFieldTypeType
    Data: Optional[str] = None

class CreateByteMatchSetRequestRequestTypeDef(BaseModel):
    Name: str
    ChangeToken: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateGeoMatchSetRequestRequestTypeDef(BaseModel):
    Name: str
    ChangeToken: str

class CreateIPSetRequestRequestTypeDef(BaseModel):
    Name: str
    ChangeToken: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateRegexMatchSetRequestRequestTypeDef(BaseModel):
    Name: str
    ChangeToken: str

class CreateRegexPatternSetRequestRequestTypeDef(BaseModel):
    Name: str
    ChangeToken: str

class RegexPatternSetTypeDef(BaseModel):
    RegexPatternSetId: str
    RegexPatternStrings: List[str]
    Name: Optional[str] = None

class RuleGroupTypeDef(BaseModel):
    RuleGroupId: str
    Name: Optional[str] = None
    MetricName: Optional[str] = None

class CreateSizeConstraintSetRequestRequestTypeDef(BaseModel):
    Name: str
    ChangeToken: str

class CreateSqlInjectionMatchSetRequestRequestTypeDef(BaseModel):
    Name: str
    ChangeToken: str

class CreateWebACLMigrationStackRequestRequestTypeDef(BaseModel):
    WebACLId: str
    S3BucketName: str
    IgnoreUnsupportedType: bool

class CreateXssMatchSetRequestRequestTypeDef(BaseModel):
    Name: str
    ChangeToken: str

class DeleteByteMatchSetRequestRequestTypeDef(BaseModel):
    ByteMatchSetId: str
    ChangeToken: str

class DeleteGeoMatchSetRequestRequestTypeDef(BaseModel):
    GeoMatchSetId: str
    ChangeToken: str

class DeleteIPSetRequestRequestTypeDef(BaseModel):
    IPSetId: str
    ChangeToken: str

class DeleteLoggingConfigurationRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DeletePermissionPolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DeleteRateBasedRuleRequestRequestTypeDef(BaseModel):
    RuleId: str
    ChangeToken: str

class DeleteRegexMatchSetRequestRequestTypeDef(BaseModel):
    RegexMatchSetId: str
    ChangeToken: str

class DeleteRegexPatternSetRequestRequestTypeDef(BaseModel):
    RegexPatternSetId: str
    ChangeToken: str

class DeleteRuleGroupRequestRequestTypeDef(BaseModel):
    RuleGroupId: str
    ChangeToken: str

class DeleteRuleRequestRequestTypeDef(BaseModel):
    RuleId: str
    ChangeToken: str

class DeleteSizeConstraintSetRequestRequestTypeDef(BaseModel):
    SizeConstraintSetId: str
    ChangeToken: str

class DeleteSqlInjectionMatchSetRequestRequestTypeDef(BaseModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str

class DeleteWebACLRequestRequestTypeDef(BaseModel):
    WebACLId: str
    ChangeToken: str

class DeleteXssMatchSetRequestRequestTypeDef(BaseModel):
    XssMatchSetId: str
    ChangeToken: str

class DisassociateWebACLRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GeoMatchConstraintTypeDef(BaseModel):
    Type: Literal["Country"]
    Value: GeoMatchConstraintValueType

class GeoMatchSetSummaryTypeDef(BaseModel):
    GeoMatchSetId: str
    Name: str

class GetByteMatchSetRequestRequestTypeDef(BaseModel):
    ByteMatchSetId: str

class GetChangeTokenStatusRequestRequestTypeDef(BaseModel):
    ChangeToken: str

class GetGeoMatchSetRequestRequestTypeDef(BaseModel):
    GeoMatchSetId: str

class GetIPSetRequestRequestTypeDef(BaseModel):
    IPSetId: str

class GetLoggingConfigurationRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GetPermissionPolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GetRateBasedRuleManagedKeysRequestRequestTypeDef(BaseModel):
    RuleId: str
    NextMarker: Optional[str] = None

class GetRateBasedRuleRequestRequestTypeDef(BaseModel):
    RuleId: str

class GetRegexMatchSetRequestRequestTypeDef(BaseModel):
    RegexMatchSetId: str

class GetRegexPatternSetRequestRequestTypeDef(BaseModel):
    RegexPatternSetId: str

class GetRuleGroupRequestRequestTypeDef(BaseModel):
    RuleGroupId: str

class GetRuleRequestRequestTypeDef(BaseModel):
    RuleId: str

class GetSizeConstraintSetRequestRequestTypeDef(BaseModel):
    SizeConstraintSetId: str

class GetSqlInjectionMatchSetRequestRequestTypeDef(BaseModel):
    SqlInjectionMatchSetId: str

class GetWebACLForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class WebACLSummaryTypeDef(BaseModel):
    WebACLId: str
    Name: str

class GetWebACLRequestRequestTypeDef(BaseModel):
    WebACLId: str

class GetXssMatchSetRequestRequestTypeDef(BaseModel):
    XssMatchSetId: str

class HTTPHeaderTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class IPSetDescriptorTypeDef(BaseModel):
    Type: IPSetDescriptorTypeType
    Value: str

class IPSetSummaryTypeDef(BaseModel):
    IPSetId: str
    Name: str

class ListActivatedRulesInRuleGroupRequestRequestTypeDef(BaseModel):
    RuleGroupId: Optional[str] = None
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListByteMatchSetsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListGeoMatchSetsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListIPSetsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListLoggingConfigurationsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListRateBasedRulesRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class RuleSummaryTypeDef(BaseModel):
    RuleId: str
    Name: str

class ListRegexMatchSetsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class RegexMatchSetSummaryTypeDef(BaseModel):
    RegexMatchSetId: str
    Name: str

class ListRegexPatternSetsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class RegexPatternSetSummaryTypeDef(BaseModel):
    RegexPatternSetId: str
    Name: str

class ListResourcesForWebACLRequestRequestTypeDef(BaseModel):
    WebACLId: str
    ResourceType: Optional[ResourceTypeType] = None

class ListRuleGroupsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class RuleGroupSummaryTypeDef(BaseModel):
    RuleGroupId: str
    Name: str

class ListRulesRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListSizeConstraintSetsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class SizeConstraintSetSummaryTypeDef(BaseModel):
    SizeConstraintSetId: str
    Name: str

class ListSqlInjectionMatchSetsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class SqlInjectionMatchSetSummaryTypeDef(BaseModel):
    SqlInjectionMatchSetId: str
    Name: str

class ListSubscribedRuleGroupsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class SubscribedRuleGroupSummaryTypeDef(BaseModel):
    RuleGroupId: str
    Name: str
    MetricName: str

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListWebACLsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListXssMatchSetsRequestRequestTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class XssMatchSetSummaryTypeDef(BaseModel):
    XssMatchSetId: str
    Name: str

class PredicateTypeDef(BaseModel):
    Negated: bool
    Type: PredicateTypeType
    DataId: str

class PutPermissionPolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Policy: str

class RegexPatternSetUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    RegexPatternString: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ActivatedRuleTypeDef(BaseModel):
    Priority: int
    RuleId: str
    Action: Optional[WafActionTypeDef] = None
    OverrideAction: Optional[WafOverrideActionTypeDef] = None
    Type: Optional[WafRuleTypeType] = None
    ExcludedRules: Optional[List[ExcludedRuleTypeDef]] = None

class ByteMatchTupleTypeDef(BaseModel):
    FieldToMatch: FieldToMatchTypeDef
    TargetString: bytes
    TextTransformation: TextTransformationType
    PositionalConstraint: PositionalConstraintType

class LoggingConfigurationTypeDef(BaseModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatchTypeDef]] = None

class RegexMatchTupleTypeDef(BaseModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType
    RegexPatternSetId: str

class SizeConstraintTypeDef(BaseModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType
    ComparisonOperator: ComparisonOperatorType
    Size: int

class SqlInjectionMatchTupleTypeDef(BaseModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType

class XssMatchTupleTypeDef(BaseModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType

class CreateWebACLMigrationStackResponseTypeDef(BaseModel):
    S3ObjectUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteByteMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGeoMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIPSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRateBasedRuleResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegexMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegexPatternSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleGroupResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSizeConstraintSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSqlInjectionMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWebACLResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteXssMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeTokenResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeTokenStatusResponseTypeDef(BaseModel):
    ChangeTokenStatus: ChangeTokenStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionPolicyResponseTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedRuleManagedKeysResponseTypeDef(BaseModel):
    ManagedKeys: List[str]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListByteMatchSetsResponseTypeDef(BaseModel):
    NextMarker: str
    ByteMatchSets: List[ByteMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesForWebACLResponseTypeDef(BaseModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateByteMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeoMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIPSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRateBasedRuleResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexPatternSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSizeConstraintSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSqlInjectionMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebACLResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateXssMatchSetResponseTypeDef(BaseModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRateBasedRuleRequestRequestTypeDef(BaseModel):
    Name: str
    MetricName: str
    RateKey: Literal["IP"]
    RateLimit: int
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateRuleGroupRequestRequestTypeDef(BaseModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateRuleRequestRequestTypeDef(BaseModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateWebACLRequestRequestTypeDef(BaseModel):
    Name: str
    MetricName: str
    DefaultAction: WafActionTypeDef
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagInfoForResourceTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    TagList: Optional[List[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateRegexPatternSetResponseTypeDef(BaseModel):
    RegexPatternSet: RegexPatternSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegexPatternSetResponseTypeDef(BaseModel):
    RegexPatternSet: RegexPatternSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupResponseTypeDef(BaseModel):
    RuleGroup: RuleGroupTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleGroupResponseTypeDef(BaseModel):
    RuleGroup: RuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GeoMatchSetTypeDef(BaseModel):
    GeoMatchSetId: str
    GeoMatchConstraints: List[GeoMatchConstraintTypeDef]
    Name: Optional[str] = None

class GeoMatchSetUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    GeoMatchConstraint: GeoMatchConstraintTypeDef

class ListGeoMatchSetsResponseTypeDef(BaseModel):
    NextMarker: str
    GeoMatchSets: List[GeoMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebACLForResourceResponseTypeDef(BaseModel):
    WebACLSummary: WebACLSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebACLsResponseTypeDef(BaseModel):
    NextMarker: str
    WebACLs: List[WebACLSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class HTTPRequestTypeDef(BaseModel):
    ClientIP: Optional[str] = None
    Country: Optional[str] = None
    URI: Optional[str] = None
    Method: Optional[str] = None
    HTTPVersion: Optional[str] = None
    Headers: Optional[List[HTTPHeaderTypeDef]] = None

class IPSetTypeDef(BaseModel):
    IPSetId: str
    IPSetDescriptors: List[IPSetDescriptorTypeDef]
    Name: Optional[str] = None

class IPSetUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    IPSetDescriptor: IPSetDescriptorTypeDef

class ListIPSetsResponseTypeDef(BaseModel):
    NextMarker: str
    IPSets: List[IPSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRateBasedRulesResponseTypeDef(BaseModel):
    NextMarker: str
    Rules: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesResponseTypeDef(BaseModel):
    NextMarker: str
    Rules: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRegexMatchSetsResponseTypeDef(BaseModel):
    NextMarker: str
    RegexMatchSets: List[RegexMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRegexPatternSetsResponseTypeDef(BaseModel):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRuleGroupsResponseTypeDef(BaseModel):
    NextMarker: str
    RuleGroups: List[RuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSizeConstraintSetsResponseTypeDef(BaseModel):
    NextMarker: str
    SizeConstraintSets: List[SizeConstraintSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSqlInjectionMatchSetsResponseTypeDef(BaseModel):
    NextMarker: str
    SqlInjectionMatchSets: List[SqlInjectionMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscribedRuleGroupsResponseTypeDef(BaseModel):
    NextMarker: str
    RuleGroups: List[SubscribedRuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListXssMatchSetsResponseTypeDef(BaseModel):
    NextMarker: str
    XssMatchSets: List[XssMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RateBasedRuleTypeDef(BaseModel):
    RuleId: str
    MatchPredicates: List[PredicateTypeDef]
    RateKey: Literal["IP"]
    RateLimit: int
    Name: Optional[str] = None
    MetricName: Optional[str] = None

class RuleTypeDef(BaseModel):
    RuleId: str
    Predicates: List[PredicateTypeDef]
    Name: Optional[str] = None
    MetricName: Optional[str] = None

class RuleUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    Predicate: PredicateTypeDef

class UpdateRegexPatternSetRequestRequestTypeDef(BaseModel):
    RegexPatternSetId: str
    Updates: Sequence[RegexPatternSetUpdateTypeDef]
    ChangeToken: str

class TimeWindowTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class ListActivatedRulesInRuleGroupResponseTypeDef(BaseModel):
    NextMarker: str
    ActivatedRules: List[ActivatedRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleGroupUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleTypeDef

class WebACLTypeDef(BaseModel):
    WebACLId: str
    DefaultAction: WafActionTypeDef
    Rules: List[ActivatedRuleTypeDef]
    Name: Optional[str] = None
    MetricName: Optional[str] = None
    WebACLArn: Optional[str] = None

class WebACLUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleTypeDef

class ByteMatchSetTypeDef(BaseModel):
    ByteMatchSetId: str
    ByteMatchTuples: List[ByteMatchTupleTypeDef]
    Name: Optional[str] = None

class ByteMatchSetUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    ByteMatchTuple: ByteMatchTupleTypeDef

class GetLoggingConfigurationResponseTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggingConfigurationsResponseTypeDef(BaseModel):
    LoggingConfigurations: List[LoggingConfigurationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingConfigurationRequestRequestTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationTypeDef

class PutLoggingConfigurationResponseTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegexMatchSetTypeDef(BaseModel):
    RegexMatchSetId: Optional[str] = None
    Name: Optional[str] = None
    RegexMatchTuples: Optional[List[RegexMatchTupleTypeDef]] = None

class RegexMatchSetUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    RegexMatchTuple: RegexMatchTupleTypeDef

class SizeConstraintSetTypeDef(BaseModel):
    SizeConstraintSetId: str
    SizeConstraints: List[SizeConstraintTypeDef]
    Name: Optional[str] = None

class SizeConstraintSetUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    SizeConstraint: SizeConstraintTypeDef

class SqlInjectionMatchSetTypeDef(BaseModel):
    SqlInjectionMatchSetId: str
    SqlInjectionMatchTuples: List[SqlInjectionMatchTupleTypeDef]
    Name: Optional[str] = None

class SqlInjectionMatchSetUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    SqlInjectionMatchTuple: SqlInjectionMatchTupleTypeDef

class XssMatchSetTypeDef(BaseModel):
    XssMatchSetId: str
    XssMatchTuples: List[XssMatchTupleTypeDef]
    Name: Optional[str] = None

class XssMatchSetUpdateTypeDef(BaseModel):
    Action: ChangeActionType
    XssMatchTuple: XssMatchTupleTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    NextMarker: str
    TagInfoForResource: TagInfoForResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGeoMatchSetResponseTypeDef(BaseModel):
    GeoMatchSet: GeoMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGeoMatchSetResponseTypeDef(BaseModel):
    GeoMatchSet: GeoMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeoMatchSetRequestRequestTypeDef(BaseModel):
    GeoMatchSetId: str
    ChangeToken: str
    Updates: Sequence[GeoMatchSetUpdateTypeDef]

class SampledHTTPRequestTypeDef(BaseModel):
    Request: HTTPRequestTypeDef
    Weight: int
    Timestamp: Optional[datetime] = None
    Action: Optional[str] = None
    RuleWithinRuleGroup: Optional[str] = None

class CreateIPSetResponseTypeDef(BaseModel):
    IPSet: IPSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIPSetResponseTypeDef(BaseModel):
    IPSet: IPSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIPSetRequestRequestTypeDef(BaseModel):
    IPSetId: str
    ChangeToken: str
    Updates: Sequence[IPSetUpdateTypeDef]

class CreateRateBasedRuleResponseTypeDef(BaseModel):
    Rule: RateBasedRuleTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedRuleResponseTypeDef(BaseModel):
    Rule: RateBasedRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleResponseTypeDef(BaseModel):
    Rule: RuleTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleResponseTypeDef(BaseModel):
    Rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRateBasedRuleRequestRequestTypeDef(BaseModel):
    RuleId: str
    ChangeToken: str
    Updates: Sequence[RuleUpdateTypeDef]
    RateLimit: int

class UpdateRuleRequestRequestTypeDef(BaseModel):
    RuleId: str
    ChangeToken: str
    Updates: Sequence[RuleUpdateTypeDef]

class GetSampledRequestsRequestRequestTypeDef(BaseModel):
    WebAclId: str
    RuleId: str
    TimeWindow: TimeWindowTypeDef
    MaxItems: int

class UpdateRuleGroupRequestRequestTypeDef(BaseModel):
    RuleGroupId: str
    Updates: Sequence[RuleGroupUpdateTypeDef]
    ChangeToken: str

class CreateWebACLResponseTypeDef(BaseModel):
    WebACL: WebACLTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebACLResponseTypeDef(BaseModel):
    WebACL: WebACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebACLRequestRequestTypeDef(BaseModel):
    WebACLId: str
    ChangeToken: str
    Updates: Optional[Sequence[WebACLUpdateTypeDef]] = None
    DefaultAction: Optional[WafActionTypeDef] = None

class CreateByteMatchSetResponseTypeDef(BaseModel):
    ByteMatchSet: ByteMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetByteMatchSetResponseTypeDef(BaseModel):
    ByteMatchSet: ByteMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateByteMatchSetRequestRequestTypeDef(BaseModel):
    ByteMatchSetId: str
    ChangeToken: str
    Updates: Sequence[ByteMatchSetUpdateTypeDef]

class CreateRegexMatchSetResponseTypeDef(BaseModel):
    RegexMatchSet: RegexMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegexMatchSetResponseTypeDef(BaseModel):
    RegexMatchSet: RegexMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexMatchSetRequestRequestTypeDef(BaseModel):
    RegexMatchSetId: str
    Updates: Sequence[RegexMatchSetUpdateTypeDef]
    ChangeToken: str

class CreateSizeConstraintSetResponseTypeDef(BaseModel):
    SizeConstraintSet: SizeConstraintSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSizeConstraintSetResponseTypeDef(BaseModel):
    SizeConstraintSet: SizeConstraintSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSizeConstraintSetRequestRequestTypeDef(BaseModel):
    SizeConstraintSetId: str
    ChangeToken: str
    Updates: Sequence[SizeConstraintSetUpdateTypeDef]

class CreateSqlInjectionMatchSetResponseTypeDef(BaseModel):
    SqlInjectionMatchSet: SqlInjectionMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSqlInjectionMatchSetResponseTypeDef(BaseModel):
    SqlInjectionMatchSet: SqlInjectionMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSqlInjectionMatchSetRequestRequestTypeDef(BaseModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str
    Updates: Sequence[SqlInjectionMatchSetUpdateTypeDef]

class CreateXssMatchSetResponseTypeDef(BaseModel):
    XssMatchSet: XssMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetXssMatchSetResponseTypeDef(BaseModel):
    XssMatchSet: XssMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateXssMatchSetRequestRequestTypeDef(BaseModel):
    XssMatchSetId: str
    ChangeToken: str
    Updates: Sequence[XssMatchSetUpdateTypeDef]

class GetSampledRequestsResponseTypeDef(BaseModel):
    SampledRequests: List[SampledHTTPRequestTypeDef]
    PopulationSize: int
    TimeWindow: TimeWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


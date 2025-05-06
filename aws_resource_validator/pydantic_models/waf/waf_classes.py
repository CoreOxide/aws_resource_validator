from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.waf.waf_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ExcludedRule(BaseValidatorModel):
    RuleId: str


class WafAction(BaseValidatorModel):
    Type: WafActionTypeType


class WafOverrideAction(BaseValidatorModel):
    Type: WafOverrideActionTypeType

Blob = Union[str, bytes, IO[Any], StreamingBody]


class ByteMatchSetSummary(BaseValidatorModel):
    ByteMatchSetId: str
    Name: str


class FieldToMatch(BaseValidatorModel):
    Type: MatchFieldTypeType
    Data: Optional[str] = None


class CreateByteMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateGeoMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class CreateIPSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CreateRegexMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class CreateRegexPatternSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class RegexPatternSet(BaseValidatorModel):
    RegexPatternSetId: str
    RegexPatternStrings: List[str]
    Name: Optional[str] = None


class RuleGroup(BaseValidatorModel):
    RuleGroupId: str
    Name: Optional[str] = None
    MetricName: Optional[str] = None


class CreateSizeConstraintSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class CreateSqlInjectionMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class CreateWebACLMigrationStackRequest(BaseValidatorModel):
    WebACLId: str
    S3BucketName: str
    IgnoreUnsupportedType: bool


class CreateXssMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class DeleteByteMatchSetRequest(BaseValidatorModel):
    ByteMatchSetId: str
    ChangeToken: str


class DeleteGeoMatchSetRequest(BaseValidatorModel):
    GeoMatchSetId: str
    ChangeToken: str


class DeleteIPSetRequest(BaseValidatorModel):
    IPSetId: str
    ChangeToken: str


class DeleteLoggingConfigurationRequest(BaseValidatorModel):
    ResourceArn: str


class DeletePermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DeleteRateBasedRuleRequest(BaseValidatorModel):
    RuleId: str
    ChangeToken: str


class DeleteRegexMatchSetRequest(BaseValidatorModel):
    RegexMatchSetId: str
    ChangeToken: str


class DeleteRegexPatternSetRequest(BaseValidatorModel):
    RegexPatternSetId: str
    ChangeToken: str


class DeleteRuleGroupRequest(BaseValidatorModel):
    RuleGroupId: str
    ChangeToken: str


class DeleteRuleRequest(BaseValidatorModel):
    RuleId: str
    ChangeToken: str


class DeleteSizeConstraintSetRequest(BaseValidatorModel):
    SizeConstraintSetId: str
    ChangeToken: str


class DeleteSqlInjectionMatchSetRequest(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str


class DeleteWebACLRequest(BaseValidatorModel):
    WebACLId: str
    ChangeToken: str


class DeleteXssMatchSetRequest(BaseValidatorModel):
    XssMatchSetId: str
    ChangeToken: str


class GeoMatchConstraint(BaseValidatorModel):
    Type: Literal['Country']
    Value: GeoMatchConstraintValueType


class GeoMatchSetSummary(BaseValidatorModel):
    GeoMatchSetId: str
    Name: str


class GetByteMatchSetRequest(BaseValidatorModel):
    ByteMatchSetId: str


class GetChangeTokenStatusRequest(BaseValidatorModel):
    ChangeToken: str


class GetGeoMatchSetRequest(BaseValidatorModel):
    GeoMatchSetId: str


class GetIPSetRequest(BaseValidatorModel):
    IPSetId: str


class GetLoggingConfigurationRequest(BaseValidatorModel):
    ResourceArn: str


class GetPermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetRateBasedRuleManagedKeysRequest(BaseValidatorModel):
    RuleId: str
    NextMarker: Optional[str] = None


class GetRateBasedRuleRequest(BaseValidatorModel):
    RuleId: str


class GetRegexMatchSetRequest(BaseValidatorModel):
    RegexMatchSetId: str


class GetRegexPatternSetRequest(BaseValidatorModel):
    RegexPatternSetId: str


class GetRuleGroupRequest(BaseValidatorModel):
    RuleGroupId: str


class GetRuleRequest(BaseValidatorModel):
    RuleId: str


class TimeWindowOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


class GetSizeConstraintSetRequest(BaseValidatorModel):
    SizeConstraintSetId: str


class GetSqlInjectionMatchSetRequest(BaseValidatorModel):
    SqlInjectionMatchSetId: str


class GetWebACLRequest(BaseValidatorModel):
    WebACLId: str


class GetXssMatchSetRequest(BaseValidatorModel):
    XssMatchSetId: str


class HTTPHeader(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class IPSetDescriptor(BaseValidatorModel):
    Type: IPSetDescriptorTypeType
    Value: str


class IPSetSummary(BaseValidatorModel):
    IPSetId: str
    Name: str


class ListActivatedRulesInRuleGroupRequest(BaseValidatorModel):
    RuleGroupId: Optional[str] = None
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListByteMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListGeoMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListIPSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListLoggingConfigurationsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListRateBasedRulesRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RuleSummary(BaseValidatorModel):
    RuleId: str
    Name: str


class ListRegexMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RegexMatchSetSummary(BaseValidatorModel):
    RegexMatchSetId: str
    Name: str


class ListRegexPatternSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RegexPatternSetSummary(BaseValidatorModel):
    RegexPatternSetId: str
    Name: str


class ListRuleGroupsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RuleGroupSummary(BaseValidatorModel):
    RuleGroupId: str
    Name: str


class ListRulesRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListSizeConstraintSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SizeConstraintSetSummary(BaseValidatorModel):
    SizeConstraintSetId: str
    Name: str


class ListSqlInjectionMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SqlInjectionMatchSetSummary(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    Name: str


class ListSubscribedRuleGroupsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SubscribedRuleGroupSummary(BaseValidatorModel):
    RuleGroupId: str
    Name: str
    MetricName: str


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListWebACLsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class WebACLSummary(BaseValidatorModel):
    WebACLId: str
    Name: str


class ListXssMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class XssMatchSetSummary(BaseValidatorModel):
    XssMatchSetId: str
    Name: str


class Predicate(BaseValidatorModel):
    Negated: bool
    Type: PredicateTypeType
    DataId: str


class PutPermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RegexPatternSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    RegexPatternString: str

Timestamp = Union[datetime, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class ActivatedRuleOutput(BaseValidatorModel):
    Priority: int
    RuleId: str
    Action: Optional[WafAction] = None
    OverrideAction: Optional[WafOverrideAction] = None
    Type: Optional[WafRuleTypeType] = None
    ExcludedRules: Optional[List[ExcludedRule]] = None


class ActivatedRule(BaseValidatorModel):
    Priority: int
    RuleId: str
    Action: Optional[WafAction] = None
    OverrideAction: Optional[WafOverrideAction] = None
    Type: Optional[WafRuleTypeType] = None
    ExcludedRules: Optional[List[ExcludedRule]] = None


class ByteMatchTupleOutput(BaseValidatorModel):
    FieldToMatch: FieldToMatch
    TargetString: bytes
    TextTransformation: TextTransformationType
    PositionalConstraint: PositionalConstraintType


class ByteMatchTuple(BaseValidatorModel):
    FieldToMatch: FieldToMatch
    TargetString: Blob
    TextTransformation: TextTransformationType
    PositionalConstraint: PositionalConstraintType


class LoggingConfigurationOutput(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatch]] = None


class LoggingConfiguration(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatch]] = None


class RegexMatchTuple(BaseValidatorModel):
    FieldToMatch: FieldToMatch
    TextTransformation: TextTransformationType
    RegexPatternSetId: str


class SizeConstraint(BaseValidatorModel):
    FieldToMatch: FieldToMatch
    TextTransformation: TextTransformationType
    ComparisonOperator: ComparisonOperatorType
    Size: int


class SqlInjectionMatchTuple(BaseValidatorModel):
    FieldToMatch: FieldToMatch
    TextTransformation: TextTransformationType


class XssMatchTuple(BaseValidatorModel):
    FieldToMatch: FieldToMatch
    TextTransformation: TextTransformationType


class CreateWebACLMigrationStackResponse(BaseValidatorModel):
    S3ObjectUrl: str
    ResponseMetadata: ResponseMetadata


class DeleteByteMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteGeoMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteIPSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteRateBasedRuleResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteRegexMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteRegexPatternSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteRuleGroupResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteRuleResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteSizeConstraintSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteSqlInjectionMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteWebACLResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class DeleteXssMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetChangeTokenResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetChangeTokenStatusResponse(BaseValidatorModel):
    ChangeTokenStatus: ChangeTokenStatusType
    ResponseMetadata: ResponseMetadata


class GetPermissionPolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetRateBasedRuleManagedKeysResponse(BaseValidatorModel):
    ManagedKeys: List[str]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ListByteMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    ByteMatchSets: List[ByteMatchSetSummary]
    ResponseMetadata: ResponseMetadata


class UpdateByteMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateGeoMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateIPSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateRateBasedRuleResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateRegexMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateRegexPatternSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateRuleGroupResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateRuleResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateSizeConstraintSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateSqlInjectionMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateWebACLResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class UpdateXssMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class CreateRateBasedRuleRequest(BaseValidatorModel):
    Name: str
    MetricName: str
    RateKey: Literal['IP']
    RateLimit: int
    ChangeToken: str
    Tags: Optional[List[Tag]] = None


class CreateRuleGroupRequest(BaseValidatorModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[List[Tag]] = None


class CreateRuleRequest(BaseValidatorModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[List[Tag]] = None


class CreateWebACLRequest(BaseValidatorModel):
    Name: str
    MetricName: str
    DefaultAction: WafAction
    ChangeToken: str
    Tags: Optional[List[Tag]] = None


class TagInfoForResource(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    TagList: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class CreateRegexPatternSetResponse(BaseValidatorModel):
    RegexPatternSet: RegexPatternSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetRegexPatternSetResponse(BaseValidatorModel):
    RegexPatternSet: RegexPatternSet
    ResponseMetadata: ResponseMetadata


class CreateRuleGroupResponse(BaseValidatorModel):
    RuleGroup: RuleGroup
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetRuleGroupResponse(BaseValidatorModel):
    RuleGroup: RuleGroup
    ResponseMetadata: ResponseMetadata


class GeoMatchSet(BaseValidatorModel):
    GeoMatchSetId: str
    GeoMatchConstraints: List[GeoMatchConstraint]
    Name: Optional[str] = None


class GeoMatchSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    GeoMatchConstraint: GeoMatchConstraint


class ListGeoMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    GeoMatchSets: List[GeoMatchSetSummary]
    ResponseMetadata: ResponseMetadata


class GetRateBasedRuleManagedKeysRequestPaginate(BaseValidatorModel):
    RuleId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListActivatedRulesInRuleGroupRequestPaginate(BaseValidatorModel):
    RuleGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListByteMatchSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGeoMatchSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIPSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLoggingConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRateBasedRulesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRegexMatchSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRegexPatternSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRuleGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRulesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSizeConstraintSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSqlInjectionMatchSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscribedRuleGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWebACLsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListXssMatchSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class HTTPRequest(BaseValidatorModel):
    ClientIP: Optional[str] = None
    Country: Optional[str] = None
    URI: Optional[str] = None
    Method: Optional[str] = None
    HTTPVersion: Optional[str] = None
    Headers: Optional[List[HTTPHeader]] = None


class IPSet(BaseValidatorModel):
    IPSetId: str
    IPSetDescriptors: List[IPSetDescriptor]
    Name: Optional[str] = None


class IPSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    IPSetDescriptor: IPSetDescriptor


class ListIPSetsResponse(BaseValidatorModel):
    NextMarker: str
    IPSets: List[IPSetSummary]
    ResponseMetadata: ResponseMetadata


class ListRateBasedRulesResponse(BaseValidatorModel):
    NextMarker: str
    Rules: List[RuleSummary]
    ResponseMetadata: ResponseMetadata


class ListRulesResponse(BaseValidatorModel):
    NextMarker: str
    Rules: List[RuleSummary]
    ResponseMetadata: ResponseMetadata


class ListRegexMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    RegexMatchSets: List[RegexMatchSetSummary]
    ResponseMetadata: ResponseMetadata


class ListRegexPatternSetsResponse(BaseValidatorModel):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummary]
    ResponseMetadata: ResponseMetadata


class ListRuleGroupsResponse(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[RuleGroupSummary]
    ResponseMetadata: ResponseMetadata


class ListSizeConstraintSetsResponse(BaseValidatorModel):
    NextMarker: str
    SizeConstraintSets: List[SizeConstraintSetSummary]
    ResponseMetadata: ResponseMetadata


class ListSqlInjectionMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    SqlInjectionMatchSets: List[SqlInjectionMatchSetSummary]
    ResponseMetadata: ResponseMetadata


class ListSubscribedRuleGroupsResponse(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[SubscribedRuleGroupSummary]
    ResponseMetadata: ResponseMetadata


class ListWebACLsResponse(BaseValidatorModel):
    NextMarker: str
    WebACLs: List[WebACLSummary]
    ResponseMetadata: ResponseMetadata


class ListXssMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    XssMatchSets: List[XssMatchSetSummary]
    ResponseMetadata: ResponseMetadata


class RateBasedRule(BaseValidatorModel):
    RuleId: str
    MatchPredicates: List[Predicate]
    RateKey: Literal['IP']
    RateLimit: int
    Name: Optional[str] = None
    MetricName: Optional[str] = None


class Rule(BaseValidatorModel):
    RuleId: str
    Predicates: List[Predicate]
    Name: Optional[str] = None
    MetricName: Optional[str] = None


class RuleUpdate(BaseValidatorModel):
    Action: ChangeActionType
    Predicate: Predicate


class UpdateRegexPatternSetRequest(BaseValidatorModel):
    RegexPatternSetId: str
    Updates: List[RegexPatternSetUpdate]
    ChangeToken: str


class TimeWindow(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp


class ListActivatedRulesInRuleGroupResponse(BaseValidatorModel):
    NextMarker: str
    ActivatedRules: List[ActivatedRuleOutput]
    ResponseMetadata: ResponseMetadata


class WebACL(BaseValidatorModel):
    WebACLId: str
    DefaultAction: WafAction
    Rules: List[ActivatedRuleOutput]
    Name: Optional[str] = None
    MetricName: Optional[str] = None
    WebACLArn: Optional[str] = None

ActivatedRuleUnion = Union[ActivatedRule, ActivatedRuleOutput]


class ByteMatchSet(BaseValidatorModel):
    ByteMatchSetId: str
    ByteMatchTuples: List[ByteMatchTupleOutput]
    Name: Optional[str] = None

ByteMatchTupleUnion = Union[ByteMatchTuple, ByteMatchTupleOutput]


class GetLoggingConfigurationResponse(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationOutput
    ResponseMetadata: ResponseMetadata


class ListLoggingConfigurationsResponse(BaseValidatorModel):
    LoggingConfigurations: List[LoggingConfigurationOutput]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class PutLoggingConfigurationResponse(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationOutput
    ResponseMetadata: ResponseMetadata

LoggingConfigurationUnion = Union[LoggingConfiguration, LoggingConfigurationOutput]


class RegexMatchSet(BaseValidatorModel):
    RegexMatchSetId: Optional[str] = None
    Name: Optional[str] = None
    RegexMatchTuples: Optional[List[RegexMatchTuple]] = None


class RegexMatchSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    RegexMatchTuple: RegexMatchTuple


class SizeConstraintSet(BaseValidatorModel):
    SizeConstraintSetId: str
    SizeConstraints: List[SizeConstraint]
    Name: Optional[str] = None


class SizeConstraintSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    SizeConstraint: SizeConstraint


class SqlInjectionMatchSet(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    SqlInjectionMatchTuples: List[SqlInjectionMatchTuple]
    Name: Optional[str] = None


class SqlInjectionMatchSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    SqlInjectionMatchTuple: SqlInjectionMatchTuple


class XssMatchSet(BaseValidatorModel):
    XssMatchSetId: str
    XssMatchTuples: List[XssMatchTuple]
    Name: Optional[str] = None


class XssMatchSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    XssMatchTuple: XssMatchTuple


class ListTagsForResourceResponse(BaseValidatorModel):
    NextMarker: str
    TagInfoForResource: TagInfoForResource
    ResponseMetadata: ResponseMetadata


class CreateGeoMatchSetResponse(BaseValidatorModel):
    GeoMatchSet: GeoMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetGeoMatchSetResponse(BaseValidatorModel):
    GeoMatchSet: GeoMatchSet
    ResponseMetadata: ResponseMetadata


class UpdateGeoMatchSetRequest(BaseValidatorModel):
    GeoMatchSetId: str
    ChangeToken: str
    Updates: List[GeoMatchSetUpdate]


class SampledHTTPRequest(BaseValidatorModel):
    Request: HTTPRequest
    Weight: int
    Timestamp: Optional[datetime] = None
    Action: Optional[str] = None
    RuleWithinRuleGroup: Optional[str] = None


class CreateIPSetResponse(BaseValidatorModel):
    IPSet: IPSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetIPSetResponse(BaseValidatorModel):
    IPSet: IPSet
    ResponseMetadata: ResponseMetadata


class UpdateIPSetRequest(BaseValidatorModel):
    IPSetId: str
    ChangeToken: str
    Updates: List[IPSetUpdate]


class CreateRateBasedRuleResponse(BaseValidatorModel):
    Rule: RateBasedRule
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetRateBasedRuleResponse(BaseValidatorModel):
    Rule: RateBasedRule
    ResponseMetadata: ResponseMetadata


class CreateRuleResponse(BaseValidatorModel):
    Rule: Rule
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetRuleResponse(BaseValidatorModel):
    Rule: Rule
    ResponseMetadata: ResponseMetadata


class UpdateRateBasedRuleRequest(BaseValidatorModel):
    RuleId: str
    ChangeToken: str
    Updates: List[RuleUpdate]
    RateLimit: int


class UpdateRuleRequest(BaseValidatorModel):
    RuleId: str
    ChangeToken: str
    Updates: List[RuleUpdate]

TimeWindowUnion = Union[TimeWindow, TimeWindowOutput]


class CreateWebACLResponse(BaseValidatorModel):
    WebACL: WebACL
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetWebACLResponse(BaseValidatorModel):
    WebACL: WebACL
    ResponseMetadata: ResponseMetadata


class RuleGroupUpdate(BaseValidatorModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleUnion


class WebACLUpdate(BaseValidatorModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleUnion


class CreateByteMatchSetResponse(BaseValidatorModel):
    ByteMatchSet: ByteMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetByteMatchSetResponse(BaseValidatorModel):
    ByteMatchSet: ByteMatchSet
    ResponseMetadata: ResponseMetadata


class ByteMatchSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    ByteMatchTuple: ByteMatchTupleUnion


class PutLoggingConfigurationRequest(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationUnion


class CreateRegexMatchSetResponse(BaseValidatorModel):
    RegexMatchSet: RegexMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetRegexMatchSetResponse(BaseValidatorModel):
    RegexMatchSet: RegexMatchSet
    ResponseMetadata: ResponseMetadata


class UpdateRegexMatchSetRequest(BaseValidatorModel):
    RegexMatchSetId: str
    Updates: List[RegexMatchSetUpdate]
    ChangeToken: str


class CreateSizeConstraintSetResponse(BaseValidatorModel):
    SizeConstraintSet: SizeConstraintSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetSizeConstraintSetResponse(BaseValidatorModel):
    SizeConstraintSet: SizeConstraintSet
    ResponseMetadata: ResponseMetadata


class UpdateSizeConstraintSetRequest(BaseValidatorModel):
    SizeConstraintSetId: str
    ChangeToken: str
    Updates: List[SizeConstraintSetUpdate]


class CreateSqlInjectionMatchSetResponse(BaseValidatorModel):
    SqlInjectionMatchSet: SqlInjectionMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetSqlInjectionMatchSetResponse(BaseValidatorModel):
    SqlInjectionMatchSet: SqlInjectionMatchSet
    ResponseMetadata: ResponseMetadata


class UpdateSqlInjectionMatchSetRequest(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str
    Updates: List[SqlInjectionMatchSetUpdate]


class CreateXssMatchSetResponse(BaseValidatorModel):
    XssMatchSet: XssMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetXssMatchSetResponse(BaseValidatorModel):
    XssMatchSet: XssMatchSet
    ResponseMetadata: ResponseMetadata


class UpdateXssMatchSetRequest(BaseValidatorModel):
    XssMatchSetId: str
    ChangeToken: str
    Updates: List[XssMatchSetUpdate]


class GetSampledRequestsResponse(BaseValidatorModel):
    SampledRequests: List[SampledHTTPRequest]
    PopulationSize: int
    TimeWindow: TimeWindowOutput
    ResponseMetadata: ResponseMetadata


class GetSampledRequestsRequest(BaseValidatorModel):
    WebAclId: str
    RuleId: str
    TimeWindow: TimeWindowUnion
    MaxItems: int


class UpdateRuleGroupRequest(BaseValidatorModel):
    RuleGroupId: str
    Updates: List[RuleGroupUpdate]
    ChangeToken: str


class UpdateWebACLRequest(BaseValidatorModel):
    WebACLId: str
    ChangeToken: str
    Updates: Optional[List[WebACLUpdate]] = None
    DefaultAction: Optional[WafAction] = None


class UpdateByteMatchSetRequest(BaseValidatorModel):
    ByteMatchSetId: str
    ChangeToken: str
    Updates: List[ByteMatchSetUpdate]
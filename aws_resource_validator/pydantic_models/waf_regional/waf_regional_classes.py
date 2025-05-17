from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.waf_regional.waf_regional_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ExcludedRule(BaseValidatorModel):
    RuleId: str


class WafAction(BaseValidatorModel):
    Type: WafActionTypeType


class WafOverrideAction(BaseValidatorModel):
    Type: WafOverrideActionTypeType


class AssociateWebACLRequest(BaseValidatorModel):
    WebACLId: str
    ResourceArn: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class ByteMatchSetSummary(BaseValidatorModel):
    ByteMatchSetId: str
    Name: str


class FieldToMatch(BaseValidatorModel):
    Type: MatchFieldTypeType
    Data: Optional[str] = None


# This class is the input for the 'create_byte_match_set' function.
class CreateByteMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_geo_match_set' function.
class CreateGeoMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


# This class is the input for the 'create_ip_set' function.
class CreateIPSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


# This class is the input for the 'create_regex_match_set' function.
class CreateRegexMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


# This class is the input for the 'create_regex_pattern_set' function.
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


# This class is the input for the 'create_size_constraint_set' function.
class CreateSizeConstraintSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


# This class is the input for the 'create_sql_injection_match_set' function.
class CreateSqlInjectionMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


# This class is the input for the 'create_web_acl_migration_stack' function.
class CreateWebACLMigrationStackRequest(BaseValidatorModel):
    WebACLId: str
    S3BucketName: str
    IgnoreUnsupportedType: bool


# This class is the input for the 'create_xss_match_set' function.
class CreateXssMatchSetRequest(BaseValidatorModel):
    Name: str
    ChangeToken: str


# This class is the input for the 'delete_byte_match_set' function.
class DeleteByteMatchSetRequest(BaseValidatorModel):
    ByteMatchSetId: str
    ChangeToken: str


# This class is the input for the 'delete_geo_match_set' function.
class DeleteGeoMatchSetRequest(BaseValidatorModel):
    GeoMatchSetId: str
    ChangeToken: str


# This class is the input for the 'delete_ip_set' function.
class DeleteIPSetRequest(BaseValidatorModel):
    IPSetId: str
    ChangeToken: str


class DeleteLoggingConfigurationRequest(BaseValidatorModel):
    ResourceArn: str


class DeletePermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'delete_rate_based_rule' function.
class DeleteRateBasedRuleRequest(BaseValidatorModel):
    RuleId: str
    ChangeToken: str


# This class is the input for the 'delete_regex_match_set' function.
class DeleteRegexMatchSetRequest(BaseValidatorModel):
    RegexMatchSetId: str
    ChangeToken: str


# This class is the input for the 'delete_regex_pattern_set' function.
class DeleteRegexPatternSetRequest(BaseValidatorModel):
    RegexPatternSetId: str
    ChangeToken: str


# This class is the input for the 'delete_rule_group' function.
class DeleteRuleGroupRequest(BaseValidatorModel):
    RuleGroupId: str
    ChangeToken: str


# This class is the input for the 'delete_rule' function.
class DeleteRuleRequest(BaseValidatorModel):
    RuleId: str
    ChangeToken: str


# This class is the input for the 'delete_size_constraint_set' function.
class DeleteSizeConstraintSetRequest(BaseValidatorModel):
    SizeConstraintSetId: str
    ChangeToken: str


# This class is the input for the 'delete_sql_injection_match_set' function.
class DeleteSqlInjectionMatchSetRequest(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str


# This class is the input for the 'delete_web_acl' function.
class DeleteWebACLRequest(BaseValidatorModel):
    WebACLId: str
    ChangeToken: str


# This class is the input for the 'delete_xss_match_set' function.
class DeleteXssMatchSetRequest(BaseValidatorModel):
    XssMatchSetId: str
    ChangeToken: str


class DisassociateWebACLRequest(BaseValidatorModel):
    ResourceArn: str


class GeoMatchConstraint(BaseValidatorModel):
    Type: Literal['Country']
    Value: GeoMatchConstraintValueType


class GeoMatchSetSummary(BaseValidatorModel):
    GeoMatchSetId: str
    Name: str


# This class is the input for the 'get_byte_match_set' function.
class GetByteMatchSetRequest(BaseValidatorModel):
    ByteMatchSetId: str


# This class is the input for the 'get_change_token_status' function.
class GetChangeTokenStatusRequest(BaseValidatorModel):
    ChangeToken: str


# This class is the input for the 'get_geo_match_set' function.
class GetGeoMatchSetRequest(BaseValidatorModel):
    GeoMatchSetId: str


# This class is the input for the 'get_ip_set' function.
class GetIPSetRequest(BaseValidatorModel):
    IPSetId: str


# This class is the input for the 'get_logging_configuration' function.
class GetLoggingConfigurationRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_permission_policy' function.
class GetPermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_rate_based_rule_managed_keys' function.
class GetRateBasedRuleManagedKeysRequest(BaseValidatorModel):
    RuleId: str
    NextMarker: Optional[str] = None


# This class is the input for the 'get_rate_based_rule' function.
class GetRateBasedRuleRequest(BaseValidatorModel):
    RuleId: str


# This class is the input for the 'get_regex_match_set' function.
class GetRegexMatchSetRequest(BaseValidatorModel):
    RegexMatchSetId: str


# This class is the input for the 'get_regex_pattern_set' function.
class GetRegexPatternSetRequest(BaseValidatorModel):
    RegexPatternSetId: str


# This class is the input for the 'get_rule_group' function.
class GetRuleGroupRequest(BaseValidatorModel):
    RuleGroupId: str


# This class is the input for the 'get_rule' function.
class GetRuleRequest(BaseValidatorModel):
    RuleId: str


class TimeWindowOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


# This class is the input for the 'get_size_constraint_set' function.
class GetSizeConstraintSetRequest(BaseValidatorModel):
    SizeConstraintSetId: str


# This class is the input for the 'get_sql_injection_match_set' function.
class GetSqlInjectionMatchSetRequest(BaseValidatorModel):
    SqlInjectionMatchSetId: str


# This class is the input for the 'get_web_acl_for_resource' function.
class GetWebACLForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class WebACLSummary(BaseValidatorModel):
    WebACLId: str
    Name: str


# This class is the input for the 'get_web_acl' function.
class GetWebACLRequest(BaseValidatorModel):
    WebACLId: str


# This class is the input for the 'get_xss_match_set' function.
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


# This class is the input for the 'list_activated_rules_in_rule_group' function.
class ListActivatedRulesInRuleGroupRequest(BaseValidatorModel):
    RuleGroupId: Optional[str] = None
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_byte_match_sets' function.
class ListByteMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_geo_match_sets' function.
class ListGeoMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_ip_sets' function.
class ListIPSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_logging_configurations' function.
class ListLoggingConfigurationsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_rate_based_rules' function.
class ListRateBasedRulesRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RuleSummary(BaseValidatorModel):
    RuleId: str
    Name: str


# This class is the input for the 'list_regex_match_sets' function.
class ListRegexMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RegexMatchSetSummary(BaseValidatorModel):
    RegexMatchSetId: str
    Name: str


# This class is the input for the 'list_regex_pattern_sets' function.
class ListRegexPatternSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RegexPatternSetSummary(BaseValidatorModel):
    RegexPatternSetId: str
    Name: str


# This class is the input for the 'list_resources_for_web_acl' function.
class ListResourcesForWebACLRequest(BaseValidatorModel):
    WebACLId: str
    ResourceType: Optional[ResourceTypeType] = None


# This class is the input for the 'list_rule_groups' function.
class ListRuleGroupsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RuleGroupSummary(BaseValidatorModel):
    RuleGroupId: str
    Name: str


# This class is the input for the 'list_rules' function.
class ListRulesRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_size_constraint_sets' function.
class ListSizeConstraintSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SizeConstraintSetSummary(BaseValidatorModel):
    SizeConstraintSetId: str
    Name: str


# This class is the input for the 'list_sql_injection_match_sets' function.
class ListSqlInjectionMatchSetsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SqlInjectionMatchSetSummary(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    Name: str


# This class is the input for the 'list_subscribed_rule_groups' function.
class ListSubscribedRuleGroupsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SubscribedRuleGroupSummary(BaseValidatorModel):
    RuleGroupId: str
    Name: str
    MetricName: str


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_web_acls' function.
class ListWebACLsRequest(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_xss_match_sets' function.
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


# This class is the output for the 'create_web_acl_migration_stack' function.
class CreateWebACLMigrationStackResponse(BaseValidatorModel):
    S3ObjectUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_byte_match_set' function.
class DeleteByteMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_geo_match_set' function.
class DeleteGeoMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ip_set' function.
class DeleteIPSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_rate_based_rule' function.
class DeleteRateBasedRuleResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_regex_match_set' function.
class DeleteRegexMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_regex_pattern_set' function.
class DeleteRegexPatternSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_rule_group' function.
class DeleteRuleGroupResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_rule' function.
class DeleteRuleResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_size_constraint_set' function.
class DeleteSizeConstraintSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_sql_injection_match_set' function.
class DeleteSqlInjectionMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_web_acl' function.
class DeleteWebACLResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_xss_match_set' function.
class DeleteXssMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


class GetChangeTokenResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_change_token_status' function.
class GetChangeTokenStatusResponse(BaseValidatorModel):
    ChangeTokenStatus: ChangeTokenStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_permission_policy' function.
class GetPermissionPolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rate_based_rule_managed_keys' function.
class GetRateBasedRuleManagedKeysResponse(BaseValidatorModel):
    ManagedKeys: List[str]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_byte_match_sets' function.
class ListByteMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    ByteMatchSets: List[ByteMatchSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resources_for_web_acl' function.
class ListResourcesForWebACLResponse(BaseValidatorModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_byte_match_set' function.
class UpdateByteMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_geo_match_set' function.
class UpdateGeoMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ip_set' function.
class UpdateIPSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_rate_based_rule' function.
class UpdateRateBasedRuleResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_regex_match_set' function.
class UpdateRegexMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_regex_pattern_set' function.
class UpdateRegexPatternSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_rule_group' function.
class UpdateRuleGroupResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_rule' function.
class UpdateRuleResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_size_constraint_set' function.
class UpdateSizeConstraintSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_sql_injection_match_set' function.
class UpdateSqlInjectionMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_web_acl' function.
class UpdateWebACLResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_xss_match_set' function.
class UpdateXssMatchSetResponse(BaseValidatorModel):
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_rate_based_rule' function.
class CreateRateBasedRuleRequest(BaseValidatorModel):
    Name: str
    MetricName: str
    RateKey: Literal['IP']
    RateLimit: int
    ChangeToken: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_rule_group' function.
class CreateRuleGroupRequest(BaseValidatorModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_rule' function.
class CreateRuleRequest(BaseValidatorModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_web_acl' function.
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


# This class is the output for the 'create_regex_pattern_set' function.
class CreateRegexPatternSetResponse(BaseValidatorModel):
    RegexPatternSet: RegexPatternSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_regex_pattern_set' function.
class GetRegexPatternSetResponse(BaseValidatorModel):
    RegexPatternSet: RegexPatternSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_rule_group' function.
class CreateRuleGroupResponse(BaseValidatorModel):
    RuleGroup: RuleGroup
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rule_group' function.
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


# This class is the output for the 'list_geo_match_sets' function.
class ListGeoMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    GeoMatchSets: List[GeoMatchSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_web_acl_for_resource' function.
class GetWebACLForResourceResponse(BaseValidatorModel):
    WebACLSummary: WebACLSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_web_acls' function.
class ListWebACLsResponse(BaseValidatorModel):
    NextMarker: str
    WebACLs: List[WebACLSummary]
    ResponseMetadata: ResponseMetadata


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


# This class is the output for the 'list_ip_sets' function.
class ListIPSetsResponse(BaseValidatorModel):
    NextMarker: str
    IPSets: List[IPSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_rate_based_rules' function.
class ListRateBasedRulesResponse(BaseValidatorModel):
    NextMarker: str
    Rules: List[RuleSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_rules' function.
class ListRulesResponse(BaseValidatorModel):
    NextMarker: str
    Rules: List[RuleSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_regex_match_sets' function.
class ListRegexMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    RegexMatchSets: List[RegexMatchSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_regex_pattern_sets' function.
class ListRegexPatternSetsResponse(BaseValidatorModel):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_rule_groups' function.
class ListRuleGroupsResponse(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[RuleGroupSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_size_constraint_sets' function.
class ListSizeConstraintSetsResponse(BaseValidatorModel):
    NextMarker: str
    SizeConstraintSets: List[SizeConstraintSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_sql_injection_match_sets' function.
class ListSqlInjectionMatchSetsResponse(BaseValidatorModel):
    NextMarker: str
    SqlInjectionMatchSets: List[SqlInjectionMatchSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_subscribed_rule_groups' function.
class ListSubscribedRuleGroupsResponse(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[SubscribedRuleGroupSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_xss_match_sets' function.
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


# This class is the input for the 'update_regex_pattern_set' function.
class UpdateRegexPatternSetRequest(BaseValidatorModel):
    RegexPatternSetId: str
    Updates: List[RegexPatternSetUpdate]
    ChangeToken: str


class TimeWindow(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp


# This class is the output for the 'list_activated_rules_in_rule_group' function.
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


# This class is the output for the 'get_logging_configuration' function.
class GetLoggingConfigurationResponse(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_logging_configurations' function.
class ListLoggingConfigurationsResponse(BaseValidatorModel):
    LoggingConfigurations: List[LoggingConfigurationOutput]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_logging_configuration' function.
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


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    NextMarker: str
    TagInfoForResource: TagInfoForResource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_geo_match_set' function.
class CreateGeoMatchSetResponse(BaseValidatorModel):
    GeoMatchSet: GeoMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_geo_match_set' function.
class GetGeoMatchSetResponse(BaseValidatorModel):
    GeoMatchSet: GeoMatchSet
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_geo_match_set' function.
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


# This class is the output for the 'create_ip_set' function.
class CreateIPSetResponse(BaseValidatorModel):
    IPSet: IPSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ip_set' function.
class GetIPSetResponse(BaseValidatorModel):
    IPSet: IPSet
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_ip_set' function.
class UpdateIPSetRequest(BaseValidatorModel):
    IPSetId: str
    ChangeToken: str
    Updates: List[IPSetUpdate]


# This class is the output for the 'create_rate_based_rule' function.
class CreateRateBasedRuleResponse(BaseValidatorModel):
    Rule: RateBasedRule
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rate_based_rule' function.
class GetRateBasedRuleResponse(BaseValidatorModel):
    Rule: RateBasedRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_rule' function.
class CreateRuleResponse(BaseValidatorModel):
    Rule: Rule
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rule' function.
class GetRuleResponse(BaseValidatorModel):
    Rule: Rule
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_rate_based_rule' function.
class UpdateRateBasedRuleRequest(BaseValidatorModel):
    RuleId: str
    ChangeToken: str
    Updates: List[RuleUpdate]
    RateLimit: int


# This class is the input for the 'update_rule' function.
class UpdateRuleRequest(BaseValidatorModel):
    RuleId: str
    ChangeToken: str
    Updates: List[RuleUpdate]

TimeWindowUnion = Union[TimeWindow, TimeWindowOutput]


# This class is the output for the 'create_web_acl' function.
class CreateWebACLResponse(BaseValidatorModel):
    WebACL: WebACL
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_web_acl' function.
class GetWebACLResponse(BaseValidatorModel):
    WebACL: WebACL
    ResponseMetadata: ResponseMetadata


class RuleGroupUpdate(BaseValidatorModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleUnion


class WebACLUpdate(BaseValidatorModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleUnion


# This class is the output for the 'create_byte_match_set' function.
class CreateByteMatchSetResponse(BaseValidatorModel):
    ByteMatchSet: ByteMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_byte_match_set' function.
class GetByteMatchSetResponse(BaseValidatorModel):
    ByteMatchSet: ByteMatchSet
    ResponseMetadata: ResponseMetadata


class ByteMatchSetUpdate(BaseValidatorModel):
    Action: ChangeActionType
    ByteMatchTuple: ByteMatchTupleUnion


# This class is the input for the 'put_logging_configuration' function.
class PutLoggingConfigurationRequest(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationUnion


# This class is the output for the 'create_regex_match_set' function.
class CreateRegexMatchSetResponse(BaseValidatorModel):
    RegexMatchSet: RegexMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_regex_match_set' function.
class GetRegexMatchSetResponse(BaseValidatorModel):
    RegexMatchSet: RegexMatchSet
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_regex_match_set' function.
class UpdateRegexMatchSetRequest(BaseValidatorModel):
    RegexMatchSetId: str
    Updates: List[RegexMatchSetUpdate]
    ChangeToken: str


# This class is the output for the 'create_size_constraint_set' function.
class CreateSizeConstraintSetResponse(BaseValidatorModel):
    SizeConstraintSet: SizeConstraintSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_size_constraint_set' function.
class GetSizeConstraintSetResponse(BaseValidatorModel):
    SizeConstraintSet: SizeConstraintSet
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_size_constraint_set' function.
class UpdateSizeConstraintSetRequest(BaseValidatorModel):
    SizeConstraintSetId: str
    ChangeToken: str
    Updates: List[SizeConstraintSetUpdate]


# This class is the output for the 'create_sql_injection_match_set' function.
class CreateSqlInjectionMatchSetResponse(BaseValidatorModel):
    SqlInjectionMatchSet: SqlInjectionMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sql_injection_match_set' function.
class GetSqlInjectionMatchSetResponse(BaseValidatorModel):
    SqlInjectionMatchSet: SqlInjectionMatchSet
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_sql_injection_match_set' function.
class UpdateSqlInjectionMatchSetRequest(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str
    Updates: List[SqlInjectionMatchSetUpdate]


# This class is the output for the 'create_xss_match_set' function.
class CreateXssMatchSetResponse(BaseValidatorModel):
    XssMatchSet: XssMatchSet
    ChangeToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_xss_match_set' function.
class GetXssMatchSetResponse(BaseValidatorModel):
    XssMatchSet: XssMatchSet
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_xss_match_set' function.
class UpdateXssMatchSetRequest(BaseValidatorModel):
    XssMatchSetId: str
    ChangeToken: str
    Updates: List[XssMatchSetUpdate]


# This class is the output for the 'get_sampled_requests' function.
class GetSampledRequestsResponse(BaseValidatorModel):
    SampledRequests: List[SampledHTTPRequest]
    PopulationSize: int
    TimeWindow: TimeWindowOutput
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'get_sampled_requests' function.
class GetSampledRequestsRequest(BaseValidatorModel):
    WebAclId: str
    RuleId: str
    TimeWindow: TimeWindowUnion
    MaxItems: int


# This class is the input for the 'update_rule_group' function.
class UpdateRuleGroupRequest(BaseValidatorModel):
    RuleGroupId: str
    Updates: List[RuleGroupUpdate]
    ChangeToken: str


# This class is the input for the 'update_web_acl' function.
class UpdateWebACLRequest(BaseValidatorModel):
    WebACLId: str
    ChangeToken: str
    Updates: Optional[List[WebACLUpdate]] = None
    DefaultAction: Optional[WafAction] = None


# This class is the input for the 'update_byte_match_set' function.
class UpdateByteMatchSetRequest(BaseValidatorModel):
    ByteMatchSetId: str
    ChangeToken: str
    Updates: List[ByteMatchSetUpdate]
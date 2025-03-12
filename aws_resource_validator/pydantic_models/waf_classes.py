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
from aws_resource_validator.pydantic_models.waf_constants import *

class ExcludedRuleTypeDef(BaseValidatorModel):
    RuleId: str


class ByteMatchSetSummaryTypeDef(BaseValidatorModel):
    ByteMatchSetId: str
    Name: str


class CreateByteMatchSetRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateGeoMatchSetRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str


class CreateIPSetRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CreateRegexMatchSetRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str


class CreateRegexPatternSetRequestTypeDef(BaseValidatorModel):
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


class CreateSizeConstraintSetRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str


class CreateSqlInjectionMatchSetRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str


class CreateWebACLMigrationStackRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    S3BucketName: str
    IgnoreUnsupportedType: bool


class CreateXssMatchSetRequestTypeDef(BaseValidatorModel):
    Name: str
    ChangeToken: str


class DeleteByteMatchSetRequestTypeDef(BaseValidatorModel):
    ByteMatchSetId: str
    ChangeToken: str


class DeleteGeoMatchSetRequestTypeDef(BaseValidatorModel):
    GeoMatchSetId: str
    ChangeToken: str


class DeleteIPSetRequestTypeDef(BaseValidatorModel):
    IPSetId: str
    ChangeToken: str


class DeleteLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DeletePermissionPolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DeleteRateBasedRuleRequestTypeDef(BaseValidatorModel):
    RuleId: str
    ChangeToken: str


class DeleteRegexMatchSetRequestTypeDef(BaseValidatorModel):
    RegexMatchSetId: str
    ChangeToken: str


class DeleteRegexPatternSetRequestTypeDef(BaseValidatorModel):
    RegexPatternSetId: str
    ChangeToken: str


class DeleteRuleGroupRequestTypeDef(BaseValidatorModel):
    RuleGroupId: str
    ChangeToken: str


class DeleteRuleRequestTypeDef(BaseValidatorModel):
    RuleId: str
    ChangeToken: str


class DeleteSizeConstraintSetRequestTypeDef(BaseValidatorModel):
    SizeConstraintSetId: str
    ChangeToken: str


class DeleteSqlInjectionMatchSetRequestTypeDef(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    ChangeToken: str


class DeleteWebACLRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    ChangeToken: str


class DeleteXssMatchSetRequestTypeDef(BaseValidatorModel):
    XssMatchSetId: str
    ChangeToken: str


class GeoMatchSetSummaryTypeDef(BaseValidatorModel):
    GeoMatchSetId: str
    Name: str


class GetByteMatchSetRequestTypeDef(BaseValidatorModel):
    ByteMatchSetId: str


class GetChangeTokenStatusRequestTypeDef(BaseValidatorModel):
    ChangeToken: str


class GetGeoMatchSetRequestTypeDef(BaseValidatorModel):
    GeoMatchSetId: str


class GetIPSetRequestTypeDef(BaseValidatorModel):
    IPSetId: str


class GetLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class GetPermissionPolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetRateBasedRuleManagedKeysRequestTypeDef(BaseValidatorModel):
    RuleId: str
    NextMarker: Optional[str] = None


class GetRateBasedRuleRequestTypeDef(BaseValidatorModel):
    RuleId: str


class GetRegexMatchSetRequestTypeDef(BaseValidatorModel):
    RegexMatchSetId: str


class GetRegexPatternSetRequestTypeDef(BaseValidatorModel):
    RegexPatternSetId: str


class GetRuleGroupRequestTypeDef(BaseValidatorModel):
    RuleGroupId: str


class GetRuleRequestTypeDef(BaseValidatorModel):
    RuleId: str


class TimeWindowOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


class GetSizeConstraintSetRequestTypeDef(BaseValidatorModel):
    SizeConstraintSetId: str


class GetSqlInjectionMatchSetRequestTypeDef(BaseValidatorModel):
    SqlInjectionMatchSetId: str


class GetWebACLRequestTypeDef(BaseValidatorModel):
    WebACLId: str


class GetXssMatchSetRequestTypeDef(BaseValidatorModel):
    XssMatchSetId: str


class HTTPHeaderTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class IPSetSummaryTypeDef(BaseValidatorModel):
    IPSetId: str
    Name: str


class ListActivatedRulesInRuleGroupRequestTypeDef(BaseValidatorModel):
    RuleGroupId: Optional[str] = None
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListByteMatchSetsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListGeoMatchSetsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListIPSetsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListLoggingConfigurationsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListRateBasedRulesRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RuleSummaryTypeDef(BaseValidatorModel):
    RuleId: str
    Name: str


class ListRegexMatchSetsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RegexMatchSetSummaryTypeDef(BaseValidatorModel):
    RegexMatchSetId: str
    Name: str


class ListRegexPatternSetsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RegexPatternSetSummaryTypeDef(BaseValidatorModel):
    RegexPatternSetId: str
    Name: str


class ListRuleGroupsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class RuleGroupSummaryTypeDef(BaseValidatorModel):
    RuleGroupId: str
    Name: str


class ListRulesRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListSizeConstraintSetsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SizeConstraintSetSummaryTypeDef(BaseValidatorModel):
    SizeConstraintSetId: str
    Name: str


class ListSqlInjectionMatchSetsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SqlInjectionMatchSetSummaryTypeDef(BaseValidatorModel):
    SqlInjectionMatchSetId: str
    Name: str


class ListSubscribedRuleGroupsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class SubscribedRuleGroupSummaryTypeDef(BaseValidatorModel):
    RuleGroupId: str
    Name: str
    MetricName: str


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListWebACLsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class WebACLSummaryTypeDef(BaseValidatorModel):
    WebACLId: str
    Name: str


class ListXssMatchSetsRequestTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class XssMatchSetSummaryTypeDef(BaseValidatorModel):
    XssMatchSetId: str
    Name: str


class PutPermissionPolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RegexPatternSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    RegexPatternString: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class FieldToMatchTypeDef(BaseValidatorModel):
    pass


class ByteMatchTupleOutputTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchTypeDef
    TargetString: bytes
    TextTransformation: TextTransformationType
    PositionalConstraint: PositionalConstraintType


class BlobTypeDef(BaseValidatorModel):
    pass


class ByteMatchTupleTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchTypeDef
    TargetString: BlobTypeDef
    TextTransformation: TextTransformationType
    PositionalConstraint: PositionalConstraintType


class LoggingConfigurationOutputTypeDef(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatchTypeDef]] = None


class LoggingConfigurationTypeDef(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: Sequence[str]
    RedactedFields: Optional[Sequence[FieldToMatchTypeDef]] = None


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


class CreateRateBasedRuleRequestTypeDef(BaseValidatorModel):
    Name: str
    MetricName: str
    RateKey: Literal["IP"]
    RateLimit: int
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateRuleGroupRequestTypeDef(BaseValidatorModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateRuleRequestTypeDef(BaseValidatorModel):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class WafActionTypeDef(BaseValidatorModel):
    pass


class CreateWebACLRequestTypeDef(BaseValidatorModel):
    Name: str
    MetricName: str
    DefaultAction: WafActionTypeDef
    ChangeToken: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagInfoForResourceTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    TagList: Optional[List[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
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


class GeoMatchConstraintTypeDef(BaseValidatorModel):
    pass


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


class GetRateBasedRuleManagedKeysRequestPaginateTypeDef(BaseValidatorModel):
    RuleId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListActivatedRulesInRuleGroupRequestPaginateTypeDef(BaseValidatorModel):
    RuleGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListByteMatchSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGeoMatchSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIPSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLoggingConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRateBasedRulesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRegexMatchSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRegexPatternSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRuleGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRulesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSizeConstraintSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSqlInjectionMatchSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscribedRuleGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWebACLsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListXssMatchSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class HTTPRequestTypeDef(BaseValidatorModel):
    ClientIP: Optional[str] = None
    Country: Optional[str] = None
    URI: Optional[str] = None
    Method: Optional[str] = None
    HTTPVersion: Optional[str] = None
    Headers: Optional[List[HTTPHeaderTypeDef]] = None


class IPSetDescriptorTypeDef(BaseValidatorModel):
    pass


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


class ListWebACLsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    WebACLs: List[WebACLSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListXssMatchSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    XssMatchSets: List[XssMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PredicateTypeDef(BaseValidatorModel):
    pass


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


class UpdateRegexPatternSetRequestTypeDef(BaseValidatorModel):
    RegexPatternSetId: str
    Updates: Sequence[RegexPatternSetUpdateTypeDef]
    ChangeToken: str


class TimestampTypeDef(BaseValidatorModel):
    pass


class TimeWindowTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef


class ActivatedRuleOutputTypeDef(BaseValidatorModel):
    pass


class ListActivatedRulesInRuleGroupResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    ActivatedRules: List[ActivatedRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class WebACLTypeDef(BaseValidatorModel):
    WebACLId: str
    DefaultAction: WafActionTypeDef
    Rules: List[ActivatedRuleOutputTypeDef]
    Name: Optional[str] = None
    MetricName: Optional[str] = None
    WebACLArn: Optional[str] = None


class ByteMatchSetTypeDef(BaseValidatorModel):
    ByteMatchSetId: str
    ByteMatchTuples: List[ByteMatchTupleOutputTypeDef]
    Name: Optional[str] = None


class GetLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLoggingConfigurationsResponseTypeDef(BaseValidatorModel):
    LoggingConfigurations: List[LoggingConfigurationOutputTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationOutputTypeDef
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


class UpdateGeoMatchSetRequestTypeDef(BaseValidatorModel):
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


class UpdateIPSetRequestTypeDef(BaseValidatorModel):
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


class UpdateRateBasedRuleRequestTypeDef(BaseValidatorModel):
    RuleId: str
    ChangeToken: str
    Updates: Sequence[RuleUpdateTypeDef]
    RateLimit: int


class UpdateRuleRequestTypeDef(BaseValidatorModel):
    RuleId: str
    ChangeToken: str
    Updates: Sequence[RuleUpdateTypeDef]


class CreateWebACLResponseTypeDef(BaseValidatorModel):
    WebACL: WebACLTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetWebACLResponseTypeDef(BaseValidatorModel):
    WebACL: WebACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ActivatedRuleUnionTypeDef(BaseValidatorModel):
    pass


class RuleGroupUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleUnionTypeDef


class WebACLUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleUnionTypeDef


class CreateByteMatchSetResponseTypeDef(BaseValidatorModel):
    ByteMatchSet: ByteMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetByteMatchSetResponseTypeDef(BaseValidatorModel):
    ByteMatchSet: ByteMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ByteMatchTupleUnionTypeDef(BaseValidatorModel):
    pass


class ByteMatchSetUpdateTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    ByteMatchTuple: ByteMatchTupleUnionTypeDef


class LoggingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationUnionTypeDef


class CreateRegexMatchSetResponseTypeDef(BaseValidatorModel):
    RegexMatchSet: RegexMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRegexMatchSetResponseTypeDef(BaseValidatorModel):
    RegexMatchSet: RegexMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRegexMatchSetRequestTypeDef(BaseValidatorModel):
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


class UpdateSizeConstraintSetRequestTypeDef(BaseValidatorModel):
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


class UpdateSqlInjectionMatchSetRequestTypeDef(BaseValidatorModel):
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


class UpdateXssMatchSetRequestTypeDef(BaseValidatorModel):
    XssMatchSetId: str
    ChangeToken: str
    Updates: Sequence[XssMatchSetUpdateTypeDef]


class GetSampledRequestsResponseTypeDef(BaseValidatorModel):
    SampledRequests: List[SampledHTTPRequestTypeDef]
    PopulationSize: int
    TimeWindow: TimeWindowOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TimeWindowUnionTypeDef(BaseValidatorModel):
    pass


class GetSampledRequestsRequestTypeDef(BaseValidatorModel):
    WebAclId: str
    RuleId: str
    TimeWindow: TimeWindowUnionTypeDef
    MaxItems: int


class UpdateRuleGroupRequestTypeDef(BaseValidatorModel):
    RuleGroupId: str
    Updates: Sequence[RuleGroupUpdateTypeDef]
    ChangeToken: str


class UpdateWebACLRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    ChangeToken: str
    Updates: Optional[Sequence[WebACLUpdateTypeDef]] = None
    DefaultAction: Optional[WafActionTypeDef] = None


class UpdateByteMatchSetRequestTypeDef(BaseValidatorModel):
    ByteMatchSetId: str
    ChangeToken: str
    Updates: Sequence[ByteMatchSetUpdateTypeDef]



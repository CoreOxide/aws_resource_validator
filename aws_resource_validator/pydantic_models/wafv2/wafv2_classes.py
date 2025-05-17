from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.wafv2.wafv2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class APIKeySummary(BaseValidatorModel):
    TokenDomains: Optional[List[str]] = None
    APIKey: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Version: Optional[int] = None


class AWSManagedRulesBotControlRuleSet(BaseValidatorModel):
    InspectionLevel: InspectionLevelType
    EnableMachineLearning: Optional[bool] = None


class ActionCondition(BaseValidatorModel):
    Action: ActionValueType


class AddressField(BaseValidatorModel):
    Identifier: str


class AndStatementOutput(BaseValidatorModel):
    Statements: List[Dict[str, Any]]


class AndStatement(BaseValidatorModel):
    Statements: List[Dict[str, Any]]


class AssociateWebACLRequest(BaseValidatorModel):
    WebACLArn: str
    ResourceArn: str


class RequestBodyAssociatedResourceTypeConfig(BaseValidatorModel):
    DefaultSizeInspectionLimit: SizeInspectionLimitType

Blob = Union[str, bytes, IO[Any], StreamingBody]


class Body(BaseValidatorModel):
    OversizeHandling: Optional[OversizeHandlingType] = None


class TextTransformation(BaseValidatorModel):
    Priority: int
    Type: TextTransformationTypeType


class ImmunityTimeProperty(BaseValidatorModel):
    ImmunityTime: int


class CaptchaResponse(BaseValidatorModel):
    ResponseCode: Optional[int] = None
    SolveTimestamp: Optional[int] = None
    FailureReason: Optional[FailureReasonType] = None


class ChallengeResponse(BaseValidatorModel):
    ResponseCode: Optional[int] = None
    SolveTimestamp: Optional[int] = None
    FailureReason: Optional[FailureReasonType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LabelNameCondition(BaseValidatorModel):
    LabelName: str


class CookieMatchPatternOutput(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedCookies: Optional[List[str]] = None
    ExcludedCookies: Optional[List[str]] = None


class CookieMatchPattern(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedCookies: Optional[List[str]] = None
    ExcludedCookies: Optional[List[str]] = None


# This class is the input for the 'create_api_key' function.
class CreateAPIKeyRequest(BaseValidatorModel):
    Scope: ScopeType
    TokenDomains: List[str]


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class IPSetSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None


class Regex(BaseValidatorModel):
    RegexString: Optional[str] = None


class RegexPatternSetSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None


class CustomResponseBody(BaseValidatorModel):
    ContentType: ResponseContentTypeType
    Content: str


class VisibilityConfig(BaseValidatorModel):
    SampledRequestsEnabled: bool
    CloudWatchMetricsEnabled: bool
    MetricName: str


class RuleGroupSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None


class WebACLSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None


class CustomHTTPHeader(BaseValidatorModel):
    Name: str
    Value: str


class FieldToProtectOutput(BaseValidatorModel):
    FieldType: FieldToProtectTypeType
    FieldKeys: Optional[List[str]] = None


class FieldToProtect(BaseValidatorModel):
    FieldType: FieldToProtectTypeType
    FieldKeys: Optional[List[str]] = None


class DeleteAPIKeyRequest(BaseValidatorModel):
    Scope: ScopeType
    APIKey: str


# This class is the input for the 'delete_firewall_manager_rule_groups' function.
class DeleteFirewallManagerRuleGroupsRequest(BaseValidatorModel):
    WebACLArn: str
    WebACLLockToken: str


class DeleteIPSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str


class DeleteLoggingConfigurationRequest(BaseValidatorModel):
    ResourceArn: str
    LogType: Optional[Literal['WAF_LOGS']] = None
    LogScope: Optional[LogScopeType] = None


class DeletePermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DeleteRegexPatternSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str


class DeleteRuleGroupRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str


class DeleteWebACLRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str


# This class is the input for the 'describe_all_managed_products' function.
class DescribeAllManagedProductsRequest(BaseValidatorModel):
    Scope: ScopeType


class ManagedProductDescriptor(BaseValidatorModel):
    VendorName: Optional[str] = None
    ManagedRuleSetName: Optional[str] = None
    ProductId: Optional[str] = None
    ProductLink: Optional[str] = None
    ProductTitle: Optional[str] = None
    ProductDescription: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    IsVersioningSupported: Optional[bool] = None
    IsAdvancedManagedRuleSet: Optional[bool] = None


# This class is the input for the 'describe_managed_products_by_vendor' function.
class DescribeManagedProductsByVendorRequest(BaseValidatorModel):
    VendorName: str
    Scope: ScopeType


# This class is the input for the 'describe_managed_rule_group' function.
class DescribeManagedRuleGroupRequest(BaseValidatorModel):
    VendorName: str
    Name: str
    Scope: ScopeType
    VersionName: Optional[str] = None


class LabelSummary(BaseValidatorModel):
    Name: Optional[str] = None


class DisassociateWebACLRequest(BaseValidatorModel):
    ResourceArn: str


class EmailField(BaseValidatorModel):
    Identifier: str


class ExcludedRule(BaseValidatorModel):
    Name: str


class HeaderOrder(BaseValidatorModel):
    OversizeHandling: OversizeHandlingType


class JA3Fingerprint(BaseValidatorModel):
    FallbackBehavior: FallbackBehaviorType


class JA4Fingerprint(BaseValidatorModel):
    FallbackBehavior: FallbackBehaviorType


class SingleHeader(BaseValidatorModel):
    Name: str


class SingleQueryArgument(BaseValidatorModel):
    Name: str


class ForwardedIPConfig(BaseValidatorModel):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType


# This class is the input for the 'generate_mobile_sdk_release_url' function.
class GenerateMobileSdkReleaseUrlRequest(BaseValidatorModel):
    Platform: PlatformType
    ReleaseVersion: str


# This class is the input for the 'get_decrypted_api_key' function.
class GetDecryptedAPIKeyRequest(BaseValidatorModel):
    Scope: ScopeType
    APIKey: str


# This class is the input for the 'get_ip_set' function.
class GetIPSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


class IPSet(BaseValidatorModel):
    Name: str
    Id: str
    ARN: str
    IPAddressVersion: IPAddressVersionType
    Addresses: List[str]
    Description: Optional[str] = None


# This class is the input for the 'get_logging_configuration' function.
class GetLoggingConfigurationRequest(BaseValidatorModel):
    ResourceArn: str
    LogType: Optional[Literal['WAF_LOGS']] = None
    LogScope: Optional[LogScopeType] = None


# This class is the input for the 'get_managed_rule_set' function.
class GetManagedRuleSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


# This class is the input for the 'get_mobile_sdk_release' function.
class GetMobileSdkReleaseRequest(BaseValidatorModel):
    Platform: PlatformType
    ReleaseVersion: str


# This class is the input for the 'get_permission_policy' function.
class GetPermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_rate_based_statement_managed_keys' function.
class GetRateBasedStatementManagedKeysRequest(BaseValidatorModel):
    Scope: ScopeType
    WebACLName: str
    WebACLId: str
    RuleName: str
    RuleGroupRuleName: Optional[str] = None


class RateBasedStatementManagedKeysIPSet(BaseValidatorModel):
    IPAddressVersion: Optional[IPAddressVersionType] = None
    Addresses: Optional[List[str]] = None


# This class is the input for the 'get_regex_pattern_set' function.
class GetRegexPatternSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


# This class is the input for the 'get_rule_group' function.
class GetRuleGroupRequest(BaseValidatorModel):
    Name: Optional[str] = None
    Scope: Optional[ScopeType] = None
    Id: Optional[str] = None
    ARN: Optional[str] = None


class TimeWindowOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


# This class is the input for the 'get_web_acl_for_resource' function.
class GetWebACLForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_web_acl' function.
class GetWebACLRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


class HTTPHeader(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class HeaderMatchPatternOutput(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedHeaders: Optional[List[str]] = None
    ExcludedHeaders: Optional[List[str]] = None


class HeaderMatchPattern(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedHeaders: Optional[List[str]] = None
    ExcludedHeaders: Optional[List[str]] = None


class IPSetForwardedIPConfig(BaseValidatorModel):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType
    Position: ForwardedIPPositionType


class JsonMatchPatternOutput(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedPaths: Optional[List[str]] = None


class JsonMatchPattern(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedPaths: Optional[List[str]] = None


class LabelMatchStatement(BaseValidatorModel):
    Scope: LabelMatchScopeType
    Key: str


class Label(BaseValidatorModel):
    Name: str


# This class is the input for the 'list_api_keys' function.
class ListAPIKeysRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_available_managed_rule_group_versions' function.
class ListAvailableManagedRuleGroupVersionsRequest(BaseValidatorModel):
    VendorName: str
    Name: str
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ManagedRuleGroupVersion(BaseValidatorModel):
    Name: Optional[str] = None
    LastUpdateTimestamp: Optional[datetime] = None


# This class is the input for the 'list_available_managed_rule_groups' function.
class ListAvailableManagedRuleGroupsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ManagedRuleGroupSummary(BaseValidatorModel):
    VendorName: Optional[str] = None
    Name: Optional[str] = None
    VersioningSupported: Optional[bool] = None
    Description: Optional[str] = None


# This class is the input for the 'list_ip_sets' function.
class ListIPSetsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_logging_configurations' function.
class ListLoggingConfigurationsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None
    LogScope: Optional[LogScopeType] = None


# This class is the input for the 'list_managed_rule_sets' function.
class ListManagedRuleSetsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ManagedRuleSetSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None
    LabelNamespace: Optional[str] = None


# This class is the input for the 'list_mobile_sdk_releases' function.
class ListMobileSdkReleasesRequest(BaseValidatorModel):
    Platform: PlatformType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ReleaseSummary(BaseValidatorModel):
    ReleaseVersion: Optional[str] = None
    Timestamp: Optional[datetime] = None


# This class is the input for the 'list_regex_pattern_sets' function.
class ListRegexPatternSetsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_resources_for_web_acl' function.
class ListResourcesForWebACLRequest(BaseValidatorModel):
    WebACLArn: str
    ResourceType: Optional[ResourceTypeType] = None


# This class is the input for the 'list_rule_groups' function.
class ListRuleGroupsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_web_acls' function.
class ListWebACLsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class PasswordField(BaseValidatorModel):
    Identifier: str


class UsernameField(BaseValidatorModel):
    Identifier: str


class ManagedRuleSetVersion(BaseValidatorModel):
    AssociatedRuleGroupArn: Optional[str] = None
    Capacity: Optional[int] = None
    ForecastedLifetime: Optional[int] = None
    PublishTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    ExpiryTimestamp: Optional[datetime] = None


class NotStatementOutput(BaseValidatorModel):
    Statement: Dict[str, Any]


class NotStatement(BaseValidatorModel):
    Statement: Dict[str, Any]


class OrStatementOutput(BaseValidatorModel):
    Statements: List[Dict[str, Any]]


class OrStatement(BaseValidatorModel):
    Statements: List[Dict[str, Any]]


class PhoneNumberField(BaseValidatorModel):
    Identifier: str


class VersionToPublish(BaseValidatorModel):
    AssociatedRuleGroupArn: Optional[str] = None
    ForecastedLifetime: Optional[int] = None


class PutPermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RateLimitJA3Fingerprint(BaseValidatorModel):
    FallbackBehavior: FallbackBehaviorType


class RateLimitJA4Fingerprint(BaseValidatorModel):
    FallbackBehavior: FallbackBehaviorType


class RateLimitLabelNamespace(BaseValidatorModel):
    Namespace: str


class ResponseInspectionBodyContainsOutput(BaseValidatorModel):
    SuccessStrings: List[str]
    FailureStrings: List[str]


class ResponseInspectionBodyContains(BaseValidatorModel):
    SuccessStrings: List[str]
    FailureStrings: List[str]


class ResponseInspectionHeaderOutput(BaseValidatorModel):
    Name: str
    SuccessValues: List[str]
    FailureValues: List[str]


class ResponseInspectionHeader(BaseValidatorModel):
    Name: str
    SuccessValues: List[str]
    FailureValues: List[str]


class ResponseInspectionJsonOutput(BaseValidatorModel):
    Identifier: str
    SuccessValues: List[str]
    FailureValues: List[str]


class ResponseInspectionJson(BaseValidatorModel):
    Identifier: str
    SuccessValues: List[str]
    FailureValues: List[str]


class ResponseInspectionStatusCodeOutput(BaseValidatorModel):
    SuccessCodes: List[int]
    FailureCodes: List[int]


class ResponseInspectionStatusCode(BaseValidatorModel):
    SuccessCodes: List[int]
    FailureCodes: List[int]

Timestamp = Union[datetime, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_ip_set' function.
class UpdateIPSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    Addresses: List[str]
    LockToken: str
    Description: Optional[str] = None

AndStatementUnion = Union[AndStatement, AndStatementOutput]


class AssociationConfigOutput(BaseValidatorModel):
    RequestBody: Optional[Dict[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfig]] = None


class AssociationConfig(BaseValidatorModel):
    RequestBody: Optional[Dict[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfig]] = None


class RateLimitCookieOutput(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitCookie(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitHeaderOutput(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitHeader(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitQueryArgumentOutput(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitQueryArgument(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitQueryStringOutput(BaseValidatorModel):
    TextTransformations: List[TextTransformation]


class RateLimitQueryString(BaseValidatorModel):
    TextTransformations: List[TextTransformation]


class RateLimitUriPathOutput(BaseValidatorModel):
    TextTransformations: List[TextTransformation]


class RateLimitUriPath(BaseValidatorModel):
    TextTransformations: List[TextTransformation]


class CaptchaConfig(BaseValidatorModel):
    ImmunityTimeProperty: Optional[ImmunityTimeProperty] = None


class ChallengeConfig(BaseValidatorModel):
    ImmunityTimeProperty: Optional[ImmunityTimeProperty] = None


# This class is the output for the 'check_capacity' function.
class CheckCapacityResponse(BaseValidatorModel):
    Capacity: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_api_key' function.
class CreateAPIKeyResponse(BaseValidatorModel):
    APIKey: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_firewall_manager_rule_groups' function.
class DeleteFirewallManagerRuleGroupsResponse(BaseValidatorModel):
    NextWebACLLockToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'generate_mobile_sdk_release_url' function.
class GenerateMobileSdkReleaseUrlResponse(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_decrypted_api_key' function.
class GetDecryptedAPIKeyResponse(BaseValidatorModel):
    TokenDomains: List[str]
    CreationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_permission_policy' function.
class GetPermissionPolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_api_keys' function.
class ListAPIKeysResponse(BaseValidatorModel):
    NextMarker: str
    APIKeySummaries: List[APIKeySummary]
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resources_for_web_acl' function.
class ListResourcesForWebACLResponse(BaseValidatorModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_managed_rule_set_versions' function.
class PutManagedRuleSetVersionsResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ip_set' function.
class UpdateIPSetResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_managed_rule_set_version_expiry_date' function.
class UpdateManagedRuleSetVersionExpiryDateResponse(BaseValidatorModel):
    ExpiringVersion: str
    ExpiryTimestamp: datetime
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_regex_pattern_set' function.
class UpdateRegexPatternSetResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_rule_group' function.
class UpdateRuleGroupResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_web_acl' function.
class UpdateWebACLResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


class Condition(BaseValidatorModel):
    ActionCondition: Optional[ActionCondition] = None
    LabelNameCondition: Optional[LabelNameCondition] = None


class CookiesOutput(BaseValidatorModel):
    MatchPattern: CookieMatchPatternOutput
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

CookieMatchPatternUnion = Union[CookieMatchPattern, CookieMatchPatternOutput]


# This class is the input for the 'create_ip_set' function.
class CreateIPSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    IPAddressVersion: IPAddressVersionType
    Addresses: List[str]
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class MobileSdkRelease(BaseValidatorModel):
    ReleaseVersion: Optional[str] = None
    Timestamp: Optional[datetime] = None
    ReleaseNotes: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagInfoForResource(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    TagList: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the output for the 'create_ip_set' function.
class CreateIPSetResponse(BaseValidatorModel):
    Summary: IPSetSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_ip_sets' function.
class ListIPSetsResponse(BaseValidatorModel):
    NextMarker: str
    IPSets: List[IPSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_regex_pattern_set' function.
class CreateRegexPatternSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    RegularExpressionList: List[Regex]
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class RegexPatternSet(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    ARN: Optional[str] = None
    Description: Optional[str] = None
    RegularExpressionList: Optional[List[Regex]] = None


# This class is the input for the 'update_regex_pattern_set' function.
class UpdateRegexPatternSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    RegularExpressionList: List[Regex]
    LockToken: str
    Description: Optional[str] = None


# This class is the output for the 'create_regex_pattern_set' function.
class CreateRegexPatternSetResponse(BaseValidatorModel):
    Summary: RegexPatternSetSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_regex_pattern_sets' function.
class ListRegexPatternSetsResponse(BaseValidatorModel):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_rule_group' function.
class CreateRuleGroupResponse(BaseValidatorModel):
    Summary: RuleGroupSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_rule_groups' function.
class ListRuleGroupsResponse(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[RuleGroupSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_web_acl' function.
class CreateWebACLResponse(BaseValidatorModel):
    Summary: WebACLSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_web_acls' function.
class ListWebACLsResponse(BaseValidatorModel):
    NextMarker: str
    WebACLs: List[WebACLSummary]
    ResponseMetadata: ResponseMetadata


class CustomRequestHandlingOutput(BaseValidatorModel):
    InsertHeaders: List[CustomHTTPHeader]


class CustomRequestHandling(BaseValidatorModel):
    InsertHeaders: List[CustomHTTPHeader]


class CustomResponseOutput(BaseValidatorModel):
    ResponseCode: int
    CustomResponseBodyKey: Optional[str] = None
    ResponseHeaders: Optional[List[CustomHTTPHeader]] = None


class CustomResponse(BaseValidatorModel):
    ResponseCode: int
    CustomResponseBodyKey: Optional[str] = None
    ResponseHeaders: Optional[List[CustomHTTPHeader]] = None


class DataProtectionOutput(BaseValidatorModel):
    Field: FieldToProtectOutput
    Action: DataProtectionActionType
    ExcludeRuleMatchDetails: Optional[bool] = None
    ExcludeRateBasedDetails: Optional[bool] = None


class DataProtection(BaseValidatorModel):
    Field: FieldToProtect
    Action: DataProtectionActionType
    ExcludeRuleMatchDetails: Optional[bool] = None
    ExcludeRateBasedDetails: Optional[bool] = None


# This class is the output for the 'describe_all_managed_products' function.
class DescribeAllManagedProductsResponse(BaseValidatorModel):
    ManagedProducts: List[ManagedProductDescriptor]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_managed_products_by_vendor' function.
class DescribeManagedProductsByVendorResponse(BaseValidatorModel):
    ManagedProducts: List[ManagedProductDescriptor]
    ResponseMetadata: ResponseMetadata


class GeoMatchStatementOutput(BaseValidatorModel):
    CountryCodes: Optional[List[CountryCodeType]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfig] = None


class GeoMatchStatement(BaseValidatorModel):
    CountryCodes: Optional[List[CountryCodeType]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfig] = None


# This class is the output for the 'get_ip_set' function.
class GetIPSetResponse(BaseValidatorModel):
    IPSet: IPSet
    LockToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rate_based_statement_managed_keys' function.
class GetRateBasedStatementManagedKeysResponse(BaseValidatorModel):
    ManagedKeysIPV4: RateBasedStatementManagedKeysIPSet
    ManagedKeysIPV6: RateBasedStatementManagedKeysIPSet
    ResponseMetadata: ResponseMetadata


class HTTPRequest(BaseValidatorModel):
    ClientIP: Optional[str] = None
    Country: Optional[str] = None
    URI: Optional[str] = None
    Method: Optional[str] = None
    HTTPVersion: Optional[str] = None
    Headers: Optional[List[HTTPHeader]] = None


class HeadersOutput(BaseValidatorModel):
    MatchPattern: HeaderMatchPatternOutput
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

HeaderMatchPatternUnion = Union[HeaderMatchPattern, HeaderMatchPatternOutput]


class IPSetReferenceStatement(BaseValidatorModel):
    ARN: str
    IPSetForwardedIPConfig: Optional[IPSetForwardedIPConfig] = None


class JsonBodyOutput(BaseValidatorModel):
    MatchPattern: JsonMatchPatternOutput
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehaviorType] = None
    OversizeHandling: Optional[OversizeHandlingType] = None

JsonMatchPatternUnion = Union[JsonMatchPattern, JsonMatchPatternOutput]


# This class is the output for the 'list_available_managed_rule_group_versions' function.
class ListAvailableManagedRuleGroupVersionsResponse(BaseValidatorModel):
    NextMarker: str
    Versions: List[ManagedRuleGroupVersion]
    CurrentDefaultVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_available_managed_rule_groups' function.
class ListAvailableManagedRuleGroupsResponse(BaseValidatorModel):
    NextMarker: str
    ManagedRuleGroups: List[ManagedRuleGroupSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_managed_rule_sets' function.
class ListManagedRuleSetsResponse(BaseValidatorModel):
    NextMarker: str
    ManagedRuleSets: List[ManagedRuleSetSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_mobile_sdk_releases' function.
class ListMobileSdkReleasesResponse(BaseValidatorModel):
    ReleaseSummaries: List[ReleaseSummary]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class RequestInspection(BaseValidatorModel):
    PayloadType: PayloadTypeType
    UsernameField: UsernameField
    PasswordField: PasswordField


class ManagedRuleSet(BaseValidatorModel):
    Name: str
    Id: str
    ARN: str
    Description: Optional[str] = None
    PublishedVersions: Optional[Dict[str, ManagedRuleSetVersion]] = None
    RecommendedVersion: Optional[str] = None
    LabelNamespace: Optional[str] = None

NotStatementUnion = Union[NotStatement, NotStatementOutput]

OrStatementUnion = Union[OrStatement, OrStatementOutput]


class RequestInspectionACFPOutput(BaseValidatorModel):
    PayloadType: PayloadTypeType
    UsernameField: Optional[UsernameField] = None
    PasswordField: Optional[PasswordField] = None
    EmailField: Optional[EmailField] = None
    PhoneNumberFields: Optional[List[PhoneNumberField]] = None
    AddressFields: Optional[List[AddressField]] = None


class RequestInspectionACFP(BaseValidatorModel):
    PayloadType: PayloadTypeType
    UsernameField: Optional[UsernameField] = None
    PasswordField: Optional[PasswordField] = None
    EmailField: Optional[EmailField] = None
    PhoneNumberFields: Optional[List[PhoneNumberField]] = None
    AddressFields: Optional[List[AddressField]] = None


# This class is the input for the 'put_managed_rule_set_versions' function.
class PutManagedRuleSetVersionsRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    RecommendedVersion: Optional[str] = None
    VersionsToPublish: Optional[Dict[str, VersionToPublish]] = None

ResponseInspectionBodyContainsUnion = Union[ResponseInspectionBodyContains, ResponseInspectionBodyContainsOutput]

ResponseInspectionHeaderUnion = Union[ResponseInspectionHeader, ResponseInspectionHeaderOutput]

ResponseInspectionJsonUnion = Union[ResponseInspectionJson, ResponseInspectionJsonOutput]


class ResponseInspectionOutput(BaseValidatorModel):
    StatusCode: Optional[ResponseInspectionStatusCodeOutput] = None
    Header: Optional[ResponseInspectionHeaderOutput] = None
    BodyContains: Optional[ResponseInspectionBodyContainsOutput] = None
    Json: Optional[ResponseInspectionJsonOutput] = None

ResponseInspectionStatusCodeUnion = Union[ResponseInspectionStatusCode, ResponseInspectionStatusCodeOutput]


class TimeWindow(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp


# This class is the input for the 'update_managed_rule_set_version_expiry_date' function.
class UpdateManagedRuleSetVersionExpiryDateRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    VersionToExpire: str
    ExpiryTimestamp: Timestamp

AssociationConfigUnion = Union[AssociationConfig, AssociationConfigOutput]

RateLimitCookieUnion = Union[RateLimitCookie, RateLimitCookieOutput]

RateLimitHeaderUnion = Union[RateLimitHeader, RateLimitHeaderOutput]

RateLimitQueryArgumentUnion = Union[RateLimitQueryArgument, RateLimitQueryArgumentOutput]

RateLimitQueryStringUnion = Union[RateLimitQueryString, RateLimitQueryStringOutput]


class RateBasedStatementCustomKeyOutput(BaseValidatorModel):
    Header: Optional[RateLimitHeaderOutput] = None
    Cookie: Optional[RateLimitCookieOutput] = None
    QueryArgument: Optional[RateLimitQueryArgumentOutput] = None
    QueryString: Optional[RateLimitQueryStringOutput] = None
    HTTPMethod: Optional[Dict[str, Any]] = None
    ForwardedIP: Optional[Dict[str, Any]] = None
    IP: Optional[Dict[str, Any]] = None
    LabelNamespace: Optional[RateLimitLabelNamespace] = None
    UriPath: Optional[RateLimitUriPathOutput] = None
    JA3Fingerprint: Optional[RateLimitJA3Fingerprint] = None
    JA4Fingerprint: Optional[RateLimitJA4Fingerprint] = None

RateLimitUriPathUnion = Union[RateLimitUriPath, RateLimitUriPathOutput]


class FilterOutput(BaseValidatorModel):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: List[Condition]


class Filter(BaseValidatorModel):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: List[Condition]


class Cookies(BaseValidatorModel):
    MatchPattern: CookieMatchPatternUnion
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType


# This class is the output for the 'get_mobile_sdk_release' function.
class GetMobileSdkReleaseResponse(BaseValidatorModel):
    MobileSdkRelease: MobileSdkRelease
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    NextMarker: str
    TagInfoForResource: TagInfoForResource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_regex_pattern_set' function.
class GetRegexPatternSetResponse(BaseValidatorModel):
    RegexPatternSet: RegexPatternSet
    LockToken: str
    ResponseMetadata: ResponseMetadata


class AllowActionOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutput] = None


class CaptchaActionOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutput] = None


class ChallengeActionOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutput] = None


class CountActionOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutput] = None

CustomRequestHandlingUnion = Union[CustomRequestHandling, CustomRequestHandlingOutput]


class BlockActionOutput(BaseValidatorModel):
    CustomResponse: Optional[CustomResponseOutput] = None

CustomResponseUnion = Union[CustomResponse, CustomResponseOutput]


class DataProtectionConfigOutput(BaseValidatorModel):
    DataProtections: List[DataProtectionOutput]


class DataProtectionConfig(BaseValidatorModel):
    DataProtections: List[DataProtection]

GeoMatchStatementUnion = Union[GeoMatchStatement, GeoMatchStatementOutput]


class SampledHTTPRequest(BaseValidatorModel):
    Request: HTTPRequest
    Weight: int
    Timestamp: Optional[datetime] = None
    Action: Optional[str] = None
    RuleNameWithinRuleGroup: Optional[str] = None
    RequestHeadersInserted: Optional[List[HTTPHeader]] = None
    ResponseCodeSent: Optional[int] = None
    Labels: Optional[List[Label]] = None
    CaptchaResponse: Optional[CaptchaResponse] = None
    ChallengeResponse: Optional[ChallengeResponse] = None
    OverriddenAction: Optional[str] = None


class Headers(BaseValidatorModel):
    MatchPattern: HeaderMatchPatternUnion
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType


class FieldToMatchOutput(BaseValidatorModel):
    SingleHeader: Optional[SingleHeader] = None
    SingleQueryArgument: Optional[SingleQueryArgument] = None
    AllQueryArguments: Optional[Dict[str, Any]] = None
    UriPath: Optional[Dict[str, Any]] = None
    QueryString: Optional[Dict[str, Any]] = None
    Body: Optional[Body] = None
    Method: Optional[Dict[str, Any]] = None
    JsonBody: Optional[JsonBodyOutput] = None
    Headers: Optional[HeadersOutput] = None
    Cookies: Optional[CookiesOutput] = None
    HeaderOrder: Optional[HeaderOrder] = None
    JA3Fingerprint: Optional[JA3Fingerprint] = None
    JA4Fingerprint: Optional[JA4Fingerprint] = None


class JsonBody(BaseValidatorModel):
    MatchPattern: JsonMatchPatternUnion
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehaviorType] = None
    OversizeHandling: Optional[OversizeHandlingType] = None


# This class is the output for the 'get_managed_rule_set' function.
class GetManagedRuleSetResponse(BaseValidatorModel):
    ManagedRuleSet: ManagedRuleSet
    LockToken: str
    ResponseMetadata: ResponseMetadata

RequestInspectionACFPUnion = Union[RequestInspectionACFP, RequestInspectionACFPOutput]


class AWSManagedRulesACFPRuleSetOutput(BaseValidatorModel):
    CreationPath: str
    RegistrationPagePath: str
    RequestInspection: RequestInspectionACFPOutput
    ResponseInspection: Optional[ResponseInspectionOutput] = None
    EnableRegexInPath: Optional[bool] = None


class AWSManagedRulesATPRuleSetOutput(BaseValidatorModel):
    LoginPath: str
    RequestInspection: Optional[RequestInspection] = None
    ResponseInspection: Optional[ResponseInspectionOutput] = None
    EnableRegexInPath: Optional[bool] = None


class ResponseInspection(BaseValidatorModel):
    StatusCode: Optional[ResponseInspectionStatusCodeUnion] = None
    Header: Optional[ResponseInspectionHeaderUnion] = None
    BodyContains: Optional[ResponseInspectionBodyContainsUnion] = None
    Json: Optional[ResponseInspectionJsonUnion] = None

TimeWindowUnion = Union[TimeWindow, TimeWindowOutput]


class RateBasedStatementOutput(BaseValidatorModel):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: Optional[int] = None
    ScopeDownStatement: Optional[Dict[str, Any]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfig] = None
    CustomKeys: Optional[List[RateBasedStatementCustomKeyOutput]] = None


class RateBasedStatementCustomKey(BaseValidatorModel):
    Header: Optional[RateLimitHeaderUnion] = None
    Cookie: Optional[RateLimitCookieUnion] = None
    QueryArgument: Optional[RateLimitQueryArgumentUnion] = None
    QueryString: Optional[RateLimitQueryStringUnion] = None
    HTTPMethod: Optional[Dict[str, Any]] = None
    ForwardedIP: Optional[Dict[str, Any]] = None
    IP: Optional[Dict[str, Any]] = None
    LabelNamespace: Optional[RateLimitLabelNamespace] = None
    UriPath: Optional[RateLimitUriPathUnion] = None
    JA3Fingerprint: Optional[RateLimitJA3Fingerprint] = None
    JA4Fingerprint: Optional[RateLimitJA4Fingerprint] = None


class LoggingFilterOutput(BaseValidatorModel):
    Filters: List[FilterOutput]
    DefaultBehavior: FilterBehaviorType


class LoggingFilter(BaseValidatorModel):
    Filters: List[Filter]
    DefaultBehavior: FilterBehaviorType

CookiesUnion = Union[Cookies, CookiesOutput]


class OverrideActionOutput(BaseValidatorModel):
    Count: Optional[CountActionOutput] = None
    None_: Optional[Dict[str, Any]] = None


class AllowAction(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingUnion] = None


class CaptchaAction(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingUnion] = None


class ChallengeAction(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingUnion] = None


class CountAction(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingUnion] = None


class DefaultActionOutput(BaseValidatorModel):
    Block: Optional[BlockActionOutput] = None
    Allow: Optional[AllowActionOutput] = None


class RuleActionOutput(BaseValidatorModel):
    Block: Optional[BlockActionOutput] = None
    Allow: Optional[AllowActionOutput] = None
    Count: Optional[CountActionOutput] = None
    Captcha: Optional[CaptchaActionOutput] = None
    Challenge: Optional[ChallengeActionOutput] = None


class BlockAction(BaseValidatorModel):
    CustomResponse: Optional[CustomResponseUnion] = None

DataProtectionConfigUnion = Union[DataProtectionConfig, DataProtectionConfigOutput]


# This class is the output for the 'get_sampled_requests' function.
class GetSampledRequestsResponse(BaseValidatorModel):
    SampledRequests: List[SampledHTTPRequest]
    PopulationSize: int
    TimeWindow: TimeWindowOutput
    ResponseMetadata: ResponseMetadata

HeadersUnion = Union[Headers, HeadersOutput]


class ByteMatchStatementOutput(BaseValidatorModel):
    SearchString: bytes
    FieldToMatch: FieldToMatchOutput
    TextTransformations: List[TextTransformation]
    PositionalConstraint: PositionalConstraintType


class RegexMatchStatementOutput(BaseValidatorModel):
    RegexString: str
    FieldToMatch: FieldToMatchOutput
    TextTransformations: List[TextTransformation]


class RegexPatternSetReferenceStatementOutput(BaseValidatorModel):
    ARN: str
    FieldToMatch: FieldToMatchOutput
    TextTransformations: List[TextTransformation]


class SizeConstraintStatementOutput(BaseValidatorModel):
    FieldToMatch: FieldToMatchOutput
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: List[TextTransformation]


class SqliMatchStatementOutput(BaseValidatorModel):
    FieldToMatch: FieldToMatchOutput
    TextTransformations: List[TextTransformation]
    SensitivityLevel: Optional[SensitivityLevelType] = None


class XssMatchStatementOutput(BaseValidatorModel):
    FieldToMatch: FieldToMatchOutput
    TextTransformations: List[TextTransformation]

JsonBodyUnion = Union[JsonBody, JsonBodyOutput]


class ManagedRuleGroupConfigOutput(BaseValidatorModel):
    LoginPath: Optional[str] = None
    PayloadType: Optional[PayloadTypeType] = None
    UsernameField: Optional[UsernameField] = None
    PasswordField: Optional[PasswordField] = None
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSet] = None
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSetOutput] = None
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSetOutput] = None

ResponseInspectionUnion = Union[ResponseInspection, ResponseInspectionOutput]


# This class is the input for the 'get_sampled_requests' function.
class GetSampledRequestsRequest(BaseValidatorModel):
    WebAclArn: str
    RuleMetricName: str
    Scope: ScopeType
    TimeWindow: TimeWindowUnion
    MaxItems: int

RateBasedStatementCustomKeyUnion = Union[RateBasedStatementCustomKey, RateBasedStatementCustomKeyOutput]


class LoggingConfigurationOutput(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatchOutput]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LoggingFilter: Optional[LoggingFilterOutput] = None
    LogType: Optional[Literal['WAF_LOGS']] = None
    LogScope: Optional[LogScopeType] = None

AllowActionUnion = Union[AllowAction, AllowActionOutput]

CaptchaActionUnion = Union[CaptchaAction, CaptchaActionOutput]

ChallengeActionUnion = Union[ChallengeAction, ChallengeActionOutput]

CountActionUnion = Union[CountAction, CountActionOutput]


class RuleActionOverrideOutput(BaseValidatorModel):
    Name: str
    ActionToUse: RuleActionOutput


class RuleSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Action: Optional[RuleActionOutput] = None

BlockActionUnion = Union[BlockAction, BlockActionOutput]


class DefaultAction(BaseValidatorModel):
    Block: Optional[BlockAction] = None
    Allow: Optional[AllowAction] = None


class FieldToMatch(BaseValidatorModel):
    SingleHeader: Optional[SingleHeader] = None
    SingleQueryArgument: Optional[SingleQueryArgument] = None
    AllQueryArguments: Optional[Dict[str, Any]] = None
    UriPath: Optional[Dict[str, Any]] = None
    QueryString: Optional[Dict[str, Any]] = None
    Body: Optional[Body] = None
    Method: Optional[Dict[str, Any]] = None
    JsonBody: Optional[JsonBodyUnion] = None
    Headers: Optional[HeadersUnion] = None
    Cookies: Optional[CookiesUnion] = None
    HeaderOrder: Optional[HeaderOrder] = None
    JA3Fingerprint: Optional[JA3Fingerprint] = None
    JA4Fingerprint: Optional[JA4Fingerprint] = None


class AWSManagedRulesACFPRuleSet(BaseValidatorModel):
    CreationPath: str
    RegistrationPagePath: str
    RequestInspection: RequestInspectionACFPUnion
    ResponseInspection: Optional[ResponseInspectionUnion] = None
    EnableRegexInPath: Optional[bool] = None


class AWSManagedRulesATPRuleSet(BaseValidatorModel):
    LoginPath: str
    RequestInspection: Optional[RequestInspection] = None
    ResponseInspection: Optional[ResponseInspectionUnion] = None
    EnableRegexInPath: Optional[bool] = None


class RateBasedStatement(BaseValidatorModel):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: Optional[int] = None
    ScopeDownStatement: Optional[Dict[str, Any]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfig] = None
    CustomKeys: Optional[List[RateBasedStatementCustomKeyUnion]] = None


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


class OverrideAction(BaseValidatorModel):
    Count: Optional[CountActionUnion] = None
    None_: Optional[Dict[str, Any]] = None


class ManagedRuleGroupStatementOutput(BaseValidatorModel):
    VendorName: str
    Name: str
    Version: Optional[str] = None
    ExcludedRules: Optional[List[ExcludedRule]] = None
    ScopeDownStatement: Optional[Dict[str, Any]] = None
    ManagedRuleGroupConfigs: Optional[List[ManagedRuleGroupConfigOutput]] = None
    RuleActionOverrides: Optional[List[RuleActionOverrideOutput]] = None


class RuleGroupReferenceStatementOutput(BaseValidatorModel):
    ARN: str
    ExcludedRules: Optional[List[ExcludedRule]] = None
    RuleActionOverrides: Optional[List[RuleActionOverrideOutput]] = None


# This class is the output for the 'describe_managed_rule_group' function.
class DescribeManagedRuleGroupResponse(BaseValidatorModel):
    VersionName: str
    SnsTopicArn: str
    Capacity: int
    Rules: List[RuleSummary]
    LabelNamespace: str
    AvailableLabels: List[LabelSummary]
    ConsumedLabels: List[LabelSummary]
    ResponseMetadata: ResponseMetadata


class RuleAction(BaseValidatorModel):
    Block: Optional[BlockActionUnion] = None
    Allow: Optional[AllowActionUnion] = None
    Count: Optional[CountActionUnion] = None
    Captcha: Optional[CaptchaActionUnion] = None
    Challenge: Optional[ChallengeActionUnion] = None

DefaultActionUnion = Union[DefaultAction, DefaultActionOutput]

FieldToMatchUnion = Union[FieldToMatch, FieldToMatchOutput]


class LoggingConfiguration(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatch]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LoggingFilter: Optional[LoggingFilter] = None
    LogType: Optional[Literal['WAF_LOGS']] = None
    LogScope: Optional[LogScopeType] = None

AWSManagedRulesACFPRuleSetUnion = Union[AWSManagedRulesACFPRuleSet, AWSManagedRulesACFPRuleSetOutput]

AWSManagedRulesATPRuleSetUnion = Union[AWSManagedRulesATPRuleSet, AWSManagedRulesATPRuleSetOutput]

RateBasedStatementUnion = Union[RateBasedStatement, RateBasedStatementOutput]

OverrideActionUnion = Union[OverrideAction, OverrideActionOutput]


class FirewallManagerStatement(BaseValidatorModel):
    ManagedRuleGroupStatement: Optional[ManagedRuleGroupStatementOutput] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementOutput] = None


class StatementOutput(BaseValidatorModel):
    ByteMatchStatement: Optional[ByteMatchStatementOutput] = None
    SqliMatchStatement: Optional[SqliMatchStatementOutput] = None
    XssMatchStatement: Optional[XssMatchStatementOutput] = None
    SizeConstraintStatement: Optional[SizeConstraintStatementOutput] = None
    GeoMatchStatement: Optional[GeoMatchStatementOutput] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementOutput] = None
    IPSetReferenceStatement: Optional[IPSetReferenceStatement] = None
    RegexPatternSetReferenceStatement: Optional[RegexPatternSetReferenceStatementOutput] = None
    RateBasedStatement: Optional[RateBasedStatementOutput] = None
    AndStatement: Optional[AndStatementOutput] = None
    OrStatement: Optional[OrStatementOutput] = None
    NotStatement: Optional[NotStatementOutput] = None
    ManagedRuleGroupStatement: Optional[ManagedRuleGroupStatementOutput] = None
    LabelMatchStatement: Optional[LabelMatchStatement] = None
    RegexMatchStatement: Optional[RegexMatchStatementOutput] = None

RuleActionUnion = Union[RuleAction, RuleActionOutput]


class ByteMatchStatement(BaseValidatorModel):
    SearchString: Blob
    FieldToMatch: FieldToMatchUnion
    TextTransformations: List[TextTransformation]
    PositionalConstraint: PositionalConstraintType


class RegexMatchStatement(BaseValidatorModel):
    RegexString: str
    FieldToMatch: FieldToMatchUnion
    TextTransformations: List[TextTransformation]


class RegexPatternSetReferenceStatement(BaseValidatorModel):
    ARN: str
    FieldToMatch: FieldToMatchUnion
    TextTransformations: List[TextTransformation]


class SizeConstraintStatement(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnion
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: List[TextTransformation]


class SqliMatchStatement(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnion
    TextTransformations: List[TextTransformation]
    SensitivityLevel: Optional[SensitivityLevelType] = None


class XssMatchStatement(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnion
    TextTransformations: List[TextTransformation]

LoggingConfigurationUnion = Union[LoggingConfiguration, LoggingConfigurationOutput]


class ManagedRuleGroupConfig(BaseValidatorModel):
    LoginPath: Optional[str] = None
    PayloadType: Optional[PayloadTypeType] = None
    UsernameField: Optional[UsernameField] = None
    PasswordField: Optional[PasswordField] = None
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSet] = None
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSetUnion] = None
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSetUnion] = None


class FirewallManagerRuleGroup(BaseValidatorModel):
    Name: str
    Priority: int
    FirewallManagerStatement: FirewallManagerStatement
    OverrideAction: OverrideActionOutput
    VisibilityConfig: VisibilityConfig


class RuleOutput(BaseValidatorModel):
    Name: str
    Priority: int
    Statement: StatementOutput
    VisibilityConfig: VisibilityConfig
    Action: Optional[RuleActionOutput] = None
    OverrideAction: Optional[OverrideActionOutput] = None
    RuleLabels: Optional[List[Label]] = None
    CaptchaConfig: Optional[CaptchaConfig] = None
    ChallengeConfig: Optional[ChallengeConfig] = None


class RuleActionOverride(BaseValidatorModel):
    Name: str
    ActionToUse: RuleActionUnion

ByteMatchStatementUnion = Union[ByteMatchStatement, ByteMatchStatementOutput]

RegexMatchStatementUnion = Union[RegexMatchStatement, RegexMatchStatementOutput]

RegexPatternSetReferenceStatementUnion = Union[RegexPatternSetReferenceStatement, RegexPatternSetReferenceStatementOutput]

SizeConstraintStatementUnion = Union[SizeConstraintStatement, SizeConstraintStatementOutput]

SqliMatchStatementUnion = Union[SqliMatchStatement, SqliMatchStatementOutput]

XssMatchStatementUnion = Union[XssMatchStatement, XssMatchStatementOutput]


# This class is the input for the 'put_logging_configuration' function.
class PutLoggingConfigurationRequest(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationUnion

ManagedRuleGroupConfigUnion = Union[ManagedRuleGroupConfig, ManagedRuleGroupConfigOutput]


class RuleGroup(BaseValidatorModel):
    Name: str
    Id: str
    Capacity: int
    ARN: str
    VisibilityConfig: VisibilityConfig
    Description: Optional[str] = None
    Rules: Optional[List[RuleOutput]] = None
    LabelNamespace: Optional[str] = None
    CustomResponseBodies: Optional[Dict[str, CustomResponseBody]] = None
    AvailableLabels: Optional[List[LabelSummary]] = None
    ConsumedLabels: Optional[List[LabelSummary]] = None


class WebACL(BaseValidatorModel):
    Name: str
    Id: str
    ARN: str
    DefaultAction: DefaultActionOutput
    VisibilityConfig: VisibilityConfig
    Description: Optional[str] = None
    Rules: Optional[List[RuleOutput]] = None
    DataProtectionConfig: Optional[DataProtectionConfigOutput] = None
    Capacity: Optional[int] = None
    PreProcessFirewallManagerRuleGroups: Optional[List[FirewallManagerRuleGroup]] = None
    PostProcessFirewallManagerRuleGroups: Optional[List[FirewallManagerRuleGroup]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LabelNamespace: Optional[str] = None
    CustomResponseBodies: Optional[Dict[str, CustomResponseBody]] = None
    CaptchaConfig: Optional[CaptchaConfig] = None
    ChallengeConfig: Optional[ChallengeConfig] = None
    TokenDomains: Optional[List[str]] = None
    AssociationConfig: Optional[AssociationConfigOutput] = None
    RetrofittedByFirewallManager: Optional[bool] = None

RuleActionOverrideUnion = Union[RuleActionOverride, RuleActionOverrideOutput]


# This class is the output for the 'get_rule_group' function.
class GetRuleGroupResponse(BaseValidatorModel):
    RuleGroup: RuleGroup
    LockToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_web_acl_for_resource' function.
class GetWebACLForResourceResponse(BaseValidatorModel):
    WebACL: WebACL
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_web_acl' function.
class GetWebACLResponse(BaseValidatorModel):
    WebACL: WebACL
    LockToken: str
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadata


class ManagedRuleGroupStatement(BaseValidatorModel):
    VendorName: str
    Name: str
    Version: Optional[str] = None
    ExcludedRules: Optional[List[ExcludedRule]] = None
    ScopeDownStatement: Optional[Dict[str, Any]] = None
    ManagedRuleGroupConfigs: Optional[List[ManagedRuleGroupConfigUnion]] = None
    RuleActionOverrides: Optional[List[RuleActionOverrideUnion]] = None


class RuleGroupReferenceStatement(BaseValidatorModel):
    ARN: str
    ExcludedRules: Optional[List[ExcludedRule]] = None
    RuleActionOverrides: Optional[List[RuleActionOverrideUnion]] = None

ManagedRuleGroupStatementUnion = Union[ManagedRuleGroupStatement, ManagedRuleGroupStatementOutput]

RuleGroupReferenceStatementUnion = Union[RuleGroupReferenceStatement, RuleGroupReferenceStatementOutput]


class Statement(BaseValidatorModel):
    ByteMatchStatement: Optional[ByteMatchStatementUnion] = None
    SqliMatchStatement: Optional[SqliMatchStatementUnion] = None
    XssMatchStatement: Optional[XssMatchStatementUnion] = None
    SizeConstraintStatement: Optional[SizeConstraintStatementUnion] = None
    GeoMatchStatement: Optional[GeoMatchStatementUnion] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementUnion] = None
    IPSetReferenceStatement: Optional[IPSetReferenceStatement] = None
    RegexPatternSetReferenceStatement: Optional[RegexPatternSetReferenceStatementUnion] = None
    RateBasedStatement: Optional[RateBasedStatementUnion] = None
    AndStatement: Optional[AndStatementUnion] = None
    OrStatement: Optional[OrStatementUnion] = None
    NotStatement: Optional[NotStatementUnion] = None
    ManagedRuleGroupStatement: Optional[ManagedRuleGroupStatementUnion] = None
    LabelMatchStatement: Optional[LabelMatchStatement] = None
    RegexMatchStatement: Optional[RegexMatchStatementUnion] = None

StatementUnion = Union[Statement, StatementOutput]


class Rule(BaseValidatorModel):
    Name: str
    Priority: int
    Statement: StatementUnion
    VisibilityConfig: VisibilityConfig
    Action: Optional[RuleActionUnion] = None
    OverrideAction: Optional[OverrideActionUnion] = None
    RuleLabels: Optional[List[Label]] = None
    CaptchaConfig: Optional[CaptchaConfig] = None
    ChallengeConfig: Optional[ChallengeConfig] = None

RuleUnion = Union[Rule, RuleOutput]


# This class is the input for the 'check_capacity' function.
class CheckCapacityRequest(BaseValidatorModel):
    Scope: ScopeType
    Rules: List[RuleUnion]


# This class is the input for the 'create_rule_group' function.
class CreateRuleGroupRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Capacity: int
    VisibilityConfig: VisibilityConfig
    Description: Optional[str] = None
    Rules: Optional[List[RuleUnion]] = None
    Tags: Optional[List[Tag]] = None
    CustomResponseBodies: Optional[Dict[str, CustomResponseBody]] = None


# This class is the input for the 'create_web_acl' function.
class CreateWebACLRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    DefaultAction: DefaultActionUnion
    VisibilityConfig: VisibilityConfig
    Description: Optional[str] = None
    Rules: Optional[List[RuleUnion]] = None
    DataProtectionConfig: Optional[DataProtectionConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    CustomResponseBodies: Optional[Dict[str, CustomResponseBody]] = None
    CaptchaConfig: Optional[CaptchaConfig] = None
    ChallengeConfig: Optional[ChallengeConfig] = None
    TokenDomains: Optional[List[str]] = None
    AssociationConfig: Optional[AssociationConfigUnion] = None


# This class is the input for the 'update_rule_group' function.
class UpdateRuleGroupRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    VisibilityConfig: VisibilityConfig
    LockToken: str
    Description: Optional[str] = None
    Rules: Optional[List[RuleUnion]] = None
    CustomResponseBodies: Optional[Dict[str, CustomResponseBody]] = None


# This class is the input for the 'update_web_acl' function.
class UpdateWebACLRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    DefaultAction: DefaultActionUnion
    VisibilityConfig: VisibilityConfig
    LockToken: str
    Description: Optional[str] = None
    Rules: Optional[List[RuleUnion]] = None
    DataProtectionConfig: Optional[DataProtectionConfigUnion] = None
    CustomResponseBodies: Optional[Dict[str, CustomResponseBody]] = None
    CaptchaConfig: Optional[CaptchaConfig] = None
    ChallengeConfig: Optional[ChallengeConfig] = None
    TokenDomains: Optional[List[str]] = None
    AssociationConfig: Optional[AssociationConfigUnion] = None
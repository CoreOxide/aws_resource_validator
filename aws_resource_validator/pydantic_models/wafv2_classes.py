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
from aws_resource_validator.pydantic_models.wafv2_constants import *

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
    Statements: Sequence[Mapping[str, Any]]


class AssociateWebACLRequest(BaseValidatorModel):
    WebACLArn: str
    ResourceArn: str


class RequestBodyAssociatedResourceTypeConfig(BaseValidatorModel):
    DefaultSizeInspectionLimit: SizeInspectionLimitType


class Body(BaseValidatorModel):
    OversizeHandling: Optional[OversizeHandlingType] = None


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
    All: Optional[Mapping[str, Any]] = None
    IncludedCookies: Optional[Sequence[str]] = None
    ExcludedCookies: Optional[Sequence[str]] = None


class CreateAPIKeyRequest(BaseValidatorModel):
    Scope: ScopeType
    TokenDomains: Sequence[str]


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
    FieldKeys: Optional[Sequence[str]] = None


class DeleteAPIKeyRequest(BaseValidatorModel):
    Scope: ScopeType
    APIKey: str


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
    LogType: Optional[Literal["WAF_LOGS"]] = None
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


class DescribeManagedProductsByVendorRequest(BaseValidatorModel):
    VendorName: str
    Scope: ScopeType


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


class GenerateMobileSdkReleaseUrlRequest(BaseValidatorModel):
    Platform: PlatformType
    ReleaseVersion: str


class GetDecryptedAPIKeyRequest(BaseValidatorModel):
    Scope: ScopeType
    APIKey: str


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


class GetLoggingConfigurationRequest(BaseValidatorModel):
    ResourceArn: str
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None


class GetManagedRuleSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


class GetMobileSdkReleaseRequest(BaseValidatorModel):
    Platform: PlatformType
    ReleaseVersion: str


class GetPermissionPolicyRequest(BaseValidatorModel):
    ResourceArn: str


class GetRateBasedStatementManagedKeysRequest(BaseValidatorModel):
    Scope: ScopeType
    WebACLName: str
    WebACLId: str
    RuleName: str
    RuleGroupRuleName: Optional[str] = None


class RateBasedStatementManagedKeysIPSet(BaseValidatorModel):
    IPAddressVersion: Optional[IPAddressVersionType] = None
    Addresses: Optional[List[str]] = None


class GetRegexPatternSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


class GetRuleGroupRequest(BaseValidatorModel):
    Name: Optional[str] = None
    Scope: Optional[ScopeType] = None
    Id: Optional[str] = None
    ARN: Optional[str] = None


class TimeWindowOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


class GetWebACLForResourceRequest(BaseValidatorModel):
    ResourceArn: str


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
    All: Optional[Mapping[str, Any]] = None
    IncludedHeaders: Optional[Sequence[str]] = None
    ExcludedHeaders: Optional[Sequence[str]] = None


class IPSetForwardedIPConfig(BaseValidatorModel):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType
    Position: ForwardedIPPositionType


class JsonMatchPatternOutput(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedPaths: Optional[List[str]] = None


class JsonMatchPattern(BaseValidatorModel):
    All: Optional[Mapping[str, Any]] = None
    IncludedPaths: Optional[Sequence[str]] = None


class LabelMatchStatement(BaseValidatorModel):
    Scope: LabelMatchScopeType
    Key: str


class Label(BaseValidatorModel):
    Name: str


class ListAPIKeysRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListAvailableManagedRuleGroupVersionsRequest(BaseValidatorModel):
    VendorName: str
    Name: str
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ManagedRuleGroupVersion(BaseValidatorModel):
    Name: Optional[str] = None
    LastUpdateTimestamp: Optional[datetime] = None


class ListAvailableManagedRuleGroupsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ManagedRuleGroupSummary(BaseValidatorModel):
    VendorName: Optional[str] = None
    Name: Optional[str] = None
    VersioningSupported: Optional[bool] = None
    Description: Optional[str] = None


class ListIPSetsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListLoggingConfigurationsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None
    LogScope: Optional[LogScopeType] = None


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


class ListMobileSdkReleasesRequest(BaseValidatorModel):
    Platform: PlatformType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ReleaseSummary(BaseValidatorModel):
    ReleaseVersion: Optional[str] = None
    Timestamp: Optional[datetime] = None


class ListRegexPatternSetsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListResourcesForWebACLRequest(BaseValidatorModel):
    WebACLArn: str
    ResourceType: Optional[ResourceTypeType] = None


class ListRuleGroupsRequest(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


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
    Statement: Mapping[str, Any]


class OrStatementOutput(BaseValidatorModel):
    Statements: List[Dict[str, Any]]


class OrStatement(BaseValidatorModel):
    Statements: Sequence[Mapping[str, Any]]


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
    SuccessStrings: Sequence[str]
    FailureStrings: Sequence[str]


class ResponseInspectionHeaderOutput(BaseValidatorModel):
    Name: str
    SuccessValues: List[str]
    FailureValues: List[str]


class ResponseInspectionHeader(BaseValidatorModel):
    Name: str
    SuccessValues: Sequence[str]
    FailureValues: Sequence[str]


class ResponseInspectionJsonOutput(BaseValidatorModel):
    Identifier: str
    SuccessValues: List[str]
    FailureValues: List[str]


class ResponseInspectionJson(BaseValidatorModel):
    Identifier: str
    SuccessValues: Sequence[str]
    FailureValues: Sequence[str]


class ResponseInspectionStatusCodeOutput(BaseValidatorModel):
    SuccessCodes: List[int]
    FailureCodes: List[int]


class ResponseInspectionStatusCode(BaseValidatorModel):
    SuccessCodes: Sequence[int]
    FailureCodes: Sequence[int]


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateIPSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    Addresses: Sequence[str]
    LockToken: str
    Description: Optional[str] = None


class AssociationConfigOutput(BaseValidatorModel):
    RequestBody: Optional[ Dict[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfig] ] = None


class AssociationConfig(BaseValidatorModel):
    RequestBody: Optional[ Mapping[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfig] ] = None


class TextTransformation(BaseValidatorModel):
    pass


class RateLimitCookieOutput(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitCookie(BaseValidatorModel):
    Name: str
    TextTransformations: Sequence[TextTransformation]


class RateLimitHeaderOutput(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitHeader(BaseValidatorModel):
    Name: str
    TextTransformations: Sequence[TextTransformation]


class RateLimitQueryArgumentOutput(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformation]


class RateLimitQueryArgument(BaseValidatorModel):
    Name: str
    TextTransformations: Sequence[TextTransformation]


class RateLimitQueryStringOutput(BaseValidatorModel):
    TextTransformations: List[TextTransformation]


class RateLimitQueryString(BaseValidatorModel):
    TextTransformations: Sequence[TextTransformation]


class RateLimitUriPathOutput(BaseValidatorModel):
    TextTransformations: List[TextTransformation]


class RateLimitUriPath(BaseValidatorModel):
    TextTransformations: Sequence[TextTransformation]


class CaptchaConfig(BaseValidatorModel):
    ImmunityTimeProperty: Optional[ImmunityTimeProperty] = None


class ChallengeConfig(BaseValidatorModel):
    ImmunityTimeProperty: Optional[ImmunityTimeProperty] = None


class CheckCapacityResponse(BaseValidatorModel):
    Capacity: int
    ResponseMetadata: ResponseMetadata


class CreateAPIKeyResponse(BaseValidatorModel):
    APIKey: str
    ResponseMetadata: ResponseMetadata


class DeleteFirewallManagerRuleGroupsResponse(BaseValidatorModel):
    NextWebACLLockToken: str
    ResponseMetadata: ResponseMetadata


class GenerateMobileSdkReleaseUrlResponse(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadata


class GetDecryptedAPIKeyResponse(BaseValidatorModel):
    TokenDomains: List[str]
    CreationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetPermissionPolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class ListAPIKeysResponse(BaseValidatorModel):
    NextMarker: str
    APIKeySummaries: List[APIKeySummary]
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadata


class ListResourcesForWebACLResponse(BaseValidatorModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadata


class PutManagedRuleSetVersionsResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


class UpdateIPSetResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


class UpdateManagedRuleSetVersionExpiryDateResponse(BaseValidatorModel):
    ExpiringVersion: str
    ExpiryTimestamp: datetime
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


class UpdateRegexPatternSetResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


class UpdateRuleGroupResponse(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadata


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


class CreateIPSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    IPAddressVersion: IPAddressVersionType
    Addresses: Sequence[str]
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


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
    Tags: Sequence[Tag]


class CreateIPSetResponse(BaseValidatorModel):
    Summary: IPSetSummary
    ResponseMetadata: ResponseMetadata


class ListIPSetsResponse(BaseValidatorModel):
    NextMarker: str
    IPSets: List[IPSetSummary]
    ResponseMetadata: ResponseMetadata


class CreateRegexPatternSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    RegularExpressionList: Sequence[Regex]
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class RegexPatternSet(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    ARN: Optional[str] = None
    Description: Optional[str] = None
    RegularExpressionList: Optional[List[Regex]] = None


class UpdateRegexPatternSetRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    RegularExpressionList: Sequence[Regex]
    LockToken: str
    Description: Optional[str] = None


class CreateRegexPatternSetResponse(BaseValidatorModel):
    Summary: RegexPatternSetSummary
    ResponseMetadata: ResponseMetadata


class ListRegexPatternSetsResponse(BaseValidatorModel):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummary]
    ResponseMetadata: ResponseMetadata


class CreateRuleGroupResponse(BaseValidatorModel):
    Summary: RuleGroupSummary
    ResponseMetadata: ResponseMetadata


class ListRuleGroupsResponse(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[RuleGroupSummary]
    ResponseMetadata: ResponseMetadata


class CreateWebACLResponse(BaseValidatorModel):
    Summary: WebACLSummary
    ResponseMetadata: ResponseMetadata


class ListWebACLsResponse(BaseValidatorModel):
    NextMarker: str
    WebACLs: List[WebACLSummary]
    ResponseMetadata: ResponseMetadata


class CustomRequestHandlingOutput(BaseValidatorModel):
    InsertHeaders: List[CustomHTTPHeader]


class CustomRequestHandling(BaseValidatorModel):
    InsertHeaders: Sequence[CustomHTTPHeader]


class CustomResponseOutput(BaseValidatorModel):
    ResponseCode: int
    CustomResponseBodyKey: Optional[str] = None
    ResponseHeaders: Optional[List[CustomHTTPHeader]] = None


class CustomResponse(BaseValidatorModel):
    ResponseCode: int
    CustomResponseBodyKey: Optional[str] = None
    ResponseHeaders: Optional[Sequence[CustomHTTPHeader]] = None


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


class DescribeAllManagedProductsResponse(BaseValidatorModel):
    ManagedProducts: List[ManagedProductDescriptor]
    ResponseMetadata: ResponseMetadata


class DescribeManagedProductsByVendorResponse(BaseValidatorModel):
    ManagedProducts: List[ManagedProductDescriptor]
    ResponseMetadata: ResponseMetadata


class GeoMatchStatementOutput(BaseValidatorModel):
    CountryCodes: Optional[List[CountryCodeType]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfig] = None


class GeoMatchStatement(BaseValidatorModel):
    CountryCodes: Optional[Sequence[CountryCodeType]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfig] = None


class GetIPSetResponse(BaseValidatorModel):
    IPSet: IPSet
    LockToken: str
    ResponseMetadata: ResponseMetadata


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


class IPSetReferenceStatement(BaseValidatorModel):
    ARN: str
    IPSetForwardedIPConfig: Optional[IPSetForwardedIPConfig] = None


class JsonBodyOutput(BaseValidatorModel):
    MatchPattern: JsonMatchPatternOutput
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehaviorType] = None
    OversizeHandling: Optional[OversizeHandlingType] = None


class ListAvailableManagedRuleGroupVersionsResponse(BaseValidatorModel):
    NextMarker: str
    Versions: List[ManagedRuleGroupVersion]
    CurrentDefaultVersion: str
    ResponseMetadata: ResponseMetadata


class ListAvailableManagedRuleGroupsResponse(BaseValidatorModel):
    NextMarker: str
    ManagedRuleGroups: List[ManagedRuleGroupSummary]
    ResponseMetadata: ResponseMetadata


class ListManagedRuleSetsResponse(BaseValidatorModel):
    NextMarker: str
    ManagedRuleSets: List[ManagedRuleSetSummary]
    ResponseMetadata: ResponseMetadata


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
    PhoneNumberFields: Optional[Sequence[PhoneNumberField]] = None
    AddressFields: Optional[Sequence[AddressField]] = None


class PutManagedRuleSetVersionsRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    RecommendedVersion: Optional[str] = None
    VersionsToPublish: Optional[Mapping[str, VersionToPublish]] = None


class ResponseInspectionOutput(BaseValidatorModel):
    StatusCode: Optional[ResponseInspectionStatusCodeOutput] = None
    Header: Optional[ResponseInspectionHeaderOutput] = None
    BodyContains: Optional[ResponseInspectionBodyContainsOutput] = None
    Json: Optional[ResponseInspectionJsonOutput] = None


class Timestamp(BaseValidatorModel):
    pass


class TimeWindow(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp


class UpdateManagedRuleSetVersionExpiryDateRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    VersionToExpire: str
    ExpiryTimestamp: Timestamp


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


class FilterOutput(BaseValidatorModel):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: List[Condition]


class Filter(BaseValidatorModel):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: Sequence[Condition]


class CookieMatchPatternUnion(BaseValidatorModel):
    pass


class Cookies(BaseValidatorModel):
    MatchPattern: CookieMatchPatternUnion
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType


class GetMobileSdkReleaseResponse(BaseValidatorModel):
    MobileSdkRelease: MobileSdkRelease
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    NextMarker: str
    TagInfoForResource: TagInfoForResource
    ResponseMetadata: ResponseMetadata


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


class BlockActionOutput(BaseValidatorModel):
    CustomResponse: Optional[CustomResponseOutput] = None


class DataProtectionConfigOutput(BaseValidatorModel):
    DataProtections: List[DataProtectionOutput]


class DataProtectionConfig(BaseValidatorModel):
    DataProtections: Sequence[DataProtection]


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


class HeaderMatchPatternUnion(BaseValidatorModel):
    pass


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


class JsonMatchPatternUnion(BaseValidatorModel):
    pass


class JsonBody(BaseValidatorModel):
    MatchPattern: JsonMatchPatternUnion
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehaviorType] = None
    OversizeHandling: Optional[OversizeHandlingType] = None


class GetManagedRuleSetResponse(BaseValidatorModel):
    ManagedRuleSet: ManagedRuleSet
    LockToken: str
    ResponseMetadata: ResponseMetadata


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


class ResponseInspectionHeaderUnion(BaseValidatorModel):
    pass


class ResponseInspectionBodyContainsUnion(BaseValidatorModel):
    pass


class ResponseInspectionJsonUnion(BaseValidatorModel):
    pass


class ResponseInspectionStatusCodeUnion(BaseValidatorModel):
    pass


class ResponseInspection(BaseValidatorModel):
    StatusCode: Optional[ResponseInspectionStatusCodeUnion] = None
    Header: Optional[ResponseInspectionHeaderUnion] = None
    BodyContains: Optional[ResponseInspectionBodyContainsUnion] = None
    Json: Optional[ResponseInspectionJsonUnion] = None


class RateBasedStatementOutput(BaseValidatorModel):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: Optional[int] = None
    ScopeDownStatement: Optional[Dict[str, Any]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfig] = None
    CustomKeys: Optional[List[RateBasedStatementCustomKeyOutput]] = None


class RateLimitQueryArgumentUnion(BaseValidatorModel):
    pass


class RateLimitUriPathUnion(BaseValidatorModel):
    pass


class RateLimitCookieUnion(BaseValidatorModel):
    pass


class RateLimitHeaderUnion(BaseValidatorModel):
    pass


class RateLimitQueryStringUnion(BaseValidatorModel):
    pass


class RateBasedStatementCustomKey(BaseValidatorModel):
    Header: Optional[RateLimitHeaderUnion] = None
    Cookie: Optional[RateLimitCookieUnion] = None
    QueryArgument: Optional[RateLimitQueryArgumentUnion] = None
    QueryString: Optional[RateLimitQueryStringUnion] = None
    HTTPMethod: Optional[Mapping[str, Any]] = None
    ForwardedIP: Optional[Mapping[str, Any]] = None
    IP: Optional[Mapping[str, Any]] = None
    LabelNamespace: Optional[RateLimitLabelNamespace] = None
    UriPath: Optional[RateLimitUriPathUnion] = None
    JA3Fingerprint: Optional[RateLimitJA3Fingerprint] = None
    JA4Fingerprint: Optional[RateLimitJA4Fingerprint] = None


class LoggingFilterOutput(BaseValidatorModel):
    Filters: List[FilterOutput]
    DefaultBehavior: FilterBehaviorType


class LoggingFilter(BaseValidatorModel):
    Filters: Sequence[Filter]
    DefaultBehavior: FilterBehaviorType


class CustomRequestHandlingUnion(BaseValidatorModel):
    pass


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


class CustomResponseUnion(BaseValidatorModel):
    pass


class BlockAction(BaseValidatorModel):
    CustomResponse: Optional[CustomResponseUnion] = None


class GetSampledRequestsResponse(BaseValidatorModel):
    SampledRequests: List[SampledHTTPRequest]
    PopulationSize: int
    TimeWindow: TimeWindowOutput
    ResponseMetadata: ResponseMetadata


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


class ManagedRuleGroupConfigOutput(BaseValidatorModel):
    LoginPath: Optional[str] = None
    PayloadType: Optional[PayloadTypeType] = None
    UsernameField: Optional[UsernameField] = None
    PasswordField: Optional[PasswordField] = None
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSet] = None
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSetOutput] = None
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSetOutput] = None


class TimeWindowUnion(BaseValidatorModel):
    pass


class GetSampledRequestsRequest(BaseValidatorModel):
    WebAclArn: str
    RuleMetricName: str
    Scope: ScopeType
    TimeWindow: TimeWindowUnion
    MaxItems: int


class LoggingConfigurationOutput(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatchOutput]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LoggingFilter: Optional[LoggingFilterOutput] = None
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None


class RuleActionOverrideOutput(BaseValidatorModel):
    Name: str
    ActionToUse: RuleActionOutput


class RuleSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Action: Optional[RuleActionOutput] = None


class DefaultAction(BaseValidatorModel):
    Block: Optional[BlockAction] = None
    Allow: Optional[AllowAction] = None


class JsonBodyUnion(BaseValidatorModel):
    pass


class HeadersUnion(BaseValidatorModel):
    pass


class CookiesUnion(BaseValidatorModel):
    pass


class FieldToMatch(BaseValidatorModel):
    SingleHeader: Optional[SingleHeader] = None
    SingleQueryArgument: Optional[SingleQueryArgument] = None
    AllQueryArguments: Optional[Mapping[str, Any]] = None
    UriPath: Optional[Mapping[str, Any]] = None
    QueryString: Optional[Mapping[str, Any]] = None
    Body: Optional[Body] = None
    Method: Optional[Mapping[str, Any]] = None
    JsonBody: Optional[JsonBodyUnion] = None
    Headers: Optional[HeadersUnion] = None
    Cookies: Optional[CookiesUnion] = None
    HeaderOrder: Optional[HeaderOrder] = None
    JA3Fingerprint: Optional[JA3Fingerprint] = None
    JA4Fingerprint: Optional[JA4Fingerprint] = None


class ResponseInspectionUnion(BaseValidatorModel):
    pass


class RequestInspectionACFPUnion(BaseValidatorModel):
    pass


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


class RateBasedStatementCustomKeyUnion(BaseValidatorModel):
    pass


class RateBasedStatement(BaseValidatorModel):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: Optional[int] = None
    ScopeDownStatement: Optional[Mapping[str, Any]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfig] = None
    CustomKeys: Optional[Sequence[RateBasedStatementCustomKeyUnion]] = None


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


class DescribeManagedRuleGroupResponse(BaseValidatorModel):
    VersionName: str
    SnsTopicArn: str
    Capacity: int
    Rules: List[RuleSummary]
    LabelNamespace: str
    AvailableLabels: List[LabelSummary]
    ConsumedLabels: List[LabelSummary]
    ResponseMetadata: ResponseMetadata


class CaptchaActionUnion(BaseValidatorModel):
    pass


class AllowActionUnion(BaseValidatorModel):
    pass


class CountActionUnion(BaseValidatorModel):
    pass


class BlockActionUnion(BaseValidatorModel):
    pass


class ChallengeActionUnion(BaseValidatorModel):
    pass


class RuleAction(BaseValidatorModel):
    Block: Optional[BlockActionUnion] = None
    Allow: Optional[AllowActionUnion] = None
    Count: Optional[CountActionUnion] = None
    Captcha: Optional[CaptchaActionUnion] = None
    Challenge: Optional[ChallengeActionUnion] = None


class LoggingConfiguration(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: Sequence[str]
    RedactedFields: Optional[Sequence[FieldToMatch]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LoggingFilter: Optional[LoggingFilter] = None
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None


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


class Blob(BaseValidatorModel):
    pass


class FieldToMatchUnion(BaseValidatorModel):
    pass


class ByteMatchStatement(BaseValidatorModel):
    SearchString: Blob
    FieldToMatch: FieldToMatchUnion
    TextTransformations: Sequence[TextTransformation]
    PositionalConstraint: PositionalConstraintType


class RegexMatchStatement(BaseValidatorModel):
    RegexString: str
    FieldToMatch: FieldToMatchUnion
    TextTransformations: Sequence[TextTransformation]


class RegexPatternSetReferenceStatement(BaseValidatorModel):
    ARN: str
    FieldToMatch: FieldToMatchUnion
    TextTransformations: Sequence[TextTransformation]


class SizeConstraintStatement(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnion
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: Sequence[TextTransformation]


class SqliMatchStatement(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnion
    TextTransformations: Sequence[TextTransformation]
    SensitivityLevel: Optional[SensitivityLevelType] = None


class XssMatchStatement(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnion
    TextTransformations: Sequence[TextTransformation]


class AWSManagedRulesACFPRuleSetUnion(BaseValidatorModel):
    pass


class AWSManagedRulesATPRuleSetUnion(BaseValidatorModel):
    pass


class ManagedRuleGroupConfig(BaseValidatorModel):
    LoginPath: Optional[str] = None
    PayloadType: Optional[PayloadTypeType] = None
    UsernameField: Optional[UsernameField] = None
    PasswordField: Optional[PasswordField] = None
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSet] = None
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSetUnion] = None
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSetUnion] = None


class OverrideActionOutput(BaseValidatorModel):
    pass


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


class RuleActionUnion(BaseValidatorModel):
    pass


class RuleActionOverride(BaseValidatorModel):
    Name: str
    ActionToUse: RuleActionUnion


class LoggingConfigurationUnion(BaseValidatorModel):
    pass


class PutLoggingConfigurationRequest(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationUnion


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


class GetRuleGroupResponse(BaseValidatorModel):
    RuleGroup: RuleGroup
    LockToken: str
    ResponseMetadata: ResponseMetadata


class GetWebACLForResourceResponse(BaseValidatorModel):
    WebACL: WebACL
    ResponseMetadata: ResponseMetadata


class GetWebACLResponse(BaseValidatorModel):
    WebACL: WebACL
    LockToken: str
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadata


class RuleActionOverrideUnion(BaseValidatorModel):
    pass


class ManagedRuleGroupConfigUnion(BaseValidatorModel):
    pass


class ManagedRuleGroupStatement(BaseValidatorModel):
    VendorName: str
    Name: str
    Version: Optional[str] = None
    ExcludedRules: Optional[Sequence[ExcludedRule]] = None
    ScopeDownStatement: Optional[Mapping[str, Any]] = None
    ManagedRuleGroupConfigs: Optional[Sequence[ManagedRuleGroupConfigUnion]] = None
    RuleActionOverrides: Optional[Sequence[RuleActionOverrideUnion]] = None


class RuleGroupReferenceStatement(BaseValidatorModel):
    ARN: str
    ExcludedRules: Optional[Sequence[ExcludedRule]] = None
    RuleActionOverrides: Optional[Sequence[RuleActionOverrideUnion]] = None


class RateBasedStatementUnion(BaseValidatorModel):
    pass


class OrStatementUnion(BaseValidatorModel):
    pass


class RegexMatchStatementUnion(BaseValidatorModel):
    pass


class SizeConstraintStatementUnion(BaseValidatorModel):
    pass


class XssMatchStatementUnion(BaseValidatorModel):
    pass


class NotStatementUnion(BaseValidatorModel):
    pass


class RegexPatternSetReferenceStatementUnion(BaseValidatorModel):
    pass


class AndStatementUnion(BaseValidatorModel):
    pass


class RuleGroupReferenceStatementUnion(BaseValidatorModel):
    pass


class ManagedRuleGroupStatementUnion(BaseValidatorModel):
    pass


class ByteMatchStatementUnion(BaseValidatorModel):
    pass


class SqliMatchStatementUnion(BaseValidatorModel):
    pass


class GeoMatchStatementUnion(BaseValidatorModel):
    pass


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


class StatementUnion(BaseValidatorModel):
    pass


class OverrideActionUnion(BaseValidatorModel):
    pass


class Rule(BaseValidatorModel):
    Name: str
    Priority: int
    Statement: StatementUnion
    VisibilityConfig: VisibilityConfig
    Action: Optional[RuleActionUnion] = None
    OverrideAction: Optional[OverrideActionUnion] = None
    RuleLabels: Optional[Sequence[Label]] = None
    CaptchaConfig: Optional[CaptchaConfig] = None
    ChallengeConfig: Optional[ChallengeConfig] = None


class RuleUnion(BaseValidatorModel):
    pass


class CheckCapacityRequest(BaseValidatorModel):
    Scope: ScopeType
    Rules: Sequence[RuleUnion]


class CreateRuleGroupRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Capacity: int
    VisibilityConfig: VisibilityConfig
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnion]] = None
    Tags: Optional[Sequence[Tag]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBody]] = None


class DefaultActionUnion(BaseValidatorModel):
    pass


class AssociationConfigUnion(BaseValidatorModel):
    pass


class DataProtectionConfigUnion(BaseValidatorModel):
    pass


class CreateWebACLRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    DefaultAction: DefaultActionUnion
    VisibilityConfig: VisibilityConfig
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnion]] = None
    DataProtectionConfig: Optional[DataProtectionConfigUnion] = None
    Tags: Optional[Sequence[Tag]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBody]] = None
    CaptchaConfig: Optional[CaptchaConfig] = None
    ChallengeConfig: Optional[ChallengeConfig] = None
    TokenDomains: Optional[Sequence[str]] = None
    AssociationConfig: Optional[AssociationConfigUnion] = None


class UpdateRuleGroupRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    VisibilityConfig: VisibilityConfig
    LockToken: str
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnion]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBody]] = None


class UpdateWebACLRequest(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    DefaultAction: DefaultActionUnion
    VisibilityConfig: VisibilityConfig
    LockToken: str
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnion]] = None
    DataProtectionConfig: Optional[DataProtectionConfigUnion] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBody]] = None
    CaptchaConfig: Optional[CaptchaConfig] = None
    ChallengeConfig: Optional[ChallengeConfig] = None
    TokenDomains: Optional[Sequence[str]] = None
    AssociationConfig: Optional[AssociationConfigUnion] = None



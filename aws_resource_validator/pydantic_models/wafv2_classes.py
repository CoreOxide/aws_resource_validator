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

class APIKeySummaryTypeDef(BaseValidatorModel):
    TokenDomains: Optional[List[str]] = None
    APIKey: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Version: Optional[int] = None


class AWSManagedRulesBotControlRuleSetTypeDef(BaseValidatorModel):
    InspectionLevel: InspectionLevelType
    EnableMachineLearning: Optional[bool] = None


class ActionConditionTypeDef(BaseValidatorModel):
    Action: ActionValueType


class AddressFieldTypeDef(BaseValidatorModel):
    Identifier: str


class AndStatementOutputTypeDef(BaseValidatorModel):
    Statements: List[Dict[str, Any]]


class AndStatementTypeDef(BaseValidatorModel):
    Statements: Sequence[Mapping[str, Any]]


class AssociateWebACLRequestTypeDef(BaseValidatorModel):
    WebACLArn: str
    ResourceArn: str


class RequestBodyAssociatedResourceTypeConfigTypeDef(BaseValidatorModel):
    DefaultSizeInspectionLimit: SizeInspectionLimitType


class BodyTypeDef(BaseValidatorModel):
    OversizeHandling: Optional[OversizeHandlingType] = None


class ImmunityTimePropertyTypeDef(BaseValidatorModel):
    ImmunityTime: int


class CaptchaResponseTypeDef(BaseValidatorModel):
    ResponseCode: Optional[int] = None
    SolveTimestamp: Optional[int] = None
    FailureReason: Optional[FailureReasonType] = None


class ChallengeResponseTypeDef(BaseValidatorModel):
    ResponseCode: Optional[int] = None
    SolveTimestamp: Optional[int] = None
    FailureReason: Optional[FailureReasonType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LabelNameConditionTypeDef(BaseValidatorModel):
    LabelName: str


class CookieMatchPatternOutputTypeDef(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedCookies: Optional[List[str]] = None
    ExcludedCookies: Optional[List[str]] = None


class CookieMatchPatternTypeDef(BaseValidatorModel):
    All: Optional[Mapping[str, Any]] = None
    IncludedCookies: Optional[Sequence[str]] = None
    ExcludedCookies: Optional[Sequence[str]] = None


class CreateAPIKeyRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    TokenDomains: Sequence[str]


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class IPSetSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None


class RegexTypeDef(BaseValidatorModel):
    RegexString: Optional[str] = None


class RegexPatternSetSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None


class CustomResponseBodyTypeDef(BaseValidatorModel):
    ContentType: ResponseContentTypeType
    Content: str


class VisibilityConfigTypeDef(BaseValidatorModel):
    SampledRequestsEnabled: bool
    CloudWatchMetricsEnabled: bool
    MetricName: str


class RuleGroupSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None


class WebACLSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None


class CustomHTTPHeaderTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class FieldToProtectOutputTypeDef(BaseValidatorModel):
    FieldType: FieldToProtectTypeType
    FieldKeys: Optional[List[str]] = None


class FieldToProtectTypeDef(BaseValidatorModel):
    FieldType: FieldToProtectTypeType
    FieldKeys: Optional[Sequence[str]] = None


class DeleteAPIKeyRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    APIKey: str


class DeleteFirewallManagerRuleGroupsRequestTypeDef(BaseValidatorModel):
    WebACLArn: str
    WebACLLockToken: str


class DeleteIPSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str


class DeleteLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None


class DeletePermissionPolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DeleteRegexPatternSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str


class DeleteRuleGroupRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str


class DeleteWebACLRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str


class DescribeAllManagedProductsRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType


class ManagedProductDescriptorTypeDef(BaseValidatorModel):
    VendorName: Optional[str] = None
    ManagedRuleSetName: Optional[str] = None
    ProductId: Optional[str] = None
    ProductLink: Optional[str] = None
    ProductTitle: Optional[str] = None
    ProductDescription: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    IsVersioningSupported: Optional[bool] = None
    IsAdvancedManagedRuleSet: Optional[bool] = None


class DescribeManagedProductsByVendorRequestTypeDef(BaseValidatorModel):
    VendorName: str
    Scope: ScopeType


class DescribeManagedRuleGroupRequestTypeDef(BaseValidatorModel):
    VendorName: str
    Name: str
    Scope: ScopeType
    VersionName: Optional[str] = None


class LabelSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class DisassociateWebACLRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class EmailFieldTypeDef(BaseValidatorModel):
    Identifier: str


class ExcludedRuleTypeDef(BaseValidatorModel):
    Name: str


class HeaderOrderTypeDef(BaseValidatorModel):
    OversizeHandling: OversizeHandlingType


class JA3FingerprintTypeDef(BaseValidatorModel):
    FallbackBehavior: FallbackBehaviorType


class JA4FingerprintTypeDef(BaseValidatorModel):
    FallbackBehavior: FallbackBehaviorType


class SingleHeaderTypeDef(BaseValidatorModel):
    Name: str


class SingleQueryArgumentTypeDef(BaseValidatorModel):
    Name: str


class ForwardedIPConfigTypeDef(BaseValidatorModel):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType


class GenerateMobileSdkReleaseUrlRequestTypeDef(BaseValidatorModel):
    Platform: PlatformType
    ReleaseVersion: str


class GetDecryptedAPIKeyRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    APIKey: str


class GetIPSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


class IPSetTypeDef(BaseValidatorModel):
    Name: str
    Id: str
    ARN: str
    IPAddressVersion: IPAddressVersionType
    Addresses: List[str]
    Description: Optional[str] = None


class GetLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None


class GetManagedRuleSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


class GetMobileSdkReleaseRequestTypeDef(BaseValidatorModel):
    Platform: PlatformType
    ReleaseVersion: str


class GetPermissionPolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class GetRateBasedStatementManagedKeysRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    WebACLName: str
    WebACLId: str
    RuleName: str
    RuleGroupRuleName: Optional[str] = None


class RateBasedStatementManagedKeysIPSetTypeDef(BaseValidatorModel):
    IPAddressVersion: Optional[IPAddressVersionType] = None
    Addresses: Optional[List[str]] = None


class GetRegexPatternSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


class GetRuleGroupRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Scope: Optional[ScopeType] = None
    Id: Optional[str] = None
    ARN: Optional[str] = None


class TimeWindowOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


class GetWebACLForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class GetWebACLRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str


class HTTPHeaderTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class HeaderMatchPatternOutputTypeDef(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedHeaders: Optional[List[str]] = None
    ExcludedHeaders: Optional[List[str]] = None


class HeaderMatchPatternTypeDef(BaseValidatorModel):
    All: Optional[Mapping[str, Any]] = None
    IncludedHeaders: Optional[Sequence[str]] = None
    ExcludedHeaders: Optional[Sequence[str]] = None


class IPSetForwardedIPConfigTypeDef(BaseValidatorModel):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType
    Position: ForwardedIPPositionType


class JsonMatchPatternOutputTypeDef(BaseValidatorModel):
    All: Optional[Dict[str, Any]] = None
    IncludedPaths: Optional[List[str]] = None


class JsonMatchPatternTypeDef(BaseValidatorModel):
    All: Optional[Mapping[str, Any]] = None
    IncludedPaths: Optional[Sequence[str]] = None


class LabelMatchStatementTypeDef(BaseValidatorModel):
    Scope: LabelMatchScopeType
    Key: str


class LabelTypeDef(BaseValidatorModel):
    Name: str


class ListAPIKeysRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListAvailableManagedRuleGroupVersionsRequestTypeDef(BaseValidatorModel):
    VendorName: str
    Name: str
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ManagedRuleGroupVersionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    LastUpdateTimestamp: Optional[datetime] = None


class ListAvailableManagedRuleGroupsRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ManagedRuleGroupSummaryTypeDef(BaseValidatorModel):
    VendorName: Optional[str] = None
    Name: Optional[str] = None
    VersioningSupported: Optional[bool] = None
    Description: Optional[str] = None


class ListIPSetsRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListLoggingConfigurationsRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None
    LogScope: Optional[LogScopeType] = None


class ListManagedRuleSetsRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ManagedRuleSetSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None
    LabelNamespace: Optional[str] = None


class ListMobileSdkReleasesRequestTypeDef(BaseValidatorModel):
    Platform: PlatformType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ReleaseSummaryTypeDef(BaseValidatorModel):
    ReleaseVersion: Optional[str] = None
    Timestamp: Optional[datetime] = None


class ListRegexPatternSetsRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListResourcesForWebACLRequestTypeDef(BaseValidatorModel):
    WebACLArn: str
    ResourceType: Optional[ResourceTypeType] = None


class ListRuleGroupsRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class ListWebACLsRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None


class PasswordFieldTypeDef(BaseValidatorModel):
    Identifier: str


class UsernameFieldTypeDef(BaseValidatorModel):
    Identifier: str


class ManagedRuleSetVersionTypeDef(BaseValidatorModel):
    AssociatedRuleGroupArn: Optional[str] = None
    Capacity: Optional[int] = None
    ForecastedLifetime: Optional[int] = None
    PublishTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    ExpiryTimestamp: Optional[datetime] = None


class NotStatementOutputTypeDef(BaseValidatorModel):
    Statement: Dict[str, Any]


class NotStatementTypeDef(BaseValidatorModel):
    Statement: Mapping[str, Any]


class OrStatementOutputTypeDef(BaseValidatorModel):
    Statements: List[Dict[str, Any]]


class OrStatementTypeDef(BaseValidatorModel):
    Statements: Sequence[Mapping[str, Any]]


class PhoneNumberFieldTypeDef(BaseValidatorModel):
    Identifier: str


class VersionToPublishTypeDef(BaseValidatorModel):
    AssociatedRuleGroupArn: Optional[str] = None
    ForecastedLifetime: Optional[int] = None


class PutPermissionPolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RateLimitJA3FingerprintTypeDef(BaseValidatorModel):
    FallbackBehavior: FallbackBehaviorType


class RateLimitJA4FingerprintTypeDef(BaseValidatorModel):
    FallbackBehavior: FallbackBehaviorType


class RateLimitLabelNamespaceTypeDef(BaseValidatorModel):
    Namespace: str


class ResponseInspectionBodyContainsOutputTypeDef(BaseValidatorModel):
    SuccessStrings: List[str]
    FailureStrings: List[str]


class ResponseInspectionBodyContainsTypeDef(BaseValidatorModel):
    SuccessStrings: Sequence[str]
    FailureStrings: Sequence[str]


class ResponseInspectionHeaderOutputTypeDef(BaseValidatorModel):
    Name: str
    SuccessValues: List[str]
    FailureValues: List[str]


class ResponseInspectionHeaderTypeDef(BaseValidatorModel):
    Name: str
    SuccessValues: Sequence[str]
    FailureValues: Sequence[str]


class ResponseInspectionJsonOutputTypeDef(BaseValidatorModel):
    Identifier: str
    SuccessValues: List[str]
    FailureValues: List[str]


class ResponseInspectionJsonTypeDef(BaseValidatorModel):
    Identifier: str
    SuccessValues: Sequence[str]
    FailureValues: Sequence[str]


class ResponseInspectionStatusCodeOutputTypeDef(BaseValidatorModel):
    SuccessCodes: List[int]
    FailureCodes: List[int]


class ResponseInspectionStatusCodeTypeDef(BaseValidatorModel):
    SuccessCodes: Sequence[int]
    FailureCodes: Sequence[int]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateIPSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    Addresses: Sequence[str]
    LockToken: str
    Description: Optional[str] = None


class AssociationConfigOutputTypeDef(BaseValidatorModel):
    RequestBody: Optional[ Dict[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfigTypeDef] ] = None


class AssociationConfigTypeDef(BaseValidatorModel):
    RequestBody: Optional[ Mapping[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfigTypeDef] ] = None


class TextTransformationTypeDef(BaseValidatorModel):
    pass


class RateLimitCookieOutputTypeDef(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]


class RateLimitCookieTypeDef(BaseValidatorModel):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]


class RateLimitHeaderOutputTypeDef(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]


class RateLimitHeaderTypeDef(BaseValidatorModel):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]


class RateLimitQueryArgumentOutputTypeDef(BaseValidatorModel):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]


class RateLimitQueryArgumentTypeDef(BaseValidatorModel):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]


class RateLimitQueryStringOutputTypeDef(BaseValidatorModel):
    TextTransformations: List[TextTransformationTypeDef]


class RateLimitQueryStringTypeDef(BaseValidatorModel):
    TextTransformations: Sequence[TextTransformationTypeDef]


class RateLimitUriPathOutputTypeDef(BaseValidatorModel):
    TextTransformations: List[TextTransformationTypeDef]


class RateLimitUriPathTypeDef(BaseValidatorModel):
    TextTransformations: Sequence[TextTransformationTypeDef]


class CaptchaConfigTypeDef(BaseValidatorModel):
    ImmunityTimeProperty: Optional[ImmunityTimePropertyTypeDef] = None


class ChallengeConfigTypeDef(BaseValidatorModel):
    ImmunityTimeProperty: Optional[ImmunityTimePropertyTypeDef] = None


class CheckCapacityResponseTypeDef(BaseValidatorModel):
    Capacity: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAPIKeyResponseTypeDef(BaseValidatorModel):
    APIKey: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFirewallManagerRuleGroupsResponseTypeDef(BaseValidatorModel):
    NextWebACLLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GenerateMobileSdkReleaseUrlResponseTypeDef(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDecryptedAPIKeyResponseTypeDef(BaseValidatorModel):
    TokenDomains: List[str]
    CreationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetPermissionPolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAPIKeysResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    APIKeySummaries: List[APIKeySummaryTypeDef]
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourcesForWebACLResponseTypeDef(BaseValidatorModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutManagedRuleSetVersionsResponseTypeDef(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIPSetResponseTypeDef(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateManagedRuleSetVersionExpiryDateResponseTypeDef(BaseValidatorModel):
    ExpiringVersion: str
    ExpiryTimestamp: datetime
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRegexPatternSetResponseTypeDef(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRuleGroupResponseTypeDef(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWebACLResponseTypeDef(BaseValidatorModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ConditionTypeDef(BaseValidatorModel):
    ActionCondition: Optional[ActionConditionTypeDef] = None
    LabelNameCondition: Optional[LabelNameConditionTypeDef] = None


class CookiesOutputTypeDef(BaseValidatorModel):
    MatchPattern: CookieMatchPatternOutputTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType


class CreateIPSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    IPAddressVersion: IPAddressVersionType
    Addresses: Sequence[str]
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class MobileSdkReleaseTypeDef(BaseValidatorModel):
    ReleaseVersion: Optional[str] = None
    Timestamp: Optional[datetime] = None
    ReleaseNotes: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class TagInfoForResourceTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    TagList: Optional[List[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateIPSetResponseTypeDef(BaseValidatorModel):
    Summary: IPSetSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListIPSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    IPSets: List[IPSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRegexPatternSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    RegularExpressionList: Sequence[RegexTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class RegexPatternSetTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    ARN: Optional[str] = None
    Description: Optional[str] = None
    RegularExpressionList: Optional[List[RegexTypeDef]] = None


class UpdateRegexPatternSetRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    RegularExpressionList: Sequence[RegexTypeDef]
    LockToken: str
    Description: Optional[str] = None


class CreateRegexPatternSetResponseTypeDef(BaseValidatorModel):
    Summary: RegexPatternSetSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRegexPatternSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRuleGroupResponseTypeDef(BaseValidatorModel):
    Summary: RuleGroupSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRuleGroupsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    RuleGroups: List[RuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWebACLResponseTypeDef(BaseValidatorModel):
    Summary: WebACLSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListWebACLsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    WebACLs: List[WebACLSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CustomRequestHandlingOutputTypeDef(BaseValidatorModel):
    InsertHeaders: List[CustomHTTPHeaderTypeDef]


class CustomRequestHandlingTypeDef(BaseValidatorModel):
    InsertHeaders: Sequence[CustomHTTPHeaderTypeDef]


class CustomResponseOutputTypeDef(BaseValidatorModel):
    ResponseCode: int
    CustomResponseBodyKey: Optional[str] = None
    ResponseHeaders: Optional[List[CustomHTTPHeaderTypeDef]] = None


class CustomResponseTypeDef(BaseValidatorModel):
    ResponseCode: int
    CustomResponseBodyKey: Optional[str] = None
    ResponseHeaders: Optional[Sequence[CustomHTTPHeaderTypeDef]] = None


class DataProtectionOutputTypeDef(BaseValidatorModel):
    Field: FieldToProtectOutputTypeDef
    Action: DataProtectionActionType
    ExcludeRuleMatchDetails: Optional[bool] = None
    ExcludeRateBasedDetails: Optional[bool] = None


class DataProtectionTypeDef(BaseValidatorModel):
    Field: FieldToProtectTypeDef
    Action: DataProtectionActionType
    ExcludeRuleMatchDetails: Optional[bool] = None
    ExcludeRateBasedDetails: Optional[bool] = None


class DescribeAllManagedProductsResponseTypeDef(BaseValidatorModel):
    ManagedProducts: List[ManagedProductDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeManagedProductsByVendorResponseTypeDef(BaseValidatorModel):
    ManagedProducts: List[ManagedProductDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GeoMatchStatementOutputTypeDef(BaseValidatorModel):
    CountryCodes: Optional[List[CountryCodeType]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfigTypeDef] = None


class GeoMatchStatementTypeDef(BaseValidatorModel):
    CountryCodes: Optional[Sequence[CountryCodeType]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfigTypeDef] = None


class GetIPSetResponseTypeDef(BaseValidatorModel):
    IPSet: IPSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRateBasedStatementManagedKeysResponseTypeDef(BaseValidatorModel):
    ManagedKeysIPV4: RateBasedStatementManagedKeysIPSetTypeDef
    ManagedKeysIPV6: RateBasedStatementManagedKeysIPSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class HTTPRequestTypeDef(BaseValidatorModel):
    ClientIP: Optional[str] = None
    Country: Optional[str] = None
    URI: Optional[str] = None
    Method: Optional[str] = None
    HTTPVersion: Optional[str] = None
    Headers: Optional[List[HTTPHeaderTypeDef]] = None


class HeadersOutputTypeDef(BaseValidatorModel):
    MatchPattern: HeaderMatchPatternOutputTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType


class IPSetReferenceStatementTypeDef(BaseValidatorModel):
    ARN: str
    IPSetForwardedIPConfig: Optional[IPSetForwardedIPConfigTypeDef] = None


class JsonBodyOutputTypeDef(BaseValidatorModel):
    MatchPattern: JsonMatchPatternOutputTypeDef
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehaviorType] = None
    OversizeHandling: Optional[OversizeHandlingType] = None


class ListAvailableManagedRuleGroupVersionsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Versions: List[ManagedRuleGroupVersionTypeDef]
    CurrentDefaultVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAvailableManagedRuleGroupsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    ManagedRuleGroups: List[ManagedRuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListManagedRuleSetsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    ManagedRuleSets: List[ManagedRuleSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListMobileSdkReleasesResponseTypeDef(BaseValidatorModel):
    ReleaseSummaries: List[ReleaseSummaryTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class RequestInspectionTypeDef(BaseValidatorModel):
    PayloadType: PayloadTypeType
    UsernameField: UsernameFieldTypeDef
    PasswordField: PasswordFieldTypeDef


class ManagedRuleSetTypeDef(BaseValidatorModel):
    Name: str
    Id: str
    ARN: str
    Description: Optional[str] = None
    PublishedVersions: Optional[Dict[str, ManagedRuleSetVersionTypeDef]] = None
    RecommendedVersion: Optional[str] = None
    LabelNamespace: Optional[str] = None


class RequestInspectionACFPOutputTypeDef(BaseValidatorModel):
    PayloadType: PayloadTypeType
    UsernameField: Optional[UsernameFieldTypeDef] = None
    PasswordField: Optional[PasswordFieldTypeDef] = None
    EmailField: Optional[EmailFieldTypeDef] = None
    PhoneNumberFields: Optional[List[PhoneNumberFieldTypeDef]] = None
    AddressFields: Optional[List[AddressFieldTypeDef]] = None


class RequestInspectionACFPTypeDef(BaseValidatorModel):
    PayloadType: PayloadTypeType
    UsernameField: Optional[UsernameFieldTypeDef] = None
    PasswordField: Optional[PasswordFieldTypeDef] = None
    EmailField: Optional[EmailFieldTypeDef] = None
    PhoneNumberFields: Optional[Sequence[PhoneNumberFieldTypeDef]] = None
    AddressFields: Optional[Sequence[AddressFieldTypeDef]] = None


class PutManagedRuleSetVersionsRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    RecommendedVersion: Optional[str] = None
    VersionsToPublish: Optional[Mapping[str, VersionToPublishTypeDef]] = None


class ResponseInspectionOutputTypeDef(BaseValidatorModel):
    StatusCode: Optional[ResponseInspectionStatusCodeOutputTypeDef] = None
    Header: Optional[ResponseInspectionHeaderOutputTypeDef] = None
    BodyContains: Optional[ResponseInspectionBodyContainsOutputTypeDef] = None
    Json: Optional[ResponseInspectionJsonOutputTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class TimeWindowTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef


class UpdateManagedRuleSetVersionExpiryDateRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    VersionToExpire: str
    ExpiryTimestamp: TimestampTypeDef


class RateBasedStatementCustomKeyOutputTypeDef(BaseValidatorModel):
    Header: Optional[RateLimitHeaderOutputTypeDef] = None
    Cookie: Optional[RateLimitCookieOutputTypeDef] = None
    QueryArgument: Optional[RateLimitQueryArgumentOutputTypeDef] = None
    QueryString: Optional[RateLimitQueryStringOutputTypeDef] = None
    HTTPMethod: Optional[Dict[str, Any]] = None
    ForwardedIP: Optional[Dict[str, Any]] = None
    IP: Optional[Dict[str, Any]] = None
    LabelNamespace: Optional[RateLimitLabelNamespaceTypeDef] = None
    UriPath: Optional[RateLimitUriPathOutputTypeDef] = None
    JA3Fingerprint: Optional[RateLimitJA3FingerprintTypeDef] = None
    JA4Fingerprint: Optional[RateLimitJA4FingerprintTypeDef] = None


class FilterOutputTypeDef(BaseValidatorModel):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: List[ConditionTypeDef]


class FilterTypeDef(BaseValidatorModel):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: Sequence[ConditionTypeDef]


class CookieMatchPatternUnionTypeDef(BaseValidatorModel):
    pass


class CookiesTypeDef(BaseValidatorModel):
    MatchPattern: CookieMatchPatternUnionTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType


class GetMobileSdkReleaseResponseTypeDef(BaseValidatorModel):
    MobileSdkRelease: MobileSdkReleaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    TagInfoForResource: TagInfoForResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRegexPatternSetResponseTypeDef(BaseValidatorModel):
    RegexPatternSet: RegexPatternSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class AllowActionOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutputTypeDef] = None


class CaptchaActionOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutputTypeDef] = None


class ChallengeActionOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutputTypeDef] = None


class CountActionOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutputTypeDef] = None


class BlockActionOutputTypeDef(BaseValidatorModel):
    CustomResponse: Optional[CustomResponseOutputTypeDef] = None


class DataProtectionConfigOutputTypeDef(BaseValidatorModel):
    DataProtections: List[DataProtectionOutputTypeDef]


class DataProtectionConfigTypeDef(BaseValidatorModel):
    DataProtections: Sequence[DataProtectionTypeDef]


class SampledHTTPRequestTypeDef(BaseValidatorModel):
    Request: HTTPRequestTypeDef
    Weight: int
    Timestamp: Optional[datetime] = None
    Action: Optional[str] = None
    RuleNameWithinRuleGroup: Optional[str] = None
    RequestHeadersInserted: Optional[List[HTTPHeaderTypeDef]] = None
    ResponseCodeSent: Optional[int] = None
    Labels: Optional[List[LabelTypeDef]] = None
    CaptchaResponse: Optional[CaptchaResponseTypeDef] = None
    ChallengeResponse: Optional[ChallengeResponseTypeDef] = None
    OverriddenAction: Optional[str] = None


class HeaderMatchPatternUnionTypeDef(BaseValidatorModel):
    pass


class HeadersTypeDef(BaseValidatorModel):
    MatchPattern: HeaderMatchPatternUnionTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType


class FieldToMatchOutputTypeDef(BaseValidatorModel):
    SingleHeader: Optional[SingleHeaderTypeDef] = None
    SingleQueryArgument: Optional[SingleQueryArgumentTypeDef] = None
    AllQueryArguments: Optional[Dict[str, Any]] = None
    UriPath: Optional[Dict[str, Any]] = None
    QueryString: Optional[Dict[str, Any]] = None
    Body: Optional[BodyTypeDef] = None
    Method: Optional[Dict[str, Any]] = None
    JsonBody: Optional[JsonBodyOutputTypeDef] = None
    Headers: Optional[HeadersOutputTypeDef] = None
    Cookies: Optional[CookiesOutputTypeDef] = None
    HeaderOrder: Optional[HeaderOrderTypeDef] = None
    JA3Fingerprint: Optional[JA3FingerprintTypeDef] = None
    JA4Fingerprint: Optional[JA4FingerprintTypeDef] = None


class JsonMatchPatternUnionTypeDef(BaseValidatorModel):
    pass


class JsonBodyTypeDef(BaseValidatorModel):
    MatchPattern: JsonMatchPatternUnionTypeDef
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehaviorType] = None
    OversizeHandling: Optional[OversizeHandlingType] = None


class GetManagedRuleSetResponseTypeDef(BaseValidatorModel):
    ManagedRuleSet: ManagedRuleSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class AWSManagedRulesACFPRuleSetOutputTypeDef(BaseValidatorModel):
    CreationPath: str
    RegistrationPagePath: str
    RequestInspection: RequestInspectionACFPOutputTypeDef
    ResponseInspection: Optional[ResponseInspectionOutputTypeDef] = None
    EnableRegexInPath: Optional[bool] = None


class AWSManagedRulesATPRuleSetOutputTypeDef(BaseValidatorModel):
    LoginPath: str
    RequestInspection: Optional[RequestInspectionTypeDef] = None
    ResponseInspection: Optional[ResponseInspectionOutputTypeDef] = None
    EnableRegexInPath: Optional[bool] = None


class ResponseInspectionHeaderUnionTypeDef(BaseValidatorModel):
    pass


class ResponseInspectionBodyContainsUnionTypeDef(BaseValidatorModel):
    pass


class ResponseInspectionJsonUnionTypeDef(BaseValidatorModel):
    pass


class ResponseInspectionStatusCodeUnionTypeDef(BaseValidatorModel):
    pass


class ResponseInspectionTypeDef(BaseValidatorModel):
    StatusCode: Optional[ResponseInspectionStatusCodeUnionTypeDef] = None
    Header: Optional[ResponseInspectionHeaderUnionTypeDef] = None
    BodyContains: Optional[ResponseInspectionBodyContainsUnionTypeDef] = None
    Json: Optional[ResponseInspectionJsonUnionTypeDef] = None


class RateBasedStatementOutputTypeDef(BaseValidatorModel):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: Optional[int] = None
    ScopeDownStatement: Optional[Dict[str, Any]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfigTypeDef] = None
    CustomKeys: Optional[List[RateBasedStatementCustomKeyOutputTypeDef]] = None


class RateLimitQueryArgumentUnionTypeDef(BaseValidatorModel):
    pass


class RateLimitUriPathUnionTypeDef(BaseValidatorModel):
    pass


class RateLimitCookieUnionTypeDef(BaseValidatorModel):
    pass


class RateLimitHeaderUnionTypeDef(BaseValidatorModel):
    pass


class RateLimitQueryStringUnionTypeDef(BaseValidatorModel):
    pass


class RateBasedStatementCustomKeyTypeDef(BaseValidatorModel):
    Header: Optional[RateLimitHeaderUnionTypeDef] = None
    Cookie: Optional[RateLimitCookieUnionTypeDef] = None
    QueryArgument: Optional[RateLimitQueryArgumentUnionTypeDef] = None
    QueryString: Optional[RateLimitQueryStringUnionTypeDef] = None
    HTTPMethod: Optional[Mapping[str, Any]] = None
    ForwardedIP: Optional[Mapping[str, Any]] = None
    IP: Optional[Mapping[str, Any]] = None
    LabelNamespace: Optional[RateLimitLabelNamespaceTypeDef] = None
    UriPath: Optional[RateLimitUriPathUnionTypeDef] = None
    JA3Fingerprint: Optional[RateLimitJA3FingerprintTypeDef] = None
    JA4Fingerprint: Optional[RateLimitJA4FingerprintTypeDef] = None


class LoggingFilterOutputTypeDef(BaseValidatorModel):
    Filters: List[FilterOutputTypeDef]
    DefaultBehavior: FilterBehaviorType


class LoggingFilterTypeDef(BaseValidatorModel):
    Filters: Sequence[FilterTypeDef]
    DefaultBehavior: FilterBehaviorType


class CustomRequestHandlingUnionTypeDef(BaseValidatorModel):
    pass


class AllowActionTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingUnionTypeDef] = None


class CaptchaActionTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingUnionTypeDef] = None


class ChallengeActionTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingUnionTypeDef] = None


class CountActionTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[CustomRequestHandlingUnionTypeDef] = None


class DefaultActionOutputTypeDef(BaseValidatorModel):
    Block: Optional[BlockActionOutputTypeDef] = None
    Allow: Optional[AllowActionOutputTypeDef] = None


class RuleActionOutputTypeDef(BaseValidatorModel):
    Block: Optional[BlockActionOutputTypeDef] = None
    Allow: Optional[AllowActionOutputTypeDef] = None
    Count: Optional[CountActionOutputTypeDef] = None
    Captcha: Optional[CaptchaActionOutputTypeDef] = None
    Challenge: Optional[ChallengeActionOutputTypeDef] = None


class CustomResponseUnionTypeDef(BaseValidatorModel):
    pass


class BlockActionTypeDef(BaseValidatorModel):
    CustomResponse: Optional[CustomResponseUnionTypeDef] = None


class GetSampledRequestsResponseTypeDef(BaseValidatorModel):
    SampledRequests: List[SampledHTTPRequestTypeDef]
    PopulationSize: int
    TimeWindow: TimeWindowOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ByteMatchStatementOutputTypeDef(BaseValidatorModel):
    SearchString: bytes
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]
    PositionalConstraint: PositionalConstraintType


class RegexMatchStatementOutputTypeDef(BaseValidatorModel):
    RegexString: str
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]


class RegexPatternSetReferenceStatementOutputTypeDef(BaseValidatorModel):
    ARN: str
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]


class SizeConstraintStatementOutputTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchOutputTypeDef
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: List[TextTransformationTypeDef]


class SqliMatchStatementOutputTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]
    SensitivityLevel: Optional[SensitivityLevelType] = None


class XssMatchStatementOutputTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]


class ManagedRuleGroupConfigOutputTypeDef(BaseValidatorModel):
    LoginPath: Optional[str] = None
    PayloadType: Optional[PayloadTypeType] = None
    UsernameField: Optional[UsernameFieldTypeDef] = None
    PasswordField: Optional[PasswordFieldTypeDef] = None
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSetTypeDef] = None
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSetOutputTypeDef] = None
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSetOutputTypeDef] = None


class TimeWindowUnionTypeDef(BaseValidatorModel):
    pass


class GetSampledRequestsRequestTypeDef(BaseValidatorModel):
    WebAclArn: str
    RuleMetricName: str
    Scope: ScopeType
    TimeWindow: TimeWindowUnionTypeDef
    MaxItems: int


class LoggingConfigurationOutputTypeDef(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatchOutputTypeDef]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LoggingFilter: Optional[LoggingFilterOutputTypeDef] = None
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None


class RuleActionOverrideOutputTypeDef(BaseValidatorModel):
    Name: str
    ActionToUse: RuleActionOutputTypeDef


class RuleSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Action: Optional[RuleActionOutputTypeDef] = None


class DefaultActionTypeDef(BaseValidatorModel):
    Block: Optional[BlockActionTypeDef] = None
    Allow: Optional[AllowActionTypeDef] = None


class JsonBodyUnionTypeDef(BaseValidatorModel):
    pass


class HeadersUnionTypeDef(BaseValidatorModel):
    pass


class CookiesUnionTypeDef(BaseValidatorModel):
    pass


class FieldToMatchTypeDef(BaseValidatorModel):
    SingleHeader: Optional[SingleHeaderTypeDef] = None
    SingleQueryArgument: Optional[SingleQueryArgumentTypeDef] = None
    AllQueryArguments: Optional[Mapping[str, Any]] = None
    UriPath: Optional[Mapping[str, Any]] = None
    QueryString: Optional[Mapping[str, Any]] = None
    Body: Optional[BodyTypeDef] = None
    Method: Optional[Mapping[str, Any]] = None
    JsonBody: Optional[JsonBodyUnionTypeDef] = None
    Headers: Optional[HeadersUnionTypeDef] = None
    Cookies: Optional[CookiesUnionTypeDef] = None
    HeaderOrder: Optional[HeaderOrderTypeDef] = None
    JA3Fingerprint: Optional[JA3FingerprintTypeDef] = None
    JA4Fingerprint: Optional[JA4FingerprintTypeDef] = None


class ResponseInspectionUnionTypeDef(BaseValidatorModel):
    pass


class RequestInspectionACFPUnionTypeDef(BaseValidatorModel):
    pass


class AWSManagedRulesACFPRuleSetTypeDef(BaseValidatorModel):
    CreationPath: str
    RegistrationPagePath: str
    RequestInspection: RequestInspectionACFPUnionTypeDef
    ResponseInspection: Optional[ResponseInspectionUnionTypeDef] = None
    EnableRegexInPath: Optional[bool] = None


class AWSManagedRulesATPRuleSetTypeDef(BaseValidatorModel):
    LoginPath: str
    RequestInspection: Optional[RequestInspectionTypeDef] = None
    ResponseInspection: Optional[ResponseInspectionUnionTypeDef] = None
    EnableRegexInPath: Optional[bool] = None


class RateBasedStatementCustomKeyUnionTypeDef(BaseValidatorModel):
    pass


class RateBasedStatementTypeDef(BaseValidatorModel):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: Optional[int] = None
    ScopeDownStatement: Optional[Mapping[str, Any]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfigTypeDef] = None
    CustomKeys: Optional[Sequence[RateBasedStatementCustomKeyUnionTypeDef]] = None


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


class ManagedRuleGroupStatementOutputTypeDef(BaseValidatorModel):
    VendorName: str
    Name: str
    Version: Optional[str] = None
    ExcludedRules: Optional[List[ExcludedRuleTypeDef]] = None
    ScopeDownStatement: Optional[Dict[str, Any]] = None
    ManagedRuleGroupConfigs: Optional[List[ManagedRuleGroupConfigOutputTypeDef]] = None
    RuleActionOverrides: Optional[List[RuleActionOverrideOutputTypeDef]] = None


class RuleGroupReferenceStatementOutputTypeDef(BaseValidatorModel):
    ARN: str
    ExcludedRules: Optional[List[ExcludedRuleTypeDef]] = None
    RuleActionOverrides: Optional[List[RuleActionOverrideOutputTypeDef]] = None


class DescribeManagedRuleGroupResponseTypeDef(BaseValidatorModel):
    VersionName: str
    SnsTopicArn: str
    Capacity: int
    Rules: List[RuleSummaryTypeDef]
    LabelNamespace: str
    AvailableLabels: List[LabelSummaryTypeDef]
    ConsumedLabels: List[LabelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CaptchaActionUnionTypeDef(BaseValidatorModel):
    pass


class AllowActionUnionTypeDef(BaseValidatorModel):
    pass


class CountActionUnionTypeDef(BaseValidatorModel):
    pass


class BlockActionUnionTypeDef(BaseValidatorModel):
    pass


class ChallengeActionUnionTypeDef(BaseValidatorModel):
    pass


class RuleActionTypeDef(BaseValidatorModel):
    Block: Optional[BlockActionUnionTypeDef] = None
    Allow: Optional[AllowActionUnionTypeDef] = None
    Count: Optional[CountActionUnionTypeDef] = None
    Captcha: Optional[CaptchaActionUnionTypeDef] = None
    Challenge: Optional[ChallengeActionUnionTypeDef] = None


class LoggingConfigurationTypeDef(BaseValidatorModel):
    ResourceArn: str
    LogDestinationConfigs: Sequence[str]
    RedactedFields: Optional[Sequence[FieldToMatchTypeDef]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LoggingFilter: Optional[LoggingFilterTypeDef] = None
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None


class FirewallManagerStatementTypeDef(BaseValidatorModel):
    ManagedRuleGroupStatement: Optional[ManagedRuleGroupStatementOutputTypeDef] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementOutputTypeDef] = None


class StatementOutputTypeDef(BaseValidatorModel):
    ByteMatchStatement: Optional[ByteMatchStatementOutputTypeDef] = None
    SqliMatchStatement: Optional[SqliMatchStatementOutputTypeDef] = None
    XssMatchStatement: Optional[XssMatchStatementOutputTypeDef] = None
    SizeConstraintStatement: Optional[SizeConstraintStatementOutputTypeDef] = None
    GeoMatchStatement: Optional[GeoMatchStatementOutputTypeDef] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementOutputTypeDef] = None
    IPSetReferenceStatement: Optional[IPSetReferenceStatementTypeDef] = None
    RegexPatternSetReferenceStatement: Optional[RegexPatternSetReferenceStatementOutputTypeDef] = None
    RateBasedStatement: Optional[RateBasedStatementOutputTypeDef] = None
    AndStatement: Optional[AndStatementOutputTypeDef] = None
    OrStatement: Optional[OrStatementOutputTypeDef] = None
    NotStatement: Optional[NotStatementOutputTypeDef] = None
    ManagedRuleGroupStatement: Optional[ManagedRuleGroupStatementOutputTypeDef] = None
    LabelMatchStatement: Optional[LabelMatchStatementTypeDef] = None
    RegexMatchStatement: Optional[RegexMatchStatementOutputTypeDef] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class FieldToMatchUnionTypeDef(BaseValidatorModel):
    pass


class ByteMatchStatementTypeDef(BaseValidatorModel):
    SearchString: BlobTypeDef
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]
    PositionalConstraint: PositionalConstraintType


class RegexMatchStatementTypeDef(BaseValidatorModel):
    RegexString: str
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]


class RegexPatternSetReferenceStatementTypeDef(BaseValidatorModel):
    ARN: str
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]


class SizeConstraintStatementTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnionTypeDef
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: Sequence[TextTransformationTypeDef]


class SqliMatchStatementTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]
    SensitivityLevel: Optional[SensitivityLevelType] = None


class XssMatchStatementTypeDef(BaseValidatorModel):
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]


class AWSManagedRulesACFPRuleSetUnionTypeDef(BaseValidatorModel):
    pass


class AWSManagedRulesATPRuleSetUnionTypeDef(BaseValidatorModel):
    pass


class ManagedRuleGroupConfigTypeDef(BaseValidatorModel):
    LoginPath: Optional[str] = None
    PayloadType: Optional[PayloadTypeType] = None
    UsernameField: Optional[UsernameFieldTypeDef] = None
    PasswordField: Optional[PasswordFieldTypeDef] = None
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSetTypeDef] = None
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSetUnionTypeDef] = None
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSetUnionTypeDef] = None


class OverrideActionOutputTypeDef(BaseValidatorModel):
    pass


class FirewallManagerRuleGroupTypeDef(BaseValidatorModel):
    Name: str
    Priority: int
    FirewallManagerStatement: FirewallManagerStatementTypeDef
    OverrideAction: OverrideActionOutputTypeDef
    VisibilityConfig: VisibilityConfigTypeDef


class RuleOutputTypeDef(BaseValidatorModel):
    Name: str
    Priority: int
    Statement: StatementOutputTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Action: Optional[RuleActionOutputTypeDef] = None
    OverrideAction: Optional[OverrideActionOutputTypeDef] = None
    RuleLabels: Optional[List[LabelTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None


class RuleActionUnionTypeDef(BaseValidatorModel):
    pass


class RuleActionOverrideTypeDef(BaseValidatorModel):
    Name: str
    ActionToUse: RuleActionUnionTypeDef


class LoggingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationUnionTypeDef


class RuleGroupTypeDef(BaseValidatorModel):
    Name: str
    Id: str
    Capacity: int
    ARN: str
    VisibilityConfig: VisibilityConfigTypeDef
    Description: Optional[str] = None
    Rules: Optional[List[RuleOutputTypeDef]] = None
    LabelNamespace: Optional[str] = None
    CustomResponseBodies: Optional[Dict[str, CustomResponseBodyTypeDef]] = None
    AvailableLabels: Optional[List[LabelSummaryTypeDef]] = None
    ConsumedLabels: Optional[List[LabelSummaryTypeDef]] = None


class WebACLTypeDef(BaseValidatorModel):
    Name: str
    Id: str
    ARN: str
    DefaultAction: DefaultActionOutputTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Description: Optional[str] = None
    Rules: Optional[List[RuleOutputTypeDef]] = None
    DataProtectionConfig: Optional[DataProtectionConfigOutputTypeDef] = None
    Capacity: Optional[int] = None
    PreProcessFirewallManagerRuleGroups: Optional[List[FirewallManagerRuleGroupTypeDef]] = None
    PostProcessFirewallManagerRuleGroups: Optional[List[FirewallManagerRuleGroupTypeDef]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LabelNamespace: Optional[str] = None
    CustomResponseBodies: Optional[Dict[str, CustomResponseBodyTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None
    TokenDomains: Optional[List[str]] = None
    AssociationConfig: Optional[AssociationConfigOutputTypeDef] = None
    RetrofittedByFirewallManager: Optional[bool] = None


class GetRuleGroupResponseTypeDef(BaseValidatorModel):
    RuleGroup: RuleGroupTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetWebACLForResourceResponseTypeDef(BaseValidatorModel):
    WebACL: WebACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetWebACLResponseTypeDef(BaseValidatorModel):
    WebACL: WebACLTypeDef
    LockToken: str
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadataTypeDef


class RuleActionOverrideUnionTypeDef(BaseValidatorModel):
    pass


class ManagedRuleGroupConfigUnionTypeDef(BaseValidatorModel):
    pass


class ManagedRuleGroupStatementTypeDef(BaseValidatorModel):
    VendorName: str
    Name: str
    Version: Optional[str] = None
    ExcludedRules: Optional[Sequence[ExcludedRuleTypeDef]] = None
    ScopeDownStatement: Optional[Mapping[str, Any]] = None
    ManagedRuleGroupConfigs: Optional[Sequence[ManagedRuleGroupConfigUnionTypeDef]] = None
    RuleActionOverrides: Optional[Sequence[RuleActionOverrideUnionTypeDef]] = None


class RuleGroupReferenceStatementTypeDef(BaseValidatorModel):
    ARN: str
    ExcludedRules: Optional[Sequence[ExcludedRuleTypeDef]] = None
    RuleActionOverrides: Optional[Sequence[RuleActionOverrideUnionTypeDef]] = None


class RateBasedStatementUnionTypeDef(BaseValidatorModel):
    pass


class OrStatementUnionTypeDef(BaseValidatorModel):
    pass


class RegexMatchStatementUnionTypeDef(BaseValidatorModel):
    pass


class SizeConstraintStatementUnionTypeDef(BaseValidatorModel):
    pass


class XssMatchStatementUnionTypeDef(BaseValidatorModel):
    pass


class NotStatementUnionTypeDef(BaseValidatorModel):
    pass


class RegexPatternSetReferenceStatementUnionTypeDef(BaseValidatorModel):
    pass


class AndStatementUnionTypeDef(BaseValidatorModel):
    pass


class RuleGroupReferenceStatementUnionTypeDef(BaseValidatorModel):
    pass


class ManagedRuleGroupStatementUnionTypeDef(BaseValidatorModel):
    pass


class ByteMatchStatementUnionTypeDef(BaseValidatorModel):
    pass


class SqliMatchStatementUnionTypeDef(BaseValidatorModel):
    pass


class GeoMatchStatementUnionTypeDef(BaseValidatorModel):
    pass


class StatementTypeDef(BaseValidatorModel):
    ByteMatchStatement: Optional[ByteMatchStatementUnionTypeDef] = None
    SqliMatchStatement: Optional[SqliMatchStatementUnionTypeDef] = None
    XssMatchStatement: Optional[XssMatchStatementUnionTypeDef] = None
    SizeConstraintStatement: Optional[SizeConstraintStatementUnionTypeDef] = None
    GeoMatchStatement: Optional[GeoMatchStatementUnionTypeDef] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementUnionTypeDef] = None
    IPSetReferenceStatement: Optional[IPSetReferenceStatementTypeDef] = None
    RegexPatternSetReferenceStatement: Optional[RegexPatternSetReferenceStatementUnionTypeDef] = None
    RateBasedStatement: Optional[RateBasedStatementUnionTypeDef] = None
    AndStatement: Optional[AndStatementUnionTypeDef] = None
    OrStatement: Optional[OrStatementUnionTypeDef] = None
    NotStatement: Optional[NotStatementUnionTypeDef] = None
    ManagedRuleGroupStatement: Optional[ManagedRuleGroupStatementUnionTypeDef] = None
    LabelMatchStatement: Optional[LabelMatchStatementTypeDef] = None
    RegexMatchStatement: Optional[RegexMatchStatementUnionTypeDef] = None


class StatementUnionTypeDef(BaseValidatorModel):
    pass


class OverrideActionUnionTypeDef(BaseValidatorModel):
    pass


class RuleTypeDef(BaseValidatorModel):
    Name: str
    Priority: int
    Statement: StatementUnionTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Action: Optional[RuleActionUnionTypeDef] = None
    OverrideAction: Optional[OverrideActionUnionTypeDef] = None
    RuleLabels: Optional[Sequence[LabelTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None


class RuleUnionTypeDef(BaseValidatorModel):
    pass


class CheckCapacityRequestTypeDef(BaseValidatorModel):
    Scope: ScopeType
    Rules: Sequence[RuleUnionTypeDef]


class CreateRuleGroupRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Capacity: int
    VisibilityConfig: VisibilityConfigTypeDef
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBodyTypeDef]] = None


class DefaultActionUnionTypeDef(BaseValidatorModel):
    pass


class AssociationConfigUnionTypeDef(BaseValidatorModel):
    pass


class DataProtectionConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateWebACLRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    DefaultAction: DefaultActionUnionTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None
    DataProtectionConfig: Optional[DataProtectionConfigUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBodyTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None
    TokenDomains: Optional[Sequence[str]] = None
    AssociationConfig: Optional[AssociationConfigUnionTypeDef] = None


class UpdateRuleGroupRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    VisibilityConfig: VisibilityConfigTypeDef
    LockToken: str
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBodyTypeDef]] = None


class UpdateWebACLRequestTypeDef(BaseValidatorModel):
    Name: str
    Scope: ScopeType
    Id: str
    DefaultAction: DefaultActionUnionTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    LockToken: str
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None
    DataProtectionConfig: Optional[DataProtectionConfigUnionTypeDef] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBodyTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None
    TokenDomains: Optional[Sequence[str]] = None
    AssociationConfig: Optional[AssociationConfigUnionTypeDef] = None



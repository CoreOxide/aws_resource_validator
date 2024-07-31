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
from aws_resource_validator.pydantic_models.wafv2_constants import *

class APIKeySummaryTypeDef(BaseModel):
    TokenDomains: Optional[List[str]] = None
    APIKey: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Version: Optional[int] = None

class AWSManagedRulesBotControlRuleSetTypeDef(BaseModel):
    InspectionLevel: InspectionLevelType
    EnableMachineLearning: Optional[bool] = None

class ActionConditionTypeDef(BaseModel):
    Action: ActionValueType

class AddressFieldTypeDef(BaseModel):
    Identifier: str

class AndStatementOutputTypeDef(BaseModel):
    Statements: List["StatementOutputTypeDef"]

class AndStatementTypeDef(BaseModel):
    Statements: Sequence["StatementTypeDef"]

class AssociateWebACLRequestRequestTypeDef(BaseModel):
    WebACLArn: str
    ResourceArn: str

class RequestBodyAssociatedResourceTypeConfigTypeDef(BaseModel):
    DefaultSizeInspectionLimit: SizeInspectionLimitType

class BodyTypeDef(BaseModel):
    OversizeHandling: Optional[OversizeHandlingType] = None

class TextTransformationTypeDef(BaseModel):
    Priority: int
    Type: TextTransformationTypeType

class ImmunityTimePropertyTypeDef(BaseModel):
    ImmunityTime: int

class CaptchaResponseTypeDef(BaseModel):
    ResponseCode: Optional[int] = None
    SolveTimestamp: Optional[int] = None
    FailureReason: Optional[FailureReasonType] = None

class ChallengeResponseTypeDef(BaseModel):
    ResponseCode: Optional[int] = None
    SolveTimestamp: Optional[int] = None
    FailureReason: Optional[FailureReasonType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class LabelNameConditionTypeDef(BaseModel):
    LabelName: str

class CookieMatchPatternOutputTypeDef(BaseModel):
    All: Optional[Dict[str, Any]] = None
    IncludedCookies: Optional[List[str]] = None
    ExcludedCookies: Optional[List[str]] = None

class CookieMatchPatternTypeDef(BaseModel):
    All: Optional[Mapping[str, Any]] = None
    IncludedCookies: Optional[Sequence[str]] = None
    ExcludedCookies: Optional[Sequence[str]] = None

class CreateAPIKeyRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    TokenDomains: Sequence[str]

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class IPSetSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None

class RegexTypeDef(BaseModel):
    RegexString: Optional[str] = None

class RegexPatternSetSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None

class CustomResponseBodyTypeDef(BaseModel):
    ContentType: ResponseContentTypeType
    Content: str

class VisibilityConfigTypeDef(BaseModel):
    SampledRequestsEnabled: bool
    CloudWatchMetricsEnabled: bool
    MetricName: str

class RuleGroupSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None

class WebACLSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None

class CustomHTTPHeaderTypeDef(BaseModel):
    Name: str
    Value: str

class DeleteAPIKeyRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    APIKey: str

class DeleteFirewallManagerRuleGroupsRequestRequestTypeDef(BaseModel):
    WebACLArn: str
    WebACLLockToken: str

class DeleteIPSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str

class DeleteLoggingConfigurationRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None

class DeletePermissionPolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DeleteRegexPatternSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str

class DeleteRuleGroupRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str

class DeleteWebACLRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str

class DescribeAllManagedProductsRequestRequestTypeDef(BaseModel):
    Scope: ScopeType

class ManagedProductDescriptorTypeDef(BaseModel):
    VendorName: Optional[str] = None
    ManagedRuleSetName: Optional[str] = None
    ProductId: Optional[str] = None
    ProductLink: Optional[str] = None
    ProductTitle: Optional[str] = None
    ProductDescription: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    IsVersioningSupported: Optional[bool] = None
    IsAdvancedManagedRuleSet: Optional[bool] = None

class DescribeManagedProductsByVendorRequestRequestTypeDef(BaseModel):
    VendorName: str
    Scope: ScopeType

class DescribeManagedRuleGroupRequestRequestTypeDef(BaseModel):
    VendorName: str
    Name: str
    Scope: ScopeType
    VersionName: Optional[str] = None

class LabelSummaryTypeDef(BaseModel):
    Name: Optional[str] = None

class DisassociateWebACLRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class EmailFieldTypeDef(BaseModel):
    Identifier: str

class ExcludedRuleTypeDef(BaseModel):
    Name: str

class HeaderOrderTypeDef(BaseModel):
    OversizeHandling: OversizeHandlingType

class JA3FingerprintTypeDef(BaseModel):
    FallbackBehavior: FallbackBehaviorType

class SingleHeaderTypeDef(BaseModel):
    Name: str

class SingleQueryArgumentTypeDef(BaseModel):
    Name: str

class ForwardedIPConfigTypeDef(BaseModel):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType

class GenerateMobileSdkReleaseUrlRequestRequestTypeDef(BaseModel):
    Platform: PlatformType
    ReleaseVersion: str

class GetDecryptedAPIKeyRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    APIKey: str

class GetIPSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str

class IPSetTypeDef(BaseModel):
    Name: str
    Id: str
    ARN: str
    IPAddressVersion: IPAddressVersionType
    Addresses: List[str]
    Description: Optional[str] = None

class GetLoggingConfigurationRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None

class GetManagedRuleSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str

class GetMobileSdkReleaseRequestRequestTypeDef(BaseModel):
    Platform: PlatformType
    ReleaseVersion: str

class GetPermissionPolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GetRateBasedStatementManagedKeysRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    WebACLName: str
    WebACLId: str
    RuleName: str
    RuleGroupRuleName: Optional[str] = None

class RateBasedStatementManagedKeysIPSetTypeDef(BaseModel):
    IPAddressVersion: Optional[IPAddressVersionType] = None
    Addresses: Optional[List[str]] = None

class GetRegexPatternSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str

class GetRuleGroupRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    Scope: Optional[ScopeType] = None
    Id: Optional[str] = None
    ARN: Optional[str] = None

class TimeWindowOutputTypeDef(BaseModel):
    StartTime: datetime
    EndTime: datetime

class GetWebACLForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GetWebACLRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str

class HTTPHeaderTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class HeaderMatchPatternOutputTypeDef(BaseModel):
    All: Optional[Dict[str, Any]] = None
    IncludedHeaders: Optional[List[str]] = None
    ExcludedHeaders: Optional[List[str]] = None

class HeaderMatchPatternTypeDef(BaseModel):
    All: Optional[Mapping[str, Any]] = None
    IncludedHeaders: Optional[Sequence[str]] = None
    ExcludedHeaders: Optional[Sequence[str]] = None

class IPSetForwardedIPConfigTypeDef(BaseModel):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType
    Position: ForwardedIPPositionType

class JsonMatchPatternOutputTypeDef(BaseModel):
    All: Optional[Dict[str, Any]] = None
    IncludedPaths: Optional[List[str]] = None

class JsonMatchPatternTypeDef(BaseModel):
    All: Optional[Mapping[str, Any]] = None
    IncludedPaths: Optional[Sequence[str]] = None

class LabelMatchStatementTypeDef(BaseModel):
    Scope: LabelMatchScopeType
    Key: str

class LabelTypeDef(BaseModel):
    Name: str

class ListAPIKeysRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef(BaseModel):
    VendorName: str
    Name: str
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ManagedRuleGroupVersionTypeDef(BaseModel):
    Name: Optional[str] = None
    LastUpdateTimestamp: Optional[datetime] = None

class ListAvailableManagedRuleGroupsRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ManagedRuleGroupSummaryTypeDef(BaseModel):
    VendorName: Optional[str] = None
    Name: Optional[str] = None
    VersioningSupported: Optional[bool] = None
    Description: Optional[str] = None

class ListIPSetsRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListLoggingConfigurationsRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None
    LogScope: Optional[LogScopeType] = None

class ListManagedRuleSetsRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ManagedRuleSetSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Description: Optional[str] = None
    LockToken: Optional[str] = None
    ARN: Optional[str] = None
    LabelNamespace: Optional[str] = None

class ListMobileSdkReleasesRequestRequestTypeDef(BaseModel):
    Platform: PlatformType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ReleaseSummaryTypeDef(BaseModel):
    ReleaseVersion: Optional[str] = None
    Timestamp: Optional[datetime] = None

class ListRegexPatternSetsRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListResourcesForWebACLRequestRequestTypeDef(BaseModel):
    WebACLArn: str
    ResourceType: Optional[ResourceTypeType] = None

class ListRuleGroupsRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class ListWebACLsRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    NextMarker: Optional[str] = None
    Limit: Optional[int] = None

class PasswordFieldTypeDef(BaseModel):
    Identifier: str

class UsernameFieldTypeDef(BaseModel):
    Identifier: str

class ManagedRuleSetVersionTypeDef(BaseModel):
    AssociatedRuleGroupArn: Optional[str] = None
    Capacity: Optional[int] = None
    ForecastedLifetime: Optional[int] = None
    PublishTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    ExpiryTimestamp: Optional[datetime] = None

class NotStatementTypeDef(BaseModel):
    Statement: "StatementTypeDef"

class OrStatementOutputTypeDef(BaseModel):
    Statements: List["StatementOutputTypeDef"]

class OrStatementTypeDef(BaseModel):
    Statements: Sequence["StatementTypeDef"]

class PhoneNumberFieldTypeDef(BaseModel):
    Identifier: str

class VersionToPublishTypeDef(BaseModel):
    AssociatedRuleGroupArn: Optional[str] = None
    ForecastedLifetime: Optional[int] = None

class PutPermissionPolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Policy: str

class RateLimitLabelNamespaceTypeDef(BaseModel):
    Namespace: str

class ResponseInspectionBodyContainsOutputTypeDef(BaseModel):
    SuccessStrings: List[str]
    FailureStrings: List[str]

class ResponseInspectionBodyContainsTypeDef(BaseModel):
    SuccessStrings: Sequence[str]
    FailureStrings: Sequence[str]

class ResponseInspectionHeaderOutputTypeDef(BaseModel):
    Name: str
    SuccessValues: List[str]
    FailureValues: List[str]

class ResponseInspectionHeaderTypeDef(BaseModel):
    Name: str
    SuccessValues: Sequence[str]
    FailureValues: Sequence[str]

class ResponseInspectionJsonOutputTypeDef(BaseModel):
    Identifier: str
    SuccessValues: List[str]
    FailureValues: List[str]

class ResponseInspectionJsonTypeDef(BaseModel):
    Identifier: str
    SuccessValues: Sequence[str]
    FailureValues: Sequence[str]

class ResponseInspectionStatusCodeOutputTypeDef(BaseModel):
    SuccessCodes: List[int]
    FailureCodes: List[int]

class ResponseInspectionStatusCodeTypeDef(BaseModel):
    SuccessCodes: Sequence[int]
    FailureCodes: Sequence[int]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateIPSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    Addresses: Sequence[str]
    LockToken: str
    Description: Optional[str] = None

class AssociationConfigOutputTypeDef(BaseModel):
    RequestBody: Optional[       Dict[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfigTypeDef] = None

class AssociationConfigTypeDef(BaseModel):
    RequestBody: Optional[       Mapping[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfigTypeDef] = None

class RateLimitCookieOutputTypeDef(BaseModel):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitCookieTypeDef(BaseModel):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]

class RateLimitHeaderOutputTypeDef(BaseModel):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitHeaderTypeDef(BaseModel):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]

class RateLimitQueryArgumentOutputTypeDef(BaseModel):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitQueryArgumentTypeDef(BaseModel):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]

class RateLimitQueryStringOutputTypeDef(BaseModel):
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitQueryStringTypeDef(BaseModel):
    TextTransformations: Sequence[TextTransformationTypeDef]

class RateLimitUriPathOutputTypeDef(BaseModel):
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitUriPathTypeDef(BaseModel):
    TextTransformations: Sequence[TextTransformationTypeDef]

class CaptchaConfigTypeDef(BaseModel):
    ImmunityTimeProperty: Optional[ImmunityTimePropertyTypeDef] = None

class ChallengeConfigTypeDef(BaseModel):
    ImmunityTimeProperty: Optional[ImmunityTimePropertyTypeDef] = None

class CheckCapacityResponseTypeDef(BaseModel):
    Capacity: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAPIKeyResponseTypeDef(BaseModel):
    APIKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallManagerRuleGroupsResponseTypeDef(BaseModel):
    NextWebACLLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMobileSdkReleaseUrlResponseTypeDef(BaseModel):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDecryptedAPIKeyResponseTypeDef(BaseModel):
    TokenDomains: List[str]
    CreationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionPolicyResponseTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAPIKeysResponseTypeDef(BaseModel):
    NextMarker: str
    APIKeySummaries: List[APIKeySummaryTypeDef]
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesForWebACLResponseTypeDef(BaseModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedRuleSetVersionsResponseTypeDef(BaseModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIPSetResponseTypeDef(BaseModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateManagedRuleSetVersionExpiryDateResponseTypeDef(BaseModel):
    ExpiringVersion: str
    ExpiryTimestamp: datetime
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexPatternSetResponseTypeDef(BaseModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupResponseTypeDef(BaseModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebACLResponseTypeDef(BaseModel):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConditionTypeDef(BaseModel):
    ActionCondition: Optional[ActionConditionTypeDef] = None
    LabelNameCondition: Optional[LabelNameConditionTypeDef] = None

class CookiesOutputTypeDef(BaseModel):
    MatchPattern: CookieMatchPatternOutputTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

class CookiesTypeDef(BaseModel):
    MatchPattern: CookieMatchPatternTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

class CreateIPSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    IPAddressVersion: IPAddressVersionType
    Addresses: Sequence[str]
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MobileSdkReleaseTypeDef(BaseModel):
    ReleaseVersion: Optional[str] = None
    Timestamp: Optional[datetime] = None
    ReleaseNotes: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagInfoForResourceTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    TagList: Optional[List[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateIPSetResponseTypeDef(BaseModel):
    Summary: IPSetSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIPSetsResponseTypeDef(BaseModel):
    NextMarker: str
    IPSets: List[IPSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegexPatternSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    RegularExpressionList: Sequence[RegexTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class RegexPatternSetTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    ARN: Optional[str] = None
    Description: Optional[str] = None
    RegularExpressionList: Optional[List[RegexTypeDef]] = None

class UpdateRegexPatternSetRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    RegularExpressionList: Sequence[RegexTypeDef]
    LockToken: str
    Description: Optional[str] = None

class CreateRegexPatternSetResponseTypeDef(BaseModel):
    Summary: RegexPatternSetSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRegexPatternSetsResponseTypeDef(BaseModel):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupResponseTypeDef(BaseModel):
    Summary: RuleGroupSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRuleGroupsResponseTypeDef(BaseModel):
    NextMarker: str
    RuleGroups: List[RuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWebACLResponseTypeDef(BaseModel):
    Summary: WebACLSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebACLsResponseTypeDef(BaseModel):
    NextMarker: str
    WebACLs: List[WebACLSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomRequestHandlingOutputTypeDef(BaseModel):
    InsertHeaders: List[CustomHTTPHeaderTypeDef]

class CustomRequestHandlingTypeDef(BaseModel):
    InsertHeaders: Sequence[CustomHTTPHeaderTypeDef]

class CustomResponseOutputTypeDef(BaseModel):
    ResponseCode: int
    CustomResponseBodyKey: Optional[str] = None
    ResponseHeaders: Optional[List[CustomHTTPHeaderTypeDef]] = None

class CustomResponseTypeDef(BaseModel):
    ResponseCode: int
    CustomResponseBodyKey: Optional[str] = None
    ResponseHeaders: Optional[Sequence[CustomHTTPHeaderTypeDef]] = None

class DescribeAllManagedProductsResponseTypeDef(BaseModel):
    ManagedProducts: List[ManagedProductDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeManagedProductsByVendorResponseTypeDef(BaseModel):
    ManagedProducts: List[ManagedProductDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GeoMatchStatementOutputTypeDef(BaseModel):
    CountryCodes: Optional[List[CountryCodeType]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfigTypeDef] = None

class GeoMatchStatementTypeDef(BaseModel):
    CountryCodes: Optional[Sequence[CountryCodeType]] = None
    ForwardedIPConfig: Optional[ForwardedIPConfigTypeDef] = None

class GetIPSetResponseTypeDef(BaseModel):
    IPSet: IPSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedStatementManagedKeysResponseTypeDef(BaseModel):
    ManagedKeysIPV4: RateBasedStatementManagedKeysIPSetTypeDef
    ManagedKeysIPV6: RateBasedStatementManagedKeysIPSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HTTPRequestTypeDef(BaseModel):
    ClientIP: Optional[str] = None
    Country: Optional[str] = None
    URI: Optional[str] = None
    Method: Optional[str] = None
    HTTPVersion: Optional[str] = None
    Headers: Optional[List[HTTPHeaderTypeDef]] = None

class HeadersOutputTypeDef(BaseModel):
    MatchPattern: HeaderMatchPatternOutputTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

class HeadersTypeDef(BaseModel):
    MatchPattern: HeaderMatchPatternTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

class IPSetReferenceStatementTypeDef(BaseModel):
    ARN: str
    IPSetForwardedIPConfig: Optional[IPSetForwardedIPConfigTypeDef] = None

class JsonBodyOutputTypeDef(BaseModel):
    MatchPattern: JsonMatchPatternOutputTypeDef
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehaviorType] = None
    OversizeHandling: Optional[OversizeHandlingType] = None

class JsonBodyTypeDef(BaseModel):
    MatchPattern: JsonMatchPatternTypeDef
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehaviorType] = None
    OversizeHandling: Optional[OversizeHandlingType] = None

class ListAvailableManagedRuleGroupVersionsResponseTypeDef(BaseModel):
    NextMarker: str
    Versions: List[ManagedRuleGroupVersionTypeDef]
    CurrentDefaultVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableManagedRuleGroupsResponseTypeDef(BaseModel):
    NextMarker: str
    ManagedRuleGroups: List[ManagedRuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedRuleSetsResponseTypeDef(BaseModel):
    NextMarker: str
    ManagedRuleSets: List[ManagedRuleSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMobileSdkReleasesResponseTypeDef(BaseModel):
    ReleaseSummaries: List[ReleaseSummaryTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RequestInspectionTypeDef(BaseModel):
    PayloadType: PayloadTypeType
    UsernameField: UsernameFieldTypeDef
    PasswordField: PasswordFieldTypeDef

class ManagedRuleSetTypeDef(BaseModel):
    Name: str
    Id: str
    ARN: str
    Description: Optional[str] = None
    PublishedVersions: Optional[Dict[str, ManagedRuleSetVersionTypeDef]] = None
    RecommendedVersion: Optional[str] = None
    LabelNamespace: Optional[str] = None

class RequestInspectionACFPOutputTypeDef(BaseModel):
    PayloadType: PayloadTypeType
    UsernameField: Optional[UsernameFieldTypeDef] = None
    PasswordField: Optional[PasswordFieldTypeDef] = None
    EmailField: Optional[EmailFieldTypeDef] = None
    PhoneNumberFields: Optional[List[PhoneNumberFieldTypeDef]] = None
    AddressFields: Optional[List[AddressFieldTypeDef]] = None

class RequestInspectionACFPTypeDef(BaseModel):
    PayloadType: PayloadTypeType
    UsernameField: Optional[UsernameFieldTypeDef] = None
    PasswordField: Optional[PasswordFieldTypeDef] = None
    EmailField: Optional[EmailFieldTypeDef] = None
    PhoneNumberFields: Optional[Sequence[PhoneNumberFieldTypeDef]] = None
    AddressFields: Optional[Sequence[AddressFieldTypeDef]] = None

class PutManagedRuleSetVersionsRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    RecommendedVersion: Optional[str] = None
    VersionsToPublish: Optional[Mapping[str, VersionToPublishTypeDef]] = None

class ResponseInspectionOutputTypeDef(BaseModel):
    StatusCode: Optional[ResponseInspectionStatusCodeOutputTypeDef] = None
    Header: Optional[ResponseInspectionHeaderOutputTypeDef] = None
    BodyContains: Optional[ResponseInspectionBodyContainsOutputTypeDef] = None
    Json: Optional[ResponseInspectionJsonOutputTypeDef] = None

class ResponseInspectionTypeDef(BaseModel):
    StatusCode: Optional[ResponseInspectionStatusCodeTypeDef] = None
    Header: Optional[ResponseInspectionHeaderTypeDef] = None
    BodyContains: Optional[ResponseInspectionBodyContainsTypeDef] = None
    Json: Optional[ResponseInspectionJsonTypeDef] = None

class TimeWindowTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    VersionToExpire: str
    ExpiryTimestamp: TimestampTypeDef

class RateBasedStatementCustomKeyOutputTypeDef(BaseModel):
    Header: Optional[RateLimitHeaderOutputTypeDef] = None
    Cookie: Optional[RateLimitCookieOutputTypeDef] = None
    QueryArgument: Optional[RateLimitQueryArgumentOutputTypeDef] = None
    QueryString: Optional[RateLimitQueryStringOutputTypeDef] = None
    HTTPMethod: Optional[Dict[str, Any]] = None
    ForwardedIP: Optional[Dict[str, Any]] = None
    IP: Optional[Dict[str, Any]] = None
    LabelNamespace: Optional[RateLimitLabelNamespaceTypeDef] = None
    UriPath: Optional[RateLimitUriPathOutputTypeDef] = None

class RateBasedStatementCustomKeyTypeDef(BaseModel):
    Header: Optional[RateLimitHeaderTypeDef] = None
    Cookie: Optional[RateLimitCookieTypeDef] = None
    QueryArgument: Optional[RateLimitQueryArgumentTypeDef] = None
    QueryString: Optional[RateLimitQueryStringTypeDef] = None
    HTTPMethod: Optional[Mapping[str, Any]] = None
    ForwardedIP: Optional[Mapping[str, Any]] = None
    IP: Optional[Mapping[str, Any]] = None
    LabelNamespace: Optional[RateLimitLabelNamespaceTypeDef] = None
    UriPath: Optional[RateLimitUriPathTypeDef] = None

class FilterOutputTypeDef(BaseModel):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: List[ConditionTypeDef]

class FilterTypeDef(BaseModel):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: Sequence[ConditionTypeDef]

class GetMobileSdkReleaseResponseTypeDef(BaseModel):
    MobileSdkRelease: MobileSdkReleaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    NextMarker: str
    TagInfoForResource: TagInfoForResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegexPatternSetResponseTypeDef(BaseModel):
    RegexPatternSet: RegexPatternSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AllowActionOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutputTypeDef] = None

class CaptchaActionOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutputTypeDef] = None

class ChallengeActionOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutputTypeDef] = None

class CountActionOutputTypeDef(BaseModel):
    CustomRequestHandling: Optional[CustomRequestHandlingOutputTypeDef] = None

class AllowActionTypeDef(BaseModel):
    CustomRequestHandling: Optional[CustomRequestHandlingTypeDef] = None

class CaptchaActionTypeDef(BaseModel):
    CustomRequestHandling: Optional[CustomRequestHandlingTypeDef] = None

class ChallengeActionTypeDef(BaseModel):
    CustomRequestHandling: Optional[CustomRequestHandlingTypeDef] = None

class CountActionTypeDef(BaseModel):
    CustomRequestHandling: Optional[CustomRequestHandlingTypeDef] = None

class BlockActionOutputTypeDef(BaseModel):
    CustomResponse: Optional[CustomResponseOutputTypeDef] = None

class BlockActionTypeDef(BaseModel):
    CustomResponse: Optional[CustomResponseTypeDef] = None

class SampledHTTPRequestTypeDef(BaseModel):
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

class FieldToMatchOutputTypeDef(BaseModel):
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

class FieldToMatchTypeDef(BaseModel):
    SingleHeader: Optional[SingleHeaderTypeDef] = None
    SingleQueryArgument: Optional[SingleQueryArgumentTypeDef] = None
    AllQueryArguments: Optional[Mapping[str, Any]] = None
    UriPath: Optional[Mapping[str, Any]] = None
    QueryString: Optional[Mapping[str, Any]] = None
    Body: Optional[BodyTypeDef] = None
    Method: Optional[Mapping[str, Any]] = None
    JsonBody: Optional[JsonBodyTypeDef] = None
    Headers: Optional[HeadersTypeDef] = None
    Cookies: Optional[CookiesTypeDef] = None
    HeaderOrder: Optional[HeaderOrderTypeDef] = None
    JA3Fingerprint: Optional[JA3FingerprintTypeDef] = None

class GetManagedRuleSetResponseTypeDef(BaseModel):
    ManagedRuleSet: ManagedRuleSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AWSManagedRulesACFPRuleSetOutputTypeDef(BaseModel):
    CreationPath: str
    RegistrationPagePath: str
    RequestInspection: RequestInspectionACFPOutputTypeDef
    ResponseInspection: Optional[ResponseInspectionOutputTypeDef] = None
    EnableRegexInPath: Optional[bool] = None

class AWSManagedRulesATPRuleSetOutputTypeDef(BaseModel):
    LoginPath: str
    RequestInspection: Optional[RequestInspectionTypeDef] = None
    ResponseInspection: Optional[ResponseInspectionOutputTypeDef] = None
    EnableRegexInPath: Optional[bool] = None

class AWSManagedRulesACFPRuleSetTypeDef(BaseModel):
    CreationPath: str
    RegistrationPagePath: str
    RequestInspection: RequestInspectionACFPTypeDef
    ResponseInspection: Optional[ResponseInspectionTypeDef] = None
    EnableRegexInPath: Optional[bool] = None

class AWSManagedRulesATPRuleSetTypeDef(BaseModel):
    LoginPath: str
    RequestInspection: Optional[RequestInspectionTypeDef] = None
    ResponseInspection: Optional[ResponseInspectionTypeDef] = None
    EnableRegexInPath: Optional[bool] = None

class GetSampledRequestsRequestRequestTypeDef(BaseModel):
    WebAclArn: str
    RuleMetricName: str
    Scope: ScopeType
    TimeWindow: TimeWindowTypeDef
    MaxItems: int

class RateBasedStatementOutputTypeDef(BaseModel):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: Optional[int] = None
    ScopeDownStatement: Optional["StatementOutputTypeDef"] = None
    ForwardedIPConfig: Optional[ForwardedIPConfigTypeDef] = None
    CustomKeys: Optional[List[RateBasedStatementCustomKeyOutputTypeDef]] = None

class RateBasedStatementTypeDef(BaseModel):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: Optional[int] = None
    ScopeDownStatement: Optional["StatementTypeDef"] = None
    ForwardedIPConfig: Optional[ForwardedIPConfigTypeDef] = None
    CustomKeys: Optional[Sequence[RateBasedStatementCustomKeyTypeDef]] = None

class LoggingFilterOutputTypeDef(BaseModel):
    Filters: List[FilterOutputTypeDef]
    DefaultBehavior: FilterBehaviorType

class LoggingFilterTypeDef(BaseModel):
    Filters: Sequence[FilterTypeDef]
    DefaultBehavior: FilterBehaviorType

class OverrideActionOutputTypeDef(BaseModel):
    Count: Optional[CountActionOutputTypeDef] = None
    None: Optional[Dict[str, Any]] = None

class OverrideActionTypeDef(BaseModel):
    Count: Optional[CountActionTypeDef] = None
    None: Optional[Mapping[str, Any]] = None

class DefaultActionOutputTypeDef(BaseModel):
    Block: Optional[BlockActionOutputTypeDef] = None
    Allow: Optional[AllowActionOutputTypeDef] = None

class RuleActionOutputTypeDef(BaseModel):
    Block: Optional[BlockActionOutputTypeDef] = None
    Allow: Optional[AllowActionOutputTypeDef] = None
    Count: Optional[CountActionOutputTypeDef] = None
    Captcha: Optional[CaptchaActionOutputTypeDef] = None
    Challenge: Optional[ChallengeActionOutputTypeDef] = None

class DefaultActionTypeDef(BaseModel):
    Block: Optional[BlockActionTypeDef] = None
    Allow: Optional[AllowActionTypeDef] = None

class RuleActionTypeDef(BaseModel):
    Block: Optional[BlockActionTypeDef] = None
    Allow: Optional[AllowActionTypeDef] = None
    Count: Optional[CountActionTypeDef] = None
    Captcha: Optional[CaptchaActionTypeDef] = None
    Challenge: Optional[ChallengeActionTypeDef] = None

class GetSampledRequestsResponseTypeDef(BaseModel):
    SampledRequests: List[SampledHTTPRequestTypeDef]
    PopulationSize: int
    TimeWindow: TimeWindowOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ByteMatchStatementOutputTypeDef(BaseModel):
    SearchString: bytes
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]
    PositionalConstraint: PositionalConstraintType

class RegexMatchStatementOutputTypeDef(BaseModel):
    RegexString: str
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]

class RegexPatternSetReferenceStatementOutputTypeDef(BaseModel):
    ARN: str
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]

class SizeConstraintStatementOutputTypeDef(BaseModel):
    FieldToMatch: FieldToMatchOutputTypeDef
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: List[TextTransformationTypeDef]

class SqliMatchStatementOutputTypeDef(BaseModel):
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]
    SensitivityLevel: Optional[SensitivityLevelType] = None

class XssMatchStatementOutputTypeDef(BaseModel):
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]

class ByteMatchStatementTypeDef(BaseModel):
    SearchString: BlobTypeDef
    FieldToMatch: FieldToMatchTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]
    PositionalConstraint: PositionalConstraintType

class RegexMatchStatementTypeDef(BaseModel):
    RegexString: str
    FieldToMatch: FieldToMatchTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]

class RegexPatternSetReferenceStatementTypeDef(BaseModel):
    ARN: str
    FieldToMatch: FieldToMatchTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]

class SizeConstraintStatementTypeDef(BaseModel):
    FieldToMatch: FieldToMatchTypeDef
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: Sequence[TextTransformationTypeDef]

class SqliMatchStatementTypeDef(BaseModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]
    SensitivityLevel: Optional[SensitivityLevelType] = None

class XssMatchStatementTypeDef(BaseModel):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]

class ManagedRuleGroupConfigOutputTypeDef(BaseModel):
    LoginPath: Optional[str] = None
    PayloadType: Optional[PayloadTypeType] = None
    UsernameField: Optional[UsernameFieldTypeDef] = None
    PasswordField: Optional[PasswordFieldTypeDef] = None
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSetTypeDef] = None
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSetOutputTypeDef] = None
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSetOutputTypeDef] = None

class ManagedRuleGroupConfigTypeDef(BaseModel):
    LoginPath: Optional[str] = None
    PayloadType: Optional[PayloadTypeType] = None
    UsernameField: Optional[UsernameFieldTypeDef] = None
    PasswordField: Optional[PasswordFieldTypeDef] = None
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSetTypeDef] = None
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSetTypeDef] = None
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSetTypeDef] = None

class LoggingConfigurationOutputTypeDef(BaseModel):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: Optional[List[FieldToMatchOutputTypeDef]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LoggingFilter: Optional[LoggingFilterOutputTypeDef] = None
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None

class LoggingConfigurationTypeDef(BaseModel):
    ResourceArn: str
    LogDestinationConfigs: Sequence[str]
    RedactedFields: Optional[Sequence[FieldToMatchTypeDef]] = None
    ManagedByFirewallManager: Optional[bool] = None
    LoggingFilter: Optional[LoggingFilterTypeDef] = None
    LogType: Optional[Literal["WAF_LOGS"]] = None
    LogScope: Optional[LogScopeType] = None

class RuleActionOverrideOutputTypeDef(BaseModel):
    Name: str
    ActionToUse: RuleActionOutputTypeDef

class RuleOutputTypeDef(BaseModel):
    Name: str
    Priority: int
    Statement: "StatementOutputTypeDef"
    VisibilityConfig: VisibilityConfigTypeDef
    Action: Optional[RuleActionOutputTypeDef] = None
    OverrideAction: Optional[OverrideActionOutputTypeDef] = None
    RuleLabels: Optional[List[LabelTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None

class RuleSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Action: Optional[RuleActionOutputTypeDef] = None

class RuleActionOverrideTypeDef(BaseModel):
    Name: str
    ActionToUse: RuleActionTypeDef

class RuleTypeDef(BaseModel):
    Name: str
    Priority: int
    Statement: "StatementTypeDef"
    VisibilityConfig: VisibilityConfigTypeDef
    Action: Optional[RuleActionTypeDef] = None
    OverrideAction: Optional[OverrideActionTypeDef] = None
    RuleLabels: Optional[Sequence[LabelTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None

class GetLoggingConfigurationResponseTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggingConfigurationsResponseTypeDef(BaseModel):
    LoggingConfigurations: List[LoggingConfigurationOutputTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingConfigurationResponseTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingConfigurationRequestRequestTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationTypeDef

class ManagedRuleGroupStatementOutputTypeDef(BaseModel):
    VendorName: str
    Name: str
    Version: Optional[str] = None
    ExcludedRules: Optional[List[ExcludedRuleTypeDef]] = None
    ScopeDownStatement: Optional["StatementOutputTypeDef"] = None
    ManagedRuleGroupConfigs: Optional[List[ManagedRuleGroupConfigOutputTypeDef]] = None
    RuleActionOverrides: Optional[List[RuleActionOverrideOutputTypeDef]] = None

class RuleGroupReferenceStatementOutputTypeDef(BaseModel):
    ARN: str
    ExcludedRules: Optional[List[ExcludedRuleTypeDef]] = None
    RuleActionOverrides: Optional[List[RuleActionOverrideOutputTypeDef]] = None

class RuleGroupTypeDef(BaseModel):
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

class DescribeManagedRuleGroupResponseTypeDef(BaseModel):
    VersionName: str
    SnsTopicArn: str
    Capacity: int
    Rules: List[RuleSummaryTypeDef]
    LabelNamespace: str
    AvailableLabels: List[LabelSummaryTypeDef]
    ConsumedLabels: List[LabelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedRuleGroupStatementTypeDef(BaseModel):
    VendorName: str
    Name: str
    Version: Optional[str] = None
    ExcludedRules: Optional[Sequence[ExcludedRuleTypeDef]] = None
    ScopeDownStatement: Optional["StatementTypeDef"] = None
    ManagedRuleGroupConfigs: Optional[Sequence[ManagedRuleGroupConfigTypeDef]] = None
    RuleActionOverrides: Optional[Sequence[RuleActionOverrideTypeDef]] = None

class RuleGroupReferenceStatementTypeDef(BaseModel):
    ARN: str
    ExcludedRules: Optional[Sequence[ExcludedRuleTypeDef]] = None
    RuleActionOverrides: Optional[Sequence[RuleActionOverrideTypeDef]] = None

class FirewallManagerStatementTypeDef(BaseModel):
    ManagedRuleGroupStatement: Optional[ManagedRuleGroupStatementOutputTypeDef] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementOutputTypeDef] = None

class StatementOutputTypeDef(BaseModel):
    ByteMatchStatement: Optional[ByteMatchStatementOutputTypeDef] = None
    SqliMatchStatement: Optional[SqliMatchStatementOutputTypeDef] = None
    XssMatchStatement: Optional[XssMatchStatementOutputTypeDef] = None
    SizeConstraintStatement: Optional[SizeConstraintStatementOutputTypeDef] = None
    GeoMatchStatement: Optional[GeoMatchStatementOutputTypeDef] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementOutputTypeDef] = None
    IPSetReferenceStatement: Optional[IPSetReferenceStatementTypeDef] = None
    RegexPatternSetReferenceStatement: Optional[       RegexPatternSetReferenceStatementOutputTypeDef     ] = None
    RateBasedStatement: Optional[Dict[str, Any]] = None
    AndStatement: Optional[Dict[str, Any]] = None
    OrStatement: Optional[Dict[str, Any]] = None
    NotStatement: Optional[NotStatementTypeDef] = None
    ManagedRuleGroupStatement: Optional[Dict[str, Any]] = None
    LabelMatchStatement: Optional[LabelMatchStatementTypeDef] = None
    RegexMatchStatement: Optional[RegexMatchStatementOutputTypeDef] = None

class GetRuleGroupResponseTypeDef(BaseModel):
    RuleGroup: RuleGroupTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StatementTypeDef(BaseModel):
    ByteMatchStatement: Optional[ByteMatchStatementTypeDef] = None
    SqliMatchStatement: Optional[SqliMatchStatementTypeDef] = None
    XssMatchStatement: Optional[XssMatchStatementTypeDef] = None
    SizeConstraintStatement: Optional[SizeConstraintStatementTypeDef] = None
    GeoMatchStatement: Optional[GeoMatchStatementTypeDef] = None
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatementTypeDef] = None
    IPSetReferenceStatement: Optional[IPSetReferenceStatementTypeDef] = None
    RegexPatternSetReferenceStatement: Optional[RegexPatternSetReferenceStatementTypeDef] = None
    RateBasedStatement: Optional[Dict[str, Any]] = None
    AndStatement: Optional[Dict[str, Any]] = None
    OrStatement: Optional[Dict[str, Any]] = None
    NotStatement: Optional[Dict[str, Any]] = None
    ManagedRuleGroupStatement: Optional[Dict[str, Any]] = None
    LabelMatchStatement: Optional[LabelMatchStatementTypeDef] = None
    RegexMatchStatement: Optional[RegexMatchStatementTypeDef] = None

class CheckCapacityRequestRequestTypeDef(BaseModel):
    Scope: ScopeType
    Rules: Sequence[RuleUnionTypeDef]

class CreateRuleGroupRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Capacity: int
    VisibilityConfig: VisibilityConfigTypeDef
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBodyTypeDef]] = None

class CreateWebACLRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    DefaultAction: DefaultActionTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBodyTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None
    TokenDomains: Optional[Sequence[str]] = None
    AssociationConfig: Optional[AssociationConfigTypeDef] = None

class UpdateRuleGroupRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    VisibilityConfig: VisibilityConfigTypeDef
    LockToken: str
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBodyTypeDef]] = None

class UpdateWebACLRequestRequestTypeDef(BaseModel):
    Name: str
    Scope: ScopeType
    Id: str
    DefaultAction: DefaultActionTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    LockToken: str
    Description: Optional[str] = None
    Rules: Optional[Sequence[RuleUnionTypeDef]] = None
    CustomResponseBodies: Optional[Mapping[str, CustomResponseBodyTypeDef]] = None
    CaptchaConfig: Optional[CaptchaConfigTypeDef] = None
    ChallengeConfig: Optional[ChallengeConfigTypeDef] = None
    TokenDomains: Optional[Sequence[str]] = None
    AssociationConfig: Optional[AssociationConfigTypeDef] = None

class FirewallManagerRuleGroupTypeDef(BaseModel):
    Name: str
    Priority: int
    FirewallManagerStatement: FirewallManagerStatementTypeDef
    OverrideAction: OverrideActionOutputTypeDef
    VisibilityConfig: VisibilityConfigTypeDef

class WebACLTypeDef(BaseModel):
    Name: str
    Id: str
    ARN: str
    DefaultAction: DefaultActionOutputTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Description: Optional[str] = None
    Rules: Optional[List[RuleOutputTypeDef]] = None
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

class GetWebACLForResourceResponseTypeDef(BaseModel):
    WebACL: WebACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebACLResponseTypeDef(BaseModel):
    WebACL: WebACLTypeDef
    LockToken: str
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadataTypeDef


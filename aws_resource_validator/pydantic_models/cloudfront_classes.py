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
from aws_resource_validator.pydantic_models.cloudfront_constants import *

class AliasICPRecordalTypeDef(BaseModel):
    CNAME: Optional[str] = None
    ICPRecordalStatus: Optional[ICPRecordalStatusType] = None

class AliasesOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class AliasesTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class CachedMethodsOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[MethodType]

class CachedMethodsTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[MethodType]

class AssociateAliasRequestRequestTypeDef(BaseModel):
    TargetDistributionId: str
    Alias: str

class TrustedKeyGroupsOutputTypeDef(BaseModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[str]] = None

class TrustedSignersOutputTypeDef(BaseModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[str]] = None

class TrustedKeyGroupsTypeDef(BaseModel):
    Enabled: bool
    Quantity: int
    Items: Optional[Sequence[str]] = None

class TrustedSignersTypeDef(BaseModel):
    Enabled: bool
    Quantity: int
    Items: Optional[Sequence[str]] = None

class CookieNamesOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class CookieNamesTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class HeadersOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class HeadersTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class QueryStringNamesOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class QueryStringNamesTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class CloudFrontOriginAccessIdentityConfigTypeDef(BaseModel):
    CallerReference: str
    Comment: str

class CloudFrontOriginAccessIdentitySummaryTypeDef(BaseModel):
    Id: str
    S3CanonicalUserId: str
    Comment: str

class ConflictingAliasTypeDef(BaseModel):
    Alias: Optional[str] = None
    DistributionId: Optional[str] = None
    AccountId: Optional[str] = None

class ContentTypeProfileTypeDef(BaseModel):
    Format: Literal["URLEncoded"]
    ContentType: str
    ProfileId: Optional[str] = None

class StagingDistributionDnsNamesOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class StagingDistributionDnsNamesTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class ContinuousDeploymentSingleHeaderConfigTypeDef(BaseModel):
    Header: str
    Value: str

class SessionStickinessConfigTypeDef(BaseModel):
    IdleTTL: int
    MaximumTTL: int

class CopyDistributionRequestRequestTypeDef(BaseModel):
    PrimaryDistributionId: str
    CallerReference: str
    Staging: Optional[bool] = None
    IfMatch: Optional[str] = None
    Enabled: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class KeyGroupConfigTypeDef(BaseModel):
    Name: str
    Items: Sequence[str]
    Comment: Optional[str] = None

class ImportSourceTypeDef(BaseModel):
    SourceType: Literal["S3"]
    SourceARN: str

class KeyValueStoreTypeDef(BaseModel):
    Name: str
    Id: str
    Comment: str
    ARN: str
    LastModifiedTime: datetime
    Status: Optional[str] = None

class OriginAccessControlConfigTypeDef(BaseModel):
    Name: str
    SigningProtocol: Literal["sigv4"]
    SigningBehavior: OriginAccessControlSigningBehaviorsType
    OriginAccessControlOriginType: OriginAccessControlOriginTypesType
    Description: Optional[str] = None

class PublicKeyConfigTypeDef(BaseModel):
    CallerReference: str
    Name: str
    EncodedKey: str
    Comment: Optional[str] = None

class CustomErrorResponseTypeDef(BaseModel):
    ErrorCode: int
    ResponsePagePath: Optional[str] = None
    ResponseCode: Optional[str] = None
    ErrorCachingMinTTL: Optional[int] = None

class OriginCustomHeaderTypeDef(BaseModel):
    HeaderName: str
    HeaderValue: str

class OriginSslProtocolsOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[SslProtocolType]

class OriginSslProtocolsTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[SslProtocolType]

class DeleteCachePolicyRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteContinuousDeploymentPolicyRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteDistributionRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteFieldLevelEncryptionConfigRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteFieldLevelEncryptionProfileRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteFunctionRequestRequestTypeDef(BaseModel):
    Name: str
    IfMatch: str

class DeleteKeyGroupRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteKeyValueStoreRequestRequestTypeDef(BaseModel):
    Name: str
    IfMatch: str

class DeleteMonitoringSubscriptionRequestRequestTypeDef(BaseModel):
    DistributionId: str

class DeleteOriginAccessControlRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteOriginRequestPolicyRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeletePublicKeyRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteRealtimeLogConfigRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    ARN: Optional[str] = None

class DeleteResponseHeadersPolicyRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DeleteStreamingDistributionRequestRequestTypeDef(BaseModel):
    Id: str
    IfMatch: Optional[str] = None

class DescribeFunctionRequestRequestTypeDef(BaseModel):
    Name: str
    Stage: Optional[FunctionStageType] = None

class DescribeKeyValueStoreRequestRequestTypeDef(BaseModel):
    Name: str

class LoggingConfigTypeDef(BaseModel):
    Enabled: bool
    IncludeCookies: bool
    Bucket: str
    Prefix: str

class ViewerCertificateTypeDef(BaseModel):
    CloudFrontDefaultCertificate: Optional[bool] = None
    IAMCertificateId: Optional[str] = None
    ACMCertificateArn: Optional[str] = None
    SSLSupportMethod: Optional[SSLSupportMethodType] = None
    MinimumProtocolVersion: Optional[MinimumProtocolVersionType] = None
    Certificate: Optional[str] = None
    CertificateSource: Optional[CertificateSourceType] = None

class DistributionIdListTypeDef(BaseModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[str]] = None

class FieldPatternsOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class FieldPatternsTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class KinesisStreamConfigTypeDef(BaseModel):
    RoleARN: str
    StreamARN: str

class QueryStringCacheKeysOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class QueryStringCacheKeysTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class FunctionAssociationTypeDef(BaseModel):
    FunctionARN: str
    EventType: EventTypeType

class FunctionMetadataTypeDef(BaseModel):
    FunctionARN: str
    LastModifiedTime: datetime
    Stage: Optional[FunctionStageType] = None
    CreatedTime: Optional[datetime] = None

class GeoRestrictionOutputTypeDef(BaseModel):
    RestrictionType: GeoRestrictionTypeType
    Quantity: int
    Items: Optional[List[str]] = None

class GeoRestrictionTypeDef(BaseModel):
    RestrictionType: GeoRestrictionTypeType
    Quantity: int
    Items: Optional[Sequence[str]] = None

class GetCachePolicyConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetCachePolicyRequestRequestTypeDef(BaseModel):
    Id: str

class GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetCloudFrontOriginAccessIdentityRequestRequestTypeDef(BaseModel):
    Id: str

class GetContinuousDeploymentPolicyConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetContinuousDeploymentPolicyRequestRequestTypeDef(BaseModel):
    Id: str

class GetDistributionConfigRequestRequestTypeDef(BaseModel):
    Id: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetDistributionRequestRequestTypeDef(BaseModel):
    Id: str

class GetFieldLevelEncryptionConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetFieldLevelEncryptionProfileRequestRequestTypeDef(BaseModel):
    Id: str

class GetFieldLevelEncryptionRequestRequestTypeDef(BaseModel):
    Id: str

class GetFunctionRequestRequestTypeDef(BaseModel):
    Name: str
    Stage: Optional[FunctionStageType] = None

class GetInvalidationRequestRequestTypeDef(BaseModel):
    DistributionId: str
    Id: str

class GetKeyGroupConfigRequestRequestTypeDef(BaseModel):
    Id: str

class KeyGroupConfigOutputTypeDef(BaseModel):
    Name: str
    Items: List[str]
    Comment: Optional[str] = None

class GetKeyGroupRequestRequestTypeDef(BaseModel):
    Id: str

class GetMonitoringSubscriptionRequestRequestTypeDef(BaseModel):
    DistributionId: str

class GetOriginAccessControlConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetOriginAccessControlRequestRequestTypeDef(BaseModel):
    Id: str

class GetOriginRequestPolicyConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetOriginRequestPolicyRequestRequestTypeDef(BaseModel):
    Id: str

class GetPublicKeyConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetPublicKeyRequestRequestTypeDef(BaseModel):
    Id: str

class GetRealtimeLogConfigRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    ARN: Optional[str] = None

class GetResponseHeadersPolicyConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetResponseHeadersPolicyRequestRequestTypeDef(BaseModel):
    Id: str

class GetStreamingDistributionConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetStreamingDistributionRequestRequestTypeDef(BaseModel):
    Id: str

class PathsOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class PathsTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class InvalidationSummaryTypeDef(BaseModel):
    Id: str
    CreateTime: datetime
    Status: str

class KeyPairIdsTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class KeyValueStoreAssociationTypeDef(BaseModel):
    KeyValueStoreARN: str

class LambdaFunctionAssociationTypeDef(BaseModel):
    LambdaFunctionARN: str
    EventType: EventTypeType
    IncludeBody: Optional[bool] = None

class ListCachePoliciesRequestRequestTypeDef(BaseModel):
    Type: Optional[CachePolicyTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListConflictingAliasesRequestRequestTypeDef(BaseModel):
    DistributionId: str
    Alias: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListContinuousDeploymentPoliciesRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListDistributionsByCachePolicyIdRequestRequestTypeDef(BaseModel):
    CachePolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListDistributionsByKeyGroupRequestRequestTypeDef(BaseModel):
    KeyGroupId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef(BaseModel):
    OriginRequestPolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListDistributionsByRealtimeLogConfigRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    RealtimeLogConfigName: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None

class ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef(BaseModel):
    ResponseHeadersPolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListDistributionsByWebACLIdRequestRequestTypeDef(BaseModel):
    WebACLId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListDistributionsRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListFieldLevelEncryptionConfigsRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListFieldLevelEncryptionProfilesRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListFunctionsRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    Stage: Optional[FunctionStageType] = None

class ListInvalidationsRequestRequestTypeDef(BaseModel):
    DistributionId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListKeyGroupsRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListKeyValueStoresRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    Status: Optional[str] = None

class ListOriginAccessControlsRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListOriginRequestPoliciesRequestRequestTypeDef(BaseModel):
    Type: Optional[OriginRequestPolicyTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListPublicKeysRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListRealtimeLogConfigsRequestRequestTypeDef(BaseModel):
    MaxItems: Optional[str] = None
    Marker: Optional[str] = None

class ListResponseHeadersPoliciesRequestRequestTypeDef(BaseModel):
    Type: Optional[ResponseHeadersPolicyTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListStreamingDistributionsRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    Resource: str

class RealtimeMetricsSubscriptionConfigTypeDef(BaseModel):
    RealtimeMetricsSubscriptionStatus: RealtimeMetricsSubscriptionStatusType

class OriginAccessControlSummaryTypeDef(BaseModel):
    Id: str
    Description: str
    Name: str
    SigningProtocol: Literal["sigv4"]
    SigningBehavior: OriginAccessControlSigningBehaviorsType
    OriginAccessControlOriginType: OriginAccessControlOriginTypesType

class StatusCodesOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[int]

class StatusCodesTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[int]

class OriginGroupMemberTypeDef(BaseModel):
    OriginId: str

class OriginShieldTypeDef(BaseModel):
    Enabled: bool
    OriginShieldRegion: Optional[str] = None

class S3OriginConfigTypeDef(BaseModel):
    OriginAccessIdentity: str

class PublicKeySummaryTypeDef(BaseModel):
    Id: str
    Name: str
    CreatedTime: datetime
    EncodedKey: str
    Comment: Optional[str] = None

class PublishFunctionRequestRequestTypeDef(BaseModel):
    Name: str
    IfMatch: str

class QueryArgProfileTypeDef(BaseModel):
    QueryArg: str
    ProfileId: str

class ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[str]

class ResponseHeadersPolicyAccessControlAllowHeadersTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[str]

class ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[ResponseHeadersPolicyAccessControlAllowMethodsValuesType]

class ResponseHeadersPolicyAccessControlAllowMethodsTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[ResponseHeadersPolicyAccessControlAllowMethodsValuesType]

class ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[str]

class ResponseHeadersPolicyAccessControlAllowOriginsTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[str]

class ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[str]] = None

class ResponseHeadersPolicyAccessControlExposeHeadersTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None

class ResponseHeadersPolicyServerTimingHeadersConfigTypeDef(BaseModel):
    Enabled: bool
    SamplingRate: Optional[float] = None

class ResponseHeadersPolicyContentSecurityPolicyTypeDef(BaseModel):
    Override: bool
    ContentSecurityPolicy: str

class ResponseHeadersPolicyContentTypeOptionsTypeDef(BaseModel):
    Override: bool

class ResponseHeadersPolicyCustomHeaderTypeDef(BaseModel):
    Header: str
    Value: str
    Override: bool

class ResponseHeadersPolicyFrameOptionsTypeDef(BaseModel):
    Override: bool
    FrameOption: FrameOptionsListType

class ResponseHeadersPolicyReferrerPolicyTypeDef(BaseModel):
    Override: bool
    ReferrerPolicy: ReferrerPolicyListType

class ResponseHeadersPolicyRemoveHeaderTypeDef(BaseModel):
    Header: str

class ResponseHeadersPolicyStrictTransportSecurityTypeDef(BaseModel):
    Override: bool
    AccessControlMaxAgeSec: int
    IncludeSubdomains: Optional[bool] = None
    Preload: Optional[bool] = None

class ResponseHeadersPolicyXSSProtectionTypeDef(BaseModel):
    Override: bool
    Protection: bool
    ModeBlock: Optional[bool] = None
    ReportUri: Optional[str] = None

class S3OriginTypeDef(BaseModel):
    DomainName: str
    OriginAccessIdentity: str

class StreamingLoggingConfigTypeDef(BaseModel):
    Enabled: bool
    Bucket: str
    Prefix: str

class TagKeysTypeDef(BaseModel):
    Items: Optional[Sequence[str]] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class UpdateDistributionWithStagingConfigRequestRequestTypeDef(BaseModel):
    Id: str
    StagingDistributionId: Optional[str] = None
    IfMatch: Optional[str] = None

class UpdateKeyValueStoreRequestRequestTypeDef(BaseModel):
    Name: str
    Comment: str
    IfMatch: str

class AllowedMethodsOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[MethodType]
    CachedMethods: Optional[CachedMethodsOutputTypeDef] = None

class AllowedMethodsTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[MethodType]
    CachedMethods: Optional[CachedMethodsTypeDef] = None

class TestFunctionRequestRequestTypeDef(BaseModel):
    Name: str
    IfMatch: str
    EventObject: BlobTypeDef
    Stage: Optional[FunctionStageType] = None

class CachePolicyCookiesConfigOutputTypeDef(BaseModel):
    CookieBehavior: CachePolicyCookieBehaviorType
    Cookies: Optional[CookieNamesOutputTypeDef] = None

class CookiePreferenceOutputTypeDef(BaseModel):
    Forward: ItemSelectionType
    WhitelistedNames: Optional[CookieNamesOutputTypeDef] = None

class OriginRequestPolicyCookiesConfigOutputTypeDef(BaseModel):
    CookieBehavior: OriginRequestPolicyCookieBehaviorType
    Cookies: Optional[CookieNamesOutputTypeDef] = None

class CachePolicyCookiesConfigTypeDef(BaseModel):
    CookieBehavior: CachePolicyCookieBehaviorType
    Cookies: Optional[CookieNamesTypeDef] = None

class CookiePreferenceTypeDef(BaseModel):
    Forward: ItemSelectionType
    WhitelistedNames: Optional[CookieNamesTypeDef] = None

class OriginRequestPolicyCookiesConfigTypeDef(BaseModel):
    CookieBehavior: OriginRequestPolicyCookieBehaviorType
    Cookies: Optional[CookieNamesTypeDef] = None

class CachePolicyHeadersConfigOutputTypeDef(BaseModel):
    HeaderBehavior: CachePolicyHeaderBehaviorType
    Headers: Optional[HeadersOutputTypeDef] = None

class OriginRequestPolicyHeadersConfigOutputTypeDef(BaseModel):
    HeaderBehavior: OriginRequestPolicyHeaderBehaviorType
    Headers: Optional[HeadersOutputTypeDef] = None

class CachePolicyHeadersConfigTypeDef(BaseModel):
    HeaderBehavior: CachePolicyHeaderBehaviorType
    Headers: Optional[HeadersTypeDef] = None

class OriginRequestPolicyHeadersConfigTypeDef(BaseModel):
    HeaderBehavior: OriginRequestPolicyHeaderBehaviorType
    Headers: Optional[HeadersTypeDef] = None

class CachePolicyQueryStringsConfigOutputTypeDef(BaseModel):
    QueryStringBehavior: CachePolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesOutputTypeDef] = None

class OriginRequestPolicyQueryStringsConfigOutputTypeDef(BaseModel):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesOutputTypeDef] = None

class CachePolicyQueryStringsConfigTypeDef(BaseModel):
    QueryStringBehavior: CachePolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesTypeDef] = None

class OriginRequestPolicyQueryStringsConfigTypeDef(BaseModel):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesTypeDef] = None

class CloudFrontOriginAccessIdentityTypeDef(BaseModel):
    Id: str
    S3CanonicalUserId: str
    CloudFrontOriginAccessIdentityConfig: Optional[       CloudFrontOriginAccessIdentityConfigTypeDef     ] = None

class CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef(BaseModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef

class UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef(BaseModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class CloudFrontOriginAccessIdentityListTypeDef(BaseModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[CloudFrontOriginAccessIdentitySummaryTypeDef]] = None

class ConflictingAliasesListTypeDef(BaseModel):
    NextMarker: Optional[str] = None
    MaxItems: Optional[int] = None
    Quantity: Optional[int] = None
    Items: Optional[List[ConflictingAliasTypeDef]] = None

class ContentTypeProfilesOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[ContentTypeProfileTypeDef]] = None

class ContentTypeProfilesTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[ContentTypeProfileTypeDef]] = None

class ContinuousDeploymentSingleWeightConfigTypeDef(BaseModel):
    Weight: float
    SessionStickinessConfig: Optional[SessionStickinessConfigTypeDef] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCloudFrontOriginAccessIdentityConfigResultTypeDef(BaseModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionResultTypeDef(BaseModel):
    FunctionCode: StreamingBody
    ETag: str
    ContentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKeyGroupRequestRequestTypeDef(BaseModel):
    KeyGroupConfig: KeyGroupConfigTypeDef

class UpdateKeyGroupRequestRequestTypeDef(BaseModel):
    KeyGroupConfig: KeyGroupConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class CreateKeyValueStoreRequestRequestTypeDef(BaseModel):
    Name: str
    Comment: Optional[str] = None
    ImportSource: Optional[ImportSourceTypeDef] = None

class CreateKeyValueStoreResultTypeDef(BaseModel):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyValueStoreResultTypeDef(BaseModel):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class KeyValueStoreListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[KeyValueStoreTypeDef]] = None

class UpdateKeyValueStoreResultTypeDef(BaseModel):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOriginAccessControlRequestRequestTypeDef(BaseModel):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef

class GetOriginAccessControlConfigResultTypeDef(BaseModel):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginAccessControlTypeDef(BaseModel):
    Id: str
    OriginAccessControlConfig: Optional[OriginAccessControlConfigTypeDef] = None

class UpdateOriginAccessControlRequestRequestTypeDef(BaseModel):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class CreatePublicKeyRequestRequestTypeDef(BaseModel):
    PublicKeyConfig: PublicKeyConfigTypeDef

class GetPublicKeyConfigResultTypeDef(BaseModel):
    PublicKeyConfig: PublicKeyConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublicKeyTypeDef(BaseModel):
    Id: str
    CreatedTime: datetime
    PublicKeyConfig: PublicKeyConfigTypeDef

class UpdatePublicKeyRequestRequestTypeDef(BaseModel):
    PublicKeyConfig: PublicKeyConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class CustomErrorResponsesOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[CustomErrorResponseTypeDef]] = None

class CustomErrorResponsesTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[CustomErrorResponseTypeDef]] = None

class CustomHeadersOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[OriginCustomHeaderTypeDef]] = None

class CustomHeadersTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[OriginCustomHeaderTypeDef]] = None

class CustomOriginConfigOutputTypeDef(BaseModel):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsOutputTypeDef] = None
    OriginReadTimeout: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None

class CustomOriginConfigTypeDef(BaseModel):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsTypeDef] = None
    OriginReadTimeout: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None

class ListDistributionsByCachePolicyIdResultTypeDef(BaseModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByKeyGroupResultTypeDef(BaseModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByOriginRequestPolicyIdResultTypeDef(BaseModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByResponseHeadersPolicyIdResultTypeDef(BaseModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptionEntityOutputTypeDef(BaseModel):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: FieldPatternsOutputTypeDef

class EncryptionEntityTypeDef(BaseModel):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: FieldPatternsTypeDef

class EndPointTypeDef(BaseModel):
    StreamType: str
    KinesisStreamConfig: Optional[KinesisStreamConfigTypeDef] = None

class FunctionAssociationsOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[FunctionAssociationTypeDef]] = None

class FunctionAssociationsTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[FunctionAssociationTypeDef]] = None

class RestrictionsOutputTypeDef(BaseModel):
    GeoRestriction: GeoRestrictionOutputTypeDef

class RestrictionsTypeDef(BaseModel):
    GeoRestriction: GeoRestrictionTypeDef

class GetDistributionRequestDistributionDeployedWaitTypeDef(BaseModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetInvalidationRequestInvalidationCompletedWaitTypeDef(BaseModel):
    DistributionId: str
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef(BaseModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetKeyGroupConfigResultTypeDef(BaseModel):
    KeyGroupConfig: KeyGroupConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class KeyGroupTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    KeyGroupConfig: KeyGroupConfigOutputTypeDef

class InvalidationBatchOutputTypeDef(BaseModel):
    Paths: PathsOutputTypeDef
    CallerReference: str

class InvalidationBatchTypeDef(BaseModel):
    Paths: PathsTypeDef
    CallerReference: str

class InvalidationListTypeDef(BaseModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[InvalidationSummaryTypeDef]] = None

class KGKeyPairIdsTypeDef(BaseModel):
    KeyGroupId: Optional[str] = None
    KeyPairIds: Optional[KeyPairIdsTypeDef] = None

class SignerTypeDef(BaseModel):
    AwsAccountNumber: Optional[str] = None
    KeyPairIds: Optional[KeyPairIdsTypeDef] = None

class KeyValueStoreAssociationsOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[KeyValueStoreAssociationTypeDef]] = None

class KeyValueStoreAssociationsTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[KeyValueStoreAssociationTypeDef]] = None

class LambdaFunctionAssociationsOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[LambdaFunctionAssociationTypeDef]] = None

class LambdaFunctionAssociationsTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[LambdaFunctionAssociationTypeDef]] = None

class ListCloudFrontOriginAccessIdentitiesRequestListCloudFrontOriginAccessIdentitiesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDistributionsRequestListDistributionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInvalidationsRequestListInvalidationsPaginateTypeDef(BaseModel):
    DistributionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeyValueStoresRequestListKeyValueStoresPaginateTypeDef(BaseModel):
    Status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamingDistributionsRequestListStreamingDistributionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MonitoringSubscriptionTypeDef(BaseModel):
    RealtimeMetricsSubscriptionConfig: Optional[RealtimeMetricsSubscriptionConfigTypeDef] = None

class OriginAccessControlListTypeDef(BaseModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[OriginAccessControlSummaryTypeDef]] = None

class OriginGroupFailoverCriteriaOutputTypeDef(BaseModel):
    StatusCodes: StatusCodesOutputTypeDef

class OriginGroupFailoverCriteriaTypeDef(BaseModel):
    StatusCodes: StatusCodesTypeDef

class OriginGroupMembersOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[OriginGroupMemberTypeDef]

class OriginGroupMembersTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[OriginGroupMemberTypeDef]

class PublicKeyListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[PublicKeySummaryTypeDef]] = None

class QueryArgProfilesOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[QueryArgProfileTypeDef]] = None

class QueryArgProfilesTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[QueryArgProfileTypeDef]] = None

class ResponseHeadersPolicyCorsConfigOutputTypeDef(BaseModel):
    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef
    AccessControlAllowCredentials: bool
    OriginOverride: bool
    AccessControlExposeHeaders: Optional[       ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef     ] = None
    AccessControlMaxAgeSec: Optional[int] = None

class ResponseHeadersPolicyCorsConfigTypeDef(BaseModel):
    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOriginsTypeDef
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeadersTypeDef
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethodsTypeDef
    AccessControlAllowCredentials: bool
    OriginOverride: bool
    AccessControlExposeHeaders: Optional[       ResponseHeadersPolicyAccessControlExposeHeadersTypeDef     ] = None
    AccessControlMaxAgeSec: Optional[int] = None

class ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[ResponseHeadersPolicyCustomHeaderTypeDef]] = None

class ResponseHeadersPolicyCustomHeadersConfigTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[ResponseHeadersPolicyCustomHeaderTypeDef]] = None

class ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[ResponseHeadersPolicyRemoveHeaderTypeDef]] = None

class ResponseHeadersPolicyRemoveHeadersConfigTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[ResponseHeadersPolicyRemoveHeaderTypeDef]] = None

class ResponseHeadersPolicySecurityHeadersConfigTypeDef(BaseModel):
    XSSProtection: Optional[ResponseHeadersPolicyXSSProtectionTypeDef] = None
    FrameOptions: Optional[ResponseHeadersPolicyFrameOptionsTypeDef] = None
    ReferrerPolicy: Optional[ResponseHeadersPolicyReferrerPolicyTypeDef] = None
    ContentSecurityPolicy: Optional[ResponseHeadersPolicyContentSecurityPolicyTypeDef] = None
    ContentTypeOptions: Optional[ResponseHeadersPolicyContentTypeOptionsTypeDef] = None
    StrictTransportSecurity: Optional[ResponseHeadersPolicyStrictTransportSecurityTypeDef] = None

class StreamingDistributionSummaryTypeDef(BaseModel):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    DomainName: str
    S3Origin: S3OriginTypeDef
    Aliases: AliasesOutputTypeDef
    TrustedSigners: TrustedSignersOutputTypeDef
    Comment: str
    PriceClass: PriceClassType
    Enabled: bool

class StreamingDistributionConfigOutputTypeDef(BaseModel):
    CallerReference: str
    S3Origin: S3OriginTypeDef
    Comment: str
    TrustedSigners: TrustedSignersOutputTypeDef
    Enabled: bool
    Aliases: Optional[AliasesOutputTypeDef] = None
    Logging: Optional[StreamingLoggingConfigTypeDef] = None
    PriceClass: Optional[PriceClassType] = None

class StreamingDistributionConfigTypeDef(BaseModel):
    CallerReference: str
    S3Origin: S3OriginTypeDef
    Comment: str
    TrustedSigners: TrustedSignersTypeDef
    Enabled: bool
    Aliases: Optional[AliasesTypeDef] = None
    Logging: Optional[StreamingLoggingConfigTypeDef] = None
    PriceClass: Optional[PriceClassType] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    Resource: str
    TagKeys: TagKeysTypeDef

class TagsOutputTypeDef(BaseModel):
    Items: Optional[List[TagTypeDef]] = None

class TagsTypeDef(BaseModel):
    Items: Optional[Sequence[TagTypeDef]] = None

class ForwardedValuesOutputTypeDef(BaseModel):
    QueryString: bool
    Cookies: CookiePreferenceOutputTypeDef
    Headers: Optional[HeadersOutputTypeDef] = None
    QueryStringCacheKeys: Optional[QueryStringCacheKeysOutputTypeDef] = None

class ForwardedValuesTypeDef(BaseModel):
    QueryString: bool
    Cookies: CookiePreferenceTypeDef
    Headers: Optional[HeadersTypeDef] = None
    QueryStringCacheKeys: Optional[QueryStringCacheKeysTypeDef] = None

class ParametersInCacheKeyAndForwardedToOriginOutputTypeDef(BaseModel):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: CachePolicyHeadersConfigOutputTypeDef
    CookiesConfig: CachePolicyCookiesConfigOutputTypeDef
    QueryStringsConfig: CachePolicyQueryStringsConfigOutputTypeDef
    EnableAcceptEncodingBrotli: Optional[bool] = None

class OriginRequestPolicyConfigOutputTypeDef(BaseModel):
    Name: str
    HeadersConfig: OriginRequestPolicyHeadersConfigOutputTypeDef
    CookiesConfig: OriginRequestPolicyCookiesConfigOutputTypeDef
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfigOutputTypeDef
    Comment: Optional[str] = None

class ParametersInCacheKeyAndForwardedToOriginTypeDef(BaseModel):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: CachePolicyHeadersConfigTypeDef
    CookiesConfig: CachePolicyCookiesConfigTypeDef
    QueryStringsConfig: CachePolicyQueryStringsConfigTypeDef
    EnableAcceptEncodingBrotli: Optional[bool] = None

class OriginRequestPolicyConfigTypeDef(BaseModel):
    Name: str
    HeadersConfig: OriginRequestPolicyHeadersConfigTypeDef
    CookiesConfig: OriginRequestPolicyCookiesConfigTypeDef
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfigTypeDef
    Comment: Optional[str] = None

class CreateCloudFrontOriginAccessIdentityResultTypeDef(BaseModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCloudFrontOriginAccessIdentityResultTypeDef(BaseModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCloudFrontOriginAccessIdentityResultTypeDef(BaseModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCloudFrontOriginAccessIdentitiesResultTypeDef(BaseModel):
    CloudFrontOriginAccessIdentityList: CloudFrontOriginAccessIdentityListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConflictingAliasesResultTypeDef(BaseModel):
    ConflictingAliasesList: ConflictingAliasesListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ContentTypeProfileConfigOutputTypeDef(BaseModel):
    ForwardWhenContentTypeIsUnknown: bool
    ContentTypeProfiles: Optional[ContentTypeProfilesOutputTypeDef] = None

class ContentTypeProfileConfigTypeDef(BaseModel):
    ForwardWhenContentTypeIsUnknown: bool
    ContentTypeProfiles: Optional[ContentTypeProfilesTypeDef] = None

class TrafficConfigTypeDef(BaseModel):
    Type: ContinuousDeploymentPolicyTypeType
    SingleWeightConfig: Optional[ContinuousDeploymentSingleWeightConfigTypeDef] = None
    SingleHeaderConfig: Optional[ContinuousDeploymentSingleHeaderConfigTypeDef] = None

class ListKeyValueStoresResultTypeDef(BaseModel):
    KeyValueStoreList: KeyValueStoreListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOriginAccessControlResultTypeDef(BaseModel):
    OriginAccessControl: OriginAccessControlTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginAccessControlResultTypeDef(BaseModel):
    OriginAccessControl: OriginAccessControlTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOriginAccessControlResultTypeDef(BaseModel):
    OriginAccessControl: OriginAccessControlTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePublicKeyResultTypeDef(BaseModel):
    PublicKey: PublicKeyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyResultTypeDef(BaseModel):
    PublicKey: PublicKeyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePublicKeyResultTypeDef(BaseModel):
    PublicKey: PublicKeyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginOutputTypeDef(BaseModel):
    Id: str
    DomainName: str
    OriginPath: Optional[str] = None
    CustomHeaders: Optional[CustomHeadersOutputTypeDef] = None
    S3OriginConfig: Optional[S3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[CustomOriginConfigOutputTypeDef] = None
    ConnectionAttempts: Optional[int] = None
    ConnectionTimeout: Optional[int] = None
    OriginShield: Optional[OriginShieldTypeDef] = None
    OriginAccessControlId: Optional[str] = None

class OriginTypeDef(BaseModel):
    Id: str
    DomainName: str
    OriginPath: Optional[str] = None
    CustomHeaders: Optional[CustomHeadersTypeDef] = None
    S3OriginConfig: Optional[S3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[CustomOriginConfigTypeDef] = None
    ConnectionAttempts: Optional[int] = None
    ConnectionTimeout: Optional[int] = None
    OriginShield: Optional[OriginShieldTypeDef] = None
    OriginAccessControlId: Optional[str] = None

class EncryptionEntitiesOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[EncryptionEntityOutputTypeDef]] = None

class EncryptionEntitiesTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[EncryptionEntityTypeDef]] = None

class CreateRealtimeLogConfigRequestRequestTypeDef(BaseModel):
    EndPoints: Sequence[EndPointTypeDef]
    Fields: Sequence[str]
    Name: str
    SamplingRate: int

class RealtimeLogConfigTypeDef(BaseModel):
    ARN: str
    Name: str
    SamplingRate: int
    EndPoints: List[EndPointTypeDef]
    Fields: List[str]

class UpdateRealtimeLogConfigRequestRequestTypeDef(BaseModel):
    EndPoints: Optional[Sequence[EndPointTypeDef]] = None
    Fields: Optional[Sequence[str]] = None
    Name: Optional[str] = None
    ARN: Optional[str] = None
    SamplingRate: Optional[int] = None

class CreateKeyGroupResultTypeDef(BaseModel):
    KeyGroup: KeyGroupTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyGroupResultTypeDef(BaseModel):
    KeyGroup: KeyGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class KeyGroupSummaryTypeDef(BaseModel):
    KeyGroup: KeyGroupTypeDef

class UpdateKeyGroupResultTypeDef(BaseModel):
    KeyGroup: KeyGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvalidationTypeDef(BaseModel):
    Id: str
    Status: str
    CreateTime: datetime
    InvalidationBatch: InvalidationBatchOutputTypeDef

class CreateInvalidationRequestRequestTypeDef(BaseModel):
    DistributionId: str
    InvalidationBatch: InvalidationBatchTypeDef

class ListInvalidationsResultTypeDef(BaseModel):
    InvalidationList: InvalidationListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActiveTrustedKeyGroupsTypeDef(BaseModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[KGKeyPairIdsTypeDef]] = None

class ActiveTrustedSignersTypeDef(BaseModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[SignerTypeDef]] = None

class FunctionConfigOutputTypeDef(BaseModel):
    Comment: str
    Runtime: FunctionRuntimeType
    KeyValueStoreAssociations: Optional[KeyValueStoreAssociationsOutputTypeDef] = None

class FunctionConfigTypeDef(BaseModel):
    Comment: str
    Runtime: FunctionRuntimeType
    KeyValueStoreAssociations: Optional[KeyValueStoreAssociationsTypeDef] = None

class CreateMonitoringSubscriptionRequestRequestTypeDef(BaseModel):
    DistributionId: str
    MonitoringSubscription: MonitoringSubscriptionTypeDef

class CreateMonitoringSubscriptionResultTypeDef(BaseModel):
    MonitoringSubscription: MonitoringSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMonitoringSubscriptionResultTypeDef(BaseModel):
    MonitoringSubscription: MonitoringSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOriginAccessControlsResultTypeDef(BaseModel):
    OriginAccessControlList: OriginAccessControlListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OriginGroupOutputTypeDef(BaseModel):
    Id: str
    FailoverCriteria: OriginGroupFailoverCriteriaOutputTypeDef
    Members: OriginGroupMembersOutputTypeDef

class OriginGroupTypeDef(BaseModel):
    Id: str
    FailoverCriteria: OriginGroupFailoverCriteriaTypeDef
    Members: OriginGroupMembersTypeDef

class ListPublicKeysResultTypeDef(BaseModel):
    PublicKeyList: PublicKeyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryArgProfileConfigOutputTypeDef(BaseModel):
    ForwardWhenQueryArgProfileIsUnknown: bool
    QueryArgProfiles: Optional[QueryArgProfilesOutputTypeDef] = None

class QueryArgProfileConfigTypeDef(BaseModel):
    ForwardWhenQueryArgProfileIsUnknown: bool
    QueryArgProfiles: Optional[QueryArgProfilesTypeDef] = None

class ResponseHeadersPolicyConfigOutputTypeDef(BaseModel):
    Name: str
    Comment: Optional[str] = None
    CorsConfig: Optional[ResponseHeadersPolicyCorsConfigOutputTypeDef] = None
    SecurityHeadersConfig: Optional[ResponseHeadersPolicySecurityHeadersConfigTypeDef] = None
    ServerTimingHeadersConfig: Optional[       ResponseHeadersPolicyServerTimingHeadersConfigTypeDef     ] = None
    CustomHeadersConfig: Optional[ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef] = None
    RemoveHeadersConfig: Optional[ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef] = None

class ResponseHeadersPolicyConfigTypeDef(BaseModel):
    Name: str
    Comment: Optional[str] = None
    CorsConfig: Optional[ResponseHeadersPolicyCorsConfigTypeDef] = None
    SecurityHeadersConfig: Optional[ResponseHeadersPolicySecurityHeadersConfigTypeDef] = None
    ServerTimingHeadersConfig: Optional[       ResponseHeadersPolicyServerTimingHeadersConfigTypeDef     ] = None
    CustomHeadersConfig: Optional[ResponseHeadersPolicyCustomHeadersConfigTypeDef] = None
    RemoveHeadersConfig: Optional[ResponseHeadersPolicyRemoveHeadersConfigTypeDef] = None

class StreamingDistributionListTypeDef(BaseModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[StreamingDistributionSummaryTypeDef]] = None

class GetStreamingDistributionConfigResultTypeDef(BaseModel):
    StreamingDistributionConfig: StreamingDistributionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingDistributionRequestRequestTypeDef(BaseModel):
    StreamingDistributionConfig: StreamingDistributionConfigTypeDef

class UpdateStreamingDistributionRequestRequestTypeDef(BaseModel):
    StreamingDistributionConfig: StreamingDistributionConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class ListTagsForResourceResultTypeDef(BaseModel):
    Tags: TagsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StreamingDistributionConfigWithTagsTypeDef(BaseModel):
    StreamingDistributionConfig: StreamingDistributionConfigTypeDef
    Tags: TagsTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    Resource: str
    Tags: TagsTypeDef

class CacheBehaviorOutputTypeDef(BaseModel):
    PathPattern: str
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersOutputTypeDef] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsOutputTypeDef] = None
    AllowedMethods: Optional[AllowedMethodsOutputTypeDef] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsOutputTypeDef] = None
    FunctionAssociations: Optional[FunctionAssociationsOutputTypeDef] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    ForwardedValues: Optional[ForwardedValuesOutputTypeDef] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None

class DefaultCacheBehaviorOutputTypeDef(BaseModel):
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersOutputTypeDef] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsOutputTypeDef] = None
    AllowedMethods: Optional[AllowedMethodsOutputTypeDef] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsOutputTypeDef] = None
    FunctionAssociations: Optional[FunctionAssociationsOutputTypeDef] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    ForwardedValues: Optional[ForwardedValuesOutputTypeDef] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None

class CacheBehaviorTypeDef(BaseModel):
    PathPattern: str
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersTypeDef] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsTypeDef] = None
    AllowedMethods: Optional[AllowedMethodsTypeDef] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsTypeDef] = None
    FunctionAssociations: Optional[FunctionAssociationsTypeDef] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    ForwardedValues: Optional[ForwardedValuesTypeDef] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None

class DefaultCacheBehaviorTypeDef(BaseModel):
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersTypeDef] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsTypeDef] = None
    AllowedMethods: Optional[AllowedMethodsTypeDef] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsTypeDef] = None
    FunctionAssociations: Optional[FunctionAssociationsTypeDef] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    ForwardedValues: Optional[ForwardedValuesTypeDef] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None

class CachePolicyConfigOutputTypeDef(BaseModel):
    Name: str
    MinTTL: int
    Comment: Optional[str] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None
    ParametersInCacheKeyAndForwardedToOrigin: Optional[       ParametersInCacheKeyAndForwardedToOriginOutputTypeDef     ] = None

class GetOriginRequestPolicyConfigResultTypeDef(BaseModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginRequestPolicyTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    OriginRequestPolicyConfig: OriginRequestPolicyConfigOutputTypeDef

class CachePolicyConfigTypeDef(BaseModel):
    Name: str
    MinTTL: int
    Comment: Optional[str] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None
    ParametersInCacheKeyAndForwardedToOrigin: Optional[       ParametersInCacheKeyAndForwardedToOriginTypeDef     ] = None

class CreateOriginRequestPolicyRequestRequestTypeDef(BaseModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigTypeDef

class UpdateOriginRequestPolicyRequestRequestTypeDef(BaseModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class ContinuousDeploymentPolicyConfigOutputTypeDef(BaseModel):
    StagingDistributionDnsNames: StagingDistributionDnsNamesOutputTypeDef
    Enabled: bool
    TrafficConfig: Optional[TrafficConfigTypeDef] = None

class ContinuousDeploymentPolicyConfigTypeDef(BaseModel):
    StagingDistributionDnsNames: StagingDistributionDnsNamesTypeDef
    Enabled: bool
    TrafficConfig: Optional[TrafficConfigTypeDef] = None

class OriginsOutputTypeDef(BaseModel):
    Quantity: int
    Items: List[OriginOutputTypeDef]

class OriginsTypeDef(BaseModel):
    Quantity: int
    Items: Sequence[OriginTypeDef]

class FieldLevelEncryptionProfileConfigOutputTypeDef(BaseModel):
    Name: str
    CallerReference: str
    EncryptionEntities: EncryptionEntitiesOutputTypeDef
    Comment: Optional[str] = None

class FieldLevelEncryptionProfileSummaryTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    Name: str
    EncryptionEntities: EncryptionEntitiesOutputTypeDef
    Comment: Optional[str] = None

class FieldLevelEncryptionProfileConfigTypeDef(BaseModel):
    Name: str
    CallerReference: str
    EncryptionEntities: EncryptionEntitiesTypeDef
    Comment: Optional[str] = None

class CreateRealtimeLogConfigResultTypeDef(BaseModel):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRealtimeLogConfigResultTypeDef(BaseModel):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RealtimeLogConfigsTypeDef(BaseModel):
    MaxItems: int
    IsTruncated: bool
    Marker: str
    Items: Optional[List[RealtimeLogConfigTypeDef]] = None
    NextMarker: Optional[str] = None

class UpdateRealtimeLogConfigResultTypeDef(BaseModel):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KeyGroupListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[KeyGroupSummaryTypeDef]] = None

class CreateInvalidationResultTypeDef(BaseModel):
    Location: str
    Invalidation: InvalidationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvalidationResultTypeDef(BaseModel):
    Invalidation: InvalidationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StreamingDistributionTypeDef(BaseModel):
    Id: str
    ARN: str
    Status: str
    DomainName: str
    ActiveTrustedSigners: ActiveTrustedSignersTypeDef
    StreamingDistributionConfig: StreamingDistributionConfigOutputTypeDef
    LastModifiedTime: Optional[datetime] = None

class FunctionSummaryTypeDef(BaseModel):
    Name: str
    FunctionConfig: FunctionConfigOutputTypeDef
    FunctionMetadata: FunctionMetadataTypeDef
    Status: Optional[str] = None

class CreateFunctionRequestRequestTypeDef(BaseModel):
    Name: str
    FunctionConfig: FunctionConfigTypeDef
    FunctionCode: BlobTypeDef

class UpdateFunctionRequestRequestTypeDef(BaseModel):
    Name: str
    IfMatch: str
    FunctionConfig: FunctionConfigTypeDef
    FunctionCode: BlobTypeDef

class OriginGroupsOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[OriginGroupOutputTypeDef]] = None

class OriginGroupsTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[OriginGroupTypeDef]] = None

class FieldLevelEncryptionConfigOutputTypeDef(BaseModel):
    CallerReference: str
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfigOutputTypeDef] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfigOutputTypeDef] = None

class FieldLevelEncryptionSummaryTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfigOutputTypeDef] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfigOutputTypeDef] = None

class FieldLevelEncryptionConfigTypeDef(BaseModel):
    CallerReference: str
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfigTypeDef] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfigTypeDef] = None

class GetResponseHeadersPolicyConfigResultTypeDef(BaseModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseHeadersPolicyTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigOutputTypeDef

class CreateResponseHeadersPolicyRequestRequestTypeDef(BaseModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigTypeDef

class UpdateResponseHeadersPolicyRequestRequestTypeDef(BaseModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class ListStreamingDistributionsResultTypeDef(BaseModel):
    StreamingDistributionList: StreamingDistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingDistributionWithTagsRequestRequestTypeDef(BaseModel):
    StreamingDistributionConfigWithTags: StreamingDistributionConfigWithTagsTypeDef

class CacheBehaviorsOutputTypeDef(BaseModel):
    Quantity: int
    Items: Optional[List[CacheBehaviorOutputTypeDef]] = None

class CacheBehaviorsTypeDef(BaseModel):
    Quantity: int
    Items: Optional[Sequence[CacheBehaviorTypeDef]] = None

class CachePolicyTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    CachePolicyConfig: CachePolicyConfigOutputTypeDef

class GetCachePolicyConfigResultTypeDef(BaseModel):
    CachePolicyConfig: CachePolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOriginRequestPolicyResultTypeDef(BaseModel):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginRequestPolicyResultTypeDef(BaseModel):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginRequestPolicySummaryTypeDef(BaseModel):
    Type: OriginRequestPolicyTypeType
    OriginRequestPolicy: OriginRequestPolicyTypeDef

class UpdateOriginRequestPolicyResultTypeDef(BaseModel):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCachePolicyRequestRequestTypeDef(BaseModel):
    CachePolicyConfig: CachePolicyConfigTypeDef

class UpdateCachePolicyRequestRequestTypeDef(BaseModel):
    CachePolicyConfig: CachePolicyConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class ContinuousDeploymentPolicyTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigOutputTypeDef

class GetContinuousDeploymentPolicyConfigResultTypeDef(BaseModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContinuousDeploymentPolicyRequestRequestTypeDef(BaseModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigTypeDef

class UpdateContinuousDeploymentPolicyRequestRequestTypeDef(BaseModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class FieldLevelEncryptionProfileTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigOutputTypeDef

class GetFieldLevelEncryptionProfileConfigResultTypeDef(BaseModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldLevelEncryptionProfileListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FieldLevelEncryptionProfileSummaryTypeDef]] = None

class CreateFieldLevelEncryptionProfileRequestRequestTypeDef(BaseModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigTypeDef

class UpdateFieldLevelEncryptionProfileRequestRequestTypeDef(BaseModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class ListRealtimeLogConfigsResultTypeDef(BaseModel):
    RealtimeLogConfigs: RealtimeLogConfigsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyGroupsResultTypeDef(BaseModel):
    KeyGroupList: KeyGroupListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingDistributionResultTypeDef(BaseModel):
    StreamingDistribution: StreamingDistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingDistributionWithTagsResultTypeDef(BaseModel):
    StreamingDistribution: StreamingDistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamingDistributionResultTypeDef(BaseModel):
    StreamingDistribution: StreamingDistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStreamingDistributionResultTypeDef(BaseModel):
    StreamingDistribution: StreamingDistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionResultTypeDef(BaseModel):
    FunctionSummary: FunctionSummaryTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFunctionResultTypeDef(BaseModel):
    FunctionSummary: FunctionSummaryTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FunctionSummaryTypeDef]] = None

class PublishFunctionResultTypeDef(BaseModel):
    FunctionSummary: FunctionSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestResultTypeDef(BaseModel):
    FunctionSummary: Optional[FunctionSummaryTypeDef] = None
    ComputeUtilization: Optional[str] = None
    FunctionExecutionLogs: Optional[List[str]] = None
    FunctionErrorMessage: Optional[str] = None
    FunctionOutput: Optional[str] = None

class UpdateFunctionResultTypeDef(BaseModel):
    FunctionSummary: FunctionSummaryTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldLevelEncryptionTypeDef(BaseModel):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigOutputTypeDef

class GetFieldLevelEncryptionConfigResultTypeDef(BaseModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldLevelEncryptionListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FieldLevelEncryptionSummaryTypeDef]] = None

class CreateFieldLevelEncryptionConfigRequestRequestTypeDef(BaseModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigTypeDef

class UpdateFieldLevelEncryptionConfigRequestRequestTypeDef(BaseModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class CreateResponseHeadersPolicyResultTypeDef(BaseModel):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResponseHeadersPolicyResultTypeDef(BaseModel):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseHeadersPolicySummaryTypeDef(BaseModel):
    Type: ResponseHeadersPolicyTypeType
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef

class UpdateResponseHeadersPolicyResultTypeDef(BaseModel):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DistributionConfigOutputTypeDef(BaseModel):
    CallerReference: str
    Origins: OriginsOutputTypeDef
    DefaultCacheBehavior: DefaultCacheBehaviorOutputTypeDef
    Comment: str
    Enabled: bool
    Aliases: Optional[AliasesOutputTypeDef] = None
    DefaultRootObject: Optional[str] = None
    OriginGroups: Optional[OriginGroupsOutputTypeDef] = None
    CacheBehaviors: Optional[CacheBehaviorsOutputTypeDef] = None
    CustomErrorResponses: Optional[CustomErrorResponsesOutputTypeDef] = None
    Logging: Optional[LoggingConfigTypeDef] = None
    PriceClass: Optional[PriceClassType] = None
    ViewerCertificate: Optional[ViewerCertificateTypeDef] = None
    Restrictions: Optional[RestrictionsOutputTypeDef] = None
    WebACLId: Optional[str] = None
    HttpVersion: Optional[HttpVersionType] = None
    IsIPV6Enabled: Optional[bool] = None
    ContinuousDeploymentPolicyId: Optional[str] = None
    Staging: Optional[bool] = None

class DistributionSummaryTypeDef(BaseModel):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    DomainName: str
    Aliases: AliasesOutputTypeDef
    Origins: OriginsOutputTypeDef
    DefaultCacheBehavior: DefaultCacheBehaviorOutputTypeDef
    CacheBehaviors: CacheBehaviorsOutputTypeDef
    CustomErrorResponses: CustomErrorResponsesOutputTypeDef
    Comment: str
    PriceClass: PriceClassType
    Enabled: bool
    ViewerCertificate: ViewerCertificateTypeDef
    Restrictions: RestrictionsOutputTypeDef
    WebACLId: str
    HttpVersion: HttpVersionType
    IsIPV6Enabled: bool
    Staging: bool
    OriginGroups: Optional[OriginGroupsOutputTypeDef] = None
    AliasICPRecordals: Optional[List[AliasICPRecordalTypeDef]] = None

class DistributionConfigTypeDef(BaseModel):
    CallerReference: str
    Origins: OriginsTypeDef
    DefaultCacheBehavior: DefaultCacheBehaviorTypeDef
    Comment: str
    Enabled: bool
    Aliases: Optional[AliasesTypeDef] = None
    DefaultRootObject: Optional[str] = None
    OriginGroups: Optional[OriginGroupsTypeDef] = None
    CacheBehaviors: Optional[CacheBehaviorsTypeDef] = None
    CustomErrorResponses: Optional[CustomErrorResponsesTypeDef] = None
    Logging: Optional[LoggingConfigTypeDef] = None
    PriceClass: Optional[PriceClassType] = None
    ViewerCertificate: Optional[ViewerCertificateTypeDef] = None
    Restrictions: Optional[RestrictionsTypeDef] = None
    WebACLId: Optional[str] = None
    HttpVersion: Optional[HttpVersionType] = None
    IsIPV6Enabled: Optional[bool] = None
    ContinuousDeploymentPolicyId: Optional[str] = None
    Staging: Optional[bool] = None

class CachePolicySummaryTypeDef(BaseModel):
    Type: CachePolicyTypeType
    CachePolicy: CachePolicyTypeDef

class CreateCachePolicyResultTypeDef(BaseModel):
    CachePolicy: CachePolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCachePolicyResultTypeDef(BaseModel):
    CachePolicy: CachePolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCachePolicyResultTypeDef(BaseModel):
    CachePolicy: CachePolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginRequestPolicyListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[OriginRequestPolicySummaryTypeDef]] = None

class ContinuousDeploymentPolicySummaryTypeDef(BaseModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef

class CreateContinuousDeploymentPolicyResultTypeDef(BaseModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContinuousDeploymentPolicyResultTypeDef(BaseModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContinuousDeploymentPolicyResultTypeDef(BaseModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFieldLevelEncryptionProfileResultTypeDef(BaseModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFieldLevelEncryptionProfileResultTypeDef(BaseModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFieldLevelEncryptionProfileResultTypeDef(BaseModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFieldLevelEncryptionProfilesResultTypeDef(BaseModel):
    FieldLevelEncryptionProfileList: FieldLevelEncryptionProfileListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsResultTypeDef(BaseModel):
    FunctionList: FunctionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestFunctionResultTypeDef(BaseModel):
    TestResult: TestResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFieldLevelEncryptionConfigResultTypeDef(BaseModel):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFieldLevelEncryptionResultTypeDef(BaseModel):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFieldLevelEncryptionConfigResultTypeDef(BaseModel):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFieldLevelEncryptionConfigsResultTypeDef(BaseModel):
    FieldLevelEncryptionList: FieldLevelEncryptionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseHeadersPolicyListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[ResponseHeadersPolicySummaryTypeDef]] = None

class DistributionTypeDef(BaseModel):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    InProgressInvalidationBatches: int
    DomainName: str
    DistributionConfig: DistributionConfigOutputTypeDef
    ActiveTrustedSigners: Optional[ActiveTrustedSignersTypeDef] = None
    ActiveTrustedKeyGroups: Optional[ActiveTrustedKeyGroupsTypeDef] = None
    AliasICPRecordals: Optional[List[AliasICPRecordalTypeDef]] = None

class GetDistributionConfigResultTypeDef(BaseModel):
    DistributionConfig: DistributionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DistributionListTypeDef(BaseModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[DistributionSummaryTypeDef]] = None

class CreateDistributionRequestRequestTypeDef(BaseModel):
    DistributionConfig: DistributionConfigTypeDef

class DistributionConfigWithTagsTypeDef(BaseModel):
    DistributionConfig: DistributionConfigTypeDef
    Tags: TagsTypeDef

class UpdateDistributionRequestRequestTypeDef(BaseModel):
    DistributionConfig: DistributionConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None

class CachePolicyListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[CachePolicySummaryTypeDef]] = None

class ListOriginRequestPoliciesResultTypeDef(BaseModel):
    OriginRequestPolicyList: OriginRequestPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ContinuousDeploymentPolicyListTypeDef(BaseModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[ContinuousDeploymentPolicySummaryTypeDef]] = None

class ListResponseHeadersPoliciesResultTypeDef(BaseModel):
    ResponseHeadersPolicyList: ResponseHeadersPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyDistributionResultTypeDef(BaseModel):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDistributionResultTypeDef(BaseModel):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDistributionWithTagsResultTypeDef(BaseModel):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionResultTypeDef(BaseModel):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionResultTypeDef(BaseModel):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionWithStagingConfigResultTypeDef(BaseModel):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByRealtimeLogConfigResultTypeDef(BaseModel):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsByWebACLIdResultTypeDef(BaseModel):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributionsResultTypeDef(BaseModel):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDistributionWithTagsRequestRequestTypeDef(BaseModel):
    DistributionConfigWithTags: DistributionConfigWithTagsTypeDef

class ListCachePoliciesResultTypeDef(BaseModel):
    CachePolicyList: CachePolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContinuousDeploymentPoliciesResultTypeDef(BaseModel):
    ContinuousDeploymentPolicyList: ContinuousDeploymentPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.cloudfront_constants import *

class AliasICPRecordalTypeDef(BaseValidatorModel):
    CNAME: Optional[str] = None
    ICPRecordalStatus: Optional[ICPRecordalStatusType] = None


class AliasesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class AliasesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class CachedMethodsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[MethodType]


class AnycastIpListSummaryTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Status: str
    Arn: str
    IpCount: int
    LastModifiedTime: datetime


class AnycastIpListTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Status: str
    Arn: str
    AnycastIps: List[str]
    IpCount: int
    LastModifiedTime: datetime


class AssociateAliasRequestTypeDef(BaseValidatorModel):
    TargetDistributionId: str
    Alias: str


class GrpcConfigTypeDef(BaseValidatorModel):
    Enabled: bool


class TrustedKeyGroupsOutputTypeDef(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[str]] = None


class TrustedSignersOutputTypeDef(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[str]] = None


class CookieNamesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class CookieNamesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class HeadersOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class HeadersTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class QueryStringNamesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class QueryStringNamesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class CachedMethodsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[MethodType]


class CloudFrontOriginAccessIdentityConfigTypeDef(BaseValidatorModel):
    CallerReference: str
    Comment: str


class CloudFrontOriginAccessIdentitySummaryTypeDef(BaseValidatorModel):
    Id: str
    S3CanonicalUserId: str
    Comment: str


class ConflictingAliasTypeDef(BaseValidatorModel):
    Alias: Optional[str] = None
    DistributionId: Optional[str] = None
    AccountId: Optional[str] = None


class ContentTypeProfileTypeDef(BaseValidatorModel):
    Format: Literal["URLEncoded"]
    ContentType: str
    ProfileId: Optional[str] = None


class StagingDistributionDnsNamesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class StagingDistributionDnsNamesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class ContinuousDeploymentSingleHeaderConfigTypeDef(BaseValidatorModel):
    Header: str
    Value: str


class SessionStickinessConfigTypeDef(BaseValidatorModel):
    IdleTTL: int
    MaximumTTL: int


class CopyDistributionRequestTypeDef(BaseValidatorModel):
    PrimaryDistributionId: str
    CallerReference: str
    Staging: Optional[bool] = None
    IfMatch: Optional[str] = None
    Enabled: Optional[bool] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ImportSourceTypeDef(BaseValidatorModel):
    SourceType: Literal["S3"]
    SourceARN: str


class KeyValueStoreTypeDef(BaseValidatorModel):
    Name: str
    Id: str
    Comment: str
    ARN: str
    LastModifiedTime: datetime
    Status: Optional[str] = None


class OriginAccessControlConfigTypeDef(BaseValidatorModel):
    Name: str
    SigningProtocol: Literal["sigv4"]
    SigningBehavior: OriginAccessControlSigningBehaviorsType
    OriginAccessControlOriginType: OriginAccessControlOriginTypesType
    Description: Optional[str] = None


class PublicKeyConfigTypeDef(BaseValidatorModel):
    CallerReference: str
    Name: str
    EncodedKey: str
    Comment: Optional[str] = None


class CustomErrorResponseTypeDef(BaseValidatorModel):
    ErrorCode: int
    ResponsePagePath: Optional[str] = None
    ResponseCode: Optional[str] = None
    ErrorCachingMinTTL: Optional[int] = None


class OriginCustomHeaderTypeDef(BaseValidatorModel):
    HeaderName: str
    HeaderValue: str


class OriginSslProtocolsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[SslProtocolType]


class DeleteAnycastIpListRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: str


class DeleteCachePolicyRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteCloudFrontOriginAccessIdentityRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteContinuousDeploymentPolicyRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteDistributionRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteFieldLevelEncryptionConfigRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteFieldLevelEncryptionProfileRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteFunctionRequestTypeDef(BaseValidatorModel):
    Name: str
    IfMatch: str


class DeleteKeyGroupRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteKeyValueStoreRequestTypeDef(BaseValidatorModel):
    Name: str
    IfMatch: str


class DeleteMonitoringSubscriptionRequestTypeDef(BaseValidatorModel):
    DistributionId: str


class DeleteOriginAccessControlRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteOriginRequestPolicyRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeletePublicKeyRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteRealtimeLogConfigRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ARN: Optional[str] = None


class DeleteResponseHeadersPolicyRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteStreamingDistributionRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


class DeleteVpcOriginRequestTypeDef(BaseValidatorModel):
    Id: str
    IfMatch: str


class DescribeFunctionRequestTypeDef(BaseValidatorModel):
    Name: str
    Stage: Optional[FunctionStageType] = None


class DescribeKeyValueStoreRequestTypeDef(BaseValidatorModel):
    Name: str


class LoggingConfigTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    IncludeCookies: Optional[bool] = None
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None


class ViewerCertificateTypeDef(BaseValidatorModel):
    CloudFrontDefaultCertificate: Optional[bool] = None
    IAMCertificateId: Optional[str] = None
    ACMCertificateArn: Optional[str] = None
    SSLSupportMethod: Optional[SSLSupportMethodType] = None
    MinimumProtocolVersion: Optional[MinimumProtocolVersionType] = None
    Certificate: Optional[str] = None
    CertificateSource: Optional[CertificateSourceType] = None


class DistributionIdListTypeDef(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[str]] = None


class FieldPatternsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class FieldPatternsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class KinesisStreamConfigTypeDef(BaseValidatorModel):
    RoleARN: str
    StreamARN: str


class QueryStringCacheKeysOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class FunctionAssociationTypeDef(BaseValidatorModel):
    FunctionARN: str
    EventType: EventTypeType


class FunctionMetadataTypeDef(BaseValidatorModel):
    FunctionARN: str
    LastModifiedTime: datetime
    Stage: Optional[FunctionStageType] = None
    CreatedTime: Optional[datetime] = None


class GeoRestrictionOutputTypeDef(BaseValidatorModel):
    RestrictionType: GeoRestrictionTypeType
    Quantity: int
    Items: Optional[List[str]] = None


class GeoRestrictionTypeDef(BaseValidatorModel):
    RestrictionType: GeoRestrictionTypeType
    Quantity: int
    Items: Optional[Sequence[str]] = None


class GetAnycastIpListRequestTypeDef(BaseValidatorModel):
    Id: str


class GetCachePolicyConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetCachePolicyRequestTypeDef(BaseValidatorModel):
    Id: str


class GetCloudFrontOriginAccessIdentityConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetCloudFrontOriginAccessIdentityRequestTypeDef(BaseValidatorModel):
    Id: str


class GetContinuousDeploymentPolicyConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetContinuousDeploymentPolicyRequestTypeDef(BaseValidatorModel):
    Id: str


class GetDistributionConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetDistributionRequestTypeDef(BaseValidatorModel):
    Id: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetFieldLevelEncryptionConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetFieldLevelEncryptionProfileConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetFieldLevelEncryptionProfileRequestTypeDef(BaseValidatorModel):
    Id: str


class GetFieldLevelEncryptionRequestTypeDef(BaseValidatorModel):
    Id: str


class GetFunctionRequestTypeDef(BaseValidatorModel):
    Name: str
    Stage: Optional[FunctionStageType] = None


class GetInvalidationRequestTypeDef(BaseValidatorModel):
    DistributionId: str
    Id: str


class GetKeyGroupConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class KeyGroupConfigOutputTypeDef(BaseValidatorModel):
    Name: str
    Items: List[str]
    Comment: Optional[str] = None


class GetKeyGroupRequestTypeDef(BaseValidatorModel):
    Id: str


class GetMonitoringSubscriptionRequestTypeDef(BaseValidatorModel):
    DistributionId: str


class GetOriginAccessControlConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetOriginAccessControlRequestTypeDef(BaseValidatorModel):
    Id: str


class GetOriginRequestPolicyConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetOriginRequestPolicyRequestTypeDef(BaseValidatorModel):
    Id: str


class GetPublicKeyConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetPublicKeyRequestTypeDef(BaseValidatorModel):
    Id: str


class GetRealtimeLogConfigRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ARN: Optional[str] = None


class GetResponseHeadersPolicyConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetResponseHeadersPolicyRequestTypeDef(BaseValidatorModel):
    Id: str


class GetStreamingDistributionConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetStreamingDistributionRequestTypeDef(BaseValidatorModel):
    Id: str


class GetVpcOriginRequestTypeDef(BaseValidatorModel):
    Id: str


class PathsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class PathsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class InvalidationSummaryTypeDef(BaseValidatorModel):
    Id: str
    CreateTime: datetime
    Status: str


class KeyPairIdsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class KeyGroupConfigTypeDef(BaseValidatorModel):
    Name: str
    Items: Sequence[str]
    Comment: Optional[str] = None


class KeyValueStoreAssociationTypeDef(BaseValidatorModel):
    KeyValueStoreARN: str


class LambdaFunctionAssociationTypeDef(BaseValidatorModel):
    LambdaFunctionARN: str
    EventType: EventTypeType
    IncludeBody: Optional[bool] = None


class ListAnycastIpListsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCloudFrontOriginAccessIdentitiesRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListConflictingAliasesRequestTypeDef(BaseValidatorModel):
    DistributionId: str
    Alias: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListContinuousDeploymentPoliciesRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListDistributionsByAnycastIpListIdRequestTypeDef(BaseValidatorModel):
    AnycastIpListId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListDistributionsByCachePolicyIdRequestTypeDef(BaseValidatorModel):
    CachePolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListDistributionsByKeyGroupRequestTypeDef(BaseValidatorModel):
    KeyGroupId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListDistributionsByOriginRequestPolicyIdRequestTypeDef(BaseValidatorModel):
    OriginRequestPolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListDistributionsByRealtimeLogConfigRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    RealtimeLogConfigName: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None


class ListDistributionsByResponseHeadersPolicyIdRequestTypeDef(BaseValidatorModel):
    ResponseHeadersPolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListDistributionsByVpcOriginIdRequestTypeDef(BaseValidatorModel):
    VpcOriginId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListDistributionsByWebACLIdRequestTypeDef(BaseValidatorModel):
    WebACLId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListDistributionsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListFieldLevelEncryptionConfigsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListFieldLevelEncryptionProfilesRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListFunctionsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    Stage: Optional[FunctionStageType] = None


class ListInvalidationsRequestTypeDef(BaseValidatorModel):
    DistributionId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListKeyGroupsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListKeyValueStoresRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    Status: Optional[str] = None


class ListOriginAccessControlsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListPublicKeysRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListRealtimeLogConfigsRequestTypeDef(BaseValidatorModel):
    MaxItems: Optional[str] = None
    Marker: Optional[str] = None


class ListStreamingDistributionsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    Resource: str


class ListVpcOriginsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class RealtimeMetricsSubscriptionConfigTypeDef(BaseValidatorModel):
    RealtimeMetricsSubscriptionStatus: RealtimeMetricsSubscriptionStatusType


class OriginAccessControlSummaryTypeDef(BaseValidatorModel):
    Id: str
    Description: str
    Name: str
    SigningProtocol: Literal["sigv4"]
    SigningBehavior: OriginAccessControlSigningBehaviorsType
    OriginAccessControlOriginType: OriginAccessControlOriginTypesType


class StatusCodesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[int]


class OriginGroupMemberTypeDef(BaseValidatorModel):
    OriginId: str


class OriginShieldTypeDef(BaseValidatorModel):
    Enabled: bool
    OriginShieldRegion: Optional[str] = None


class S3OriginConfigTypeDef(BaseValidatorModel):
    OriginAccessIdentity: str


class VpcOriginConfigTypeDef(BaseValidatorModel):
    VpcOriginId: str
    OriginReadTimeout: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None


class OriginSslProtocolsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[SslProtocolType]


class PublicKeySummaryTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    CreatedTime: datetime
    EncodedKey: str
    Comment: Optional[str] = None


class PublishFunctionRequestTypeDef(BaseValidatorModel):
    Name: str
    IfMatch: str


class QueryArgProfileTypeDef(BaseValidatorModel):
    QueryArg: str
    ProfileId: str


class QueryStringCacheKeysTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[str]


class ResponseHeadersPolicyAccessControlAllowHeadersTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[str]


class ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[ResponseHeadersPolicyAccessControlAllowMethodsValuesType]


class ResponseHeadersPolicyAccessControlAllowMethodsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[ResponseHeadersPolicyAccessControlAllowMethodsValuesType]


class ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[str]


class ResponseHeadersPolicyAccessControlAllowOriginsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[str]


class ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class ResponseHeadersPolicyAccessControlExposeHeadersTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[str]] = None


class ResponseHeadersPolicyServerTimingHeadersConfigTypeDef(BaseValidatorModel):
    Enabled: bool
    SamplingRate: Optional[float] = None


class ResponseHeadersPolicyContentSecurityPolicyTypeDef(BaseValidatorModel):
    Override: bool
    ContentSecurityPolicy: str


class ResponseHeadersPolicyContentTypeOptionsTypeDef(BaseValidatorModel):
    Override: bool


class ResponseHeadersPolicyCustomHeaderTypeDef(BaseValidatorModel):
    Header: str
    Value: str
    Override: bool


class ResponseHeadersPolicyFrameOptionsTypeDef(BaseValidatorModel):
    Override: bool
    FrameOption: FrameOptionsListType


class ResponseHeadersPolicyReferrerPolicyTypeDef(BaseValidatorModel):
    Override: bool
    ReferrerPolicy: ReferrerPolicyListType


class ResponseHeadersPolicyRemoveHeaderTypeDef(BaseValidatorModel):
    Header: str


class ResponseHeadersPolicyStrictTransportSecurityTypeDef(BaseValidatorModel):
    Override: bool
    AccessControlMaxAgeSec: int
    IncludeSubdomains: Optional[bool] = None
    Preload: Optional[bool] = None


class ResponseHeadersPolicyXSSProtectionTypeDef(BaseValidatorModel):
    Override: bool
    Protection: bool
    ModeBlock: Optional[bool] = None
    ReportUri: Optional[str] = None


class S3OriginTypeDef(BaseValidatorModel):
    DomainName: str
    OriginAccessIdentity: str


class StatusCodesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[int]


class StreamingLoggingConfigTypeDef(BaseValidatorModel):
    Enabled: bool
    Bucket: str
    Prefix: str


class TagKeysTypeDef(BaseValidatorModel):
    Items: Optional[Sequence[str]] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class TrustedKeyGroupsTypeDef(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[Sequence[str]] = None


class TrustedSignersTypeDef(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[Sequence[str]] = None


class UpdateDistributionWithStagingConfigRequestTypeDef(BaseValidatorModel):
    Id: str
    StagingDistributionId: Optional[str] = None
    IfMatch: Optional[str] = None


class UpdateKeyValueStoreRequestTypeDef(BaseValidatorModel):
    Name: str
    Comment: str
    IfMatch: str


class VpcOriginSummaryTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Status: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    Arn: str
    OriginEndpointArn: str


class AllowedMethodsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[MethodType]
    CachedMethods: Optional[CachedMethodsOutputTypeDef] = None


class AnycastIpListCollectionTypeDef(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    Items: Optional[List[AnycastIpListSummaryTypeDef]] = None
    NextMarker: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class TestFunctionRequestTypeDef(BaseValidatorModel):
    Name: str
    IfMatch: str
    EventObject: BlobTypeDef
    Stage: Optional[FunctionStageType] = None


class CachePolicyCookiesConfigOutputTypeDef(BaseValidatorModel):
    CookieBehavior: CachePolicyCookieBehaviorType
    Cookies: Optional[CookieNamesOutputTypeDef] = None


class CookiePreferenceOutputTypeDef(BaseValidatorModel):
    Forward: ItemSelectionType
    WhitelistedNames: Optional[CookieNamesOutputTypeDef] = None


class OriginRequestPolicyCookiesConfigOutputTypeDef(BaseValidatorModel):
    CookieBehavior: OriginRequestPolicyCookieBehaviorType
    Cookies: Optional[CookieNamesOutputTypeDef] = None


class CachePolicyCookiesConfigTypeDef(BaseValidatorModel):
    CookieBehavior: CachePolicyCookieBehaviorType
    Cookies: Optional[CookieNamesTypeDef] = None


class OriginRequestPolicyCookiesConfigTypeDef(BaseValidatorModel):
    CookieBehavior: OriginRequestPolicyCookieBehaviorType
    Cookies: Optional[CookieNamesTypeDef] = None


class CachePolicyHeadersConfigOutputTypeDef(BaseValidatorModel):
    HeaderBehavior: CachePolicyHeaderBehaviorType
    Headers: Optional[HeadersOutputTypeDef] = None


class OriginRequestPolicyHeadersConfigOutputTypeDef(BaseValidatorModel):
    HeaderBehavior: OriginRequestPolicyHeaderBehaviorType
    Headers: Optional[HeadersOutputTypeDef] = None


class CachePolicyHeadersConfigTypeDef(BaseValidatorModel):
    HeaderBehavior: CachePolicyHeaderBehaviorType
    Headers: Optional[HeadersTypeDef] = None


class OriginRequestPolicyHeadersConfigTypeDef(BaseValidatorModel):
    HeaderBehavior: OriginRequestPolicyHeaderBehaviorType
    Headers: Optional[HeadersTypeDef] = None


class CachePolicyQueryStringsConfigOutputTypeDef(BaseValidatorModel):
    QueryStringBehavior: CachePolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesOutputTypeDef] = None


class OriginRequestPolicyQueryStringsConfigOutputTypeDef(BaseValidatorModel):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesOutputTypeDef] = None


class CachePolicyQueryStringsConfigTypeDef(BaseValidatorModel):
    QueryStringBehavior: CachePolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesTypeDef] = None


class OriginRequestPolicyQueryStringsConfigTypeDef(BaseValidatorModel):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesTypeDef] = None


class CloudFrontOriginAccessIdentityTypeDef(BaseValidatorModel):
    Id: str
    S3CanonicalUserId: str
    CloudFrontOriginAccessIdentityConfig: Optional[CloudFrontOriginAccessIdentityConfigTypeDef] = None


class CreateCloudFrontOriginAccessIdentityRequestTypeDef(BaseValidatorModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef


class UpdateCloudFrontOriginAccessIdentityRequestTypeDef(BaseValidatorModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None


class CloudFrontOriginAccessIdentityListTypeDef(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[CloudFrontOriginAccessIdentitySummaryTypeDef]] = None


class ConflictingAliasesListTypeDef(BaseValidatorModel):
    NextMarker: Optional[str] = None
    MaxItems: Optional[int] = None
    Quantity: Optional[int] = None
    Items: Optional[List[ConflictingAliasTypeDef]] = None


class ContentTypeProfilesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ContentTypeProfileTypeDef]] = None


class ContentTypeProfilesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[ContentTypeProfileTypeDef]] = None


class ContinuousDeploymentSingleWeightConfigTypeDef(BaseValidatorModel):
    Weight: float
    SessionStickinessConfig: Optional[SessionStickinessConfigTypeDef] = None


class CreateAnycastIpListResultTypeDef(BaseValidatorModel):
    AnycastIpList: AnycastIpListTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAnycastIpListResultTypeDef(BaseValidatorModel):
    AnycastIpList: AnycastIpListTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCloudFrontOriginAccessIdentityConfigResultTypeDef(BaseValidatorModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetFunctionResultTypeDef(BaseValidatorModel):
    FunctionCode: StreamingBody
    ETag: str
    ContentType: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateKeyValueStoreRequestTypeDef(BaseValidatorModel):
    Name: str
    Comment: Optional[str] = None
    ImportSource: Optional[ImportSourceTypeDef] = None


class CreateKeyValueStoreResultTypeDef(BaseValidatorModel):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeKeyValueStoreResultTypeDef(BaseValidatorModel):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class KeyValueStoreListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[KeyValueStoreTypeDef]] = None


class UpdateKeyValueStoreResultTypeDef(BaseValidatorModel):
    KeyValueStore: KeyValueStoreTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOriginAccessControlRequestTypeDef(BaseValidatorModel):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef


class GetOriginAccessControlConfigResultTypeDef(BaseValidatorModel):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class OriginAccessControlTypeDef(BaseValidatorModel):
    Id: str
    OriginAccessControlConfig: Optional[OriginAccessControlConfigTypeDef] = None


class UpdateOriginAccessControlRequestTypeDef(BaseValidatorModel):
    OriginAccessControlConfig: OriginAccessControlConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None


class CreatePublicKeyRequestTypeDef(BaseValidatorModel):
    PublicKeyConfig: PublicKeyConfigTypeDef


class GetPublicKeyConfigResultTypeDef(BaseValidatorModel):
    PublicKeyConfig: PublicKeyConfigTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class PublicKeyTypeDef(BaseValidatorModel):
    Id: str
    CreatedTime: datetime
    PublicKeyConfig: PublicKeyConfigTypeDef


class UpdatePublicKeyRequestTypeDef(BaseValidatorModel):
    PublicKeyConfig: PublicKeyConfigTypeDef
    Id: str
    IfMatch: Optional[str] = None


class CustomErrorResponsesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[CustomErrorResponseTypeDef]] = None


class CustomErrorResponsesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[CustomErrorResponseTypeDef]] = None


class CustomHeadersOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[OriginCustomHeaderTypeDef]] = None


class CustomHeadersTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[OriginCustomHeaderTypeDef]] = None


class CustomOriginConfigOutputTypeDef(BaseValidatorModel):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsOutputTypeDef] = None
    OriginReadTimeout: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None


class VpcOriginEndpointConfigOutputTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsOutputTypeDef] = None


class ListDistributionsByCachePolicyIdResultTypeDef(BaseValidatorModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributionsByKeyGroupResultTypeDef(BaseValidatorModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributionsByOriginRequestPolicyIdResultTypeDef(BaseValidatorModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributionsByResponseHeadersPolicyIdResultTypeDef(BaseValidatorModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributionsByVpcOriginIdResultTypeDef(BaseValidatorModel):
    DistributionIdList: DistributionIdListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EncryptionEntityOutputTypeDef(BaseValidatorModel):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: FieldPatternsOutputTypeDef


class EncryptionEntityTypeDef(BaseValidatorModel):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: FieldPatternsTypeDef


class EndPointTypeDef(BaseValidatorModel):
    StreamType: str
    KinesisStreamConfig: Optional[KinesisStreamConfigTypeDef] = None


class FunctionAssociationsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[FunctionAssociationTypeDef]] = None


class FunctionAssociationsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[FunctionAssociationTypeDef]] = None


class RestrictionsOutputTypeDef(BaseValidatorModel):
    GeoRestriction: GeoRestrictionOutputTypeDef


class GetDistributionRequestWaitTypeDef(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetInvalidationRequestWaitTypeDef(BaseValidatorModel):
    DistributionId: str
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetStreamingDistributionRequestWaitTypeDef(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetKeyGroupConfigResultTypeDef(BaseValidatorModel):
    KeyGroupConfig: KeyGroupConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class KeyGroupTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    KeyGroupConfig: KeyGroupConfigOutputTypeDef


class InvalidationBatchOutputTypeDef(BaseValidatorModel):
    Paths: PathsOutputTypeDef
    CallerReference: str


class InvalidationBatchTypeDef(BaseValidatorModel):
    Paths: PathsTypeDef
    CallerReference: str


class InvalidationListTypeDef(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[InvalidationSummaryTypeDef]] = None


class KGKeyPairIdsTypeDef(BaseValidatorModel):
    KeyGroupId: Optional[str] = None
    KeyPairIds: Optional[KeyPairIdsTypeDef] = None


class SignerTypeDef(BaseValidatorModel):
    AwsAccountNumber: Optional[str] = None
    KeyPairIds: Optional[KeyPairIdsTypeDef] = None


class KeyValueStoreAssociationsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[KeyValueStoreAssociationTypeDef]] = None


class KeyValueStoreAssociationsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[KeyValueStoreAssociationTypeDef]] = None


class LambdaFunctionAssociationsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[LambdaFunctionAssociationTypeDef]] = None


class LambdaFunctionAssociationsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[LambdaFunctionAssociationTypeDef]] = None


class ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDistributionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInvalidationsRequestPaginateTypeDef(BaseValidatorModel):
    DistributionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListKeyValueStoresRequestPaginateTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPublicKeysRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamingDistributionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MonitoringSubscriptionTypeDef(BaseValidatorModel):
    RealtimeMetricsSubscriptionConfig: Optional[RealtimeMetricsSubscriptionConfigTypeDef] = None


class OriginAccessControlListTypeDef(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[OriginAccessControlSummaryTypeDef]] = None


class OriginGroupFailoverCriteriaOutputTypeDef(BaseValidatorModel):
    StatusCodes: StatusCodesOutputTypeDef


class OriginGroupMembersOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[OriginGroupMemberTypeDef]


class OriginGroupMembersTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[OriginGroupMemberTypeDef]


class VpcOriginEndpointConfigTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsTypeDef] = None


class PublicKeyListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[PublicKeySummaryTypeDef]] = None


class QueryArgProfilesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[QueryArgProfileTypeDef]] = None


class QueryArgProfilesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[QueryArgProfileTypeDef]] = None


class ResponseHeadersPolicyCorsConfigOutputTypeDef(BaseValidatorModel):
    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef
    AccessControlAllowCredentials: bool
    OriginOverride: bool
    AccessControlExposeHeaders: Optional[ ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef ] = None
    AccessControlMaxAgeSec: Optional[int] = None


class ResponseHeadersPolicyCorsConfigTypeDef(BaseValidatorModel):
    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOriginsTypeDef
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeadersTypeDef
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethodsTypeDef
    AccessControlAllowCredentials: bool
    OriginOverride: bool
    AccessControlExposeHeaders: Optional[ResponseHeadersPolicyAccessControlExposeHeadersTypeDef] = None
    AccessControlMaxAgeSec: Optional[int] = None


class ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ResponseHeadersPolicyCustomHeaderTypeDef]] = None


class ResponseHeadersPolicyCustomHeadersConfigTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[ResponseHeadersPolicyCustomHeaderTypeDef]] = None


class ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ResponseHeadersPolicyRemoveHeaderTypeDef]] = None


class ResponseHeadersPolicyRemoveHeadersConfigTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[ResponseHeadersPolicyRemoveHeaderTypeDef]] = None


class ResponseHeadersPolicySecurityHeadersConfigTypeDef(BaseValidatorModel):
    XSSProtection: Optional[ResponseHeadersPolicyXSSProtectionTypeDef] = None
    FrameOptions: Optional[ResponseHeadersPolicyFrameOptionsTypeDef] = None
    ReferrerPolicy: Optional[ResponseHeadersPolicyReferrerPolicyTypeDef] = None
    ContentSecurityPolicy: Optional[ResponseHeadersPolicyContentSecurityPolicyTypeDef] = None
    ContentTypeOptions: Optional[ResponseHeadersPolicyContentTypeOptionsTypeDef] = None
    StrictTransportSecurity: Optional[ResponseHeadersPolicyStrictTransportSecurityTypeDef] = None


class StreamingDistributionSummaryTypeDef(BaseValidatorModel):
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


class StreamingDistributionConfigOutputTypeDef(BaseValidatorModel):
    CallerReference: str
    S3Origin: S3OriginTypeDef
    Comment: str
    TrustedSigners: TrustedSignersOutputTypeDef
    Enabled: bool
    Aliases: Optional[AliasesOutputTypeDef] = None
    Logging: Optional[StreamingLoggingConfigTypeDef] = None
    PriceClass: Optional[PriceClassType] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    Resource: str
    TagKeys: TagKeysTypeDef


class TagsOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[TagTypeDef]] = None


class TagsTypeDef(BaseValidatorModel):
    Items: Optional[Sequence[TagTypeDef]] = None


class VpcOriginListTypeDef(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[VpcOriginSummaryTypeDef]] = None


class ListAnycastIpListsResultTypeDef(BaseValidatorModel):
    AnycastIpLists: AnycastIpListCollectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ForwardedValuesOutputTypeDef(BaseValidatorModel):
    QueryString: bool
    Cookies: CookiePreferenceOutputTypeDef
    Headers: Optional[HeadersOutputTypeDef] = None
    QueryStringCacheKeys: Optional[QueryStringCacheKeysOutputTypeDef] = None


class CookieNamesUnionTypeDef(BaseValidatorModel):
    pass


class CookiePreferenceTypeDef(BaseValidatorModel):
    Forward: ItemSelectionType
    WhitelistedNames: Optional[CookieNamesUnionTypeDef] = None


class ParametersInCacheKeyAndForwardedToOriginOutputTypeDef(BaseValidatorModel):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: CachePolicyHeadersConfigOutputTypeDef
    CookiesConfig: CachePolicyCookiesConfigOutputTypeDef
    QueryStringsConfig: CachePolicyQueryStringsConfigOutputTypeDef
    EnableAcceptEncodingBrotli: Optional[bool] = None


class OriginRequestPolicyConfigOutputTypeDef(BaseValidatorModel):
    Name: str
    HeadersConfig: OriginRequestPolicyHeadersConfigOutputTypeDef
    CookiesConfig: OriginRequestPolicyCookiesConfigOutputTypeDef
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfigOutputTypeDef
    Comment: Optional[str] = None


class ParametersInCacheKeyAndForwardedToOriginTypeDef(BaseValidatorModel):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: CachePolicyHeadersConfigTypeDef
    CookiesConfig: CachePolicyCookiesConfigTypeDef
    QueryStringsConfig: CachePolicyQueryStringsConfigTypeDef
    EnableAcceptEncodingBrotli: Optional[bool] = None


class OriginRequestPolicyConfigTypeDef(BaseValidatorModel):
    Name: str
    HeadersConfig: OriginRequestPolicyHeadersConfigTypeDef
    CookiesConfig: OriginRequestPolicyCookiesConfigTypeDef
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfigTypeDef
    Comment: Optional[str] = None


class CachedMethodsUnionTypeDef(BaseValidatorModel):
    pass


class AllowedMethodsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[MethodType]
    CachedMethods: Optional[CachedMethodsUnionTypeDef] = None


class CreateCloudFrontOriginAccessIdentityResultTypeDef(BaseValidatorModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCloudFrontOriginAccessIdentityResultTypeDef(BaseValidatorModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCloudFrontOriginAccessIdentityResultTypeDef(BaseValidatorModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentityTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListCloudFrontOriginAccessIdentitiesResultTypeDef(BaseValidatorModel):
    CloudFrontOriginAccessIdentityList: CloudFrontOriginAccessIdentityListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListConflictingAliasesResultTypeDef(BaseValidatorModel):
    ConflictingAliasesList: ConflictingAliasesListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ContentTypeProfileConfigOutputTypeDef(BaseValidatorModel):
    ForwardWhenContentTypeIsUnknown: bool
    ContentTypeProfiles: Optional[ContentTypeProfilesOutputTypeDef] = None


class ContentTypeProfileConfigTypeDef(BaseValidatorModel):
    ForwardWhenContentTypeIsUnknown: bool
    ContentTypeProfiles: Optional[ContentTypeProfilesTypeDef] = None


class ListKeyValueStoresResultTypeDef(BaseValidatorModel):
    KeyValueStoreList: KeyValueStoreListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOriginAccessControlResultTypeDef(BaseValidatorModel):
    OriginAccessControl: OriginAccessControlTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetOriginAccessControlResultTypeDef(BaseValidatorModel):
    OriginAccessControl: OriginAccessControlTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateOriginAccessControlResultTypeDef(BaseValidatorModel):
    OriginAccessControl: OriginAccessControlTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePublicKeyResultTypeDef(BaseValidatorModel):
    PublicKey: PublicKeyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPublicKeyResultTypeDef(BaseValidatorModel):
    PublicKey: PublicKeyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePublicKeyResultTypeDef(BaseValidatorModel):
    PublicKey: PublicKeyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class OriginOutputTypeDef(BaseValidatorModel):
    Id: str
    DomainName: str
    OriginPath: Optional[str] = None
    CustomHeaders: Optional[CustomHeadersOutputTypeDef] = None
    S3OriginConfig: Optional[S3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[CustomOriginConfigOutputTypeDef] = None
    VpcOriginConfig: Optional[VpcOriginConfigTypeDef] = None
    ConnectionAttempts: Optional[int] = None
    ConnectionTimeout: Optional[int] = None
    OriginShield: Optional[OriginShieldTypeDef] = None
    OriginAccessControlId: Optional[str] = None


class VpcOriginTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    Status: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    VpcOriginEndpointConfig: VpcOriginEndpointConfigOutputTypeDef


class EncryptionEntitiesOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[EncryptionEntityOutputTypeDef]] = None


class EncryptionEntitiesTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[EncryptionEntityTypeDef]] = None


class CreateRealtimeLogConfigRequestTypeDef(BaseValidatorModel):
    EndPoints: Sequence[EndPointTypeDef]
    Fields: Sequence[str]
    Name: str
    SamplingRate: int


class RealtimeLogConfigTypeDef(BaseValidatorModel):
    ARN: str
    Name: str
    SamplingRate: int
    EndPoints: List[EndPointTypeDef]
    Fields: List[str]


class UpdateRealtimeLogConfigRequestTypeDef(BaseValidatorModel):
    EndPoints: Optional[Sequence[EndPointTypeDef]] = None
    Fields: Optional[Sequence[str]] = None
    Name: Optional[str] = None
    ARN: Optional[str] = None
    SamplingRate: Optional[int] = None


class GeoRestrictionUnionTypeDef(BaseValidatorModel):
    pass


class RestrictionsTypeDef(BaseValidatorModel):
    GeoRestriction: GeoRestrictionUnionTypeDef


class CreateKeyGroupResultTypeDef(BaseValidatorModel):
    KeyGroup: KeyGroupTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetKeyGroupResultTypeDef(BaseValidatorModel):
    KeyGroup: KeyGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class KeyGroupSummaryTypeDef(BaseValidatorModel):
    KeyGroup: KeyGroupTypeDef


class UpdateKeyGroupResultTypeDef(BaseValidatorModel):
    KeyGroup: KeyGroupTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class InvalidationTypeDef(BaseValidatorModel):
    Id: str
    Status: str
    CreateTime: datetime
    InvalidationBatch: InvalidationBatchOutputTypeDef


class ListInvalidationsResultTypeDef(BaseValidatorModel):
    InvalidationList: InvalidationListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ActiveTrustedKeyGroupsTypeDef(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[KGKeyPairIdsTypeDef]] = None


class ActiveTrustedSignersTypeDef(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[SignerTypeDef]] = None


class KeyGroupConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateKeyGroupRequestTypeDef(BaseValidatorModel):
    KeyGroupConfig: KeyGroupConfigUnionTypeDef


class UpdateKeyGroupRequestTypeDef(BaseValidatorModel):
    KeyGroupConfig: KeyGroupConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class FunctionConfigOutputTypeDef(BaseValidatorModel):
    Comment: str
    Runtime: FunctionRuntimeType
    KeyValueStoreAssociations: Optional[KeyValueStoreAssociationsOutputTypeDef] = None


class FunctionConfigTypeDef(BaseValidatorModel):
    Comment: str
    Runtime: FunctionRuntimeType
    KeyValueStoreAssociations: Optional[KeyValueStoreAssociationsTypeDef] = None


class CreateMonitoringSubscriptionRequestTypeDef(BaseValidatorModel):
    DistributionId: str
    MonitoringSubscription: MonitoringSubscriptionTypeDef


class CreateMonitoringSubscriptionResultTypeDef(BaseValidatorModel):
    MonitoringSubscription: MonitoringSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMonitoringSubscriptionResultTypeDef(BaseValidatorModel):
    MonitoringSubscription: MonitoringSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListOriginAccessControlsResultTypeDef(BaseValidatorModel):
    OriginAccessControlList: OriginAccessControlListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OriginGroupOutputTypeDef(BaseValidatorModel):
    Id: str
    FailoverCriteria: OriginGroupFailoverCriteriaOutputTypeDef
    Members: OriginGroupMembersOutputTypeDef
    SelectionCriteria: Optional[OriginGroupSelectionCriteriaType] = None


class OriginSslProtocolsUnionTypeDef(BaseValidatorModel):
    pass


class CustomOriginConfigTypeDef(BaseValidatorModel):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsUnionTypeDef] = None
    OriginReadTimeout: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None


class ListPublicKeysResultTypeDef(BaseValidatorModel):
    PublicKeyList: PublicKeyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class QueryArgProfileConfigOutputTypeDef(BaseValidatorModel):
    ForwardWhenQueryArgProfileIsUnknown: bool
    QueryArgProfiles: Optional[QueryArgProfilesOutputTypeDef] = None


class QueryArgProfileConfigTypeDef(BaseValidatorModel):
    ForwardWhenQueryArgProfileIsUnknown: bool
    QueryArgProfiles: Optional[QueryArgProfilesTypeDef] = None


class ResponseHeadersPolicyConfigOutputTypeDef(BaseValidatorModel):
    Name: str
    Comment: Optional[str] = None
    CorsConfig: Optional[ResponseHeadersPolicyCorsConfigOutputTypeDef] = None
    SecurityHeadersConfig: Optional[ResponseHeadersPolicySecurityHeadersConfigTypeDef] = None
    ServerTimingHeadersConfig: Optional[ResponseHeadersPolicyServerTimingHeadersConfigTypeDef] = None
    CustomHeadersConfig: Optional[ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef] = None
    RemoveHeadersConfig: Optional[ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef] = None


class ResponseHeadersPolicyConfigTypeDef(BaseValidatorModel):
    Name: str
    Comment: Optional[str] = None
    CorsConfig: Optional[ResponseHeadersPolicyCorsConfigTypeDef] = None
    SecurityHeadersConfig: Optional[ResponseHeadersPolicySecurityHeadersConfigTypeDef] = None
    ServerTimingHeadersConfig: Optional[ResponseHeadersPolicyServerTimingHeadersConfigTypeDef] = None
    CustomHeadersConfig: Optional[ResponseHeadersPolicyCustomHeadersConfigTypeDef] = None
    RemoveHeadersConfig: Optional[ResponseHeadersPolicyRemoveHeadersConfigTypeDef] = None


class StreamingDistributionListTypeDef(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[StreamingDistributionSummaryTypeDef]] = None


class StatusCodesUnionTypeDef(BaseValidatorModel):
    pass


class OriginGroupFailoverCriteriaTypeDef(BaseValidatorModel):
    StatusCodes: StatusCodesUnionTypeDef


class GetStreamingDistributionConfigResultTypeDef(BaseValidatorModel):
    StreamingDistributionConfig: StreamingDistributionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    Tags: TagsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TrustedSignersUnionTypeDef(BaseValidatorModel):
    pass


class AliasesUnionTypeDef(BaseValidatorModel):
    pass


class StreamingDistributionConfigTypeDef(BaseValidatorModel):
    CallerReference: str
    S3Origin: S3OriginTypeDef
    Comment: str
    TrustedSigners: TrustedSignersUnionTypeDef
    Enabled: bool
    Aliases: Optional[AliasesUnionTypeDef] = None
    Logging: Optional[StreamingLoggingConfigTypeDef] = None
    PriceClass: Optional[PriceClassType] = None


class ListVpcOriginsResultTypeDef(BaseValidatorModel):
    VpcOriginList: VpcOriginListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CacheBehaviorOutputTypeDef(BaseValidatorModel):
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
    GrpcConfig: Optional[GrpcConfigTypeDef] = None
    ForwardedValues: Optional[ForwardedValuesOutputTypeDef] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None


class DefaultCacheBehaviorOutputTypeDef(BaseValidatorModel):
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
    GrpcConfig: Optional[GrpcConfigTypeDef] = None
    ForwardedValues: Optional[ForwardedValuesOutputTypeDef] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None


class CachePolicyConfigOutputTypeDef(BaseValidatorModel):
    Name: str
    MinTTL: int
    Comment: Optional[str] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None
    ParametersInCacheKeyAndForwardedToOrigin: Optional[ ParametersInCacheKeyAndForwardedToOriginOutputTypeDef ] = None


class GetOriginRequestPolicyConfigResultTypeDef(BaseValidatorModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class OriginRequestPolicyTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    OriginRequestPolicyConfig: OriginRequestPolicyConfigOutputTypeDef


class CachePolicyConfigTypeDef(BaseValidatorModel):
    Name: str
    MinTTL: int
    Comment: Optional[str] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None
    ParametersInCacheKeyAndForwardedToOrigin: Optional[ ParametersInCacheKeyAndForwardedToOriginTypeDef ] = None


class TrafficConfigTypeDef(BaseValidatorModel):
    pass


class ContinuousDeploymentPolicyConfigOutputTypeDef(BaseValidatorModel):
    StagingDistributionDnsNames: StagingDistributionDnsNamesOutputTypeDef
    Enabled: bool
    TrafficConfig: Optional[TrafficConfigTypeDef] = None


class ContinuousDeploymentPolicyConfigTypeDef(BaseValidatorModel):
    StagingDistributionDnsNames: StagingDistributionDnsNamesTypeDef
    Enabled: bool
    TrafficConfig: Optional[TrafficConfigTypeDef] = None


class OriginsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: List[OriginOutputTypeDef]


class CreateVpcOriginResultTypeDef(BaseValidatorModel):
    VpcOrigin: VpcOriginTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVpcOriginResultTypeDef(BaseValidatorModel):
    VpcOrigin: VpcOriginTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetVpcOriginResultTypeDef(BaseValidatorModel):
    VpcOrigin: VpcOriginTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVpcOriginResultTypeDef(BaseValidatorModel):
    VpcOrigin: VpcOriginTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class FieldLevelEncryptionProfileConfigOutputTypeDef(BaseValidatorModel):
    Name: str
    CallerReference: str
    EncryptionEntities: EncryptionEntitiesOutputTypeDef
    Comment: Optional[str] = None


class FieldLevelEncryptionProfileSummaryTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    Name: str
    EncryptionEntities: EncryptionEntitiesOutputTypeDef
    Comment: Optional[str] = None


class FieldLevelEncryptionProfileConfigTypeDef(BaseValidatorModel):
    Name: str
    CallerReference: str
    EncryptionEntities: EncryptionEntitiesTypeDef
    Comment: Optional[str] = None


class CreateRealtimeLogConfigResultTypeDef(BaseValidatorModel):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRealtimeLogConfigResultTypeDef(BaseValidatorModel):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RealtimeLogConfigsTypeDef(BaseValidatorModel):
    MaxItems: int
    IsTruncated: bool
    Marker: str
    Items: Optional[List[RealtimeLogConfigTypeDef]] = None
    NextMarker: Optional[str] = None


class UpdateRealtimeLogConfigResultTypeDef(BaseValidatorModel):
    RealtimeLogConfig: RealtimeLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class KeyGroupListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[KeyGroupSummaryTypeDef]] = None


class CreateInvalidationResultTypeDef(BaseValidatorModel):
    Location: str
    Invalidation: InvalidationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetInvalidationResultTypeDef(BaseValidatorModel):
    Invalidation: InvalidationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InvalidationBatchUnionTypeDef(BaseValidatorModel):
    pass


class CreateInvalidationRequestTypeDef(BaseValidatorModel):
    DistributionId: str
    InvalidationBatch: InvalidationBatchUnionTypeDef


class StreamingDistributionTypeDef(BaseValidatorModel):
    Id: str
    ARN: str
    Status: str
    DomainName: str
    ActiveTrustedSigners: ActiveTrustedSignersTypeDef
    StreamingDistributionConfig: StreamingDistributionConfigOutputTypeDef
    LastModifiedTime: Optional[datetime] = None


class FunctionSummaryTypeDef(BaseValidatorModel):
    Name: str
    FunctionConfig: FunctionConfigOutputTypeDef
    FunctionMetadata: FunctionMetadataTypeDef
    Status: Optional[str] = None


class OriginGroupsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[OriginGroupOutputTypeDef]] = None


class VpcOriginEndpointConfigUnionTypeDef(BaseValidatorModel):
    pass


class UpdateVpcOriginRequestTypeDef(BaseValidatorModel):
    VpcOriginEndpointConfig: VpcOriginEndpointConfigUnionTypeDef
    Id: str
    IfMatch: str


class FieldLevelEncryptionConfigOutputTypeDef(BaseValidatorModel):
    CallerReference: str
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfigOutputTypeDef] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfigOutputTypeDef] = None


class FieldLevelEncryptionSummaryTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfigOutputTypeDef] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfigOutputTypeDef] = None


class FieldLevelEncryptionConfigTypeDef(BaseValidatorModel):
    CallerReference: str
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfigTypeDef] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfigTypeDef] = None


class GetResponseHeadersPolicyConfigResultTypeDef(BaseValidatorModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResponseHeadersPolicyTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigOutputTypeDef


class ListStreamingDistributionsResultTypeDef(BaseValidatorModel):
    StreamingDistributionList: StreamingDistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TagsUnionTypeDef(BaseValidatorModel):
    pass


class CreateAnycastIpListRequestTypeDef(BaseValidatorModel):
    Name: str
    IpCount: int
    Tags: Optional[TagsUnionTypeDef] = None


class CreateVpcOriginRequestTypeDef(BaseValidatorModel):
    VpcOriginEndpointConfig: VpcOriginEndpointConfigUnionTypeDef
    Tags: Optional[TagsUnionTypeDef] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    Resource: str
    Tags: TagsUnionTypeDef


class CacheBehaviorsOutputTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[CacheBehaviorOutputTypeDef]] = None


class QueryStringCacheKeysUnionTypeDef(BaseValidatorModel):
    pass


class CookiePreferenceUnionTypeDef(BaseValidatorModel):
    pass


class HeadersUnionTypeDef(BaseValidatorModel):
    pass


class ForwardedValuesTypeDef(BaseValidatorModel):
    QueryString: bool
    Cookies: CookiePreferenceUnionTypeDef
    Headers: Optional[HeadersUnionTypeDef] = None
    QueryStringCacheKeys: Optional[QueryStringCacheKeysUnionTypeDef] = None


class CachePolicyTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    CachePolicyConfig: CachePolicyConfigOutputTypeDef


class GetCachePolicyConfigResultTypeDef(BaseValidatorModel):
    CachePolicyConfig: CachePolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOriginRequestPolicyResultTypeDef(BaseValidatorModel):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetOriginRequestPolicyResultTypeDef(BaseValidatorModel):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateOriginRequestPolicyResultTypeDef(BaseValidatorModel):
    OriginRequestPolicy: OriginRequestPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class OriginRequestPolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateOriginRequestPolicyRequestTypeDef(BaseValidatorModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigUnionTypeDef


class UpdateOriginRequestPolicyRequestTypeDef(BaseValidatorModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class ContinuousDeploymentPolicyTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigOutputTypeDef


class GetContinuousDeploymentPolicyConfigResultTypeDef(BaseValidatorModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class FieldLevelEncryptionProfileTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigOutputTypeDef


class GetFieldLevelEncryptionProfileConfigResultTypeDef(BaseValidatorModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class FieldLevelEncryptionProfileListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FieldLevelEncryptionProfileSummaryTypeDef]] = None


class ListRealtimeLogConfigsResultTypeDef(BaseValidatorModel):
    RealtimeLogConfigs: RealtimeLogConfigsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListKeyGroupsResultTypeDef(BaseValidatorModel):
    KeyGroupList: KeyGroupListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStreamingDistributionResultTypeDef(BaseValidatorModel):
    StreamingDistribution: StreamingDistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStreamingDistributionWithTagsResultTypeDef(BaseValidatorModel):
    StreamingDistribution: StreamingDistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetStreamingDistributionResultTypeDef(BaseValidatorModel):
    StreamingDistribution: StreamingDistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateStreamingDistributionResultTypeDef(BaseValidatorModel):
    StreamingDistribution: StreamingDistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFunctionResultTypeDef(BaseValidatorModel):
    FunctionSummary: FunctionSummaryTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFunctionResultTypeDef(BaseValidatorModel):
    FunctionSummary: FunctionSummaryTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class FunctionListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FunctionSummaryTypeDef]] = None


class PublishFunctionResultTypeDef(BaseValidatorModel):
    FunctionSummary: FunctionSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TestResultTypeDef(BaseValidatorModel):
    FunctionSummary: Optional[FunctionSummaryTypeDef] = None
    ComputeUtilization: Optional[str] = None
    FunctionExecutionLogs: Optional[List[str]] = None
    FunctionErrorMessage: Optional[str] = None
    FunctionOutput: Optional[str] = None


class UpdateFunctionResultTypeDef(BaseValidatorModel):
    FunctionSummary: FunctionSummaryTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class FunctionConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateFunctionRequestTypeDef(BaseValidatorModel):
    Name: str
    FunctionConfig: FunctionConfigUnionTypeDef
    FunctionCode: BlobTypeDef


class UpdateFunctionRequestTypeDef(BaseValidatorModel):
    Name: str
    IfMatch: str
    FunctionConfig: FunctionConfigUnionTypeDef
    FunctionCode: BlobTypeDef


class CustomOriginConfigUnionTypeDef(BaseValidatorModel):
    pass


class CustomHeadersUnionTypeDef(BaseValidatorModel):
    pass


class OriginTypeDef(BaseValidatorModel):
    Id: str
    DomainName: str
    OriginPath: Optional[str] = None
    CustomHeaders: Optional[CustomHeadersUnionTypeDef] = None
    S3OriginConfig: Optional[S3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[CustomOriginConfigUnionTypeDef] = None
    VpcOriginConfig: Optional[VpcOriginConfigTypeDef] = None
    ConnectionAttempts: Optional[int] = None
    ConnectionTimeout: Optional[int] = None
    OriginShield: Optional[OriginShieldTypeDef] = None
    OriginAccessControlId: Optional[str] = None


class FieldLevelEncryptionTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigOutputTypeDef


class GetFieldLevelEncryptionConfigResultTypeDef(BaseValidatorModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class FieldLevelEncryptionListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FieldLevelEncryptionSummaryTypeDef]] = None


class CreateResponseHeadersPolicyResultTypeDef(BaseValidatorModel):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResponseHeadersPolicyResultTypeDef(BaseValidatorModel):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateResponseHeadersPolicyResultTypeDef(BaseValidatorModel):
    ResponseHeadersPolicy: ResponseHeadersPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResponseHeadersPolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateResponseHeadersPolicyRequestTypeDef(BaseValidatorModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigUnionTypeDef


class UpdateResponseHeadersPolicyRequestTypeDef(BaseValidatorModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class OriginGroupMembersUnionTypeDef(BaseValidatorModel):
    pass


class OriginGroupFailoverCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class OriginGroupTypeDef(BaseValidatorModel):
    Id: str
    FailoverCriteria: OriginGroupFailoverCriteriaUnionTypeDef
    Members: OriginGroupMembersUnionTypeDef
    SelectionCriteria: Optional[OriginGroupSelectionCriteriaType] = None


class StreamingDistributionConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateStreamingDistributionRequestTypeDef(BaseValidatorModel):
    StreamingDistributionConfig: StreamingDistributionConfigUnionTypeDef


class StreamingDistributionConfigWithTagsTypeDef(BaseValidatorModel):
    StreamingDistributionConfig: StreamingDistributionConfigUnionTypeDef
    Tags: TagsUnionTypeDef


class UpdateStreamingDistributionRequestTypeDef(BaseValidatorModel):
    StreamingDistributionConfig: StreamingDistributionConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class DistributionConfigOutputTypeDef(BaseValidatorModel):
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
    AnycastIpListId: Optional[str] = None


class DistributionSummaryTypeDef(BaseValidatorModel):
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
    AnycastIpListId: Optional[str] = None


class CreateCachePolicyResultTypeDef(BaseValidatorModel):
    CachePolicy: CachePolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCachePolicyResultTypeDef(BaseValidatorModel):
    CachePolicy: CachePolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCachePolicyResultTypeDef(BaseValidatorModel):
    CachePolicy: CachePolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class OriginRequestPolicySummaryTypeDef(BaseValidatorModel):
    pass


class OriginRequestPolicyListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[OriginRequestPolicySummaryTypeDef]] = None


class CachePolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateCachePolicyRequestTypeDef(BaseValidatorModel):
    CachePolicyConfig: CachePolicyConfigUnionTypeDef


class UpdateCachePolicyRequestTypeDef(BaseValidatorModel):
    CachePolicyConfig: CachePolicyConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class ContinuousDeploymentPolicySummaryTypeDef(BaseValidatorModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef


class CreateContinuousDeploymentPolicyResultTypeDef(BaseValidatorModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetContinuousDeploymentPolicyResultTypeDef(BaseValidatorModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContinuousDeploymentPolicyResultTypeDef(BaseValidatorModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicyTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ContinuousDeploymentPolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateContinuousDeploymentPolicyRequestTypeDef(BaseValidatorModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigUnionTypeDef


class UpdateContinuousDeploymentPolicyRequestTypeDef(BaseValidatorModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class CreateFieldLevelEncryptionProfileResultTypeDef(BaseValidatorModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetFieldLevelEncryptionProfileResultTypeDef(BaseValidatorModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFieldLevelEncryptionProfileResultTypeDef(BaseValidatorModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfileTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListFieldLevelEncryptionProfilesResultTypeDef(BaseValidatorModel):
    FieldLevelEncryptionProfileList: FieldLevelEncryptionProfileListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FieldLevelEncryptionProfileConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateFieldLevelEncryptionProfileRequestTypeDef(BaseValidatorModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigUnionTypeDef


class UpdateFieldLevelEncryptionProfileRequestTypeDef(BaseValidatorModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class ListFunctionsResultTypeDef(BaseValidatorModel):
    FunctionList: FunctionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TestFunctionResultTypeDef(BaseValidatorModel):
    TestResult: TestResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFieldLevelEncryptionConfigResultTypeDef(BaseValidatorModel):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetFieldLevelEncryptionResultTypeDef(BaseValidatorModel):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFieldLevelEncryptionConfigResultTypeDef(BaseValidatorModel):
    FieldLevelEncryption: FieldLevelEncryptionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListFieldLevelEncryptionConfigsResultTypeDef(BaseValidatorModel):
    FieldLevelEncryptionList: FieldLevelEncryptionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FieldLevelEncryptionConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateFieldLevelEncryptionConfigRequestTypeDef(BaseValidatorModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigUnionTypeDef


class UpdateFieldLevelEncryptionConfigRequestTypeDef(BaseValidatorModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class ResponseHeadersPolicySummaryTypeDef(BaseValidatorModel):
    pass


class ResponseHeadersPolicyListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[ResponseHeadersPolicySummaryTypeDef]] = None


class CreateStreamingDistributionWithTagsRequestTypeDef(BaseValidatorModel):
    StreamingDistributionConfigWithTags: StreamingDistributionConfigWithTagsTypeDef


class DistributionTypeDef(BaseValidatorModel):
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


class GetDistributionConfigResultTypeDef(BaseValidatorModel):
    DistributionConfig: DistributionConfigOutputTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class DistributionListTypeDef(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[DistributionSummaryTypeDef]] = None


class TrustedKeyGroupsUnionTypeDef(BaseValidatorModel):
    pass


class ForwardedValuesUnionTypeDef(BaseValidatorModel):
    pass


class LambdaFunctionAssociationsUnionTypeDef(BaseValidatorModel):
    pass


class AllowedMethodsUnionTypeDef(BaseValidatorModel):
    pass


class FunctionAssociationsUnionTypeDef(BaseValidatorModel):
    pass


class CacheBehaviorTypeDef(BaseValidatorModel):
    PathPattern: str
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersUnionTypeDef] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsUnionTypeDef] = None
    AllowedMethods: Optional[AllowedMethodsUnionTypeDef] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsUnionTypeDef] = None
    FunctionAssociations: Optional[FunctionAssociationsUnionTypeDef] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    GrpcConfig: Optional[GrpcConfigTypeDef] = None
    ForwardedValues: Optional[ForwardedValuesUnionTypeDef] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None


class DefaultCacheBehaviorTypeDef(BaseValidatorModel):
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersUnionTypeDef] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsUnionTypeDef] = None
    AllowedMethods: Optional[AllowedMethodsUnionTypeDef] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsUnionTypeDef] = None
    FunctionAssociations: Optional[FunctionAssociationsUnionTypeDef] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    GrpcConfig: Optional[GrpcConfigTypeDef] = None
    ForwardedValues: Optional[ForwardedValuesUnionTypeDef] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None


class CachePolicySummaryTypeDef(BaseValidatorModel):
    pass


class CachePolicyListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[CachePolicySummaryTypeDef]] = None


class ListOriginRequestPoliciesResultTypeDef(BaseValidatorModel):
    OriginRequestPolicyList: OriginRequestPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ContinuousDeploymentPolicyListTypeDef(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[ContinuousDeploymentPolicySummaryTypeDef]] = None


class OriginUnionTypeDef(BaseValidatorModel):
    pass


class OriginsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Sequence[OriginUnionTypeDef]


class ListResponseHeadersPoliciesResultTypeDef(BaseValidatorModel):
    ResponseHeadersPolicyList: ResponseHeadersPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OriginGroupUnionTypeDef(BaseValidatorModel):
    pass


class OriginGroupsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[OriginGroupUnionTypeDef]] = None


class CopyDistributionResultTypeDef(BaseValidatorModel):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDistributionResultTypeDef(BaseValidatorModel):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDistributionWithTagsResultTypeDef(BaseValidatorModel):
    Distribution: DistributionTypeDef
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDistributionResultTypeDef(BaseValidatorModel):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDistributionResultTypeDef(BaseValidatorModel):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDistributionWithStagingConfigResultTypeDef(BaseValidatorModel):
    Distribution: DistributionTypeDef
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributionsByAnycastIpListIdResultTypeDef(BaseValidatorModel):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributionsByRealtimeLogConfigResultTypeDef(BaseValidatorModel):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributionsByWebACLIdResultTypeDef(BaseValidatorModel):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributionsResultTypeDef(BaseValidatorModel):
    DistributionList: DistributionListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCachePoliciesResultTypeDef(BaseValidatorModel):
    CachePolicyList: CachePolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListContinuousDeploymentPoliciesResultTypeDef(BaseValidatorModel):
    ContinuousDeploymentPolicyList: ContinuousDeploymentPolicyListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CacheBehaviorUnionTypeDef(BaseValidatorModel):
    pass


class CacheBehaviorsTypeDef(BaseValidatorModel):
    Quantity: int
    Items: Optional[Sequence[CacheBehaviorUnionTypeDef]] = None


class RestrictionsUnionTypeDef(BaseValidatorModel):
    pass


class CacheBehaviorsUnionTypeDef(BaseValidatorModel):
    pass


class DefaultCacheBehaviorUnionTypeDef(BaseValidatorModel):
    pass


class CustomErrorResponsesUnionTypeDef(BaseValidatorModel):
    pass


class OriginsUnionTypeDef(BaseValidatorModel):
    pass


class OriginGroupsUnionTypeDef(BaseValidatorModel):
    pass


class DistributionConfigTypeDef(BaseValidatorModel):
    CallerReference: str
    Origins: OriginsUnionTypeDef
    DefaultCacheBehavior: DefaultCacheBehaviorUnionTypeDef
    Comment: str
    Enabled: bool
    Aliases: Optional[AliasesUnionTypeDef] = None
    DefaultRootObject: Optional[str] = None
    OriginGroups: Optional[OriginGroupsUnionTypeDef] = None
    CacheBehaviors: Optional[CacheBehaviorsUnionTypeDef] = None
    CustomErrorResponses: Optional[CustomErrorResponsesUnionTypeDef] = None
    Logging: Optional[LoggingConfigTypeDef] = None
    PriceClass: Optional[PriceClassType] = None
    ViewerCertificate: Optional[ViewerCertificateTypeDef] = None
    Restrictions: Optional[RestrictionsUnionTypeDef] = None
    WebACLId: Optional[str] = None
    HttpVersion: Optional[HttpVersionType] = None
    IsIPV6Enabled: Optional[bool] = None
    ContinuousDeploymentPolicyId: Optional[str] = None
    Staging: Optional[bool] = None
    AnycastIpListId: Optional[str] = None


class DistributionConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateDistributionRequestTypeDef(BaseValidatorModel):
    DistributionConfig: DistributionConfigUnionTypeDef


class DistributionConfigWithTagsTypeDef(BaseValidatorModel):
    DistributionConfig: DistributionConfigUnionTypeDef
    Tags: TagsUnionTypeDef


class UpdateDistributionRequestTypeDef(BaseValidatorModel):
    DistributionConfig: DistributionConfigUnionTypeDef
    Id: str
    IfMatch: Optional[str] = None


class CreateDistributionWithTagsRequestTypeDef(BaseValidatorModel):
    DistributionConfigWithTags: DistributionConfigWithTagsTypeDef



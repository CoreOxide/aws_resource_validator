from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudfront.cloudfront_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AliasICPRecordal(BaseValidatorModel):
    CNAME: Optional[str] = None
    ICPRecordalStatus: Optional[ICPRecordalStatusType] = None


class AliasesOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class Aliases(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class CachedMethodsOutput(BaseValidatorModel):
    Quantity: int
    Items: List[MethodType]


class AnycastIpListSummary(BaseValidatorModel):
    Id: str
    Name: str
    Status: str
    Arn: str
    IpCount: int
    LastModifiedTime: datetime


class AnycastIpList(BaseValidatorModel):
    Id: str
    Name: str
    Status: str
    Arn: str
    AnycastIps: List[str]
    IpCount: int
    LastModifiedTime: datetime


# This class is the input for the 'associate_alias' function.
class AssociateAliasRequest(BaseValidatorModel):
    TargetDistributionId: str
    Alias: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class GrpcConfig(BaseValidatorModel):
    Enabled: bool


class TrustedKeyGroupsOutput(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[str]] = None


class TrustedSignersOutput(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[str]] = None


class CookieNamesOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class CookieNames(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class HeadersOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class Headers(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class QueryStringNamesOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class QueryStringNames(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class CachedMethods(BaseValidatorModel):
    Quantity: int
    Items: List[MethodType]


class CloudFrontOriginAccessIdentityConfig(BaseValidatorModel):
    CallerReference: str
    Comment: str


class CloudFrontOriginAccessIdentitySummary(BaseValidatorModel):
    Id: str
    S3CanonicalUserId: str
    Comment: str


class ConflictingAlias(BaseValidatorModel):
    Alias: Optional[str] = None
    DistributionId: Optional[str] = None
    AccountId: Optional[str] = None


class ContentTypeProfile(BaseValidatorModel):
    Format: Literal['URLEncoded']
    ContentType: str
    ProfileId: Optional[str] = None


class StagingDistributionDnsNamesOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class StagingDistributionDnsNames(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class ContinuousDeploymentSingleHeaderConfig(BaseValidatorModel):
    Header: str
    Value: str


class SessionStickinessConfig(BaseValidatorModel):
    IdleTTL: int
    MaximumTTL: int


# This class is the input for the 'copy_distribution' function.
class CopyDistributionRequest(BaseValidatorModel):
    PrimaryDistributionId: str
    CallerReference: str
    Staging: Optional[bool] = None
    IfMatch: Optional[str] = None
    Enabled: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ImportSource(BaseValidatorModel):
    SourceType: Literal['S3']
    SourceARN: str


class KeyValueStore(BaseValidatorModel):
    Name: str
    Id: str
    Comment: str
    ARN: str
    LastModifiedTime: datetime
    Status: Optional[str] = None


class OriginAccessControlConfig(BaseValidatorModel):
    Name: str
    SigningProtocol: Literal['sigv4']
    SigningBehavior: OriginAccessControlSigningBehaviorsType
    OriginAccessControlOriginType: OriginAccessControlOriginTypesType
    Description: Optional[str] = None


class PublicKeyConfig(BaseValidatorModel):
    CallerReference: str
    Name: str
    EncodedKey: str
    Comment: Optional[str] = None


class CustomErrorResponse(BaseValidatorModel):
    ErrorCode: int
    ResponsePagePath: Optional[str] = None
    ResponseCode: Optional[str] = None
    ErrorCachingMinTTL: Optional[int] = None


class OriginCustomHeader(BaseValidatorModel):
    HeaderName: str
    HeaderValue: str


class OriginSslProtocolsOutput(BaseValidatorModel):
    Quantity: int
    Items: List[SslProtocolType]


# This class is the input for the 'delete_anycast_ip_list' function.
class DeleteAnycastIpListRequest(BaseValidatorModel):
    Id: str
    IfMatch: str


# This class is the input for the 'delete_cache_policy' function.
class DeleteCachePolicyRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_cloud_front_origin_access_identity' function.
class DeleteCloudFrontOriginAccessIdentityRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_continuous_deployment_policy' function.
class DeleteContinuousDeploymentPolicyRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_distribution' function.
class DeleteDistributionRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_field_level_encryption_config' function.
class DeleteFieldLevelEncryptionConfigRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_field_level_encryption_profile' function.
class DeleteFieldLevelEncryptionProfileRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_function' function.
class DeleteFunctionRequest(BaseValidatorModel):
    Name: str
    IfMatch: str


# This class is the input for the 'delete_key_group' function.
class DeleteKeyGroupRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_key_value_store' function.
class DeleteKeyValueStoreRequest(BaseValidatorModel):
    Name: str
    IfMatch: str


class DeleteMonitoringSubscriptionRequest(BaseValidatorModel):
    DistributionId: str


# This class is the input for the 'delete_origin_access_control' function.
class DeleteOriginAccessControlRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_origin_request_policy' function.
class DeleteOriginRequestPolicyRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_public_key' function.
class DeletePublicKeyRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_realtime_log_config' function.
class DeleteRealtimeLogConfigRequest(BaseValidatorModel):
    Name: Optional[str] = None
    ARN: Optional[str] = None


# This class is the input for the 'delete_response_headers_policy' function.
class DeleteResponseHeadersPolicyRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_streaming_distribution' function.
class DeleteStreamingDistributionRequest(BaseValidatorModel):
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'delete_vpc_origin' function.
class DeleteVpcOriginRequest(BaseValidatorModel):
    Id: str
    IfMatch: str


# This class is the input for the 'describe_function' function.
class DescribeFunctionRequest(BaseValidatorModel):
    Name: str
    Stage: Optional[FunctionStageType] = None


# This class is the input for the 'describe_key_value_store' function.
class DescribeKeyValueStoreRequest(BaseValidatorModel):
    Name: str


class LoggingConfig(BaseValidatorModel):
    Enabled: Optional[bool] = None
    IncludeCookies: Optional[bool] = None
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None


class ViewerCertificate(BaseValidatorModel):
    CloudFrontDefaultCertificate: Optional[bool] = None
    IAMCertificateId: Optional[str] = None
    ACMCertificateArn: Optional[str] = None
    SSLSupportMethod: Optional[SSLSupportMethodType] = None
    MinimumProtocolVersion: Optional[MinimumProtocolVersionType] = None
    Certificate: Optional[str] = None
    CertificateSource: Optional[CertificateSourceType] = None


class DistributionIdList(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[str]] = None


class FieldPatternsOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class FieldPatterns(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class KinesisStreamConfig(BaseValidatorModel):
    RoleARN: str
    StreamARN: str


class QueryStringCacheKeysOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class FunctionAssociation(BaseValidatorModel):
    FunctionARN: str
    EventType: EventTypeType


class FunctionMetadata(BaseValidatorModel):
    FunctionARN: str
    LastModifiedTime: datetime
    Stage: Optional[FunctionStageType] = None
    CreatedTime: Optional[datetime] = None


class GeoRestrictionOutput(BaseValidatorModel):
    RestrictionType: GeoRestrictionTypeType
    Quantity: int
    Items: Optional[List[str]] = None


class GeoRestriction(BaseValidatorModel):
    RestrictionType: GeoRestrictionTypeType
    Quantity: int
    Items: Optional[List[str]] = None


# This class is the input for the 'get_anycast_ip_list' function.
class GetAnycastIpListRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_cache_policy_config' function.
class GetCachePolicyConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_cache_policy' function.
class GetCachePolicyRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_cloud_front_origin_access_identity_config' function.
class GetCloudFrontOriginAccessIdentityConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_cloud_front_origin_access_identity' function.
class GetCloudFrontOriginAccessIdentityRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_continuous_deployment_policy_config' function.
class GetContinuousDeploymentPolicyConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_continuous_deployment_policy' function.
class GetContinuousDeploymentPolicyRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_distribution_config' function.
class GetDistributionConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_distribution' function.
class GetDistributionRequest(BaseValidatorModel):
    Id: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'get_field_level_encryption_config' function.
class GetFieldLevelEncryptionConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_field_level_encryption_profile_config' function.
class GetFieldLevelEncryptionProfileConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_field_level_encryption_profile' function.
class GetFieldLevelEncryptionProfileRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_field_level_encryption' function.
class GetFieldLevelEncryptionRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_function' function.
class GetFunctionRequest(BaseValidatorModel):
    Name: str
    Stage: Optional[FunctionStageType] = None


# This class is the input for the 'get_invalidation' function.
class GetInvalidationRequest(BaseValidatorModel):
    DistributionId: str
    Id: str


# This class is the input for the 'get_key_group_config' function.
class GetKeyGroupConfigRequest(BaseValidatorModel):
    Id: str


class KeyGroupConfigOutput(BaseValidatorModel):
    Name: str
    Items: List[str]
    Comment: Optional[str] = None


# This class is the input for the 'get_key_group' function.
class GetKeyGroupRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_monitoring_subscription' function.
class GetMonitoringSubscriptionRequest(BaseValidatorModel):
    DistributionId: str


# This class is the input for the 'get_origin_access_control_config' function.
class GetOriginAccessControlConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_origin_access_control' function.
class GetOriginAccessControlRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_origin_request_policy_config' function.
class GetOriginRequestPolicyConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_origin_request_policy' function.
class GetOriginRequestPolicyRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_public_key_config' function.
class GetPublicKeyConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_public_key' function.
class GetPublicKeyRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_realtime_log_config' function.
class GetRealtimeLogConfigRequest(BaseValidatorModel):
    Name: Optional[str] = None
    ARN: Optional[str] = None


# This class is the input for the 'get_response_headers_policy_config' function.
class GetResponseHeadersPolicyConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_response_headers_policy' function.
class GetResponseHeadersPolicyRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_streaming_distribution_config' function.
class GetStreamingDistributionConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_streaming_distribution' function.
class GetStreamingDistributionRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_vpc_origin' function.
class GetVpcOriginRequest(BaseValidatorModel):
    Id: str


class PathsOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class Paths(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class InvalidationSummary(BaseValidatorModel):
    Id: str
    CreateTime: datetime
    Status: str


class KeyPairIds(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class KeyGroupConfig(BaseValidatorModel):
    Name: str
    Items: List[str]
    Comment: Optional[str] = None


class KeyValueStoreAssociation(BaseValidatorModel):
    KeyValueStoreARN: str


class LambdaFunctionAssociation(BaseValidatorModel):
    LambdaFunctionARN: str
    EventType: EventTypeType
    IncludeBody: Optional[bool] = None


# This class is the input for the 'list_anycast_ip_lists' function.
class ListAnycastIpListsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_cache_policies' function.
class ListCachePoliciesRequest(BaseValidatorModel):
    Type: Optional[CachePolicyTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_cloud_front_origin_access_identities' function.
class ListCloudFrontOriginAccessIdentitiesRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_conflicting_aliases' function.
class ListConflictingAliasesRequest(BaseValidatorModel):
    DistributionId: str
    Alias: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_continuous_deployment_policies' function.
class ListContinuousDeploymentPoliciesRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_distributions_by_anycast_ip_list_id' function.
class ListDistributionsByAnycastIpListIdRequest(BaseValidatorModel):
    AnycastIpListId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_distributions_by_cache_policy_id' function.
class ListDistributionsByCachePolicyIdRequest(BaseValidatorModel):
    CachePolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_distributions_by_key_group' function.
class ListDistributionsByKeyGroupRequest(BaseValidatorModel):
    KeyGroupId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_distributions_by_origin_request_policy_id' function.
class ListDistributionsByOriginRequestPolicyIdRequest(BaseValidatorModel):
    OriginRequestPolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_distributions_by_realtime_log_config' function.
class ListDistributionsByRealtimeLogConfigRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    RealtimeLogConfigName: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None


# This class is the input for the 'list_distributions_by_response_headers_policy_id' function.
class ListDistributionsByResponseHeadersPolicyIdRequest(BaseValidatorModel):
    ResponseHeadersPolicyId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_distributions_by_vpc_origin_id' function.
class ListDistributionsByVpcOriginIdRequest(BaseValidatorModel):
    VpcOriginId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_distributions_by_web_acl_id' function.
class ListDistributionsByWebACLIdRequest(BaseValidatorModel):
    WebACLId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_distributions' function.
class ListDistributionsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_field_level_encryption_configs' function.
class ListFieldLevelEncryptionConfigsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_field_level_encryption_profiles' function.
class ListFieldLevelEncryptionProfilesRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_functions' function.
class ListFunctionsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    Stage: Optional[FunctionStageType] = None


# This class is the input for the 'list_invalidations' function.
class ListInvalidationsRequest(BaseValidatorModel):
    DistributionId: str
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_key_groups' function.
class ListKeyGroupsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_key_value_stores' function.
class ListKeyValueStoresRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    Status: Optional[str] = None


# This class is the input for the 'list_origin_access_controls' function.
class ListOriginAccessControlsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_origin_request_policies' function.
class ListOriginRequestPoliciesRequest(BaseValidatorModel):
    Type: Optional[OriginRequestPolicyTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_public_keys' function.
class ListPublicKeysRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_realtime_log_configs' function.
class ListRealtimeLogConfigsRequest(BaseValidatorModel):
    MaxItems: Optional[str] = None
    Marker: Optional[str] = None


# This class is the input for the 'list_response_headers_policies' function.
class ListResponseHeadersPoliciesRequest(BaseValidatorModel):
    Type: Optional[ResponseHeadersPolicyTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_streaming_distributions' function.
class ListStreamingDistributionsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    Resource: str


# This class is the input for the 'list_vpc_origins' function.
class ListVpcOriginsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class RealtimeMetricsSubscriptionConfig(BaseValidatorModel):
    RealtimeMetricsSubscriptionStatus: RealtimeMetricsSubscriptionStatusType


class OriginAccessControlSummary(BaseValidatorModel):
    Id: str
    Description: str
    Name: str
    SigningProtocol: Literal['sigv4']
    SigningBehavior: OriginAccessControlSigningBehaviorsType
    OriginAccessControlOriginType: OriginAccessControlOriginTypesType


class StatusCodesOutput(BaseValidatorModel):
    Quantity: int
    Items: List[int]


class OriginGroupMember(BaseValidatorModel):
    OriginId: str


class OriginShield(BaseValidatorModel):
    Enabled: bool
    OriginShieldRegion: Optional[str] = None


class S3OriginConfig(BaseValidatorModel):
    OriginAccessIdentity: str


class VpcOriginConfig(BaseValidatorModel):
    VpcOriginId: str
    OriginReadTimeout: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None


class OriginSslProtocols(BaseValidatorModel):
    Quantity: int
    Items: List[SslProtocolType]


class PublicKeySummary(BaseValidatorModel):
    Id: str
    Name: str
    CreatedTime: datetime
    EncodedKey: str
    Comment: Optional[str] = None


# This class is the input for the 'publish_function' function.
class PublishFunctionRequest(BaseValidatorModel):
    Name: str
    IfMatch: str


class QueryArgProfile(BaseValidatorModel):
    QueryArg: str
    ProfileId: str


class QueryStringCacheKeys(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class ResponseHeadersPolicyAccessControlAllowHeadersOutput(BaseValidatorModel):
    Quantity: int
    Items: List[str]


class ResponseHeadersPolicyAccessControlAllowHeaders(BaseValidatorModel):
    Quantity: int
    Items: List[str]


class ResponseHeadersPolicyAccessControlAllowMethodsOutput(BaseValidatorModel):
    Quantity: int
    Items: List[ResponseHeadersPolicyAccessControlAllowMethodsValuesType]


class ResponseHeadersPolicyAccessControlAllowMethods(BaseValidatorModel):
    Quantity: int
    Items: List[ResponseHeadersPolicyAccessControlAllowMethodsValuesType]


class ResponseHeadersPolicyAccessControlAllowOriginsOutput(BaseValidatorModel):
    Quantity: int
    Items: List[str]


class ResponseHeadersPolicyAccessControlAllowOrigins(BaseValidatorModel):
    Quantity: int
    Items: List[str]


class ResponseHeadersPolicyAccessControlExposeHeadersOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class ResponseHeadersPolicyAccessControlExposeHeaders(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[str]] = None


class ResponseHeadersPolicyServerTimingHeadersConfig(BaseValidatorModel):
    Enabled: bool
    SamplingRate: Optional[float] = None


class ResponseHeadersPolicyContentSecurityPolicy(BaseValidatorModel):
    Override: bool
    ContentSecurityPolicy: str


class ResponseHeadersPolicyContentTypeOptions(BaseValidatorModel):
    Override: bool


class ResponseHeadersPolicyCustomHeader(BaseValidatorModel):
    Header: str
    Value: str
    Override: bool


class ResponseHeadersPolicyFrameOptions(BaseValidatorModel):
    Override: bool
    FrameOption: FrameOptionsListType


class ResponseHeadersPolicyReferrerPolicy(BaseValidatorModel):
    Override: bool
    ReferrerPolicy: ReferrerPolicyListType


class ResponseHeadersPolicyRemoveHeader(BaseValidatorModel):
    Header: str


class ResponseHeadersPolicyStrictTransportSecurity(BaseValidatorModel):
    Override: bool
    AccessControlMaxAgeSec: int
    IncludeSubdomains: Optional[bool] = None
    Preload: Optional[bool] = None


class ResponseHeadersPolicyXSSProtection(BaseValidatorModel):
    Override: bool
    Protection: bool
    ModeBlock: Optional[bool] = None
    ReportUri: Optional[str] = None


class S3Origin(BaseValidatorModel):
    DomainName: str
    OriginAccessIdentity: str


class StatusCodes(BaseValidatorModel):
    Quantity: int
    Items: List[int]


class StreamingLoggingConfig(BaseValidatorModel):
    Enabled: bool
    Bucket: str
    Prefix: str


class TagKeys(BaseValidatorModel):
    Items: Optional[List[str]] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class TrustedKeyGroups(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[str]] = None


class TrustedSigners(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[str]] = None


# This class is the input for the 'update_distribution_with_staging_config' function.
class UpdateDistributionWithStagingConfigRequest(BaseValidatorModel):
    Id: str
    StagingDistributionId: Optional[str] = None
    IfMatch: Optional[str] = None


# This class is the input for the 'update_key_value_store' function.
class UpdateKeyValueStoreRequest(BaseValidatorModel):
    Name: str
    Comment: str
    IfMatch: str


class VpcOriginSummary(BaseValidatorModel):
    Id: str
    Name: str
    Status: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    Arn: str
    OriginEndpointArn: str

AliasesUnion = Union[Aliases, AliasesOutput]


class AllowedMethodsOutput(BaseValidatorModel):
    Quantity: int
    Items: List[MethodType]
    CachedMethods: Optional[CachedMethodsOutput] = None


class AnycastIpListCollection(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    Items: Optional[List[AnycastIpListSummary]] = None
    NextMarker: Optional[str] = None


# This class is the input for the 'test_function' function.
class TestFunctionRequest(BaseValidatorModel):
    Name: str
    IfMatch: str
    EventObject: Blob
    Stage: Optional[FunctionStageType] = None


class CachePolicyCookiesConfigOutput(BaseValidatorModel):
    CookieBehavior: CachePolicyCookieBehaviorType
    Cookies: Optional[CookieNamesOutput] = None


class CookiePreferenceOutput(BaseValidatorModel):
    Forward: ItemSelectionType
    WhitelistedNames: Optional[CookieNamesOutput] = None


class OriginRequestPolicyCookiesConfigOutput(BaseValidatorModel):
    CookieBehavior: OriginRequestPolicyCookieBehaviorType
    Cookies: Optional[CookieNamesOutput] = None


class CachePolicyCookiesConfig(BaseValidatorModel):
    CookieBehavior: CachePolicyCookieBehaviorType
    Cookies: Optional[CookieNames] = None

CookieNamesUnion = Union[CookieNames, CookieNamesOutput]


class OriginRequestPolicyCookiesConfig(BaseValidatorModel):
    CookieBehavior: OriginRequestPolicyCookieBehaviorType
    Cookies: Optional[CookieNames] = None


class CachePolicyHeadersConfigOutput(BaseValidatorModel):
    HeaderBehavior: CachePolicyHeaderBehaviorType
    Headers: Optional[HeadersOutput] = None


class OriginRequestPolicyHeadersConfigOutput(BaseValidatorModel):
    HeaderBehavior: OriginRequestPolicyHeaderBehaviorType
    Headers: Optional[HeadersOutput] = None


class CachePolicyHeadersConfig(BaseValidatorModel):
    HeaderBehavior: CachePolicyHeaderBehaviorType
    Headers: Optional[Headers] = None

HeadersUnion = Union[Headers, HeadersOutput]


class OriginRequestPolicyHeadersConfig(BaseValidatorModel):
    HeaderBehavior: OriginRequestPolicyHeaderBehaviorType
    Headers: Optional[Headers] = None


class CachePolicyQueryStringsConfigOutput(BaseValidatorModel):
    QueryStringBehavior: CachePolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesOutput] = None


class OriginRequestPolicyQueryStringsConfigOutput(BaseValidatorModel):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNamesOutput] = None


class CachePolicyQueryStringsConfig(BaseValidatorModel):
    QueryStringBehavior: CachePolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNames] = None


class OriginRequestPolicyQueryStringsConfig(BaseValidatorModel):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehaviorType
    QueryStrings: Optional[QueryStringNames] = None

CachedMethodsUnion = Union[CachedMethods, CachedMethodsOutput]


class CloudFrontOriginAccessIdentity(BaseValidatorModel):
    Id: str
    S3CanonicalUserId: str
    CloudFrontOriginAccessIdentityConfig: Optional[CloudFrontOriginAccessIdentityConfig] = None


# This class is the input for the 'create_cloud_front_origin_access_identity' function.
class CreateCloudFrontOriginAccessIdentityRequest(BaseValidatorModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfig


# This class is the input for the 'update_cloud_front_origin_access_identity' function.
class UpdateCloudFrontOriginAccessIdentityRequest(BaseValidatorModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfig
    Id: str
    IfMatch: Optional[str] = None


class CloudFrontOriginAccessIdentityList(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[CloudFrontOriginAccessIdentitySummary]] = None


class ConflictingAliasesList(BaseValidatorModel):
    NextMarker: Optional[str] = None
    MaxItems: Optional[int] = None
    Quantity: Optional[int] = None
    Items: Optional[List[ConflictingAlias]] = None


class ContentTypeProfilesOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ContentTypeProfile]] = None


class ContentTypeProfiles(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ContentTypeProfile]] = None


class ContinuousDeploymentSingleWeightConfig(BaseValidatorModel):
    Weight: float
    SessionStickinessConfig: Optional[SessionStickinessConfig] = None


# This class is the output for the 'create_anycast_ip_list' function.
class CreateAnycastIpListResult(BaseValidatorModel):
    AnycastIpList: AnycastIpList
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_anycast_ip_list' function.
class GetAnycastIpListResult(BaseValidatorModel):
    AnycastIpList: AnycastIpList
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cloud_front_origin_access_identity_config' function.
class GetCloudFrontOriginAccessIdentityConfigResult(BaseValidatorModel):
    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfig
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_function' function.
class GetFunctionResult(BaseValidatorModel):
    FunctionCode: StreamingBody
    ETag: str
    ContentType: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_key_value_store' function.
class CreateKeyValueStoreRequest(BaseValidatorModel):
    Name: str
    Comment: Optional[str] = None
    ImportSource: Optional[ImportSource] = None


# This class is the output for the 'create_key_value_store' function.
class CreateKeyValueStoreResult(BaseValidatorModel):
    KeyValueStore: KeyValueStore
    ETag: str
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_key_value_store' function.
class DescribeKeyValueStoreResult(BaseValidatorModel):
    KeyValueStore: KeyValueStore
    ETag: str
    ResponseMetadata: ResponseMetadata


class KeyValueStoreList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[KeyValueStore]] = None


# This class is the output for the 'update_key_value_store' function.
class UpdateKeyValueStoreResult(BaseValidatorModel):
    KeyValueStore: KeyValueStore
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_origin_access_control' function.
class CreateOriginAccessControlRequest(BaseValidatorModel):
    OriginAccessControlConfig: OriginAccessControlConfig


# This class is the output for the 'get_origin_access_control_config' function.
class GetOriginAccessControlConfigResult(BaseValidatorModel):
    OriginAccessControlConfig: OriginAccessControlConfig
    ETag: str
    ResponseMetadata: ResponseMetadata


class OriginAccessControl(BaseValidatorModel):
    Id: str
    OriginAccessControlConfig: Optional[OriginAccessControlConfig] = None


# This class is the input for the 'update_origin_access_control' function.
class UpdateOriginAccessControlRequest(BaseValidatorModel):
    OriginAccessControlConfig: OriginAccessControlConfig
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'create_public_key' function.
class CreatePublicKeyRequest(BaseValidatorModel):
    PublicKeyConfig: PublicKeyConfig


# This class is the output for the 'get_public_key_config' function.
class GetPublicKeyConfigResult(BaseValidatorModel):
    PublicKeyConfig: PublicKeyConfig
    ETag: str
    ResponseMetadata: ResponseMetadata


class PublicKey(BaseValidatorModel):
    Id: str
    CreatedTime: datetime
    PublicKeyConfig: PublicKeyConfig


# This class is the input for the 'update_public_key' function.
class UpdatePublicKeyRequest(BaseValidatorModel):
    PublicKeyConfig: PublicKeyConfig
    Id: str
    IfMatch: Optional[str] = None


class CustomErrorResponsesOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[CustomErrorResponse]] = None


class CustomErrorResponses(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[CustomErrorResponse]] = None


class CustomHeadersOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[OriginCustomHeader]] = None


class CustomHeaders(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[OriginCustomHeader]] = None


class CustomOriginConfigOutput(BaseValidatorModel):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsOutput] = None
    OriginReadTimeout: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None


class VpcOriginEndpointConfigOutput(BaseValidatorModel):
    Name: str
    Arn: str
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsOutput] = None


# This class is the output for the 'list_distributions_by_cache_policy_id' function.
class ListDistributionsByCachePolicyIdResult(BaseValidatorModel):
    DistributionIdList: DistributionIdList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributions_by_key_group' function.
class ListDistributionsByKeyGroupResult(BaseValidatorModel):
    DistributionIdList: DistributionIdList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributions_by_origin_request_policy_id' function.
class ListDistributionsByOriginRequestPolicyIdResult(BaseValidatorModel):
    DistributionIdList: DistributionIdList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributions_by_response_headers_policy_id' function.
class ListDistributionsByResponseHeadersPolicyIdResult(BaseValidatorModel):
    DistributionIdList: DistributionIdList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributions_by_vpc_origin_id' function.
class ListDistributionsByVpcOriginIdResult(BaseValidatorModel):
    DistributionIdList: DistributionIdList
    ResponseMetadata: ResponseMetadata


class EncryptionEntityOutput(BaseValidatorModel):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: FieldPatternsOutput


class EncryptionEntity(BaseValidatorModel):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: FieldPatterns


class EndPoint(BaseValidatorModel):
    StreamType: str
    KinesisStreamConfig: Optional[KinesisStreamConfig] = None


class FunctionAssociationsOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[FunctionAssociation]] = None


class FunctionAssociations(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[FunctionAssociation]] = None


class RestrictionsOutput(BaseValidatorModel):
    GeoRestriction: GeoRestrictionOutput

GeoRestrictionUnion = Union[GeoRestriction, GeoRestrictionOutput]


class GetDistributionRequestWait(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetInvalidationRequestWait(BaseValidatorModel):
    DistributionId: str
    Id: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetStreamingDistributionRequestWait(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'get_key_group_config' function.
class GetKeyGroupConfigResult(BaseValidatorModel):
    KeyGroupConfig: KeyGroupConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata


class KeyGroup(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    KeyGroupConfig: KeyGroupConfigOutput


class InvalidationBatchOutput(BaseValidatorModel):
    Paths: PathsOutput
    CallerReference: str


class InvalidationBatch(BaseValidatorModel):
    Paths: Paths
    CallerReference: str


class InvalidationList(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[InvalidationSummary]] = None


class KGKeyPairIds(BaseValidatorModel):
    KeyGroupId: Optional[str] = None
    KeyPairIds: Optional[KeyPairIds] = None


class Signer(BaseValidatorModel):
    AwsAccountNumber: Optional[str] = None
    KeyPairIds: Optional[KeyPairIds] = None

KeyGroupConfigUnion = Union[KeyGroupConfig, KeyGroupConfigOutput]


class KeyValueStoreAssociationsOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[KeyValueStoreAssociation]] = None


class KeyValueStoreAssociations(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[KeyValueStoreAssociation]] = None


class LambdaFunctionAssociationsOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[LambdaFunctionAssociation]] = None


class LambdaFunctionAssociations(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[LambdaFunctionAssociation]] = None


class ListCloudFrontOriginAccessIdentitiesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDistributionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInvalidationsRequestPaginate(BaseValidatorModel):
    DistributionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKeyValueStoresRequestPaginate(BaseValidatorModel):
    Status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPublicKeysRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamingDistributionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class MonitoringSubscription(BaseValidatorModel):
    RealtimeMetricsSubscriptionConfig: Optional[RealtimeMetricsSubscriptionConfig] = None


class OriginAccessControlList(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[OriginAccessControlSummary]] = None


class OriginGroupFailoverCriteriaOutput(BaseValidatorModel):
    StatusCodes: StatusCodesOutput


class OriginGroupMembersOutput(BaseValidatorModel):
    Quantity: int
    Items: List[OriginGroupMember]


class OriginGroupMembers(BaseValidatorModel):
    Quantity: int
    Items: List[OriginGroupMember]

OriginSslProtocolsUnion = Union[OriginSslProtocols, OriginSslProtocolsOutput]


class VpcOriginEndpointConfig(BaseValidatorModel):
    Name: str
    Arn: str
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocols] = None


class PublicKeyList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[PublicKeySummary]] = None


class QueryArgProfilesOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[QueryArgProfile]] = None


class QueryArgProfiles(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[QueryArgProfile]] = None

QueryStringCacheKeysUnion = Union[QueryStringCacheKeys, QueryStringCacheKeysOutput]


class ResponseHeadersPolicyCorsConfigOutput(BaseValidatorModel):
    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOriginsOutput
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeadersOutput
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethodsOutput
    AccessControlAllowCredentials: bool
    OriginOverride: bool
    AccessControlExposeHeaders: Optional[ResponseHeadersPolicyAccessControlExposeHeadersOutput] = None
    AccessControlMaxAgeSec: Optional[int] = None


class ResponseHeadersPolicyCorsConfig(BaseValidatorModel):
    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOrigins
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeaders
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethods
    AccessControlAllowCredentials: bool
    OriginOverride: bool
    AccessControlExposeHeaders: Optional[ResponseHeadersPolicyAccessControlExposeHeaders] = None
    AccessControlMaxAgeSec: Optional[int] = None


class ResponseHeadersPolicyCustomHeadersConfigOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ResponseHeadersPolicyCustomHeader]] = None


class ResponseHeadersPolicyCustomHeadersConfig(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ResponseHeadersPolicyCustomHeader]] = None


class ResponseHeadersPolicyRemoveHeadersConfigOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ResponseHeadersPolicyRemoveHeader]] = None


class ResponseHeadersPolicyRemoveHeadersConfig(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[ResponseHeadersPolicyRemoveHeader]] = None


class ResponseHeadersPolicySecurityHeadersConfig(BaseValidatorModel):
    XSSProtection: Optional[ResponseHeadersPolicyXSSProtection] = None
    FrameOptions: Optional[ResponseHeadersPolicyFrameOptions] = None
    ReferrerPolicy: Optional[ResponseHeadersPolicyReferrerPolicy] = None
    ContentSecurityPolicy: Optional[ResponseHeadersPolicyContentSecurityPolicy] = None
    ContentTypeOptions: Optional[ResponseHeadersPolicyContentTypeOptions] = None
    StrictTransportSecurity: Optional[ResponseHeadersPolicyStrictTransportSecurity] = None


class StreamingDistributionSummary(BaseValidatorModel):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    DomainName: str
    S3Origin: S3Origin
    Aliases: AliasesOutput
    TrustedSigners: TrustedSignersOutput
    Comment: str
    PriceClass: PriceClassType
    Enabled: bool

StatusCodesUnion = Union[StatusCodes, StatusCodesOutput]


class StreamingDistributionConfigOutput(BaseValidatorModel):
    CallerReference: str
    S3Origin: S3Origin
    Comment: str
    TrustedSigners: TrustedSignersOutput
    Enabled: bool
    Aliases: Optional[AliasesOutput] = None
    Logging: Optional[StreamingLoggingConfig] = None
    PriceClass: Optional[PriceClassType] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    Resource: str
    TagKeys: TagKeys


class TagsOutput(BaseValidatorModel):
    Items: Optional[List[Tag]] = None


class Tags(BaseValidatorModel):
    Items: Optional[List[Tag]] = None

TrustedKeyGroupsUnion = Union[TrustedKeyGroups, TrustedKeyGroupsOutput]

TrustedSignersUnion = Union[TrustedSigners, TrustedSignersOutput]


class VpcOriginList(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[VpcOriginSummary]] = None


# This class is the output for the 'list_anycast_ip_lists' function.
class ListAnycastIpListsResult(BaseValidatorModel):
    AnycastIpLists: AnycastIpListCollection
    ResponseMetadata: ResponseMetadata


class ForwardedValuesOutput(BaseValidatorModel):
    QueryString: bool
    Cookies: CookiePreferenceOutput
    Headers: Optional[HeadersOutput] = None
    QueryStringCacheKeys: Optional[QueryStringCacheKeysOutput] = None


class CookiePreference(BaseValidatorModel):
    Forward: ItemSelectionType
    WhitelistedNames: Optional[CookieNamesUnion] = None


class ParametersInCacheKeyAndForwardedToOriginOutput(BaseValidatorModel):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: CachePolicyHeadersConfigOutput
    CookiesConfig: CachePolicyCookiesConfigOutput
    QueryStringsConfig: CachePolicyQueryStringsConfigOutput
    EnableAcceptEncodingBrotli: Optional[bool] = None


class OriginRequestPolicyConfigOutput(BaseValidatorModel):
    Name: str
    HeadersConfig: OriginRequestPolicyHeadersConfigOutput
    CookiesConfig: OriginRequestPolicyCookiesConfigOutput
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfigOutput
    Comment: Optional[str] = None


class ParametersInCacheKeyAndForwardedToOrigin(BaseValidatorModel):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: CachePolicyHeadersConfig
    CookiesConfig: CachePolicyCookiesConfig
    QueryStringsConfig: CachePolicyQueryStringsConfig
    EnableAcceptEncodingBrotli: Optional[bool] = None


class OriginRequestPolicyConfig(BaseValidatorModel):
    Name: str
    HeadersConfig: OriginRequestPolicyHeadersConfig
    CookiesConfig: OriginRequestPolicyCookiesConfig
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfig
    Comment: Optional[str] = None


class AllowedMethods(BaseValidatorModel):
    Quantity: int
    Items: List[MethodType]
    CachedMethods: Optional[CachedMethodsUnion] = None


# This class is the output for the 'create_cloud_front_origin_access_identity' function.
class CreateCloudFrontOriginAccessIdentityResult(BaseValidatorModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentity
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cloud_front_origin_access_identity' function.
class GetCloudFrontOriginAccessIdentityResult(BaseValidatorModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentity
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cloud_front_origin_access_identity' function.
class UpdateCloudFrontOriginAccessIdentityResult(BaseValidatorModel):
    CloudFrontOriginAccessIdentity: CloudFrontOriginAccessIdentity
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_cloud_front_origin_access_identities' function.
class ListCloudFrontOriginAccessIdentitiesResult(BaseValidatorModel):
    CloudFrontOriginAccessIdentityList: CloudFrontOriginAccessIdentityList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_conflicting_aliases' function.
class ListConflictingAliasesResult(BaseValidatorModel):
    ConflictingAliasesList: ConflictingAliasesList
    ResponseMetadata: ResponseMetadata


class ContentTypeProfileConfigOutput(BaseValidatorModel):
    ForwardWhenContentTypeIsUnknown: bool
    ContentTypeProfiles: Optional[ContentTypeProfilesOutput] = None


class ContentTypeProfileConfig(BaseValidatorModel):
    ForwardWhenContentTypeIsUnknown: bool
    ContentTypeProfiles: Optional[ContentTypeProfiles] = None


class TrafficConfig(BaseValidatorModel):
    Type: ContinuousDeploymentPolicyTypeType
    SingleWeightConfig: Optional[ContinuousDeploymentSingleWeightConfig] = None
    SingleHeaderConfig: Optional[ContinuousDeploymentSingleHeaderConfig] = None


# This class is the output for the 'list_key_value_stores' function.
class ListKeyValueStoresResult(BaseValidatorModel):
    KeyValueStoreList: KeyValueStoreList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_origin_access_control' function.
class CreateOriginAccessControlResult(BaseValidatorModel):
    OriginAccessControl: OriginAccessControl
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_origin_access_control' function.
class GetOriginAccessControlResult(BaseValidatorModel):
    OriginAccessControl: OriginAccessControl
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_origin_access_control' function.
class UpdateOriginAccessControlResult(BaseValidatorModel):
    OriginAccessControl: OriginAccessControl
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_public_key' function.
class CreatePublicKeyResult(BaseValidatorModel):
    PublicKey: PublicKey
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_public_key' function.
class GetPublicKeyResult(BaseValidatorModel):
    PublicKey: PublicKey
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_public_key' function.
class UpdatePublicKeyResult(BaseValidatorModel):
    PublicKey: PublicKey
    ETag: str
    ResponseMetadata: ResponseMetadata

CustomErrorResponsesUnion = Union[CustomErrorResponses, CustomErrorResponsesOutput]

CustomHeadersUnion = Union[CustomHeaders, CustomHeadersOutput]


class OriginOutput(BaseValidatorModel):
    Id: str
    DomainName: str
    OriginPath: Optional[str] = None
    CustomHeaders: Optional[CustomHeadersOutput] = None
    S3OriginConfig: Optional[S3OriginConfig] = None
    CustomOriginConfig: Optional[CustomOriginConfigOutput] = None
    VpcOriginConfig: Optional[VpcOriginConfig] = None
    ConnectionAttempts: Optional[int] = None
    ConnectionTimeout: Optional[int] = None
    OriginShield: Optional[OriginShield] = None
    OriginAccessControlId: Optional[str] = None


class VpcOrigin(BaseValidatorModel):
    Id: str
    Arn: str
    Status: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    VpcOriginEndpointConfig: VpcOriginEndpointConfigOutput


class EncryptionEntitiesOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[EncryptionEntityOutput]] = None


class EncryptionEntities(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[EncryptionEntity]] = None


# This class is the input for the 'create_realtime_log_config' function.
class CreateRealtimeLogConfigRequest(BaseValidatorModel):
    EndPoints: List[EndPoint]
    Fields: List[str]
    Name: str
    SamplingRate: int


class RealtimeLogConfig(BaseValidatorModel):
    ARN: str
    Name: str
    SamplingRate: int
    EndPoints: List[EndPoint]
    Fields: List[str]


# This class is the input for the 'update_realtime_log_config' function.
class UpdateRealtimeLogConfigRequest(BaseValidatorModel):
    EndPoints: Optional[List[EndPoint]] = None
    Fields: Optional[List[str]] = None
    Name: Optional[str] = None
    ARN: Optional[str] = None
    SamplingRate: Optional[int] = None

FunctionAssociationsUnion = Union[FunctionAssociations, FunctionAssociationsOutput]


class Restrictions(BaseValidatorModel):
    GeoRestriction: GeoRestrictionUnion


# This class is the output for the 'create_key_group' function.
class CreateKeyGroupResult(BaseValidatorModel):
    KeyGroup: KeyGroup
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_key_group' function.
class GetKeyGroupResult(BaseValidatorModel):
    KeyGroup: KeyGroup
    ETag: str
    ResponseMetadata: ResponseMetadata


class KeyGroupSummary(BaseValidatorModel):
    KeyGroup: KeyGroup


# This class is the output for the 'update_key_group' function.
class UpdateKeyGroupResult(BaseValidatorModel):
    KeyGroup: KeyGroup
    ETag: str
    ResponseMetadata: ResponseMetadata


class Invalidation(BaseValidatorModel):
    Id: str
    Status: str
    CreateTime: datetime
    InvalidationBatch: InvalidationBatchOutput

InvalidationBatchUnion = Union[InvalidationBatch, InvalidationBatchOutput]


# This class is the output for the 'list_invalidations' function.
class ListInvalidationsResult(BaseValidatorModel):
    InvalidationList: InvalidationList
    ResponseMetadata: ResponseMetadata


class ActiveTrustedKeyGroups(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[KGKeyPairIds]] = None


class ActiveTrustedSigners(BaseValidatorModel):
    Enabled: bool
    Quantity: int
    Items: Optional[List[Signer]] = None


# This class is the input for the 'create_key_group' function.
class CreateKeyGroupRequest(BaseValidatorModel):
    KeyGroupConfig: KeyGroupConfigUnion


# This class is the input for the 'update_key_group' function.
class UpdateKeyGroupRequest(BaseValidatorModel):
    KeyGroupConfig: KeyGroupConfigUnion
    Id: str
    IfMatch: Optional[str] = None


class FunctionConfigOutput(BaseValidatorModel):
    Comment: str
    Runtime: FunctionRuntimeType
    KeyValueStoreAssociations: Optional[KeyValueStoreAssociationsOutput] = None


class FunctionConfig(BaseValidatorModel):
    Comment: str
    Runtime: FunctionRuntimeType
    KeyValueStoreAssociations: Optional[KeyValueStoreAssociations] = None

LambdaFunctionAssociationsUnion = Union[LambdaFunctionAssociations, LambdaFunctionAssociationsOutput]


# This class is the input for the 'create_monitoring_subscription' function.
class CreateMonitoringSubscriptionRequest(BaseValidatorModel):
    DistributionId: str
    MonitoringSubscription: MonitoringSubscription


# This class is the output for the 'create_monitoring_subscription' function.
class CreateMonitoringSubscriptionResult(BaseValidatorModel):
    MonitoringSubscription: MonitoringSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_monitoring_subscription' function.
class GetMonitoringSubscriptionResult(BaseValidatorModel):
    MonitoringSubscription: MonitoringSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_origin_access_controls' function.
class ListOriginAccessControlsResult(BaseValidatorModel):
    OriginAccessControlList: OriginAccessControlList
    ResponseMetadata: ResponseMetadata


class OriginGroupOutput(BaseValidatorModel):
    Id: str
    FailoverCriteria: OriginGroupFailoverCriteriaOutput
    Members: OriginGroupMembersOutput
    SelectionCriteria: Optional[OriginGroupSelectionCriteriaType] = None

OriginGroupMembersUnion = Union[OriginGroupMembers, OriginGroupMembersOutput]


class CustomOriginConfig(BaseValidatorModel):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicyType
    OriginSslProtocols: Optional[OriginSslProtocolsUnion] = None
    OriginReadTimeout: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None

VpcOriginEndpointConfigUnion = Union[VpcOriginEndpointConfig, VpcOriginEndpointConfigOutput]


# This class is the output for the 'list_public_keys' function.
class ListPublicKeysResult(BaseValidatorModel):
    PublicKeyList: PublicKeyList
    ResponseMetadata: ResponseMetadata


class QueryArgProfileConfigOutput(BaseValidatorModel):
    ForwardWhenQueryArgProfileIsUnknown: bool
    QueryArgProfiles: Optional[QueryArgProfilesOutput] = None


class QueryArgProfileConfig(BaseValidatorModel):
    ForwardWhenQueryArgProfileIsUnknown: bool
    QueryArgProfiles: Optional[QueryArgProfiles] = None


class ResponseHeadersPolicyConfigOutput(BaseValidatorModel):
    Name: str
    Comment: Optional[str] = None
    CorsConfig: Optional[ResponseHeadersPolicyCorsConfigOutput] = None
    SecurityHeadersConfig: Optional[ResponseHeadersPolicySecurityHeadersConfig] = None
    ServerTimingHeadersConfig: Optional[ResponseHeadersPolicyServerTimingHeadersConfig] = None
    CustomHeadersConfig: Optional[ResponseHeadersPolicyCustomHeadersConfigOutput] = None
    RemoveHeadersConfig: Optional[ResponseHeadersPolicyRemoveHeadersConfigOutput] = None


class ResponseHeadersPolicyConfig(BaseValidatorModel):
    Name: str
    Comment: Optional[str] = None
    CorsConfig: Optional[ResponseHeadersPolicyCorsConfig] = None
    SecurityHeadersConfig: Optional[ResponseHeadersPolicySecurityHeadersConfig] = None
    ServerTimingHeadersConfig: Optional[ResponseHeadersPolicyServerTimingHeadersConfig] = None
    CustomHeadersConfig: Optional[ResponseHeadersPolicyCustomHeadersConfig] = None
    RemoveHeadersConfig: Optional[ResponseHeadersPolicyRemoveHeadersConfig] = None


class StreamingDistributionList(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[StreamingDistributionSummary]] = None


class OriginGroupFailoverCriteria(BaseValidatorModel):
    StatusCodes: StatusCodesUnion


# This class is the output for the 'get_streaming_distribution_config' function.
class GetStreamingDistributionConfigResult(BaseValidatorModel):
    StreamingDistributionConfig: StreamingDistributionConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResult(BaseValidatorModel):
    Tags: TagsOutput
    ResponseMetadata: ResponseMetadata

TagsUnion = Union[Tags, TagsOutput]


class StreamingDistributionConfig(BaseValidatorModel):
    CallerReference: str
    S3Origin: S3Origin
    Comment: str
    TrustedSigners: TrustedSignersUnion
    Enabled: bool
    Aliases: Optional[AliasesUnion] = None
    Logging: Optional[StreamingLoggingConfig] = None
    PriceClass: Optional[PriceClassType] = None


# This class is the output for the 'list_vpc_origins' function.
class ListVpcOriginsResult(BaseValidatorModel):
    VpcOriginList: VpcOriginList
    ResponseMetadata: ResponseMetadata


class CacheBehaviorOutput(BaseValidatorModel):
    PathPattern: str
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersOutput] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsOutput] = None
    AllowedMethods: Optional[AllowedMethodsOutput] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsOutput] = None
    FunctionAssociations: Optional[FunctionAssociationsOutput] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    GrpcConfig: Optional[GrpcConfig] = None
    ForwardedValues: Optional[ForwardedValuesOutput] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None


class DefaultCacheBehaviorOutput(BaseValidatorModel):
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersOutput] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsOutput] = None
    AllowedMethods: Optional[AllowedMethodsOutput] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsOutput] = None
    FunctionAssociations: Optional[FunctionAssociationsOutput] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    GrpcConfig: Optional[GrpcConfig] = None
    ForwardedValues: Optional[ForwardedValuesOutput] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None

CookiePreferenceUnion = Union[CookiePreference, CookiePreferenceOutput]


class CachePolicyConfigOutput(BaseValidatorModel):
    Name: str
    MinTTL: int
    Comment: Optional[str] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None
    ParametersInCacheKeyAndForwardedToOrigin: Optional[ParametersInCacheKeyAndForwardedToOriginOutput] = None


# This class is the output for the 'get_origin_request_policy_config' function.
class GetOriginRequestPolicyConfigResult(BaseValidatorModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata


class OriginRequestPolicy(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    OriginRequestPolicyConfig: OriginRequestPolicyConfigOutput


class CachePolicyConfig(BaseValidatorModel):
    Name: str
    MinTTL: int
    Comment: Optional[str] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None
    ParametersInCacheKeyAndForwardedToOrigin: Optional[ParametersInCacheKeyAndForwardedToOrigin] = None

OriginRequestPolicyConfigUnion = Union[OriginRequestPolicyConfig, OriginRequestPolicyConfigOutput]

AllowedMethodsUnion = Union[AllowedMethods, AllowedMethodsOutput]


class ContinuousDeploymentPolicyConfigOutput(BaseValidatorModel):
    StagingDistributionDnsNames: StagingDistributionDnsNamesOutput
    Enabled: bool
    TrafficConfig: Optional[TrafficConfig] = None


class ContinuousDeploymentPolicyConfig(BaseValidatorModel):
    StagingDistributionDnsNames: StagingDistributionDnsNames
    Enabled: bool
    TrafficConfig: Optional[TrafficConfig] = None


class OriginsOutput(BaseValidatorModel):
    Quantity: int
    Items: List[OriginOutput]


# This class is the output for the 'create_vpc_origin' function.
class CreateVpcOriginResult(BaseValidatorModel):
    VpcOrigin: VpcOrigin
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_origin' function.
class DeleteVpcOriginResult(BaseValidatorModel):
    VpcOrigin: VpcOrigin
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_vpc_origin' function.
class GetVpcOriginResult(BaseValidatorModel):
    VpcOrigin: VpcOrigin
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vpc_origin' function.
class UpdateVpcOriginResult(BaseValidatorModel):
    VpcOrigin: VpcOrigin
    ETag: str
    ResponseMetadata: ResponseMetadata


class FieldLevelEncryptionProfileConfigOutput(BaseValidatorModel):
    Name: str
    CallerReference: str
    EncryptionEntities: EncryptionEntitiesOutput
    Comment: Optional[str] = None


class FieldLevelEncryptionProfileSummary(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    Name: str
    EncryptionEntities: EncryptionEntitiesOutput
    Comment: Optional[str] = None


class FieldLevelEncryptionProfileConfig(BaseValidatorModel):
    Name: str
    CallerReference: str
    EncryptionEntities: EncryptionEntities
    Comment: Optional[str] = None


# This class is the output for the 'create_realtime_log_config' function.
class CreateRealtimeLogConfigResult(BaseValidatorModel):
    RealtimeLogConfig: RealtimeLogConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_realtime_log_config' function.
class GetRealtimeLogConfigResult(BaseValidatorModel):
    RealtimeLogConfig: RealtimeLogConfig
    ResponseMetadata: ResponseMetadata


class RealtimeLogConfigs(BaseValidatorModel):
    MaxItems: int
    IsTruncated: bool
    Marker: str
    Items: Optional[List[RealtimeLogConfig]] = None
    NextMarker: Optional[str] = None


# This class is the output for the 'update_realtime_log_config' function.
class UpdateRealtimeLogConfigResult(BaseValidatorModel):
    RealtimeLogConfig: RealtimeLogConfig
    ResponseMetadata: ResponseMetadata

RestrictionsUnion = Union[Restrictions, RestrictionsOutput]


class KeyGroupList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[KeyGroupSummary]] = None


# This class is the output for the 'create_invalidation' function.
class CreateInvalidationResult(BaseValidatorModel):
    Location: str
    Invalidation: Invalidation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_invalidation' function.
class GetInvalidationResult(BaseValidatorModel):
    Invalidation: Invalidation
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_invalidation' function.
class CreateInvalidationRequest(BaseValidatorModel):
    DistributionId: str
    InvalidationBatch: InvalidationBatchUnion


class StreamingDistribution(BaseValidatorModel):
    Id: str
    ARN: str
    Status: str
    DomainName: str
    ActiveTrustedSigners: ActiveTrustedSigners
    StreamingDistributionConfig: StreamingDistributionConfigOutput
    LastModifiedTime: Optional[datetime] = None


class FunctionSummary(BaseValidatorModel):
    Name: str
    FunctionConfig: FunctionConfigOutput
    FunctionMetadata: FunctionMetadata
    Status: Optional[str] = None

FunctionConfigUnion = Union[FunctionConfig, FunctionConfigOutput]


class OriginGroupsOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[OriginGroupOutput]] = None

CustomOriginConfigUnion = Union[CustomOriginConfig, CustomOriginConfigOutput]


# This class is the input for the 'update_vpc_origin' function.
class UpdateVpcOriginRequest(BaseValidatorModel):
    VpcOriginEndpointConfig: VpcOriginEndpointConfigUnion
    Id: str
    IfMatch: str


class FieldLevelEncryptionConfigOutput(BaseValidatorModel):
    CallerReference: str
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfigOutput] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfigOutput] = None


class FieldLevelEncryptionSummary(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfigOutput] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfigOutput] = None


class FieldLevelEncryptionConfig(BaseValidatorModel):
    CallerReference: str
    Comment: Optional[str] = None
    QueryArgProfileConfig: Optional[QueryArgProfileConfig] = None
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfig] = None


# This class is the output for the 'get_response_headers_policy_config' function.
class GetResponseHeadersPolicyConfigResult(BaseValidatorModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata


class ResponseHeadersPolicy(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigOutput

ResponseHeadersPolicyConfigUnion = Union[ResponseHeadersPolicyConfig, ResponseHeadersPolicyConfigOutput]


# This class is the output for the 'list_streaming_distributions' function.
class ListStreamingDistributionsResult(BaseValidatorModel):
    StreamingDistributionList: StreamingDistributionList
    ResponseMetadata: ResponseMetadata

OriginGroupFailoverCriteriaUnion = Union[OriginGroupFailoverCriteria, OriginGroupFailoverCriteriaOutput]


# This class is the input for the 'create_anycast_ip_list' function.
class CreateAnycastIpListRequest(BaseValidatorModel):
    Name: str
    IpCount: int
    Tags: Optional[TagsUnion] = None


# This class is the input for the 'create_vpc_origin' function.
class CreateVpcOriginRequest(BaseValidatorModel):
    VpcOriginEndpointConfig: VpcOriginEndpointConfigUnion
    Tags: Optional[TagsUnion] = None


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    Resource: str
    Tags: TagsUnion

StreamingDistributionConfigUnion = Union[StreamingDistributionConfig, StreamingDistributionConfigOutput]


class CacheBehaviorsOutput(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[CacheBehaviorOutput]] = None


class ForwardedValues(BaseValidatorModel):
    QueryString: bool
    Cookies: CookiePreferenceUnion
    Headers: Optional[HeadersUnion] = None
    QueryStringCacheKeys: Optional[QueryStringCacheKeysUnion] = None


class CachePolicy(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    CachePolicyConfig: CachePolicyConfigOutput


# This class is the output for the 'get_cache_policy_config' function.
class GetCachePolicyConfigResult(BaseValidatorModel):
    CachePolicyConfig: CachePolicyConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_origin_request_policy' function.
class CreateOriginRequestPolicyResult(BaseValidatorModel):
    OriginRequestPolicy: OriginRequestPolicy
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_origin_request_policy' function.
class GetOriginRequestPolicyResult(BaseValidatorModel):
    OriginRequestPolicy: OriginRequestPolicy
    ETag: str
    ResponseMetadata: ResponseMetadata


class OriginRequestPolicySummary(BaseValidatorModel):
    Type: OriginRequestPolicyTypeType
    OriginRequestPolicy: OriginRequestPolicy


# This class is the output for the 'update_origin_request_policy' function.
class UpdateOriginRequestPolicyResult(BaseValidatorModel):
    OriginRequestPolicy: OriginRequestPolicy
    ETag: str
    ResponseMetadata: ResponseMetadata

CachePolicyConfigUnion = Union[CachePolicyConfig, CachePolicyConfigOutput]


# This class is the input for the 'create_origin_request_policy' function.
class CreateOriginRequestPolicyRequest(BaseValidatorModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigUnion


# This class is the input for the 'update_origin_request_policy' function.
class UpdateOriginRequestPolicyRequest(BaseValidatorModel):
    OriginRequestPolicyConfig: OriginRequestPolicyConfigUnion
    Id: str
    IfMatch: Optional[str] = None


class ContinuousDeploymentPolicy(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigOutput


# This class is the output for the 'get_continuous_deployment_policy_config' function.
class GetContinuousDeploymentPolicyConfigResult(BaseValidatorModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata

ContinuousDeploymentPolicyConfigUnion = Union[ContinuousDeploymentPolicyConfig, ContinuousDeploymentPolicyConfigOutput]


class FieldLevelEncryptionProfile(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigOutput


# This class is the output for the 'get_field_level_encryption_profile_config' function.
class GetFieldLevelEncryptionProfileConfigResult(BaseValidatorModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata


class FieldLevelEncryptionProfileList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FieldLevelEncryptionProfileSummary]] = None

FieldLevelEncryptionProfileConfigUnion = Union[FieldLevelEncryptionProfileConfig, FieldLevelEncryptionProfileConfigOutput]


# This class is the output for the 'list_realtime_log_configs' function.
class ListRealtimeLogConfigsResult(BaseValidatorModel):
    RealtimeLogConfigs: RealtimeLogConfigs
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_key_groups' function.
class ListKeyGroupsResult(BaseValidatorModel):
    KeyGroupList: KeyGroupList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_streaming_distribution' function.
class CreateStreamingDistributionResult(BaseValidatorModel):
    StreamingDistribution: StreamingDistribution
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_streaming_distribution_with_tags' function.
class CreateStreamingDistributionWithTagsResult(BaseValidatorModel):
    StreamingDistribution: StreamingDistribution
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_streaming_distribution' function.
class GetStreamingDistributionResult(BaseValidatorModel):
    StreamingDistribution: StreamingDistribution
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_streaming_distribution' function.
class UpdateStreamingDistributionResult(BaseValidatorModel):
    StreamingDistribution: StreamingDistribution
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_function' function.
class CreateFunctionResult(BaseValidatorModel):
    FunctionSummary: FunctionSummary
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_function' function.
class DescribeFunctionResult(BaseValidatorModel):
    FunctionSummary: FunctionSummary
    ETag: str
    ResponseMetadata: ResponseMetadata


class FunctionList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FunctionSummary]] = None


# This class is the output for the 'publish_function' function.
class PublishFunctionResult(BaseValidatorModel):
    FunctionSummary: FunctionSummary
    ResponseMetadata: ResponseMetadata


class TestResult(BaseValidatorModel):
    FunctionSummary: Optional[FunctionSummary] = None
    ComputeUtilization: Optional[str] = None
    FunctionExecutionLogs: Optional[List[str]] = None
    FunctionErrorMessage: Optional[str] = None
    FunctionOutput: Optional[str] = None


# This class is the output for the 'update_function' function.
class UpdateFunctionResult(BaseValidatorModel):
    FunctionSummary: FunctionSummary
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_function' function.
class CreateFunctionRequest(BaseValidatorModel):
    Name: str
    FunctionConfig: FunctionConfigUnion
    FunctionCode: Blob


# This class is the input for the 'update_function' function.
class UpdateFunctionRequest(BaseValidatorModel):
    Name: str
    IfMatch: str
    FunctionConfig: FunctionConfigUnion
    FunctionCode: Blob


class Origin(BaseValidatorModel):
    Id: str
    DomainName: str
    OriginPath: Optional[str] = None
    CustomHeaders: Optional[CustomHeadersUnion] = None
    S3OriginConfig: Optional[S3OriginConfig] = None
    CustomOriginConfig: Optional[CustomOriginConfigUnion] = None
    VpcOriginConfig: Optional[VpcOriginConfig] = None
    ConnectionAttempts: Optional[int] = None
    ConnectionTimeout: Optional[int] = None
    OriginShield: Optional[OriginShield] = None
    OriginAccessControlId: Optional[str] = None


class FieldLevelEncryption(BaseValidatorModel):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigOutput


# This class is the output for the 'get_field_level_encryption_config' function.
class GetFieldLevelEncryptionConfigResult(BaseValidatorModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata


class FieldLevelEncryptionList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[FieldLevelEncryptionSummary]] = None

FieldLevelEncryptionConfigUnion = Union[FieldLevelEncryptionConfig, FieldLevelEncryptionConfigOutput]


# This class is the output for the 'create_response_headers_policy' function.
class CreateResponseHeadersPolicyResult(BaseValidatorModel):
    ResponseHeadersPolicy: ResponseHeadersPolicy
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_response_headers_policy' function.
class GetResponseHeadersPolicyResult(BaseValidatorModel):
    ResponseHeadersPolicy: ResponseHeadersPolicy
    ETag: str
    ResponseMetadata: ResponseMetadata


class ResponseHeadersPolicySummary(BaseValidatorModel):
    Type: ResponseHeadersPolicyTypeType
    ResponseHeadersPolicy: ResponseHeadersPolicy


# This class is the output for the 'update_response_headers_policy' function.
class UpdateResponseHeadersPolicyResult(BaseValidatorModel):
    ResponseHeadersPolicy: ResponseHeadersPolicy
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_response_headers_policy' function.
class CreateResponseHeadersPolicyRequest(BaseValidatorModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigUnion


# This class is the input for the 'update_response_headers_policy' function.
class UpdateResponseHeadersPolicyRequest(BaseValidatorModel):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfigUnion
    Id: str
    IfMatch: Optional[str] = None


class OriginGroup(BaseValidatorModel):
    Id: str
    FailoverCriteria: OriginGroupFailoverCriteriaUnion
    Members: OriginGroupMembersUnion
    SelectionCriteria: Optional[OriginGroupSelectionCriteriaType] = None


# This class is the input for the 'create_streaming_distribution' function.
class CreateStreamingDistributionRequest(BaseValidatorModel):
    StreamingDistributionConfig: StreamingDistributionConfigUnion


class StreamingDistributionConfigWithTags(BaseValidatorModel):
    StreamingDistributionConfig: StreamingDistributionConfigUnion
    Tags: TagsUnion


# This class is the input for the 'update_streaming_distribution' function.
class UpdateStreamingDistributionRequest(BaseValidatorModel):
    StreamingDistributionConfig: StreamingDistributionConfigUnion
    Id: str
    IfMatch: Optional[str] = None


class DistributionConfigOutput(BaseValidatorModel):
    CallerReference: str
    Origins: OriginsOutput
    DefaultCacheBehavior: DefaultCacheBehaviorOutput
    Comment: str
    Enabled: bool
    Aliases: Optional[AliasesOutput] = None
    DefaultRootObject: Optional[str] = None
    OriginGroups: Optional[OriginGroupsOutput] = None
    CacheBehaviors: Optional[CacheBehaviorsOutput] = None
    CustomErrorResponses: Optional[CustomErrorResponsesOutput] = None
    Logging: Optional[LoggingConfig] = None
    PriceClass: Optional[PriceClassType] = None
    ViewerCertificate: Optional[ViewerCertificate] = None
    Restrictions: Optional[RestrictionsOutput] = None
    WebACLId: Optional[str] = None
    HttpVersion: Optional[HttpVersionType] = None
    IsIPV6Enabled: Optional[bool] = None
    ContinuousDeploymentPolicyId: Optional[str] = None
    Staging: Optional[bool] = None
    AnycastIpListId: Optional[str] = None


class DistributionSummary(BaseValidatorModel):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    DomainName: str
    Aliases: AliasesOutput
    Origins: OriginsOutput
    DefaultCacheBehavior: DefaultCacheBehaviorOutput
    CacheBehaviors: CacheBehaviorsOutput
    CustomErrorResponses: CustomErrorResponsesOutput
    Comment: str
    PriceClass: PriceClassType
    Enabled: bool
    ViewerCertificate: ViewerCertificate
    Restrictions: RestrictionsOutput
    WebACLId: str
    HttpVersion: HttpVersionType
    IsIPV6Enabled: bool
    Staging: bool
    OriginGroups: Optional[OriginGroupsOutput] = None
    AliasICPRecordals: Optional[List[AliasICPRecordal]] = None
    AnycastIpListId: Optional[str] = None

ForwardedValuesUnion = Union[ForwardedValues, ForwardedValuesOutput]


class CachePolicySummary(BaseValidatorModel):
    Type: CachePolicyTypeType
    CachePolicy: CachePolicy


# This class is the output for the 'create_cache_policy' function.
class CreateCachePolicyResult(BaseValidatorModel):
    CachePolicy: CachePolicy
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cache_policy' function.
class GetCachePolicyResult(BaseValidatorModel):
    CachePolicy: CachePolicy
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cache_policy' function.
class UpdateCachePolicyResult(BaseValidatorModel):
    CachePolicy: CachePolicy
    ETag: str
    ResponseMetadata: ResponseMetadata


class OriginRequestPolicyList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[OriginRequestPolicySummary]] = None


# This class is the input for the 'create_cache_policy' function.
class CreateCachePolicyRequest(BaseValidatorModel):
    CachePolicyConfig: CachePolicyConfigUnion


# This class is the input for the 'update_cache_policy' function.
class UpdateCachePolicyRequest(BaseValidatorModel):
    CachePolicyConfig: CachePolicyConfigUnion
    Id: str
    IfMatch: Optional[str] = None


class ContinuousDeploymentPolicySummary(BaseValidatorModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicy


# This class is the output for the 'create_continuous_deployment_policy' function.
class CreateContinuousDeploymentPolicyResult(BaseValidatorModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicy
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_continuous_deployment_policy' function.
class GetContinuousDeploymentPolicyResult(BaseValidatorModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicy
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_continuous_deployment_policy' function.
class UpdateContinuousDeploymentPolicyResult(BaseValidatorModel):
    ContinuousDeploymentPolicy: ContinuousDeploymentPolicy
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_continuous_deployment_policy' function.
class CreateContinuousDeploymentPolicyRequest(BaseValidatorModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigUnion


# This class is the input for the 'update_continuous_deployment_policy' function.
class UpdateContinuousDeploymentPolicyRequest(BaseValidatorModel):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfigUnion
    Id: str
    IfMatch: Optional[str] = None


# This class is the output for the 'create_field_level_encryption_profile' function.
class CreateFieldLevelEncryptionProfileResult(BaseValidatorModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfile
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_field_level_encryption_profile' function.
class GetFieldLevelEncryptionProfileResult(BaseValidatorModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfile
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_field_level_encryption_profile' function.
class UpdateFieldLevelEncryptionProfileResult(BaseValidatorModel):
    FieldLevelEncryptionProfile: FieldLevelEncryptionProfile
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_field_level_encryption_profiles' function.
class ListFieldLevelEncryptionProfilesResult(BaseValidatorModel):
    FieldLevelEncryptionProfileList: FieldLevelEncryptionProfileList
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_field_level_encryption_profile' function.
class CreateFieldLevelEncryptionProfileRequest(BaseValidatorModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigUnion


# This class is the input for the 'update_field_level_encryption_profile' function.
class UpdateFieldLevelEncryptionProfileRequest(BaseValidatorModel):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfigUnion
    Id: str
    IfMatch: Optional[str] = None


# This class is the output for the 'list_functions' function.
class ListFunctionsResult(BaseValidatorModel):
    FunctionList: FunctionList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_function' function.
class TestFunctionResult(BaseValidatorModel):
    TestResult: TestResult
    ResponseMetadata: ResponseMetadata

OriginUnion = Union[Origin, OriginOutput]


# This class is the output for the 'create_field_level_encryption_config' function.
class CreateFieldLevelEncryptionConfigResult(BaseValidatorModel):
    FieldLevelEncryption: FieldLevelEncryption
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_field_level_encryption' function.
class GetFieldLevelEncryptionResult(BaseValidatorModel):
    FieldLevelEncryption: FieldLevelEncryption
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_field_level_encryption_config' function.
class UpdateFieldLevelEncryptionConfigResult(BaseValidatorModel):
    FieldLevelEncryption: FieldLevelEncryption
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_field_level_encryption_configs' function.
class ListFieldLevelEncryptionConfigsResult(BaseValidatorModel):
    FieldLevelEncryptionList: FieldLevelEncryptionList
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_field_level_encryption_config' function.
class CreateFieldLevelEncryptionConfigRequest(BaseValidatorModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigUnion


# This class is the input for the 'update_field_level_encryption_config' function.
class UpdateFieldLevelEncryptionConfigRequest(BaseValidatorModel):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfigUnion
    Id: str
    IfMatch: Optional[str] = None


class ResponseHeadersPolicyList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[ResponseHeadersPolicySummary]] = None

OriginGroupUnion = Union[OriginGroup, OriginGroupOutput]


# This class is the input for the 'create_streaming_distribution_with_tags' function.
class CreateStreamingDistributionWithTagsRequest(BaseValidatorModel):
    StreamingDistributionConfigWithTags: StreamingDistributionConfigWithTags


class Distribution(BaseValidatorModel):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    InProgressInvalidationBatches: int
    DomainName: str
    DistributionConfig: DistributionConfigOutput
    ActiveTrustedSigners: Optional[ActiveTrustedSigners] = None
    ActiveTrustedKeyGroups: Optional[ActiveTrustedKeyGroups] = None
    AliasICPRecordals: Optional[List[AliasICPRecordal]] = None


# This class is the output for the 'get_distribution_config' function.
class GetDistributionConfigResult(BaseValidatorModel):
    DistributionConfig: DistributionConfigOutput
    ETag: str
    ResponseMetadata: ResponseMetadata


class DistributionList(BaseValidatorModel):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[DistributionSummary]] = None


class CacheBehavior(BaseValidatorModel):
    PathPattern: str
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersUnion] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsUnion] = None
    AllowedMethods: Optional[AllowedMethodsUnion] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsUnion] = None
    FunctionAssociations: Optional[FunctionAssociationsUnion] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    GrpcConfig: Optional[GrpcConfig] = None
    ForwardedValues: Optional[ForwardedValuesUnion] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None


class DefaultCacheBehavior(BaseValidatorModel):
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicyType
    TrustedSigners: Optional[TrustedSignersUnion] = None
    TrustedKeyGroups: Optional[TrustedKeyGroupsUnion] = None
    AllowedMethods: Optional[AllowedMethodsUnion] = None
    SmoothStreaming: Optional[bool] = None
    Compress: Optional[bool] = None
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociationsUnion] = None
    FunctionAssociations: Optional[FunctionAssociationsUnion] = None
    FieldLevelEncryptionId: Optional[str] = None
    RealtimeLogConfigArn: Optional[str] = None
    CachePolicyId: Optional[str] = None
    OriginRequestPolicyId: Optional[str] = None
    ResponseHeadersPolicyId: Optional[str] = None
    GrpcConfig: Optional[GrpcConfig] = None
    ForwardedValues: Optional[ForwardedValuesUnion] = None
    MinTTL: Optional[int] = None
    DefaultTTL: Optional[int] = None
    MaxTTL: Optional[int] = None


class CachePolicyList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[CachePolicySummary]] = None


# This class is the output for the 'list_origin_request_policies' function.
class ListOriginRequestPoliciesResult(BaseValidatorModel):
    OriginRequestPolicyList: OriginRequestPolicyList
    ResponseMetadata: ResponseMetadata


class ContinuousDeploymentPolicyList(BaseValidatorModel):
    MaxItems: int
    Quantity: int
    NextMarker: Optional[str] = None
    Items: Optional[List[ContinuousDeploymentPolicySummary]] = None


class Origins(BaseValidatorModel):
    Quantity: int
    Items: List[OriginUnion]


# This class is the output for the 'list_response_headers_policies' function.
class ListResponseHeadersPoliciesResult(BaseValidatorModel):
    ResponseHeadersPolicyList: ResponseHeadersPolicyList
    ResponseMetadata: ResponseMetadata


class OriginGroups(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[OriginGroupUnion]] = None


# This class is the output for the 'copy_distribution' function.
class CopyDistributionResult(BaseValidatorModel):
    Distribution: Distribution
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_distribution' function.
class CreateDistributionResult(BaseValidatorModel):
    Distribution: Distribution
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_distribution_with_tags' function.
class CreateDistributionWithTagsResult(BaseValidatorModel):
    Distribution: Distribution
    Location: str
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_distribution' function.
class GetDistributionResult(BaseValidatorModel):
    Distribution: Distribution
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_distribution' function.
class UpdateDistributionResult(BaseValidatorModel):
    Distribution: Distribution
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_distribution_with_staging_config' function.
class UpdateDistributionWithStagingConfigResult(BaseValidatorModel):
    Distribution: Distribution
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributions_by_anycast_ip_list_id' function.
class ListDistributionsByAnycastIpListIdResult(BaseValidatorModel):
    DistributionList: DistributionList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributions_by_realtime_log_config' function.
class ListDistributionsByRealtimeLogConfigResult(BaseValidatorModel):
    DistributionList: DistributionList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributions_by_web_acl_id' function.
class ListDistributionsByWebACLIdResult(BaseValidatorModel):
    DistributionList: DistributionList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributions' function.
class ListDistributionsResult(BaseValidatorModel):
    DistributionList: DistributionList
    ResponseMetadata: ResponseMetadata

CacheBehaviorUnion = Union[CacheBehavior, CacheBehaviorOutput]

DefaultCacheBehaviorUnion = Union[DefaultCacheBehavior, DefaultCacheBehaviorOutput]


# This class is the output for the 'list_cache_policies' function.
class ListCachePoliciesResult(BaseValidatorModel):
    CachePolicyList: CachePolicyList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_continuous_deployment_policies' function.
class ListContinuousDeploymentPoliciesResult(BaseValidatorModel):
    ContinuousDeploymentPolicyList: ContinuousDeploymentPolicyList
    ResponseMetadata: ResponseMetadata

OriginsUnion = Union[Origins, OriginsOutput]

OriginGroupsUnion = Union[OriginGroups, OriginGroupsOutput]


class CacheBehaviors(BaseValidatorModel):
    Quantity: int
    Items: Optional[List[CacheBehaviorUnion]] = None

CacheBehaviorsUnion = Union[CacheBehaviors, CacheBehaviorsOutput]


class DistributionConfig(BaseValidatorModel):
    CallerReference: str
    Origins: OriginsUnion
    DefaultCacheBehavior: DefaultCacheBehaviorUnion
    Comment: str
    Enabled: bool
    Aliases: Optional[AliasesUnion] = None
    DefaultRootObject: Optional[str] = None
    OriginGroups: Optional[OriginGroupsUnion] = None
    CacheBehaviors: Optional[CacheBehaviorsUnion] = None
    CustomErrorResponses: Optional[CustomErrorResponsesUnion] = None
    Logging: Optional[LoggingConfig] = None
    PriceClass: Optional[PriceClassType] = None
    ViewerCertificate: Optional[ViewerCertificate] = None
    Restrictions: Optional[RestrictionsUnion] = None
    WebACLId: Optional[str] = None
    HttpVersion: Optional[HttpVersionType] = None
    IsIPV6Enabled: Optional[bool] = None
    ContinuousDeploymentPolicyId: Optional[str] = None
    Staging: Optional[bool] = None
    AnycastIpListId: Optional[str] = None

DistributionConfigUnion = Union[DistributionConfig, DistributionConfigOutput]


# This class is the input for the 'create_distribution' function.
class CreateDistributionRequest(BaseValidatorModel):
    DistributionConfig: DistributionConfigUnion


class DistributionConfigWithTags(BaseValidatorModel):
    DistributionConfig: DistributionConfigUnion
    Tags: TagsUnion


# This class is the input for the 'update_distribution' function.
class UpdateDistributionRequest(BaseValidatorModel):
    DistributionConfig: DistributionConfigUnion
    Id: str
    IfMatch: Optional[str] = None


# This class is the input for the 'create_distribution_with_tags' function.
class CreateDistributionWithTagsRequest(BaseValidatorModel):
    DistributionConfigWithTags: DistributionConfigWithTags
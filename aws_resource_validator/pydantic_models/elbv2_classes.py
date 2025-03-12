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
from aws_resource_validator.pydantic_models.elbv2_constants import *

class AuthenticateCognitoActionConfigOutputTypeDef(BaseValidatorModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None
    OnUnauthenticatedRequest: Optional[AuthenticateCognitoActionConditionalBehaviorEnumType] = None


class AuthenticateOidcActionConfigOutputTypeDef(BaseValidatorModel):
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    ClientId: str
    ClientSecret: Optional[str] = None
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None
    OnUnauthenticatedRequest: Optional[AuthenticateOidcActionConditionalBehaviorEnumType] = None
    UseExistingClientSecret: Optional[bool] = None


class FixedResponseActionConfigTypeDef(BaseValidatorModel):
    StatusCode: str
    MessageBody: Optional[str] = None
    ContentType: Optional[str] = None


class CertificateTypeDef(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    IsDefault: Optional[bool] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class RevocationContentTypeDef(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    RevocationType: Optional[Literal["CRL"]] = None


class TrustStoreRevocationTypeDef(BaseValidatorModel):
    TrustStoreArn: Optional[str] = None
    RevocationId: Optional[int] = None
    RevocationType: Optional[Literal["CRL"]] = None
    NumberOfRevokedEntries: Optional[int] = None


class AdministrativeOverrideTypeDef(BaseValidatorModel):
    State: Optional[TargetAdministrativeOverrideStateEnumType] = None
    Reason: Optional[TargetAdministrativeOverrideReasonEnumType] = None
    Description: Optional[str] = None


class AnomalyDetectionTypeDef(BaseValidatorModel):
    Result: Optional[AnomalyResultEnumType] = None
    MitigationInEffect: Optional[MitigationInEffectEnumType] = None


class AuthenticateCognitoActionConfigTypeDef(BaseValidatorModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Mapping[str, str]] = None
    OnUnauthenticatedRequest: Optional[AuthenticateCognitoActionConditionalBehaviorEnumType] = None


class AuthenticateOidcActionConfigTypeDef(BaseValidatorModel):
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    ClientId: str
    ClientSecret: Optional[str] = None
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Mapping[str, str]] = None
    OnUnauthenticatedRequest: Optional[AuthenticateOidcActionConditionalBehaviorEnumType] = None
    UseExistingClientSecret: Optional[bool] = None


class LoadBalancerAddressTypeDef(BaseValidatorModel):
    IpAddress: Optional[str] = None
    AllocationId: Optional[str] = None
    PrivateIPv4Address: Optional[str] = None
    IPv6Address: Optional[str] = None


class CapacityReservationStatusTypeDef(BaseValidatorModel):
    Code: Optional[CapacityReservationStateEnumType] = None
    Reason: Optional[str] = None


class CipherTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Priority: Optional[int] = None


class MutualAuthenticationAttributesTypeDef(BaseValidatorModel):
    Mode: Optional[str] = None
    TrustStoreArn: Optional[str] = None
    IgnoreClientCertificateExpiry: Optional[bool] = None
    TrustStoreAssociationStatus: Optional[TrustStoreAssociationStatusEnumType] = None
    AdvertiseTrustStoreCaNames: Optional[AdvertiseTrustStoreCaNamesEnumType] = None


class IpamPoolsTypeDef(BaseValidatorModel):
    Ipv4IpamPoolId: Optional[str] = None


class SubnetMappingTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    AllocationId: Optional[str] = None
    PrivateIPv4Address: Optional[str] = None
    IPv6Address: Optional[str] = None
    SourceNatIpv6Prefix: Optional[str] = None


class MatcherTypeDef(BaseValidatorModel):
    HttpCode: Optional[str] = None
    GrpcCode: Optional[str] = None


class TrustStoreTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    TrustStoreArn: Optional[str] = None
    Status: Optional[TrustStoreStatusType] = None
    NumberOfCaCertificates: Optional[int] = None
    TotalRevokedEntries: Optional[int] = None


class DeleteListenerInputTypeDef(BaseValidatorModel):
    ListenerArn: str


class DeleteLoadBalancerInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str


class DeleteRuleInputTypeDef(BaseValidatorModel):
    RuleArn: str


class DeleteSharedTrustStoreAssociationInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    ResourceArn: str


class DeleteTargetGroupInputTypeDef(BaseValidatorModel):
    TargetGroupArn: str


class DeleteTrustStoreInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str


class TargetDescriptionTypeDef(BaseValidatorModel):
    Id: str
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAccountLimitsInputTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class LimitTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Max: Optional[str] = None


class DescribeCapacityReservationInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str


class MinimumLoadBalancerCapacityTypeDef(BaseValidatorModel):
    CapacityUnits: Optional[int] = None


class DescribeListenerAttributesInputTypeDef(BaseValidatorModel):
    ListenerArn: str


class ListenerAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeListenerCertificatesInputTypeDef(BaseValidatorModel):
    ListenerArn: str
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeListenersInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeLoadBalancerAttributesInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str


class LoadBalancerAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeLoadBalancersInputTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeRulesInputTypeDef(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeSSLPoliciesInputTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None


class DescribeTagsInputTypeDef(BaseValidatorModel):
    ResourceArns: Sequence[str]


class DescribeTargetGroupAttributesInputTypeDef(BaseValidatorModel):
    TargetGroupArn: str


class TargetGroupAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeTargetGroupsInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeTrustStoreAssociationsInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class TrustStoreAssociationTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class DescribeTrustStoreRevocationTypeDef(BaseValidatorModel):
    TrustStoreArn: Optional[str] = None
    RevocationId: Optional[int] = None
    RevocationType: Optional[Literal["CRL"]] = None
    NumberOfRevokedEntries: Optional[int] = None


class DescribeTrustStoreRevocationsInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: Optional[Sequence[int]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeTrustStoresInputTypeDef(BaseValidatorModel):
    TrustStoreArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class TargetGroupStickinessConfigTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    DurationSeconds: Optional[int] = None


class TargetGroupTupleTypeDef(BaseValidatorModel):
    TargetGroupArn: Optional[str] = None
    Weight: Optional[int] = None


class GetResourcePolicyInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class GetTrustStoreCaCertificatesBundleInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str


class GetTrustStoreRevocationContentInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    RevocationId: int


class HostHeaderConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None


class HostHeaderConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None


class HttpHeaderConditionConfigOutputTypeDef(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[List[str]] = None


class HttpHeaderConditionConfigTypeDef(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class HttpRequestMethodConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None


class HttpRequestMethodConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None


class LoadBalancerStateTypeDef(BaseValidatorModel):
    Code: Optional[LoadBalancerStateEnumType] = None
    Reason: Optional[str] = None


class ModifyTrustStoreInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None


class PathPatternConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None


class PathPatternConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None


class QueryStringKeyValuePairTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class RemoveTagsInputTypeDef(BaseValidatorModel):
    ResourceArns: Sequence[str]
    TagKeys: Sequence[str]


class RemoveTrustStoreRevocationsInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: Sequence[int]


class SourceIpConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None


class RulePriorityPairTypeDef(BaseValidatorModel):
    RuleArn: Optional[str] = None
    Priority: Optional[int] = None


class SetIpAddressTypeInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    IpAddressType: IpAddressTypeType


class SetSecurityGroupsInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    SecurityGroups: Sequence[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Optional[ EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType ] = None


class SourceIpConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None


class TargetHealthTypeDef(BaseValidatorModel):
    State: Optional[TargetHealthStateEnumType] = None
    Reason: Optional[TargetHealthReasonEnumType] = None
    Description: Optional[str] = None


class AddListenerCertificatesInputTypeDef(BaseValidatorModel):
    ListenerArn: str
    Certificates: Sequence[CertificateTypeDef]


class RemoveListenerCertificatesInputTypeDef(BaseValidatorModel):
    ListenerArn: str
    Certificates: Sequence[CertificateTypeDef]


class AddListenerCertificatesOutputTypeDef(BaseValidatorModel):
    Certificates: List[CertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeListenerCertificatesOutputTypeDef(BaseValidatorModel):
    Certificates: List[CertificateTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyOutputTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTrustStoreCaCertificatesBundleOutputTypeDef(BaseValidatorModel):
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTrustStoreRevocationContentOutputTypeDef(BaseValidatorModel):
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class SetIpAddressTypeOutputTypeDef(BaseValidatorModel):
    IpAddressType: IpAddressTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class SetSecurityGroupsOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: ( EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType )
    ResponseMetadata: ResponseMetadataTypeDef


class AddTagsInputTypeDef(BaseValidatorModel):
    ResourceArns: Sequence[str]
    Tags: Sequence[TagTypeDef]


class CreateTrustStoreInputTypeDef(BaseValidatorModel):
    Name: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagDescriptionTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class AddTrustStoreRevocationsInputTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    RevocationContents: Optional[Sequence[RevocationContentTypeDef]] = None


class AddTrustStoreRevocationsOutputTypeDef(BaseValidatorModel):
    TrustStoreRevocations: List[TrustStoreRevocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AvailabilityZoneTypeDef(BaseValidatorModel):
    ZoneName: Optional[str] = None
    SubnetId: Optional[str] = None
    OutpostId: Optional[str] = None
    LoadBalancerAddresses: Optional[List[LoadBalancerAddressTypeDef]] = None
    SourceNatIpv6Prefixes: Optional[List[str]] = None


class ZonalCapacityReservationStateTypeDef(BaseValidatorModel):
    State: Optional[CapacityReservationStatusTypeDef] = None
    AvailabilityZone: Optional[str] = None
    EffectiveCapacityUnits: Optional[float] = None


class SslPolicyTypeDef(BaseValidatorModel):
    SslProtocols: Optional[List[str]] = None
    Ciphers: Optional[List[CipherTypeDef]] = None
    Name: Optional[str] = None
    SupportedLoadBalancerTypes: Optional[List[str]] = None


class ModifyIpPoolsInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    IpamPools: Optional[IpamPoolsTypeDef] = None
    RemoveIpamPools: Optional[Sequence[Literal["ipv4"]]] = None


class ModifyIpPoolsOutputTypeDef(BaseValidatorModel):
    IpamPools: IpamPoolsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SetSubnetsInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    Subnets: Optional[Sequence[str]] = None
    SubnetMappings: Optional[Sequence[SubnetMappingTypeDef]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    EnablePrefixForIpv6SourceNat: Optional[EnablePrefixForIpv6SourceNatEnumType] = None


class ModifyTargetGroupInputTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    HealthCheckProtocol: Optional[ProtocolEnumType] = None
    HealthCheckPort: Optional[str] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckEnabled: Optional[bool] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    HealthCheckTimeoutSeconds: Optional[int] = None
    HealthyThresholdCount: Optional[int] = None
    UnhealthyThresholdCount: Optional[int] = None
    Matcher: Optional[MatcherTypeDef] = None


class CreateTrustStoreOutputTypeDef(BaseValidatorModel):
    TrustStores: List[TrustStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTrustStoresOutputTypeDef(BaseValidatorModel):
    TrustStores: List[TrustStoreTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyTrustStoreOutputTypeDef(BaseValidatorModel):
    TrustStores: List[TrustStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterTargetsInputTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Sequence[TargetDescriptionTypeDef]


class DescribeTargetHealthInputTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None


class RegisterTargetsInputTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Sequence[TargetDescriptionTypeDef]


class DescribeAccountLimitsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeListenerCertificatesInputPaginateTypeDef(BaseValidatorModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeListenersInputPaginateTypeDef(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeLoadBalancersInputPaginateTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRulesInputPaginateTypeDef(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSSLPoliciesInputPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTargetGroupsInputPaginateTypeDef(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAccountLimitsOutputTypeDef(BaseValidatorModel):
    Limits: List[LimitTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyCapacityReservationInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    MinimumLoadBalancerCapacity: Optional[MinimumLoadBalancerCapacityTypeDef] = None
    ResetCapacityReservation: Optional[bool] = None


class DescribeListenerAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[ListenerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyListenerAttributesInputTypeDef(BaseValidatorModel):
    ListenerArn: str
    Attributes: Sequence[ListenerAttributeTypeDef]


class ModifyListenerAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[ListenerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[LoadBalancerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyLoadBalancerAttributesInputTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    Attributes: Sequence[LoadBalancerAttributeTypeDef]


class ModifyLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[LoadBalancerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLoadBalancersInputWaitExtraExtraTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeLoadBalancersInputWaitExtraTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeLoadBalancersInputWaitTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeTargetHealthInputWaitExtraTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeTargetHealthInputWaitTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeTargetGroupAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[TargetGroupAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyTargetGroupAttributesInputTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Attributes: Sequence[TargetGroupAttributeTypeDef]


class ModifyTargetGroupAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[TargetGroupAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTrustStoreAssociationsOutputTypeDef(BaseValidatorModel):
    TrustStoreAssociations: List[TrustStoreAssociationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTrustStoreRevocationsOutputTypeDef(BaseValidatorModel):
    TrustStoreRevocations: List[DescribeTrustStoreRevocationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ForwardActionConfigOutputTypeDef(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroupTupleTypeDef]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfigTypeDef] = None


class ForwardActionConfigTypeDef(BaseValidatorModel):
    TargetGroups: Optional[Sequence[TargetGroupTupleTypeDef]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfigTypeDef] = None


class QueryStringConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[QueryStringKeyValuePairTypeDef]] = None


class QueryStringConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[QueryStringKeyValuePairTypeDef]] = None


class SetRulePrioritiesInputTypeDef(BaseValidatorModel):
    RulePriorities: Sequence[RulePriorityPairTypeDef]


class TargetHealthDescriptionTypeDef(BaseValidatorModel):
    Target: Optional[TargetDescriptionTypeDef] = None
    HealthCheckPort: Optional[str] = None
    TargetHealth: Optional[TargetHealthTypeDef] = None
    AnomalyDetection: Optional[AnomalyDetectionTypeDef] = None
    AdministrativeOverride: Optional[AdministrativeOverrideTypeDef] = None


class DescribeTagsOutputTypeDef(BaseValidatorModel):
    TagDescriptions: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SetSubnetsOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: List[AvailabilityZoneTypeDef]
    IpAddressType: IpAddressTypeType
    EnablePrefixForIpv6SourceNat: EnablePrefixForIpv6SourceNatEnumType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCapacityReservationOutputTypeDef(BaseValidatorModel):
    LastModifiedTime: datetime
    DecreaseRequestsRemaining: int
    MinimumLoadBalancerCapacity: MinimumLoadBalancerCapacityTypeDef
    CapacityReservationState: List[ZonalCapacityReservationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyCapacityReservationOutputTypeDef(BaseValidatorModel):
    LastModifiedTime: datetime
    DecreaseRequestsRemaining: int
    MinimumLoadBalancerCapacity: MinimumLoadBalancerCapacityTypeDef
    CapacityReservationState: List[ZonalCapacityReservationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSSLPoliciesOutputTypeDef(BaseValidatorModel):
    SslPolicies: List[SslPolicyTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class TargetGroupTypeDef(BaseValidatorModel):
    pass


class CreateTargetGroupOutputTypeDef(BaseValidatorModel):
    TargetGroups: List[TargetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTargetGroupsOutputTypeDef(BaseValidatorModel):
    TargetGroups: List[TargetGroupTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyTargetGroupOutputTypeDef(BaseValidatorModel):
    TargetGroups: List[TargetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RuleConditionOutputTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[List[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigOutputTypeDef] = None
    PathPatternConfig: Optional[PathPatternConditionConfigOutputTypeDef] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigOutputTypeDef] = None
    QueryStringConfig: Optional[QueryStringConditionConfigOutputTypeDef] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigOutputTypeDef] = None
    SourceIpConfig: Optional[SourceIpConditionConfigOutputTypeDef] = None


class DescribeTargetHealthOutputTypeDef(BaseValidatorModel):
    TargetHealthDescriptions: List[TargetHealthDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LoadBalancerTypeDef(BaseValidatorModel):
    pass


class CreateLoadBalancerOutputTypeDef(BaseValidatorModel):
    LoadBalancers: List[LoadBalancerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLoadBalancersOutputTypeDef(BaseValidatorModel):
    LoadBalancers: List[LoadBalancerTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ActionOutputTypeDef(BaseValidatorModel):
    pass


class RuleTypeDef(BaseValidatorModel):
    RuleArn: Optional[str] = None
    Priority: Optional[str] = None
    Conditions: Optional[List[RuleConditionOutputTypeDef]] = None
    Actions: Optional[List[ActionOutputTypeDef]] = None
    IsDefault: Optional[bool] = None


class HostHeaderConditionConfigUnionTypeDef(BaseValidatorModel):
    pass


class QueryStringConditionConfigUnionTypeDef(BaseValidatorModel):
    pass


class HttpHeaderConditionConfigUnionTypeDef(BaseValidatorModel):
    pass


class PathPatternConditionConfigUnionTypeDef(BaseValidatorModel):
    pass


class SourceIpConditionConfigUnionTypeDef(BaseValidatorModel):
    pass


class HttpRequestMethodConditionConfigUnionTypeDef(BaseValidatorModel):
    pass


class RuleConditionTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigUnionTypeDef] = None
    PathPatternConfig: Optional[PathPatternConditionConfigUnionTypeDef] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigUnionTypeDef] = None
    QueryStringConfig: Optional[QueryStringConditionConfigUnionTypeDef] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigUnionTypeDef] = None
    SourceIpConfig: Optional[SourceIpConditionConfigUnionTypeDef] = None


class ListenerTypeDef(BaseValidatorModel):
    pass


class CreateListenerOutputTypeDef(BaseValidatorModel):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeListenersOutputTypeDef(BaseValidatorModel):
    Listeners: List[ListenerTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyListenerOutputTypeDef(BaseValidatorModel):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRuleOutputTypeDef(BaseValidatorModel):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRulesOutputTypeDef(BaseValidatorModel):
    Rules: List[RuleTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyRuleOutputTypeDef(BaseValidatorModel):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SetRulePrioritiesOutputTypeDef(BaseValidatorModel):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RuleConditionUnionTypeDef(BaseValidatorModel):
    pass


class ActionUnionTypeDef(BaseValidatorModel):
    pass


class CreateRuleInputTypeDef(BaseValidatorModel):
    ListenerArn: str
    Conditions: Sequence[RuleConditionUnionTypeDef]
    Priority: int
    Actions: Sequence[ActionUnionTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None


class ModifyRuleInputTypeDef(BaseValidatorModel):
    RuleArn: str
    Conditions: Optional[Sequence[RuleConditionUnionTypeDef]] = None
    Actions: Optional[Sequence[ActionUnionTypeDef]] = None



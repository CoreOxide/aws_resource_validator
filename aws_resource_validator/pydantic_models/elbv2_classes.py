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
from aws_resource_validator.pydantic_models.elbv2_constants import *

class AuthenticateCognitoActionConfigExtraOutputTypeDef(BaseModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None
    OnUnauthenticatedRequest: Optional[       AuthenticateCognitoActionConditionalBehaviorEnumType     ] = None

class AuthenticateOidcActionConfigExtraOutputTypeDef(BaseModel):
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

class FixedResponseActionConfigTypeDef(BaseModel):
    StatusCode: str
    MessageBody: Optional[str] = None
    ContentType: Optional[str] = None

class RedirectActionConfigTypeDef(BaseModel):
    StatusCode: RedirectActionStatusCodeEnumType
    Protocol: Optional[str] = None
    Port: Optional[str] = None
    Host: Optional[str] = None
    Path: Optional[str] = None
    Query: Optional[str] = None

class AuthenticateCognitoActionConfigOutputTypeDef(BaseModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None
    OnUnauthenticatedRequest: Optional[       AuthenticateCognitoActionConditionalBehaviorEnumType     ] = None

class AuthenticateOidcActionConfigOutputTypeDef(BaseModel):
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

class AuthenticateCognitoActionConfigTypeDef(BaseModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Mapping[str, str]] = None
    OnUnauthenticatedRequest: Optional[       AuthenticateCognitoActionConditionalBehaviorEnumType     ] = None

class AuthenticateOidcActionConfigTypeDef(BaseModel):
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

class CertificateTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    IsDefault: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class RevocationContentTypeDef(BaseModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    RevocationType: Optional[Literal["CRL"]] = None

class TrustStoreRevocationTypeDef(BaseModel):
    TrustStoreArn: Optional[str] = None
    RevocationId: Optional[int] = None
    RevocationType: Optional[Literal["CRL"]] = None
    NumberOfRevokedEntries: Optional[int] = None

class AnomalyDetectionTypeDef(BaseModel):
    Result: Optional[AnomalyResultEnumType] = None
    MitigationInEffect: Optional[MitigationInEffectEnumType] = None

class LoadBalancerAddressTypeDef(BaseModel):
    IpAddress: Optional[str] = None
    AllocationId: Optional[str] = None
    PrivateIPv4Address: Optional[str] = None
    IPv6Address: Optional[str] = None

class CipherTypeDef(BaseModel):
    Name: Optional[str] = None
    Priority: Optional[int] = None

class MutualAuthenticationAttributesTypeDef(BaseModel):
    Mode: Optional[str] = None
    TrustStoreArn: Optional[str] = None
    IgnoreClientCertificateExpiry: Optional[bool] = None

class SubnetMappingTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    AllocationId: Optional[str] = None
    PrivateIPv4Address: Optional[str] = None
    IPv6Address: Optional[str] = None

class MatcherTypeDef(BaseModel):
    HttpCode: Optional[str] = None
    GrpcCode: Optional[str] = None

class TrustStoreTypeDef(BaseModel):
    Name: Optional[str] = None
    TrustStoreArn: Optional[str] = None
    Status: Optional[TrustStoreStatusType] = None
    NumberOfCaCertificates: Optional[int] = None
    TotalRevokedEntries: Optional[int] = None

class DeleteListenerInputRequestTypeDef(BaseModel):
    ListenerArn: str

class DeleteLoadBalancerInputRequestTypeDef(BaseModel):
    LoadBalancerArn: str

class DeleteRuleInputRequestTypeDef(BaseModel):
    RuleArn: str

class DeleteTargetGroupInputRequestTypeDef(BaseModel):
    TargetGroupArn: str

class DeleteTrustStoreInputRequestTypeDef(BaseModel):
    TrustStoreArn: str

class TargetDescriptionTypeDef(BaseModel):
    Id: str
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccountLimitsInputRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class LimitTypeDef(BaseModel):
    Name: Optional[str] = None
    Max: Optional[str] = None

class DescribeListenerCertificatesInputRequestTypeDef(BaseModel):
    ListenerArn: str
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeListenersInputRequestTypeDef(BaseModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeLoadBalancerAttributesInputRequestTypeDef(BaseModel):
    LoadBalancerArn: str

class LoadBalancerAttributeTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeLoadBalancersInputRequestTypeDef(BaseModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeRulesInputRequestTypeDef(BaseModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeSSLPoliciesInputRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None

class DescribeTagsInputRequestTypeDef(BaseModel):
    ResourceArns: Sequence[str]

class DescribeTargetGroupAttributesInputRequestTypeDef(BaseModel):
    TargetGroupArn: str

class TargetGroupAttributeTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class DescribeTargetGroupsInputRequestTypeDef(BaseModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeTrustStoreAssociationsInputRequestTypeDef(BaseModel):
    TrustStoreArn: str
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class TrustStoreAssociationTypeDef(BaseModel):
    ResourceArn: Optional[str] = None

class DescribeTrustStoreRevocationTypeDef(BaseModel):
    TrustStoreArn: Optional[str] = None
    RevocationId: Optional[int] = None
    RevocationType: Optional[Literal["CRL"]] = None
    NumberOfRevokedEntries: Optional[int] = None

class DescribeTrustStoreRevocationsInputRequestTypeDef(BaseModel):
    TrustStoreArn: str
    RevocationIds: Optional[Sequence[int]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeTrustStoresInputRequestTypeDef(BaseModel):
    TrustStoreArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class TargetGroupStickinessConfigTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    DurationSeconds: Optional[int] = None

class TargetGroupTupleTypeDef(BaseModel):
    TargetGroupArn: Optional[str] = None
    Weight: Optional[int] = None

class GetTrustStoreCaCertificatesBundleInputRequestTypeDef(BaseModel):
    TrustStoreArn: str

class GetTrustStoreRevocationContentInputRequestTypeDef(BaseModel):
    TrustStoreArn: str
    RevocationId: int

class HostHeaderConditionConfigExtraOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class HostHeaderConditionConfigOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class HostHeaderConditionConfigTypeDef(BaseModel):
    Values: Optional[Sequence[str]] = None

class HttpHeaderConditionConfigExtraOutputTypeDef(BaseModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[List[str]] = None

class HttpHeaderConditionConfigOutputTypeDef(BaseModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[List[str]] = None

class HttpHeaderConditionConfigTypeDef(BaseModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class HttpRequestMethodConditionConfigExtraOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class HttpRequestMethodConditionConfigOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class HttpRequestMethodConditionConfigTypeDef(BaseModel):
    Values: Optional[Sequence[str]] = None

class LoadBalancerStateTypeDef(BaseModel):
    Code: Optional[LoadBalancerStateEnumType] = None
    Reason: Optional[str] = None

class ModifyTrustStoreInputRequestTypeDef(BaseModel):
    TrustStoreArn: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None

class PathPatternConditionConfigExtraOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class PathPatternConditionConfigOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class PathPatternConditionConfigTypeDef(BaseModel):
    Values: Optional[Sequence[str]] = None

class QueryStringKeyValuePairTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class RemoveTagsInputRequestTypeDef(BaseModel):
    ResourceArns: Sequence[str]
    TagKeys: Sequence[str]

class RemoveTrustStoreRevocationsInputRequestTypeDef(BaseModel):
    TrustStoreArn: str
    RevocationIds: Sequence[int]

class SourceIpConditionConfigExtraOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class SourceIpConditionConfigOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class SourceIpConditionConfigTypeDef(BaseModel):
    Values: Optional[Sequence[str]] = None

class RulePriorityPairTypeDef(BaseModel):
    RuleArn: Optional[str] = None
    Priority: Optional[int] = None

class SetIpAddressTypeInputRequestTypeDef(BaseModel):
    LoadBalancerArn: str
    IpAddressType: IpAddressTypeType

class SetSecurityGroupsInputRequestTypeDef(BaseModel):
    LoadBalancerArn: str
    SecurityGroups: Sequence[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Optional[       EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType     ] = None

class TargetHealthTypeDef(BaseModel):
    State: Optional[TargetHealthStateEnumType] = None
    Reason: Optional[TargetHealthReasonEnumType] = None
    Description: Optional[str] = None

class AddListenerCertificatesInputRequestTypeDef(BaseModel):
    ListenerArn: str
    Certificates: Sequence[CertificateTypeDef]

class RemoveListenerCertificatesInputRequestTypeDef(BaseModel):
    ListenerArn: str
    Certificates: Sequence[CertificateTypeDef]

class AddListenerCertificatesOutputTypeDef(BaseModel):
    Certificates: List[CertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeListenerCertificatesOutputTypeDef(BaseModel):
    Certificates: List[CertificateTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreCaCertificatesBundleOutputTypeDef(BaseModel):
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreRevocationContentOutputTypeDef(BaseModel):
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetIpAddressTypeOutputTypeDef(BaseModel):
    IpAddressType: IpAddressTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class SetSecurityGroupsOutputTypeDef(BaseModel):
    SecurityGroupIds: List[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsInputRequestTypeDef(BaseModel):
    ResourceArns: Sequence[str]
    Tags: Sequence[TagTypeDef]

class CreateTrustStoreInputRequestTypeDef(BaseModel):
    Name: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagDescriptionTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class AddTrustStoreRevocationsInputRequestTypeDef(BaseModel):
    TrustStoreArn: str
    RevocationContents: Optional[Sequence[RevocationContentTypeDef]] = None

class AddTrustStoreRevocationsOutputTypeDef(BaseModel):
    TrustStoreRevocations: List[TrustStoreRevocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AvailabilityZoneTypeDef(BaseModel):
    ZoneName: Optional[str] = None
    SubnetId: Optional[str] = None
    OutpostId: Optional[str] = None
    LoadBalancerAddresses: Optional[List[LoadBalancerAddressTypeDef]] = None

class SslPolicyTypeDef(BaseModel):
    SslProtocols: Optional[List[str]] = None
    Ciphers: Optional[List[CipherTypeDef]] = None
    Name: Optional[str] = None
    SupportedLoadBalancerTypes: Optional[List[str]] = None

class CreateLoadBalancerInputRequestTypeDef(BaseModel):
    Name: str
    Subnets: Optional[Sequence[str]] = None
    SubnetMappings: Optional[Sequence[SubnetMappingTypeDef]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    Scheme: Optional[LoadBalancerSchemeEnumType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Type: Optional[LoadBalancerTypeEnumType] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None

class SetSubnetsInputRequestTypeDef(BaseModel):
    LoadBalancerArn: str
    Subnets: Optional[Sequence[str]] = None
    SubnetMappings: Optional[Sequence[SubnetMappingTypeDef]] = None
    IpAddressType: Optional[IpAddressTypeType] = None

class CreateTargetGroupInputRequestTypeDef(BaseModel):
    Name: str
    Protocol: Optional[ProtocolEnumType] = None
    ProtocolVersion: Optional[str] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    HealthCheckProtocol: Optional[ProtocolEnumType] = None
    HealthCheckPort: Optional[str] = None
    HealthCheckEnabled: Optional[bool] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    HealthCheckTimeoutSeconds: Optional[int] = None
    HealthyThresholdCount: Optional[int] = None
    UnhealthyThresholdCount: Optional[int] = None
    Matcher: Optional[MatcherTypeDef] = None
    TargetType: Optional[TargetTypeEnumType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    IpAddressType: Optional[TargetGroupIpAddressTypeEnumType] = None

class ModifyTargetGroupInputRequestTypeDef(BaseModel):
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

class TargetGroupTypeDef(BaseModel):
    TargetGroupArn: Optional[str] = None
    TargetGroupName: Optional[str] = None
    Protocol: Optional[ProtocolEnumType] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    HealthCheckProtocol: Optional[ProtocolEnumType] = None
    HealthCheckPort: Optional[str] = None
    HealthCheckEnabled: Optional[bool] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    HealthCheckTimeoutSeconds: Optional[int] = None
    HealthyThresholdCount: Optional[int] = None
    UnhealthyThresholdCount: Optional[int] = None
    HealthCheckPath: Optional[str] = None
    Matcher: Optional[MatcherTypeDef] = None
    LoadBalancerArns: Optional[List[str]] = None
    TargetType: Optional[TargetTypeEnumType] = None
    ProtocolVersion: Optional[str] = None
    IpAddressType: Optional[TargetGroupIpAddressTypeEnumType] = None

class CreateTrustStoreOutputTypeDef(BaseModel):
    TrustStores: List[TrustStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustStoresOutputTypeDef(BaseModel):
    TrustStores: List[TrustStoreTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTrustStoreOutputTypeDef(BaseModel):
    TrustStores: List[TrustStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTargetsInputRequestTypeDef(BaseModel):
    TargetGroupArn: str
    Targets: Sequence[TargetDescriptionTypeDef]

class DescribeTargetHealthInputRequestTypeDef(BaseModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None

class RegisterTargetsInputRequestTypeDef(BaseModel):
    TargetGroupArn: str
    Targets: Sequence[TargetDescriptionTypeDef]

class DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef(BaseModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeListenersInputDescribeListenersPaginateTypeDef(BaseModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef(BaseModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRulesInputDescribeRulesPaginateTypeDef(BaseModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef(BaseModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountLimitsOutputTypeDef(BaseModel):
    Limits: List[LimitTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancerAttributesOutputTypeDef(BaseModel):
    Attributes: List[LoadBalancerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLoadBalancerAttributesInputRequestTypeDef(BaseModel):
    LoadBalancerArn: str
    Attributes: Sequence[LoadBalancerAttributeTypeDef]

class ModifyLoadBalancerAttributesOutputTypeDef(BaseModel):
    Attributes: List[LoadBalancerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef(BaseModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef(BaseModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef(BaseModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTargetHealthInputTargetDeregisteredWaitTypeDef(BaseModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTargetHealthInputTargetInServiceWaitTypeDef(BaseModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTargetGroupAttributesOutputTypeDef(BaseModel):
    Attributes: List[TargetGroupAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTargetGroupAttributesInputRequestTypeDef(BaseModel):
    TargetGroupArn: str
    Attributes: Sequence[TargetGroupAttributeTypeDef]

class ModifyTargetGroupAttributesOutputTypeDef(BaseModel):
    Attributes: List[TargetGroupAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustStoreAssociationsOutputTypeDef(BaseModel):
    TrustStoreAssociations: List[TrustStoreAssociationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustStoreRevocationsOutputTypeDef(BaseModel):
    TrustStoreRevocations: List[DescribeTrustStoreRevocationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ForwardActionConfigExtraOutputTypeDef(BaseModel):
    TargetGroups: Optional[List[TargetGroupTupleTypeDef]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfigTypeDef] = None

class ForwardActionConfigOutputTypeDef(BaseModel):
    TargetGroups: Optional[List[TargetGroupTupleTypeDef]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfigTypeDef] = None

class ForwardActionConfigTypeDef(BaseModel):
    TargetGroups: Optional[Sequence[TargetGroupTupleTypeDef]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfigTypeDef] = None

class QueryStringConditionConfigExtraOutputTypeDef(BaseModel):
    Values: Optional[List[QueryStringKeyValuePairTypeDef]] = None

class QueryStringConditionConfigOutputTypeDef(BaseModel):
    Values: Optional[List[QueryStringKeyValuePairTypeDef]] = None

class QueryStringConditionConfigTypeDef(BaseModel):
    Values: Optional[Sequence[QueryStringKeyValuePairTypeDef]] = None

class SetRulePrioritiesInputRequestTypeDef(BaseModel):
    RulePriorities: Sequence[RulePriorityPairTypeDef]

class TargetHealthDescriptionTypeDef(BaseModel):
    Target: Optional[TargetDescriptionTypeDef] = None
    HealthCheckPort: Optional[str] = None
    TargetHealth: Optional[TargetHealthTypeDef] = None
    AnomalyDetection: Optional[AnomalyDetectionTypeDef] = None

class DescribeTagsOutputTypeDef(BaseModel):
    TagDescriptions: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LoadBalancerTypeDef(BaseModel):
    LoadBalancerArn: Optional[str] = None
    DNSName: Optional[str] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LoadBalancerName: Optional[str] = None
    Scheme: Optional[LoadBalancerSchemeEnumType] = None
    VpcId: Optional[str] = None
    State: Optional[LoadBalancerStateTypeDef] = None
    Type: Optional[LoadBalancerTypeEnumType] = None
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    SecurityGroups: Optional[List[str]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Optional[str] = None

class SetSubnetsOutputTypeDef(BaseModel):
    AvailabilityZones: List[AvailabilityZoneTypeDef]
    IpAddressType: IpAddressTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSSLPoliciesOutputTypeDef(BaseModel):
    SslPolicies: List[SslPolicyTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTargetGroupOutputTypeDef(BaseModel):
    TargetGroups: List[TargetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTargetGroupsOutputTypeDef(BaseModel):
    TargetGroups: List[TargetGroupTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTargetGroupOutputTypeDef(BaseModel):
    TargetGroups: List[TargetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ActionExtraOutputTypeDef(BaseModel):
    Type: ActionTypeEnumType
    TargetGroupArn: Optional[str] = None
    AuthenticateOidcConfig: Optional[AuthenticateOidcActionConfigExtraOutputTypeDef] = None
    AuthenticateCognitoConfig: Optional[AuthenticateCognitoActionConfigExtraOutputTypeDef] = None
    Order: Optional[int] = None
    RedirectConfig: Optional[RedirectActionConfigTypeDef] = None
    FixedResponseConfig: Optional[FixedResponseActionConfigTypeDef] = None
    ForwardConfig: Optional[ForwardActionConfigExtraOutputTypeDef] = None

class ActionOutputTypeDef(BaseModel):
    Type: ActionTypeEnumType
    TargetGroupArn: Optional[str] = None
    AuthenticateOidcConfig: Optional[AuthenticateOidcActionConfigOutputTypeDef] = None
    AuthenticateCognitoConfig: Optional[AuthenticateCognitoActionConfigOutputTypeDef] = None
    Order: Optional[int] = None
    RedirectConfig: Optional[RedirectActionConfigTypeDef] = None
    FixedResponseConfig: Optional[FixedResponseActionConfigTypeDef] = None
    ForwardConfig: Optional[ForwardActionConfigOutputTypeDef] = None

class ActionTypeDef(BaseModel):
    Type: ActionTypeEnumType
    TargetGroupArn: Optional[str] = None
    AuthenticateOidcConfig: Optional[AuthenticateOidcActionConfigTypeDef] = None
    AuthenticateCognitoConfig: Optional[AuthenticateCognitoActionConfigTypeDef] = None
    Order: Optional[int] = None
    RedirectConfig: Optional[RedirectActionConfigTypeDef] = None
    FixedResponseConfig: Optional[FixedResponseActionConfigTypeDef] = None
    ForwardConfig: Optional[ForwardActionConfigTypeDef] = None

class RuleConditionExtraOutputTypeDef(BaseModel):
    Field: Optional[str] = None
    Values: Optional[List[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigExtraOutputTypeDef] = None
    PathPatternConfig: Optional[PathPatternConditionConfigExtraOutputTypeDef] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigExtraOutputTypeDef] = None
    QueryStringConfig: Optional[QueryStringConditionConfigExtraOutputTypeDef] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigExtraOutputTypeDef] = None
    SourceIpConfig: Optional[SourceIpConditionConfigExtraOutputTypeDef] = None

class RuleConditionOutputTypeDef(BaseModel):
    Field: Optional[str] = None
    Values: Optional[List[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigOutputTypeDef] = None
    PathPatternConfig: Optional[PathPatternConditionConfigOutputTypeDef] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigOutputTypeDef] = None
    QueryStringConfig: Optional[QueryStringConditionConfigOutputTypeDef] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigOutputTypeDef] = None
    SourceIpConfig: Optional[SourceIpConditionConfigOutputTypeDef] = None

class RuleConditionTypeDef(BaseModel):
    Field: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigTypeDef] = None
    PathPatternConfig: Optional[PathPatternConditionConfigTypeDef] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigTypeDef] = None
    QueryStringConfig: Optional[QueryStringConditionConfigTypeDef] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigTypeDef] = None
    SourceIpConfig: Optional[SourceIpConditionConfigTypeDef] = None

class DescribeTargetHealthOutputTypeDef(BaseModel):
    TargetHealthDescriptions: List[TargetHealthDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoadBalancerOutputTypeDef(BaseModel):
    LoadBalancers: List[LoadBalancerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancersOutputTypeDef(BaseModel):
    LoadBalancers: List[LoadBalancerTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTypeDef(BaseModel):
    ListenerArn: Optional[str] = None
    LoadBalancerArn: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolEnumType] = None
    Certificates: Optional[List[CertificateTypeDef]] = None
    SslPolicy: Optional[str] = None
    DefaultActions: Optional[List[ActionOutputTypeDef]] = None
    AlpnPolicy: Optional[List[str]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributesTypeDef] = None

class RuleTypeDef(BaseModel):
    RuleArn: Optional[str] = None
    Priority: Optional[str] = None
    Conditions: Optional[List[RuleConditionOutputTypeDef]] = None
    Actions: Optional[List[ActionOutputTypeDef]] = None
    IsDefault: Optional[bool] = None

class CreateListenerOutputTypeDef(BaseModel):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeListenersOutputTypeDef(BaseModel):
    Listeners: List[ListenerTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyListenerOutputTypeDef(BaseModel):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateListenerInputRequestTypeDef(BaseModel):
    LoadBalancerArn: str
    DefaultActions: Sequence[ActionUnionTypeDef]
    Protocol: Optional[ProtocolEnumType] = None
    Port: Optional[int] = None
    SslPolicy: Optional[str] = None
    Certificates: Optional[Sequence[CertificateTypeDef]] = None
    AlpnPolicy: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributesTypeDef] = None

class ModifyListenerInputRequestTypeDef(BaseModel):
    ListenerArn: str
    Port: Optional[int] = None
    Protocol: Optional[ProtocolEnumType] = None
    SslPolicy: Optional[str] = None
    Certificates: Optional[Sequence[CertificateTypeDef]] = None
    DefaultActions: Optional[Sequence[ActionUnionTypeDef]] = None
    AlpnPolicy: Optional[Sequence[str]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributesTypeDef] = None

class CreateRuleOutputTypeDef(BaseModel):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRulesOutputTypeDef(BaseModel):
    Rules: List[RuleTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyRuleOutputTypeDef(BaseModel):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetRulePrioritiesOutputTypeDef(BaseModel):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleInputRequestTypeDef(BaseModel):
    ListenerArn: str
    Conditions: Sequence[RuleConditionUnionTypeDef]
    Priority: int
    Actions: Sequence[ActionUnionTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None

class ModifyRuleInputRequestTypeDef(BaseModel):
    RuleArn: str
    Conditions: Optional[Sequence[RuleConditionUnionTypeDef]] = None
    Actions: Optional[Sequence[ActionUnionTypeDef]] = None


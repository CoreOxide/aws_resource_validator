from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AuthenticateCognitoActionConfigExtraOutputTypeDef(BaseValidatorModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None
    OnUnauthenticatedRequest: Optional[       AuthenticateCognitoActionConditionalBehaviorEnumType     ] = None

class AuthenticateOidcActionConfigExtraOutputTypeDef(BaseValidatorModel):
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

class RedirectActionConfigTypeDef(BaseValidatorModel):
    StatusCode: RedirectActionStatusCodeEnumType
    Protocol: Optional[str] = None
    Port: Optional[str] = None
    Host: Optional[str] = None
    Path: Optional[str] = None
    Query: Optional[str] = None

class AuthenticateCognitoActionConfigOutputTypeDef(BaseValidatorModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None
    OnUnauthenticatedRequest: Optional[       AuthenticateCognitoActionConditionalBehaviorEnumType     ] = None

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

class AuthenticateCognitoActionConfigTypeDef(BaseValidatorModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Mapping[str, str]] = None
    OnUnauthenticatedRequest: Optional[       AuthenticateCognitoActionConditionalBehaviorEnumType     ] = None

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

class AnomalyDetectionTypeDef(BaseValidatorModel):
    Result: Optional[AnomalyResultEnumType] = None
    MitigationInEffect: Optional[MitigationInEffectEnumType] = None

class LoadBalancerAddressTypeDef(BaseValidatorModel):
    IpAddress: Optional[str] = None
    AllocationId: Optional[str] = None
    PrivateIPv4Address: Optional[str] = None
    IPv6Address: Optional[str] = None

class CipherTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Priority: Optional[int] = None

class MutualAuthenticationAttributesTypeDef(BaseValidatorModel):
    Mode: Optional[str] = None
    TrustStoreArn: Optional[str] = None
    IgnoreClientCertificateExpiry: Optional[bool] = None

class SubnetMappingTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    AllocationId: Optional[str] = None
    PrivateIPv4Address: Optional[str] = None
    IPv6Address: Optional[str] = None

class MatcherTypeDef(BaseValidatorModel):
    HttpCode: Optional[str] = None
    GrpcCode: Optional[str] = None

class TrustStoreTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    TrustStoreArn: Optional[str] = None
    Status: Optional[TrustStoreStatusType] = None
    NumberOfCaCertificates: Optional[int] = None
    TotalRevokedEntries: Optional[int] = None

class DeleteListenerInputRequestTypeDef(BaseValidatorModel):
    ListenerArn: str

class DeleteLoadBalancerInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: str

class DeleteRuleInputRequestTypeDef(BaseValidatorModel):
    RuleArn: str

class DeleteTargetGroupInputRequestTypeDef(BaseValidatorModel):
    TargetGroupArn: str

class DeleteTrustStoreInputRequestTypeDef(BaseValidatorModel):
    TrustStoreArn: str

class TargetDescriptionTypeDef(BaseValidatorModel):
    Id: str
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccountLimitsInputRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class LimitTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Max: Optional[str] = None

class DescribeListenerCertificatesInputRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeListenersInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeLoadBalancerAttributesInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: str

class LoadBalancerAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeLoadBalancersInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeRulesInputRequestTypeDef(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeSSLPoliciesInputRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None

class DescribeTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceArns: Sequence[str]

class DescribeTargetGroupAttributesInputRequestTypeDef(BaseValidatorModel):
    TargetGroupArn: str

class TargetGroupAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class DescribeTargetGroupsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeTrustStoreAssociationsInputRequestTypeDef(BaseValidatorModel):
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

class DescribeTrustStoreRevocationsInputRequestTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: Optional[Sequence[int]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeTrustStoresInputRequestTypeDef(BaseValidatorModel):
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

class GetTrustStoreCaCertificatesBundleInputRequestTypeDef(BaseValidatorModel):
    TrustStoreArn: str

class GetTrustStoreRevocationContentInputRequestTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    RevocationId: int

class HostHeaderConditionConfigExtraOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class HostHeaderConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class HostHeaderConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None

class HttpHeaderConditionConfigExtraOutputTypeDef(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[List[str]] = None

class HttpHeaderConditionConfigOutputTypeDef(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[List[str]] = None

class HttpHeaderConditionConfigTypeDef(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class HttpRequestMethodConditionConfigExtraOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class HttpRequestMethodConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class HttpRequestMethodConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None

class LoadBalancerStateTypeDef(BaseValidatorModel):
    Code: Optional[LoadBalancerStateEnumType] = None
    Reason: Optional[str] = None

class ModifyTrustStoreInputRequestTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None

class PathPatternConditionConfigExtraOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class PathPatternConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class PathPatternConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None

class QueryStringKeyValuePairTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class RemoveTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceArns: Sequence[str]
    TagKeys: Sequence[str]

class RemoveTrustStoreRevocationsInputRequestTypeDef(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: Sequence[int]

class SourceIpConditionConfigExtraOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class SourceIpConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None

class SourceIpConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None

class RulePriorityPairTypeDef(BaseValidatorModel):
    RuleArn: Optional[str] = None
    Priority: Optional[int] = None

class SetIpAddressTypeInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    IpAddressType: IpAddressTypeType

class SetSecurityGroupsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    SecurityGroups: Sequence[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Optional[       EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType     ] = None

class TargetHealthTypeDef(BaseValidatorModel):
    State: Optional[TargetHealthStateEnumType] = None
    Reason: Optional[TargetHealthReasonEnumType] = None
    Description: Optional[str] = None

class AddListenerCertificatesInputRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    Certificates: Sequence[CertificateTypeDef]

class RemoveListenerCertificatesInputRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    Certificates: Sequence[CertificateTypeDef]

class AddListenerCertificatesOutputTypeDef(BaseValidatorModel):
    Certificates: List[CertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeListenerCertificatesOutputTypeDef(BaseValidatorModel):
    Certificates: List[CertificateTypeDef]
    NextMarker: str
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
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceArns: Sequence[str]
    Tags: Sequence[TagTypeDef]

class CreateTrustStoreInputRequestTypeDef(BaseValidatorModel):
    Name: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagDescriptionTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class AddTrustStoreRevocationsInputRequestTypeDef(BaseValidatorModel):
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

class SslPolicyTypeDef(BaseValidatorModel):
    SslProtocols: Optional[List[str]] = None
    Ciphers: Optional[List[CipherTypeDef]] = None
    Name: Optional[str] = None
    SupportedLoadBalancerTypes: Optional[List[str]] = None

class CreateLoadBalancerInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Subnets: Optional[Sequence[str]] = None
    SubnetMappings: Optional[Sequence[SubnetMappingTypeDef]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    Scheme: Optional[LoadBalancerSchemeEnumType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Type: Optional[LoadBalancerTypeEnumType] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None

class SetSubnetsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    Subnets: Optional[Sequence[str]] = None
    SubnetMappings: Optional[Sequence[SubnetMappingTypeDef]] = None
    IpAddressType: Optional[IpAddressTypeType] = None

class CreateTargetGroupInputRequestTypeDef(BaseValidatorModel):
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

class ModifyTargetGroupInputRequestTypeDef(BaseValidatorModel):
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

class TargetGroupTypeDef(BaseValidatorModel):
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

class DeregisterTargetsInputRequestTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Sequence[TargetDescriptionTypeDef]

class DescribeTargetHealthInputRequestTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None

class RegisterTargetsInputRequestTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Sequence[TargetDescriptionTypeDef]

class DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef(BaseValidatorModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeListenersInputDescribeListenersPaginateTypeDef(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRulesInputDescribeRulesPaginateTypeDef(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountLimitsOutputTypeDef(BaseValidatorModel):
    Limits: List[LimitTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[LoadBalancerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLoadBalancerAttributesInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    Attributes: Sequence[LoadBalancerAttributeTypeDef]

class ModifyLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[LoadBalancerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTargetHealthInputTargetDeregisteredWaitTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTargetHealthInputTargetInServiceWaitTypeDef(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescriptionTypeDef]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTargetGroupAttributesOutputTypeDef(BaseValidatorModel):
    Attributes: List[TargetGroupAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTargetGroupAttributesInputRequestTypeDef(BaseValidatorModel):
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

class ForwardActionConfigExtraOutputTypeDef(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroupTupleTypeDef]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfigTypeDef] = None

class ForwardActionConfigOutputTypeDef(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroupTupleTypeDef]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfigTypeDef] = None

class ForwardActionConfigTypeDef(BaseValidatorModel):
    TargetGroups: Optional[Sequence[TargetGroupTupleTypeDef]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfigTypeDef] = None

class QueryStringConditionConfigExtraOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[QueryStringKeyValuePairTypeDef]] = None

class QueryStringConditionConfigOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[QueryStringKeyValuePairTypeDef]] = None

class QueryStringConditionConfigTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[QueryStringKeyValuePairTypeDef]] = None

class SetRulePrioritiesInputRequestTypeDef(BaseValidatorModel):
    RulePriorities: Sequence[RulePriorityPairTypeDef]

class TargetHealthDescriptionTypeDef(BaseValidatorModel):
    Target: Optional[TargetDescriptionTypeDef] = None
    HealthCheckPort: Optional[str] = None
    TargetHealth: Optional[TargetHealthTypeDef] = None
    AnomalyDetection: Optional[AnomalyDetectionTypeDef] = None

class DescribeTagsOutputTypeDef(BaseValidatorModel):
    TagDescriptions: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LoadBalancerTypeDef(BaseValidatorModel):
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

class SetSubnetsOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: List[AvailabilityZoneTypeDef]
    IpAddressType: IpAddressTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSSLPoliciesOutputTypeDef(BaseValidatorModel):
    SslPolicies: List[SslPolicyTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ActionExtraOutputTypeDef(BaseValidatorModel):
    Type: ActionTypeEnumType
    TargetGroupArn: Optional[str] = None
    AuthenticateOidcConfig: Optional[AuthenticateOidcActionConfigExtraOutputTypeDef] = None
    AuthenticateCognitoConfig: Optional[AuthenticateCognitoActionConfigExtraOutputTypeDef] = None
    Order: Optional[int] = None
    RedirectConfig: Optional[RedirectActionConfigTypeDef] = None
    FixedResponseConfig: Optional[FixedResponseActionConfigTypeDef] = None
    ForwardConfig: Optional[ForwardActionConfigExtraOutputTypeDef] = None

class ActionOutputTypeDef(BaseValidatorModel):
    Type: ActionTypeEnumType
    TargetGroupArn: Optional[str] = None
    AuthenticateOidcConfig: Optional[AuthenticateOidcActionConfigOutputTypeDef] = None
    AuthenticateCognitoConfig: Optional[AuthenticateCognitoActionConfigOutputTypeDef] = None
    Order: Optional[int] = None
    RedirectConfig: Optional[RedirectActionConfigTypeDef] = None
    FixedResponseConfig: Optional[FixedResponseActionConfigTypeDef] = None
    ForwardConfig: Optional[ForwardActionConfigOutputTypeDef] = None

class ActionTypeDef(BaseValidatorModel):
    Type: ActionTypeEnumType
    TargetGroupArn: Optional[str] = None
    AuthenticateOidcConfig: Optional[AuthenticateOidcActionConfigTypeDef] = None
    AuthenticateCognitoConfig: Optional[AuthenticateCognitoActionConfigTypeDef] = None
    Order: Optional[int] = None
    RedirectConfig: Optional[RedirectActionConfigTypeDef] = None
    FixedResponseConfig: Optional[FixedResponseActionConfigTypeDef] = None
    ForwardConfig: Optional[ForwardActionConfigTypeDef] = None

class RuleConditionExtraOutputTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[List[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigExtraOutputTypeDef] = None
    PathPatternConfig: Optional[PathPatternConditionConfigExtraOutputTypeDef] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigExtraOutputTypeDef] = None
    QueryStringConfig: Optional[QueryStringConditionConfigExtraOutputTypeDef] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigExtraOutputTypeDef] = None
    SourceIpConfig: Optional[SourceIpConditionConfigExtraOutputTypeDef] = None

class RuleConditionOutputTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[List[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigOutputTypeDef] = None
    PathPatternConfig: Optional[PathPatternConditionConfigOutputTypeDef] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigOutputTypeDef] = None
    QueryStringConfig: Optional[QueryStringConditionConfigOutputTypeDef] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigOutputTypeDef] = None
    SourceIpConfig: Optional[SourceIpConditionConfigOutputTypeDef] = None

class RuleConditionTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigTypeDef] = None
    PathPatternConfig: Optional[PathPatternConditionConfigTypeDef] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigTypeDef] = None
    QueryStringConfig: Optional[QueryStringConditionConfigTypeDef] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigTypeDef] = None
    SourceIpConfig: Optional[SourceIpConditionConfigTypeDef] = None

class DescribeTargetHealthOutputTypeDef(BaseValidatorModel):
    TargetHealthDescriptions: List[TargetHealthDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoadBalancerOutputTypeDef(BaseValidatorModel):
    LoadBalancers: List[LoadBalancerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancersOutputTypeDef(BaseValidatorModel):
    LoadBalancers: List[LoadBalancerTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTypeDef(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    LoadBalancerArn: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolEnumType] = None
    Certificates: Optional[List[CertificateTypeDef]] = None
    SslPolicy: Optional[str] = None
    DefaultActions: Optional[List[ActionOutputTypeDef]] = None
    AlpnPolicy: Optional[List[str]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributesTypeDef] = None

class RuleTypeDef(BaseValidatorModel):
    RuleArn: Optional[str] = None
    Priority: Optional[str] = None
    Conditions: Optional[List[RuleConditionOutputTypeDef]] = None
    Actions: Optional[List[ActionOutputTypeDef]] = None
    IsDefault: Optional[bool] = None

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

class CreateListenerInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerArn: str
    DefaultActions: Sequence[ActionUnionTypeDef]
    Protocol: Optional[ProtocolEnumType] = None
    Port: Optional[int] = None
    SslPolicy: Optional[str] = None
    Certificates: Optional[Sequence[CertificateTypeDef]] = None
    AlpnPolicy: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributesTypeDef] = None

class ModifyListenerInputRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    Port: Optional[int] = None
    Protocol: Optional[ProtocolEnumType] = None
    SslPolicy: Optional[str] = None
    Certificates: Optional[Sequence[CertificateTypeDef]] = None
    DefaultActions: Optional[Sequence[ActionUnionTypeDef]] = None
    AlpnPolicy: Optional[Sequence[str]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributesTypeDef] = None

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

class CreateRuleInputRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    Conditions: Sequence[RuleConditionUnionTypeDef]
    Priority: int
    Actions: Sequence[ActionUnionTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None

class ModifyRuleInputRequestTypeDef(BaseValidatorModel):
    RuleArn: str
    Conditions: Optional[Sequence[RuleConditionUnionTypeDef]] = None
    Actions: Optional[Sequence[ActionUnionTypeDef]] = None


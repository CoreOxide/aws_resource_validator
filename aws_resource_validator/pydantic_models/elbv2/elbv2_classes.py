from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.elbv2.elbv2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AuthenticateCognitoActionConfigOutput(BaseValidatorModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None
    OnUnauthenticatedRequest: Optional[AuthenticateCognitoActionConditionalBehaviorEnumType] = None


class AuthenticateOidcActionConfigOutput(BaseValidatorModel):
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


class FixedResponseActionConfig(BaseValidatorModel):
    StatusCode: str
    MessageBody: Optional[str] = None
    ContentType: Optional[str] = None


class RedirectActionConfig(BaseValidatorModel):
    StatusCode: RedirectActionStatusCodeEnumType
    Protocol: Optional[str] = None
    Port: Optional[str] = None
    Host: Optional[str] = None
    Path: Optional[str] = None
    Query: Optional[str] = None


class Certificate(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    IsDefault: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class RevocationContent(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    RevocationType: Optional[Literal['CRL']] = None


class TrustStoreRevocation(BaseValidatorModel):
    TrustStoreArn: Optional[str] = None
    RevocationId: Optional[int] = None
    RevocationType: Optional[Literal['CRL']] = None
    NumberOfRevokedEntries: Optional[int] = None


class AdministrativeOverride(BaseValidatorModel):
    State: Optional[TargetAdministrativeOverrideStateEnumType] = None
    Reason: Optional[TargetAdministrativeOverrideReasonEnumType] = None
    Description: Optional[str] = None


class AnomalyDetection(BaseValidatorModel):
    Result: Optional[AnomalyResultEnumType] = None
    MitigationInEffect: Optional[MitigationInEffectEnumType] = None


class AuthenticateCognitoActionConfig(BaseValidatorModel):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: Optional[str] = None
    Scope: Optional[str] = None
    SessionTimeout: Optional[int] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None
    OnUnauthenticatedRequest: Optional[AuthenticateCognitoActionConditionalBehaviorEnumType] = None


class AuthenticateOidcActionConfig(BaseValidatorModel):
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


class LoadBalancerAddress(BaseValidatorModel):
    IpAddress: Optional[str] = None
    AllocationId: Optional[str] = None
    PrivateIPv4Address: Optional[str] = None
    IPv6Address: Optional[str] = None


class CapacityReservationStatus(BaseValidatorModel):
    Code: Optional[CapacityReservationStateEnumType] = None
    Reason: Optional[str] = None


class Cipher(BaseValidatorModel):
    Name: Optional[str] = None
    Priority: Optional[int] = None


class MutualAuthenticationAttributes(BaseValidatorModel):
    Mode: Optional[str] = None
    TrustStoreArn: Optional[str] = None
    IgnoreClientCertificateExpiry: Optional[bool] = None
    TrustStoreAssociationStatus: Optional[TrustStoreAssociationStatusEnumType] = None
    AdvertiseTrustStoreCaNames: Optional[AdvertiseTrustStoreCaNamesEnumType] = None


class IpamPools(BaseValidatorModel):
    Ipv4IpamPoolId: Optional[str] = None


class SubnetMapping(BaseValidatorModel):
    SubnetId: Optional[str] = None
    AllocationId: Optional[str] = None
    PrivateIPv4Address: Optional[str] = None
    IPv6Address: Optional[str] = None
    SourceNatIpv6Prefix: Optional[str] = None


class Matcher(BaseValidatorModel):
    HttpCode: Optional[str] = None
    GrpcCode: Optional[str] = None


class TrustStore(BaseValidatorModel):
    Name: Optional[str] = None
    TrustStoreArn: Optional[str] = None
    Status: Optional[TrustStoreStatusType] = None
    NumberOfCaCertificates: Optional[int] = None
    TotalRevokedEntries: Optional[int] = None


class DeleteListenerInput(BaseValidatorModel):
    ListenerArn: str


class DeleteLoadBalancerInput(BaseValidatorModel):
    LoadBalancerArn: str


class DeleteRuleInput(BaseValidatorModel):
    RuleArn: str


class DeleteSharedTrustStoreAssociationInput(BaseValidatorModel):
    TrustStoreArn: str
    ResourceArn: str


class DeleteTargetGroupInput(BaseValidatorModel):
    TargetGroupArn: str


class DeleteTrustStoreInput(BaseValidatorModel):
    TrustStoreArn: str


class TargetDescription(BaseValidatorModel):
    Id: str
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_account_limits' function.
class DescribeAccountLimitsInput(BaseValidatorModel):
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class Limit(BaseValidatorModel):
    Name: Optional[str] = None
    Max: Optional[str] = None


# This class is the input for the 'describe_capacity_reservation' function.
class DescribeCapacityReservationInput(BaseValidatorModel):
    LoadBalancerArn: str


class MinimumLoadBalancerCapacity(BaseValidatorModel):
    CapacityUnits: Optional[int] = None


# This class is the input for the 'describe_listener_attributes' function.
class DescribeListenerAttributesInput(BaseValidatorModel):
    ListenerArn: str


class ListenerAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'describe_listener_certificates' function.
class DescribeListenerCertificatesInput(BaseValidatorModel):
    ListenerArn: str
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'describe_listeners' function.
class DescribeListenersInput(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'describe_load_balancer_attributes' function.
class DescribeLoadBalancerAttributesInput(BaseValidatorModel):
    LoadBalancerArn: str


class LoadBalancerAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'describe_load_balancers' function.
class DescribeLoadBalancersInput(BaseValidatorModel):
    LoadBalancerArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_rules' function.
class DescribeRulesInput(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'describe_ssl_policies' function.
class DescribeSSLPoliciesInput(BaseValidatorModel):
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsInput(BaseValidatorModel):
    ResourceArns: List[str]


# This class is the input for the 'describe_target_group_attributes' function.
class DescribeTargetGroupAttributesInput(BaseValidatorModel):
    TargetGroupArn: str


class TargetGroupAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'describe_target_groups' function.
class DescribeTargetGroupsInput(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'describe_trust_store_associations' function.
class DescribeTrustStoreAssociationsInput(BaseValidatorModel):
    TrustStoreArn: str
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class TrustStoreAssociation(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class DescribeTrustStoreRevocation(BaseValidatorModel):
    TrustStoreArn: Optional[str] = None
    RevocationId: Optional[int] = None
    RevocationType: Optional[Literal['CRL']] = None
    NumberOfRevokedEntries: Optional[int] = None


# This class is the input for the 'describe_trust_store_revocations' function.
class DescribeTrustStoreRevocationsInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: Optional[List[int]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'describe_trust_stores' function.
class DescribeTrustStoresInput(BaseValidatorModel):
    TrustStoreArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class TargetGroupStickinessConfig(BaseValidatorModel):
    Enabled: Optional[bool] = None
    DurationSeconds: Optional[int] = None


class TargetGroupTuple(BaseValidatorModel):
    TargetGroupArn: Optional[str] = None
    Weight: Optional[int] = None


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyInput(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_trust_store_ca_certificates_bundle' function.
class GetTrustStoreCaCertificatesBundleInput(BaseValidatorModel):
    TrustStoreArn: str


# This class is the input for the 'get_trust_store_revocation_content' function.
class GetTrustStoreRevocationContentInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationId: int


class HostHeaderConditionConfigOutput(BaseValidatorModel):
    Values: Optional[List[str]] = None


class HostHeaderConditionConfig(BaseValidatorModel):
    Values: Optional[List[str]] = None


class HttpHeaderConditionConfigOutput(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[List[str]] = None


class HttpHeaderConditionConfig(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[List[str]] = None


class HttpRequestMethodConditionConfigOutput(BaseValidatorModel):
    Values: Optional[List[str]] = None


class HttpRequestMethodConditionConfig(BaseValidatorModel):
    Values: Optional[List[str]] = None


class LoadBalancerState(BaseValidatorModel):
    Code: Optional[LoadBalancerStateEnumType] = None
    Reason: Optional[str] = None


# This class is the input for the 'modify_trust_store' function.
class ModifyTrustStoreInput(BaseValidatorModel):
    TrustStoreArn: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None


class PathPatternConditionConfigOutput(BaseValidatorModel):
    Values: Optional[List[str]] = None


class PathPatternConditionConfig(BaseValidatorModel):
    Values: Optional[List[str]] = None


class QueryStringKeyValuePair(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class RemoveTagsInput(BaseValidatorModel):
    ResourceArns: List[str]
    TagKeys: List[str]


class RemoveTrustStoreRevocationsInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: List[int]


class SourceIpConditionConfigOutput(BaseValidatorModel):
    Values: Optional[List[str]] = None


class RulePriorityPair(BaseValidatorModel):
    RuleArn: Optional[str] = None
    Priority: Optional[int] = None


# This class is the input for the 'set_ip_address_type' function.
class SetIpAddressTypeInput(BaseValidatorModel):
    LoadBalancerArn: str
    IpAddressType: IpAddressTypeType


# This class is the input for the 'set_security_groups' function.
class SetSecurityGroupsInput(BaseValidatorModel):
    LoadBalancerArn: str
    SecurityGroups: List[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Optional[EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType] = None


class SourceIpConditionConfig(BaseValidatorModel):
    Values: Optional[List[str]] = None


class TargetHealth(BaseValidatorModel):
    State: Optional[TargetHealthStateEnumType] = None
    Reason: Optional[TargetHealthReasonEnumType] = None
    Description: Optional[str] = None


# This class is the input for the 'add_listener_certificates' function.
class AddListenerCertificatesInput(BaseValidatorModel):
    ListenerArn: str
    Certificates: List[Certificate]


class RemoveListenerCertificatesInput(BaseValidatorModel):
    ListenerArn: str
    Certificates: List[Certificate]


# This class is the output for the 'add_listener_certificates' function.
class AddListenerCertificatesOutput(BaseValidatorModel):
    Certificates: List[Certificate]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_listener_certificates' function.
class DescribeListenerCertificatesOutput(BaseValidatorModel):
    Certificates: List[Certificate]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_trust_store_ca_certificates_bundle' function.
class GetTrustStoreCaCertificatesBundleOutput(BaseValidatorModel):
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_trust_store_revocation_content' function.
class GetTrustStoreRevocationContentOutput(BaseValidatorModel):
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_ip_address_type' function.
class SetIpAddressTypeOutput(BaseValidatorModel):
    IpAddressType: IpAddressTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_security_groups' function.
class SetSecurityGroupsOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType
    ResponseMetadata: ResponseMetadata


class AddTagsInput(BaseValidatorModel):
    ResourceArns: List[str]
    Tags: List[Tag]


# This class is the input for the 'create_trust_store' function.
class CreateTrustStoreInput(BaseValidatorModel):
    Name: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagDescription(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'add_trust_store_revocations' function.
class AddTrustStoreRevocationsInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationContents: Optional[List[RevocationContent]] = None


# This class is the output for the 'add_trust_store_revocations' function.
class AddTrustStoreRevocationsOutput(BaseValidatorModel):
    TrustStoreRevocations: List[TrustStoreRevocation]
    ResponseMetadata: ResponseMetadata

AuthenticateCognitoActionConfigUnion = Union[AuthenticateCognitoActionConfig, AuthenticateCognitoActionConfigOutput]

AuthenticateOidcActionConfigUnion = Union[AuthenticateOidcActionConfig, AuthenticateOidcActionConfigOutput]


class AvailabilityZone(BaseValidatorModel):
    ZoneName: Optional[str] = None
    SubnetId: Optional[str] = None
    OutpostId: Optional[str] = None
    LoadBalancerAddresses: Optional[List[LoadBalancerAddress]] = None
    SourceNatIpv6Prefixes: Optional[List[str]] = None


class ZonalCapacityReservationState(BaseValidatorModel):
    State: Optional[CapacityReservationStatus] = None
    AvailabilityZone: Optional[str] = None
    EffectiveCapacityUnits: Optional[float] = None


class SslPolicy(BaseValidatorModel):
    SslProtocols: Optional[List[str]] = None
    Ciphers: Optional[List[Cipher]] = None
    Name: Optional[str] = None
    SupportedLoadBalancerTypes: Optional[List[str]] = None


# This class is the input for the 'modify_ip_pools' function.
class ModifyIpPoolsInput(BaseValidatorModel):
    LoadBalancerArn: str
    IpamPools: Optional[IpamPools] = None
    RemoveIpamPools: Optional[List[Literal['ipv4']]] = None


# This class is the output for the 'modify_ip_pools' function.
class ModifyIpPoolsOutput(BaseValidatorModel):
    IpamPools: IpamPools
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_load_balancer' function.
class CreateLoadBalancerInput(BaseValidatorModel):
    Name: str
    Subnets: Optional[List[str]] = None
    SubnetMappings: Optional[List[SubnetMapping]] = None
    SecurityGroups: Optional[List[str]] = None
    Scheme: Optional[LoadBalancerSchemeEnumType] = None
    Tags: Optional[List[Tag]] = None
    Type: Optional[LoadBalancerTypeEnumType] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    EnablePrefixForIpv6SourceNat: Optional[EnablePrefixForIpv6SourceNatEnumType] = None
    IpamPools: Optional[IpamPools] = None


# This class is the input for the 'set_subnets' function.
class SetSubnetsInput(BaseValidatorModel):
    LoadBalancerArn: str
    Subnets: Optional[List[str]] = None
    SubnetMappings: Optional[List[SubnetMapping]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    EnablePrefixForIpv6SourceNat: Optional[EnablePrefixForIpv6SourceNatEnumType] = None


# This class is the input for the 'create_target_group' function.
class CreateTargetGroupInput(BaseValidatorModel):
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
    Matcher: Optional[Matcher] = None
    TargetType: Optional[TargetTypeEnumType] = None
    Tags: Optional[List[Tag]] = None
    IpAddressType: Optional[TargetGroupIpAddressTypeEnumType] = None


# This class is the input for the 'modify_target_group' function.
class ModifyTargetGroupInput(BaseValidatorModel):
    TargetGroupArn: str
    HealthCheckProtocol: Optional[ProtocolEnumType] = None
    HealthCheckPort: Optional[str] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckEnabled: Optional[bool] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    HealthCheckTimeoutSeconds: Optional[int] = None
    HealthyThresholdCount: Optional[int] = None
    UnhealthyThresholdCount: Optional[int] = None
    Matcher: Optional[Matcher] = None


class TargetGroup(BaseValidatorModel):
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
    Matcher: Optional[Matcher] = None
    LoadBalancerArns: Optional[List[str]] = None
    TargetType: Optional[TargetTypeEnumType] = None
    ProtocolVersion: Optional[str] = None
    IpAddressType: Optional[TargetGroupIpAddressTypeEnumType] = None


# This class is the output for the 'create_trust_store' function.
class CreateTrustStoreOutput(BaseValidatorModel):
    TrustStores: List[TrustStore]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_trust_stores' function.
class DescribeTrustStoresOutput(BaseValidatorModel):
    TrustStores: List[TrustStore]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_trust_store' function.
class ModifyTrustStoreOutput(BaseValidatorModel):
    TrustStores: List[TrustStore]
    ResponseMetadata: ResponseMetadata


class DeregisterTargetsInput(BaseValidatorModel):
    TargetGroupArn: str
    Targets: List[TargetDescription]


# This class is the input for the 'describe_target_health' function.
class DescribeTargetHealthInput(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[List[TargetDescription]] = None
    Include: Optional[List[DescribeTargetHealthInputIncludeEnumType]] = None


class RegisterTargetsInput(BaseValidatorModel):
    TargetGroupArn: str
    Targets: List[TargetDescription]


class DescribeAccountLimitsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeListenerCertificatesInputPaginate(BaseValidatorModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeListenersInputPaginate(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLoadBalancersInputPaginate(BaseValidatorModel):
    LoadBalancerArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRulesInputPaginate(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSSLPoliciesInputPaginate(BaseValidatorModel):
    Names: Optional[List[str]] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTargetGroupsInputPaginate(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_account_limits' function.
class DescribeAccountLimitsOutput(BaseValidatorModel):
    Limits: List[Limit]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'modify_capacity_reservation' function.
class ModifyCapacityReservationInput(BaseValidatorModel):
    LoadBalancerArn: str
    MinimumLoadBalancerCapacity: Optional[MinimumLoadBalancerCapacity] = None
    ResetCapacityReservation: Optional[bool] = None


# This class is the output for the 'describe_listener_attributes' function.
class DescribeListenerAttributesOutput(BaseValidatorModel):
    Attributes: List[ListenerAttribute]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'modify_listener_attributes' function.
class ModifyListenerAttributesInput(BaseValidatorModel):
    ListenerArn: str
    Attributes: List[ListenerAttribute]


# This class is the output for the 'modify_listener_attributes' function.
class ModifyListenerAttributesOutput(BaseValidatorModel):
    Attributes: List[ListenerAttribute]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_load_balancer_attributes' function.
class DescribeLoadBalancerAttributesOutput(BaseValidatorModel):
    Attributes: List[LoadBalancerAttribute]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'modify_load_balancer_attributes' function.
class ModifyLoadBalancerAttributesInput(BaseValidatorModel):
    LoadBalancerArn: str
    Attributes: List[LoadBalancerAttribute]


# This class is the output for the 'modify_load_balancer_attributes' function.
class ModifyLoadBalancerAttributesOutput(BaseValidatorModel):
    Attributes: List[LoadBalancerAttribute]
    ResponseMetadata: ResponseMetadata


class DescribeLoadBalancersInputWaitExtraExtra(BaseValidatorModel):
    LoadBalancerArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeLoadBalancersInputWaitExtra(BaseValidatorModel):
    LoadBalancerArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeLoadBalancersInputWait(BaseValidatorModel):
    LoadBalancerArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTargetHealthInputWaitExtra(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[List[TargetDescription]] = None
    Include: Optional[List[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTargetHealthInputWait(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[List[TargetDescription]] = None
    Include: Optional[List[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'describe_target_group_attributes' function.
class DescribeTargetGroupAttributesOutput(BaseValidatorModel):
    Attributes: List[TargetGroupAttribute]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'modify_target_group_attributes' function.
class ModifyTargetGroupAttributesInput(BaseValidatorModel):
    TargetGroupArn: str
    Attributes: List[TargetGroupAttribute]


# This class is the output for the 'modify_target_group_attributes' function.
class ModifyTargetGroupAttributesOutput(BaseValidatorModel):
    Attributes: List[TargetGroupAttribute]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_trust_store_associations' function.
class DescribeTrustStoreAssociationsOutput(BaseValidatorModel):
    TrustStoreAssociations: List[TrustStoreAssociation]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_trust_store_revocations' function.
class DescribeTrustStoreRevocationsOutput(BaseValidatorModel):
    TrustStoreRevocations: List[DescribeTrustStoreRevocation]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ForwardActionConfigOutput(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroupTuple]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfig] = None


class ForwardActionConfig(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroupTuple]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfig] = None

HostHeaderConditionConfigUnion = Union[HostHeaderConditionConfig, HostHeaderConditionConfigOutput]

HttpHeaderConditionConfigUnion = Union[HttpHeaderConditionConfig, HttpHeaderConditionConfigOutput]

HttpRequestMethodConditionConfigUnion = Union[HttpRequestMethodConditionConfig, HttpRequestMethodConditionConfigOutput]

PathPatternConditionConfigUnion = Union[PathPatternConditionConfig, PathPatternConditionConfigOutput]


class QueryStringConditionConfigOutput(BaseValidatorModel):
    Values: Optional[List[QueryStringKeyValuePair]] = None


class QueryStringConditionConfig(BaseValidatorModel):
    Values: Optional[List[QueryStringKeyValuePair]] = None


# This class is the input for the 'set_rule_priorities' function.
class SetRulePrioritiesInput(BaseValidatorModel):
    RulePriorities: List[RulePriorityPair]

SourceIpConditionConfigUnion = Union[SourceIpConditionConfig, SourceIpConditionConfigOutput]


class TargetHealthDescription(BaseValidatorModel):
    Target: Optional[TargetDescription] = None
    HealthCheckPort: Optional[str] = None
    TargetHealth: Optional[TargetHealth] = None
    AnomalyDetection: Optional[AnomalyDetection] = None
    AdministrativeOverride: Optional[AdministrativeOverride] = None


# This class is the output for the 'describe_tags' function.
class DescribeTagsOutput(BaseValidatorModel):
    TagDescriptions: List[TagDescription]
    ResponseMetadata: ResponseMetadata


class LoadBalancer(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    DNSName: Optional[str] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LoadBalancerName: Optional[str] = None
    Scheme: Optional[LoadBalancerSchemeEnumType] = None
    VpcId: Optional[str] = None
    State: Optional[LoadBalancerState] = None
    Type: Optional[LoadBalancerTypeEnumType] = None
    AvailabilityZones: Optional[List[AvailabilityZone]] = None
    SecurityGroups: Optional[List[str]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Optional[str] = None
    EnablePrefixForIpv6SourceNat: Optional[EnablePrefixForIpv6SourceNatEnumType] = None
    IpamPools: Optional[IpamPools] = None


# This class is the output for the 'set_subnets' function.
class SetSubnetsOutput(BaseValidatorModel):
    AvailabilityZones: List[AvailabilityZone]
    IpAddressType: IpAddressTypeType
    EnablePrefixForIpv6SourceNat: EnablePrefixForIpv6SourceNatEnumType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_capacity_reservation' function.
class DescribeCapacityReservationOutput(BaseValidatorModel):
    LastModifiedTime: datetime
    DecreaseRequestsRemaining: int
    MinimumLoadBalancerCapacity: MinimumLoadBalancerCapacity
    CapacityReservationState: List[ZonalCapacityReservationState]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_capacity_reservation' function.
class ModifyCapacityReservationOutput(BaseValidatorModel):
    LastModifiedTime: datetime
    DecreaseRequestsRemaining: int
    MinimumLoadBalancerCapacity: MinimumLoadBalancerCapacity
    CapacityReservationState: List[ZonalCapacityReservationState]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ssl_policies' function.
class DescribeSSLPoliciesOutput(BaseValidatorModel):
    SslPolicies: List[SslPolicy]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_target_group' function.
class CreateTargetGroupOutput(BaseValidatorModel):
    TargetGroups: List[TargetGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_target_groups' function.
class DescribeTargetGroupsOutput(BaseValidatorModel):
    TargetGroups: List[TargetGroup]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_target_group' function.
class ModifyTargetGroupOutput(BaseValidatorModel):
    TargetGroups: List[TargetGroup]
    ResponseMetadata: ResponseMetadata


class ActionOutput(BaseValidatorModel):
    Type: ActionTypeEnumType
    TargetGroupArn: Optional[str] = None
    AuthenticateOidcConfig: Optional[AuthenticateOidcActionConfigOutput] = None
    AuthenticateCognitoConfig: Optional[AuthenticateCognitoActionConfigOutput] = None
    Order: Optional[int] = None
    RedirectConfig: Optional[RedirectActionConfig] = None
    FixedResponseConfig: Optional[FixedResponseActionConfig] = None
    ForwardConfig: Optional[ForwardActionConfigOutput] = None

ForwardActionConfigUnion = Union[ForwardActionConfig, ForwardActionConfigOutput]


class RuleConditionOutput(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[List[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigOutput] = None
    PathPatternConfig: Optional[PathPatternConditionConfigOutput] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigOutput] = None
    QueryStringConfig: Optional[QueryStringConditionConfigOutput] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigOutput] = None
    SourceIpConfig: Optional[SourceIpConditionConfigOutput] = None

QueryStringConditionConfigUnion = Union[QueryStringConditionConfig, QueryStringConditionConfigOutput]


# This class is the output for the 'describe_target_health' function.
class DescribeTargetHealthOutput(BaseValidatorModel):
    TargetHealthDescriptions: List[TargetHealthDescription]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_load_balancer' function.
class CreateLoadBalancerOutput(BaseValidatorModel):
    LoadBalancers: List[LoadBalancer]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_load_balancers' function.
class DescribeLoadBalancersOutput(BaseValidatorModel):
    LoadBalancers: List[LoadBalancer]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class Listener(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    LoadBalancerArn: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolEnumType] = None
    Certificates: Optional[List[Certificate]] = None
    SslPolicy: Optional[str] = None
    DefaultActions: Optional[List[ActionOutput]] = None
    AlpnPolicy: Optional[List[str]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributes] = None


class Action(BaseValidatorModel):
    Type: ActionTypeEnumType
    TargetGroupArn: Optional[str] = None
    AuthenticateOidcConfig: Optional[AuthenticateOidcActionConfigUnion] = None
    AuthenticateCognitoConfig: Optional[AuthenticateCognitoActionConfigUnion] = None
    Order: Optional[int] = None
    RedirectConfig: Optional[RedirectActionConfig] = None
    FixedResponseConfig: Optional[FixedResponseActionConfig] = None
    ForwardConfig: Optional[ForwardActionConfigUnion] = None


class Rule(BaseValidatorModel):
    RuleArn: Optional[str] = None
    Priority: Optional[str] = None
    Conditions: Optional[List[RuleConditionOutput]] = None
    Actions: Optional[List[ActionOutput]] = None
    IsDefault: Optional[bool] = None


class RuleCondition(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[List[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigUnion] = None
    PathPatternConfig: Optional[PathPatternConditionConfigUnion] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigUnion] = None
    QueryStringConfig: Optional[QueryStringConditionConfigUnion] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigUnion] = None
    SourceIpConfig: Optional[SourceIpConditionConfigUnion] = None


# This class is the output for the 'create_listener' function.
class CreateListenerOutput(BaseValidatorModel):
    Listeners: List[Listener]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_listeners' function.
class DescribeListenersOutput(BaseValidatorModel):
    Listeners: List[Listener]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_listener' function.
class ModifyListenerOutput(BaseValidatorModel):
    Listeners: List[Listener]
    ResponseMetadata: ResponseMetadata

ActionUnion = Union[Action, ActionOutput]


# This class is the output for the 'create_rule' function.
class CreateRuleOutput(BaseValidatorModel):
    Rules: List[Rule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_rules' function.
class DescribeRulesOutput(BaseValidatorModel):
    Rules: List[Rule]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_rule' function.
class ModifyRuleOutput(BaseValidatorModel):
    Rules: List[Rule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_rule_priorities' function.
class SetRulePrioritiesOutput(BaseValidatorModel):
    Rules: List[Rule]
    ResponseMetadata: ResponseMetadata

RuleConditionUnion = Union[RuleCondition, RuleConditionOutput]


# This class is the input for the 'create_listener' function.
class CreateListenerInput(BaseValidatorModel):
    LoadBalancerArn: str
    DefaultActions: List[ActionUnion]
    Protocol: Optional[ProtocolEnumType] = None
    Port: Optional[int] = None
    SslPolicy: Optional[str] = None
    Certificates: Optional[List[Certificate]] = None
    AlpnPolicy: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributes] = None


# This class is the input for the 'modify_listener' function.
class ModifyListenerInput(BaseValidatorModel):
    ListenerArn: str
    Port: Optional[int] = None
    Protocol: Optional[ProtocolEnumType] = None
    SslPolicy: Optional[str] = None
    Certificates: Optional[List[Certificate]] = None
    DefaultActions: Optional[List[ActionUnion]] = None
    AlpnPolicy: Optional[List[str]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributes] = None


# This class is the input for the 'create_rule' function.
class CreateRuleInput(BaseValidatorModel):
    ListenerArn: str
    Conditions: List[RuleConditionUnion]
    Priority: int
    Actions: List[ActionUnion]
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'modify_rule' function.
class ModifyRuleInput(BaseValidatorModel):
    RuleArn: str
    Conditions: Optional[List[RuleConditionUnion]] = None
    Actions: Optional[List[ActionUnion]] = None
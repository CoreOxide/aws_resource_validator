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


class DescribeAccountLimitsInput(BaseValidatorModel):
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class Limit(BaseValidatorModel):
    Name: Optional[str] = None
    Max: Optional[str] = None


class DescribeCapacityReservationInput(BaseValidatorModel):
    LoadBalancerArn: str


class MinimumLoadBalancerCapacity(BaseValidatorModel):
    CapacityUnits: Optional[int] = None


class DescribeListenerAttributesInput(BaseValidatorModel):
    ListenerArn: str


class ListenerAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeListenerCertificatesInput(BaseValidatorModel):
    ListenerArn: str
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeListenersInput(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeLoadBalancerAttributesInput(BaseValidatorModel):
    LoadBalancerArn: str


class LoadBalancerAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeLoadBalancersInput(BaseValidatorModel):
    LoadBalancerArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeRulesInput(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeSSLPoliciesInput(BaseValidatorModel):
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None


class DescribeTagsInput(BaseValidatorModel):
    ResourceArns: List[str]


class DescribeTargetGroupAttributesInput(BaseValidatorModel):
    TargetGroupArn: str


class TargetGroupAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeTargetGroupsInput(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[List[str]] = None
    Names: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


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


class DescribeTrustStoreRevocationsInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: Optional[List[int]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


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


class GetResourcePolicyInput(BaseValidatorModel):
    ResourceArn: str


class GetTrustStoreCaCertificatesBundleInput(BaseValidatorModel):
    TrustStoreArn: str


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


class SetIpAddressTypeInput(BaseValidatorModel):
    LoadBalancerArn: str
    IpAddressType: IpAddressTypeType


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


class AddListenerCertificatesInput(BaseValidatorModel):
    ListenerArn: str
    Certificates: List[Certificate]


class RemoveListenerCertificatesInput(BaseValidatorModel):
    ListenerArn: str
    Certificates: List[Certificate]


class AddListenerCertificatesOutput(BaseValidatorModel):
    Certificates: List[Certificate]
    ResponseMetadata: ResponseMetadata


class DescribeListenerCertificatesOutput(BaseValidatorModel):
    Certificates: List[Certificate]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetTrustStoreCaCertificatesBundleOutput(BaseValidatorModel):
    Location: str
    ResponseMetadata: ResponseMetadata


class GetTrustStoreRevocationContentOutput(BaseValidatorModel):
    Location: str
    ResponseMetadata: ResponseMetadata


class SetIpAddressTypeOutput(BaseValidatorModel):
    IpAddressType: IpAddressTypeType
    ResponseMetadata: ResponseMetadata


class SetSecurityGroupsOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType
    ResponseMetadata: ResponseMetadata


class AddTagsInput(BaseValidatorModel):
    ResourceArns: List[str]
    Tags: List[Tag]


class CreateTrustStoreInput(BaseValidatorModel):
    Name: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagDescription(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class AddTrustStoreRevocationsInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationContents: Optional[List[RevocationContent]] = None


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


class ModifyIpPoolsInput(BaseValidatorModel):
    LoadBalancerArn: str
    IpamPools: Optional[IpamPools] = None
    RemoveIpamPools: Optional[List[Literal['ipv4']]] = None


class ModifyIpPoolsOutput(BaseValidatorModel):
    IpamPools: IpamPools
    ResponseMetadata: ResponseMetadata


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


class SetSubnetsInput(BaseValidatorModel):
    LoadBalancerArn: str
    Subnets: Optional[List[str]] = None
    SubnetMappings: Optional[List[SubnetMapping]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    EnablePrefixForIpv6SourceNat: Optional[EnablePrefixForIpv6SourceNatEnumType] = None


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


class CreateTrustStoreOutput(BaseValidatorModel):
    TrustStores: List[TrustStore]
    ResponseMetadata: ResponseMetadata


class DescribeTrustStoresOutput(BaseValidatorModel):
    TrustStores: List[TrustStore]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ModifyTrustStoreOutput(BaseValidatorModel):
    TrustStores: List[TrustStore]
    ResponseMetadata: ResponseMetadata


class DeregisterTargetsInput(BaseValidatorModel):
    TargetGroupArn: str
    Targets: List[TargetDescription]


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


class DescribeAccountLimitsOutput(BaseValidatorModel):
    Limits: List[Limit]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ModifyCapacityReservationInput(BaseValidatorModel):
    LoadBalancerArn: str
    MinimumLoadBalancerCapacity: Optional[MinimumLoadBalancerCapacity] = None
    ResetCapacityReservation: Optional[bool] = None


class DescribeListenerAttributesOutput(BaseValidatorModel):
    Attributes: List[ListenerAttribute]
    ResponseMetadata: ResponseMetadata


class ModifyListenerAttributesInput(BaseValidatorModel):
    ListenerArn: str
    Attributes: List[ListenerAttribute]


class ModifyListenerAttributesOutput(BaseValidatorModel):
    Attributes: List[ListenerAttribute]
    ResponseMetadata: ResponseMetadata


class DescribeLoadBalancerAttributesOutput(BaseValidatorModel):
    Attributes: List[LoadBalancerAttribute]
    ResponseMetadata: ResponseMetadata


class ModifyLoadBalancerAttributesInput(BaseValidatorModel):
    LoadBalancerArn: str
    Attributes: List[LoadBalancerAttribute]


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


class DescribeTargetGroupAttributesOutput(BaseValidatorModel):
    Attributes: List[TargetGroupAttribute]
    ResponseMetadata: ResponseMetadata


class ModifyTargetGroupAttributesInput(BaseValidatorModel):
    TargetGroupArn: str
    Attributes: List[TargetGroupAttribute]


class ModifyTargetGroupAttributesOutput(BaseValidatorModel):
    Attributes: List[TargetGroupAttribute]
    ResponseMetadata: ResponseMetadata


class DescribeTrustStoreAssociationsOutput(BaseValidatorModel):
    TrustStoreAssociations: List[TrustStoreAssociation]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


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


class SetRulePrioritiesInput(BaseValidatorModel):
    RulePriorities: List[RulePriorityPair]

SourceIpConditionConfigUnion = Union[SourceIpConditionConfig, SourceIpConditionConfigOutput]


class TargetHealthDescription(BaseValidatorModel):
    Target: Optional[TargetDescription] = None
    HealthCheckPort: Optional[str] = None
    TargetHealth: Optional[TargetHealth] = None
    AnomalyDetection: Optional[AnomalyDetection] = None
    AdministrativeOverride: Optional[AdministrativeOverride] = None


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


class SetSubnetsOutput(BaseValidatorModel):
    AvailabilityZones: List[AvailabilityZone]
    IpAddressType: IpAddressTypeType
    EnablePrefixForIpv6SourceNat: EnablePrefixForIpv6SourceNatEnumType
    ResponseMetadata: ResponseMetadata


class DescribeCapacityReservationOutput(BaseValidatorModel):
    LastModifiedTime: datetime
    DecreaseRequestsRemaining: int
    MinimumLoadBalancerCapacity: MinimumLoadBalancerCapacity
    CapacityReservationState: List[ZonalCapacityReservationState]
    ResponseMetadata: ResponseMetadata


class ModifyCapacityReservationOutput(BaseValidatorModel):
    LastModifiedTime: datetime
    DecreaseRequestsRemaining: int
    MinimumLoadBalancerCapacity: MinimumLoadBalancerCapacity
    CapacityReservationState: List[ZonalCapacityReservationState]
    ResponseMetadata: ResponseMetadata


class DescribeSSLPoliciesOutput(BaseValidatorModel):
    SslPolicies: List[SslPolicy]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class CreateTargetGroupOutput(BaseValidatorModel):
    TargetGroups: List[TargetGroup]
    ResponseMetadata: ResponseMetadata


class DescribeTargetGroupsOutput(BaseValidatorModel):
    TargetGroups: List[TargetGroup]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


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


class DescribeTargetHealthOutput(BaseValidatorModel):
    TargetHealthDescriptions: List[TargetHealthDescription]
    ResponseMetadata: ResponseMetadata


class CreateLoadBalancerOutput(BaseValidatorModel):
    LoadBalancers: List[LoadBalancer]
    ResponseMetadata: ResponseMetadata


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


class CreateListenerOutput(BaseValidatorModel):
    Listeners: List[Listener]
    ResponseMetadata: ResponseMetadata


class DescribeListenersOutput(BaseValidatorModel):
    Listeners: List[Listener]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ModifyListenerOutput(BaseValidatorModel):
    Listeners: List[Listener]
    ResponseMetadata: ResponseMetadata

ActionUnion = Union[Action, ActionOutput]


class CreateRuleOutput(BaseValidatorModel):
    Rules: List[Rule]
    ResponseMetadata: ResponseMetadata


class DescribeRulesOutput(BaseValidatorModel):
    Rules: List[Rule]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ModifyRuleOutput(BaseValidatorModel):
    Rules: List[Rule]
    ResponseMetadata: ResponseMetadata


class SetRulePrioritiesOutput(BaseValidatorModel):
    Rules: List[Rule]
    ResponseMetadata: ResponseMetadata

RuleConditionUnion = Union[RuleCondition, RuleConditionOutput]


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


class ModifyListenerInput(BaseValidatorModel):
    ListenerArn: str
    Port: Optional[int] = None
    Protocol: Optional[ProtocolEnumType] = None
    SslPolicy: Optional[str] = None
    Certificates: Optional[List[Certificate]] = None
    DefaultActions: Optional[List[ActionUnion]] = None
    AlpnPolicy: Optional[List[str]] = None
    MutualAuthentication: Optional[MutualAuthenticationAttributes] = None


class CreateRuleInput(BaseValidatorModel):
    ListenerArn: str
    Conditions: List[RuleConditionUnion]
    Priority: int
    Actions: List[ActionUnion]
    Tags: Optional[List[Tag]] = None


class ModifyRuleInput(BaseValidatorModel):
    RuleArn: str
    Conditions: Optional[List[RuleConditionUnion]] = None
    Actions: Optional[List[ActionUnion]] = None
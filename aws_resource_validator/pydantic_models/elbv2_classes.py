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
    RevocationType: Optional[Literal["CRL"]] = None


class TrustStoreRevocation(BaseValidatorModel):
    TrustStoreArn: Optional[str] = None
    RevocationId: Optional[int] = None
    RevocationType: Optional[Literal["CRL"]] = None
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
    AuthenticationRequestExtraParams: Optional[Mapping[str, str]] = None
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
    AuthenticationRequestExtraParams: Optional[Mapping[str, str]] = None
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
    ListenerArns: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeLoadBalancerAttributesInput(BaseValidatorModel):
    LoadBalancerArn: str


class LoadBalancerAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeLoadBalancersInput(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeRulesInput(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeSSLPoliciesInput(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None


class DescribeTagsInput(BaseValidatorModel):
    ResourceArns: Sequence[str]


class DescribeTargetGroupAttributesInput(BaseValidatorModel):
    TargetGroupArn: str


class TargetGroupAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DescribeTargetGroupsInput(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
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
    RevocationType: Optional[Literal["CRL"]] = None
    NumberOfRevokedEntries: Optional[int] = None


class DescribeTrustStoreRevocationsInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: Optional[Sequence[int]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeTrustStoresInput(BaseValidatorModel):
    TrustStoreArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
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
    Values: Optional[Sequence[str]] = None


class HttpHeaderConditionConfigOutput(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[List[str]] = None


class HttpHeaderConditionConfig(BaseValidatorModel):
    HttpHeaderName: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class HttpRequestMethodConditionConfigOutput(BaseValidatorModel):
    Values: Optional[List[str]] = None


class HttpRequestMethodConditionConfig(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None


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
    Values: Optional[Sequence[str]] = None


class QueryStringKeyValuePair(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class RemoveTagsInput(BaseValidatorModel):
    ResourceArns: Sequence[str]
    TagKeys: Sequence[str]


class RemoveTrustStoreRevocationsInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationIds: Sequence[int]


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
    SecurityGroups: Sequence[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Optional[ EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType ] = None


class SourceIpConditionConfig(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None


class TargetHealth(BaseValidatorModel):
    State: Optional[TargetHealthStateEnumType] = None
    Reason: Optional[TargetHealthReasonEnumType] = None
    Description: Optional[str] = None


class AddListenerCertificatesInput(BaseValidatorModel):
    ListenerArn: str
    Certificates: Sequence[Certificate]


class RemoveListenerCertificatesInput(BaseValidatorModel):
    ListenerArn: str
    Certificates: Sequence[Certificate]


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
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: ( EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType )
    ResponseMetadata: ResponseMetadata


class AddTagsInput(BaseValidatorModel):
    ResourceArns: Sequence[str]
    Tags: Sequence[Tag]


class CreateTrustStoreInput(BaseValidatorModel):
    Name: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class TagDescription(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class AddTrustStoreRevocationsInput(BaseValidatorModel):
    TrustStoreArn: str
    RevocationContents: Optional[Sequence[RevocationContent]] = None


class AddTrustStoreRevocationsOutput(BaseValidatorModel):
    TrustStoreRevocations: List[TrustStoreRevocation]
    ResponseMetadata: ResponseMetadata


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
    RemoveIpamPools: Optional[Sequence[Literal["ipv4"]]] = None


class ModifyIpPoolsOutput(BaseValidatorModel):
    IpamPools: IpamPools
    ResponseMetadata: ResponseMetadata


class SetSubnetsInput(BaseValidatorModel):
    LoadBalancerArn: str
    Subnets: Optional[Sequence[str]] = None
    SubnetMappings: Optional[Sequence[SubnetMapping]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    EnablePrefixForIpv6SourceNat: Optional[EnablePrefixForIpv6SourceNatEnumType] = None


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
    Targets: Sequence[TargetDescription]


class DescribeTargetHealthInput(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescription]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None


class RegisterTargetsInput(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Sequence[TargetDescription]


class DescribeAccountLimitsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeListenerCertificatesInputPaginate(BaseValidatorModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeListenersInputPaginate(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    ListenerArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLoadBalancersInputPaginate(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRulesInputPaginate(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    RuleArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSSLPoliciesInputPaginate(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    LoadBalancerType: Optional[LoadBalancerTypeEnumType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTargetGroupsInputPaginate(BaseValidatorModel):
    LoadBalancerArn: Optional[str] = None
    TargetGroupArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
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
    Attributes: Sequence[ListenerAttribute]


class ModifyListenerAttributesOutput(BaseValidatorModel):
    Attributes: List[ListenerAttribute]
    ResponseMetadata: ResponseMetadata


class DescribeLoadBalancerAttributesOutput(BaseValidatorModel):
    Attributes: List[LoadBalancerAttribute]
    ResponseMetadata: ResponseMetadata


class ModifyLoadBalancerAttributesInput(BaseValidatorModel):
    LoadBalancerArn: str
    Attributes: Sequence[LoadBalancerAttribute]


class ModifyLoadBalancerAttributesOutput(BaseValidatorModel):
    Attributes: List[LoadBalancerAttribute]
    ResponseMetadata: ResponseMetadata


class DescribeLoadBalancersInputWaitExtraExtra(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeLoadBalancersInputWaitExtra(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeLoadBalancersInputWait(BaseValidatorModel):
    LoadBalancerArns: Optional[Sequence[str]] = None
    Names: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTargetHealthInputWaitExtra(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescription]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTargetHealthInputWait(BaseValidatorModel):
    TargetGroupArn: str
    Targets: Optional[Sequence[TargetDescription]] = None
    Include: Optional[Sequence[DescribeTargetHealthInputIncludeEnumType]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTargetGroupAttributesOutput(BaseValidatorModel):
    Attributes: List[TargetGroupAttribute]
    ResponseMetadata: ResponseMetadata


class ModifyTargetGroupAttributesInput(BaseValidatorModel):
    TargetGroupArn: str
    Attributes: Sequence[TargetGroupAttribute]


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
    TargetGroups: Optional[Sequence[TargetGroupTuple]] = None
    TargetGroupStickinessConfig: Optional[TargetGroupStickinessConfig] = None


class QueryStringConditionConfigOutput(BaseValidatorModel):
    Values: Optional[List[QueryStringKeyValuePair]] = None


class QueryStringConditionConfig(BaseValidatorModel):
    Values: Optional[Sequence[QueryStringKeyValuePair]] = None


class SetRulePrioritiesInput(BaseValidatorModel):
    RulePriorities: Sequence[RulePriorityPair]


class TargetHealthDescription(BaseValidatorModel):
    Target: Optional[TargetDescription] = None
    HealthCheckPort: Optional[str] = None
    TargetHealth: Optional[TargetHealth] = None
    AnomalyDetection: Optional[AnomalyDetection] = None
    AdministrativeOverride: Optional[AdministrativeOverride] = None


class DescribeTagsOutput(BaseValidatorModel):
    TagDescriptions: List[TagDescription]
    ResponseMetadata: ResponseMetadata


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


class TargetGroup(BaseValidatorModel):
    pass


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


class RuleConditionOutput(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[List[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigOutput] = None
    PathPatternConfig: Optional[PathPatternConditionConfigOutput] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigOutput] = None
    QueryStringConfig: Optional[QueryStringConditionConfigOutput] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigOutput] = None
    SourceIpConfig: Optional[SourceIpConditionConfigOutput] = None


class DescribeTargetHealthOutput(BaseValidatorModel):
    TargetHealthDescriptions: List[TargetHealthDescription]
    ResponseMetadata: ResponseMetadata


class LoadBalancer(BaseValidatorModel):
    pass


class CreateLoadBalancerOutput(BaseValidatorModel):
    LoadBalancers: List[LoadBalancer]
    ResponseMetadata: ResponseMetadata


class DescribeLoadBalancersOutput(BaseValidatorModel):
    LoadBalancers: List[LoadBalancer]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ActionOutput(BaseValidatorModel):
    pass


class Rule(BaseValidatorModel):
    RuleArn: Optional[str] = None
    Priority: Optional[str] = None
    Conditions: Optional[List[RuleConditionOutput]] = None
    Actions: Optional[List[ActionOutput]] = None
    IsDefault: Optional[bool] = None


class HostHeaderConditionConfigUnion(BaseValidatorModel):
    pass


class QueryStringConditionConfigUnion(BaseValidatorModel):
    pass


class HttpHeaderConditionConfigUnion(BaseValidatorModel):
    pass


class PathPatternConditionConfigUnion(BaseValidatorModel):
    pass


class SourceIpConditionConfigUnion(BaseValidatorModel):
    pass


class HttpRequestMethodConditionConfigUnion(BaseValidatorModel):
    pass


class RuleCondition(BaseValidatorModel):
    Field: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    HostHeaderConfig: Optional[HostHeaderConditionConfigUnion] = None
    PathPatternConfig: Optional[PathPatternConditionConfigUnion] = None
    HttpHeaderConfig: Optional[HttpHeaderConditionConfigUnion] = None
    QueryStringConfig: Optional[QueryStringConditionConfigUnion] = None
    HttpRequestMethodConfig: Optional[HttpRequestMethodConditionConfigUnion] = None
    SourceIpConfig: Optional[SourceIpConditionConfigUnion] = None


class Listener(BaseValidatorModel):
    pass


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


class RuleConditionUnion(BaseValidatorModel):
    pass


class ActionUnion(BaseValidatorModel):
    pass


class CreateRuleInput(BaseValidatorModel):
    ListenerArn: str
    Conditions: Sequence[RuleConditionUnion]
    Priority: int
    Actions: Sequence[ActionUnion]
    Tags: Optional[Sequence[Tag]] = None


class ModifyRuleInput(BaseValidatorModel):
    RuleArn: str
    Conditions: Optional[Sequence[RuleConditionUnion]] = None
    Actions: Optional[Sequence[ActionUnion]] = None



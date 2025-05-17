from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.elb.elb_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessLog(BaseValidatorModel):
    Enabled: bool
    S3BucketName: Optional[str] = None
    EmitInterval: Optional[int] = None
    S3BucketPrefix: Optional[str] = None


# This class is the input for the 'enable_availability_zones_for_load_balancer' function.
class AddAvailabilityZonesInput(BaseValidatorModel):
    LoadBalancerName: str
    AvailabilityZones: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class AdditionalAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class AppCookieStickinessPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None
    CookieName: Optional[str] = None


# This class is the input for the 'apply_security_groups_to_load_balancer' function.
class ApplySecurityGroupsToLoadBalancerInput(BaseValidatorModel):
    LoadBalancerName: str
    SecurityGroups: List[str]


# This class is the input for the 'attach_load_balancer_to_subnets' function.
class AttachLoadBalancerToSubnetsInput(BaseValidatorModel):
    LoadBalancerName: str
    Subnets: List[str]


class BackendServerDescription(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None


class HealthCheck(BaseValidatorModel):
    Target: str
    Interval: int
    Timeout: int
    UnhealthyThreshold: int
    HealthyThreshold: int


class ConnectionDraining(BaseValidatorModel):
    Enabled: bool
    Timeout: Optional[int] = None


class ConnectionSettings(BaseValidatorModel):
    IdleTimeout: int


class Listener(BaseValidatorModel):
    Protocol: str
    LoadBalancerPort: int
    InstancePort: int
    InstanceProtocol: Optional[str] = None
    SSLCertificateId: Optional[str] = None


class CreateAppCookieStickinessPolicyInput(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    CookieName: str


class CreateLBCookieStickinessPolicyInput(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    CookieExpirationPeriod: Optional[int] = None


class PolicyAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValue: Optional[str] = None


class CrossZoneLoadBalancing(BaseValidatorModel):
    Enabled: bool


class DeleteAccessPointInput(BaseValidatorModel):
    LoadBalancerName: str


class DeleteLoadBalancerListenerInput(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerPorts: List[int]


class DeleteLoadBalancerPolicyInput(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str


class Instance(BaseValidatorModel):
    InstanceId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_load_balancers' function.
class DescribeAccessPointsInput(BaseValidatorModel):
    LoadBalancerNames: Optional[List[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'describe_account_limits' function.
class DescribeAccountLimitsInput(BaseValidatorModel):
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class Limit(BaseValidatorModel):
    Name: Optional[str] = None
    Max: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class InstanceState(BaseValidatorModel):
    InstanceId: Optional[str] = None
    State: Optional[str] = None
    ReasonCode: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'describe_load_balancer_attributes' function.
class DescribeLoadBalancerAttributesInput(BaseValidatorModel):
    LoadBalancerName: str


# This class is the input for the 'describe_load_balancer_policies' function.
class DescribeLoadBalancerPoliciesInput(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    PolicyNames: Optional[List[str]] = None


# This class is the input for the 'describe_load_balancer_policy_types' function.
class DescribeLoadBalancerPolicyTypesInput(BaseValidatorModel):
    PolicyTypeNames: Optional[List[str]] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsInput(BaseValidatorModel):
    LoadBalancerNames: List[str]


# This class is the input for the 'detach_load_balancer_from_subnets' function.
class DetachLoadBalancerFromSubnetsInput(BaseValidatorModel):
    LoadBalancerName: str
    Subnets: List[str]


class LBCookieStickinessPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None
    CookieExpirationPeriod: Optional[int] = None


class SourceSecurityGroup(BaseValidatorModel):
    OwnerAlias: Optional[str] = None
    GroupName: Optional[str] = None


class PolicyAttributeDescription(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValue: Optional[str] = None


class PolicyAttributeTypeDescription(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[str] = None
    Description: Optional[str] = None
    DefaultValue: Optional[str] = None
    Cardinality: Optional[str] = None


# This class is the input for the 'disable_availability_zones_for_load_balancer' function.
class RemoveAvailabilityZonesInput(BaseValidatorModel):
    LoadBalancerName: str
    AvailabilityZones: List[str]


class TagKeyOnly(BaseValidatorModel):
    Key: Optional[str] = None


class SetLoadBalancerListenerSSLCertificateInput(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerPort: int
    SSLCertificateId: str


class SetLoadBalancerPoliciesForBackendServerInput(BaseValidatorModel):
    LoadBalancerName: str
    InstancePort: int
    PolicyNames: List[str]


class SetLoadBalancerPoliciesOfListenerInput(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerPort: int
    PolicyNames: List[str]


# This class is the output for the 'enable_availability_zones_for_load_balancer' function.
class AddAvailabilityZonesOutput(BaseValidatorModel):
    AvailabilityZones: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'apply_security_groups_to_load_balancer' function.
class ApplySecurityGroupsToLoadBalancerOutput(BaseValidatorModel):
    SecurityGroups: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_load_balancer_to_subnets' function.
class AttachLoadBalancerToSubnetsOutput(BaseValidatorModel):
    Subnets: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_load_balancer' function.
class CreateAccessPointOutput(BaseValidatorModel):
    DNSName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_load_balancer_from_subnets' function.
class DetachLoadBalancerFromSubnetsOutput(BaseValidatorModel):
    Subnets: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_availability_zones_for_load_balancer' function.
class RemoveAvailabilityZonesOutput(BaseValidatorModel):
    AvailabilityZones: List[str]
    ResponseMetadata: ResponseMetadata


class AddTagsInput(BaseValidatorModel):
    LoadBalancerNames: List[str]
    Tags: List[Tag]


class TagDescription(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'configure_health_check' function.
class ConfigureHealthCheckInput(BaseValidatorModel):
    LoadBalancerName: str
    HealthCheck: HealthCheck


# This class is the output for the 'configure_health_check' function.
class ConfigureHealthCheckOutput(BaseValidatorModel):
    HealthCheck: HealthCheck
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_load_balancer' function.
class CreateAccessPointInput(BaseValidatorModel):
    LoadBalancerName: str
    Listeners: List[Listener]
    AvailabilityZones: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    Scheme: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateLoadBalancerListenerInput(BaseValidatorModel):
    LoadBalancerName: str
    Listeners: List[Listener]


class ListenerDescription(BaseValidatorModel):
    Listener: Optional[Listener] = None
    PolicyNames: Optional[List[str]] = None


class CreateLoadBalancerPolicyInput(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    PolicyTypeName: str
    PolicyAttributes: Optional[List[PolicyAttribute]] = None


class LoadBalancerAttributesOutput(BaseValidatorModel):
    CrossZoneLoadBalancing: Optional[CrossZoneLoadBalancing] = None
    AccessLog: Optional[AccessLog] = None
    ConnectionDraining: Optional[ConnectionDraining] = None
    ConnectionSettings: Optional[ConnectionSettings] = None
    AdditionalAttributes: Optional[List[AdditionalAttribute]] = None


class LoadBalancerAttributes(BaseValidatorModel):
    CrossZoneLoadBalancing: Optional[CrossZoneLoadBalancing] = None
    AccessLog: Optional[AccessLog] = None
    ConnectionDraining: Optional[ConnectionDraining] = None
    ConnectionSettings: Optional[ConnectionSettings] = None
    AdditionalAttributes: Optional[List[AdditionalAttribute]] = None


# This class is the input for the 'deregister_instances_from_load_balancer' function.
class DeregisterEndPointsInput(BaseValidatorModel):
    LoadBalancerName: str
    Instances: List[Instance]


# This class is the output for the 'deregister_instances_from_load_balancer' function.
class DeregisterEndPointsOutput(BaseValidatorModel):
    Instances: List[Instance]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'describe_instance_health' function.
class DescribeEndPointStateInput(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[List[Instance]] = None


# This class is the input for the 'register_instances_with_load_balancer' function.
class RegisterEndPointsInput(BaseValidatorModel):
    LoadBalancerName: str
    Instances: List[Instance]


# This class is the output for the 'register_instances_with_load_balancer' function.
class RegisterEndPointsOutput(BaseValidatorModel):
    Instances: List[Instance]
    ResponseMetadata: ResponseMetadata


class DescribeAccessPointsInputPaginate(BaseValidatorModel):
    LoadBalancerNames: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAccountLimitsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_account_limits' function.
class DescribeAccountLimitsOutput(BaseValidatorModel):
    Limits: List[Limit]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class DescribeEndPointStateInputWaitExtraExtra(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[List[Instance]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEndPointStateInputWaitExtra(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[List[Instance]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEndPointStateInputWait(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[List[Instance]] = None
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'describe_instance_health' function.
class DescribeEndPointStateOutput(BaseValidatorModel):
    InstanceStates: List[InstanceState]
    ResponseMetadata: ResponseMetadata


class Policies(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[List[AppCookieStickinessPolicy]] = None
    LBCookieStickinessPolicies: Optional[List[LBCookieStickinessPolicy]] = None
    OtherPolicies: Optional[List[str]] = None


class PolicyDescription(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyTypeName: Optional[str] = None
    PolicyAttributeDescriptions: Optional[List[PolicyAttributeDescription]] = None


class PolicyTypeDescription(BaseValidatorModel):
    PolicyTypeName: Optional[str] = None
    Description: Optional[str] = None
    PolicyAttributeTypeDescriptions: Optional[List[PolicyAttributeTypeDescription]] = None


class RemoveTagsInput(BaseValidatorModel):
    LoadBalancerNames: List[str]
    Tags: List[TagKeyOnly]


# This class is the output for the 'describe_tags' function.
class DescribeTagsOutput(BaseValidatorModel):
    TagDescriptions: List[TagDescription]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_load_balancer_attributes' function.
class DescribeLoadBalancerAttributesOutput(BaseValidatorModel):
    LoadBalancerAttributes: LoadBalancerAttributesOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_load_balancer_attributes' function.
class ModifyLoadBalancerAttributesOutput(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerAttributes: LoadBalancerAttributesOutput
    ResponseMetadata: ResponseMetadata

LoadBalancerAttributesUnion = Union[LoadBalancerAttributes, LoadBalancerAttributesOutput]


class LoadBalancerDescription(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    DNSName: Optional[str] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    ListenerDescriptions: Optional[List[ListenerDescription]] = None
    Policies: Optional[Policies] = None
    BackendServerDescriptions: Optional[List[BackendServerDescription]] = None
    AvailabilityZones: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None
    VPCId: Optional[str] = None
    Instances: Optional[List[Instance]] = None
    HealthCheck: Optional[HealthCheck] = None
    SourceSecurityGroup: Optional[SourceSecurityGroup] = None
    SecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None
    Scheme: Optional[str] = None


# This class is the output for the 'describe_load_balancer_policies' function.
class DescribeLoadBalancerPoliciesOutput(BaseValidatorModel):
    PolicyDescriptions: List[PolicyDescription]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_load_balancer_policy_types' function.
class DescribeLoadBalancerPolicyTypesOutput(BaseValidatorModel):
    PolicyTypeDescriptions: List[PolicyTypeDescription]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'modify_load_balancer_attributes' function.
class ModifyLoadBalancerAttributesInput(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerAttributes: LoadBalancerAttributesUnion


# This class is the output for the 'describe_load_balancers' function.
class DescribeAccessPointsOutput(BaseValidatorModel):
    LoadBalancerDescriptions: List[LoadBalancerDescription]
    NextMarker: str
    ResponseMetadata: ResponseMetadata
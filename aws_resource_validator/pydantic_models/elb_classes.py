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
from aws_resource_validator.pydantic_models.elb_constants import *

class AccessLogTypeDef(BaseValidatorModel):
    Enabled: bool
    S3BucketName: Optional[str] = None
    EmitInterval: Optional[int] = None
    S3BucketPrefix: Optional[str] = None


class AddAvailabilityZonesInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    AvailabilityZones: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class AdditionalAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class AppCookieStickinessPolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    CookieName: Optional[str] = None


class ApplySecurityGroupsToLoadBalancerInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    SecurityGroups: Sequence[str]


class AttachLoadBalancerToSubnetsInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Subnets: Sequence[str]


class BackendServerDescriptionTypeDef(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None


class HealthCheckTypeDef(BaseValidatorModel):
    Target: str
    Interval: int
    Timeout: int
    UnhealthyThreshold: int
    HealthyThreshold: int


class ConnectionDrainingTypeDef(BaseValidatorModel):
    Enabled: bool
    Timeout: Optional[int] = None


class ConnectionSettingsTypeDef(BaseValidatorModel):
    IdleTimeout: int


class CreateAppCookieStickinessPolicyInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    CookieName: str


class CreateLBCookieStickinessPolicyInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    CookieExpirationPeriod: Optional[int] = None


class PolicyAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValue: Optional[str] = None


class CrossZoneLoadBalancingTypeDef(BaseValidatorModel):
    Enabled: bool


class DeleteAccessPointInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str


class DeleteLoadBalancerListenerInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerPorts: Sequence[int]


class DeleteLoadBalancerPolicyInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str


class InstanceTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAccessPointsInputTypeDef(BaseValidatorModel):
    LoadBalancerNames: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class DescribeAccountLimitsInputTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    PageSize: Optional[int] = None


class LimitTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Max: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class InstanceStateTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    State: Optional[str] = None
    ReasonCode: Optional[str] = None
    Description: Optional[str] = None


class DescribeLoadBalancerAttributesInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str


class DescribeLoadBalancerPoliciesInputTypeDef(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    PolicyNames: Optional[Sequence[str]] = None


class DescribeLoadBalancerPolicyTypesInputTypeDef(BaseValidatorModel):
    PolicyTypeNames: Optional[Sequence[str]] = None


class DescribeTagsInputTypeDef(BaseValidatorModel):
    LoadBalancerNames: Sequence[str]


class DetachLoadBalancerFromSubnetsInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Subnets: Sequence[str]


class LBCookieStickinessPolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    CookieExpirationPeriod: Optional[int] = None


class SourceSecurityGroupTypeDef(BaseValidatorModel):
    OwnerAlias: Optional[str] = None
    GroupName: Optional[str] = None


class PolicyAttributeDescriptionTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValue: Optional[str] = None


class PolicyAttributeTypeDescriptionTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[str] = None
    Description: Optional[str] = None
    DefaultValue: Optional[str] = None
    Cardinality: Optional[str] = None


class RemoveAvailabilityZonesInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    AvailabilityZones: Sequence[str]


class TagKeyOnlyTypeDef(BaseValidatorModel):
    Key: Optional[str] = None


class SetLoadBalancerListenerSSLCertificateInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerPort: int
    SSLCertificateId: str


class SetLoadBalancerPoliciesForBackendServerInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    InstancePort: int
    PolicyNames: Sequence[str]


class SetLoadBalancerPoliciesOfListenerInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerPort: int
    PolicyNames: Sequence[str]


class AddAvailabilityZonesOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ApplySecurityGroupsToLoadBalancerOutputTypeDef(BaseValidatorModel):
    SecurityGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class AttachLoadBalancerToSubnetsOutputTypeDef(BaseValidatorModel):
    Subnets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAccessPointOutputTypeDef(BaseValidatorModel):
    DNSName: str
    ResponseMetadata: ResponseMetadataTypeDef


class DetachLoadBalancerFromSubnetsOutputTypeDef(BaseValidatorModel):
    Subnets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveAvailabilityZonesOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class AddTagsInputTypeDef(BaseValidatorModel):
    LoadBalancerNames: Sequence[str]
    Tags: Sequence[TagTypeDef]


class TagDescriptionTypeDef(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class ConfigureHealthCheckInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    HealthCheck: HealthCheckTypeDef


class ConfigureHealthCheckOutputTypeDef(BaseValidatorModel):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListenerTypeDef(BaseValidatorModel):
    pass


class CreateAccessPointInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Listeners: Sequence[ListenerTypeDef]
    AvailabilityZones: Optional[Sequence[str]] = None
    Subnets: Optional[Sequence[str]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    Scheme: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateLoadBalancerListenerInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Listeners: Sequence[ListenerTypeDef]


class ListenerDescriptionTypeDef(BaseValidatorModel):
    Listener: Optional[ListenerTypeDef] = None
    PolicyNames: Optional[List[str]] = None


class CreateLoadBalancerPolicyInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    PolicyTypeName: str
    PolicyAttributes: Optional[Sequence[PolicyAttributeTypeDef]] = None


class LoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    CrossZoneLoadBalancing: Optional[CrossZoneLoadBalancingTypeDef] = None
    AccessLog: Optional[AccessLogTypeDef] = None
    ConnectionDraining: Optional[ConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[ConnectionSettingsTypeDef] = None
    AdditionalAttributes: Optional[List[AdditionalAttributeTypeDef]] = None


class LoadBalancerAttributesTypeDef(BaseValidatorModel):
    CrossZoneLoadBalancing: Optional[CrossZoneLoadBalancingTypeDef] = None
    AccessLog: Optional[AccessLogTypeDef] = None
    ConnectionDraining: Optional[ConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[ConnectionSettingsTypeDef] = None
    AdditionalAttributes: Optional[Sequence[AdditionalAttributeTypeDef]] = None


class DeregisterEndPointsInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Sequence[InstanceTypeDef]


class DeregisterEndPointsOutputTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEndPointStateInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None


class RegisterEndPointsInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Sequence[InstanceTypeDef]


class RegisterEndPointsOutputTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccessPointsInputPaginateTypeDef(BaseValidatorModel):
    LoadBalancerNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAccountLimitsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAccountLimitsOutputTypeDef(BaseValidatorModel):
    Limits: List[LimitTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEndPointStateInputWaitExtraExtraTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeEndPointStateInputWaitExtraTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeEndPointStateInputWaitTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeEndPointStateOutputTypeDef(BaseValidatorModel):
    InstanceStates: List[InstanceStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PoliciesTypeDef(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[List[AppCookieStickinessPolicyTypeDef]] = None
    LBCookieStickinessPolicies: Optional[List[LBCookieStickinessPolicyTypeDef]] = None
    OtherPolicies: Optional[List[str]] = None


class PolicyDescriptionTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyTypeName: Optional[str] = None
    PolicyAttributeDescriptions: Optional[List[PolicyAttributeDescriptionTypeDef]] = None


class PolicyTypeDescriptionTypeDef(BaseValidatorModel):
    PolicyTypeName: Optional[str] = None
    Description: Optional[str] = None
    PolicyAttributeTypeDescriptions: Optional[List[PolicyAttributeTypeDescriptionTypeDef]] = None


class RemoveTagsInputTypeDef(BaseValidatorModel):
    LoadBalancerNames: Sequence[str]
    Tags: Sequence[TagKeyOnlyTypeDef]


class DescribeTagsOutputTypeDef(BaseValidatorModel):
    TagDescriptions: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    LoadBalancerAttributes: LoadBalancerAttributesOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerAttributes: LoadBalancerAttributesOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoadBalancerDescriptionTypeDef(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    DNSName: Optional[str] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    ListenerDescriptions: Optional[List[ListenerDescriptionTypeDef]] = None
    Policies: Optional[PoliciesTypeDef] = None
    BackendServerDescriptions: Optional[List[BackendServerDescriptionTypeDef]] = None
    AvailabilityZones: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None
    VPCId: Optional[str] = None
    Instances: Optional[List[InstanceTypeDef]] = None
    HealthCheck: Optional[HealthCheckTypeDef] = None
    SourceSecurityGroup: Optional[SourceSecurityGroupTypeDef] = None
    SecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None
    Scheme: Optional[str] = None


class DescribeLoadBalancerPoliciesOutputTypeDef(BaseValidatorModel):
    PolicyDescriptions: List[PolicyDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLoadBalancerPolicyTypesOutputTypeDef(BaseValidatorModel):
    PolicyTypeDescriptions: List[PolicyTypeDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LoadBalancerAttributesUnionTypeDef(BaseValidatorModel):
    pass


class ModifyLoadBalancerAttributesInputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerAttributes: LoadBalancerAttributesUnionTypeDef


class DescribeAccessPointsOutputTypeDef(BaseValidatorModel):
    LoadBalancerDescriptions: List[LoadBalancerDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef



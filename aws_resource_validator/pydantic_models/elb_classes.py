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
from aws_resource_validator.pydantic_models.elb_constants import *

class AccessLogTypeDef(BaseValidatorModel):
    Enabled: bool
    S3BucketName: Optional[str] = None
    EmitInterval: Optional[int] = None
    S3BucketPrefix: Optional[str] = None

class AddAvailabilityZonesInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    AvailabilityZones: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class AdditionalAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AppCookieStickinessPolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    CookieName: Optional[str] = None

class ApplySecurityGroupsToLoadBalancerInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    SecurityGroups: Sequence[str]

class AttachLoadBalancerToSubnetsInputRequestTypeDef(BaseValidatorModel):
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

class ListenerTypeDef(BaseValidatorModel):
    Protocol: str
    LoadBalancerPort: int
    InstancePort: int
    InstanceProtocol: Optional[str] = None
    SSLCertificateId: Optional[str] = None

class CreateAppCookieStickinessPolicyInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    CookieName: str

class CreateLBCookieStickinessPolicyInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    CookieExpirationPeriod: Optional[int] = None

class PolicyAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValue: Optional[str] = None

class CrossZoneLoadBalancingTypeDef(BaseValidatorModel):
    Enabled: bool

class DeleteAccessPointInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str

class DeleteLoadBalancerListenerInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerPorts: Sequence[int]

class DeleteLoadBalancerPolicyInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str

class InstanceTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccessPointsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerNames: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeAccountLimitsInputRequestTypeDef(BaseValidatorModel):
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

class DescribeLoadBalancerAttributesInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str

class DescribeLoadBalancerPoliciesInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    PolicyNames: Optional[Sequence[str]] = None

class DescribeLoadBalancerPolicyTypesInputRequestTypeDef(BaseValidatorModel):
    PolicyTypeNames: Optional[Sequence[str]] = None

class DescribeTagsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerNames: Sequence[str]

class DetachLoadBalancerFromSubnetsInputRequestTypeDef(BaseValidatorModel):
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

class RemoveAvailabilityZonesInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    AvailabilityZones: Sequence[str]

class TagKeyOnlyTypeDef(BaseValidatorModel):
    Key: Optional[str] = None

class SetLoadBalancerListenerSSLCertificateInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerPort: int
    SSLCertificateId: str

class SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    InstancePort: int
    PolicyNames: Sequence[str]

class SetLoadBalancerPoliciesOfListenerInputRequestTypeDef(BaseValidatorModel):
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

class AddTagsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerNames: Sequence[str]
    Tags: Sequence[TagTypeDef]

class TagDescriptionTypeDef(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ConfigureHealthCheckInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    HealthCheck: HealthCheckTypeDef

class ConfigureHealthCheckOutputTypeDef(BaseValidatorModel):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPointInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Listeners: Sequence[ListenerTypeDef]
    AvailabilityZones: Optional[Sequence[str]] = None
    Subnets: Optional[Sequence[str]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    Scheme: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateLoadBalancerListenerInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Listeners: Sequence[ListenerTypeDef]

class ListenerDescriptionTypeDef(BaseValidatorModel):
    Listener: Optional[ListenerTypeDef] = None
    PolicyNames: Optional[List[str]] = None

class CreateLoadBalancerPolicyInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    PolicyName: str
    PolicyTypeName: str
    PolicyAttributes: Optional[Sequence[PolicyAttributeTypeDef]] = None

class LoadBalancerAttributesTypeDef(BaseValidatorModel):
    CrossZoneLoadBalancing: Optional[CrossZoneLoadBalancingTypeDef] = None
    AccessLog: Optional[AccessLogTypeDef] = None
    ConnectionDraining: Optional[ConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[ConnectionSettingsTypeDef] = None
    AdditionalAttributes: Optional[List[AdditionalAttributeTypeDef]] = None

class DeregisterEndPointsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Sequence[InstanceTypeDef]

class DeregisterEndPointsOutputTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndPointStateInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None

class RegisterEndPointsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Sequence[InstanceTypeDef]

class RegisterEndPointsOutputTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessPointsInputDescribeLoadBalancersPaginateTypeDef(BaseValidatorModel):
    LoadBalancerNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountLimitsOutputTypeDef(BaseValidatorModel):
    Limits: List[LimitTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndPointStateInputInstanceDeregisteredWaitTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndPointStateInputInstanceInServiceWaitTypeDef(BaseValidatorModel):
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

class RemoveTagsInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerNames: Sequence[str]
    Tags: Sequence[TagKeyOnlyTypeDef]

class DescribeTagsOutputTypeDef(BaseValidatorModel):
    TagDescriptions: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    LoadBalancerAttributes: LoadBalancerAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLoadBalancerAttributesInputRequestTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerAttributes: LoadBalancerAttributesTypeDef

class ModifyLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    LoadBalancerName: str
    LoadBalancerAttributes: LoadBalancerAttributesTypeDef
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

class DescribeAccessPointsOutputTypeDef(BaseValidatorModel):
    LoadBalancerDescriptions: List[LoadBalancerDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


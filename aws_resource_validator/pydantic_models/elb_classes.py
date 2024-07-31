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
from aws_resource_validator.pydantic_models.elb_constants import *

class AccessLogTypeDef(BaseModel):
    Enabled: bool
    S3BucketName: Optional[str] = None
    EmitInterval: Optional[int] = None
    S3BucketPrefix: Optional[str] = None

class AddAvailabilityZonesInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    AvailabilityZones: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class AdditionalAttributeTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AppCookieStickinessPolicyTypeDef(BaseModel):
    PolicyName: Optional[str] = None
    CookieName: Optional[str] = None

class ApplySecurityGroupsToLoadBalancerInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    SecurityGroups: Sequence[str]

class AttachLoadBalancerToSubnetsInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    Subnets: Sequence[str]

class BackendServerDescriptionTypeDef(BaseModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None

class HealthCheckTypeDef(BaseModel):
    Target: str
    Interval: int
    Timeout: int
    UnhealthyThreshold: int
    HealthyThreshold: int

class ConnectionDrainingTypeDef(BaseModel):
    Enabled: bool
    Timeout: Optional[int] = None

class ConnectionSettingsTypeDef(BaseModel):
    IdleTimeout: int

class ListenerTypeDef(BaseModel):
    Protocol: str
    LoadBalancerPort: int
    InstancePort: int
    InstanceProtocol: Optional[str] = None
    SSLCertificateId: Optional[str] = None

class CreateAppCookieStickinessPolicyInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    PolicyName: str
    CookieName: str

class CreateLBCookieStickinessPolicyInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    PolicyName: str
    CookieExpirationPeriod: Optional[int] = None

class PolicyAttributeTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValue: Optional[str] = None

class CrossZoneLoadBalancingTypeDef(BaseModel):
    Enabled: bool

class DeleteAccessPointInputRequestTypeDef(BaseModel):
    LoadBalancerName: str

class DeleteLoadBalancerListenerInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    LoadBalancerPorts: Sequence[int]

class DeleteLoadBalancerPolicyInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    PolicyName: str

class InstanceTypeDef(BaseModel):
    InstanceId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccessPointsInputRequestTypeDef(BaseModel):
    LoadBalancerNames: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class DescribeAccountLimitsInputRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    PageSize: Optional[int] = None

class LimitTypeDef(BaseModel):
    Name: Optional[str] = None
    Max: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class InstanceStateTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    State: Optional[str] = None
    ReasonCode: Optional[str] = None
    Description: Optional[str] = None

class DescribeLoadBalancerAttributesInputRequestTypeDef(BaseModel):
    LoadBalancerName: str

class DescribeLoadBalancerPoliciesInputRequestTypeDef(BaseModel):
    LoadBalancerName: Optional[str] = None
    PolicyNames: Optional[Sequence[str]] = None

class DescribeLoadBalancerPolicyTypesInputRequestTypeDef(BaseModel):
    PolicyTypeNames: Optional[Sequence[str]] = None

class DescribeTagsInputRequestTypeDef(BaseModel):
    LoadBalancerNames: Sequence[str]

class DetachLoadBalancerFromSubnetsInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    Subnets: Sequence[str]

class LBCookieStickinessPolicyTypeDef(BaseModel):
    PolicyName: Optional[str] = None
    CookieExpirationPeriod: Optional[int] = None

class SourceSecurityGroupTypeDef(BaseModel):
    OwnerAlias: Optional[str] = None
    GroupName: Optional[str] = None

class PolicyAttributeDescriptionTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValue: Optional[str] = None

class PolicyAttributeTypeDescriptionTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[str] = None
    Description: Optional[str] = None
    DefaultValue: Optional[str] = None
    Cardinality: Optional[str] = None

class RemoveAvailabilityZonesInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    AvailabilityZones: Sequence[str]

class TagKeyOnlyTypeDef(BaseModel):
    Key: Optional[str] = None

class SetLoadBalancerListenerSSLCertificateInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    LoadBalancerPort: int
    SSLCertificateId: str

class SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    InstancePort: int
    PolicyNames: Sequence[str]

class SetLoadBalancerPoliciesOfListenerInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    LoadBalancerPort: int
    PolicyNames: Sequence[str]

class AddAvailabilityZonesOutputTypeDef(BaseModel):
    AvailabilityZones: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ApplySecurityGroupsToLoadBalancerOutputTypeDef(BaseModel):
    SecurityGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class AttachLoadBalancerToSubnetsOutputTypeDef(BaseModel):
    Subnets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPointOutputTypeDef(BaseModel):
    DNSName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetachLoadBalancerFromSubnetsOutputTypeDef(BaseModel):
    Subnets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveAvailabilityZonesOutputTypeDef(BaseModel):
    AvailabilityZones: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsInputRequestTypeDef(BaseModel):
    LoadBalancerNames: Sequence[str]
    Tags: Sequence[TagTypeDef]

class TagDescriptionTypeDef(BaseModel):
    LoadBalancerName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ConfigureHealthCheckInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    HealthCheck: HealthCheckTypeDef

class ConfigureHealthCheckOutputTypeDef(BaseModel):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPointInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    Listeners: Sequence[ListenerTypeDef]
    AvailabilityZones: Optional[Sequence[str]] = None
    Subnets: Optional[Sequence[str]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    Scheme: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateLoadBalancerListenerInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    Listeners: Sequence[ListenerTypeDef]

class ListenerDescriptionTypeDef(BaseModel):
    Listener: Optional[ListenerTypeDef] = None
    PolicyNames: Optional[List[str]] = None

class CreateLoadBalancerPolicyInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    PolicyName: str
    PolicyTypeName: str
    PolicyAttributes: Optional[Sequence[PolicyAttributeTypeDef]] = None

class LoadBalancerAttributesTypeDef(BaseModel):
    CrossZoneLoadBalancing: Optional[CrossZoneLoadBalancingTypeDef] = None
    AccessLog: Optional[AccessLogTypeDef] = None
    ConnectionDraining: Optional[ConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[ConnectionSettingsTypeDef] = None
    AdditionalAttributes: Optional[List[AdditionalAttributeTypeDef]] = None

class DeregisterEndPointsInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    Instances: Sequence[InstanceTypeDef]

class DeregisterEndPointsOutputTypeDef(BaseModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndPointStateInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None

class RegisterEndPointsInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    Instances: Sequence[InstanceTypeDef]

class RegisterEndPointsOutputTypeDef(BaseModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessPointsInputDescribeLoadBalancersPaginateTypeDef(BaseModel):
    LoadBalancerNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountLimitsOutputTypeDef(BaseModel):
    Limits: List[LimitTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef(BaseModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndPointStateInputInstanceDeregisteredWaitTypeDef(BaseModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndPointStateInputInstanceInServiceWaitTypeDef(BaseModel):
    LoadBalancerName: str
    Instances: Optional[Sequence[InstanceTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndPointStateOutputTypeDef(BaseModel):
    InstanceStates: List[InstanceStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PoliciesTypeDef(BaseModel):
    AppCookieStickinessPolicies: Optional[List[AppCookieStickinessPolicyTypeDef]] = None
    LBCookieStickinessPolicies: Optional[List[LBCookieStickinessPolicyTypeDef]] = None
    OtherPolicies: Optional[List[str]] = None

class PolicyDescriptionTypeDef(BaseModel):
    PolicyName: Optional[str] = None
    PolicyTypeName: Optional[str] = None
    PolicyAttributeDescriptions: Optional[List[PolicyAttributeDescriptionTypeDef]] = None

class PolicyTypeDescriptionTypeDef(BaseModel):
    PolicyTypeName: Optional[str] = None
    Description: Optional[str] = None
    PolicyAttributeTypeDescriptions: Optional[List[PolicyAttributeTypeDescriptionTypeDef]] = None

class RemoveTagsInputRequestTypeDef(BaseModel):
    LoadBalancerNames: Sequence[str]
    Tags: Sequence[TagKeyOnlyTypeDef]

class DescribeTagsOutputTypeDef(BaseModel):
    TagDescriptions: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancerAttributesOutputTypeDef(BaseModel):
    LoadBalancerAttributes: LoadBalancerAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLoadBalancerAttributesInputRequestTypeDef(BaseModel):
    LoadBalancerName: str
    LoadBalancerAttributes: LoadBalancerAttributesTypeDef

class ModifyLoadBalancerAttributesOutputTypeDef(BaseModel):
    LoadBalancerName: str
    LoadBalancerAttributes: LoadBalancerAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LoadBalancerDescriptionTypeDef(BaseModel):
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

class DescribeLoadBalancerPoliciesOutputTypeDef(BaseModel):
    PolicyDescriptions: List[PolicyDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancerPolicyTypesOutputTypeDef(BaseModel):
    PolicyTypeDescriptions: List[PolicyTypeDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessPointsOutputTypeDef(BaseModel):
    LoadBalancerDescriptions: List[LoadBalancerDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.servicediscovery.servicediscovery_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class HealthCheckConfig(BaseValidatorModel):
    Type: HealthCheckTypeType
    ResourcePath: Optional[str] = None
    FailureThreshold: Optional[int] = None


class HealthCheckCustomConfig(BaseValidatorModel):
    FailureThreshold: Optional[int] = None


# This class is the input for the 'delete_namespace' function.
class DeleteNamespaceRequest(BaseValidatorModel):
    Id: str


class DeleteServiceAttributesRequest(BaseValidatorModel):
    ServiceId: str
    Attributes: List[str]


class DeleteServiceRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'deregister_instance' function.
class DeregisterInstanceRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str


# This class is the input for the 'discover_instances' function.
class DiscoverInstancesRequest(BaseValidatorModel):
    NamespaceName: str
    ServiceName: str
    MaxResults: Optional[int] = None
    QueryParameters: Optional[Dict[str, str]] = None
    OptionalParameters: Optional[Dict[str, str]] = None
    HealthStatus: Optional[HealthStatusFilterType] = None


class HttpInstanceSummary(BaseValidatorModel):
    InstanceId: Optional[str] = None
    NamespaceName: Optional[str] = None
    ServiceName: Optional[str] = None
    HealthStatus: Optional[HealthStatusType] = None
    Attributes: Optional[Dict[str, str]] = None


# This class is the input for the 'discover_instances_revision' function.
class DiscoverInstancesRevisionRequest(BaseValidatorModel):
    NamespaceName: str
    ServiceName: str


class DnsRecord(BaseValidatorModel):
    Type: RecordTypeType
    TTL: int


class SOA(BaseValidatorModel):
    TTL: int


# This class is the input for the 'get_instance' function.
class GetInstanceRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str


class Instance(BaseValidatorModel):
    Id: str
    CreatorRequestId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


# This class is the input for the 'get_instances_health_status' function.
class GetInstancesHealthStatusRequest(BaseValidatorModel):
    ServiceId: str
    Instances: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_namespace' function.
class GetNamespaceRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_operation' function.
class GetOperationRequest(BaseValidatorModel):
    OperationId: str


class Operation(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[OperationTypeType] = None
    Status: Optional[OperationStatusType] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    CreateDate: Optional[datetime] = None
    UpdateDate: Optional[datetime] = None
    Targets: Optional[Dict[OperationTargetTypeType, str]] = None


# This class is the input for the 'get_service_attributes' function.
class GetServiceAttributesRequest(BaseValidatorModel):
    ServiceId: str


class ServiceAttributes(BaseValidatorModel):
    ServiceArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


# This class is the input for the 'get_service' function.
class GetServiceRequest(BaseValidatorModel):
    Id: str


class HttpNamespaceChange(BaseValidatorModel):
    Description: str


class HttpProperties(BaseValidatorModel):
    HttpName: Optional[str] = None


class InstanceSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_instances' function.
class ListInstancesRequest(BaseValidatorModel):
    ServiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class NamespaceFilter(BaseValidatorModel):
    Name: NamespaceFilterNameType
    Values: List[str]
    Condition: Optional[FilterConditionType] = None


class OperationFilter(BaseValidatorModel):
    Name: OperationFilterNameType
    Values: List[str]
    Condition: Optional[FilterConditionType] = None


class OperationSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Status: Optional[OperationStatusType] = None


class ServiceFilter(BaseValidatorModel):
    Name: Literal['NAMESPACE_ID']
    Values: List[str]
    Condition: Optional[FilterConditionType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class SOAChange(BaseValidatorModel):
    TTL: int


# This class is the input for the 'register_instance' function.
class RegisterInstanceRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Attributes: Dict[str, str]
    CreatorRequestId: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_instance_custom_health_status' function.
class UpdateInstanceCustomHealthStatusRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Status: CustomHealthStatusType


class UpdateServiceAttributesRequest(BaseValidatorModel):
    ServiceId: str
    Attributes: Dict[str, str]


# This class is the input for the 'create_http_namespace' function.
class CreateHttpNamespaceRequest(BaseValidatorModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the output for the 'create_http_namespace' function.
class CreateHttpNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_private_dns_namespace' function.
class CreatePrivateDnsNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_public_dns_namespace' function.
class CreatePublicDnsNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_namespace' function.
class DeleteNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_instance' function.
class DeregisterInstanceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'discover_instances_revision' function.
class DiscoverInstancesRevisionResponse(BaseValidatorModel):
    InstancesRevision: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_instance_custom_health_status' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instances_health_status' function.
class GetInstancesHealthStatusResponse(BaseValidatorModel):
    Status: Dict[str, HealthStatusType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_instance' function.
class RegisterInstanceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_http_namespace' function.
class UpdateHttpNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_private_dns_namespace' function.
class UpdatePrivateDnsNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_public_dns_namespace' function.
class UpdatePublicDnsNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service' function.
class UpdateServiceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'discover_instances' function.
class DiscoverInstancesResponse(BaseValidatorModel):
    Instances: List[HttpInstanceSummary]
    InstancesRevision: int
    ResponseMetadata: ResponseMetadata


class DnsConfigChange(BaseValidatorModel):
    DnsRecords: List[DnsRecord]


class DnsConfigOutput(BaseValidatorModel):
    DnsRecords: List[DnsRecord]
    NamespaceId: Optional[str] = None
    RoutingPolicy: Optional[RoutingPolicyType] = None


class DnsConfig(BaseValidatorModel):
    DnsRecords: List[DnsRecord]
    NamespaceId: Optional[str] = None
    RoutingPolicy: Optional[RoutingPolicyType] = None


class DnsProperties(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    SOA: Optional[SOA] = None


class PrivateDnsPropertiesMutable(BaseValidatorModel):
    SOA: SOA


class PublicDnsPropertiesMutable(BaseValidatorModel):
    SOA: SOA


# This class is the output for the 'get_instance' function.
class GetInstanceResponse(BaseValidatorModel):
    Instance: Instance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_operation' function.
class GetOperationResponse(BaseValidatorModel):
    Operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_attributes' function.
class GetServiceAttributesResponse(BaseValidatorModel):
    ServiceAttributes: ServiceAttributes
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_http_namespace' function.
class UpdateHttpNamespaceRequest(BaseValidatorModel):
    Id: str
    Namespace: HttpNamespaceChange
    UpdaterRequestId: Optional[str] = None


# This class is the output for the 'list_instances' function.
class ListInstancesResponse(BaseValidatorModel):
    Instances: List[InstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListInstancesRequestPaginate(BaseValidatorModel):
    ServiceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNamespacesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[NamespaceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_namespaces' function.
class ListNamespacesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[NamespaceFilter]] = None


class ListOperationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[OperationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_operations' function.
class ListOperationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[OperationFilter]] = None


# This class is the output for the 'list_operations' function.
class ListOperationsResponse(BaseValidatorModel):
    Operations: List[OperationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServicesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[ServiceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_services' function.
class ListServicesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[ServiceFilter]] = None


class PrivateDnsPropertiesMutableChange(BaseValidatorModel):
    SOA: SOAChange


class PublicDnsPropertiesMutableChange(BaseValidatorModel):
    SOA: SOAChange


class ServiceChange(BaseValidatorModel):
    Description: Optional[str] = None
    DnsConfig: Optional[DnsConfigChange] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None


class ServiceSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ServiceTypeType] = None
    Description: Optional[str] = None
    InstanceCount: Optional[int] = None
    DnsConfig: Optional[DnsConfigOutput] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfig] = None
    CreateDate: Optional[datetime] = None


class Service(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    NamespaceId: Optional[str] = None
    Description: Optional[str] = None
    InstanceCount: Optional[int] = None
    DnsConfig: Optional[DnsConfigOutput] = None
    Type: Optional[ServiceTypeType] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfig] = None
    CreateDate: Optional[datetime] = None
    CreatorRequestId: Optional[str] = None

DnsConfigUnion = Union[DnsConfig, DnsConfigOutput]


class NamespaceProperties(BaseValidatorModel):
    DnsProperties: Optional[DnsProperties] = None
    HttpProperties: Optional[HttpProperties] = None


class PrivateDnsNamespaceProperties(BaseValidatorModel):
    DnsProperties: PrivateDnsPropertiesMutable


class PublicDnsNamespaceProperties(BaseValidatorModel):
    DnsProperties: PublicDnsPropertiesMutable


class PrivateDnsNamespacePropertiesChange(BaseValidatorModel):
    DnsProperties: PrivateDnsPropertiesMutableChange


class PublicDnsNamespacePropertiesChange(BaseValidatorModel):
    DnsProperties: PublicDnsPropertiesMutableChange


# This class is the input for the 'update_service' function.
class UpdateServiceRequest(BaseValidatorModel):
    Id: str
    Service: ServiceChange


# This class is the output for the 'list_services' function.
class ListServicesResponse(BaseValidatorModel):
    Services: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_service' function.
class CreateServiceResponse(BaseValidatorModel):
    Service: Service
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service' function.
class GetServiceResponse(BaseValidatorModel):
    Service: Service
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_service' function.
class CreateServiceRequest(BaseValidatorModel):
    Name: str
    NamespaceId: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    DnsConfig: Optional[DnsConfigUnion] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfig] = None
    Tags: Optional[List[Tag]] = None
    Type: Optional[Literal['HTTP']] = None


class NamespaceSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[NamespaceTypeType] = None
    Description: Optional[str] = None
    ServiceCount: Optional[int] = None
    Properties: Optional[NamespaceProperties] = None
    CreateDate: Optional[datetime] = None


class Namespace(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[NamespaceTypeType] = None
    Description: Optional[str] = None
    ServiceCount: Optional[int] = None
    Properties: Optional[NamespaceProperties] = None
    CreateDate: Optional[datetime] = None
    CreatorRequestId: Optional[str] = None


# This class is the input for the 'create_private_dns_namespace' function.
class CreatePrivateDnsNamespaceRequest(BaseValidatorModel):
    Name: str
    Vpc: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Properties: Optional[PrivateDnsNamespaceProperties] = None


# This class is the input for the 'create_public_dns_namespace' function.
class CreatePublicDnsNamespaceRequest(BaseValidatorModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Properties: Optional[PublicDnsNamespaceProperties] = None


class PrivateDnsNamespaceChange(BaseValidatorModel):
    Description: Optional[str] = None
    Properties: Optional[PrivateDnsNamespacePropertiesChange] = None


class PublicDnsNamespaceChange(BaseValidatorModel):
    Description: Optional[str] = None
    Properties: Optional[PublicDnsNamespacePropertiesChange] = None


# This class is the output for the 'list_namespaces' function.
class ListNamespacesResponse(BaseValidatorModel):
    Namespaces: List[NamespaceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_namespace' function.
class GetNamespaceResponse(BaseValidatorModel):
    Namespace: Namespace
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_private_dns_namespace' function.
class UpdatePrivateDnsNamespaceRequest(BaseValidatorModel):
    Id: str
    Namespace: PrivateDnsNamespaceChange
    UpdaterRequestId: Optional[str] = None


# This class is the input for the 'update_public_dns_namespace' function.
class UpdatePublicDnsNamespaceRequest(BaseValidatorModel):
    Id: str
    Namespace: PublicDnsNamespaceChange
    UpdaterRequestId: Optional[str] = None
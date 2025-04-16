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
from aws_resource_validator.pydantic_models.servicediscovery_constants import *

class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class HealthCheckCustomConfig(BaseValidatorModel):
    FailureThreshold: Optional[int] = None


class DeleteNamespaceRequest(BaseValidatorModel):
    Id: str


class DeleteServiceAttributesRequest(BaseValidatorModel):
    ServiceId: str
    Attributes: Sequence[str]


class DeleteServiceRequest(BaseValidatorModel):
    Id: str


class DeregisterInstanceRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str


class SOA(BaseValidatorModel):
    TTL: int


class GetInstanceRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str


class Instance(BaseValidatorModel):
    Id: str
    CreatorRequestId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class GetInstancesHealthStatusRequest(BaseValidatorModel):
    ServiceId: str
    Instances: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetNamespaceRequest(BaseValidatorModel):
    Id: str


class GetOperationRequest(BaseValidatorModel):
    OperationId: str


class GetServiceAttributesRequest(BaseValidatorModel):
    ServiceId: str


class ServiceAttributes(BaseValidatorModel):
    ServiceArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


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


class ListInstancesRequest(BaseValidatorModel):
    ServiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class NamespaceFilter(BaseValidatorModel):
    Name: NamespaceFilterNameType
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None


class OperationFilter(BaseValidatorModel):
    Name: OperationFilterNameType
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None


class OperationSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Status: Optional[OperationStatusType] = None


class ServiceFilter(BaseValidatorModel):
    Name: Literal["NAMESPACE_ID"]
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class SOAChange(BaseValidatorModel):
    TTL: int


class RegisterInstanceRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Attributes: Mapping[str, str]
    CreatorRequestId: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateInstanceCustomHealthStatusRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Status: CustomHealthStatusType


class UpdateServiceAttributesRequest(BaseValidatorModel):
    ServiceId: str
    Attributes: Mapping[str, str]


class CreateHttpNamespaceRequest(BaseValidatorModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateHttpNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class CreatePrivateDnsNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class CreatePublicDnsNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class DeleteNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class DeregisterInstanceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class DiscoverInstancesRevisionResponse(BaseValidatorModel):
    InstancesRevision: int
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetInstancesHealthStatusResponse(BaseValidatorModel):
    Status: Dict[str, HealthStatusType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class RegisterInstanceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class UpdateHttpNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class UpdatePrivateDnsNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class UpdatePublicDnsNamespaceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class UpdateServiceResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class HttpInstanceSummary(BaseValidatorModel):
    pass


class DiscoverInstancesResponse(BaseValidatorModel):
    Instances: List[HttpInstanceSummary]
    InstancesRevision: int
    ResponseMetadata: ResponseMetadata


class DnsRecord(BaseValidatorModel):
    pass


class DnsConfigChange(BaseValidatorModel):
    DnsRecords: Sequence[DnsRecord]


class DnsConfigOutput(BaseValidatorModel):
    DnsRecords: List[DnsRecord]
    NamespaceId: Optional[str] = None
    RoutingPolicy: Optional[RoutingPolicyType] = None


class DnsConfig(BaseValidatorModel):
    DnsRecords: Sequence[DnsRecord]
    NamespaceId: Optional[str] = None
    RoutingPolicy: Optional[RoutingPolicyType] = None


class DnsProperties(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    SOA: Optional[SOA] = None


class PrivateDnsPropertiesMutable(BaseValidatorModel):
    SOA: SOA


class PublicDnsPropertiesMutable(BaseValidatorModel):
    SOA: SOA


class GetInstanceResponse(BaseValidatorModel):
    Instance: Instance
    ResponseMetadata: ResponseMetadata


class Operation(BaseValidatorModel):
    pass


class GetOperationResponse(BaseValidatorModel):
    Operation: Operation
    ResponseMetadata: ResponseMetadata


class GetServiceAttributesResponse(BaseValidatorModel):
    ServiceAttributes: ServiceAttributes
    ResponseMetadata: ResponseMetadata


class UpdateHttpNamespaceRequest(BaseValidatorModel):
    Id: str
    Namespace: HttpNamespaceChange
    UpdaterRequestId: Optional[str] = None


class ListInstancesResponse(BaseValidatorModel):
    Instances: List[InstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListInstancesRequestPaginate(BaseValidatorModel):
    ServiceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNamespacesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[NamespaceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNamespacesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[NamespaceFilter]] = None


class ListOperationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[OperationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOperationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[OperationFilter]] = None


class ListOperationsResponse(BaseValidatorModel):
    Operations: List[OperationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServicesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ServiceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[ServiceFilter]] = None


class PrivateDnsPropertiesMutableChange(BaseValidatorModel):
    SOA: SOAChange


class PublicDnsPropertiesMutableChange(BaseValidatorModel):
    SOA: SOAChange


class HealthCheckConfig(BaseValidatorModel):
    pass


class ServiceChange(BaseValidatorModel):
    Description: Optional[str] = None
    DnsConfig: Optional[DnsConfigChange] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None


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


class UpdateServiceRequest(BaseValidatorModel):
    Id: str
    Service: ServiceChange


class ServiceSummary(BaseValidatorModel):
    pass


class ListServicesResponse(BaseValidatorModel):
    Services: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Service(BaseValidatorModel):
    pass


class CreateServiceResponse(BaseValidatorModel):
    Service: Service
    ResponseMetadata: ResponseMetadata


class GetServiceResponse(BaseValidatorModel):
    Service: Service
    ResponseMetadata: ResponseMetadata


class CreatePrivateDnsNamespaceRequest(BaseValidatorModel):
    Name: str
    Vpc: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    Properties: Optional[PrivateDnsNamespaceProperties] = None


class CreatePublicDnsNamespaceRequest(BaseValidatorModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    Properties: Optional[PublicDnsNamespaceProperties] = None


class PrivateDnsNamespaceChange(BaseValidatorModel):
    Description: Optional[str] = None
    Properties: Optional[PrivateDnsNamespacePropertiesChange] = None


class PublicDnsNamespaceChange(BaseValidatorModel):
    Description: Optional[str] = None
    Properties: Optional[PublicDnsNamespacePropertiesChange] = None


class NamespaceSummary(BaseValidatorModel):
    pass


class ListNamespacesResponse(BaseValidatorModel):
    Namespaces: List[NamespaceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Namespace(BaseValidatorModel):
    pass


class GetNamespaceResponse(BaseValidatorModel):
    Namespace: Namespace
    ResponseMetadata: ResponseMetadata


class UpdatePrivateDnsNamespaceRequest(BaseValidatorModel):
    Id: str
    Namespace: PrivateDnsNamespaceChange
    UpdaterRequestId: Optional[str] = None


class UpdatePublicDnsNamespaceRequest(BaseValidatorModel):
    Id: str
    Namespace: PublicDnsNamespaceChange
    UpdaterRequestId: Optional[str] = None



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


class DeleteNamespaceRequest(BaseValidatorModel):
    Id: str


class DeleteServiceAttributesRequest(BaseValidatorModel):
    ServiceId: str
    Attributes: List[str]


class DeleteServiceRequest(BaseValidatorModel):
    Id: str


class DeregisterInstanceRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str


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


class DiscoverInstancesRevisionRequest(BaseValidatorModel):
    NamespaceName: str
    ServiceName: str


class DnsRecord(BaseValidatorModel):
    Type: RecordTypeType
    TTL: int


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
    Instances: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetNamespaceRequest(BaseValidatorModel):
    Id: str


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


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class SOAChange(BaseValidatorModel):
    TTL: int


class RegisterInstanceRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Attributes: Dict[str, str]
    CreatorRequestId: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class UpdateInstanceCustomHealthStatusRequest(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Status: CustomHealthStatusType


class UpdateServiceAttributesRequest(BaseValidatorModel):
    ServiceId: str
    Attributes: Dict[str, str]


class CreateHttpNamespaceRequest(BaseValidatorModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


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


class GetInstanceResponse(BaseValidatorModel):
    Instance: Instance
    ResponseMetadata: ResponseMetadata


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
    Filters: Optional[List[NamespaceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNamespacesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[NamespaceFilter]] = None


class ListOperationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[OperationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOperationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[OperationFilter]] = None


class ListOperationsResponse(BaseValidatorModel):
    Operations: List[OperationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServicesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[ServiceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


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


class UpdateServiceRequest(BaseValidatorModel):
    Id: str
    Service: ServiceChange


class ListServicesResponse(BaseValidatorModel):
    Services: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateServiceResponse(BaseValidatorModel):
    Service: Service
    ResponseMetadata: ResponseMetadata


class GetServiceResponse(BaseValidatorModel):
    Service: Service
    ResponseMetadata: ResponseMetadata


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


class CreatePrivateDnsNamespaceRequest(BaseValidatorModel):
    Name: str
    Vpc: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Properties: Optional[PrivateDnsNamespaceProperties] = None


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


class ListNamespacesResponse(BaseValidatorModel):
    Namespaces: List[NamespaceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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
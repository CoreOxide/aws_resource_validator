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

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class HealthCheckCustomConfigTypeDef(BaseValidatorModel):
    FailureThreshold: Optional[int] = None


class DeleteNamespaceRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteServiceAttributesRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    Attributes: Sequence[str]


class DeleteServiceRequestTypeDef(BaseValidatorModel):
    Id: str


class DeregisterInstanceRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    InstanceId: str


class SOATypeDef(BaseValidatorModel):
    TTL: int


class GetInstanceRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    InstanceId: str


class InstanceTypeDef(BaseValidatorModel):
    Id: str
    CreatorRequestId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class GetInstancesHealthStatusRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    Instances: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetNamespaceRequestTypeDef(BaseValidatorModel):
    Id: str


class GetOperationRequestTypeDef(BaseValidatorModel):
    OperationId: str


class GetServiceAttributesRequestTypeDef(BaseValidatorModel):
    ServiceId: str


class ServiceAttributesTypeDef(BaseValidatorModel):
    ServiceArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class GetServiceRequestTypeDef(BaseValidatorModel):
    Id: str


class HttpNamespaceChangeTypeDef(BaseValidatorModel):
    Description: str


class HttpPropertiesTypeDef(BaseValidatorModel):
    HttpName: Optional[str] = None


class InstanceSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListInstancesRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class NamespaceFilterTypeDef(BaseValidatorModel):
    Name: NamespaceFilterNameType
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None


class OperationFilterTypeDef(BaseValidatorModel):
    Name: OperationFilterNameType
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None


class OperationSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Status: Optional[OperationStatusType] = None


class ServiceFilterTypeDef(BaseValidatorModel):
    Name: Literal["NAMESPACE_ID"]
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class SOAChangeTypeDef(BaseValidatorModel):
    TTL: int


class RegisterInstanceRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Attributes: Mapping[str, str]
    CreatorRequestId: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateInstanceCustomHealthStatusRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Status: CustomHealthStatusType


class UpdateServiceAttributesRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    Attributes: Mapping[str, str]


class CreateHttpNamespaceRequestTypeDef(BaseValidatorModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateHttpNamespaceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePrivateDnsNamespaceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePublicDnsNamespaceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteNamespaceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterInstanceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DiscoverInstancesRevisionResponseTypeDef(BaseValidatorModel):
    InstancesRevision: int
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstancesHealthStatusResponseTypeDef(BaseValidatorModel):
    Status: Dict[str, HealthStatusType]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterInstanceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateHttpNamespaceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePrivateDnsNamespaceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePublicDnsNamespaceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateServiceResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class HttpInstanceSummaryTypeDef(BaseValidatorModel):
    pass


class DiscoverInstancesResponseTypeDef(BaseValidatorModel):
    Instances: List[HttpInstanceSummaryTypeDef]
    InstancesRevision: int
    ResponseMetadata: ResponseMetadataTypeDef


class DnsRecordTypeDef(BaseValidatorModel):
    pass


class DnsConfigChangeTypeDef(BaseValidatorModel):
    DnsRecords: Sequence[DnsRecordTypeDef]


class DnsConfigOutputTypeDef(BaseValidatorModel):
    DnsRecords: List[DnsRecordTypeDef]
    NamespaceId: Optional[str] = None
    RoutingPolicy: Optional[RoutingPolicyType] = None


class DnsConfigTypeDef(BaseValidatorModel):
    DnsRecords: Sequence[DnsRecordTypeDef]
    NamespaceId: Optional[str] = None
    RoutingPolicy: Optional[RoutingPolicyType] = None


class DnsPropertiesTypeDef(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    SOA: Optional[SOATypeDef] = None


class PrivateDnsPropertiesMutableTypeDef(BaseValidatorModel):
    SOA: SOATypeDef


class PublicDnsPropertiesMutableTypeDef(BaseValidatorModel):
    SOA: SOATypeDef


class GetInstanceResponseTypeDef(BaseValidatorModel):
    Instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OperationTypeDef(BaseValidatorModel):
    pass


class GetOperationResponseTypeDef(BaseValidatorModel):
    Operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetServiceAttributesResponseTypeDef(BaseValidatorModel):
    ServiceAttributes: ServiceAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateHttpNamespaceRequestTypeDef(BaseValidatorModel):
    Id: str
    Namespace: HttpNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None


class ListInstancesResponseTypeDef(BaseValidatorModel):
    Instances: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListInstancesRequestPaginateTypeDef(BaseValidatorModel):
    ServiceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNamespacesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[NamespaceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNamespacesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[NamespaceFilterTypeDef]] = None


class ListOperationsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[OperationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOperationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[OperationFilterTypeDef]] = None


class ListOperationsResponseTypeDef(BaseValidatorModel):
    Operations: List[OperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListServicesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ServiceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[ServiceFilterTypeDef]] = None


class PrivateDnsPropertiesMutableChangeTypeDef(BaseValidatorModel):
    SOA: SOAChangeTypeDef


class PublicDnsPropertiesMutableChangeTypeDef(BaseValidatorModel):
    SOA: SOAChangeTypeDef


class HealthCheckConfigTypeDef(BaseValidatorModel):
    pass


class ServiceChangeTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    DnsConfig: Optional[DnsConfigChangeTypeDef] = None
    HealthCheckConfig: Optional[HealthCheckConfigTypeDef] = None


class NamespacePropertiesTypeDef(BaseValidatorModel):
    DnsProperties: Optional[DnsPropertiesTypeDef] = None
    HttpProperties: Optional[HttpPropertiesTypeDef] = None


class PrivateDnsNamespacePropertiesTypeDef(BaseValidatorModel):
    DnsProperties: PrivateDnsPropertiesMutableTypeDef


class PublicDnsNamespacePropertiesTypeDef(BaseValidatorModel):
    DnsProperties: PublicDnsPropertiesMutableTypeDef


class PrivateDnsNamespacePropertiesChangeTypeDef(BaseValidatorModel):
    DnsProperties: PrivateDnsPropertiesMutableChangeTypeDef


class PublicDnsNamespacePropertiesChangeTypeDef(BaseValidatorModel):
    DnsProperties: PublicDnsPropertiesMutableChangeTypeDef


class UpdateServiceRequestTypeDef(BaseValidatorModel):
    Id: str
    Service: ServiceChangeTypeDef


class ServiceSummaryTypeDef(BaseValidatorModel):
    pass


class ListServicesResponseTypeDef(BaseValidatorModel):
    Services: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ServiceTypeDef(BaseValidatorModel):
    pass


class CreateServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePrivateDnsNamespaceRequestTypeDef(BaseValidatorModel):
    Name: str
    Vpc: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Properties: Optional[PrivateDnsNamespacePropertiesTypeDef] = None


class CreatePublicDnsNamespaceRequestTypeDef(BaseValidatorModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Properties: Optional[PublicDnsNamespacePropertiesTypeDef] = None


class PrivateDnsNamespaceChangeTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Properties: Optional[PrivateDnsNamespacePropertiesChangeTypeDef] = None


class PublicDnsNamespaceChangeTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Properties: Optional[PublicDnsNamespacePropertiesChangeTypeDef] = None


class NamespaceSummaryTypeDef(BaseValidatorModel):
    pass


class ListNamespacesResponseTypeDef(BaseValidatorModel):
    Namespaces: List[NamespaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class NamespaceTypeDef(BaseValidatorModel):
    pass


class GetNamespaceResponseTypeDef(BaseValidatorModel):
    Namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePrivateDnsNamespaceRequestTypeDef(BaseValidatorModel):
    Id: str
    Namespace: PrivateDnsNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None


class UpdatePublicDnsNamespaceRequestTypeDef(BaseValidatorModel):
    Id: str
    Namespace: PublicDnsNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None



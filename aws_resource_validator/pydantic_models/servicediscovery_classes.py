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
from aws_resource_validator.pydantic_models.servicediscovery_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class HealthCheckConfigTypeDef(BaseModel):
    Type: HealthCheckTypeType
    ResourcePath: Optional[str] = None
    FailureThreshold: Optional[int] = None

class HealthCheckCustomConfigTypeDef(BaseModel):
    FailureThreshold: Optional[int] = None

class DeleteNamespaceRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteServiceRequestRequestTypeDef(BaseModel):
    Id: str

class DeregisterInstanceRequestRequestTypeDef(BaseModel):
    ServiceId: str
    InstanceId: str

class DiscoverInstancesRequestRequestTypeDef(BaseModel):
    NamespaceName: str
    ServiceName: str
    MaxResults: Optional[int] = None
    QueryParameters: Optional[Mapping[str, str]] = None
    OptionalParameters: Optional[Mapping[str, str]] = None
    HealthStatus: Optional[HealthStatusFilterType] = None

class HttpInstanceSummaryTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    NamespaceName: Optional[str] = None
    ServiceName: Optional[str] = None
    HealthStatus: Optional[HealthStatusType] = None
    Attributes: Optional[Dict[str, str]] = None

class DiscoverInstancesRevisionRequestRequestTypeDef(BaseModel):
    NamespaceName: str
    ServiceName: str

class DnsRecordTypeDef(BaseModel):
    Type: RecordTypeType
    TTL: int

class SOATypeDef(BaseModel):
    TTL: int

class GetInstanceRequestRequestTypeDef(BaseModel):
    ServiceId: str
    InstanceId: str

class InstanceTypeDef(BaseModel):
    Id: str
    CreatorRequestId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None

class GetInstancesHealthStatusRequestRequestTypeDef(BaseModel):
    ServiceId: str
    Instances: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetNamespaceRequestRequestTypeDef(BaseModel):
    Id: str

class GetOperationRequestRequestTypeDef(BaseModel):
    OperationId: str

class OperationTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[OperationTypeType] = None
    Status: Optional[OperationStatusType] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    CreateDate: Optional[datetime] = None
    UpdateDate: Optional[datetime] = None
    Targets: Optional[Dict[OperationTargetTypeType, str]] = None

class GetServiceRequestRequestTypeDef(BaseModel):
    Id: str

class HttpNamespaceChangeTypeDef(BaseModel):
    Description: str

class HttpPropertiesTypeDef(BaseModel):
    HttpName: Optional[str] = None

class InstanceSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListInstancesRequestRequestTypeDef(BaseModel):
    ServiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class NamespaceFilterTypeDef(BaseModel):
    Name: NamespaceFilterNameType
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None

class OperationFilterTypeDef(BaseModel):
    Name: OperationFilterNameType
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None

class OperationSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Status: Optional[OperationStatusType] = None

class ServiceFilterTypeDef(BaseModel):
    Name: Literal["NAMESPACE_ID"]
    Values: Sequence[str]
    Condition: Optional[FilterConditionType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class SOAChangeTypeDef(BaseModel):
    TTL: int

class RegisterInstanceRequestRequestTypeDef(BaseModel):
    ServiceId: str
    InstanceId: str
    Attributes: Mapping[str, str]
    CreatorRequestId: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateInstanceCustomHealthStatusRequestRequestTypeDef(BaseModel):
    ServiceId: str
    InstanceId: str
    Status: CustomHealthStatusType

class CreateHttpNamespaceRequestRequestTypeDef(BaseModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateHttpNamespaceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePrivateDnsNamespaceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePublicDnsNamespaceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterInstanceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DiscoverInstancesRevisionResponseTypeDef(BaseModel):
    InstancesRevision: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstancesHealthStatusResponseTypeDef(BaseModel):
    Status: Dict[str, HealthStatusType]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterInstanceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHttpNamespaceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePrivateDnsNamespaceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePublicDnsNamespaceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DiscoverInstancesResponseTypeDef(BaseModel):
    Instances: List[HttpInstanceSummaryTypeDef]
    InstancesRevision: int
    ResponseMetadata: ResponseMetadataTypeDef

class DnsConfigChangeTypeDef(BaseModel):
    DnsRecords: Sequence[DnsRecordTypeDef]

class DnsConfigPaginatorTypeDef(BaseModel):
    DnsRecords: List[DnsRecordTypeDef]
    NamespaceId: Optional[str] = None
    RoutingPolicy: Optional[RoutingPolicyType] = None

class DnsConfigTypeDef(BaseModel):
    DnsRecords: Sequence[DnsRecordTypeDef]
    NamespaceId: Optional[str] = None
    RoutingPolicy: Optional[RoutingPolicyType] = None

class DnsPropertiesTypeDef(BaseModel):
    HostedZoneId: Optional[str] = None
    SOA: Optional[SOATypeDef] = None

class PrivateDnsPropertiesMutableTypeDef(BaseModel):
    SOA: SOATypeDef

class PublicDnsPropertiesMutableTypeDef(BaseModel):
    SOA: SOATypeDef

class GetInstanceResponseTypeDef(BaseModel):
    Instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOperationResponseTypeDef(BaseModel):
    Operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHttpNamespaceRequestRequestTypeDef(BaseModel):
    Id: str
    Namespace: HttpNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None

class ListInstancesResponseTypeDef(BaseModel):
    Instances: List[InstanceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstancesRequestListInstancesPaginateTypeDef(BaseModel):
    ServiceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamespacesRequestListNamespacesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[NamespaceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamespacesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[NamespaceFilterTypeDef]] = None

class ListOperationsRequestListOperationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[OperationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[OperationFilterTypeDef]] = None

class ListOperationsResponseTypeDef(BaseModel):
    Operations: List[OperationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesRequestListServicesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[ServiceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[ServiceFilterTypeDef]] = None

class PrivateDnsPropertiesMutableChangeTypeDef(BaseModel):
    SOA: SOAChangeTypeDef

class PublicDnsPropertiesMutableChangeTypeDef(BaseModel):
    SOA: SOAChangeTypeDef

class ServiceChangeTypeDef(BaseModel):
    Description: Optional[str] = None
    DnsConfig: Optional[DnsConfigChangeTypeDef] = None
    HealthCheckConfig: Optional[HealthCheckConfigTypeDef] = None

class ServiceSummaryPaginatorTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ServiceTypeType] = None
    Description: Optional[str] = None
    InstanceCount: Optional[int] = None
    DnsConfig: Optional[DnsConfigPaginatorTypeDef] = None
    HealthCheckConfig: Optional[HealthCheckConfigTypeDef] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfigTypeDef] = None
    CreateDate: Optional[datetime] = None

class CreateServiceRequestRequestTypeDef(BaseModel):
    Name: str
    NamespaceId: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    DnsConfig: Optional[DnsConfigTypeDef] = None
    HealthCheckConfig: Optional[HealthCheckConfigTypeDef] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Type: Optional[Literal["HTTP"]] = None

class ServiceSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ServiceTypeType] = None
    Description: Optional[str] = None
    InstanceCount: Optional[int] = None
    DnsConfig: Optional[DnsConfigTypeDef] = None
    HealthCheckConfig: Optional[HealthCheckConfigTypeDef] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfigTypeDef] = None
    CreateDate: Optional[datetime] = None

class ServiceTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    NamespaceId: Optional[str] = None
    Description: Optional[str] = None
    InstanceCount: Optional[int] = None
    DnsConfig: Optional[DnsConfigTypeDef] = None
    Type: Optional[ServiceTypeType] = None
    HealthCheckConfig: Optional[HealthCheckConfigTypeDef] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfigTypeDef] = None
    CreateDate: Optional[datetime] = None
    CreatorRequestId: Optional[str] = None

class NamespacePropertiesTypeDef(BaseModel):
    DnsProperties: Optional[DnsPropertiesTypeDef] = None
    HttpProperties: Optional[HttpPropertiesTypeDef] = None

class PrivateDnsNamespacePropertiesTypeDef(BaseModel):
    DnsProperties: PrivateDnsPropertiesMutableTypeDef

class PublicDnsNamespacePropertiesTypeDef(BaseModel):
    DnsProperties: PublicDnsPropertiesMutableTypeDef

class PrivateDnsNamespacePropertiesChangeTypeDef(BaseModel):
    DnsProperties: PrivateDnsPropertiesMutableChangeTypeDef

class PublicDnsNamespacePropertiesChangeTypeDef(BaseModel):
    DnsProperties: PublicDnsPropertiesMutableChangeTypeDef

class UpdateServiceRequestRequestTypeDef(BaseModel):
    Id: str
    Service: ServiceChangeTypeDef

class ListServicesResponsePaginatorTypeDef(BaseModel):
    Services: List[ServiceSummaryPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesResponseTypeDef(BaseModel):
    Services: List[ServiceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceResponseTypeDef(BaseModel):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceResponseTypeDef(BaseModel):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class NamespaceSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[NamespaceTypeType] = None
    Description: Optional[str] = None
    ServiceCount: Optional[int] = None
    Properties: Optional[NamespacePropertiesTypeDef] = None
    CreateDate: Optional[datetime] = None

class NamespaceTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[NamespaceTypeType] = None
    Description: Optional[str] = None
    ServiceCount: Optional[int] = None
    Properties: Optional[NamespacePropertiesTypeDef] = None
    CreateDate: Optional[datetime] = None
    CreatorRequestId: Optional[str] = None

class CreatePrivateDnsNamespaceRequestRequestTypeDef(BaseModel):
    Name: str
    Vpc: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Properties: Optional[PrivateDnsNamespacePropertiesTypeDef] = None

class CreatePublicDnsNamespaceRequestRequestTypeDef(BaseModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Properties: Optional[PublicDnsNamespacePropertiesTypeDef] = None

class PrivateDnsNamespaceChangeTypeDef(BaseModel):
    Description: Optional[str] = None
    Properties: Optional[PrivateDnsNamespacePropertiesChangeTypeDef] = None

class PublicDnsNamespaceChangeTypeDef(BaseModel):
    Description: Optional[str] = None
    Properties: Optional[PublicDnsNamespacePropertiesChangeTypeDef] = None

class ListNamespacesResponseTypeDef(BaseModel):
    Namespaces: List[NamespaceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamespaceResponseTypeDef(BaseModel):
    Namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePrivateDnsNamespaceRequestRequestTypeDef(BaseModel):
    Id: str
    Namespace: PrivateDnsNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None

class UpdatePublicDnsNamespaceRequestRequestTypeDef(BaseModel):
    Id: str
    Namespace: PublicDnsNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None


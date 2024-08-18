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

class HealthCheckConfigTypeDef(BaseValidatorModel):
    Type: HealthCheckTypeType
    ResourcePath: Optional[str] = None
    FailureThreshold: Optional[int] = None

class HealthCheckCustomConfigTypeDef(BaseValidatorModel):
    FailureThreshold: Optional[int] = None

class DeleteNamespaceRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeleteServiceRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeregisterInstanceRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    InstanceId: str

class DiscoverInstancesRequestRequestTypeDef(BaseValidatorModel):
    NamespaceName: str
    ServiceName: str
    MaxResults: Optional[int] = None
    QueryParameters: Optional[Mapping[str, str]] = None
    OptionalParameters: Optional[Mapping[str, str]] = None
    HealthStatus: Optional[HealthStatusFilterType] = None

class HttpInstanceSummaryTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    NamespaceName: Optional[str] = None
    ServiceName: Optional[str] = None
    HealthStatus: Optional[HealthStatusType] = None
    Attributes: Optional[Dict[str, str]] = None

class DiscoverInstancesRevisionRequestRequestTypeDef(BaseValidatorModel):
    NamespaceName: str
    ServiceName: str

class DnsRecordTypeDef(BaseValidatorModel):
    Type: RecordTypeType
    TTL: int

class SOATypeDef(BaseValidatorModel):
    TTL: int

class GetInstanceRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    InstanceId: str

class InstanceTypeDef(BaseValidatorModel):
    Id: str
    CreatorRequestId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None

class GetInstancesHealthStatusRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    Instances: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetNamespaceRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class GetOperationRequestRequestTypeDef(BaseValidatorModel):
    OperationId: str

class OperationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[OperationTypeType] = None
    Status: Optional[OperationStatusType] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    CreateDate: Optional[datetime] = None
    UpdateDate: Optional[datetime] = None
    Targets: Optional[Dict[OperationTargetTypeType, str]] = None

class GetServiceRequestRequestTypeDef(BaseValidatorModel):
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

class ListInstancesRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class SOAChangeTypeDef(BaseValidatorModel):
    TTL: int

class RegisterInstanceRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Attributes: Mapping[str, str]
    CreatorRequestId: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateInstanceCustomHealthStatusRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    InstanceId: str
    Status: CustomHealthStatusType

class CreateHttpNamespaceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class DiscoverInstancesResponseTypeDef(BaseValidatorModel):
    Instances: List[HttpInstanceSummaryTypeDef]
    InstancesRevision: int
    ResponseMetadata: ResponseMetadataTypeDef

class DnsConfigChangeTypeDef(BaseValidatorModel):
    DnsRecords: Sequence[DnsRecordTypeDef]

class DnsConfigPaginatorTypeDef(BaseValidatorModel):
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

class GetOperationResponseTypeDef(BaseValidatorModel):
    Operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHttpNamespaceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Namespace: HttpNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None

class ListInstancesResponseTypeDef(BaseValidatorModel):
    Instances: List[InstanceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstancesRequestListInstancesPaginateTypeDef(BaseValidatorModel):
    ServiceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamespacesRequestListNamespacesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[NamespaceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamespacesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[NamespaceFilterTypeDef]] = None

class ListOperationsRequestListOperationsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[OperationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[OperationFilterTypeDef]] = None

class ListOperationsResponseTypeDef(BaseValidatorModel):
    Operations: List[OperationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesRequestListServicesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ServiceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[ServiceFilterTypeDef]] = None

class PrivateDnsPropertiesMutableChangeTypeDef(BaseValidatorModel):
    SOA: SOAChangeTypeDef

class PublicDnsPropertiesMutableChangeTypeDef(BaseValidatorModel):
    SOA: SOAChangeTypeDef

class ServiceChangeTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    DnsConfig: Optional[DnsConfigChangeTypeDef] = None
    HealthCheckConfig: Optional[HealthCheckConfigTypeDef] = None

class ServiceSummaryPaginatorTypeDef(BaseValidatorModel):
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

class CreateServiceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    NamespaceId: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    DnsConfig: Optional[DnsConfigTypeDef] = None
    HealthCheckConfig: Optional[HealthCheckConfigTypeDef] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Type: Optional[Literal["HTTP"]] = None

class ServiceSummaryTypeDef(BaseValidatorModel):
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

class ServiceTypeDef(BaseValidatorModel):
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

class UpdateServiceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Service: ServiceChangeTypeDef

class ListServicesResponsePaginatorTypeDef(BaseValidatorModel):
    Services: List[ServiceSummaryPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesResponseTypeDef(BaseValidatorModel):
    Services: List[ServiceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class NamespaceSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[NamespaceTypeType] = None
    Description: Optional[str] = None
    ServiceCount: Optional[int] = None
    Properties: Optional[NamespacePropertiesTypeDef] = None
    CreateDate: Optional[datetime] = None

class NamespaceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[NamespaceTypeType] = None
    Description: Optional[str] = None
    ServiceCount: Optional[int] = None
    Properties: Optional[NamespacePropertiesTypeDef] = None
    CreateDate: Optional[datetime] = None
    CreatorRequestId: Optional[str] = None

class CreatePrivateDnsNamespaceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Vpc: str
    CreatorRequestId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Properties: Optional[PrivateDnsNamespacePropertiesTypeDef] = None

class CreatePublicDnsNamespaceRequestRequestTypeDef(BaseValidatorModel):
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

class ListNamespacesResponseTypeDef(BaseValidatorModel):
    Namespaces: List[NamespaceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamespaceResponseTypeDef(BaseValidatorModel):
    Namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePrivateDnsNamespaceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Namespace: PrivateDnsNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None

class UpdatePublicDnsNamespaceRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Namespace: PublicDnsNamespaceChangeTypeDef
    UpdaterRequestId: Optional[str] = None


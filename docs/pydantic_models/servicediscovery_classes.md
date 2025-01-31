# Servicediscovery Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateHttpNamespaceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.TagTypeDef]]


# CreateHttpNamespaceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePrivateDnsNamespaceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Vpc
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.TagTypeDef]]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsNamespacePropertiesTypeDef]


# CreatePrivateDnsNamespaceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePublicDnsNamespaceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.TagTypeDef]]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsNamespacePropertiesTypeDef]


# CreatePublicDnsNamespaceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NamespaceId
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DnsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsConfigTypeDef]

### HealthCheckConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckConfigTypeDef]

### HealthCheckCustomConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckCustomConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.TagTypeDef]]

### Type
- **Type**: typing.Optional[typing.Literal['HTTP']]


# CreateServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNamespaceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNamespaceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterInstanceRequestRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterInstanceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DiscoverInstancesRequestRequestTypeDef

### NamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### QueryParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OptionalParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### HealthStatus
- **Type**: typing.Optional[typing.Literal['ALL', 'HEALTHY', 'HEALTHY_OR_ELSE_ALL', 'UNHEALTHY']]


# DiscoverInstancesResponseTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.HttpInstanceSummaryTypeDef]
- **Required**: Yes

### InstancesRevision
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DiscoverInstancesRevisionRequestRequestTypeDef

### NamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# DiscoverInstancesRevisionResponseTypeDef

### InstancesRevision
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DnsConfigChangeTypeDef

### DnsRecords
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsRecordTypeDef]
- **Required**: Yes


# DnsConfigPaginatorTypeDef

### DnsRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsRecordTypeDef]
- **Required**: Yes

### NamespaceId
- **Type**: typing.Optional[str]

### RoutingPolicy
- **Type**: typing.Optional[typing.Literal['MULTIVALUE', 'WEIGHTED']]


# DnsConfigTypeDef

### DnsRecords
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsRecordTypeDef]
- **Required**: Yes

### NamespaceId
- **Type**: typing.Optional[str]

### RoutingPolicy
- **Type**: typing.Optional[typing.Literal['MULTIVALUE', 'WEIGHTED']]


# DnsPropertiesTypeDef

### HostedZoneId
- **Type**: typing.Optional[str]

### SOA
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.SOATypeDef]


# DnsRecordTypeDef

### Type
- **Type**: typing.Literal['A', 'AAAA', 'CNAME', 'SRV']
- **Required**: Yes

### TTL
- **Type**: <class 'int'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceRequestRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceResponseTypeDef

### Instance
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.InstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstancesHealthStatusRequestRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetInstancesHealthStatusResponseTypeDef

### Status
- **Type**: typing.Dict[str, typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNamespaceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetNamespaceResponseTypeDef

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.NamespaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOperationRequestRequestTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOperationResponseTypeDef

### Operation
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HealthCheckConfigTypeDef

### Type
- **Type**: typing.Literal['HTTP', 'HTTPS', 'TCP']
- **Required**: Yes

### ResourcePath
- **Type**: typing.Optional[str]

### FailureThreshold
- **Type**: typing.Optional[int]


# HealthCheckCustomConfigTypeDef

### FailureThreshold
- **Type**: typing.Optional[int]


# HttpInstanceSummaryTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### NamespaceName
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### HealthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# HttpNamespaceChangeTypeDef

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# HttpPropertiesTypeDef

### HttpName
- **Type**: typing.Optional[str]


# InstanceSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# InstanceTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListInstancesRequestListInstancesPaginateTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfigTypeDef]


# ListInstancesRequestRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInstancesResponseTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.InstanceSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNamespacesRequestListNamespacesPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespaceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfigTypeDef]


# ListNamespacesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespaceFilterTypeDef]]


# ListNamespacesResponseTypeDef

### Namespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespaceSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOperationsRequestListOperationsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.OperationFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfigTypeDef]


# ListOperationsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.OperationFilterTypeDef]]


# ListOperationsResponseTypeDef

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.OperationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicesRequestListServicesPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfigTypeDef]


# ListServicesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceFilterTypeDef]]


# ListServicesResponsePaginatorTypeDef

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceSummaryPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicesResponseTypeDef

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NamespaceFilterTypeDef

### Name
- **Type**: typing.Literal['HTTP_NAME', 'NAME', 'TYPE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Condition
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'EQ', 'IN']]


# NamespacePropertiesTypeDef

### DnsProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsPropertiesTypeDef]

### HttpProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HttpPropertiesTypeDef]


# NamespaceSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['DNS_PRIVATE', 'DNS_PUBLIC', 'HTTP']]

### Description
- **Type**: typing.Optional[str]

### ServiceCount
- **Type**: typing.Optional[int]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespacePropertiesTypeDef]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# NamespaceTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['DNS_PRIVATE', 'DNS_PUBLIC', 'HTTP']]

### Description
- **Type**: typing.Optional[str]

### ServiceCount
- **Type**: typing.Optional[int]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespacePropertiesTypeDef]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### CreatorRequestId
- **Type**: typing.Optional[str]


# OperationFilterTypeDef

### Name
- **Type**: typing.Literal['NAMESPACE_ID', 'SERVICE_ID', 'STATUS', 'TYPE', 'UPDATE_DATE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Condition
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'EQ', 'IN']]


# OperationSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAIL', 'PENDING', 'SUBMITTED', 'SUCCESS']]


# OperationTypeDef

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CREATE_NAMESPACE', 'DELETE_NAMESPACE', 'DEREGISTER_INSTANCE', 'REGISTER_INSTANCE', 'UPDATE_NAMESPACE', 'UPDATE_SERVICE']]

### Status
- **Type**: typing.Optional[typing.Literal['FAIL', 'PENDING', 'SUBMITTED', 'SUCCESS']]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### UpdateDate
- **Type**: typing.Optional[datetime.datetime]

### Targets
- **Type**: typing.Optional[typing.Dict[typing.Literal['INSTANCE', 'NAMESPACE', 'SERVICE'], str]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrivateDnsNamespaceChangeTypeDef

### Description
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsNamespacePropertiesChangeTypeDef]


# PrivateDnsNamespacePropertiesChangeTypeDef

### DnsProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsPropertiesMutableChangeTypeDef'>
- **Required**: Yes


# PrivateDnsNamespacePropertiesTypeDef

### DnsProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsPropertiesMutableTypeDef'>
- **Required**: Yes


# PrivateDnsPropertiesMutableChangeTypeDef

### SOA
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.SOAChangeTypeDef'>
- **Required**: Yes


# PrivateDnsPropertiesMutableTypeDef

### SOA
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.SOATypeDef'>
- **Required**: Yes


# PublicDnsNamespaceChangeTypeDef

### Description
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsNamespacePropertiesChangeTypeDef]


# PublicDnsNamespacePropertiesChangeTypeDef

### DnsProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsPropertiesMutableChangeTypeDef'>
- **Required**: Yes


# PublicDnsNamespacePropertiesTypeDef

### DnsProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsPropertiesMutableTypeDef'>
- **Required**: Yes


# PublicDnsPropertiesMutableChangeTypeDef

### SOA
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.SOAChangeTypeDef'>
- **Required**: Yes


# PublicDnsPropertiesMutableTypeDef

### SOA
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.SOATypeDef'>
- **Required**: Yes


# RegisterInstanceRequestRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]


# RegisterInstanceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# SOAChangeTypeDef

### TTL
- **Type**: <class 'int'>
- **Required**: Yes


# SOATypeDef

### TTL
- **Type**: <class 'int'>
- **Required**: Yes


# ServiceChangeTypeDef

### Description
- **Type**: typing.Optional[str]

### DnsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsConfigChangeTypeDef]

### HealthCheckConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckConfigTypeDef]


# ServiceFilterTypeDef

### Name
- **Type**: typing.Literal['NAMESPACE_ID']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Condition
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'EQ', 'IN']]


# ServiceSummaryPaginatorTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['DNS', 'DNS_HTTP', 'HTTP']]

### Description
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### DnsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsConfigPaginatorTypeDef]

### HealthCheckConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckConfigTypeDef]

### HealthCheckCustomConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckCustomConfigTypeDef]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# ServiceSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['DNS', 'DNS_HTTP', 'HTTP']]

### Description
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### DnsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsConfigTypeDef]

### HealthCheckConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckConfigTypeDef]

### HealthCheckCustomConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckCustomConfigTypeDef]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# ServiceTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NamespaceId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### DnsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsConfigTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['DNS', 'DNS_HTTP', 'HTTP']]

### HealthCheckConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckConfigTypeDef]

### HealthCheckCustomConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.HealthCheckCustomConfigTypeDef]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### CreatorRequestId
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateHttpNamespaceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.HttpNamespaceChangeTypeDef'>
- **Required**: Yes

### UpdaterRequestId
- **Type**: typing.Optional[str]


# UpdateHttpNamespaceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInstanceCustomHealthStatusRequestRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes


# UpdatePrivateDnsNamespaceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsNamespaceChangeTypeDef'>
- **Required**: Yes

### UpdaterRequestId
- **Type**: typing.Optional[str]


# UpdatePrivateDnsNamespaceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePublicDnsNamespaceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsNamespaceChangeTypeDef'>
- **Required**: Yes

### UpdaterRequestId
- **Type**: typing.Optional[str]


# UpdatePublicDnsNamespaceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceChangeTypeDef'>
- **Required**: Yes


# UpdateServiceResponseTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



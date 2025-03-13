# Servicediscovery Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateHttpNamespaceRequestTypeDef

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


# CreatePrivateDnsNamespaceRequestTypeDef

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


# CreatePublicDnsNamespaceRequestTypeDef

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


# CreateServiceResponseTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNamespaceRequestTypeDef

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


# DeleteServiceAttributesRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteServiceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterInstanceRequestTypeDef

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


# DnsConfigOutputTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceRequestTypeDef

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


# GetInstancesHealthStatusRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNamespaceRequestTypeDef

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


# GetOperationRequestTypeDef

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


# GetServiceAttributesRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceAttributesResponseTypeDef

### ServiceAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HealthCheckCustomConfigTypeDef

### FailureThreshold
- **Type**: typing.Optional[int]


# HttpInstanceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ListInstancesRequestPaginateTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfigTypeDef]


# ListInstancesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNamespacesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespaceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfigTypeDef]


# ListNamespacesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOperationsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.OperationFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfigTypeDef]


# ListOperationsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfigTypeDef]


# ListServicesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceFilterTypeDef]]


# ListServicesResponseTypeDef

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NamespaceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RegisterInstanceRequestTypeDef

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


# ServiceAttributesTypeDef

### ServiceArn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# ServiceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

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


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateHttpNamespaceRequestTypeDef

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


# UpdateInstanceCustomHealthStatusRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes


# UpdatePrivateDnsNamespaceRequestTypeDef

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


# UpdatePublicDnsNamespaceRequestTypeDef

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


# UpdateServiceAttributesRequestTypeDef

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UpdateServiceRequestTypeDef

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



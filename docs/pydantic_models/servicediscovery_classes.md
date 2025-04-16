# Servicediscovery Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateHttpNamespaceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.Tag]]


# CreateHttpNamespaceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePrivateDnsNamespaceRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.Tag]]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsNamespaceProperties]


# CreatePrivateDnsNamespaceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePublicDnsNamespaceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.Tag]]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsNamespaceProperties]


# CreatePublicDnsNamespaceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceResponse

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNamespaceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNamespaceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceAttributesRequest

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteServiceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterInstanceRequest

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterInstanceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# DiscoverInstancesResponse

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.HttpInstanceSummary]
- **Required**: Yes

### InstancesRevision
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# DiscoverInstancesRevisionResponse

### InstancesRevision
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# DnsConfig

### DnsRecords
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsRecord]
- **Required**: Yes

### NamespaceId
- **Type**: typing.Optional[str]

### RoutingPolicy
- **Type**: typing.Optional[typing.Literal['MULTIVALUE', 'WEIGHTED']]


# DnsConfigChange

### DnsRecords
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsRecord]
- **Required**: Yes


# DnsConfigOutput

### DnsRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsRecord]
- **Required**: Yes

### NamespaceId
- **Type**: typing.Optional[str]

### RoutingPolicy
- **Type**: typing.Optional[typing.Literal['MULTIVALUE', 'WEIGHTED']]


# DnsProperties

### HostedZoneId
- **Type**: typing.Optional[str]

### SOA
- **Type**: <class 'NoneType'>


# DnsRecord

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceRequest

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceResponse

### Instance
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.Instance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstancesHealthStatusRequest

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetInstancesHealthStatusResponse

### Status
- **Type**: typing.Dict[str, typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNamespaceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetNamespaceResponse

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.Namespace'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# GetOperationRequest

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOperationResponse

### Operation
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceAttributesRequest

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceAttributesResponse

### ServiceAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceResponse

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# HealthCheckConfig

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HealthCheckCustomConfig

### FailureThreshold
- **Type**: typing.Optional[int]


# HttpInstanceSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HttpNamespaceChange

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# HttpProperties

### HttpName
- **Type**: typing.Optional[str]


# Instance

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# InstanceSummary

### Id
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListInstancesRequest

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInstancesRequestPaginate

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfig]


# ListInstancesResponse

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.InstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNamespacesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespaceFilter]]


# ListNamespacesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespaceFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfig]


# ListNamespacesResponse

### Namespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.NamespaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOperationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.OperationFilter]]


# ListOperationsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.OperationFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfig]


# ListOperationsResponse

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.OperationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceFilter]]


# ListServicesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PaginatorConfig]


# ListServicesResponse

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicediscovery_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# Namespace

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NamespaceFilter

### Name
- **Type**: typing.Literal['HTTP_NAME', 'NAME', 'TYPE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Condition
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'EQ', 'IN']]


# NamespaceProperties

### DnsProperties
- **Type**: <class 'NoneType'>

### HttpProperties
- **Type**: <class 'NoneType'>


# NamespaceSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Operation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OperationFilter

### Name
- **Type**: typing.Literal['NAMESPACE_ID', 'SERVICE_ID', 'STATUS', 'TYPE', 'UPDATE_DATE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Condition
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'EQ', 'IN']]


# OperationSummary

### Id
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAIL', 'PENDING', 'SUBMITTED', 'SUCCESS']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrivateDnsNamespaceChange

### Description
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsNamespacePropertiesChange]


# PrivateDnsNamespaceProperties

### DnsProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsPropertiesMutable'>
- **Required**: Yes


# PrivateDnsNamespacePropertiesChange

### DnsProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsPropertiesMutableChange'>
- **Required**: Yes


# PrivateDnsPropertiesMutable

### SOA
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.SOA'>
- **Required**: Yes


# PrivateDnsPropertiesMutableChange

### SOA
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.SOAChange'>
- **Required**: Yes


# PublicDnsNamespaceChange

### Description
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsNamespacePropertiesChange]


# PublicDnsNamespaceProperties

### DnsProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsPropertiesMutable'>
- **Required**: Yes


# PublicDnsNamespacePropertiesChange

### DnsProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsPropertiesMutableChange'>
- **Required**: Yes


# PublicDnsPropertiesMutable

### SOA
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.SOA'>
- **Required**: Yes


# PublicDnsPropertiesMutableChange

### SOA
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.SOAChange'>
- **Required**: Yes


# RegisterInstanceRequest

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


# RegisterInstanceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# ResponseMetadata

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


# SOA

### TTL
- **Type**: <class 'int'>
- **Required**: Yes


# SOAChange

### TTL
- **Type**: <class 'int'>
- **Required**: Yes


# Service

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceAttributes

### ServiceArn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# ServiceChange

### Description
- **Type**: typing.Optional[str]

### DnsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicediscovery_classes.DnsConfigChange]

### HealthCheckConfig
- **Type**: <class 'NoneType'>


# ServiceFilter

### Name
- **Type**: typing.Literal['NAMESPACE_ID']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Condition
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'EQ', 'IN']]


# ServiceSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.servicediscovery_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateHttpNamespaceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.HttpNamespaceChange'>
- **Required**: Yes

### UpdaterRequestId
- **Type**: typing.Optional[str]


# UpdateHttpNamespaceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInstanceCustomHealthStatusRequest

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes


# UpdatePrivateDnsNamespaceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PrivateDnsNamespaceChange'>
- **Required**: Yes

### UpdaterRequestId
- **Type**: typing.Optional[str]


# UpdatePrivateDnsNamespaceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePublicDnsNamespaceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.PublicDnsNamespaceChange'>
- **Required**: Yes

### UpdaterRequestId
- **Type**: typing.Optional[str]


# UpdatePublicDnsNamespaceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceAttributesRequest

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UpdateServiceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ServiceChange'>
- **Required**: Yes


# UpdateServiceResponse

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicediscovery_classes.ResponseMetadata'>
- **Required**: Yes



# Globalaccelerator Classes

# Accelerator

### AcceleratorArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### Enabled
- **Type**: typing.Optional[bool]

### IpSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.IpSet]]

### DnsName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'IN_PROGRESS']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### DualStackDnsName
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorEvent]]


# AcceleratorAttributes

### FlowLogsEnabled
- **Type**: typing.Optional[bool]

### FlowLogsS3Bucket
- **Type**: typing.Optional[str]

### FlowLogsS3Prefix
- **Type**: typing.Optional[str]


# AcceleratorEvent

### Message
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# AddCustomRoutingEndpointsRequest

### EndpointConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointConfiguration]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# AddCustomRoutingEndpointsResponse

### EndpointDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointDescription]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# AddEndpointsRequest

### EndpointConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointConfiguration]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# AddEndpointsResponse

### EndpointDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointDescription]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# AdvertiseByoipCidrRequest

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes


# AdvertiseByoipCidrResponse

### ByoipCidr
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidr'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# AllowCustomRoutingTrafficRequest

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### DestinationPorts
- **Type**: typing.Optional[typing.Sequence[int]]

### AllowAllTrafficToEndpoint
- **Type**: typing.Optional[bool]


# Attachment

### AttachmentArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Principals
- **Type**: typing.Optional[typing.List[str]]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.Resource]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByoipCidr

### Cidr
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ADVERTISING', 'DEPROVISIONED', 'FAILED_ADVERTISING', 'FAILED_DEPROVISION', 'FAILED_PROVISION', 'FAILED_WITHDRAW', 'PENDING_ADVERTISING', 'PENDING_DEPROVISIONING', 'PENDING_PROVISIONING', 'PENDING_WITHDRAWING', 'READY']]

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidrEvent]]


# ByoipCidrEvent

### Message
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# CidrAuthorizationContext

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Signature
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAcceleratorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### IpAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.Tag]]


# CreateAcceleratorResponse

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Accelerator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCrossAccountAttachmentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### Principals
- **Type**: typing.Optional[typing.Sequence[str]]

### Resources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.Resource]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.Tag]]


# CreateCrossAccountAttachmentResponse

### CrossAccountAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Attachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomRoutingAcceleratorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### IpAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.Tag]]


# CreateCustomRoutingAcceleratorResponse

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAccelerator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomRoutingEndpointGroupRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointGroupRegion
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingDestinationConfiguration]
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomRoutingEndpointGroupResponse

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomRoutingListenerRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PortRanges
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRange]
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomRoutingListenerResponse

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingListener'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEndpointGroupRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointGroupRegion
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointConfiguration]]

### TrafficDialPercentage
- **Type**: typing.Optional[float]

### HealthCheckPort
- **Type**: typing.Optional[int]

### HealthCheckProtocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS', 'TCP']]

### HealthCheckPath
- **Type**: typing.Optional[str]

### HealthCheckIntervalSeconds
- **Type**: typing.Optional[int]

### ThresholdCount
- **Type**: typing.Optional[int]

### PortOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortOverride]]


# CreateEndpointGroupResponse

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateListenerResponse

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Listener'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# CrossAccountResource

### EndpointId
- **Type**: typing.Optional[str]

### Cidr
- **Type**: typing.Optional[str]

### AttachmentArn
- **Type**: typing.Optional[str]


# CustomRoutingAccelerator

### AcceleratorArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### Enabled
- **Type**: typing.Optional[bool]

### IpSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.IpSet]]

### DnsName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'IN_PROGRESS']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# CustomRoutingAcceleratorAttributes

### FlowLogsEnabled
- **Type**: typing.Optional[bool]

### FlowLogsS3Bucket
- **Type**: typing.Optional[str]

### FlowLogsS3Prefix
- **Type**: typing.Optional[str]


# CustomRoutingDestinationConfiguration

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes

### Protocols
- **Type**: typing.Sequence[typing.Literal['TCP', 'UDP']]
- **Required**: Yes


# CustomRoutingDestinationDescription

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['TCP', 'UDP']]]


# CustomRoutingEndpointConfiguration

### EndpointId
- **Type**: typing.Optional[str]

### AttachmentArn
- **Type**: typing.Optional[str]


# CustomRoutingEndpointDescription

### EndpointId
- **Type**: typing.Optional[str]


# CustomRoutingEndpointGroup

### EndpointGroupArn
- **Type**: typing.Optional[str]

### EndpointGroupRegion
- **Type**: typing.Optional[str]

### DestinationDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingDestinationDescription]]

### EndpointDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointDescription]]


# CustomRoutingListener

### ListenerArn
- **Type**: typing.Optional[str]

### PortRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRange]]


# DeleteAcceleratorRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCrossAccountAttachmentRequest

### AttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingAcceleratorRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingEndpointGroupRequest

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingListenerRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointGroupRequest

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListenerRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DenyCustomRoutingTrafficRequest

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### DestinationPorts
- **Type**: typing.Optional[typing.Sequence[int]]

### DenyAllTrafficToEndpoint
- **Type**: typing.Optional[bool]


# DeprovisionByoipCidrRequest

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes


# DeprovisionByoipCidrResponse

### ByoipCidr
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidr'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAcceleratorAttributesRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAcceleratorAttributesResponse

### AcceleratorAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAcceleratorRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAcceleratorResponse

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Accelerator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCrossAccountAttachmentRequest

### AttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCrossAccountAttachmentResponse

### CrossAccountAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Attachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomRoutingAcceleratorAttributesRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomRoutingAcceleratorAttributesResponse

### AcceleratorAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAcceleratorAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomRoutingAcceleratorRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomRoutingAcceleratorResponse

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAccelerator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomRoutingEndpointGroupRequest

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomRoutingEndpointGroupResponse

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomRoutingListenerRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomRoutingListenerResponse

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingListener'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointGroupRequest

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointGroupResponse

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeListenerRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeListenerResponse

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Listener'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationPortMapping

### AcceleratorArn
- **Type**: typing.Optional[str]

### AcceleratorSocketAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.SocketAddress]]

### EndpointGroupArn
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### EndpointGroupRegion
- **Type**: typing.Optional[str]

### DestinationSocketAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.SocketAddress]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### DestinationTrafficState
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointConfiguration

### EndpointId
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]

### ClientIPPreservationEnabled
- **Type**: typing.Optional[bool]

### AttachmentArn
- **Type**: typing.Optional[str]


# EndpointDescription

### EndpointId
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]

### HealthState
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'INITIAL', 'UNHEALTHY']]

### HealthReason
- **Type**: typing.Optional[str]

### ClientIPPreservationEnabled
- **Type**: typing.Optional[bool]


# EndpointGroup

### EndpointGroupArn
- **Type**: typing.Optional[str]

### EndpointGroupRegion
- **Type**: typing.Optional[str]

### EndpointDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointDescription]]

### TrafficDialPercentage
- **Type**: typing.Optional[float]

### HealthCheckPort
- **Type**: typing.Optional[int]

### HealthCheckProtocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS', 'TCP']]

### HealthCheckPath
- **Type**: typing.Optional[str]

### HealthCheckIntervalSeconds
- **Type**: typing.Optional[int]

### ThresholdCount
- **Type**: typing.Optional[int]

### PortOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortOverride]]


# EndpointIdentifier

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientIPPreservationEnabled
- **Type**: typing.Optional[bool]


# IpSet

### IpFamily
- **Type**: typing.Optional[str]

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]

### IpAddressFamily
- **Type**: typing.Optional[typing.Literal['IPv4', 'IPv6']]


# ListAcceleratorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAcceleratorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListAcceleratorsResponse

### Accelerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.Accelerator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListByoipCidrsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListByoipCidrsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListByoipCidrsResponse

### ByoipCidrs
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidr]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAttachmentsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAttachmentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListCrossAccountAttachmentsResponse

### CrossAccountAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.Attachment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountResourceAccountsResponse

### ResourceOwnerAwsAccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# ListCrossAccountResourcesRequest

### ResourceOwnerAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceleratorArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountResourcesRequestPaginate

### ResourceOwnerAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceleratorArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListCrossAccountResourcesResponse

### CrossAccountResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CrossAccountResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingAcceleratorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingAcceleratorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListCustomRoutingAcceleratorsResponse

### Accelerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAccelerator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingEndpointGroupsRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingEndpointGroupsRequestPaginate

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListCustomRoutingEndpointGroupsResponse

### EndpointGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingListenersRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingListenersRequestPaginate

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListCustomRoutingListenersResponse

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingListener]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingPortMappingsByDestinationRequest

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationAddress
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingPortMappingsByDestinationRequestPaginate

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationAddress
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListCustomRoutingPortMappingsByDestinationResponse

### DestinationPortMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.DestinationPortMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingPortMappingsRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointGroupArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingPortMappingsRequestPaginate

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListCustomRoutingPortMappingsResponse

### PortMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointGroupsRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointGroupsRequestPaginate

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListEndpointGroupsResponse

### EndpointGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListListenersRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListListenersRequestPaginate

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfig]


# ListListenersResponse

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.Listener]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# Listener

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortMapping

### AcceleratorPort
- **Type**: typing.Optional[int]

### EndpointGroupArn
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### DestinationSocketAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.SocketAddress]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['TCP', 'UDP']]]

### DestinationTrafficState
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


# PortOverride

### ListenerPort
- **Type**: typing.Optional[int]

### EndpointPort
- **Type**: typing.Optional[int]


# PortRange

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]


# ProvisionByoipCidrRequest

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes

### CidrAuthorizationContext
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CidrAuthorizationContext'>
- **Required**: Yes


# ProvisionByoipCidrResponse

### ByoipCidr
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidr'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveCustomRoutingEndpointsRequest

### EndpointIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveEndpointsRequest

### EndpointIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointIdentifier]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# Resource

### EndpointId
- **Type**: typing.Optional[str]

### Cidr
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


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


# SocketAddress

### IpAddress
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAcceleratorAttributesRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowLogsEnabled
- **Type**: typing.Optional[bool]

### FlowLogsS3Bucket
- **Type**: typing.Optional[str]

### FlowLogsS3Prefix
- **Type**: typing.Optional[str]


# UpdateAcceleratorAttributesResponse

### AcceleratorAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAcceleratorRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### IpAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]


# UpdateAcceleratorResponse

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Accelerator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCrossAccountAttachmentRequest

### AttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AddPrincipals
- **Type**: typing.Optional[typing.Sequence[str]]

### RemovePrincipals
- **Type**: typing.Optional[typing.Sequence[str]]

### AddResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.Resource]]

### RemoveResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.Resource]]


# UpdateCrossAccountAttachmentResponse

### CrossAccountAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Attachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCustomRoutingAcceleratorAttributesRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowLogsEnabled
- **Type**: typing.Optional[bool]

### FlowLogsS3Bucket
- **Type**: typing.Optional[str]

### FlowLogsS3Prefix
- **Type**: typing.Optional[str]


# UpdateCustomRoutingAcceleratorAttributesResponse

### AcceleratorAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAcceleratorAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCustomRoutingAcceleratorRequest

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### IpAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]


# UpdateCustomRoutingAcceleratorResponse

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAccelerator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCustomRoutingListenerRequest

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PortRanges
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRange]
- **Required**: Yes


# UpdateCustomRoutingListenerResponse

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingListener'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEndpointGroupRequest

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointConfiguration]]

### TrafficDialPercentage
- **Type**: typing.Optional[float]

### HealthCheckPort
- **Type**: typing.Optional[int]

### HealthCheckProtocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS', 'TCP']]

### HealthCheckPath
- **Type**: typing.Optional[str]

### HealthCheckIntervalSeconds
- **Type**: typing.Optional[int]

### ThresholdCount
- **Type**: typing.Optional[int]

### PortOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortOverride]]


# UpdateEndpointGroupResponse

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateListenerResponse

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.Listener'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes


# WithdrawByoipCidrRequest

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes


# WithdrawByoipCidrResponse

### ByoipCidr
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidr'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadata'>
- **Required**: Yes



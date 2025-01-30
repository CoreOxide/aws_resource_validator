# globalaccelerator_classes

# AcceleratorAttributesTypeDef

### FlowLogsEnabled
- **Type**: typing.Optional[bool]

### FlowLogsS3Bucket
- **Type**: typing.Optional[str]

### FlowLogsS3Prefix
- **Type**: typing.Optional[str]


# AcceleratorEventTypeDef

### Message
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# AcceleratorTypeDef

### AcceleratorArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### Enabled
- **Type**: typing.Optional[bool]

### IpSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.IpSetTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorEventTypeDef]]


# AddCustomRoutingEndpointsRequestRequestTypeDef

### EndpointConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointConfigurationTypeDef]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# AddCustomRoutingEndpointsResponseTypeDef

### EndpointDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointDescriptionTypeDef]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddEndpointsRequestRequestTypeDef

### EndpointConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointConfigurationTypeDef]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# AddEndpointsResponseTypeDef

### EndpointDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointDescriptionTypeDef]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdvertiseByoipCidrRequestRequestTypeDef

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes


# AdvertiseByoipCidrResponseTypeDef

### ByoipCidr
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidrTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AllowCustomRoutingTrafficRequestRequestTypeDef

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


# AttachmentTypeDef

### AttachmentArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Principals
- **Type**: typing.Optional[typing.List[str]]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.ResourceTypeDef]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByoipCidrEventTypeDef

### Message
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# ByoipCidrTypeDef

### Cidr
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ADVERTISING', 'DEPROVISIONED', 'FAILED_ADVERTISING', 'FAILED_DEPROVISION', 'FAILED_PROVISION', 'FAILED_WITHDRAW', 'PENDING_ADVERTISING', 'PENDING_DEPROVISIONING', 'PENDING_PROVISIONING', 'PENDING_WITHDRAWING', 'READY']]

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidrEventTypeDef]]


# CidrAuthorizationContextTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Signature
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAcceleratorRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.TagTypeDef]]


# CreateAcceleratorResponseTypeDef

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCrossAccountAttachmentRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### Principals
- **Type**: typing.Optional[typing.Sequence[str]]

### Resources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.ResourceTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.TagTypeDef]]


# CreateCrossAccountAttachmentResponseTypeDef

### CrossAccountAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomRoutingAcceleratorRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.TagTypeDef]]


# CreateCustomRoutingAcceleratorResponseTypeDef

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAcceleratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomRoutingEndpointGroupRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointGroupRegion
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingDestinationConfigurationTypeDef]
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomRoutingEndpointGroupResponseTypeDef

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomRoutingListenerRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PortRanges
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRangeTypeDef]
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomRoutingListenerResponseTypeDef

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingListenerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEndpointGroupRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointConfigurationTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortOverrideTypeDef]]


# CreateEndpointGroupResponseTypeDef

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateListenerRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PortRanges
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRangeTypeDef]
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['TCP', 'UDP']
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClientAffinity
- **Type**: typing.Optional[typing.Literal['NONE', 'SOURCE_IP']]


# CreateListenerResponseTypeDef

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ListenerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CrossAccountResourceTypeDef

### EndpointId
- **Type**: typing.Optional[str]

### Cidr
- **Type**: typing.Optional[str]

### AttachmentArn
- **Type**: typing.Optional[str]


# CustomRoutingAcceleratorAttributesTypeDef

### FlowLogsEnabled
- **Type**: typing.Optional[bool]

### FlowLogsS3Bucket
- **Type**: typing.Optional[str]

### FlowLogsS3Prefix
- **Type**: typing.Optional[str]


# CustomRoutingAcceleratorTypeDef

### AcceleratorArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### Enabled
- **Type**: typing.Optional[bool]

### IpSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.IpSetTypeDef]]

### DnsName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'IN_PROGRESS']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# CustomRoutingDestinationConfigurationTypeDef

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes

### Protocols
- **Type**: typing.Sequence[typing.Literal['TCP', 'UDP']]
- **Required**: Yes


# CustomRoutingDestinationDescriptionTypeDef

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['TCP', 'UDP']]]


# CustomRoutingEndpointConfigurationTypeDef

### EndpointId
- **Type**: typing.Optional[str]

### AttachmentArn
- **Type**: typing.Optional[str]


# CustomRoutingEndpointDescriptionTypeDef

### EndpointId
- **Type**: typing.Optional[str]


# CustomRoutingEndpointGroupTypeDef

### EndpointGroupArn
- **Type**: typing.Optional[str]

### EndpointGroupRegion
- **Type**: typing.Optional[str]

### DestinationDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingDestinationDescriptionTypeDef]]

### EndpointDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointDescriptionTypeDef]]


# CustomRoutingListenerTypeDef

### ListenerArn
- **Type**: typing.Optional[str]

### PortRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRangeTypeDef]]


# DeleteAcceleratorRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCrossAccountAttachmentRequestRequestTypeDef

### AttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingAcceleratorRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingEndpointGroupRequestRequestTypeDef

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingListenerRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointGroupRequestRequestTypeDef

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListenerRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DenyCustomRoutingTrafficRequestRequestTypeDef

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


# DeprovisionByoipCidrRequestRequestTypeDef

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes


# DeprovisionByoipCidrResponseTypeDef

### ByoipCidr
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidrTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAcceleratorAttributesRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAcceleratorAttributesResponseTypeDef

### AcceleratorAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAcceleratorRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAcceleratorResponseTypeDef

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCrossAccountAttachmentRequestRequestTypeDef

### AttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCrossAccountAttachmentResponseTypeDef

### CrossAccountAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomRoutingAcceleratorAttributesRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomRoutingAcceleratorAttributesResponseTypeDef

### AcceleratorAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAcceleratorAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomRoutingAcceleratorRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomRoutingAcceleratorResponseTypeDef

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAcceleratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomRoutingEndpointGroupRequestRequestTypeDef

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomRoutingEndpointGroupResponseTypeDef

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomRoutingListenerRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomRoutingListenerResponseTypeDef

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingListenerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointGroupRequestRequestTypeDef

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointGroupResponseTypeDef

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeListenerRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeListenerResponseTypeDef

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ListenerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationPortMappingTypeDef

### AcceleratorArn
- **Type**: typing.Optional[str]

### AcceleratorSocketAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.SocketAddressTypeDef]]

### EndpointGroupArn
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### EndpointGroupRegion
- **Type**: typing.Optional[str]

### DestinationSocketAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.SocketAddressTypeDef]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['DUAL_STACK', 'IPV4']]

### DestinationTrafficState
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointConfigurationTypeDef

### EndpointId
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]

### ClientIPPreservationEnabled
- **Type**: typing.Optional[bool]

### AttachmentArn
- **Type**: typing.Optional[str]


# EndpointDescriptionTypeDef

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


# EndpointGroupTypeDef

### EndpointGroupArn
- **Type**: typing.Optional[str]

### EndpointGroupRegion
- **Type**: typing.Optional[str]

### EndpointDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointDescriptionTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortOverrideTypeDef]]


# EndpointIdentifierTypeDef

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientIPPreservationEnabled
- **Type**: typing.Optional[bool]


# IpSetTypeDef

### IpFamily
- **Type**: typing.Optional[str]

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]

### IpAddressFamily
- **Type**: typing.Optional[typing.Literal['IPv4', 'IPv6']]


# ListAcceleratorsRequestListAcceleratorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListAcceleratorsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAcceleratorsResponseTypeDef

### Accelerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListByoipCidrsRequestListByoipCidrsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListByoipCidrsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListByoipCidrsResponseTypeDef

### ByoipCidrs
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidrTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAttachmentsRequestListCrossAccountAttachmentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCrossAccountAttachmentsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAttachmentsResponseTypeDef

### CrossAccountAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.AttachmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountResourceAccountsResponseTypeDef

### ResourceOwnerAwsAccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCrossAccountResourcesRequestListCrossAccountResourcesPaginateTypeDef

### ResourceOwnerAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceleratorArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCrossAccountResourcesRequestRequestTypeDef

### ResourceOwnerAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceleratorArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountResourcesResponseTypeDef

### CrossAccountResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CrossAccountResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingAcceleratorsRequestListCustomRoutingAcceleratorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingAcceleratorsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingAcceleratorsResponseTypeDef

### Accelerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAcceleratorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingEndpointGroupsRequestListCustomRoutingEndpointGroupsPaginateTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingEndpointGroupsRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingEndpointGroupsResponseTypeDef

### EndpointGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingEndpointGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingListenersRequestListCustomRoutingListenersPaginateTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingListenersRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingListenersResponseTypeDef

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingListenerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingPortMappingsByDestinationRequestListCustomRoutingPortMappingsByDestinationPaginateTypeDef

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationAddress
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef

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


# ListCustomRoutingPortMappingsByDestinationResponseTypeDef

### DestinationPortMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.DestinationPortMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingPortMappingsRequestListCustomRoutingPortMappingsPaginateTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingPortMappingsRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointGroupArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomRoutingPortMappingsResponseTypeDef

### PortMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointGroupsRequestListEndpointGroupsPaginateTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListEndpointGroupsRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointGroupsResponseTypeDef

### EndpointGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListListenersRequestListListenersPaginateTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListListenersRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListListenersResponseTypeDef

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.ListenerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListenerTypeDef

### ListenerArn
- **Type**: typing.Optional[str]

### PortRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRangeTypeDef]]

### Protocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### ClientAffinity
- **Type**: typing.Optional[typing.Literal['NONE', 'SOURCE_IP']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortMappingTypeDef

### AcceleratorPort
- **Type**: typing.Optional[int]

### EndpointGroupArn
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### DestinationSocketAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.SocketAddressTypeDef]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['TCP', 'UDP']]]

### DestinationTrafficState
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


# PortOverrideTypeDef

### ListenerPort
- **Type**: typing.Optional[int]

### EndpointPort
- **Type**: typing.Optional[int]


# PortRangeTypeDef

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]


# ProvisionByoipCidrRequestRequestTypeDef

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes

### CidrAuthorizationContext
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CidrAuthorizationContextTypeDef'>
- **Required**: Yes


# ProvisionByoipCidrResponseTypeDef

### ByoipCidr
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidrTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveCustomRoutingEndpointsRequestRequestTypeDef

### EndpointIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveEndpointsRequestRequestTypeDef

### EndpointIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointIdentifierTypeDef]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceTypeDef

### EndpointId
- **Type**: typing.Optional[str]

### Cidr
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


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


# SocketAddressTypeDef

### IpAddress
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAcceleratorAttributesRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowLogsEnabled
- **Type**: typing.Optional[bool]

### FlowLogsS3Bucket
- **Type**: typing.Optional[str]

### FlowLogsS3Prefix
- **Type**: typing.Optional[str]


# UpdateAcceleratorAttributesResponseTypeDef

### AcceleratorAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAcceleratorRequestRequestTypeDef

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


# UpdateAcceleratorResponseTypeDef

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AcceleratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCrossAccountAttachmentRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.ResourceTypeDef]]

### RemoveResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.ResourceTypeDef]]


# UpdateCrossAccountAttachmentResponseTypeDef

### CrossAccountAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.AttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowLogsEnabled
- **Type**: typing.Optional[bool]

### FlowLogsS3Bucket
- **Type**: typing.Optional[str]

### FlowLogsS3Prefix
- **Type**: typing.Optional[str]


# UpdateCustomRoutingAcceleratorAttributesResponseTypeDef

### AcceleratorAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAcceleratorAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCustomRoutingAcceleratorRequestRequestTypeDef

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


# UpdateCustomRoutingAcceleratorResponseTypeDef

### Accelerator
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingAcceleratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCustomRoutingListenerRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PortRanges
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRangeTypeDef]
- **Required**: Yes


# UpdateCustomRoutingListenerResponseTypeDef

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.CustomRoutingListenerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEndpointGroupRequestRequestTypeDef

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointConfigurationTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortOverrideTypeDef]]


# UpdateEndpointGroupResponseTypeDef

### EndpointGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.EndpointGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateListenerRequestRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PortRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.globalaccelerator_classes.PortRangeTypeDef]]

### Protocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### ClientAffinity
- **Type**: typing.Optional[typing.Literal['NONE', 'SOURCE_IP']]


# UpdateListenerResponseTypeDef

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ListenerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WithdrawByoipCidrRequestRequestTypeDef

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes


# WithdrawByoipCidrResponseTypeDef

### ByoipCidr
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ByoipCidrTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



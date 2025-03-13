# Globalaccelerator Classes

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


# AddCustomRoutingEndpointsRequestTypeDef

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


# AddEndpointsRequestTypeDef

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


# AdvertiseByoipCidrRequestTypeDef

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


# AllowCustomRoutingTrafficRequestTypeDef

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


# CreateAcceleratorRequestTypeDef

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


# CreateCrossAccountAttachmentRequestTypeDef

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


# CreateCustomRoutingAcceleratorRequestTypeDef

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


# CreateCustomRoutingEndpointGroupRequestTypeDef

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


# CreateCustomRoutingListenerRequestTypeDef

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


# CreateEndpointGroupRequestTypeDef

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


# DeleteAcceleratorRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCrossAccountAttachmentRequestTypeDef

### AttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingAcceleratorRequestTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingEndpointGroupRequestTypeDef

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomRoutingListenerRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointGroupRequestTypeDef

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListenerRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DenyCustomRoutingTrafficRequestTypeDef

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


# DeprovisionByoipCidrRequestTypeDef

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


# DescribeAcceleratorAttributesRequestTypeDef

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


# DescribeAcceleratorRequestTypeDef

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


# DescribeCrossAccountAttachmentRequestTypeDef

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


# DescribeCustomRoutingAcceleratorAttributesRequestTypeDef

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


# DescribeCustomRoutingAcceleratorRequestTypeDef

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


# DescribeCustomRoutingEndpointGroupRequestTypeDef

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


# DescribeCustomRoutingListenerRequestTypeDef

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


# DescribeEndpointGroupRequestTypeDef

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


# DescribeListenerRequestTypeDef

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


# ListAcceleratorsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListAcceleratorsRequestTypeDef

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


# ListByoipCidrsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListByoipCidrsRequestTypeDef

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


# ListCrossAccountAttachmentsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCrossAccountAttachmentsRequestTypeDef

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


# ListCrossAccountResourcesRequestPaginateTypeDef

### ResourceOwnerAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceleratorArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCrossAccountResourcesRequestTypeDef

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


# ListCustomRoutingAcceleratorsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingAcceleratorsRequestTypeDef

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


# ListCustomRoutingEndpointGroupsRequestPaginateTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingEndpointGroupsRequestTypeDef

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


# ListCustomRoutingListenersRequestPaginateTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingListenersRequestTypeDef

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


# ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationAddress
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingPortMappingsByDestinationRequestTypeDef

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


# ListCustomRoutingPortMappingsRequestPaginateTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListCustomRoutingPortMappingsRequestTypeDef

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


# ListEndpointGroupsRequestPaginateTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListEndpointGroupsRequestTypeDef

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


# ListListenersRequestPaginateTypeDef

### AcceleratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.globalaccelerator_classes.PaginatorConfigTypeDef]


# ListListenersRequestTypeDef

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


# ListTagsForResourceRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ProvisionByoipCidrRequestTypeDef

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


# RemoveCustomRoutingEndpointsRequestTypeDef

### EndpointIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### EndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveEndpointsRequestTypeDef

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


# TagResourceRequestTypeDef

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


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAcceleratorAttributesRequestTypeDef

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


# UpdateAcceleratorRequestTypeDef

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


# UpdateCrossAccountAttachmentRequestTypeDef

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


# UpdateCustomRoutingAcceleratorAttributesRequestTypeDef

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


# UpdateCustomRoutingAcceleratorRequestTypeDef

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


# UpdateCustomRoutingListenerRequestTypeDef

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


# UpdateEndpointGroupRequestTypeDef

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


# UpdateListenerResponseTypeDef

### Listener
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ListenerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.globalaccelerator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WithdrawByoipCidrRequestTypeDef

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



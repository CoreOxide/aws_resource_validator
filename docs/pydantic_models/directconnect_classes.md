# Directconnect Classes

# AcceptDirectConnectGatewayAssociationProposalRequest

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### proposalId
- **Type**: <class 'str'>
- **Required**: Yes

### associatedGatewayOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### overrideAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]


# AcceptDirectConnectGatewayAssociationProposalResult

### directConnectGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AllocateConnectionOnInterconnectRequest

### bandwidth
- **Type**: <class 'str'>
- **Required**: Yes

### connectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### interconnectId
- **Type**: <class 'str'>
- **Required**: Yes

### vlan
- **Type**: <class 'int'>
- **Required**: Yes


# AllocateHostedConnectionRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### bandwidth
- **Type**: <class 'str'>
- **Required**: Yes

### connectionName
- **Type**: <class 'str'>
- **Required**: Yes

### vlan
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]


# AllocatePrivateVirtualInterfaceRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### newPrivateVirtualInterfaceAllocation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.NewPrivateVirtualInterfaceAllocation'>
- **Required**: Yes


# AllocatePublicVirtualInterfaceRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### newPublicVirtualInterfaceAllocation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.NewPublicVirtualInterfaceAllocation'>
- **Required**: Yes


# AllocateTransitVirtualInterfaceRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### newTransitVirtualInterfaceAllocation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.NewTransitVirtualInterfaceAllocation'>
- **Required**: Yes


# AllocateTransitVirtualInterfaceResult

### virtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualInterface'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateConnectionWithLagRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### lagId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateHostedConnectionRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### parentConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateMacSecKeyRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### secretARN
- **Type**: typing.Optional[str]

### ckn
- **Type**: typing.Optional[str]

### cak
- **Type**: typing.Optional[str]


# AssociateMacSecKeyResponse

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### macSecKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.MacSecKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateVirtualInterfaceRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatedCoreNetwork

### id
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]

### attachmentId
- **Type**: typing.Optional[str]


# AssociatedGateway

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['transitGateway', 'virtualPrivateGateway']]

### ownerAccount
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# BGPPeer

### bgpPeerId
- **Type**: typing.Optional[str]

### asn
- **Type**: typing.Optional[int]

### authKey
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### amazonAddress
- **Type**: typing.Optional[str]

### customerAddress
- **Type**: typing.Optional[str]

### bgpPeerState
- **Type**: typing.Optional[typing.Literal['available', 'deleted', 'deleting', 'pending', 'verifying']]

### bgpStatus
- **Type**: typing.Optional[typing.Literal['down', 'unknown', 'up']]

### awsDeviceV2
- **Type**: typing.Optional[str]

### awsLogicalDeviceId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfirmConnectionRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes


# ConfirmConnectionResponse

### connectionState
- **Type**: typing.Literal['available', 'deleted', 'deleting', 'down', 'ordering', 'pending', 'rejected', 'requested', 'unknown']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ConfirmCustomerAgreementRequest

### agreementName
- **Type**: typing.Optional[str]


# ConfirmCustomerAgreementResponse

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ConfirmPrivateVirtualInterfaceRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]


# ConfirmPrivateVirtualInterfaceResponse

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ConfirmPublicVirtualInterfaceRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes


# ConfirmPublicVirtualInterfaceResponse

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ConfirmTransitVirtualInterfaceRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# ConfirmTransitVirtualInterfaceResponse

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Connection

### ownerAccount
- **Type**: typing.Optional[str]

### connectionId
- **Type**: typing.Optional[str]

### connectionName
- **Type**: typing.Optional[str]

### connectionState
- **Type**: typing.Optional[typing.Literal['available', 'deleted', 'deleting', 'down', 'ordering', 'pending', 'rejected', 'requested', 'unknown']]

### region
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[str]

### bandwidth
- **Type**: typing.Optional[str]

### vlan
- **Type**: typing.Optional[int]

### partnerName
- **Type**: typing.Optional[str]

### loaIssueTime
- **Type**: typing.Optional[datetime.datetime]

### lagId
- **Type**: typing.Optional[str]

### awsDevice
- **Type**: typing.Optional[str]

### jumboFrameCapable
- **Type**: typing.Optional[bool]

### awsDeviceV2
- **Type**: typing.Optional[str]

### awsLogicalDeviceId
- **Type**: typing.Optional[str]

### hasLogicalRedundancy
- **Type**: typing.Optional[typing.Literal['no', 'unknown', 'yes']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### providerName
- **Type**: typing.Optional[str]

### macSecCapable
- **Type**: typing.Optional[bool]

### portEncryptionStatus
- **Type**: typing.Optional[str]

### encryptionMode
- **Type**: typing.Optional[str]

### macSecKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.MacSecKey]]


# ConnectionResponse

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### connectionName
- **Type**: <class 'str'>
- **Required**: Yes

### connectionState
- **Type**: typing.Literal['available', 'deleted', 'deleting', 'down', 'ordering', 'pending', 'rejected', 'requested', 'unknown']
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### bandwidth
- **Type**: <class 'str'>
- **Required**: Yes

### vlan
- **Type**: <class 'int'>
- **Required**: Yes

### partnerName
- **Type**: <class 'str'>
- **Required**: Yes

### loaIssueTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lagId
- **Type**: <class 'str'>
- **Required**: Yes

### awsDevice
- **Type**: <class 'str'>
- **Required**: Yes

### jumboFrameCapable
- **Type**: <class 'bool'>
- **Required**: Yes

### awsDeviceV2
- **Type**: <class 'str'>
- **Required**: Yes

### awsLogicalDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### hasLogicalRedundancy
- **Type**: typing.Literal['no', 'unknown', 'yes']
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]
- **Required**: Yes

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### macSecCapable
- **Type**: <class 'bool'>
- **Required**: Yes

### portEncryptionStatus
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionMode
- **Type**: <class 'str'>
- **Required**: Yes

### macSecKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.MacSecKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Connections

### connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Connection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBGPPeerRequest

### virtualInterfaceId
- **Type**: typing.Optional[str]

### newBGPPeer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.NewBGPPeer]


# CreateBGPPeerResponse

### virtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualInterface'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectionRequest

### location
- **Type**: <class 'str'>
- **Required**: Yes

### bandwidth
- **Type**: <class 'str'>
- **Required**: Yes

### connectionName
- **Type**: <class 'str'>
- **Required**: Yes

### lagId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### providerName
- **Type**: typing.Optional[str]

### requestMACSec
- **Type**: typing.Optional[bool]


# CreateDirectConnectGatewayAssociationProposalRequest

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### directConnectGatewayOwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### addAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]

### removeAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]


# CreateDirectConnectGatewayAssociationProposalResult

### directConnectGatewayAssociationProposal
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAssociationProposal'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDirectConnectGatewayAssociationRequest

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayId
- **Type**: typing.Optional[str]

### addAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]

### virtualGatewayId
- **Type**: typing.Optional[str]


# CreateDirectConnectGatewayAssociationResult

### directConnectGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDirectConnectGatewayRequest

### directConnectGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### amazonSideAsn
- **Type**: typing.Optional[int]


# CreateDirectConnectGatewayResult

### directConnectGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGateway'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInterconnectRequest

### interconnectName
- **Type**: <class 'str'>
- **Required**: Yes

### bandwidth
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### lagId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### providerName
- **Type**: typing.Optional[str]


# CreateLagRequest

### numberOfConnections
- **Type**: <class 'int'>
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### connectionsBandwidth
- **Type**: <class 'str'>
- **Required**: Yes

### lagName
- **Type**: <class 'str'>
- **Required**: Yes

### connectionId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### childConnectionTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### providerName
- **Type**: typing.Optional[str]

### requestMACSec
- **Type**: typing.Optional[bool]


# CreatePrivateVirtualInterfaceRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### newPrivateVirtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.NewPrivateVirtualInterface'>
- **Required**: Yes


# CreatePublicVirtualInterfaceRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### newPublicVirtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.NewPublicVirtualInterface'>
- **Required**: Yes


# CreateTransitVirtualInterfaceRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### newTransitVirtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.NewTransitVirtualInterface'>
- **Required**: Yes


# CreateTransitVirtualInterfaceResult

### virtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualInterface'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerAgreement

### agreementName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]


# DeleteBGPPeerRequest

### virtualInterfaceId
- **Type**: typing.Optional[str]

### asn
- **Type**: typing.Optional[int]

### customerAddress
- **Type**: typing.Optional[str]

### bgpPeerId
- **Type**: typing.Optional[str]


# DeleteBGPPeerResponse

### virtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualInterface'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConnectionRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectConnectGatewayAssociationProposalRequest

### proposalId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectConnectGatewayAssociationProposalResult

### directConnectGatewayAssociationProposal
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAssociationProposal'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDirectConnectGatewayAssociationRequest

### associationId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualGatewayId
- **Type**: typing.Optional[str]


# DeleteDirectConnectGatewayAssociationResult

### directConnectGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDirectConnectGatewayRequest

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectConnectGatewayResult

### directConnectGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGateway'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInterconnectRequest

### interconnectId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInterconnectResponse

### interconnectState
- **Type**: typing.Literal['available', 'deleted', 'deleting', 'down', 'pending', 'requested', 'unknown']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLagRequest

### lagId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualInterfaceRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualInterfaceResponse

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectionLoaRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### providerName
- **Type**: typing.Optional[str]

### loaContentType
- **Type**: typing.Optional[typing.Literal['application/pdf']]


# DescribeConnectionLoaResponse

### loa
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Loa'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectionsOnInterconnectRequest

### interconnectId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectionsRequest

### connectionId
- **Type**: typing.Optional[str]


# DescribeCustomerMetadataResponse

### agreements
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.CustomerAgreement]
- **Required**: Yes

### nniPartnerType
- **Type**: typing.Literal['nonPartner', 'v1', 'v2']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDirectConnectGatewayAssociationProposalsRequest

### directConnectGatewayId
- **Type**: typing.Optional[str]

### proposalId
- **Type**: typing.Optional[str]

### associatedGatewayId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewayAssociationProposalsResult

### directConnectGatewayAssociationProposals
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAssociationProposal]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewayAssociationsRequest

### associationId
- **Type**: typing.Optional[str]

### associatedGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### virtualGatewayId
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewayAssociationsRequestPaginate

### associationId
- **Type**: typing.Optional[str]

### associatedGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualGatewayId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.PaginatorConfig]


# DescribeDirectConnectGatewayAssociationsResult

### directConnectGatewayAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewayAttachmentsRequest

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewayAttachmentsRequestPaginate

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.PaginatorConfig]


# DescribeDirectConnectGatewayAttachmentsResult

### directConnectGatewayAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAttachment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewaysRequest

### directConnectGatewayId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewaysRequestPaginate

### directConnectGatewayId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.PaginatorConfig]


# DescribeDirectConnectGatewaysResult

### directConnectGateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGateway]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeHostedConnectionsRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInterconnectLoaRequest

### interconnectId
- **Type**: <class 'str'>
- **Required**: Yes

### providerName
- **Type**: typing.Optional[str]

### loaContentType
- **Type**: typing.Optional[typing.Literal['application/pdf']]


# DescribeInterconnectLoaResponse

### loa
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Loa'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInterconnectsRequest

### interconnectId
- **Type**: typing.Optional[str]


# DescribeLagsRequest

### lagId
- **Type**: typing.Optional[str]


# DescribeLoaRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### providerName
- **Type**: typing.Optional[str]

### loaContentType
- **Type**: typing.Optional[typing.Literal['application/pdf']]


# DescribeRouterConfigurationRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### routerTypeIdentifier
- **Type**: typing.Optional[str]


# DescribeRouterConfigurationResponse

### customerRouterConfig
- **Type**: <class 'str'>
- **Required**: Yes

### router
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouterType'>
- **Required**: Yes

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### virtualInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTagsRequest

### resourceArns
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeTagsResponse

### resourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVirtualInterfacesRequest

### connectionId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]


# DirectConnectGateway

### directConnectGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayName
- **Type**: typing.Optional[str]

### amazonSideAsn
- **Type**: typing.Optional[int]

### ownerAccount
- **Type**: typing.Optional[str]

### directConnectGatewayState
- **Type**: typing.Optional[typing.Literal['available', 'deleted', 'deleting', 'pending']]

### stateChangeError
- **Type**: typing.Optional[str]


# DirectConnectGatewayAssociation

### directConnectGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayOwnerAccount
- **Type**: typing.Optional[str]

### associationState
- **Type**: typing.Optional[typing.Literal['associated', 'associating', 'disassociated', 'disassociating', 'updating']]

### stateChangeError
- **Type**: typing.Optional[str]

### associatedGateway
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.AssociatedGateway]

### associationId
- **Type**: typing.Optional[str]

### allowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]

### associatedCoreNetwork
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.AssociatedCoreNetwork]

### virtualGatewayId
- **Type**: typing.Optional[str]

### virtualGatewayRegion
- **Type**: typing.Optional[str]

### virtualGatewayOwnerAccount
- **Type**: typing.Optional[str]


# DirectConnectGatewayAssociationProposal

### proposalId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayOwnerAccount
- **Type**: typing.Optional[str]

### proposalState
- **Type**: typing.Optional[typing.Literal['accepted', 'deleted', 'requested']]

### associatedGateway
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.AssociatedGateway]

### existingAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]

### requestedAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]


# DirectConnectGatewayAttachment

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### virtualInterfaceRegion
- **Type**: typing.Optional[str]

### virtualInterfaceOwnerAccount
- **Type**: typing.Optional[str]

### attachmentState
- **Type**: typing.Optional[typing.Literal['attached', 'attaching', 'detached', 'detaching']]

### attachmentType
- **Type**: typing.Optional[typing.Literal['PrivateVirtualInterface', 'TransitVirtualInterface']]

### stateChangeError
- **Type**: typing.Optional[str]


# DisassociateConnectionFromLagRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### lagId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMacSecKeyRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### secretARN
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMacSecKeyResponse

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### macSecKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.MacSecKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Interconnect

### interconnectId
- **Type**: typing.Optional[str]

### interconnectName
- **Type**: typing.Optional[str]

### interconnectState
- **Type**: typing.Optional[typing.Literal['available', 'deleted', 'deleting', 'down', 'pending', 'requested', 'unknown']]

### region
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[str]

### bandwidth
- **Type**: typing.Optional[str]

### loaIssueTime
- **Type**: typing.Optional[datetime.datetime]

### lagId
- **Type**: typing.Optional[str]

### awsDevice
- **Type**: typing.Optional[str]

### jumboFrameCapable
- **Type**: typing.Optional[bool]

### awsDeviceV2
- **Type**: typing.Optional[str]

### awsLogicalDeviceId
- **Type**: typing.Optional[str]

### hasLogicalRedundancy
- **Type**: typing.Optional[typing.Literal['no', 'unknown', 'yes']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### providerName
- **Type**: typing.Optional[str]


# InterconnectResponse

### interconnectId
- **Type**: <class 'str'>
- **Required**: Yes

### interconnectName
- **Type**: <class 'str'>
- **Required**: Yes

### interconnectState
- **Type**: typing.Literal['available', 'deleted', 'deleting', 'down', 'pending', 'requested', 'unknown']
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### bandwidth
- **Type**: <class 'str'>
- **Required**: Yes

### loaIssueTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lagId
- **Type**: <class 'str'>
- **Required**: Yes

### awsDevice
- **Type**: <class 'str'>
- **Required**: Yes

### jumboFrameCapable
- **Type**: <class 'bool'>
- **Required**: Yes

### awsDeviceV2
- **Type**: <class 'str'>
- **Required**: Yes

### awsLogicalDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### hasLogicalRedundancy
- **Type**: typing.Literal['no', 'unknown', 'yes']
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]
- **Required**: Yes

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Interconnects

### interconnects
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Interconnect]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Lag

### connectionsBandwidth
- **Type**: typing.Optional[str]

### numberOfConnections
- **Type**: typing.Optional[int]

### lagId
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]

### lagName
- **Type**: typing.Optional[str]

### lagState
- **Type**: typing.Optional[typing.Literal['available', 'deleted', 'deleting', 'down', 'pending', 'requested', 'unknown']]

### location
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### minimumLinks
- **Type**: typing.Optional[int]

### awsDevice
- **Type**: typing.Optional[str]

### awsDeviceV2
- **Type**: typing.Optional[str]

### awsLogicalDeviceId
- **Type**: typing.Optional[str]

### connections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Connection]]

### allowsHostedConnections
- **Type**: typing.Optional[bool]

### jumboFrameCapable
- **Type**: typing.Optional[bool]

### hasLogicalRedundancy
- **Type**: typing.Optional[typing.Literal['no', 'unknown', 'yes']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### providerName
- **Type**: typing.Optional[str]

### macSecCapable
- **Type**: typing.Optional[bool]

### encryptionMode
- **Type**: typing.Optional[str]

### macSecKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.MacSecKey]]


# LagResponse

### connectionsBandwidth
- **Type**: <class 'str'>
- **Required**: Yes

### numberOfConnections
- **Type**: <class 'int'>
- **Required**: Yes

### lagId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### lagName
- **Type**: <class 'str'>
- **Required**: Yes

### lagState
- **Type**: typing.Literal['available', 'deleted', 'deleting', 'down', 'pending', 'requested', 'unknown']
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### minimumLinks
- **Type**: <class 'int'>
- **Required**: Yes

### awsDevice
- **Type**: <class 'str'>
- **Required**: Yes

### awsDeviceV2
- **Type**: <class 'str'>
- **Required**: Yes

### awsLogicalDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Connection]
- **Required**: Yes

### allowsHostedConnections
- **Type**: <class 'bool'>
- **Required**: Yes

### jumboFrameCapable
- **Type**: <class 'bool'>
- **Required**: Yes

### hasLogicalRedundancy
- **Type**: typing.Literal['no', 'unknown', 'yes']
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]
- **Required**: Yes

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### macSecCapable
- **Type**: <class 'bool'>
- **Required**: Yes

### encryptionMode
- **Type**: <class 'str'>
- **Required**: Yes

### macSecKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.MacSecKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Lags

### lags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Lag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ListVirtualInterfaceTestHistoryRequest

### testId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### bgpPeers
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualInterfaceTestHistoryResponse

### virtualInterfaceTestHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualInterfaceTestHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Loa

### loaContent
- **Type**: typing.Optional[bytes]

### loaContentType
- **Type**: typing.Optional[typing.Literal['application/pdf']]


# LoaResponse

### loaContent
- **Type**: <class 'bytes'>
- **Required**: Yes

### loaContentType
- **Type**: typing.Literal['application/pdf']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Location

### locationCode
- **Type**: typing.Optional[str]

### locationName
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### availablePortSpeeds
- **Type**: typing.Optional[typing.List[str]]

### availableProviders
- **Type**: typing.Optional[typing.List[str]]

### availableMacSecPortSpeeds
- **Type**: typing.Optional[typing.List[str]]


# Locations

### locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Location]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# MacSecKey

### secretARN
- **Type**: typing.Optional[str]

### ckn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]

### startOn
- **Type**: typing.Optional[str]


# NewBGPPeer

### asn
- **Type**: typing.Optional[int]

### authKey
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### amazonAddress
- **Type**: typing.Optional[str]

### customerAddress
- **Type**: typing.Optional[str]


# NewPrivateVirtualInterface

### virtualInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### vlan
- **Type**: <class 'int'>
- **Required**: Yes

### asn
- **Type**: <class 'int'>
- **Required**: Yes

### mtu
- **Type**: typing.Optional[int]

### authKey
- **Type**: typing.Optional[str]

### amazonAddress
- **Type**: typing.Optional[str]

### customerAddress
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### virtualGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### enableSiteLink
- **Type**: typing.Optional[bool]


# NewPrivateVirtualInterfaceAllocation

### virtualInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### vlan
- **Type**: <class 'int'>
- **Required**: Yes

### asn
- **Type**: <class 'int'>
- **Required**: Yes

### mtu
- **Type**: typing.Optional[int]

### authKey
- **Type**: typing.Optional[str]

### amazonAddress
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### customerAddress
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]


# NewPublicVirtualInterface

### virtualInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### vlan
- **Type**: <class 'int'>
- **Required**: Yes

### asn
- **Type**: <class 'int'>
- **Required**: Yes

### authKey
- **Type**: typing.Optional[str]

### amazonAddress
- **Type**: typing.Optional[str]

### customerAddress
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### routeFilterPrefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]


# NewPublicVirtualInterfaceAllocation

### virtualInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### vlan
- **Type**: <class 'int'>
- **Required**: Yes

### asn
- **Type**: <class 'int'>
- **Required**: Yes

### authKey
- **Type**: typing.Optional[str]

### amazonAddress
- **Type**: typing.Optional[str]

### customerAddress
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### routeFilterPrefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]


# NewTransitVirtualInterface

### virtualInterfaceName
- **Type**: typing.Optional[str]

### vlan
- **Type**: typing.Optional[int]

### asn
- **Type**: typing.Optional[int]

### mtu
- **Type**: typing.Optional[int]

### authKey
- **Type**: typing.Optional[str]

### amazonAddress
- **Type**: typing.Optional[str]

### customerAddress
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### enableSiteLink
- **Type**: typing.Optional[bool]


# NewTransitVirtualInterfaceAllocation

### virtualInterfaceName
- **Type**: typing.Optional[str]

### vlan
- **Type**: typing.Optional[int]

### asn
- **Type**: typing.Optional[int]

### mtu
- **Type**: typing.Optional[int]

### authKey
- **Type**: typing.Optional[str]

### amazonAddress
- **Type**: typing.Optional[str]

### customerAddress
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTag

### resourceArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]


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


# RouteFilterPrefix

### cidr
- **Type**: typing.Optional[str]


# RouterType

### vendor
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]

### software
- **Type**: typing.Optional[str]

### xsltTemplateName
- **Type**: typing.Optional[str]

### xsltTemplateNameForMacSec
- **Type**: typing.Optional[str]

### routerTypeIdentifier
- **Type**: typing.Optional[str]


# StartBgpFailoverTestRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### bgpPeers
- **Type**: typing.Optional[typing.List[str]]

### testDurationInMinutes
- **Type**: typing.Optional[int]


# StartBgpFailoverTestResponse

### virtualInterfaceTest
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualInterfaceTestHistory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# StopBgpFailoverTestRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes


# StopBgpFailoverTestResponse

### virtualInterfaceTest
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualInterfaceTestHistory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateConnectionRequest

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### connectionName
- **Type**: typing.Optional[str]

### encryptionMode
- **Type**: typing.Optional[str]


# UpdateDirectConnectGatewayAssociationRequest

### associationId
- **Type**: typing.Optional[str]

### addAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]

### removeAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]


# UpdateDirectConnectGatewayAssociationResult

### directConnectGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGatewayAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDirectConnectGatewayRequest

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### newDirectConnectGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDirectConnectGatewayResponse

### directConnectGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.DirectConnectGateway'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLagRequest

### lagId
- **Type**: <class 'str'>
- **Required**: Yes

### lagName
- **Type**: typing.Optional[str]

### minimumLinks
- **Type**: typing.Optional[int]

### encryptionMode
- **Type**: typing.Optional[str]


# UpdateVirtualInterfaceAttributesRequest

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### mtu
- **Type**: typing.Optional[int]

### enableSiteLink
- **Type**: typing.Optional[bool]

### virtualInterfaceName
- **Type**: typing.Optional[str]


# VirtualGateway

### virtualGatewayId
- **Type**: typing.Optional[str]

### virtualGatewayState
- **Type**: typing.Optional[str]


# VirtualGateways

### virtualGateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualGateway]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# VirtualInterface

### ownerAccount
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[str]

### connectionId
- **Type**: typing.Optional[str]

### virtualInterfaceType
- **Type**: typing.Optional[str]

### virtualInterfaceName
- **Type**: typing.Optional[str]

### vlan
- **Type**: typing.Optional[int]

### asn
- **Type**: typing.Optional[int]

### amazonSideAsn
- **Type**: typing.Optional[int]

### authKey
- **Type**: typing.Optional[str]

### amazonAddress
- **Type**: typing.Optional[str]

### customerAddress
- **Type**: typing.Optional[str]

### addressFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### virtualInterfaceState
- **Type**: typing.Optional[typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']]

### customerRouterConfig
- **Type**: typing.Optional[str]

### mtu
- **Type**: typing.Optional[int]

### jumboFrameCapable
- **Type**: typing.Optional[bool]

### virtualGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### routeFilterPrefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]]

### bgpPeers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.BGPPeer]]

### region
- **Type**: typing.Optional[str]

### awsDeviceV2
- **Type**: typing.Optional[str]

### awsLogicalDeviceId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]]

### siteLinkEnabled
- **Type**: typing.Optional[bool]


# VirtualInterfaceResponse

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### virtualInterfaceType
- **Type**: <class 'str'>
- **Required**: Yes

### virtualInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### vlan
- **Type**: <class 'int'>
- **Required**: Yes

### asn
- **Type**: <class 'int'>
- **Required**: Yes

### amazonSideAsn
- **Type**: <class 'int'>
- **Required**: Yes

### authKey
- **Type**: <class 'str'>
- **Required**: Yes

### amazonAddress
- **Type**: <class 'str'>
- **Required**: Yes

### customerAddress
- **Type**: <class 'str'>
- **Required**: Yes

### addressFamily
- **Type**: typing.Literal['ipv4', 'ipv6']
- **Required**: Yes

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### customerRouterConfig
- **Type**: <class 'str'>
- **Required**: Yes

### mtu
- **Type**: <class 'int'>
- **Required**: Yes

### jumboFrameCapable
- **Type**: <class 'bool'>
- **Required**: Yes

### virtualGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### routeFilterPrefixes
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.RouteFilterPrefix]
- **Required**: Yes

### bgpPeers
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.BGPPeer]
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### awsDeviceV2
- **Type**: <class 'str'>
- **Required**: Yes

### awsLogicalDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.Tag]
- **Required**: Yes

### siteLinkEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes


# VirtualInterfaceTestHistory

### testId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### bgpPeers
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]

### testDurationInMinutes
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# VirtualInterfaces

### virtualInterfaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect.directconnect_classes.VirtualInterface]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect.directconnect_classes.ResponseMetadata'>
- **Required**: Yes



# Directconnect Classes

# AcceptDirectConnectGatewayAssociationProposalRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]


# AcceptDirectConnectGatewayAssociationProposalResultTypeDef

### directConnectGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AllocateConnectionOnInterconnectRequestTypeDef

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


# AllocateHostedConnectionRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]


# AllocatePrivateVirtualInterfaceRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### newPrivateVirtualInterfaceAllocation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.NewPrivateVirtualInterfaceAllocationTypeDef'>
- **Required**: Yes


# AllocatePublicVirtualInterfaceRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### newPublicVirtualInterfaceAllocation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.NewPublicVirtualInterfaceAllocationTypeDef'>
- **Required**: Yes


# AllocateTransitVirtualInterfaceRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### newTransitVirtualInterfaceAllocation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.NewTransitVirtualInterfaceAllocationTypeDef'>
- **Required**: Yes


# AllocateTransitVirtualInterfaceResultTypeDef

### virtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.VirtualInterfaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateConnectionWithLagRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### lagId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateHostedConnectionRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### parentConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateMacSecKeyRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### secretARN
- **Type**: typing.Optional[str]

### ckn
- **Type**: typing.Optional[str]

### cak
- **Type**: typing.Optional[str]


# AssociateMacSecKeyResponseTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### macSecKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.MacSecKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateVirtualInterfaceRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatedCoreNetworkTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociatedGatewayTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BGPPeerTypeDef

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

# ConfirmConnectionRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes


# ConfirmConnectionResponseTypeDef

### connectionState
- **Type**: typing.Literal['available', 'deleted', 'deleting', 'down', 'ordering', 'pending', 'rejected', 'requested', 'unknown']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfirmCustomerAgreementRequestTypeDef

### agreementName
- **Type**: typing.Optional[str]


# ConfirmCustomerAgreementResponseTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfirmPrivateVirtualInterfaceRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]


# ConfirmPrivateVirtualInterfaceResponseTypeDef

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfirmPublicVirtualInterfaceRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes


# ConfirmPublicVirtualInterfaceResponseTypeDef

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfirmTransitVirtualInterfaceRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# ConfirmTransitVirtualInterfaceResponseTypeDef

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConnectionResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.MacSecKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConnectionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### providerName
- **Type**: typing.Optional[str]

### macSecCapable
- **Type**: typing.Optional[bool]

### portEncryptionStatus
- **Type**: typing.Optional[str]

### encryptionMode
- **Type**: typing.Optional[str]

### macSecKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.MacSecKeyTypeDef]]


# ConnectionsTypeDef

### connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.ConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBGPPeerRequestTypeDef

### virtualInterfaceId
- **Type**: typing.Optional[str]

### newBGPPeer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect_classes.NewBGPPeerTypeDef]


# CreateBGPPeerResponseTypeDef

### virtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.VirtualInterfaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectionRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### providerName
- **Type**: typing.Optional[str]

### requestMACSec
- **Type**: typing.Optional[bool]


# CreateDirectConnectGatewayAssociationProposalRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]

### removeAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]


# CreateDirectConnectGatewayAssociationProposalResultTypeDef

### directConnectGatewayAssociationProposal
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAssociationProposalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDirectConnectGatewayAssociationRequestTypeDef

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayId
- **Type**: typing.Optional[str]

### addAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]

### virtualGatewayId
- **Type**: typing.Optional[str]


# CreateDirectConnectGatewayAssociationResultTypeDef

### directConnectGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDirectConnectGatewayRequestTypeDef

### directConnectGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### amazonSideAsn
- **Type**: typing.Optional[int]


# CreateDirectConnectGatewayResultTypeDef

### directConnectGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInterconnectRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### providerName
- **Type**: typing.Optional[str]


# CreateLagRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### childConnectionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### providerName
- **Type**: typing.Optional[str]

### requestMACSec
- **Type**: typing.Optional[bool]


# CreatePrivateVirtualInterfaceRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### newPrivateVirtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.NewPrivateVirtualInterfaceTypeDef'>
- **Required**: Yes


# CreatePublicVirtualInterfaceRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### newPublicVirtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.NewPublicVirtualInterfaceTypeDef'>
- **Required**: Yes


# CreateTransitVirtualInterfaceRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### newTransitVirtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.NewTransitVirtualInterfaceTypeDef'>
- **Required**: Yes


# CreateTransitVirtualInterfaceResultTypeDef

### virtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.VirtualInterfaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerAgreementTypeDef

### agreementName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]


# DeleteBGPPeerRequestTypeDef

### virtualInterfaceId
- **Type**: typing.Optional[str]

### asn
- **Type**: typing.Optional[int]

### customerAddress
- **Type**: typing.Optional[str]

### bgpPeerId
- **Type**: typing.Optional[str]


# DeleteBGPPeerResponseTypeDef

### virtualInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.VirtualInterfaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConnectionRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectConnectGatewayAssociationProposalRequestTypeDef

### proposalId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectConnectGatewayAssociationProposalResultTypeDef

### directConnectGatewayAssociationProposal
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAssociationProposalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDirectConnectGatewayAssociationRequestTypeDef

### associationId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualGatewayId
- **Type**: typing.Optional[str]


# DeleteDirectConnectGatewayAssociationResultTypeDef

### directConnectGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDirectConnectGatewayRequestTypeDef

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectConnectGatewayResultTypeDef

### directConnectGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInterconnectRequestTypeDef

### interconnectId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInterconnectResponseTypeDef

### interconnectState
- **Type**: typing.Literal['available', 'deleted', 'deleting', 'down', 'pending', 'requested', 'unknown']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLagRequestTypeDef

### lagId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualInterfaceRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualInterfaceResponseTypeDef

### virtualInterfaceState
- **Type**: typing.Literal['available', 'confirming', 'deleted', 'deleting', 'down', 'pending', 'rejected', 'unknown', 'verifying']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectionLoaRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### providerName
- **Type**: typing.Optional[str]

### loaContentType
- **Type**: typing.Optional[typing.Literal['application/pdf']]


# DescribeConnectionLoaResponseTypeDef

### loa
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.LoaTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectionsOnInterconnectRequestTypeDef

### interconnectId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectionsRequestTypeDef

### connectionId
- **Type**: typing.Optional[str]


# DescribeCustomerMetadataResponseTypeDef

### agreements
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.CustomerAgreementTypeDef]
- **Required**: Yes

### nniPartnerType
- **Type**: typing.Literal['nonPartner', 'v1', 'v2']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef

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


# DescribeDirectConnectGatewayAssociationProposalsResultTypeDef

### directConnectGatewayAssociationProposals
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAssociationProposalTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef

### associationId
- **Type**: typing.Optional[str]

### associatedGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualGatewayId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect_classes.PaginatorConfigTypeDef]


# DescribeDirectConnectGatewayAssociationsRequestTypeDef

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


# DescribeDirectConnectGatewayAssociationsResultTypeDef

### directConnectGatewayAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect_classes.PaginatorConfigTypeDef]


# DescribeDirectConnectGatewayAttachmentsRequestTypeDef

### directConnectGatewayId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewayAttachmentsResultTypeDef

### directConnectGatewayAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAttachmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewaysRequestPaginateTypeDef

### directConnectGatewayId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect_classes.PaginatorConfigTypeDef]


# DescribeDirectConnectGatewaysRequestTypeDef

### directConnectGatewayId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeDirectConnectGatewaysResultTypeDef

### directConnectGateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeHostedConnectionsRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInterconnectLoaRequestTypeDef

### interconnectId
- **Type**: <class 'str'>
- **Required**: Yes

### providerName
- **Type**: typing.Optional[str]

### loaContentType
- **Type**: typing.Optional[typing.Literal['application/pdf']]


# DescribeInterconnectLoaResponseTypeDef

### loa
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.LoaTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInterconnectsRequestTypeDef

### interconnectId
- **Type**: typing.Optional[str]


# DescribeLagsRequestTypeDef

### lagId
- **Type**: typing.Optional[str]


# DescribeLoaRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### providerName
- **Type**: typing.Optional[str]

### loaContentType
- **Type**: typing.Optional[typing.Literal['application/pdf']]


# DescribeRouterConfigurationRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### routerTypeIdentifier
- **Type**: typing.Optional[str]


# DescribeRouterConfigurationResponseTypeDef

### customerRouterConfig
- **Type**: <class 'str'>
- **Required**: Yes

### router
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.RouterTypeTypeDef'>
- **Required**: Yes

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### virtualInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTagsRequestTypeDef

### resourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTagsResponseTypeDef

### resourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVirtualInterfacesRequestTypeDef

### connectionId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]


# DirectConnectGatewayAssociationProposalTypeDef

### proposalId
- **Type**: typing.Optional[str]

### directConnectGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayOwnerAccount
- **Type**: typing.Optional[str]

### proposalState
- **Type**: typing.Optional[typing.Literal['accepted', 'deleted', 'requested']]

### associatedGateway
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect_classes.AssociatedGatewayTypeDef]

### existingAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]

### requestedAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]


# DirectConnectGatewayAssociationTypeDef

### directConnectGatewayId
- **Type**: typing.Optional[str]

### directConnectGatewayOwnerAccount
- **Type**: typing.Optional[str]

### associationState
- **Type**: typing.Optional[typing.Literal['associated', 'associating', 'disassociated', 'disassociating', 'updating']]

### stateChangeError
- **Type**: typing.Optional[str]

### associatedGateway
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect_classes.AssociatedGatewayTypeDef]

### associationId
- **Type**: typing.Optional[str]

### allowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]

### associatedCoreNetwork
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.directconnect_classes.AssociatedCoreNetworkTypeDef]

### virtualGatewayId
- **Type**: typing.Optional[str]

### virtualGatewayRegion
- **Type**: typing.Optional[str]

### virtualGatewayOwnerAccount
- **Type**: typing.Optional[str]


# DirectConnectGatewayAttachmentTypeDef

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


# DirectConnectGatewayTypeDef

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


# DisassociateConnectionFromLagRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### lagId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMacSecKeyRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### secretARN
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMacSecKeyResponseTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### macSecKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.MacSecKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InterconnectResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]
- **Required**: Yes

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InterconnectTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### providerName
- **Type**: typing.Optional[str]


# InterconnectsTypeDef

### interconnects
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.InterconnectTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LagResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.ConnectionTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.MacSecKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LagTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.ConnectionTypeDef]]

### allowsHostedConnections
- **Type**: typing.Optional[bool]

### jumboFrameCapable
- **Type**: typing.Optional[bool]

### hasLogicalRedundancy
- **Type**: typing.Optional[typing.Literal['no', 'unknown', 'yes']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### providerName
- **Type**: typing.Optional[str]

### macSecCapable
- **Type**: typing.Optional[bool]

### encryptionMode
- **Type**: typing.Optional[str]

### macSecKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.MacSecKeyTypeDef]]


# LagsTypeDef

### lags
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.LagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualInterfaceTestHistoryRequestTypeDef

### testId
- **Type**: typing.Optional[str]

### virtualInterfaceId
- **Type**: typing.Optional[str]

### bgpPeers
- **Type**: typing.Optional[typing.Sequence[str]]

### status
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualInterfaceTestHistoryResponseTypeDef

### virtualInterfaceTestHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.VirtualInterfaceTestHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LoaResponseTypeDef

### loaContent
- **Type**: <class 'bytes'>
- **Required**: Yes

### loaContentType
- **Type**: typing.Literal['application/pdf']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoaTypeDef

### loaContent
- **Type**: typing.Optional[bytes]

### loaContentType
- **Type**: typing.Optional[typing.Literal['application/pdf']]


# LocationTypeDef

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


# LocationsTypeDef

### locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.LocationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MacSecKeyTypeDef

### secretARN
- **Type**: typing.Optional[str]

### ckn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]

### startOn
- **Type**: typing.Optional[str]


# NewBGPPeerTypeDef

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


# NewPrivateVirtualInterfaceAllocationTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]


# NewPrivateVirtualInterfaceTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### enableSiteLink
- **Type**: typing.Optional[bool]


# NewPublicVirtualInterfaceAllocationTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]


# NewPublicVirtualInterfaceTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]


# NewTransitVirtualInterfaceAllocationTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]


# NewTransitVirtualInterfaceTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### enableSiteLink
- **Type**: typing.Optional[bool]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTagTypeDef

### resourceArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]


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


# RouteFilterPrefixTypeDef

### cidr
- **Type**: typing.Optional[str]


# RouterTypeTypeDef

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


# StartBgpFailoverTestRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### bgpPeers
- **Type**: typing.Optional[typing.Sequence[str]]

### testDurationInMinutes
- **Type**: typing.Optional[int]


# StartBgpFailoverTestResponseTypeDef

### virtualInterfaceTest
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.VirtualInterfaceTestHistoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopBgpFailoverTestRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes


# StopBgpFailoverTestResponseTypeDef

### virtualInterfaceTest
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.VirtualInterfaceTestHistoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectionRequestTypeDef

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### connectionName
- **Type**: typing.Optional[str]

### encryptionMode
- **Type**: typing.Optional[str]


# UpdateDirectConnectGatewayAssociationRequestTypeDef

### associationId
- **Type**: typing.Optional[str]

### addAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]

### removeAllowedPrefixesToDirectConnectGateway
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]


# UpdateDirectConnectGatewayAssociationResultTypeDef

### directConnectGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDirectConnectGatewayRequestTypeDef

### directConnectGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### newDirectConnectGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDirectConnectGatewayResponseTypeDef

### directConnectGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.DirectConnectGatewayTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLagRequestTypeDef

### lagId
- **Type**: <class 'str'>
- **Required**: Yes

### lagName
- **Type**: typing.Optional[str]

### minimumLinks
- **Type**: typing.Optional[int]

### encryptionMode
- **Type**: typing.Optional[str]


# UpdateVirtualInterfaceAttributesRequestTypeDef

### virtualInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### mtu
- **Type**: typing.Optional[int]

### enableSiteLink
- **Type**: typing.Optional[bool]

### virtualInterfaceName
- **Type**: typing.Optional[str]


# VirtualGatewayTypeDef

### virtualGatewayId
- **Type**: typing.Optional[str]

### virtualGatewayState
- **Type**: typing.Optional[str]


# VirtualGatewaysTypeDef

### virtualGateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.VirtualGatewayTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VirtualInterfaceResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]
- **Required**: Yes

### bgpPeers
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.BGPPeerTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]
- **Required**: Yes

### siteLinkEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VirtualInterfaceTestHistoryTypeDef

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


# VirtualInterfaceTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.RouteFilterPrefixTypeDef]]

### bgpPeers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.BGPPeerTypeDef]]

### region
- **Type**: typing.Optional[str]

### awsDeviceV2
- **Type**: typing.Optional[str]

### awsLogicalDeviceId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.directconnect_classes.TagTypeDef]]

### siteLinkEnabled
- **Type**: typing.Optional[bool]


# VirtualInterfacesTypeDef

### virtualInterfaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.directconnect_classes.VirtualInterfaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.directconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



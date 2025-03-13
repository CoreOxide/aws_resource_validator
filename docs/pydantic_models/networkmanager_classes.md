# Networkmanager Classes

# AWSLocationTypeDef

### Zone
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]


# AcceptAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptAttachmentResponseTypeDef

### Attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccountStatusTypeDef

### AccountId
- **Type**: typing.Optional[str]

### SLRDeploymentStatus
- **Type**: typing.Optional[str]


# AssociateConnectPeerRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectPeerId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: typing.Optional[str]


# AssociateConnectPeerResponseTypeDef

### ConnectPeerAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateCustomerGatewayRequestTypeDef

### CustomerGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: typing.Optional[str]


# AssociateCustomerGatewayResponseTypeDef

### CustomerGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CustomerGatewayAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateLinkRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateLinkResponseTypeDef

### LinkAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateTransitGatewayConnectPeerRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayConnectPeerArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: typing.Optional[str]


# AssociateTransitGatewayConnectPeerResponseTypeDef

### TransitGatewayConnectPeerAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayConnectPeerAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachmentErrorTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['DIRECT_CONNECT_GATEWAY_EXISTING_ATTACHMENTS', 'DIRECT_CONNECT_GATEWAY_NOT_FOUND', 'DIRECT_CONNECT_GATEWAY_NO_PRIVATE_VIF', 'MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED', 'SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE', 'SUBNET_NOT_FOUND', 'SUBNET_NO_FREE_ADDRESSES', 'SUBNET_NO_IPV6_CIDRS', 'SUBNET_UNSUPPORTED_AVAILABILITY_ZONE', 'VPC_NOT_FOUND', 'VPN_CONNECTION_NOT_FOUND']]

### Message
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]


# AttachmentTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### CoreNetworkArn
- **Type**: typing.Optional[str]

### AttachmentId
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### AttachmentType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DIRECT_CONNECT_GATEWAY', 'SITE_TO_SITE_VPN', 'TRANSIT_GATEWAY_ROUTE_TABLE', 'VPC']]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_ATTACHMENT_ACCEPTANCE', 'PENDING_NETWORK_UPDATE', 'PENDING_TAG_ACCEPTANCE', 'REJECTED', 'UPDATING']]

### EdgeLocation
- **Type**: typing.Optional[str]

### EdgeLocations
- **Type**: typing.Optional[typing.List[str]]

### ResourceArn
- **Type**: typing.Optional[str]

### AttachmentPolicyRuleNumber
- **Type**: typing.Optional[int]

### SegmentName
- **Type**: typing.Optional[str]

### NetworkFunctionGroupName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### ProposedSegmentChange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ProposedSegmentChangeTypeDef]

### ProposedNetworkFunctionGroupChange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ProposedNetworkFunctionGroupChangeTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastModificationErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentErrorTypeDef]]


# BandwidthTypeDef

### UploadSpeed
- **Type**: typing.Optional[int]

### DownloadSpeed
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BgpOptionsTypeDef

### PeerAsn
- **Type**: typing.Optional[int]


# ConnectAttachmentOptionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectAttachmentTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef]

### TransportAttachmentId
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectAttachmentOptionsTypeDef]


# ConnectPeerAssociationTypeDef

### ConnectPeerId
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DELETING', 'PENDING']]


# ConnectPeerBgpConfigurationTypeDef

### CoreNetworkAsn
- **Type**: typing.Optional[int]

### PeerAsn
- **Type**: typing.Optional[int]

### CoreNetworkAddress
- **Type**: typing.Optional[str]

### PeerAddress
- **Type**: typing.Optional[str]


# ConnectPeerConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectPeerErrorTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['EDGE_LOCATION_NO_FREE_IPS', 'EDGE_LOCATION_PEER_DUPLICATE', 'INVALID_INSIDE_CIDR_BLOCK', 'IP_OUTSIDE_SUBNET_CIDR_RANGE', 'NO_ASSOCIATED_CIDR_BLOCK', 'SUBNET_NOT_FOUND']]

### Message
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]


# ConnectPeerSummaryTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### ConnectAttachmentId
- **Type**: typing.Optional[str]

### ConnectPeerId
- **Type**: typing.Optional[str]

### EdgeLocation
- **Type**: typing.Optional[str]

### ConnectPeerState
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### SubnetArn
- **Type**: typing.Optional[str]


# ConnectPeerTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### ConnectAttachmentId
- **Type**: typing.Optional[str]

### ConnectPeerId
- **Type**: typing.Optional[str]

### EdgeLocation
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### SubnetArn
- **Type**: typing.Optional[str]

### LastModificationErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerErrorTypeDef]]


# ConnectionHealthTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectionTypeDef

### ConnectionId
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### ConnectedDeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### ConnectedLinkId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'PENDING', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# CoreNetworkChangeEventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoreNetworkChangeEventValuesTypeDef

### EdgeLocation
- **Type**: typing.Optional[str]

### SegmentName
- **Type**: typing.Optional[str]

### NetworkFunctionGroupName
- **Type**: typing.Optional[str]

### AttachmentId
- **Type**: typing.Optional[str]

### Cidr
- **Type**: typing.Optional[str]


# CoreNetworkChangeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoreNetworkChangeValuesTypeDef

### SegmentName
- **Type**: typing.Optional[str]

### NetworkFunctionGroupName
- **Type**: typing.Optional[str]

### EdgeLocations
- **Type**: typing.Optional[typing.List[str]]

### Asn
- **Type**: typing.Optional[int]

### Cidr
- **Type**: typing.Optional[str]

### DestinationIdentifier
- **Type**: typing.Optional[str]

### InsideCidrBlocks
- **Type**: typing.Optional[typing.List[str]]

### SharedSegments
- **Type**: typing.Optional[typing.List[str]]

### ServiceInsertionActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ServiceInsertionActionTypeDef]]


# CoreNetworkEdgeTypeDef

### EdgeLocation
- **Type**: typing.Optional[str]

### Asn
- **Type**: typing.Optional[int]

### InsideCidrBlocks
- **Type**: typing.Optional[typing.List[str]]


# CoreNetworkNetworkFunctionGroupIdentifierTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### NetworkFunctionGroupName
- **Type**: typing.Optional[str]

### EdgeLocation
- **Type**: typing.Optional[str]


# CoreNetworkNetworkFunctionGroupTypeDef

### Name
- **Type**: typing.Optional[str]

### EdgeLocations
- **Type**: typing.Optional[typing.List[str]]

### Segments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ServiceInsertionSegmentsTypeDef]


# CoreNetworkPolicyErrorTypeDef

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# CoreNetworkPolicyTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### PolicyVersionId
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[typing.Literal['LATEST', 'LIVE']]

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ChangeSetState
- **Type**: typing.Optional[typing.Literal['EXECUTING', 'EXECUTION_SUCCEEDED', 'FAILED_GENERATION', 'OUT_OF_DATE', 'PENDING_GENERATION', 'READY_TO_EXECUTE']]

### PolicyErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicyErrorTypeDef]]

### PolicyDocument
- **Type**: typing.Optional[str]


# CoreNetworkPolicyVersionTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### PolicyVersionId
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[typing.Literal['LATEST', 'LIVE']]

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ChangeSetState
- **Type**: typing.Optional[typing.Literal['EXECUTING', 'EXECUTION_SUCCEEDED', 'FAILED_GENERATION', 'OUT_OF_DATE', 'PENDING_GENERATION', 'READY_TO_EXECUTE']]


# CoreNetworkSegmentEdgeIdentifierTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### SegmentName
- **Type**: typing.Optional[str]

### EdgeLocation
- **Type**: typing.Optional[str]


# CoreNetworkSegmentTypeDef

### Name
- **Type**: typing.Optional[str]

### EdgeLocations
- **Type**: typing.Optional[typing.List[str]]

### SharedSegments
- **Type**: typing.Optional[typing.List[str]]


# CoreNetworkSummaryTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### CoreNetworkArn
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'UPDATING']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# CoreNetworkTypeDef

### GlobalNetworkId
- **Type**: typing.Optional[str]

### CoreNetworkId
- **Type**: typing.Optional[str]

### CoreNetworkArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'UPDATING']]

### Segments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkSegmentTypeDef]]

### NetworkFunctionGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkNetworkFunctionGroupTypeDef]]

### Edges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkEdgeTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# CreateConnectAttachmentRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeLocation
- **Type**: <class 'str'>
- **Required**: Yes

### TransportAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectAttachmentOptionsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateConnectAttachmentResponseTypeDef

### ConnectAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectPeerRequestTypeDef

### ConnectAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerAddress
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkAddress
- **Type**: typing.Optional[str]

### BgpOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.BgpOptionsTypeDef]

### InsideCidrBlocks
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]


# CreateConnectPeerResponseTypeDef

### ConnectPeer
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectionRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: typing.Optional[str]

### ConnectedLinkId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# CreateConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCoreNetworkRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### PolicyDocument
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# CreateCoreNetworkResponseTypeDef

### CoreNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeviceResponseTypeDef

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDirectConnectGatewayAttachmentRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DirectConnectGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeLocations
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateDirectConnectGatewayAttachmentResponseTypeDef

### DirectConnectGatewayAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DirectConnectGatewayAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGlobalNetworkRequestTypeDef

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# CreateGlobalNetworkResponseTypeDef

### GlobalNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.GlobalNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLinkResponseTypeDef

### Link
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSiteRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.LocationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# CreateSiteResponseTypeDef

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.SiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSiteToSiteVpnAttachmentRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### VpnConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateSiteToSiteVpnAttachmentResponseTypeDef

### SiteToSiteVpnAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.SiteToSiteVpnAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTransitGatewayPeeringRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateTransitGatewayPeeringResponseTypeDef

### TransitGatewayPeering
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayPeeringTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTransitGatewayRouteTableAttachmentRequestTypeDef

### PeeringId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayRouteTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateTransitGatewayRouteTableAttachmentResponseTypeDef

### TransitGatewayRouteTableAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRouteTableAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcAttachmentRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.VpcOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateVpcAttachmentResponseTypeDef

### VpcAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.VpcAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerGatewayAssociationTypeDef

### CustomerGatewayArn
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DELETING', 'PENDING']]


# DeleteAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAttachmentResponseTypeDef

### Attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConnectPeerRequestTypeDef

### ConnectPeerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectPeerResponseTypeDef

### ConnectPeer
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConnectionRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCoreNetworkPolicyVersionRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteCoreNetworkPolicyVersionResponseTypeDef

### CoreNetworkPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCoreNetworkRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCoreNetworkResponseTypeDef

### CoreNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDeviceRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceResponseTypeDef

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGlobalNetworkRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalNetworkResponseTypeDef

### GlobalNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.GlobalNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLinkRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLinkResponseTypeDef

### Link
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePeeringRequestTypeDef

### PeeringId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePeeringResponseTypeDef

### Peering
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.PeeringTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSiteRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSiteResponseTypeDef

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.SiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterTransitGatewayRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTransitGatewayResponseTypeDef

### TransitGatewayRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRegistrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGlobalNetworksRequestPaginateTypeDef

### GlobalNetworkIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# DescribeGlobalNetworksRequestTypeDef

### GlobalNetworkIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeGlobalNetworksResponseTypeDef

### GlobalNetworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.GlobalNetworkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DeviceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DirectConnectGatewayAttachmentTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef]

### DirectConnectGatewayArn
- **Type**: typing.Optional[str]


# DisassociateConnectPeerRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectPeerId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateConnectPeerResponseTypeDef

### ConnectPeerAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateCustomerGatewayRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateCustomerGatewayResponseTypeDef

### CustomerGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CustomerGatewayAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateLinkRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateLinkResponseTypeDef

### LinkAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateTransitGatewayConnectPeerRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayConnectPeerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateTransitGatewayConnectPeerResponseTypeDef

### TransitGatewayConnectPeerAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayConnectPeerAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EdgeOverrideTypeDef

### EdgeSets
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### UseEdge
- **Type**: typing.Optional[str]


# ExecuteCoreNetworkChangeSetRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# GetConnectAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectAttachmentResponseTypeDef

### ConnectAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectPeerAssociationsRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectPeerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetConnectPeerAssociationsRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectPeerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetConnectPeerAssociationsResponseTypeDef

### ConnectPeerAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetConnectPeerRequestTypeDef

### ConnectPeerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectPeerResponseTypeDef

### ConnectPeer
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectionsRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetConnectionsRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetConnectionsResponseTypeDef

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCoreNetworkChangeEventsRequestPaginateTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetCoreNetworkChangeEventsRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCoreNetworkChangeEventsResponseTypeDef

### CoreNetworkChangeEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkChangeEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCoreNetworkChangeSetRequestPaginateTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetCoreNetworkChangeSetRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCoreNetworkChangeSetResponseTypeDef

### CoreNetworkChanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkChangeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCoreNetworkPolicyRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[typing.Literal['LATEST', 'LIVE']]


# GetCoreNetworkPolicyResponseTypeDef

### CoreNetworkPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCoreNetworkRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCoreNetworkResponseTypeDef

### CoreNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCustomerGatewayAssociationsRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetCustomerGatewayAssociationsRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCustomerGatewayAssociationsResponseTypeDef

### CustomerGatewayAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CustomerGatewayAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDevicesRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SiteId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetDevicesRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SiteId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetDevicesResponseTypeDef

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.DeviceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDirectConnectGatewayAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDirectConnectGatewayAttachmentResponseTypeDef

### DirectConnectGatewayAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DirectConnectGatewayAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLinkAssociationsRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetLinkAssociationsRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetLinkAssociationsResponseTypeDef

### LinkAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.LinkAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLinksResponseTypeDef

### Links
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.LinkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourceCountsRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetNetworkResourceCountsRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourceCountsResponseTypeDef

### NetworkResourceCounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkResourceCountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourceRelationshipsRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkId
- **Type**: typing.Optional[str]

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetNetworkResourceRelationshipsRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkId
- **Type**: typing.Optional[str]

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourceRelationshipsResponseTypeDef

### Relationships
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.RelationshipTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourcesRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkId
- **Type**: typing.Optional[str]

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetNetworkResourcesRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkId
- **Type**: typing.Optional[str]

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourcesResponseTypeDef

### NetworkResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkRoutesRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteTableIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteTableIdentifierTypeDef'>
- **Required**: Yes

### ExactCidrMatches
- **Type**: typing.Optional[typing.Sequence[str]]

### LongestPrefixMatches
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetOfMatches
- **Type**: typing.Optional[typing.Sequence[str]]

### SupernetOfMatches
- **Type**: typing.Optional[typing.Sequence[str]]

### PrefixListIds
- **Type**: typing.Optional[typing.Sequence[str]]

### States
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'BLACKHOLE']]]

### Types
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PROPAGATED', 'STATIC']]]

### DestinationFilters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# GetNetworkRoutesResponseTypeDef

### RouteTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkSegmentEdge
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkSegmentEdgeIdentifierTypeDef'>
- **Required**: Yes

### RouteTableType
- **Type**: typing.Literal['CORE_NETWORK_SEGMENT', 'NETWORK_FUNCTION_GROUP', 'TRANSIT_GATEWAY_ROUTE_TABLE']
- **Required**: Yes

### RouteTableTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NetworkRoutes
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkRouteTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNetworkTelemetryRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkId
- **Type**: typing.Optional[str]

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetNetworkTelemetryRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkId
- **Type**: typing.Optional[str]

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkTelemetryResponseTypeDef

### NetworkTelemetry
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkTelemetryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRouteAnalysisRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteAnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteAnalysisResponseTypeDef

### RouteAnalysis
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSiteToSiteVpnAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSiteToSiteVpnAttachmentResponseTypeDef

### SiteToSiteVpnAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.SiteToSiteVpnAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSitesRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetSitesRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetSitesResponseTypeDef

### Sites
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.SiteTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayConnectPeerAssociationsRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayConnectPeerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetTransitGatewayConnectPeerAssociationsRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayConnectPeerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayConnectPeerAssociationsResponseTypeDef

### TransitGatewayConnectPeerAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayConnectPeerAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayPeeringRequestTypeDef

### PeeringId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransitGatewayPeeringResponseTypeDef

### TransitGatewayPeering
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayPeeringTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTransitGatewayRegistrationsRequestPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetTransitGatewayRegistrationsRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayRegistrationsResponseTypeDef

### TransitGatewayRegistrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRegistrationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayRouteTableAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransitGatewayRouteTableAttachmentResponseTypeDef

### TransitGatewayRouteTableAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRouteTableAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVpcAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcAttachmentResponseTypeDef

### VpcAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.VpcAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlobalNetworkTypeDef

### GlobalNetworkId
- **Type**: typing.Optional[str]

### GlobalNetworkArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'PENDING', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# LinkAssociationTypeDef

### GlobalNetworkId
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### LinkAssociationState
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DELETING', 'PENDING']]


# LinkTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAttachmentsRequestPaginateTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### AttachmentType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DIRECT_CONNECT_GATEWAY', 'SITE_TO_SITE_VPN', 'TRANSIT_GATEWAY_ROUTE_TABLE', 'VPC']]

### EdgeLocation
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_ATTACHMENT_ACCEPTANCE', 'PENDING_NETWORK_UPDATE', 'PENDING_TAG_ACCEPTANCE', 'REJECTED', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListAttachmentsRequestTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### AttachmentType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DIRECT_CONNECT_GATEWAY', 'SITE_TO_SITE_VPN', 'TRANSIT_GATEWAY_ROUTE_TABLE', 'VPC']]

### EdgeLocation
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_ATTACHMENT_ACCEPTANCE', 'PENDING_NETWORK_UPDATE', 'PENDING_TAG_ACCEPTANCE', 'REJECTED', 'UPDATING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAttachmentsResponseTypeDef

### Attachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectPeersRequestPaginateTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### ConnectAttachmentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListConnectPeersRequestTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### ConnectAttachmentId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectPeersResponseTypeDef

### ConnectPeers
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCoreNetworkPolicyVersionsRequestPaginateTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListCoreNetworkPolicyVersionsRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreNetworkPolicyVersionsResponseTypeDef

### CoreNetworkPolicyVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicyVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCoreNetworksRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListCoreNetworksRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreNetworksResponseTypeDef

### CoreNetworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationServiceAccessStatusRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationServiceAccessStatusResponseTypeDef

### OrganizationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.OrganizationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPeeringsRequestPaginateTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### PeeringType
- **Type**: typing.Optional[typing.Literal['TRANSIT_GATEWAY']]

### EdgeLocation
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListPeeringsRequestTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### PeeringType
- **Type**: typing.Optional[typing.Literal['TRANSIT_GATEWAY']]

### EdgeLocation
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPeeringsResponseTypeDef

### Peerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.PeeringTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LocationTypeDef

### Address
- **Type**: typing.Optional[str]

### Latitude
- **Type**: typing.Optional[str]

### Longitude
- **Type**: typing.Optional[str]


# NetworkFunctionGroupTypeDef

### Name
- **Type**: typing.Optional[str]


# NetworkResourceCountTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]


# NetworkResourceSummaryTypeDef

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[str]

### NameTag
- **Type**: typing.Optional[str]

### IsMiddlebox
- **Type**: typing.Optional[bool]


# NetworkResourceTypeDef

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### CoreNetworkId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[str]

### DefinitionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### Metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# NetworkRouteDestinationTypeDef

### CoreNetworkAttachmentId
- **Type**: typing.Optional[str]

### TransitGatewayAttachmentId
- **Type**: typing.Optional[str]

### SegmentName
- **Type**: typing.Optional[str]

### NetworkFunctionGroupName
- **Type**: typing.Optional[str]

### EdgeLocation
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]


# NetworkRouteTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkTelemetryTypeDef

### RegisteredGatewayArn
- **Type**: typing.Optional[str]

### CoreNetworkId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### Address
- **Type**: typing.Optional[str]

### Health
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectionHealthTypeDef]


# OrganizationStatusTypeDef

### OrganizationId
- **Type**: typing.Optional[str]

### OrganizationAwsServiceAccessStatus
- **Type**: typing.Optional[str]

### SLRDeploymentStatus
- **Type**: typing.Optional[str]

### AccountStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.AccountStatusTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathComponentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PeeringErrorTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['EDGE_LOCATION_PEER_DUPLICATE', 'INTERNAL_ERROR', 'INVALID_TRANSIT_GATEWAY_STATE', 'MISSING_PERMISSIONS', 'TRANSIT_GATEWAY_NOT_FOUND', 'TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED']]

### Message
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### MissingPermissionsContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PermissionsErrorContextTypeDef]


# PeeringTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### CoreNetworkArn
- **Type**: typing.Optional[str]

### PeeringId
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### PeeringType
- **Type**: typing.Optional[typing.Literal['TRANSIT_GATEWAY']]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']]

### EdgeLocation
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastModificationErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.PeeringErrorTypeDef]]


# PermissionsErrorContextTypeDef

### MissingPermission
- **Type**: typing.Optional[str]


# ProposedNetworkFunctionGroupChangeTypeDef

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### AttachmentPolicyRuleNumber
- **Type**: typing.Optional[int]

### NetworkFunctionGroupName
- **Type**: typing.Optional[str]


# ProposedSegmentChangeTypeDef

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]

### AttachmentPolicyRuleNumber
- **Type**: typing.Optional[int]

### SegmentName
- **Type**: typing.Optional[str]


# PutCoreNetworkPolicyRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LatestVersionId
- **Type**: typing.Optional[int]

### ClientToken
- **Type**: typing.Optional[str]


# PutCoreNetworkPolicyResponseTypeDef

### CoreNetworkPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterTransitGatewayRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterTransitGatewayResponseTypeDef

### TransitGatewayRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRegistrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RejectAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# RejectAttachmentResponseTypeDef

### Attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RelationshipTypeDef

### From
- **Type**: typing.Optional[str]

### To
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


# RestoreCoreNetworkPolicyVersionRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# RestoreCoreNetworkPolicyVersionResponseTypeDef

### CoreNetworkPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RouteAnalysisCompletionTypeDef

### ResultCode
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'NOT_CONNECTED']]

### ReasonCode
- **Type**: typing.Optional[typing.Literal['BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND', 'CYCLIC_PATH_DETECTED', 'INACTIVE_ROUTE_FOR_DESTINATION_FOUND', 'MAX_HOPS_EXCEEDED', 'NO_DESTINATION_ARN_PROVIDED', 'POSSIBLE_MIDDLEBOX', 'ROUTE_NOT_FOUND', 'TRANSIT_GATEWAY_ATTACHMENT_ATTACH_ARN_NO_MATCH', 'TRANSIT_GATEWAY_ATTACHMENT_NOT_FOUND', 'TRANSIT_GATEWAY_ATTACHMENT_NOT_IN_TRANSIT_GATEWAY', 'TRANSIT_GATEWAY_ATTACHMENT_STABLE_ROUTE_TABLE_NOT_FOUND']]

### ReasonContext
- **Type**: typing.Optional[typing.Dict[str, str]]


# RouteAnalysisEndpointOptionsSpecificationTypeDef

### TransitGatewayAttachmentArn
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# RouteAnalysisEndpointOptionsTypeDef

### TransitGatewayAttachmentArn
- **Type**: typing.Optional[str]

### TransitGatewayArn
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# RouteAnalysisPathTypeDef

### CompletionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisCompletionTypeDef]

### Path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.PathComponentTypeDef]]


# RouteAnalysisTypeDef

### GlobalNetworkId
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### RouteAnalysisId
- **Type**: typing.Optional[str]

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING']]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisEndpointOptionsTypeDef]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisEndpointOptionsTypeDef]

### IncludeReturnPath
- **Type**: typing.Optional[bool]

### UseMiddleboxes
- **Type**: typing.Optional[bool]

### ForwardPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisPathTypeDef]

### ReturnPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisPathTypeDef]


# RouteTableIdentifierTypeDef

### TransitGatewayRouteTableArn
- **Type**: typing.Optional[str]

### CoreNetworkSegmentEdge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkSegmentEdgeIdentifierTypeDef]

### CoreNetworkNetworkFunctionGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkNetworkFunctionGroupIdentifierTypeDef]


# ServiceInsertionActionTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['send-to', 'send-via']]

### Mode
- **Type**: typing.Optional[typing.Literal['dual-hop', 'single-hop']]

### WhenSentTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.WhenSentToTypeDef]

### Via
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ViaTypeDef]


# ServiceInsertionSegmentsTypeDef

### SendVia
- **Type**: typing.Optional[typing.List[str]]

### SendTo
- **Type**: typing.Optional[typing.List[str]]


# SiteToSiteVpnAttachmentTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef]

### VpnConnectionArn
- **Type**: typing.Optional[str]


# SiteTypeDef

### SiteId
- **Type**: typing.Optional[str]

### SiteArn
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.LocationTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'PENDING', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# StartOrganizationServiceAccessUpdateRequestTypeDef

### Action
- **Type**: <class 'str'>
- **Required**: Yes


# StartOrganizationServiceAccessUpdateResponseTypeDef

### OrganizationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.OrganizationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartRouteAnalysisRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisEndpointOptionsSpecificationTypeDef'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisEndpointOptionsSpecificationTypeDef'>
- **Required**: Yes

### IncludeReturnPath
- **Type**: typing.Optional[bool]

### UseMiddleboxes
- **Type**: typing.Optional[bool]


# StartRouteAnalysisResponseTypeDef

### RouteAnalysis
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TransitGatewayConnectPeerAssociationTypeDef

### TransitGatewayConnectPeerArn
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DELETING', 'PENDING']]


# TransitGatewayPeeringTypeDef

### Peering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PeeringTypeDef]

### TransitGatewayArn
- **Type**: typing.Optional[str]

### TransitGatewayPeeringAttachmentId
- **Type**: typing.Optional[str]


# TransitGatewayRegistrationStateReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]

### Message
- **Type**: typing.Optional[str]


# TransitGatewayRegistrationTypeDef

### GlobalNetworkId
- **Type**: typing.Optional[str]

### TransitGatewayArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRegistrationStateReasonTypeDef]


# TransitGatewayRouteTableAttachmentTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef]

### PeeringId
- **Type**: typing.Optional[str]

### TransitGatewayRouteTableArn
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectionRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: typing.Optional[str]

### ConnectedLinkId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCoreNetworkRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateCoreNetworkResponseTypeDef

### CoreNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDeviceResponseTypeDef

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDirectConnectGatewayAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeLocations
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateDirectConnectGatewayAttachmentResponseTypeDef

### DirectConnectGatewayAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DirectConnectGatewayAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGlobalNetworkRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateGlobalNetworkResponseTypeDef

### GlobalNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.GlobalNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLinkResponseTypeDef

### Link
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNetworkResourceMetadataRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UpdateNetworkResourceMetadataResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSiteRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.LocationTypeDef]


# UpdateSiteResponseTypeDef

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.SiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVpcAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### AddSubnetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### RemoveSubnetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.VpcOptionsTypeDef]


# UpdateVpcAttachmentResponseTypeDef

### VpcAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.VpcAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ViaTypeDef

### NetworkFunctionGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkFunctionGroupTypeDef]]

### WithEdgeOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.EdgeOverrideTypeDef]]


# VpcAttachmentTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentTypeDef]

### SubnetArns
- **Type**: typing.Optional[typing.List[str]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.VpcOptionsTypeDef]


# VpcOptionsTypeDef

### Ipv6Support
- **Type**: typing.Optional[bool]

### ApplianceModeSupport
- **Type**: typing.Optional[bool]


# WhenSentToTypeDef

### WhenSentToSegmentsList
- **Type**: typing.Optional[typing.List[str]]



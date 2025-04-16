# Networkmanager Classes

# AWSLocation

### Zone
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]


# AcceptAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptAttachmentResponse

### Attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Attachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# AccountStatus

### AccountId
- **Type**: typing.Optional[str]

### SLRDeploymentStatus
- **Type**: typing.Optional[str]


# AssociateConnectPeerRequest

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


# AssociateConnectPeerResponse

### ConnectPeerAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateCustomerGatewayRequest

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


# AssociateCustomerGatewayResponse

### CustomerGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CustomerGatewayAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateLinkRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateLinkResponse

### LinkAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateTransitGatewayConnectPeerRequest

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


# AssociateTransitGatewayConnectPeerResponse

### TransitGatewayConnectPeerAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayConnectPeerAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Attachment

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### ProposedSegmentChange
- **Type**: <class 'NoneType'>

### ProposedNetworkFunctionGroupChange
- **Type**: <class 'NoneType'>

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastModificationErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.AttachmentError]]


# AttachmentError

### Code
- **Type**: typing.Optional[typing.Literal['DIRECT_CONNECT_GATEWAY_EXISTING_ATTACHMENTS', 'DIRECT_CONNECT_GATEWAY_NOT_FOUND', 'DIRECT_CONNECT_GATEWAY_NO_PRIVATE_VIF', 'MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED', 'SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE', 'SUBNET_NOT_FOUND', 'SUBNET_NO_FREE_ADDRESSES', 'SUBNET_NO_IPV6_CIDRS', 'SUBNET_UNSUPPORTED_AVAILABILITY_ZONE', 'VPC_NOT_FOUND', 'VPN_CONNECTION_NOT_FOUND']]

### Message
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]


# Bandwidth

### UploadSpeed
- **Type**: typing.Optional[int]

### DownloadSpeed
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BgpOptions

### PeerAsn
- **Type**: typing.Optional[int]


# ConnectAttachment

### Attachment
- **Type**: <class 'NoneType'>

### TransportAttachmentId
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectAttachmentOptions]


# ConnectAttachmentOptions

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectPeer

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerConfiguration]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### SubnetArn
- **Type**: typing.Optional[str]

### LastModificationErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerError]]


# ConnectPeerAssociation

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


# ConnectPeerBgpConfiguration

### CoreNetworkAsn
- **Type**: typing.Optional[int]

### PeerAsn
- **Type**: typing.Optional[int]

### CoreNetworkAddress
- **Type**: typing.Optional[str]

### PeerAddress
- **Type**: typing.Optional[str]


# ConnectPeerConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectPeerError

### Code
- **Type**: typing.Optional[typing.Literal['EDGE_LOCATION_NO_FREE_IPS', 'EDGE_LOCATION_PEER_DUPLICATE', 'INVALID_INSIDE_CIDR_BLOCK', 'IP_OUTSIDE_SUBNET_CIDR_RANGE', 'NO_ASSOCIATED_CIDR_BLOCK', 'SUBNET_NOT_FOUND']]

### Message
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]


# ConnectPeerSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### SubnetArn
- **Type**: typing.Optional[str]


# Connection

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]


# ConnectionHealth

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoreNetwork

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkSegment]]

### NetworkFunctionGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkNetworkFunctionGroup]]

### Edges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkEdge]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]


# CoreNetworkChange

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoreNetworkChangeEvent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoreNetworkChangeEventValues

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


# CoreNetworkChangeValues

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ServiceInsertionAction]]


# CoreNetworkEdge

### EdgeLocation
- **Type**: typing.Optional[str]

### Asn
- **Type**: typing.Optional[int]

### InsideCidrBlocks
- **Type**: typing.Optional[typing.List[str]]


# CoreNetworkNetworkFunctionGroup

### Name
- **Type**: typing.Optional[str]

### EdgeLocations
- **Type**: typing.Optional[typing.List[str]]

### Segments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ServiceInsertionSegments]


# CoreNetworkNetworkFunctionGroupIdentifier

### CoreNetworkId
- **Type**: typing.Optional[str]

### NetworkFunctionGroupName
- **Type**: typing.Optional[str]

### EdgeLocation
- **Type**: typing.Optional[str]


# CoreNetworkPolicy

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicyError]]

### PolicyDocument
- **Type**: typing.Optional[str]


# CoreNetworkPolicyError

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# CoreNetworkPolicyVersion

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


# CoreNetworkSegment

### Name
- **Type**: typing.Optional[str]

### EdgeLocations
- **Type**: typing.Optional[typing.List[str]]

### SharedSegments
- **Type**: typing.Optional[typing.List[str]]


# CoreNetworkSegmentEdgeIdentifier

### CoreNetworkId
- **Type**: typing.Optional[str]

### SegmentName
- **Type**: typing.Optional[str]

### EdgeLocation
- **Type**: typing.Optional[str]


# CoreNetworkSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]


# CreateConnectAttachmentRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectAttachmentOptions'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateConnectAttachmentResponse

### ConnectAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectPeerRequest

### ConnectAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerAddress
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkAddress
- **Type**: typing.Optional[str]

### BgpOptions
- **Type**: <class 'NoneType'>

### InsideCidrBlocks
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]


# CreateConnectPeerResponse

### ConnectPeer
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectionRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]


# CreateConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCoreNetworkRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### PolicyDocument
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# CreateCoreNetworkResponse

### CoreNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeviceResponse

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Device'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDirectConnectGatewayAttachmentRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateDirectConnectGatewayAttachmentResponse

### DirectConnectGatewayAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DirectConnectGatewayAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGlobalNetworkRequest

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]


# CreateGlobalNetworkResponse

### GlobalNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.GlobalNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLinkResponse

### Link
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Link'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSiteRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Location
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]


# CreateSiteResponse

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Site'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSiteToSiteVpnAttachmentRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### VpnConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateSiteToSiteVpnAttachmentResponse

### SiteToSiteVpnAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.SiteToSiteVpnAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTransitGatewayPeeringRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateTransitGatewayPeeringResponse

### TransitGatewayPeering
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayPeering'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTransitGatewayRouteTableAttachmentRequest

### PeeringId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayRouteTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateTransitGatewayRouteTableAttachmentResponse

### TransitGatewayRouteTableAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRouteTableAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcAttachmentRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.VpcOptions]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateVpcAttachmentResponse

### VpcAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.VpcAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerGatewayAssociation

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


# DeleteAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAttachmentResponse

### Attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Attachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConnectPeerRequest

### ConnectPeerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectPeerResponse

### ConnectPeer
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConnectionRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCoreNetworkPolicyVersionRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteCoreNetworkPolicyVersionResponse

### CoreNetworkPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCoreNetworkRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCoreNetworkResponse

### CoreNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDeviceRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceResponse

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Device'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGlobalNetworkRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalNetworkResponse

### GlobalNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.GlobalNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLinkRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLinkResponse

### Link
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Link'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePeeringRequest

### PeeringId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePeeringResponse

### Peering
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Peering'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSiteRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSiteResponse

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Site'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterTransitGatewayRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTransitGatewayResponse

### TransitGatewayRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRegistration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGlobalNetworksRequest

### GlobalNetworkIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeGlobalNetworksRequestPaginate

### GlobalNetworkIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# DescribeGlobalNetworksResponse

### GlobalNetworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.GlobalNetwork]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Device

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DirectConnectGatewayAttachment

### Attachment
- **Type**: <class 'NoneType'>

### DirectConnectGatewayArn
- **Type**: typing.Optional[str]


# DisassociateConnectPeerRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectPeerId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateConnectPeerResponse

### ConnectPeerAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateCustomerGatewayRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateCustomerGatewayResponse

### CustomerGatewayAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CustomerGatewayAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateLinkRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateLinkResponse

### LinkAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateTransitGatewayConnectPeerRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayConnectPeerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateTransitGatewayConnectPeerResponse

### TransitGatewayConnectPeerAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayConnectPeerAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# EdgeOverride

### EdgeSets
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### UseEdge
- **Type**: typing.Optional[str]


# ExecuteCoreNetworkChangeSetRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# GetConnectAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectAttachmentResponse

### ConnectAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectPeerAssociationsRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectPeerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetConnectPeerAssociationsRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectPeerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetConnectPeerAssociationsResponse

### ConnectPeerAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetConnectPeerRequest

### ConnectPeerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectPeerResponse

### ConnectPeer
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectionsRequest

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


# GetConnectionsRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetConnectionsResponse

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Connection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCoreNetworkChangeEventsRequest

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


# GetCoreNetworkChangeEventsRequestPaginate

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetCoreNetworkChangeEventsResponse

### CoreNetworkChangeEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkChangeEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCoreNetworkChangeSetRequest

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


# GetCoreNetworkChangeSetRequestPaginate

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetCoreNetworkChangeSetResponse

### CoreNetworkChanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkChange]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCoreNetworkPolicyRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[typing.Literal['LATEST', 'LIVE']]


# GetCoreNetworkPolicyResponse

### CoreNetworkPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetCoreNetworkRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCoreNetworkResponse

### CoreNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetCustomerGatewayAssociationsRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCustomerGatewayAssociationsRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetCustomerGatewayAssociationsResponse

### CustomerGatewayAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CustomerGatewayAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDevicesRequest

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


# GetDevicesRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SiteId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetDevicesResponse

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Device]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDirectConnectGatewayAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDirectConnectGatewayAttachmentResponse

### DirectConnectGatewayAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DirectConnectGatewayAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetLinkAssociationsRequest

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


# GetLinkAssociationsRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetLinkAssociationsResponse

### LinkAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.LinkAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLinksResponse

### Links
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Link]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourceCountsRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourceCountsRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetNetworkResourceCountsResponse

### NetworkResourceCounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkResourceCount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourceRelationshipsRequest

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


# GetNetworkResourceRelationshipsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetNetworkResourceRelationshipsResponse

### Relationships
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Relationship]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkResourcesRequest

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


# GetNetworkResourcesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetNetworkResourcesResponse

### NetworkResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetNetworkRoutesRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteTableIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteTableIdentifier'>
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


# GetNetworkRoutesResponse

### RouteTableArn
- **Type**: <class 'str'>
- **Required**: Yes

### CoreNetworkSegmentEdge
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkSegmentEdgeIdentifier'>
- **Required**: Yes

### RouteTableType
- **Type**: typing.Literal['CORE_NETWORK_SEGMENT', 'NETWORK_FUNCTION_GROUP', 'TRANSIT_GATEWAY_ROUTE_TABLE']
- **Required**: Yes

### RouteTableTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NetworkRoutes
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkRoute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkTelemetryRequest

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


# GetNetworkTelemetryRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetNetworkTelemetryResponse

### NetworkTelemetry
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkTelemetry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetRouteAnalysisRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteAnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteAnalysisResponse

### RouteAnalysis
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysis'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetSiteToSiteVpnAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSiteToSiteVpnAttachmentResponse

### SiteToSiteVpnAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.SiteToSiteVpnAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetSitesRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetSitesRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetSitesResponse

### Sites
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Site]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayConnectPeerAssociationsRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayConnectPeerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayConnectPeerAssociationsRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayConnectPeerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetTransitGatewayConnectPeerAssociationsResponse

### TransitGatewayConnectPeerAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayConnectPeerAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayPeeringRequest

### PeeringId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransitGatewayPeeringResponse

### TransitGatewayPeering
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayPeering'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetTransitGatewayRegistrationsRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayRegistrationsRequestPaginate

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# GetTransitGatewayRegistrationsResponse

### TransitGatewayRegistrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRegistration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTransitGatewayRouteTableAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransitGatewayRouteTableAttachmentResponse

### TransitGatewayRouteTableAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRouteTableAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetVpcAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcAttachmentResponse

### VpcAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.VpcAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GlobalNetwork

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]


# Link

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LinkAssociation

### GlobalNetworkId
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### LinkAssociationState
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DELETING', 'PENDING']]


# ListAttachmentsRequest

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


# ListAttachmentsRequestPaginate

### CoreNetworkId
- **Type**: typing.Optional[str]

### AttachmentType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DIRECT_CONNECT_GATEWAY', 'SITE_TO_SITE_VPN', 'TRANSIT_GATEWAY_ROUTE_TABLE', 'VPC']]

### EdgeLocation
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_ATTACHMENT_ACCEPTANCE', 'PENDING_NETWORK_UPDATE', 'PENDING_TAG_ACCEPTANCE', 'REJECTED', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# ListAttachmentsResponse

### Attachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Attachment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectPeersRequest

### CoreNetworkId
- **Type**: typing.Optional[str]

### ConnectAttachmentId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectPeersRequestPaginate

### CoreNetworkId
- **Type**: typing.Optional[str]

### ConnectAttachmentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# ListConnectPeersResponse

### ConnectPeers
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCoreNetworkPolicyVersionsRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreNetworkPolicyVersionsRequestPaginate

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# ListCoreNetworkPolicyVersionsResponse

### CoreNetworkPolicyVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicyVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCoreNetworksRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCoreNetworksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# ListCoreNetworksResponse

### CoreNetworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationServiceAccessStatusRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationServiceAccessStatusResponse

### OrganizationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.OrganizationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPeeringsRequest

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


# ListPeeringsRequestPaginate

### CoreNetworkId
- **Type**: typing.Optional[str]

### PeeringType
- **Type**: typing.Optional[typing.Literal['TRANSIT_GATEWAY']]

### EdgeLocation
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfig]


# ListPeeringsResponse

### Peerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Peering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Location

### Address
- **Type**: typing.Optional[str]

### Latitude
- **Type**: typing.Optional[str]

### Longitude
- **Type**: typing.Optional[str]


# NetworkFunctionGroup

### Name
- **Type**: typing.Optional[str]


# NetworkResource

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### Metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# NetworkResourceCount

### ResourceType
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]


# NetworkResourceSummary

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


# NetworkRoute

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkRouteDestination

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


# NetworkTelemetry

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectionHealth]


# OrganizationStatus

### OrganizationId
- **Type**: typing.Optional[str]

### OrganizationAwsServiceAccessStatus
- **Type**: typing.Optional[str]

### SLRDeploymentStatus
- **Type**: typing.Optional[str]

### AccountStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.AccountStatus]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathComponent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Peering

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastModificationErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.PeeringError]]


# PeeringError

### Code
- **Type**: typing.Optional[typing.Literal['EDGE_LOCATION_PEER_DUPLICATE', 'INTERNAL_ERROR', 'INVALID_TRANSIT_GATEWAY_STATE', 'MISSING_PERMISSIONS', 'TRANSIT_GATEWAY_NOT_FOUND', 'TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED']]

### Message
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### MissingPermissionsContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PermissionsErrorContext]


# PermissionsErrorContext

### MissingPermission
- **Type**: typing.Optional[str]


# ProposedNetworkFunctionGroupChange

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### AttachmentPolicyRuleNumber
- **Type**: typing.Optional[int]

### NetworkFunctionGroupName
- **Type**: typing.Optional[str]


# ProposedSegmentChange

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]

### AttachmentPolicyRuleNumber
- **Type**: typing.Optional[int]

### SegmentName
- **Type**: typing.Optional[str]


# PutCoreNetworkPolicyRequest

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


# PutCoreNetworkPolicyResponse

### CoreNetworkPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyRequest

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterTransitGatewayRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterTransitGatewayResponse

### TransitGatewayRegistration
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRegistration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# RejectAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# RejectAttachmentResponse

### Attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Attachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Relationship

### From
- **Type**: typing.Optional[str]

### To
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


# RestoreCoreNetworkPolicyVersionRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# RestoreCoreNetworkPolicyVersionResponse

### CoreNetworkPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# RouteAnalysis

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisEndpointOptions]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisEndpointOptions]

### IncludeReturnPath
- **Type**: typing.Optional[bool]

### UseMiddleboxes
- **Type**: typing.Optional[bool]

### ForwardPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisPath]

### ReturnPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisPath]


# RouteAnalysisCompletion

### ResultCode
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'NOT_CONNECTED']]

### ReasonCode
- **Type**: typing.Optional[typing.Literal['BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND', 'CYCLIC_PATH_DETECTED', 'INACTIVE_ROUTE_FOR_DESTINATION_FOUND', 'MAX_HOPS_EXCEEDED', 'NO_DESTINATION_ARN_PROVIDED', 'POSSIBLE_MIDDLEBOX', 'ROUTE_NOT_FOUND', 'TRANSIT_GATEWAY_ATTACHMENT_ATTACH_ARN_NO_MATCH', 'TRANSIT_GATEWAY_ATTACHMENT_NOT_FOUND', 'TRANSIT_GATEWAY_ATTACHMENT_NOT_IN_TRANSIT_GATEWAY', 'TRANSIT_GATEWAY_ATTACHMENT_STABLE_ROUTE_TABLE_NOT_FOUND']]

### ReasonContext
- **Type**: typing.Optional[typing.Dict[str, str]]


# RouteAnalysisEndpointOptions

### TransitGatewayAttachmentArn
- **Type**: typing.Optional[str]

### TransitGatewayArn
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# RouteAnalysisEndpointOptionsSpecification

### TransitGatewayAttachmentArn
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# RouteAnalysisPath

### CompletionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisCompletion]

### Path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.PathComponent]]


# RouteTableIdentifier

### TransitGatewayRouteTableArn
- **Type**: typing.Optional[str]

### CoreNetworkSegmentEdge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkSegmentEdgeIdentifier]

### CoreNetworkNetworkFunctionGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkNetworkFunctionGroupIdentifier]


# ServiceInsertionAction

### Action
- **Type**: typing.Optional[typing.Literal['send-to', 'send-via']]

### Mode
- **Type**: typing.Optional[typing.Literal['dual-hop', 'single-hop']]

### WhenSentTo
- **Type**: <class 'NoneType'>

### Via
- **Type**: <class 'NoneType'>


# ServiceInsertionSegments

### SendVia
- **Type**: typing.Optional[typing.List[str]]

### SendTo
- **Type**: typing.Optional[typing.List[str]]


# Site

### SiteId
- **Type**: typing.Optional[str]

### SiteArn
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Location
- **Type**: <class 'NoneType'>

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'PENDING', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]]


# SiteToSiteVpnAttachment

### Attachment
- **Type**: <class 'NoneType'>

### VpnConnectionArn
- **Type**: typing.Optional[str]


# StartOrganizationServiceAccessUpdateRequest

### Action
- **Type**: <class 'str'>
- **Required**: Yes


# StartOrganizationServiceAccessUpdateResponse

### OrganizationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.OrganizationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# StartRouteAnalysisRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisEndpointOptionsSpecification'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysisEndpointOptionsSpecification'>
- **Required**: Yes

### IncludeReturnPath
- **Type**: typing.Optional[bool]

### UseMiddleboxes
- **Type**: typing.Optional[bool]


# StartRouteAnalysisResponse

### RouteAnalysis
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.RouteAnalysis'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.Tag]
- **Required**: Yes


# TransitGatewayConnectPeerAssociation

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


# TransitGatewayPeering

### Peering
- **Type**: <class 'NoneType'>

### TransitGatewayArn
- **Type**: typing.Optional[str]

### TransitGatewayPeeringAttachmentId
- **Type**: typing.Optional[str]


# TransitGatewayRegistration

### GlobalNetworkId
- **Type**: typing.Optional[str]

### TransitGatewayArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.TransitGatewayRegistrationStateReason]


# TransitGatewayRegistrationStateReason

### Code
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]

### Message
- **Type**: typing.Optional[str]


# TransitGatewayRouteTableAttachment

### Attachment
- **Type**: <class 'NoneType'>

### PeeringId
- **Type**: typing.Optional[str]

### TransitGatewayRouteTableArn
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectionRequest

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


# UpdateConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCoreNetworkRequest

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateCoreNetworkResponse

### CoreNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDeviceResponse

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Device'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDirectConnectGatewayAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeLocations
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateDirectConnectGatewayAttachmentResponse

### DirectConnectGatewayAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DirectConnectGatewayAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGlobalNetworkRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateGlobalNetworkResponse

### GlobalNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.GlobalNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLinkResponse

### Link
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Link'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNetworkResourceMetadataRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UpdateNetworkResourceMetadataResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSiteRequest

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Location
- **Type**: <class 'NoneType'>


# UpdateSiteResponse

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.Site'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVpcAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### AddSubnetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### RemoveSubnetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.VpcOptions]


# UpdateVpcAttachmentResponse

### VpcAttachment
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.VpcAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadata'>
- **Required**: Yes


# Via

### NetworkFunctionGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkFunctionGroup]]

### WithEdgeOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.EdgeOverride]]


# VpcAttachment

### Attachment
- **Type**: <class 'NoneType'>

### SubnetArns
- **Type**: typing.Optional[typing.List[str]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.VpcOptions]


# VpcOptions

### Ipv6Support
- **Type**: typing.Optional[bool]

### ApplianceModeSupport
- **Type**: typing.Optional[bool]


# WhenSentTo

### WhenSentToSegmentsList
- **Type**: typing.Optional[typing.List[str]]



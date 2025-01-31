# Networkmanager Classes

# AWSLocationTypeDef

### Zone
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]


# AcceptAttachmentRequestRequestTypeDef

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


# AssociateConnectPeerRequestRequestTypeDef

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


# AssociateCustomerGatewayRequestRequestTypeDef

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


# AssociateLinkRequestRequestTypeDef

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


# AssociateTransitGatewayConnectPeerRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED', 'SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE', 'SUBNET_NOT_FOUND', 'SUBNET_NO_FREE_ADDRESSES', 'SUBNET_NO_IPV6_CIDRS', 'SUBNET_UNSUPPORTED_AVAILABILITY_ZONE', 'VPC_NOT_FOUND', 'VPN_CONNECTION_NOT_FOUND']]

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
- **Type**: typing.Optional[typing.Literal['CONNECT', 'SITE_TO_SITE_VPN', 'TRANSIT_GATEWAY_ROUTE_TABLE', 'VPC']]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_ATTACHMENT_ACCEPTANCE', 'PENDING_NETWORK_UPDATE', 'PENDING_TAG_ACCEPTANCE', 'REJECTED', 'UPDATING']]

### EdgeLocation
- **Type**: typing.Optional[str]

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

### Protocol
- **Type**: typing.Optional[typing.Literal['GRE', 'NO_ENCAP']]


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

### CoreNetworkAddress
- **Type**: typing.Optional[str]

### PeerAddress
- **Type**: typing.Optional[str]

### InsideCidrBlocks
- **Type**: typing.Optional[typing.List[str]]

### Protocol
- **Type**: typing.Optional[typing.Literal['GRE', 'NO_ENCAP']]

### BgpConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.ConnectPeerBgpConfigurationTypeDef]]


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

### Type
- **Type**: typing.Optional[typing.Literal['BGP', 'IPSEC']]

### Status
- **Type**: typing.Optional[typing.Literal['DOWN', 'UP']]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


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

### Type
- **Type**: typing.Optional[typing.Literal['ATTACHMENT_MAPPING', 'ATTACHMENT_POLICIES_CONFIGURATION', 'ATTACHMENT_ROUTE_PROPAGATION', 'ATTACHMENT_ROUTE_STATIC', 'CORE_NETWORK_CONFIGURATION', 'CORE_NETWORK_EDGE', 'CORE_NETWORK_SEGMENT', 'NETWORK_FUNCTION_GROUP', 'SEGMENTS_CONFIGURATION', 'SEGMENT_ACTIONS_CONFIGURATION']]

### Action
- **Type**: typing.Optional[typing.Literal['ADD', 'MODIFY', 'REMOVE']]

### IdentifierPath
- **Type**: typing.Optional[str]

### EventTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED']]

### Values
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkChangeEventValuesTypeDef]


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

### Type
- **Type**: typing.Optional[typing.Literal['ATTACHMENT_MAPPING', 'ATTACHMENT_POLICIES_CONFIGURATION', 'ATTACHMENT_ROUTE_PROPAGATION', 'ATTACHMENT_ROUTE_STATIC', 'CORE_NETWORK_CONFIGURATION', 'CORE_NETWORK_EDGE', 'CORE_NETWORK_SEGMENT', 'NETWORK_FUNCTION_GROUP', 'SEGMENTS_CONFIGURATION', 'SEGMENT_ACTIONS_CONFIGURATION']]

### Action
- **Type**: typing.Optional[typing.Literal['ADD', 'MODIFY', 'REMOVE']]

### Identifier
- **Type**: typing.Optional[str]

### PreviousValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkChangeValuesTypeDef]

### NewValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.CoreNetworkChangeValuesTypeDef]

### IdentifierPath
- **Type**: typing.Optional[str]


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


# CreateConnectAttachmentRequestRequestTypeDef

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


# CreateConnectPeerRequestRequestTypeDef

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


# CreateConnectionRequestRequestTypeDef

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


# CreateCoreNetworkRequestRequestTypeDef

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


# CreateDeviceRequestRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### AWSLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.AWSLocationTypeDef]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Vendor
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.LocationTypeDef]

### SiteId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# CreateDeviceResponseTypeDef

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGlobalNetworkRequestRequestTypeDef

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


# CreateLinkRequestRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Bandwidth
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.BandwidthTypeDef'>
- **Required**: Yes

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Provider
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# CreateLinkResponseTypeDef

### Link
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSiteRequestRequestTypeDef

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


# CreateSiteToSiteVpnAttachmentRequestRequestTypeDef

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


# CreateTransitGatewayPeeringRequestRequestTypeDef

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


# CreateTransitGatewayRouteTableAttachmentRequestRequestTypeDef

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


# CreateVpcAttachmentRequestRequestTypeDef

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


# DeleteAttachmentRequestRequestTypeDef

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


# DeleteConnectPeerRequestRequestTypeDef

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


# DeleteConnectionRequestRequestTypeDef

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


# DeleteCoreNetworkPolicyVersionRequestRequestTypeDef

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


# DeleteCoreNetworkRequestRequestTypeDef

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


# DeleteDeviceRequestRequestTypeDef

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


# DeleteGlobalNetworkRequestRequestTypeDef

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


# DeleteLinkRequestRequestTypeDef

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


# DeletePeeringRequestRequestTypeDef

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


# DeleteResourcePolicyRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSiteRequestRequestTypeDef

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


# DeregisterTransitGatewayRequestRequestTypeDef

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


# DescribeGlobalNetworksRequestDescribeGlobalNetworksPaginateTypeDef

### GlobalNetworkIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# DescribeGlobalNetworksRequestRequestTypeDef

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

### DeviceId
- **Type**: typing.Optional[str]

### DeviceArn
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### AWSLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.AWSLocationTypeDef]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Vendor
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.LocationTypeDef]

### SiteId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'PENDING', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# DisassociateConnectPeerRequestRequestTypeDef

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


# DisassociateCustomerGatewayRequestRequestTypeDef

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


# DisassociateLinkRequestRequestTypeDef

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


# DisassociateTransitGatewayConnectPeerRequestRequestTypeDef

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


# ExecuteCoreNetworkChangeSetRequestRequestTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes


# GetConnectAttachmentRequestRequestTypeDef

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


# GetConnectPeerAssociationsRequestGetConnectPeerAssociationsPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectPeerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetConnectPeerAssociationsRequestRequestTypeDef

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


# GetConnectPeerRequestRequestTypeDef

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


# GetConnectionsRequestGetConnectionsPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetConnectionsRequestRequestTypeDef

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


# GetCoreNetworkChangeEventsRequestGetCoreNetworkChangeEventsPaginateTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetCoreNetworkChangeEventsRequestRequestTypeDef

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


# GetCoreNetworkChangeSetRequestGetCoreNetworkChangeSetPaginateTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetCoreNetworkChangeSetRequestRequestTypeDef

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


# GetCoreNetworkPolicyRequestRequestTypeDef

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


# GetCoreNetworkRequestRequestTypeDef

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


# GetCustomerGatewayAssociationsRequestGetCustomerGatewayAssociationsPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetCustomerGatewayAssociationsRequestRequestTypeDef

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


# GetDevicesRequestGetDevicesPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SiteId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetDevicesRequestRequestTypeDef

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


# GetLinkAssociationsRequestGetLinkAssociationsPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: typing.Optional[str]

### LinkId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetLinkAssociationsRequestRequestTypeDef

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


# GetLinksRequestGetLinksPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SiteId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Provider
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetLinksRequestRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SiteId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Provider
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

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


# GetNetworkResourceCountsRequestGetNetworkResourceCountsPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetNetworkResourceCountsRequestRequestTypeDef

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


# GetNetworkResourceRelationshipsRequestGetNetworkResourceRelationshipsPaginateTypeDef

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


# GetNetworkResourceRelationshipsRequestRequestTypeDef

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


# GetNetworkResourcesRequestGetNetworkResourcesPaginateTypeDef

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


# GetNetworkResourcesRequestRequestTypeDef

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


# GetNetworkRoutesRequestRequestTypeDef

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


# GetNetworkTelemetryRequestGetNetworkTelemetryPaginateTypeDef

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


# GetNetworkTelemetryRequestRequestTypeDef

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


# GetResourcePolicyRequestRequestTypeDef

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


# GetRouteAnalysisRequestRequestTypeDef

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


# GetSiteToSiteVpnAttachmentRequestRequestTypeDef

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


# GetSitesRequestGetSitesPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### SiteIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetSitesRequestRequestTypeDef

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


# GetTransitGatewayConnectPeerAssociationsRequestGetTransitGatewayConnectPeerAssociationsPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayConnectPeerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef

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


# GetTransitGatewayPeeringRequestRequestTypeDef

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


# GetTransitGatewayRegistrationsRequestGetTransitGatewayRegistrationsPaginateTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### TransitGatewayArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# GetTransitGatewayRegistrationsRequestRequestTypeDef

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


# GetTransitGatewayRouteTableAttachmentRequestRequestTypeDef

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


# GetVpcAttachmentRequestRequestTypeDef

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

### LinkId
- **Type**: typing.Optional[str]

### LinkArn
- **Type**: typing.Optional[str]

### GlobalNetworkId
- **Type**: typing.Optional[str]

### SiteId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Bandwidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.BandwidthTypeDef]

### Provider
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'PENDING', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.TagTypeDef]]


# ListAttachmentsRequestListAttachmentsPaginateTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### AttachmentType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'SITE_TO_SITE_VPN', 'TRANSIT_GATEWAY_ROUTE_TABLE', 'VPC']]

### EdgeLocation
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'PENDING_ATTACHMENT_ACCEPTANCE', 'PENDING_NETWORK_UPDATE', 'PENDING_TAG_ACCEPTANCE', 'REJECTED', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListAttachmentsRequestRequestTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### AttachmentType
- **Type**: typing.Optional[typing.Literal['CONNECT', 'SITE_TO_SITE_VPN', 'TRANSIT_GATEWAY_ROUTE_TABLE', 'VPC']]

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


# ListConnectPeersRequestListConnectPeersPaginateTypeDef

### CoreNetworkId
- **Type**: typing.Optional[str]

### ConnectAttachmentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListConnectPeersRequestRequestTypeDef

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


# ListCoreNetworkPolicyVersionsRequestListCoreNetworkPolicyVersionsPaginateTypeDef

### CoreNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListCoreNetworkPolicyVersionsRequestRequestTypeDef

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


# ListCoreNetworksRequestListCoreNetworksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.PaginatorConfigTypeDef]


# ListCoreNetworksRequestRequestTypeDef

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


# ListOrganizationServiceAccessStatusRequestRequestTypeDef

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


# ListPeeringsRequestListPeeringsPaginateTypeDef

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


# ListPeeringsRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkRouteDestinationTypeDef]]

### PrefixListId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'BLACKHOLE']]

### Type
- **Type**: typing.Optional[typing.Literal['PROPAGATED', 'STATIC']]


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

### Sequence
- **Type**: typing.Optional[int]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.NetworkResourceSummaryTypeDef]

### DestinationCidrBlock
- **Type**: typing.Optional[str]


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


# PutCoreNetworkPolicyRequestRequestTypeDef

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


# PutResourcePolicyRequestRequestTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterTransitGatewayRequestRequestTypeDef

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


# RejectAttachmentRequestRequestTypeDef

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


# RestoreCoreNetworkPolicyVersionRequestRequestTypeDef

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


# StartOrganizationServiceAccessUpdateRequestRequestTypeDef

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


# StartRouteAnalysisRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectionRequestRequestTypeDef

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


# UpdateCoreNetworkRequestRequestTypeDef

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


# UpdateDeviceRequestRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### AWSLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.AWSLocationTypeDef]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Vendor
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.LocationTypeDef]

### SiteId
- **Type**: typing.Optional[str]


# UpdateDeviceResponseTypeDef

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.DeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGlobalNetworkRequestRequestTypeDef

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


# UpdateLinkRequestRequestTypeDef

### GlobalNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Bandwidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.networkmanager_classes.BandwidthTypeDef]

### Provider
- **Type**: typing.Optional[str]


# UpdateLinkResponseTypeDef

### Link
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.LinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.networkmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNetworkResourceMetadataRequestRequestTypeDef

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


# UpdateSiteRequestRequestTypeDef

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


# UpdateVpcAttachmentRequestRequestTypeDef

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



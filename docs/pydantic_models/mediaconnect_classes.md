# mediaconnect_classes

# AddBridgeFlowSourceRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FlowVpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]


# AddBridgeNetworkOutputRequestTypeDef

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']
- **Required**: Yes

### Ttl
- **Type**: <class 'int'>
- **Required**: Yes


# AddBridgeNetworkSourceRequestTypeDef

### MulticastIp
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']
- **Required**: Yes


# AddBridgeOutputRequestTypeDef

### NetworkOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeNetworkOutputRequestTypeDef]


# AddBridgeOutputsRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeOutputRequestTypeDef]
- **Required**: Yes


# AddBridgeOutputsResponseTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddBridgeSourceRequestTypeDef

### FlowSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeFlowSourceRequestTypeDef]

### NetworkSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeNetworkSourceRequestTypeDef]


# AddBridgeSourcesRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeSourceRequestTypeDef]
- **Required**: Yes


# AddBridgeSourcesResponseTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddEgressGatewayBridgeRequestTypeDef

### MaxBitrate
- **Type**: <class 'int'>
- **Required**: Yes


# AddFlowMediaStreamsRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreams
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddMediaStreamRequestTypeDef]
- **Required**: Yes


# AddFlowMediaStreamsResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreams
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddFlowOutputsRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddOutputRequestTypeDef]
- **Required**: Yes


# AddFlowOutputsResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.OutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddFlowSourcesRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.SetSourceRequestTypeDef]
- **Required**: Yes


# AddFlowSourcesResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.SourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddFlowVpcInterfacesRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaces
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceRequestTypeDef]
- **Required**: Yes


# AddFlowVpcInterfacesResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddIngressGatewayBridgeRequestTypeDef

### MaxBitrate
- **Type**: <class 'int'>
- **Required**: Yes

### MaxOutputs
- **Type**: <class 'int'>
- **Required**: Yes


# AddMaintenanceTypeDef

### MaintenanceDay
- **Type**: typing.Literal['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
- **Required**: Yes

### MaintenanceStartHour
- **Type**: <class 'str'>
- **Required**: Yes


# AddMediaStreamRequestTypeDef

### MediaStreamId
- **Type**: <class 'int'>
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreamType
- **Type**: typing.Literal['ancillary-data', 'audio', 'video']
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamAttributesRequestTypeDef]

### ClockRate
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### VideoFormat
- **Type**: typing.Optional[str]


# AddOutputRequestTypeDef

### Protocol
- **Type**: typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']
- **Required**: Yes

### CidrAllowList
- **Type**: typing.Optional[typing.Sequence[str]]

### Description
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncryptionTypeDef]

### MaxLatency
- **Type**: typing.Optional[int]

### MediaStreamOutputConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamOutputConfigurationRequestTypeDef]]

### MinLatency
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### RemoteId
- **Type**: typing.Optional[str]

### SenderControlPort
- **Type**: typing.Optional[int]

### SmoothingLatency
- **Type**: typing.Optional[int]

### StreamId
- **Type**: typing.Optional[str]

### VpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]

### OutputStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BridgeFlowOutputTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# BridgeFlowSourceTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FlowVpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]

### OutputArn
- **Type**: typing.Optional[str]


# BridgeNetworkOutputTypeDef

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']
- **Required**: Yes

### Ttl
- **Type**: <class 'int'>
- **Required**: Yes


# BridgeNetworkSourceTypeDef

### MulticastIp
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']
- **Required**: Yes


# BridgeOutputTypeDef

### FlowOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeFlowOutputTypeDef]

### NetworkOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeNetworkOutputTypeDef]


# BridgeSourceTypeDef

### FlowSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeFlowSourceTypeDef]

### NetworkSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeNetworkSourceTypeDef]


# BridgeTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### BridgeState
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'DEPLOYING', 'STANDBY', 'STARTING', 'START_FAILED', 'START_PENDING', 'STOPPING', 'STOP_FAILED', 'UPDATING']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlacementArn
- **Type**: <class 'str'>
- **Required**: Yes

### BridgeMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetailTypeDef]]

### EgressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EgressGatewayBridgeTypeDef]

### IngressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.IngressGatewayBridgeTypeDef]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeOutputTypeDef]]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FailoverConfigTypeDef]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeSourceTypeDef]]


# CreateBridgeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlacementArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeSourceRequestTypeDef]
- **Required**: Yes

### EgressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddEgressGatewayBridgeRequestTypeDef]

### IngressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddIngressGatewayBridgeRequestTypeDef]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeOutputRequestTypeDef]]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FailoverConfigTypeDef]


# CreateBridgeResponseTypeDef

### Bridge
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFlowRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### Entitlements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.GrantEntitlementRequestTypeDef]]

### MediaStreams
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddMediaStreamRequestTypeDef]]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddOutputRequestTypeDef]]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.SetSourceRequestTypeDef]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FailoverConfigTypeDef]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.SetSourceRequestTypeDef]]

### VpcInterfaces
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceRequestTypeDef]]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddMaintenanceTypeDef]


# CreateFlowResponseTypeDef

### Flow
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.FlowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGatewayRequestRequestTypeDef

### EgressCidrBlocks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Networks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayNetworkTypeDef]
- **Required**: Yes


# CreateGatewayResponseTypeDef

### Gateway
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBridgeRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBridgeResponseTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFlowRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGatewayRequestRequestTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGatewayResponseTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterGatewayInstanceRequestRequestTypeDef

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# DeregisterGatewayInstanceResponseTypeDef

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceState
- **Type**: typing.Literal['ACTIVE', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_ERROR', 'REGISTERING', 'REGISTRATION_ERROR']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBridgeRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBridgeResponseTypeDef

### Bridge
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFlowRequestFlowActiveWaitTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.WaiterConfigTypeDef]


# DescribeFlowRequestFlowDeletedWaitTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.WaiterConfigTypeDef]


# DescribeFlowRequestFlowStandbyWaitTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.WaiterConfigTypeDef]


# DescribeFlowRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowResponseTypeDef

### Flow
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.FlowTypeDef'>
- **Required**: Yes

### Messages
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.MessagesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFlowSourceMetadataRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowSourceMetadataResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetailTypeDef]
- **Required**: Yes

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TransportMediaInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.TransportMediaInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGatewayInstanceRequestRequestTypeDef

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayInstanceResponseTypeDef

### GatewayInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGatewayRequestRequestTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayResponseTypeDef

### Gateway
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOfferingRequestRequestTypeDef

### OfferingArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOfferingResponseTypeDef

### Offering
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.OfferingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReservationRequestRequestTypeDef

### ReservationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReservationResponseTypeDef

### Reservation
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ReservationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationConfigurationRequestTypeDef

### DestinationIp
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPort
- **Type**: <class 'int'>
- **Required**: Yes

### Interface
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.InterfaceRequestTypeDef'>
- **Required**: Yes


# DestinationConfigurationTypeDef

### DestinationIp
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPort
- **Type**: <class 'int'>
- **Required**: Yes

### Interface
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.InterfaceTypeDef'>
- **Required**: Yes

### OutboundIp
- **Type**: <class 'str'>
- **Required**: Yes


# EgressGatewayBridgeTypeDef

### MaxBitrate
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncodingParametersRequestTypeDef

### CompressionFactor
- **Type**: <class 'float'>
- **Required**: Yes

### EncoderProfile
- **Type**: typing.Literal['high', 'main']
- **Required**: Yes


# EncodingParametersTypeDef

### CompressionFactor
- **Type**: <class 'float'>
- **Required**: Yes

### EncoderProfile
- **Type**: typing.Literal['high', 'main']
- **Required**: Yes


# EncryptionTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Algorithm
- **Type**: typing.Optional[typing.Literal['aes128', 'aes192', 'aes256']]

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### KeyType
- **Type**: typing.Optional[typing.Literal['speke', 'srt-password', 'static-key']]

### Region
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# EntitlementTypeDef

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Subscribers
- **Type**: typing.List[str]
- **Required**: Yes

### DataTransferSubscriberFeePercent
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncryptionTypeDef]

### EntitlementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FailoverConfigTypeDef

### FailoverMode
- **Type**: typing.Optional[typing.Literal['FAILOVER', 'MERGE']]

### RecoveryWindow
- **Type**: typing.Optional[int]

### SourcePriority
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.SourcePriorityTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FlowTypeDef

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.EntitlementTypeDef]
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.OutputTypeDef]
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.SourceTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EgressIp
- **Type**: typing.Optional[str]

### MediaStreams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamTypeDef]]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FailoverConfigTypeDef]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.SourceTypeDef]]

### VpcInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceTypeDef]]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MaintenanceTypeDef]


# FmtpRequestTypeDef

### ChannelOrder
- **Type**: typing.Optional[str]

### Colorimetry
- **Type**: typing.Optional[typing.Literal['BT2020', 'BT2100', 'BT601', 'BT709', 'ST2065-1', 'ST2065-3', 'XYZ']]

### ExactFramerate
- **Type**: typing.Optional[str]

### Par
- **Type**: typing.Optional[str]

### Range
- **Type**: typing.Optional[typing.Literal['FULL', 'FULLPROTECT', 'NARROW']]

### ScanMode
- **Type**: typing.Optional[typing.Literal['interlace', 'progressive', 'progressive-segmented-frame']]

### Tcs
- **Type**: typing.Optional[typing.Literal['BT2100LINHLG', 'BT2100LINPQ', 'DENSITY', 'HLG', 'LINEAR', 'PQ', 'SDR', 'ST2065-1', 'ST428-1']]


# FmtpTypeDef

### ChannelOrder
- **Type**: typing.Optional[str]

### Colorimetry
- **Type**: typing.Optional[typing.Literal['BT2020', 'BT2100', 'BT601', 'BT709', 'ST2065-1', 'ST2065-3', 'XYZ']]

### ExactFramerate
- **Type**: typing.Optional[str]

### Par
- **Type**: typing.Optional[str]

### Range
- **Type**: typing.Optional[typing.Literal['FULL', 'FULLPROTECT', 'NARROW']]

### ScanMode
- **Type**: typing.Optional[typing.Literal['interlace', 'progressive', 'progressive-segmented-frame']]

### Tcs
- **Type**: typing.Optional[typing.Literal['BT2100LINHLG', 'BT2100LINPQ', 'DENSITY', 'HLG', 'LINEAR', 'PQ', 'SDR', 'ST2065-1', 'ST428-1']]


# FrameResolutionTypeDef

### FrameHeight
- **Type**: <class 'int'>
- **Required**: Yes

### FrameWidth
- **Type**: <class 'int'>
- **Required**: Yes


# GatewayBridgeSourceTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]


# GatewayInstanceTypeDef

### BridgePlacement
- **Type**: typing.Literal['AVAILABLE', 'LOCKED']
- **Required**: Yes

### ConnectionStatus
- **Type**: typing.Literal['CONNECTED', 'DISCONNECTED']
- **Required**: Yes

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceState
- **Type**: typing.Literal['ACTIVE', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_ERROR', 'REGISTERING', 'REGISTRATION_ERROR']
- **Required**: Yes

### RunningBridgeCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetailTypeDef]]


# GatewayNetworkTypeDef

### CidrBlock
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GatewayTypeDef

### EgressCidrBlocks
- **Type**: typing.List[str]
- **Required**: Yes

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayNetworkTypeDef]
- **Required**: Yes

### GatewayMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetailTypeDef]]

### GatewayState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'ERROR', 'UPDATING']]


# GrantEntitlementRequestTypeDef

### Subscribers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DataTransferSubscriberFeePercent
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncryptionTypeDef]

### EntitlementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Name
- **Type**: typing.Optional[str]


# GrantFlowEntitlementsRequestRequestTypeDef

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.GrantEntitlementRequestTypeDef]
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# GrantFlowEntitlementsResponseTypeDef

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.EntitlementTypeDef]
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IngressGatewayBridgeTypeDef

### MaxBitrate
- **Type**: <class 'int'>
- **Required**: Yes

### MaxOutputs
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]


# InputConfigurationRequestTypeDef

### InputPort
- **Type**: <class 'int'>
- **Required**: Yes

### Interface
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.InterfaceRequestTypeDef'>
- **Required**: Yes


# InputConfigurationTypeDef

### InputIp
- **Type**: <class 'str'>
- **Required**: Yes

### InputPort
- **Type**: <class 'int'>
- **Required**: Yes

### Interface
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.InterfaceTypeDef'>
- **Required**: Yes


# InterfaceRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# InterfaceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ListBridgesRequestListBridgesPaginateTypeDef

### FilterArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfigTypeDef]


# ListBridgesRequestRequestTypeDef

### FilterArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBridgesResponseTypeDef

### Bridges
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedBridgeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitlementsRequestListEntitlementsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfigTypeDef]


# ListEntitlementsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEntitlementsResponseTypeDef

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedEntitlementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlowsRequestListFlowsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfigTypeDef]


# ListFlowsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFlowsResponseTypeDef

### Flows
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedFlowTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGatewayInstancesRequestListGatewayInstancesPaginateTypeDef

### FilterArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfigTypeDef]


# ListGatewayInstancesRequestRequestTypeDef

### FilterArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGatewayInstancesResponseTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedGatewayInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGatewaysRequestListGatewaysPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfigTypeDef]


# ListGatewaysRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGatewaysResponseTypeDef

### Gateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedGatewayTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequestListOfferingsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfigTypeDef]


# ListOfferingsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOfferingsResponseTypeDef

### Offerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.OfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReservationsRequestListReservationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfigTypeDef]


# ListReservationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReservationsResponseTypeDef

### Reservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ReservationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListedBridgeTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### BridgeState
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'DEPLOYING', 'STANDBY', 'STARTING', 'START_FAILED', 'START_PENDING', 'STOPPING', 'STOP_FAILED', 'UPDATING']
- **Required**: Yes

### BridgeType
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlacementArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListedEntitlementTypeDef

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementName
- **Type**: <class 'str'>
- **Required**: Yes

### DataTransferSubscriberFeePercent
- **Type**: typing.Optional[int]


# ListedFlowTypeDef

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Literal['ENTITLED', 'OWNED']
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MaintenanceTypeDef]


# ListedGatewayInstanceTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_ERROR', 'REGISTERING', 'REGISTRATION_ERROR']]


# ListedGatewayTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayState
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# MaintenanceTypeDef

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']]

### MaintenanceDeadline
- **Type**: typing.Optional[str]

### MaintenanceScheduledDate
- **Type**: typing.Optional[str]

### MaintenanceStartHour
- **Type**: typing.Optional[str]


# MediaStreamAttributesRequestTypeDef

### Fmtp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FmtpRequestTypeDef]

### Lang
- **Type**: typing.Optional[str]


# MediaStreamAttributesTypeDef

### Fmtp
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.FmtpTypeDef'>
- **Required**: Yes

### Lang
- **Type**: typing.Optional[str]


# MediaStreamOutputConfigurationRequestTypeDef

### EncodingName
- **Type**: typing.Literal['jxsv', 'pcm', 'raw', 'smpte291']
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.DestinationConfigurationRequestTypeDef]]

### EncodingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncodingParametersRequestTypeDef]


# MediaStreamOutputConfigurationTypeDef

### EncodingName
- **Type**: typing.Literal['jxsv', 'pcm', 'raw', 'smpte291']
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.DestinationConfigurationTypeDef]]

### EncodingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncodingParametersTypeDef]


# MediaStreamSourceConfigurationRequestTypeDef

### EncodingName
- **Type**: typing.Literal['jxsv', 'pcm', 'raw', 'smpte291']
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.InputConfigurationRequestTypeDef]]


# MediaStreamSourceConfigurationTypeDef

### EncodingName
- **Type**: typing.Literal['jxsv', 'pcm', 'raw', 'smpte291']
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.InputConfigurationTypeDef]]


# MediaStreamTypeDef

### Fmt
- **Type**: <class 'int'>
- **Required**: Yes

### MediaStreamId
- **Type**: <class 'int'>
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreamType
- **Type**: typing.Literal['ancillary-data', 'audio', 'video']
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamAttributesTypeDef]

### ClockRate
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### VideoFormat
- **Type**: typing.Optional[str]


# MessageDetailTypeDef

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: typing.Optional[str]


# MessagesTypeDef

### Errors
- **Type**: typing.List[str]
- **Required**: Yes


# OfferingTypeDef

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### DurationUnits
- **Type**: typing.Literal['MONTHS']
- **Required**: Yes

### OfferingArn
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingDescription
- **Type**: <class 'str'>
- **Required**: Yes

### PricePerUnit
- **Type**: <class 'str'>
- **Required**: Yes

### PriceUnits
- **Type**: typing.Literal['HOURLY']
- **Required**: Yes

### ResourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResourceSpecificationTypeDef'>
- **Required**: Yes


# OutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataTransferSubscriberFeePercent
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncryptionTypeDef]

### EntitlementArn
- **Type**: typing.Optional[str]

### ListenerAddress
- **Type**: typing.Optional[str]

### MediaLiveInputArn
- **Type**: typing.Optional[str]

### MediaStreamOutputConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamOutputConfigurationTypeDef]]

### Port
- **Type**: typing.Optional[int]

### Transport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.TransportTypeDef]

### VpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]

### BridgeArn
- **Type**: typing.Optional[str]

### BridgePorts
- **Type**: typing.Optional[typing.List[int]]

### OutputStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PurchaseOfferingRequestRequestTypeDef

### OfferingArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### Start
- **Type**: <class 'str'>
- **Required**: Yes


# PurchaseOfferingResponseTypeDef

### Reservation
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ReservationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveBridgeOutputRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveBridgeOutputResponseTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveBridgeSourceRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveBridgeSourceResponseTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveFlowMediaStreamRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFlowMediaStreamResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveFlowOutputRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFlowOutputResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveFlowSourceRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFlowSourceResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveFlowVpcInterfaceRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFlowVpcInterfaceResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### NonDeletedNetworkInterfaceIds
- **Type**: typing.List[str]
- **Required**: Yes

### VpcInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReservationTypeDef

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### DurationUnits
- **Type**: typing.Literal['MONTHS']
- **Required**: Yes

### End
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingArn
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingDescription
- **Type**: <class 'str'>
- **Required**: Yes

### PricePerUnit
- **Type**: <class 'str'>
- **Required**: Yes

### PriceUnits
- **Type**: typing.Literal['HOURLY']
- **Required**: Yes

### ReservationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationState
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'EXPIRED', 'PROCESSING']
- **Required**: Yes

### ResourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResourceSpecificationTypeDef'>
- **Required**: Yes

### Start
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceSpecificationTypeDef

### ResourceType
- **Type**: typing.Literal['Mbps_Outbound_Bandwidth']
- **Required**: Yes

### ReservedBitrate
- **Type**: typing.Optional[int]


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


# RevokeFlowEntitlementRequestRequestTypeDef

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeFlowEntitlementResponseTypeDef

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetGatewayBridgeSourceRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]


# SetSourceRequestTypeDef

### Decryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncryptionTypeDef]

### Description
- **Type**: typing.Optional[str]

### EntitlementArn
- **Type**: typing.Optional[str]

### IngestPort
- **Type**: typing.Optional[int]

### MaxBitrate
- **Type**: typing.Optional[int]

### MaxLatency
- **Type**: typing.Optional[int]

### MaxSyncBuffer
- **Type**: typing.Optional[int]

### MediaStreamSourceConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamSourceConfigurationRequestTypeDef]]

### MinLatency
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']]

### SenderControlPort
- **Type**: typing.Optional[int]

### SenderIpAddress
- **Type**: typing.Optional[str]

### SourceListenerAddress
- **Type**: typing.Optional[str]

### SourceListenerPort
- **Type**: typing.Optional[int]

### StreamId
- **Type**: typing.Optional[str]

### VpcInterfaceName
- **Type**: typing.Optional[str]

### WhitelistCidr
- **Type**: typing.Optional[str]

### GatewayBridgeSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.SetGatewayBridgeSourceRequestTypeDef]


# SourcePriorityTypeDef

### PrimarySource
- **Type**: typing.Optional[str]


# SourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataTransferSubscriberFeePercent
- **Type**: typing.Optional[int]

### Decryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncryptionTypeDef]

### Description
- **Type**: typing.Optional[str]

### EntitlementArn
- **Type**: typing.Optional[str]

### IngestIp
- **Type**: typing.Optional[str]

### IngestPort
- **Type**: typing.Optional[int]

### MediaStreamSourceConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamSourceConfigurationTypeDef]]

### SenderControlPort
- **Type**: typing.Optional[int]

### SenderIpAddress
- **Type**: typing.Optional[str]

### Transport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.TransportTypeDef]

### VpcInterfaceName
- **Type**: typing.Optional[str]

### WhitelistCidr
- **Type**: typing.Optional[str]

### GatewayBridgeSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayBridgeSourceTypeDef]


# StartFlowRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartFlowResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopFlowRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopFlowResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TransportMediaInfoTypeDef

### Programs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.TransportStreamProgramTypeDef]
- **Required**: Yes


# TransportStreamProgramTypeDef

### PcrPid
- **Type**: <class 'int'>
- **Required**: Yes

### ProgramNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ProgramPid
- **Type**: <class 'int'>
- **Required**: Yes

### Streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.TransportStreamTypeDef]
- **Required**: Yes

### ProgramName
- **Type**: typing.Optional[str]


# TransportStreamTypeDef

### Pid
- **Type**: <class 'int'>
- **Required**: Yes

### StreamType
- **Type**: <class 'str'>
- **Required**: Yes

### Channels
- **Type**: typing.Optional[int]

### Codec
- **Type**: typing.Optional[str]

### FrameRate
- **Type**: typing.Optional[str]

### FrameResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FrameResolutionTypeDef]

### SampleRate
- **Type**: typing.Optional[int]

### SampleSize
- **Type**: typing.Optional[int]


# TransportTypeDef

### Protocol
- **Type**: typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']
- **Required**: Yes

### CidrAllowList
- **Type**: typing.Optional[typing.List[str]]

### MaxBitrate
- **Type**: typing.Optional[int]

### MaxLatency
- **Type**: typing.Optional[int]

### MaxSyncBuffer
- **Type**: typing.Optional[int]

### MinLatency
- **Type**: typing.Optional[int]

### RemoteId
- **Type**: typing.Optional[str]

### SenderControlPort
- **Type**: typing.Optional[int]

### SenderIpAddress
- **Type**: typing.Optional[str]

### SmoothingLatency
- **Type**: typing.Optional[int]

### SourceListenerAddress
- **Type**: typing.Optional[str]

### SourceListenerPort
- **Type**: typing.Optional[int]

### StreamId
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBridgeFlowSourceRequestTypeDef

### FlowArn
- **Type**: typing.Optional[str]

### FlowVpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]


# UpdateBridgeNetworkOutputRequestTypeDef

### IpAddress
- **Type**: typing.Optional[str]

### NetworkName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']]

### Ttl
- **Type**: typing.Optional[int]


# UpdateBridgeNetworkSourceRequestTypeDef

### MulticastIp
- **Type**: typing.Optional[str]

### NetworkName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']]


# UpdateBridgeOutputRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputName
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateBridgeNetworkOutputRequestTypeDef]


# UpdateBridgeOutputResponseTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBridgeRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### EgressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateEgressGatewayBridgeRequestTypeDef]

### IngressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateIngressGatewayBridgeRequestTypeDef]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateFailoverConfigTypeDef]


# UpdateBridgeResponseTypeDef

### Bridge
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBridgeSourceRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateBridgeFlowSourceRequestTypeDef]

### NetworkSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateBridgeNetworkSourceRequestTypeDef]


# UpdateBridgeSourceResponseTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBridgeStateRequestRequestTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'STANDBY']
- **Required**: Yes


# UpdateBridgeStateResponseTypeDef

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'STANDBY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEgressGatewayBridgeRequestTypeDef

### MaxBitrate
- **Type**: typing.Optional[int]


# UpdateEncryptionTypeDef

### Algorithm
- **Type**: typing.Optional[typing.Literal['aes128', 'aes192', 'aes256']]

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### KeyType
- **Type**: typing.Optional[typing.Literal['speke', 'srt-password', 'static-key']]

### Region
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# UpdateFailoverConfigTypeDef

### FailoverMode
- **Type**: typing.Optional[typing.Literal['FAILOVER', 'MERGE']]

### RecoveryWindow
- **Type**: typing.Optional[int]

### SourcePriority
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.SourcePriorityTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateFlowEntitlementRequestRequestTypeDef

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateEncryptionTypeDef]

### EntitlementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Subscribers
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateFlowEntitlementResponseTypeDef

### Entitlement
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.EntitlementTypeDef'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlowMediaStreamRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamAttributesRequestTypeDef]

### ClockRate
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### MediaStreamType
- **Type**: typing.Optional[typing.Literal['ancillary-data', 'audio', 'video']]

### VideoFormat
- **Type**: typing.Optional[str]


# UpdateFlowMediaStreamResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStream
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlowOutputRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputArn
- **Type**: <class 'str'>
- **Required**: Yes

### CidrAllowList
- **Type**: typing.Optional[typing.Sequence[str]]

### Description
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateEncryptionTypeDef]

### MaxLatency
- **Type**: typing.Optional[int]

### MediaStreamOutputConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamOutputConfigurationRequestTypeDef]]

### MinLatency
- **Type**: typing.Optional[int]

### Port
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']]

### RemoteId
- **Type**: typing.Optional[str]

### SenderControlPort
- **Type**: typing.Optional[int]

### SenderIpAddress
- **Type**: typing.Optional[str]

### SmoothingLatency
- **Type**: typing.Optional[int]

### StreamId
- **Type**: typing.Optional[str]

### VpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]

### OutputStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateFlowOutputResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.OutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlowRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateFailoverConfigTypeDef]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateMaintenanceTypeDef]


# UpdateFlowResponseTypeDef

### Flow
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.FlowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlowSourceRequestRequestTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Decryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateEncryptionTypeDef]

### Description
- **Type**: typing.Optional[str]

### EntitlementArn
- **Type**: typing.Optional[str]

### IngestPort
- **Type**: typing.Optional[int]

### MaxBitrate
- **Type**: typing.Optional[int]

### MaxLatency
- **Type**: typing.Optional[int]

### MaxSyncBuffer
- **Type**: typing.Optional[int]

### MediaStreamSourceConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamSourceConfigurationRequestTypeDef]]

### MinLatency
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['cdi', 'fujitsu-qos', 'rist', 'rtp', 'rtp-fec', 'srt-caller', 'srt-listener', 'st2110-jpegxs', 'udp', 'zixi-pull', 'zixi-push']]

### SenderControlPort
- **Type**: typing.Optional[int]

### SenderIpAddress
- **Type**: typing.Optional[str]

### SourceListenerAddress
- **Type**: typing.Optional[str]

### SourceListenerPort
- **Type**: typing.Optional[int]

### StreamId
- **Type**: typing.Optional[str]

### VpcInterfaceName
- **Type**: typing.Optional[str]

### WhitelistCidr
- **Type**: typing.Optional[str]

### GatewayBridgeSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateGatewayBridgeSourceRequestTypeDef]


# UpdateFlowSourceResponseTypeDef

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.SourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGatewayBridgeSourceRequestTypeDef

### BridgeArn
- **Type**: typing.Optional[str]

### VpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachmentTypeDef]


# UpdateGatewayInstanceRequestRequestTypeDef

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### BridgePlacement
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'LOCKED']]


# UpdateGatewayInstanceResponseTypeDef

### BridgePlacement
- **Type**: typing.Literal['AVAILABLE', 'LOCKED']
- **Required**: Yes

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIngressGatewayBridgeRequestTypeDef

### MaxBitrate
- **Type**: typing.Optional[int]

### MaxOutputs
- **Type**: typing.Optional[int]


# UpdateMaintenanceTypeDef

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']]

### MaintenanceScheduledDate
- **Type**: typing.Optional[str]

### MaintenanceStartHour
- **Type**: typing.Optional[str]


# VpcInterfaceAttachmentTypeDef

### VpcInterfaceName
- **Type**: typing.Optional[str]


# VpcInterfaceRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceType
- **Type**: typing.Optional[typing.Literal['efa', 'ena']]


# VpcInterfaceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceIds
- **Type**: typing.List[str]
- **Required**: Yes

### NetworkInterfaceType
- **Type**: typing.Literal['efa', 'ena']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



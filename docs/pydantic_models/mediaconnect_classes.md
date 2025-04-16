# Mediaconnect Classes

# AddBridgeFlowSourceRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FlowVpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachment]


# AddBridgeNetworkOutputRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddBridgeNetworkSourceRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddBridgeOutputRequest

### NetworkOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeNetworkOutputRequest]


# AddBridgeOutputsRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeOutputRequest]
- **Required**: Yes


# AddBridgeOutputsResponse

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AddBridgeSourceRequest

### FlowSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeFlowSourceRequest]

### NetworkSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeNetworkSourceRequest]


# AddBridgeSourcesRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeSourceRequest]
- **Required**: Yes


# AddBridgeSourcesResponse

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AddEgressGatewayBridgeRequest

### MaxBitrate
- **Type**: <class 'int'>
- **Required**: Yes


# AddFlowMediaStreamsRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreams
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddMediaStreamRequest]
- **Required**: Yes


# AddFlowMediaStreamsResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreams
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AddFlowOutputsRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddOutputRequest]
- **Required**: Yes


# AddFlowOutputsResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.Output]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AddFlowSourcesRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.SetSourceRequest]
- **Required**: Yes


# AddFlowSourcesResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.Source]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AddFlowVpcInterfacesRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaces
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceRequest]
- **Required**: Yes


# AddFlowVpcInterfacesResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterface]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AddIngressGatewayBridgeRequest

### MaxBitrate
- **Type**: <class 'int'>
- **Required**: Yes

### MaxOutputs
- **Type**: <class 'int'>
- **Required**: Yes


# AddMaintenance

### MaintenanceDay
- **Type**: typing.Literal['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
- **Required**: Yes

### MaintenanceStartHour
- **Type**: <class 'str'>
- **Required**: Yes


# AddMediaStreamRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamAttributesRequest]

### ClockRate
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### VideoFormat
- **Type**: typing.Optional[str]


# AddOutputRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudioMonitoringSetting

### SilentAudio
- **Type**: <class 'NoneType'>


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlackFrames

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ThresholdSeconds
- **Type**: typing.Optional[int]


# Bridge

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetail]]

### EgressGatewayBridge
- **Type**: <class 'NoneType'>

### IngressGatewayBridge
- **Type**: <class 'NoneType'>

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeOutput]]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FailoverConfig]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeSource]]


# BridgeFlowOutput

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# BridgeFlowSource

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FlowVpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachment]

### OutputArn
- **Type**: typing.Optional[str]


# BridgeNetworkOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BridgeNetworkSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BridgeOutput

### FlowOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeFlowOutput]

### NetworkOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeNetworkOutput]


# BridgeSource

### FlowSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeFlowSource]

### NetworkSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeNetworkSource]


# CreateBridgeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlacementArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeSourceRequest]
- **Required**: Yes

### EgressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddEgressGatewayBridgeRequest]

### IngressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddIngressGatewayBridgeRequest]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddBridgeOutputRequest]]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FailoverConfig]


# CreateBridgeResponse

### Bridge
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Bridge'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFlowRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### Entitlements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.GrantEntitlementRequest]]

### MediaStreams
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddMediaStreamRequest]]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AddOutputRequest]]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.SetSourceRequest]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FailoverConfig]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.SetSourceRequest]]

### VpcInterfaces
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceRequest]]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.AddMaintenance]

### SourceMonitoringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MonitoringConfigUnion]


# CreateFlowResponse

### Flow
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Flow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGatewayRequest

### EgressCidrBlocks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Networks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayNetwork]
- **Required**: Yes


# CreateGatewayResponse

### Gateway
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Gateway'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBridgeRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBridgeResponse

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFlowRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGatewayRequest

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGatewayResponse

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterGatewayInstanceRequest

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# DeregisterGatewayInstanceResponse

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceState
- **Type**: typing.Literal['ACTIVE', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_ERROR', 'REGISTERING', 'REGISTRATION_ERROR']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBridgeRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBridgeResponse

### Bridge
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Bridge'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFlowRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowRequestWait

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeFlowRequestWaitExtra

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeFlowRequestWaitExtraExtra

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeFlowResponse

### Flow
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Flow'>
- **Required**: Yes

### Messages
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Messages'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFlowSourceMetadataRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowSourceMetadataResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetail]
- **Required**: Yes

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TransportMediaInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.TransportMediaInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFlowSourceThumbnailRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowSourceThumbnailResponse

### ThumbnailDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ThumbnailDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGatewayInstanceRequest

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayInstanceResponse

### GatewayInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGatewayRequest

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayResponse

### Gateway
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Gateway'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOfferingRequest

### OfferingArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOfferingResponse

### Offering
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Offering'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReservationRequest

### ReservationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReservationResponse

### Reservation
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Reservation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationConfiguration

### DestinationIp
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPort
- **Type**: <class 'int'>
- **Required**: Yes

### Interface
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Interface'>
- **Required**: Yes

### OutboundIp
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfigurationRequest

### DestinationIp
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPort
- **Type**: <class 'int'>
- **Required**: Yes

### Interface
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.InterfaceRequest'>
- **Required**: Yes


# EgressGatewayBridge

### MaxBitrate
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# EncodingParameters

### CompressionFactor
- **Type**: <class 'float'>
- **Required**: Yes

### EncoderProfile
- **Type**: typing.Literal['high', 'main']
- **Required**: Yes


# EncodingParametersRequest

### CompressionFactor
- **Type**: <class 'float'>
- **Required**: Yes

### EncoderProfile
- **Type**: typing.Literal['high', 'main']
- **Required**: Yes


# Encryption

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


# Entitlement

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
- **Type**: <class 'NoneType'>

### EntitlementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FailoverConfig

### FailoverMode
- **Type**: typing.Optional[typing.Literal['FAILOVER', 'MERGE']]

### RecoveryWindow
- **Type**: typing.Optional[int]

### SourcePriority
- **Type**: <class 'NoneType'>

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# Flow

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.Entitlement]
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.Output]
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Source'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EgressIp
- **Type**: typing.Optional[str]

### MediaStreams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStream]]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FailoverConfig]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.Source]]

### VpcInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterface]]

### Maintenance
- **Type**: <class 'NoneType'>

### SourceMonitoringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MonitoringConfigOutput]


# Fmtp

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


# FmtpRequest

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


# FrameResolution

### FrameHeight
- **Type**: <class 'int'>
- **Required**: Yes

### FrameWidth
- **Type**: <class 'int'>
- **Required**: Yes


# FrozenFrames

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ThresholdSeconds
- **Type**: typing.Optional[int]


# Gateway

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.GatewayNetwork]
- **Required**: Yes

### GatewayMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetail]]

### GatewayState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'ERROR', 'UPDATING']]


# GatewayBridgeSource

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaceAttachment
- **Type**: <class 'NoneType'>


# GatewayInstance

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetail]]


# GatewayNetwork

### CidrBlock
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GrantEntitlementRequest

### Subscribers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DataTransferSubscriberFeePercent
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Encryption
- **Type**: <class 'NoneType'>

### EntitlementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Name
- **Type**: typing.Optional[str]


# GrantFlowEntitlementsRequest

### Entitlements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.GrantEntitlementRequest]
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# GrantFlowEntitlementsResponse

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.Entitlement]
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# IngressGatewayBridge

### MaxBitrate
- **Type**: <class 'int'>
- **Required**: Yes

### MaxOutputs
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]


# InputConfiguration

### InputIp
- **Type**: <class 'str'>
- **Required**: Yes

### InputPort
- **Type**: <class 'int'>
- **Required**: Yes

### Interface
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Interface'>
- **Required**: Yes


# InputConfigurationRequest

### InputPort
- **Type**: <class 'int'>
- **Required**: Yes

### Interface
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.InterfaceRequest'>
- **Required**: Yes


# Interface

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# InterfaceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ListBridgesRequest

### FilterArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBridgesRequestPaginate

### FilterArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfig]


# ListBridgesResponse

### Bridges
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedBridge]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitlementsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEntitlementsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfig]


# ListEntitlementsResponse

### Entitlements
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedEntitlement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlowsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFlowsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfig]


# ListFlowsResponse

### Flows
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedFlow]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGatewayInstancesRequest

### FilterArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGatewayInstancesRequestPaginate

### FilterArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfig]


# ListGatewayInstancesResponse

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedGatewayInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGatewaysRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGatewaysRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfig]


# ListGatewaysResponse

### Gateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.ListedGateway]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfig]


# ListOfferingsResponse

### Offerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.Offering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReservationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReservationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.PaginatorConfig]


# ListReservationsResponse

### Reservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.Reservation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ListedBridge

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


# ListedEntitlement

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### EntitlementName
- **Type**: <class 'str'>
- **Required**: Yes

### DataTransferSubscriberFeePercent
- **Type**: typing.Optional[int]


# ListedFlow

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
- **Type**: <class 'NoneType'>


# ListedGateway

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayState
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ListedGatewayInstance

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


# Maintenance

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']]

### MaintenanceDeadline
- **Type**: typing.Optional[str]

### MaintenanceScheduledDate
- **Type**: typing.Optional[str]

### MaintenanceStartHour
- **Type**: typing.Optional[str]


# MediaStream

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamAttributes]

### ClockRate
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### VideoFormat
- **Type**: typing.Optional[str]


# MediaStreamAttributes

### Fmtp
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Fmtp'>
- **Required**: Yes

### Lang
- **Type**: typing.Optional[str]


# MediaStreamAttributesRequest

### Fmtp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.FmtpRequest]

### Lang
- **Type**: typing.Optional[str]


# MediaStreamOutputConfiguration

### EncodingName
- **Type**: typing.Literal['jxsv', 'pcm', 'raw', 'smpte291']
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.DestinationConfiguration]]

### EncodingParameters
- **Type**: <class 'NoneType'>


# MediaStreamOutputConfigurationRequest

### EncodingName
- **Type**: typing.Literal['jxsv', 'pcm', 'raw', 'smpte291']
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.DestinationConfigurationRequest]]

### EncodingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.EncodingParametersRequest]


# MediaStreamSourceConfiguration

### EncodingName
- **Type**: typing.Literal['jxsv', 'pcm', 'raw', 'smpte291']
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.InputConfiguration]]


# MediaStreamSourceConfigurationRequest

### EncodingName
- **Type**: typing.Literal['jxsv', 'pcm', 'raw', 'smpte291']
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.InputConfigurationRequest]]


# MessageDetail

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: typing.Optional[str]


# Messages

### Errors
- **Type**: typing.List[str]
- **Required**: Yes


# MonitoringConfig

### ThumbnailState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AudioMonitoringSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.AudioMonitoringSetting]]

### ContentQualityAnalysisState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### VideoMonitoringSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconnect_classes.VideoMonitoringSetting]]


# MonitoringConfigOutput

### ThumbnailState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AudioMonitoringSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.AudioMonitoringSetting]]

### ContentQualityAnalysisState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### VideoMonitoringSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.VideoMonitoringSetting]]


# MonitoringConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MulticastSourceSettings

### MulticastSourceIp
- **Type**: typing.Optional[str]


# Offering

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResourceSpecification'>
- **Required**: Yes


# Output

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
- **Type**: <class 'NoneType'>

### EntitlementArn
- **Type**: typing.Optional[str]

### ListenerAddress
- **Type**: typing.Optional[str]

### MediaLiveInputArn
- **Type**: typing.Optional[str]

### MediaStreamOutputConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamOutputConfiguration]]

### Port
- **Type**: typing.Optional[int]

### Transport
- **Type**: <class 'NoneType'>

### VpcInterfaceAttachment
- **Type**: <class 'NoneType'>

### BridgeArn
- **Type**: typing.Optional[str]

### BridgePorts
- **Type**: typing.Optional[typing.List[int]]

### OutputStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PurchaseOfferingRequest

### OfferingArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### Start
- **Type**: <class 'str'>
- **Required**: Yes


# PurchaseOfferingResponse

### Reservation
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Reservation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveBridgeOutputRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveBridgeOutputResponse

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveBridgeSourceRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveBridgeSourceResponse

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveFlowMediaStreamRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFlowMediaStreamResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveFlowOutputRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFlowOutputResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveFlowSourceRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFlowSourceResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveFlowVpcInterfaceRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaceName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFlowVpcInterfaceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Reservation

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResourceSpecification'>
- **Required**: Yes

### Start
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceSpecification

### ResourceType
- **Type**: typing.Literal['Mbps_Outbound_Bandwidth']
- **Required**: Yes

### ReservedBitrate
- **Type**: typing.Optional[int]


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


# RevokeFlowEntitlementRequest

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeFlowEntitlementResponse

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# SetGatewayBridgeSourceRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcInterfaceAttachment
- **Type**: <class 'NoneType'>


# SetSourceRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SilentAudio

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ThresholdSeconds
- **Type**: typing.Optional[int]


# Source

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataTransferSubscriberFeePercent
- **Type**: typing.Optional[int]

### Decryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.Encryption]

### Description
- **Type**: typing.Optional[str]

### EntitlementArn
- **Type**: typing.Optional[str]

### IngestIp
- **Type**: typing.Optional[str]

### IngestPort
- **Type**: typing.Optional[int]

### MediaStreamSourceConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamSourceConfiguration]]

### SenderControlPort
- **Type**: typing.Optional[int]

### SenderIpAddress
- **Type**: typing.Optional[str]

### Transport
- **Type**: <class 'NoneType'>

### VpcInterfaceName
- **Type**: typing.Optional[str]

### WhitelistCidr
- **Type**: typing.Optional[str]

### GatewayBridgeSource
- **Type**: <class 'NoneType'>


# SourcePriority

### PrimarySource
- **Type**: typing.Optional[str]


# StartFlowRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartFlowResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# StopFlowRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopFlowResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'ERROR', 'STANDBY', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ThumbnailDetails

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ThumbnailMessages
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.MessageDetail]
- **Required**: Yes

### Thumbnail
- **Type**: typing.Optional[str]

### Timecode
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# Transport

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransportMediaInfo

### Programs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.TransportStreamProgram]
- **Required**: Yes


# TransportStream

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
- **Type**: <class 'NoneType'>

### SampleRate
- **Type**: typing.Optional[int]

### SampleSize
- **Type**: typing.Optional[int]


# TransportStreamProgram

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconnect_classes.TransportStream]
- **Required**: Yes

### ProgramName
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBridgeFlowSourceRequest

### FlowArn
- **Type**: typing.Optional[str]

### FlowVpcInterfaceAttachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.VpcInterfaceAttachment]


# UpdateBridgeNetworkOutputRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateBridgeNetworkSourceRequest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateBridgeOutputRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputName
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateBridgeNetworkOutputRequest]


# UpdateBridgeOutputResponse

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBridgeRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### EgressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateEgressGatewayBridgeRequest]

### IngressGatewayBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateIngressGatewayBridgeRequest]

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateFailoverConfig]


# UpdateBridgeResponse

### Bridge
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Bridge'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBridgeSourceRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateBridgeFlowSourceRequest]

### NetworkSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateBridgeNetworkSourceRequest]


# UpdateBridgeSourceResponse

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.BridgeSource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBridgeStateRequest

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'STANDBY']
- **Required**: Yes


# UpdateBridgeStateResponse

### BridgeArn
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'STANDBY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEgressGatewayBridgeRequest

### MaxBitrate
- **Type**: typing.Optional[int]


# UpdateEncryption

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


# UpdateFailoverConfig

### FailoverMode
- **Type**: typing.Optional[typing.Literal['FAILOVER', 'MERGE']]

### RecoveryWindow
- **Type**: typing.Optional[int]

### SourcePriority
- **Type**: <class 'NoneType'>

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateFlowEntitlementRequest

### EntitlementArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateEncryption]

### EntitlementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Subscribers
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateFlowEntitlementResponse

### Entitlement
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Entitlement'>
- **Required**: Yes

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFlowMediaStreamRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStreamAttributesRequest]

### ClockRate
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### MediaStreamType
- **Type**: typing.Optional[typing.Literal['ancillary-data', 'audio', 'video']]

### VideoFormat
- **Type**: typing.Optional[str]


# UpdateFlowMediaStreamResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStream
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.MediaStream'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFlowOutputResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Output'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFlowRequest

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateFailoverConfig]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.UpdateMaintenance]

### SourceMonitoringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconnect_classes.MonitoringConfigUnion]


# UpdateFlowResponse

### Flow
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Flow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFlowSourceResponse

### FlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.Source'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGatewayBridgeSourceRequest

### BridgeArn
- **Type**: typing.Optional[str]

### VpcInterfaceAttachment
- **Type**: <class 'NoneType'>


# UpdateGatewayInstanceRequest

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### BridgePlacement
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'LOCKED']]


# UpdateGatewayInstanceResponse

### BridgePlacement
- **Type**: typing.Literal['AVAILABLE', 'LOCKED']
- **Required**: Yes

### GatewayInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIngressGatewayBridgeRequest

### MaxBitrate
- **Type**: typing.Optional[int]

### MaxOutputs
- **Type**: typing.Optional[int]


# UpdateMaintenance

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']]

### MaintenanceScheduledDate
- **Type**: typing.Optional[str]

### MaintenanceStartHour
- **Type**: typing.Optional[str]


# VideoMonitoringSetting

### BlackFrames
- **Type**: <class 'NoneType'>

### FrozenFrames
- **Type**: <class 'NoneType'>


# VpcInterface

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


# VpcInterfaceAttachment

### VpcInterfaceName
- **Type**: typing.Optional[str]


# VpcInterfaceRequest

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


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



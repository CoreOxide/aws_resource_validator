from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.mediaconnect_constants import *

class VpcInterfaceAttachmentTypeDef(BaseModel):
    VpcInterfaceName: Optional[str] = None

class AddBridgeNetworkOutputRequestTypeDef(BaseModel):
    IpAddress: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType
    Ttl: int

class AddBridgeNetworkSourceRequestTypeDef(BaseModel):
    MulticastIp: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AddEgressGatewayBridgeRequestTypeDef(BaseModel):
    MaxBitrate: int

class VpcInterfaceRequestTypeDef(BaseModel):
    Name: str
    RoleArn: str
    SecurityGroupIds: Sequence[str]
    SubnetId: str
    NetworkInterfaceType: Optional[NetworkInterfaceTypeType] = None

class VpcInterfaceTypeDef(BaseModel):
    Name: str
    NetworkInterfaceIds: List[str]
    NetworkInterfaceType: NetworkInterfaceTypeType
    RoleArn: str
    SecurityGroupIds: List[str]
    SubnetId: str

class AddIngressGatewayBridgeRequestTypeDef(BaseModel):
    MaxBitrate: int
    MaxOutputs: int

class AddMaintenanceTypeDef(BaseModel):
    MaintenanceDay: MaintenanceDayType
    MaintenanceStartHour: str

class EncryptionTypeDef(BaseModel):
    RoleArn: str
    Algorithm: Optional[AlgorithmType] = None
    ConstantInitializationVector: Optional[str] = None
    DeviceId: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Region: Optional[str] = None
    ResourceId: Optional[str] = None
    SecretArn: Optional[str] = None
    Url: Optional[str] = None

class BridgeFlowOutputTypeDef(BaseModel):
    FlowArn: str
    FlowSourceArn: str
    Name: str

class BridgeNetworkOutputTypeDef(BaseModel):
    IpAddress: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType
    Ttl: int

class BridgeNetworkSourceTypeDef(BaseModel):
    MulticastIp: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType

class EgressGatewayBridgeTypeDef(BaseModel):
    MaxBitrate: int
    InstanceId: Optional[str] = None

class IngressGatewayBridgeTypeDef(BaseModel):
    MaxBitrate: int
    MaxOutputs: int
    InstanceId: Optional[str] = None

class MessageDetailTypeDef(BaseModel):
    Code: str
    Message: str
    ResourceName: Optional[str] = None

class GatewayNetworkTypeDef(BaseModel):
    CidrBlock: str
    Name: str

class DeleteBridgeRequestRequestTypeDef(BaseModel):
    BridgeArn: str

class DeleteFlowRequestRequestTypeDef(BaseModel):
    FlowArn: str

class DeleteGatewayRequestRequestTypeDef(BaseModel):
    GatewayArn: str

class DeregisterGatewayInstanceRequestRequestTypeDef(BaseModel):
    GatewayInstanceArn: str
    Force: Optional[bool] = None

class DescribeBridgeRequestRequestTypeDef(BaseModel):
    BridgeArn: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeFlowRequestRequestTypeDef(BaseModel):
    FlowArn: str

class MessagesTypeDef(BaseModel):
    Errors: List[str]

class DescribeFlowSourceMetadataRequestRequestTypeDef(BaseModel):
    FlowArn: str

class DescribeGatewayInstanceRequestRequestTypeDef(BaseModel):
    GatewayInstanceArn: str

class DescribeGatewayRequestRequestTypeDef(BaseModel):
    GatewayArn: str

class DescribeOfferingRequestRequestTypeDef(BaseModel):
    OfferingArn: str

class DescribeReservationRequestRequestTypeDef(BaseModel):
    ReservationArn: str

class InterfaceRequestTypeDef(BaseModel):
    Name: str

class InterfaceTypeDef(BaseModel):
    Name: str

class EncodingParametersRequestTypeDef(BaseModel):
    CompressionFactor: float
    EncoderProfile: EncoderProfileType

class EncodingParametersTypeDef(BaseModel):
    CompressionFactor: float
    EncoderProfile: EncoderProfileType

class SourcePriorityTypeDef(BaseModel):
    PrimarySource: Optional[str] = None

class MaintenanceTypeDef(BaseModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceDeadline: Optional[str] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartHour: Optional[str] = None

class FmtpRequestTypeDef(BaseModel):
    ChannelOrder: Optional[str] = None
    Colorimetry: Optional[ColorimetryType] = None
    ExactFramerate: Optional[str] = None
    Par: Optional[str] = None
    Range: Optional[RangeType] = None
    ScanMode: Optional[ScanModeType] = None
    Tcs: Optional[TcsType] = None

class FmtpTypeDef(BaseModel):
    ChannelOrder: Optional[str] = None
    Colorimetry: Optional[ColorimetryType] = None
    ExactFramerate: Optional[str] = None
    Par: Optional[str] = None
    Range: Optional[RangeType] = None
    ScanMode: Optional[ScanModeType] = None
    Tcs: Optional[TcsType] = None

class FrameResolutionTypeDef(BaseModel):
    FrameHeight: int
    FrameWidth: int

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBridgesRequestRequestTypeDef(BaseModel):
    FilterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedBridgeTypeDef(BaseModel):
    BridgeArn: str
    BridgeState: BridgeStateType
    BridgeType: str
    Name: str
    PlacementArn: str

class ListEntitlementsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedEntitlementTypeDef(BaseModel):
    EntitlementArn: str
    EntitlementName: str
    DataTransferSubscriberFeePercent: Optional[int] = None

class ListFlowsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGatewayInstancesRequestRequestTypeDef(BaseModel):
    FilterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedGatewayInstanceTypeDef(BaseModel):
    GatewayArn: str
    GatewayInstanceArn: str
    InstanceId: str
    InstanceState: Optional[InstanceStateType] = None

class ListGatewaysRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedGatewayTypeDef(BaseModel):
    GatewayArn: str
    GatewayState: GatewayStateType
    Name: str

class ListOfferingsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListReservationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ResourceSpecificationTypeDef(BaseModel):
    ResourceType: Literal["Mbps_Outbound_Bandwidth"]
    ReservedBitrate: Optional[int] = None

class TransportTypeDef(BaseModel):
    Protocol: ProtocolType
    CidrAllowList: Optional[List[str]] = None
    MaxBitrate: Optional[int] = None
    MaxLatency: Optional[int] = None
    MaxSyncBuffer: Optional[int] = None
    MinLatency: Optional[int] = None
    RemoteId: Optional[str] = None
    SenderControlPort: Optional[int] = None
    SenderIpAddress: Optional[str] = None
    SmoothingLatency: Optional[int] = None
    SourceListenerAddress: Optional[str] = None
    SourceListenerPort: Optional[int] = None
    StreamId: Optional[str] = None

class PurchaseOfferingRequestRequestTypeDef(BaseModel):
    OfferingArn: str
    ReservationName: str
    Start: str

class RemoveBridgeOutputRequestRequestTypeDef(BaseModel):
    BridgeArn: str
    OutputName: str

class RemoveBridgeSourceRequestRequestTypeDef(BaseModel):
    BridgeArn: str
    SourceName: str

class RemoveFlowMediaStreamRequestRequestTypeDef(BaseModel):
    FlowArn: str
    MediaStreamName: str

class RemoveFlowOutputRequestRequestTypeDef(BaseModel):
    FlowArn: str
    OutputArn: str

class RemoveFlowSourceRequestRequestTypeDef(BaseModel):
    FlowArn: str
    SourceArn: str

class RemoveFlowVpcInterfaceRequestRequestTypeDef(BaseModel):
    FlowArn: str
    VpcInterfaceName: str

class RevokeFlowEntitlementRequestRequestTypeDef(BaseModel):
    EntitlementArn: str
    FlowArn: str

class StartFlowRequestRequestTypeDef(BaseModel):
    FlowArn: str

class StopFlowRequestRequestTypeDef(BaseModel):
    FlowArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateBridgeNetworkOutputRequestTypeDef(BaseModel):
    IpAddress: Optional[str] = None
    NetworkName: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolType] = None
    Ttl: Optional[int] = None

class UpdateBridgeNetworkSourceRequestTypeDef(BaseModel):
    MulticastIp: Optional[str] = None
    NetworkName: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolType] = None

class UpdateEgressGatewayBridgeRequestTypeDef(BaseModel):
    MaxBitrate: Optional[int] = None

class UpdateIngressGatewayBridgeRequestTypeDef(BaseModel):
    MaxBitrate: Optional[int] = None
    MaxOutputs: Optional[int] = None

class UpdateBridgeStateRequestRequestTypeDef(BaseModel):
    BridgeArn: str
    DesiredState: DesiredStateType

class UpdateEncryptionTypeDef(BaseModel):
    Algorithm: Optional[AlgorithmType] = None
    ConstantInitializationVector: Optional[str] = None
    DeviceId: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Region: Optional[str] = None
    ResourceId: Optional[str] = None
    RoleArn: Optional[str] = None
    SecretArn: Optional[str] = None
    Url: Optional[str] = None

class UpdateMaintenanceTypeDef(BaseModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartHour: Optional[str] = None

class UpdateGatewayInstanceRequestRequestTypeDef(BaseModel):
    GatewayInstanceArn: str
    BridgePlacement: Optional[BridgePlacementType] = None

class AddBridgeFlowSourceRequestTypeDef(BaseModel):
    FlowArn: str
    Name: str
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class BridgeFlowSourceTypeDef(BaseModel):
    FlowArn: str
    Name: str
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None
    OutputArn: Optional[str] = None

class GatewayBridgeSourceTypeDef(BaseModel):
    BridgeArn: str
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class SetGatewayBridgeSourceRequestTypeDef(BaseModel):
    BridgeArn: str
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class UpdateBridgeFlowSourceRequestTypeDef(BaseModel):
    FlowArn: Optional[str] = None
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class UpdateGatewayBridgeSourceRequestTypeDef(BaseModel):
    BridgeArn: Optional[str] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class AddBridgeOutputRequestTypeDef(BaseModel):
    NetworkOutput: Optional[AddBridgeNetworkOutputRequestTypeDef] = None

class DeleteBridgeResponseTypeDef(BaseModel):
    BridgeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowResponseTypeDef(BaseModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayResponseTypeDef(BaseModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterGatewayInstanceResponseTypeDef(BaseModel):
    GatewayInstanceArn: str
    InstanceState: InstanceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveBridgeOutputResponseTypeDef(BaseModel):
    BridgeArn: str
    OutputName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveBridgeSourceResponseTypeDef(BaseModel):
    BridgeArn: str
    SourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowMediaStreamResponseTypeDef(BaseModel):
    FlowArn: str
    MediaStreamName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowOutputResponseTypeDef(BaseModel):
    FlowArn: str
    OutputArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowSourceResponseTypeDef(BaseModel):
    FlowArn: str
    SourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowVpcInterfaceResponseTypeDef(BaseModel):
    FlowArn: str
    NonDeletedNetworkInterfaceIds: List[str]
    VpcInterfaceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeFlowEntitlementResponseTypeDef(BaseModel):
    EntitlementArn: str
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlowResponseTypeDef(BaseModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopFlowResponseTypeDef(BaseModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeStateResponseTypeDef(BaseModel):
    BridgeArn: str
    DesiredState: DesiredStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayInstanceResponseTypeDef(BaseModel):
    BridgePlacement: BridgePlacementType
    GatewayInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowVpcInterfacesRequestRequestTypeDef(BaseModel):
    FlowArn: str
    VpcInterfaces: Sequence[VpcInterfaceRequestTypeDef]

class AddFlowVpcInterfacesResponseTypeDef(BaseModel):
    FlowArn: str
    VpcInterfaces: List[VpcInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EntitlementTypeDef(BaseModel):
    EntitlementArn: str
    Name: str
    Subscribers: List[str]
    DataTransferSubscriberFeePercent: Optional[int] = None
    Description: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None

class GrantEntitlementRequestTypeDef(BaseModel):
    Subscribers: Sequence[str]
    DataTransferSubscriberFeePercent: Optional[int] = None
    Description: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None
    Name: Optional[str] = None

class BridgeOutputTypeDef(BaseModel):
    FlowOutput: Optional[BridgeFlowOutputTypeDef] = None
    NetworkOutput: Optional[BridgeNetworkOutputTypeDef] = None

class GatewayInstanceTypeDef(BaseModel):
    BridgePlacement: BridgePlacementType
    ConnectionStatus: ConnectionStatusType
    GatewayArn: str
    GatewayInstanceArn: str
    InstanceId: str
    InstanceState: InstanceStateType
    RunningBridgeCount: int
    InstanceMessages: Optional[List[MessageDetailTypeDef]] = None

class CreateGatewayRequestRequestTypeDef(BaseModel):
    EgressCidrBlocks: Sequence[str]
    Name: str
    Networks: Sequence[GatewayNetworkTypeDef]

class GatewayTypeDef(BaseModel):
    EgressCidrBlocks: List[str]
    GatewayArn: str
    Name: str
    Networks: List[GatewayNetworkTypeDef]
    GatewayMessages: Optional[List[MessageDetailTypeDef]] = None
    GatewayState: Optional[GatewayStateType] = None

class DescribeFlowRequestFlowActiveWaitTypeDef(BaseModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFlowRequestFlowDeletedWaitTypeDef(BaseModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFlowRequestFlowStandbyWaitTypeDef(BaseModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DestinationConfigurationRequestTypeDef(BaseModel):
    DestinationIp: str
    DestinationPort: int
    Interface: InterfaceRequestTypeDef

class InputConfigurationRequestTypeDef(BaseModel):
    InputPort: int
    Interface: InterfaceRequestTypeDef

class DestinationConfigurationTypeDef(BaseModel):
    DestinationIp: str
    DestinationPort: int
    Interface: InterfaceTypeDef
    OutboundIp: str

class InputConfigurationTypeDef(BaseModel):
    InputIp: str
    InputPort: int
    Interface: InterfaceTypeDef

class FailoverConfigTypeDef(BaseModel):
    FailoverMode: Optional[FailoverModeType] = None
    RecoveryWindow: Optional[int] = None
    SourcePriority: Optional[SourcePriorityTypeDef] = None
    State: Optional[StateType] = None

class UpdateFailoverConfigTypeDef(BaseModel):
    FailoverMode: Optional[FailoverModeType] = None
    RecoveryWindow: Optional[int] = None
    SourcePriority: Optional[SourcePriorityTypeDef] = None
    State: Optional[StateType] = None

class ListedFlowTypeDef(BaseModel):
    AvailabilityZone: str
    Description: str
    FlowArn: str
    Name: str
    SourceType: SourceTypeType
    Status: StatusType
    Maintenance: Optional[MaintenanceTypeDef] = None

class MediaStreamAttributesRequestTypeDef(BaseModel):
    Fmtp: Optional[FmtpRequestTypeDef] = None
    Lang: Optional[str] = None

class MediaStreamAttributesTypeDef(BaseModel):
    Fmtp: FmtpTypeDef
    Lang: Optional[str] = None

class TransportStreamTypeDef(BaseModel):
    Pid: int
    StreamType: str
    Channels: Optional[int] = None
    Codec: Optional[str] = None
    FrameRate: Optional[str] = None
    FrameResolution: Optional[FrameResolutionTypeDef] = None
    SampleRate: Optional[int] = None
    SampleSize: Optional[int] = None

class ListBridgesRequestListBridgesPaginateTypeDef(BaseModel):
    FilterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntitlementsRequestListEntitlementsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowsRequestListFlowsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGatewayInstancesRequestListGatewayInstancesPaginateTypeDef(BaseModel):
    FilterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGatewaysRequestListGatewaysPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingsRequestListOfferingsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReservationsRequestListReservationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBridgesResponseTypeDef(BaseModel):
    Bridges: List[ListedBridgeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEntitlementsResponseTypeDef(BaseModel):
    Entitlements: List[ListedEntitlementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListGatewayInstancesResponseTypeDef(BaseModel):
    Instances: List[ListedGatewayInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListGatewaysResponseTypeDef(BaseModel):
    Gateways: List[ListedGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OfferingTypeDef(BaseModel):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal["HOURLY"]
    ResourceSpecification: ResourceSpecificationTypeDef

class ReservationTypeDef(BaseModel):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    End: str
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal["HOURLY"]
    ReservationArn: str
    ReservationName: str
    ReservationState: ReservationStateType
    ResourceSpecification: ResourceSpecificationTypeDef
    Start: str

class UpdateBridgeOutputRequestRequestTypeDef(BaseModel):
    BridgeArn: str
    OutputName: str
    NetworkOutput: Optional[UpdateBridgeNetworkOutputRequestTypeDef] = None

class UpdateFlowEntitlementRequestRequestTypeDef(BaseModel):
    EntitlementArn: str
    FlowArn: str
    Description: Optional[str] = None
    Encryption: Optional[UpdateEncryptionTypeDef] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None
    Subscribers: Optional[Sequence[str]] = None

class AddBridgeSourceRequestTypeDef(BaseModel):
    FlowSource: Optional[AddBridgeFlowSourceRequestTypeDef] = None
    NetworkSource: Optional[AddBridgeNetworkSourceRequestTypeDef] = None

class BridgeSourceTypeDef(BaseModel):
    FlowSource: Optional[BridgeFlowSourceTypeDef] = None
    NetworkSource: Optional[BridgeNetworkSourceTypeDef] = None

class UpdateBridgeSourceRequestRequestTypeDef(BaseModel):
    BridgeArn: str
    SourceName: str
    FlowSource: Optional[UpdateBridgeFlowSourceRequestTypeDef] = None
    NetworkSource: Optional[UpdateBridgeNetworkSourceRequestTypeDef] = None

class AddBridgeOutputsRequestRequestTypeDef(BaseModel):
    BridgeArn: str
    Outputs: Sequence[AddBridgeOutputRequestTypeDef]

class GrantFlowEntitlementsResponseTypeDef(BaseModel):
    Entitlements: List[EntitlementTypeDef]
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowEntitlementResponseTypeDef(BaseModel):
    Entitlement: EntitlementTypeDef
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GrantFlowEntitlementsRequestRequestTypeDef(BaseModel):
    Entitlements: Sequence[GrantEntitlementRequestTypeDef]
    FlowArn: str

class AddBridgeOutputsResponseTypeDef(BaseModel):
    BridgeArn: str
    Outputs: List[BridgeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeOutputResponseTypeDef(BaseModel):
    BridgeArn: str
    Output: BridgeOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayInstanceResponseTypeDef(BaseModel):
    GatewayInstance: GatewayInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGatewayResponseTypeDef(BaseModel):
    Gateway: GatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayResponseTypeDef(BaseModel):
    Gateway: GatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaStreamOutputConfigurationRequestTypeDef(BaseModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    DestinationConfigurations: Optional[Sequence[DestinationConfigurationRequestTypeDef]] = None
    EncodingParameters: Optional[EncodingParametersRequestTypeDef] = None

class MediaStreamSourceConfigurationRequestTypeDef(BaseModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    InputConfigurations: Optional[Sequence[InputConfigurationRequestTypeDef]] = None

class MediaStreamOutputConfigurationTypeDef(BaseModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    DestinationConfigurations: Optional[List[DestinationConfigurationTypeDef]] = None
    EncodingParameters: Optional[EncodingParametersTypeDef] = None

class MediaStreamSourceConfigurationTypeDef(BaseModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    InputConfigurations: Optional[List[InputConfigurationTypeDef]] = None

class UpdateBridgeRequestRequestTypeDef(BaseModel):
    BridgeArn: str
    EgressGatewayBridge: Optional[UpdateEgressGatewayBridgeRequestTypeDef] = None
    IngressGatewayBridge: Optional[UpdateIngressGatewayBridgeRequestTypeDef] = None
    SourceFailoverConfig: Optional[UpdateFailoverConfigTypeDef] = None

class UpdateFlowRequestRequestTypeDef(BaseModel):
    FlowArn: str
    SourceFailoverConfig: Optional[UpdateFailoverConfigTypeDef] = None
    Maintenance: Optional[UpdateMaintenanceTypeDef] = None

class ListFlowsResponseTypeDef(BaseModel):
    Flows: List[ListedFlowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AddMediaStreamRequestTypeDef(BaseModel):
    MediaStreamId: int
    MediaStreamName: str
    MediaStreamType: MediaStreamTypeType
    Attributes: Optional[MediaStreamAttributesRequestTypeDef] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    VideoFormat: Optional[str] = None

class UpdateFlowMediaStreamRequestRequestTypeDef(BaseModel):
    FlowArn: str
    MediaStreamName: str
    Attributes: Optional[MediaStreamAttributesRequestTypeDef] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    MediaStreamType: Optional[MediaStreamTypeType] = None
    VideoFormat: Optional[str] = None

class MediaStreamTypeDef(BaseModel):
    Fmt: int
    MediaStreamId: int
    MediaStreamName: str
    MediaStreamType: MediaStreamTypeType
    Attributes: Optional[MediaStreamAttributesTypeDef] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    VideoFormat: Optional[str] = None

class TransportStreamProgramTypeDef(BaseModel):
    PcrPid: int
    ProgramNumber: int
    ProgramPid: int
    Streams: List[TransportStreamTypeDef]
    ProgramName: Optional[str] = None

class DescribeOfferingResponseTypeDef(BaseModel):
    Offering: OfferingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingsResponseTypeDef(BaseModel):
    Offerings: List[OfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservationResponseTypeDef(BaseModel):
    Reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReservationsResponseTypeDef(BaseModel):
    Reservations: List[ReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseOfferingResponseTypeDef(BaseModel):
    Reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddBridgeSourcesRequestRequestTypeDef(BaseModel):
    BridgeArn: str
    Sources: Sequence[AddBridgeSourceRequestTypeDef]

class CreateBridgeRequestRequestTypeDef(BaseModel):
    Name: str
    PlacementArn: str
    Sources: Sequence[AddBridgeSourceRequestTypeDef]
    EgressGatewayBridge: Optional[AddEgressGatewayBridgeRequestTypeDef] = None
    IngressGatewayBridge: Optional[AddIngressGatewayBridgeRequestTypeDef] = None
    Outputs: Optional[Sequence[AddBridgeOutputRequestTypeDef]] = None
    SourceFailoverConfig: Optional[FailoverConfigTypeDef] = None

class AddBridgeSourcesResponseTypeDef(BaseModel):
    BridgeArn: str
    Sources: List[BridgeSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BridgeTypeDef(BaseModel):
    BridgeArn: str
    BridgeState: BridgeStateType
    Name: str
    PlacementArn: str
    BridgeMessages: Optional[List[MessageDetailTypeDef]] = None
    EgressGatewayBridge: Optional[EgressGatewayBridgeTypeDef] = None
    IngressGatewayBridge: Optional[IngressGatewayBridgeTypeDef] = None
    Outputs: Optional[List[BridgeOutputTypeDef]] = None
    SourceFailoverConfig: Optional[FailoverConfigTypeDef] = None
    Sources: Optional[List[BridgeSourceTypeDef]] = None

class UpdateBridgeSourceResponseTypeDef(BaseModel):
    BridgeArn: str
    Source: BridgeSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddOutputRequestTypeDef(BaseModel):
    Protocol: ProtocolType
    CidrAllowList: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    Destination: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    MaxLatency: Optional[int] = None
    MediaStreamOutputConfigurations: Optional[       Sequence[MediaStreamOutputConfigurationRequestTypeDef]     ] = None
    MinLatency: Optional[int] = None
    Name: Optional[str] = None
    Port: Optional[int] = None
    RemoteId: Optional[str] = None
    SenderControlPort: Optional[int] = None
    SmoothingLatency: Optional[int] = None
    StreamId: Optional[str] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None
    OutputStatus: Optional[OutputStatusType] = None

class UpdateFlowOutputRequestRequestTypeDef(BaseModel):
    FlowArn: str
    OutputArn: str
    CidrAllowList: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    Destination: Optional[str] = None
    Encryption: Optional[UpdateEncryptionTypeDef] = None
    MaxLatency: Optional[int] = None
    MediaStreamOutputConfigurations: Optional[       Sequence[MediaStreamOutputConfigurationRequestTypeDef]     ] = None
    MinLatency: Optional[int] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolType] = None
    RemoteId: Optional[str] = None
    SenderControlPort: Optional[int] = None
    SenderIpAddress: Optional[str] = None
    SmoothingLatency: Optional[int] = None
    StreamId: Optional[str] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None
    OutputStatus: Optional[OutputStatusType] = None

class SetSourceRequestTypeDef(BaseModel):
    Decryption: Optional[EncryptionTypeDef] = None
    Description: Optional[str] = None
    EntitlementArn: Optional[str] = None
    IngestPort: Optional[int] = None
    MaxBitrate: Optional[int] = None
    MaxLatency: Optional[int] = None
    MaxSyncBuffer: Optional[int] = None
    MediaStreamSourceConfigurations: Optional[       Sequence[MediaStreamSourceConfigurationRequestTypeDef]     ] = None
    MinLatency: Optional[int] = None
    Name: Optional[str] = None
    Protocol: Optional[ProtocolType] = None
    SenderControlPort: Optional[int] = None
    SenderIpAddress: Optional[str] = None
    SourceListenerAddress: Optional[str] = None
    SourceListenerPort: Optional[int] = None
    StreamId: Optional[str] = None
    VpcInterfaceName: Optional[str] = None
    WhitelistCidr: Optional[str] = None
    GatewayBridgeSource: Optional[SetGatewayBridgeSourceRequestTypeDef] = None

class UpdateFlowSourceRequestRequestTypeDef(BaseModel):
    FlowArn: str
    SourceArn: str
    Decryption: Optional[UpdateEncryptionTypeDef] = None
    Description: Optional[str] = None
    EntitlementArn: Optional[str] = None
    IngestPort: Optional[int] = None
    MaxBitrate: Optional[int] = None
    MaxLatency: Optional[int] = None
    MaxSyncBuffer: Optional[int] = None
    MediaStreamSourceConfigurations: Optional[       Sequence[MediaStreamSourceConfigurationRequestTypeDef]     ] = None
    MinLatency: Optional[int] = None
    Protocol: Optional[ProtocolType] = None
    SenderControlPort: Optional[int] = None
    SenderIpAddress: Optional[str] = None
    SourceListenerAddress: Optional[str] = None
    SourceListenerPort: Optional[int] = None
    StreamId: Optional[str] = None
    VpcInterfaceName: Optional[str] = None
    WhitelistCidr: Optional[str] = None
    GatewayBridgeSource: Optional[UpdateGatewayBridgeSourceRequestTypeDef] = None

class OutputTypeDef(BaseModel):
    Name: str
    OutputArn: str
    DataTransferSubscriberFeePercent: Optional[int] = None
    Description: Optional[str] = None
    Destination: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    EntitlementArn: Optional[str] = None
    ListenerAddress: Optional[str] = None
    MediaLiveInputArn: Optional[str] = None
    MediaStreamOutputConfigurations: Optional[List[MediaStreamOutputConfigurationTypeDef]] = None
    Port: Optional[int] = None
    Transport: Optional[TransportTypeDef] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None
    BridgeArn: Optional[str] = None
    BridgePorts: Optional[List[int]] = None
    OutputStatus: Optional[OutputStatusType] = None

class SourceTypeDef(BaseModel):
    Name: str
    SourceArn: str
    DataTransferSubscriberFeePercent: Optional[int] = None
    Decryption: Optional[EncryptionTypeDef] = None
    Description: Optional[str] = None
    EntitlementArn: Optional[str] = None
    IngestIp: Optional[str] = None
    IngestPort: Optional[int] = None
    MediaStreamSourceConfigurations: Optional[List[MediaStreamSourceConfigurationTypeDef]] = None
    SenderControlPort: Optional[int] = None
    SenderIpAddress: Optional[str] = None
    Transport: Optional[TransportTypeDef] = None
    VpcInterfaceName: Optional[str] = None
    WhitelistCidr: Optional[str] = None
    GatewayBridgeSource: Optional[GatewayBridgeSourceTypeDef] = None

class AddFlowMediaStreamsRequestRequestTypeDef(BaseModel):
    FlowArn: str
    MediaStreams: Sequence[AddMediaStreamRequestTypeDef]

class AddFlowMediaStreamsResponseTypeDef(BaseModel):
    FlowArn: str
    MediaStreams: List[MediaStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowMediaStreamResponseTypeDef(BaseModel):
    FlowArn: str
    MediaStream: MediaStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransportMediaInfoTypeDef(BaseModel):
    Programs: List[TransportStreamProgramTypeDef]

class CreateBridgeResponseTypeDef(BaseModel):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBridgeResponseTypeDef(BaseModel):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeResponseTypeDef(BaseModel):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowOutputsRequestRequestTypeDef(BaseModel):
    FlowArn: str
    Outputs: Sequence[AddOutputRequestTypeDef]

class AddFlowSourcesRequestRequestTypeDef(BaseModel):
    FlowArn: str
    Sources: Sequence[SetSourceRequestTypeDef]

class CreateFlowRequestRequestTypeDef(BaseModel):
    Name: str
    AvailabilityZone: Optional[str] = None
    Entitlements: Optional[Sequence[GrantEntitlementRequestTypeDef]] = None
    MediaStreams: Optional[Sequence[AddMediaStreamRequestTypeDef]] = None
    Outputs: Optional[Sequence[AddOutputRequestTypeDef]] = None
    Source: Optional[SetSourceRequestTypeDef] = None
    SourceFailoverConfig: Optional[FailoverConfigTypeDef] = None
    Sources: Optional[Sequence[SetSourceRequestTypeDef]] = None
    VpcInterfaces: Optional[Sequence[VpcInterfaceRequestTypeDef]] = None
    Maintenance: Optional[AddMaintenanceTypeDef] = None

class AddFlowOutputsResponseTypeDef(BaseModel):
    FlowArn: str
    Outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowOutputResponseTypeDef(BaseModel):
    FlowArn: str
    Output: OutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowSourcesResponseTypeDef(BaseModel):
    FlowArn: str
    Sources: List[SourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FlowTypeDef(BaseModel):
    AvailabilityZone: str
    Entitlements: List[EntitlementTypeDef]
    FlowArn: str
    Name: str
    Outputs: List[OutputTypeDef]
    Source: SourceTypeDef
    Status: StatusType
    Description: Optional[str] = None
    EgressIp: Optional[str] = None
    MediaStreams: Optional[List[MediaStreamTypeDef]] = None
    SourceFailoverConfig: Optional[FailoverConfigTypeDef] = None
    Sources: Optional[List[SourceTypeDef]] = None
    VpcInterfaces: Optional[List[VpcInterfaceTypeDef]] = None
    Maintenance: Optional[MaintenanceTypeDef] = None

class UpdateFlowSourceResponseTypeDef(BaseModel):
    FlowArn: str
    Source: SourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlowSourceMetadataResponseTypeDef(BaseModel):
    FlowArn: str
    Messages: List[MessageDetailTypeDef]
    Timestamp: datetime
    TransportMediaInfo: TransportMediaInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowResponseTypeDef(BaseModel):
    Flow: FlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlowResponseTypeDef(BaseModel):
    Flow: FlowTypeDef
    Messages: MessagesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowResponseTypeDef(BaseModel):
    Flow: FlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


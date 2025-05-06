from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediaconnect.mediaconnect_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class VpcInterfaceAttachment(BaseValidatorModel):
    VpcInterfaceName: Optional[str] = None


class AddBridgeNetworkOutputRequest(BaseValidatorModel):
    IpAddress: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType
    Ttl: int


class MulticastSourceSettings(BaseValidatorModel):
    MulticastSourceIp: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AddEgressGatewayBridgeRequest(BaseValidatorModel):
    MaxBitrate: int


class VpcInterfaceRequest(BaseValidatorModel):
    Name: str
    RoleArn: str
    SecurityGroupIds: List[str]
    SubnetId: str
    NetworkInterfaceType: Optional[NetworkInterfaceTypeType] = None


class VpcInterface(BaseValidatorModel):
    Name: str
    NetworkInterfaceIds: List[str]
    NetworkInterfaceType: NetworkInterfaceTypeType
    RoleArn: str
    SecurityGroupIds: List[str]
    SubnetId: str


class AddIngressGatewayBridgeRequest(BaseValidatorModel):
    MaxBitrate: int
    MaxOutputs: int


class AddMaintenance(BaseValidatorModel):
    MaintenanceDay: MaintenanceDayType
    MaintenanceStartHour: str


class Encryption(BaseValidatorModel):
    RoleArn: str
    Algorithm: Optional[AlgorithmType] = None
    ConstantInitializationVector: Optional[str] = None
    DeviceId: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Region: Optional[str] = None
    ResourceId: Optional[str] = None
    SecretArn: Optional[str] = None
    Url: Optional[str] = None


class SilentAudio(BaseValidatorModel):
    State: Optional[StateType] = None
    ThresholdSeconds: Optional[int] = None


class BlackFrames(BaseValidatorModel):
    State: Optional[StateType] = None
    ThresholdSeconds: Optional[int] = None


class BridgeFlowOutput(BaseValidatorModel):
    FlowArn: str
    FlowSourceArn: str
    Name: str


class BridgeNetworkOutput(BaseValidatorModel):
    IpAddress: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType
    Ttl: int


class EgressGatewayBridge(BaseValidatorModel):
    MaxBitrate: int
    InstanceId: Optional[str] = None


class IngressGatewayBridge(BaseValidatorModel):
    MaxBitrate: int
    MaxOutputs: int
    InstanceId: Optional[str] = None


class MessageDetail(BaseValidatorModel):
    Code: str
    Message: str
    ResourceName: Optional[str] = None


class GatewayNetwork(BaseValidatorModel):
    CidrBlock: str
    Name: str


class DeleteBridgeRequest(BaseValidatorModel):
    BridgeArn: str


class DeleteFlowRequest(BaseValidatorModel):
    FlowArn: str


class DeleteGatewayRequest(BaseValidatorModel):
    GatewayArn: str


class DeregisterGatewayInstanceRequest(BaseValidatorModel):
    GatewayInstanceArn: str
    Force: Optional[bool] = None


class DescribeBridgeRequest(BaseValidatorModel):
    BridgeArn: str


class DescribeFlowRequest(BaseValidatorModel):
    FlowArn: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class Messages(BaseValidatorModel):
    Errors: List[str]


class DescribeFlowSourceMetadataRequest(BaseValidatorModel):
    FlowArn: str


class DescribeFlowSourceThumbnailRequest(BaseValidatorModel):
    FlowArn: str


class DescribeGatewayInstanceRequest(BaseValidatorModel):
    GatewayInstanceArn: str


class DescribeGatewayRequest(BaseValidatorModel):
    GatewayArn: str


class DescribeOfferingRequest(BaseValidatorModel):
    OfferingArn: str


class DescribeReservationRequest(BaseValidatorModel):
    ReservationArn: str


class InterfaceRequest(BaseValidatorModel):
    Name: str


class Interface(BaseValidatorModel):
    Name: str


class EncodingParametersRequest(BaseValidatorModel):
    CompressionFactor: float
    EncoderProfile: EncoderProfileType


class EncodingParameters(BaseValidatorModel):
    CompressionFactor: float
    EncoderProfile: EncoderProfileType


class SourcePriority(BaseValidatorModel):
    PrimarySource: Optional[str] = None


class Maintenance(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceDeadline: Optional[str] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartHour: Optional[str] = None


class FmtpRequest(BaseValidatorModel):
    ChannelOrder: Optional[str] = None
    Colorimetry: Optional[ColorimetryType] = None
    ExactFramerate: Optional[str] = None
    Par: Optional[str] = None
    Range: Optional[RangeType] = None
    ScanMode: Optional[ScanModeType] = None
    Tcs: Optional[TcsType] = None


class Fmtp(BaseValidatorModel):
    ChannelOrder: Optional[str] = None
    Colorimetry: Optional[ColorimetryType] = None
    ExactFramerate: Optional[str] = None
    Par: Optional[str] = None
    Range: Optional[RangeType] = None
    ScanMode: Optional[ScanModeType] = None
    Tcs: Optional[TcsType] = None


class FrameResolution(BaseValidatorModel):
    FrameHeight: int
    FrameWidth: int


class FrozenFrames(BaseValidatorModel):
    State: Optional[StateType] = None
    ThresholdSeconds: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBridgesRequest(BaseValidatorModel):
    FilterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedBridge(BaseValidatorModel):
    BridgeArn: str
    BridgeState: BridgeStateType
    BridgeType: str
    Name: str
    PlacementArn: str


class ListEntitlementsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedEntitlement(BaseValidatorModel):
    EntitlementArn: str
    EntitlementName: str
    DataTransferSubscriberFeePercent: Optional[int] = None


class ListFlowsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGatewayInstancesRequest(BaseValidatorModel):
    FilterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedGatewayInstance(BaseValidatorModel):
    GatewayArn: str
    GatewayInstanceArn: str
    InstanceId: str
    InstanceState: Optional[InstanceStateType] = None


class ListGatewaysRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedGateway(BaseValidatorModel):
    GatewayArn: str
    GatewayState: GatewayStateType
    Name: str


class ListOfferingsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListReservationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ResourceSpecification(BaseValidatorModel):
    ResourceType: Literal['Mbps_Outbound_Bandwidth']
    ReservedBitrate: Optional[int] = None


class Transport(BaseValidatorModel):
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


class PurchaseOfferingRequest(BaseValidatorModel):
    OfferingArn: str
    ReservationName: str
    Start: str


class RemoveBridgeOutputRequest(BaseValidatorModel):
    BridgeArn: str
    OutputName: str


class RemoveBridgeSourceRequest(BaseValidatorModel):
    BridgeArn: str
    SourceName: str


class RemoveFlowMediaStreamRequest(BaseValidatorModel):
    FlowArn: str
    MediaStreamName: str


class RemoveFlowOutputRequest(BaseValidatorModel):
    FlowArn: str
    OutputArn: str


class RemoveFlowSourceRequest(BaseValidatorModel):
    FlowArn: str
    SourceArn: str


class RemoveFlowVpcInterfaceRequest(BaseValidatorModel):
    FlowArn: str
    VpcInterfaceName: str


class RevokeFlowEntitlementRequest(BaseValidatorModel):
    EntitlementArn: str
    FlowArn: str


class StartFlowRequest(BaseValidatorModel):
    FlowArn: str


class StopFlowRequest(BaseValidatorModel):
    FlowArn: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateBridgeNetworkOutputRequest(BaseValidatorModel):
    IpAddress: Optional[str] = None
    NetworkName: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolType] = None
    Ttl: Optional[int] = None


class UpdateEgressGatewayBridgeRequest(BaseValidatorModel):
    MaxBitrate: Optional[int] = None


class UpdateIngressGatewayBridgeRequest(BaseValidatorModel):
    MaxBitrate: Optional[int] = None
    MaxOutputs: Optional[int] = None


class UpdateBridgeStateRequest(BaseValidatorModel):
    BridgeArn: str
    DesiredState: DesiredStateType


class UpdateEncryption(BaseValidatorModel):
    Algorithm: Optional[AlgorithmType] = None
    ConstantInitializationVector: Optional[str] = None
    DeviceId: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Region: Optional[str] = None
    ResourceId: Optional[str] = None
    RoleArn: Optional[str] = None
    SecretArn: Optional[str] = None
    Url: Optional[str] = None


class UpdateMaintenance(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartHour: Optional[str] = None


class UpdateGatewayInstanceRequest(BaseValidatorModel):
    GatewayInstanceArn: str
    BridgePlacement: Optional[BridgePlacementType] = None


class AddBridgeFlowSourceRequest(BaseValidatorModel):
    FlowArn: str
    Name: str
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None


class BridgeFlowSource(BaseValidatorModel):
    FlowArn: str
    Name: str
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None
    OutputArn: Optional[str] = None


class GatewayBridgeSource(BaseValidatorModel):
    BridgeArn: str
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None


class SetGatewayBridgeSourceRequest(BaseValidatorModel):
    BridgeArn: str
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None


class UpdateBridgeFlowSourceRequest(BaseValidatorModel):
    FlowArn: Optional[str] = None
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None


class UpdateGatewayBridgeSourceRequest(BaseValidatorModel):
    BridgeArn: Optional[str] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None


class AddBridgeOutputRequest(BaseValidatorModel):
    NetworkOutput: Optional[AddBridgeNetworkOutputRequest] = None


class AddBridgeNetworkSourceRequest(BaseValidatorModel):
    MulticastIp: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType
    MulticastSourceSettings: Optional[MulticastSourceSettings] = None


class BridgeNetworkSource(BaseValidatorModel):
    MulticastIp: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType
    MulticastSourceSettings: Optional[MulticastSourceSettings] = None


class UpdateBridgeNetworkSourceRequest(BaseValidatorModel):
    MulticastIp: Optional[str] = None
    MulticastSourceSettings: Optional[MulticastSourceSettings] = None
    NetworkName: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolType] = None


class DeleteBridgeResponse(BaseValidatorModel):
    BridgeArn: str
    ResponseMetadata: ResponseMetadata


class DeleteFlowResponse(BaseValidatorModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class DeleteGatewayResponse(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadata


class DeregisterGatewayInstanceResponse(BaseValidatorModel):
    GatewayInstanceArn: str
    InstanceState: InstanceStateType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RemoveBridgeOutputResponse(BaseValidatorModel):
    BridgeArn: str
    OutputName: str
    ResponseMetadata: ResponseMetadata


class RemoveBridgeSourceResponse(BaseValidatorModel):
    BridgeArn: str
    SourceName: str
    ResponseMetadata: ResponseMetadata


class RemoveFlowMediaStreamResponse(BaseValidatorModel):
    FlowArn: str
    MediaStreamName: str
    ResponseMetadata: ResponseMetadata


class RemoveFlowOutputResponse(BaseValidatorModel):
    FlowArn: str
    OutputArn: str
    ResponseMetadata: ResponseMetadata


class RemoveFlowSourceResponse(BaseValidatorModel):
    FlowArn: str
    SourceArn: str
    ResponseMetadata: ResponseMetadata


class RemoveFlowVpcInterfaceResponse(BaseValidatorModel):
    FlowArn: str
    NonDeletedNetworkInterfaceIds: List[str]
    VpcInterfaceName: str
    ResponseMetadata: ResponseMetadata


class RevokeFlowEntitlementResponse(BaseValidatorModel):
    EntitlementArn: str
    FlowArn: str
    ResponseMetadata: ResponseMetadata


class StartFlowResponse(BaseValidatorModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class StopFlowResponse(BaseValidatorModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class UpdateBridgeStateResponse(BaseValidatorModel):
    BridgeArn: str
    DesiredState: DesiredStateType
    ResponseMetadata: ResponseMetadata


class UpdateGatewayInstanceResponse(BaseValidatorModel):
    BridgePlacement: BridgePlacementType
    GatewayInstanceArn: str
    ResponseMetadata: ResponseMetadata


class AddFlowVpcInterfacesRequest(BaseValidatorModel):
    FlowArn: str
    VpcInterfaces: List[VpcInterfaceRequest]


class AddFlowVpcInterfacesResponse(BaseValidatorModel):
    FlowArn: str
    VpcInterfaces: List[VpcInterface]
    ResponseMetadata: ResponseMetadata


class Entitlement(BaseValidatorModel):
    EntitlementArn: str
    Name: str
    Subscribers: List[str]
    DataTransferSubscriberFeePercent: Optional[int] = None
    Description: Optional[str] = None
    Encryption: Optional[Encryption] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None


class GrantEntitlementRequest(BaseValidatorModel):
    Subscribers: List[str]
    DataTransferSubscriberFeePercent: Optional[int] = None
    Description: Optional[str] = None
    Encryption: Optional[Encryption] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None
    Name: Optional[str] = None


class AudioMonitoringSetting(BaseValidatorModel):
    SilentAudio: Optional[SilentAudio] = None


class BridgeOutput(BaseValidatorModel):
    FlowOutput: Optional[BridgeFlowOutput] = None
    NetworkOutput: Optional[BridgeNetworkOutput] = None


class GatewayInstance(BaseValidatorModel):
    BridgePlacement: BridgePlacementType
    ConnectionStatus: ConnectionStatusType
    GatewayArn: str
    GatewayInstanceArn: str
    InstanceId: str
    InstanceState: InstanceStateType
    RunningBridgeCount: int
    InstanceMessages: Optional[List[MessageDetail]] = None


class ThumbnailDetails(BaseValidatorModel):
    FlowArn: str
    ThumbnailMessages: List[MessageDetail]
    Thumbnail: Optional[str] = None
    Timecode: Optional[str] = None
    Timestamp: Optional[datetime] = None


class CreateGatewayRequest(BaseValidatorModel):
    EgressCidrBlocks: List[str]
    Name: str
    Networks: List[GatewayNetwork]


class Gateway(BaseValidatorModel):
    EgressCidrBlocks: List[str]
    GatewayArn: str
    Name: str
    Networks: List[GatewayNetwork]
    GatewayMessages: Optional[List[MessageDetail]] = None
    GatewayState: Optional[GatewayStateType] = None


class DescribeFlowRequestWaitExtraExtra(BaseValidatorModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeFlowRequestWaitExtra(BaseValidatorModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeFlowRequestWait(BaseValidatorModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DestinationConfigurationRequest(BaseValidatorModel):
    DestinationIp: str
    DestinationPort: int
    Interface: InterfaceRequest


class InputConfigurationRequest(BaseValidatorModel):
    InputPort: int
    Interface: InterfaceRequest


class DestinationConfiguration(BaseValidatorModel):
    DestinationIp: str
    DestinationPort: int
    Interface: Interface
    OutboundIp: str


class InputConfiguration(BaseValidatorModel):
    InputIp: str
    InputPort: int
    Interface: Interface


class FailoverConfig(BaseValidatorModel):
    FailoverMode: Optional[FailoverModeType] = None
    RecoveryWindow: Optional[int] = None
    SourcePriority: Optional[SourcePriority] = None
    State: Optional[StateType] = None


class UpdateFailoverConfig(BaseValidatorModel):
    FailoverMode: Optional[FailoverModeType] = None
    RecoveryWindow: Optional[int] = None
    SourcePriority: Optional[SourcePriority] = None
    State: Optional[StateType] = None


class ListedFlow(BaseValidatorModel):
    AvailabilityZone: str
    Description: str
    FlowArn: str
    Name: str
    SourceType: SourceTypeType
    Status: StatusType
    Maintenance: Optional[Maintenance] = None


class MediaStreamAttributesRequest(BaseValidatorModel):
    Fmtp: Optional[FmtpRequest] = None
    Lang: Optional[str] = None


class MediaStreamAttributes(BaseValidatorModel):
    Fmtp: Fmtp
    Lang: Optional[str] = None


class TransportStream(BaseValidatorModel):
    Pid: int
    StreamType: str
    Channels: Optional[int] = None
    Codec: Optional[str] = None
    FrameRate: Optional[str] = None
    FrameResolution: Optional[FrameResolution] = None
    SampleRate: Optional[int] = None
    SampleSize: Optional[int] = None


class VideoMonitoringSetting(BaseValidatorModel):
    BlackFrames: Optional[BlackFrames] = None
    FrozenFrames: Optional[FrozenFrames] = None


class ListBridgesRequestPaginate(BaseValidatorModel):
    FilterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEntitlementsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFlowsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGatewayInstancesRequestPaginate(BaseValidatorModel):
    FilterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGatewaysRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOfferingsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReservationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBridgesResponse(BaseValidatorModel):
    Bridges: List[ListedBridge]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEntitlementsResponse(BaseValidatorModel):
    Entitlements: List[ListedEntitlement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGatewayInstancesResponse(BaseValidatorModel):
    Instances: List[ListedGatewayInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGatewaysResponse(BaseValidatorModel):
    Gateways: List[ListedGateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Offering(BaseValidatorModel):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal['MONTHS']
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal['HOURLY']
    ResourceSpecification: ResourceSpecification


class Reservation(BaseValidatorModel):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal['MONTHS']
    End: str
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal['HOURLY']
    ReservationArn: str
    ReservationName: str
    ReservationState: ReservationStateType
    ResourceSpecification: ResourceSpecification
    Start: str


class UpdateBridgeOutputRequest(BaseValidatorModel):
    BridgeArn: str
    OutputName: str
    NetworkOutput: Optional[UpdateBridgeNetworkOutputRequest] = None


class UpdateFlowEntitlementRequest(BaseValidatorModel):
    EntitlementArn: str
    FlowArn: str
    Description: Optional[str] = None
    Encryption: Optional[UpdateEncryption] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None
    Subscribers: Optional[List[str]] = None


class AddBridgeOutputsRequest(BaseValidatorModel):
    BridgeArn: str
    Outputs: List[AddBridgeOutputRequest]


class AddBridgeSourceRequest(BaseValidatorModel):
    FlowSource: Optional[AddBridgeFlowSourceRequest] = None
    NetworkSource: Optional[AddBridgeNetworkSourceRequest] = None


class BridgeSource(BaseValidatorModel):
    FlowSource: Optional[BridgeFlowSource] = None
    NetworkSource: Optional[BridgeNetworkSource] = None


class UpdateBridgeSourceRequest(BaseValidatorModel):
    BridgeArn: str
    SourceName: str
    FlowSource: Optional[UpdateBridgeFlowSourceRequest] = None
    NetworkSource: Optional[UpdateBridgeNetworkSourceRequest] = None


class GrantFlowEntitlementsResponse(BaseValidatorModel):
    Entitlements: List[Entitlement]
    FlowArn: str
    ResponseMetadata: ResponseMetadata


class UpdateFlowEntitlementResponse(BaseValidatorModel):
    Entitlement: Entitlement
    FlowArn: str
    ResponseMetadata: ResponseMetadata


class GrantFlowEntitlementsRequest(BaseValidatorModel):
    Entitlements: List[GrantEntitlementRequest]
    FlowArn: str


class AddBridgeOutputsResponse(BaseValidatorModel):
    BridgeArn: str
    Outputs: List[BridgeOutput]
    ResponseMetadata: ResponseMetadata


class UpdateBridgeOutputResponse(BaseValidatorModel):
    BridgeArn: str
    Output: BridgeOutput
    ResponseMetadata: ResponseMetadata


class DescribeGatewayInstanceResponse(BaseValidatorModel):
    GatewayInstance: GatewayInstance
    ResponseMetadata: ResponseMetadata


class DescribeFlowSourceThumbnailResponse(BaseValidatorModel):
    ThumbnailDetails: ThumbnailDetails
    ResponseMetadata: ResponseMetadata


class CreateGatewayResponse(BaseValidatorModel):
    Gateway: Gateway
    ResponseMetadata: ResponseMetadata


class DescribeGatewayResponse(BaseValidatorModel):
    Gateway: Gateway
    ResponseMetadata: ResponseMetadata


class MediaStreamOutputConfigurationRequest(BaseValidatorModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    DestinationConfigurations: Optional[List[DestinationConfigurationRequest]] = None
    EncodingParameters: Optional[EncodingParametersRequest] = None


class MediaStreamSourceConfigurationRequest(BaseValidatorModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    InputConfigurations: Optional[List[InputConfigurationRequest]] = None


class MediaStreamOutputConfiguration(BaseValidatorModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    DestinationConfigurations: Optional[List[DestinationConfiguration]] = None
    EncodingParameters: Optional[EncodingParameters] = None


class MediaStreamSourceConfiguration(BaseValidatorModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    InputConfigurations: Optional[List[InputConfiguration]] = None


class UpdateBridgeRequest(BaseValidatorModel):
    BridgeArn: str
    EgressGatewayBridge: Optional[UpdateEgressGatewayBridgeRequest] = None
    IngressGatewayBridge: Optional[UpdateIngressGatewayBridgeRequest] = None
    SourceFailoverConfig: Optional[UpdateFailoverConfig] = None


class ListFlowsResponse(BaseValidatorModel):
    Flows: List[ListedFlow]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AddMediaStreamRequest(BaseValidatorModel):
    MediaStreamId: int
    MediaStreamName: str
    MediaStreamType: MediaStreamTypeType
    Attributes: Optional[MediaStreamAttributesRequest] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    VideoFormat: Optional[str] = None


class UpdateFlowMediaStreamRequest(BaseValidatorModel):
    FlowArn: str
    MediaStreamName: str
    Attributes: Optional[MediaStreamAttributesRequest] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    MediaStreamType: Optional[MediaStreamTypeType] = None
    VideoFormat: Optional[str] = None


class MediaStream(BaseValidatorModel):
    Fmt: int
    MediaStreamId: int
    MediaStreamName: str
    MediaStreamType: MediaStreamTypeType
    Attributes: Optional[MediaStreamAttributes] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    VideoFormat: Optional[str] = None


class TransportStreamProgram(BaseValidatorModel):
    PcrPid: int
    ProgramNumber: int
    ProgramPid: int
    Streams: List[TransportStream]
    ProgramName: Optional[str] = None


class MonitoringConfigOutput(BaseValidatorModel):
    ThumbnailState: Optional[ThumbnailStateType] = None
    AudioMonitoringSettings: Optional[List[AudioMonitoringSetting]] = None
    ContentQualityAnalysisState: Optional[ContentQualityAnalysisStateType] = None
    VideoMonitoringSettings: Optional[List[VideoMonitoringSetting]] = None


class MonitoringConfig(BaseValidatorModel):
    ThumbnailState: Optional[ThumbnailStateType] = None
    AudioMonitoringSettings: Optional[List[AudioMonitoringSetting]] = None
    ContentQualityAnalysisState: Optional[ContentQualityAnalysisStateType] = None
    VideoMonitoringSettings: Optional[List[VideoMonitoringSetting]] = None


class DescribeOfferingResponse(BaseValidatorModel):
    Offering: Offering
    ResponseMetadata: ResponseMetadata


class ListOfferingsResponse(BaseValidatorModel):
    Offerings: List[Offering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeReservationResponse(BaseValidatorModel):
    Reservation: Reservation
    ResponseMetadata: ResponseMetadata


class ListReservationsResponse(BaseValidatorModel):
    Reservations: List[Reservation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PurchaseOfferingResponse(BaseValidatorModel):
    Reservation: Reservation
    ResponseMetadata: ResponseMetadata


class AddBridgeSourcesRequest(BaseValidatorModel):
    BridgeArn: str
    Sources: List[AddBridgeSourceRequest]


class CreateBridgeRequest(BaseValidatorModel):
    Name: str
    PlacementArn: str
    Sources: List[AddBridgeSourceRequest]
    EgressGatewayBridge: Optional[AddEgressGatewayBridgeRequest] = None
    IngressGatewayBridge: Optional[AddIngressGatewayBridgeRequest] = None
    Outputs: Optional[List[AddBridgeOutputRequest]] = None
    SourceFailoverConfig: Optional[FailoverConfig] = None


class AddBridgeSourcesResponse(BaseValidatorModel):
    BridgeArn: str
    Sources: List[BridgeSource]
    ResponseMetadata: ResponseMetadata


class Bridge(BaseValidatorModel):
    BridgeArn: str
    BridgeState: BridgeStateType
    Name: str
    PlacementArn: str
    BridgeMessages: Optional[List[MessageDetail]] = None
    EgressGatewayBridge: Optional[EgressGatewayBridge] = None
    IngressGatewayBridge: Optional[IngressGatewayBridge] = None
    Outputs: Optional[List[BridgeOutput]] = None
    SourceFailoverConfig: Optional[FailoverConfig] = None
    Sources: Optional[List[BridgeSource]] = None


class UpdateBridgeSourceResponse(BaseValidatorModel):
    BridgeArn: str
    Source: BridgeSource
    ResponseMetadata: ResponseMetadata


class AddOutputRequest(BaseValidatorModel):
    Protocol: ProtocolType
    CidrAllowList: Optional[List[str]] = None
    Description: Optional[str] = None
    Destination: Optional[str] = None
    Encryption: Optional[Encryption] = None
    MaxLatency: Optional[int] = None
    MediaStreamOutputConfigurations: Optional[List[MediaStreamOutputConfigurationRequest]] = None
    MinLatency: Optional[int] = None
    Name: Optional[str] = None
    Port: Optional[int] = None
    RemoteId: Optional[str] = None
    SenderControlPort: Optional[int] = None
    SmoothingLatency: Optional[int] = None
    StreamId: Optional[str] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None
    OutputStatus: Optional[OutputStatusType] = None


class UpdateFlowOutputRequest(BaseValidatorModel):
    FlowArn: str
    OutputArn: str
    CidrAllowList: Optional[List[str]] = None
    Description: Optional[str] = None
    Destination: Optional[str] = None
    Encryption: Optional[UpdateEncryption] = None
    MaxLatency: Optional[int] = None
    MediaStreamOutputConfigurations: Optional[List[MediaStreamOutputConfigurationRequest]] = None
    MinLatency: Optional[int] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolType] = None
    RemoteId: Optional[str] = None
    SenderControlPort: Optional[int] = None
    SenderIpAddress: Optional[str] = None
    SmoothingLatency: Optional[int] = None
    StreamId: Optional[str] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None
    OutputStatus: Optional[OutputStatusType] = None


class SetSourceRequest(BaseValidatorModel):
    Decryption: Optional[Encryption] = None
    Description: Optional[str] = None
    EntitlementArn: Optional[str] = None
    IngestPort: Optional[int] = None
    MaxBitrate: Optional[int] = None
    MaxLatency: Optional[int] = None
    MaxSyncBuffer: Optional[int] = None
    MediaStreamSourceConfigurations: Optional[List[MediaStreamSourceConfigurationRequest]] = None
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
    GatewayBridgeSource: Optional[SetGatewayBridgeSourceRequest] = None


class UpdateFlowSourceRequest(BaseValidatorModel):
    FlowArn: str
    SourceArn: str
    Decryption: Optional[UpdateEncryption] = None
    Description: Optional[str] = None
    EntitlementArn: Optional[str] = None
    IngestPort: Optional[int] = None
    MaxBitrate: Optional[int] = None
    MaxLatency: Optional[int] = None
    MaxSyncBuffer: Optional[int] = None
    MediaStreamSourceConfigurations: Optional[List[MediaStreamSourceConfigurationRequest]] = None
    MinLatency: Optional[int] = None
    Protocol: Optional[ProtocolType] = None
    SenderControlPort: Optional[int] = None
    SenderIpAddress: Optional[str] = None
    SourceListenerAddress: Optional[str] = None
    SourceListenerPort: Optional[int] = None
    StreamId: Optional[str] = None
    VpcInterfaceName: Optional[str] = None
    WhitelistCidr: Optional[str] = None
    GatewayBridgeSource: Optional[UpdateGatewayBridgeSourceRequest] = None


class Output(BaseValidatorModel):
    Name: str
    OutputArn: str
    DataTransferSubscriberFeePercent: Optional[int] = None
    Description: Optional[str] = None
    Destination: Optional[str] = None
    Encryption: Optional[Encryption] = None
    EntitlementArn: Optional[str] = None
    ListenerAddress: Optional[str] = None
    MediaLiveInputArn: Optional[str] = None
    MediaStreamOutputConfigurations: Optional[List[MediaStreamOutputConfiguration]] = None
    Port: Optional[int] = None
    Transport: Optional[Transport] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachment] = None
    BridgeArn: Optional[str] = None
    BridgePorts: Optional[List[int]] = None
    OutputStatus: Optional[OutputStatusType] = None


class Source(BaseValidatorModel):
    Name: str
    SourceArn: str
    DataTransferSubscriberFeePercent: Optional[int] = None
    Decryption: Optional[Encryption] = None
    Description: Optional[str] = None
    EntitlementArn: Optional[str] = None
    IngestIp: Optional[str] = None
    IngestPort: Optional[int] = None
    MediaStreamSourceConfigurations: Optional[List[MediaStreamSourceConfiguration]] = None
    SenderControlPort: Optional[int] = None
    SenderIpAddress: Optional[str] = None
    Transport: Optional[Transport] = None
    VpcInterfaceName: Optional[str] = None
    WhitelistCidr: Optional[str] = None
    GatewayBridgeSource: Optional[GatewayBridgeSource] = None


class AddFlowMediaStreamsRequest(BaseValidatorModel):
    FlowArn: str
    MediaStreams: List[AddMediaStreamRequest]


class AddFlowMediaStreamsResponse(BaseValidatorModel):
    FlowArn: str
    MediaStreams: List[MediaStream]
    ResponseMetadata: ResponseMetadata


class UpdateFlowMediaStreamResponse(BaseValidatorModel):
    FlowArn: str
    MediaStream: MediaStream
    ResponseMetadata: ResponseMetadata


class TransportMediaInfo(BaseValidatorModel):
    Programs: List[TransportStreamProgram]

MonitoringConfigUnion = Union[MonitoringConfig, MonitoringConfigOutput]


class CreateBridgeResponse(BaseValidatorModel):
    Bridge: Bridge
    ResponseMetadata: ResponseMetadata


class DescribeBridgeResponse(BaseValidatorModel):
    Bridge: Bridge
    ResponseMetadata: ResponseMetadata


class UpdateBridgeResponse(BaseValidatorModel):
    Bridge: Bridge
    ResponseMetadata: ResponseMetadata


class AddFlowOutputsRequest(BaseValidatorModel):
    FlowArn: str
    Outputs: List[AddOutputRequest]


class AddFlowSourcesRequest(BaseValidatorModel):
    FlowArn: str
    Sources: List[SetSourceRequest]


class AddFlowOutputsResponse(BaseValidatorModel):
    FlowArn: str
    Outputs: List[Output]
    ResponseMetadata: ResponseMetadata


class UpdateFlowOutputResponse(BaseValidatorModel):
    FlowArn: str
    Output: Output
    ResponseMetadata: ResponseMetadata


class AddFlowSourcesResponse(BaseValidatorModel):
    FlowArn: str
    Sources: List[Source]
    ResponseMetadata: ResponseMetadata


class Flow(BaseValidatorModel):
    AvailabilityZone: str
    Entitlements: List[Entitlement]
    FlowArn: str
    Name: str
    Outputs: List[Output]
    Source: Source
    Status: StatusType
    Description: Optional[str] = None
    EgressIp: Optional[str] = None
    MediaStreams: Optional[List[MediaStream]] = None
    SourceFailoverConfig: Optional[FailoverConfig] = None
    Sources: Optional[List[Source]] = None
    VpcInterfaces: Optional[List[VpcInterface]] = None
    Maintenance: Optional[Maintenance] = None
    SourceMonitoringConfig: Optional[MonitoringConfigOutput] = None


class UpdateFlowSourceResponse(BaseValidatorModel):
    FlowArn: str
    Source: Source
    ResponseMetadata: ResponseMetadata


class DescribeFlowSourceMetadataResponse(BaseValidatorModel):
    FlowArn: str
    Messages: List[MessageDetail]
    Timestamp: datetime
    TransportMediaInfo: TransportMediaInfo
    ResponseMetadata: ResponseMetadata


class CreateFlowRequest(BaseValidatorModel):
    Name: str
    AvailabilityZone: Optional[str] = None
    Entitlements: Optional[List[GrantEntitlementRequest]] = None
    MediaStreams: Optional[List[AddMediaStreamRequest]] = None
    Outputs: Optional[List[AddOutputRequest]] = None
    Source: Optional[SetSourceRequest] = None
    SourceFailoverConfig: Optional[FailoverConfig] = None
    Sources: Optional[List[SetSourceRequest]] = None
    VpcInterfaces: Optional[List[VpcInterfaceRequest]] = None
    Maintenance: Optional[AddMaintenance] = None
    SourceMonitoringConfig: Optional[MonitoringConfigUnion] = None


class UpdateFlowRequest(BaseValidatorModel):
    FlowArn: str
    SourceFailoverConfig: Optional[UpdateFailoverConfig] = None
    Maintenance: Optional[UpdateMaintenance] = None
    SourceMonitoringConfig: Optional[MonitoringConfigUnion] = None


class CreateFlowResponse(BaseValidatorModel):
    Flow: Flow
    ResponseMetadata: ResponseMetadata


class DescribeFlowResponse(BaseValidatorModel):
    Flow: Flow
    Messages: Messages
    ResponseMetadata: ResponseMetadata


class UpdateFlowResponse(BaseValidatorModel):
    Flow: Flow
    ResponseMetadata: ResponseMetadata
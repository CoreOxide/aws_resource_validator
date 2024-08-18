from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class VpcInterfaceAttachmentTypeDef(BaseValidatorModel):
    VpcInterfaceName: Optional[str] = None

class AddBridgeNetworkOutputRequestTypeDef(BaseValidatorModel):
    IpAddress: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType
    Ttl: int

class AddBridgeNetworkSourceRequestTypeDef(BaseValidatorModel):
    MulticastIp: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AddEgressGatewayBridgeRequestTypeDef(BaseValidatorModel):
    MaxBitrate: int

class VpcInterfaceRequestTypeDef(BaseValidatorModel):
    Name: str
    RoleArn: str
    SecurityGroupIds: Sequence[str]
    SubnetId: str
    NetworkInterfaceType: Optional[NetworkInterfaceTypeType] = None

class VpcInterfaceTypeDef(BaseValidatorModel):
    Name: str
    NetworkInterfaceIds: List[str]
    NetworkInterfaceType: NetworkInterfaceTypeType
    RoleArn: str
    SecurityGroupIds: List[str]
    SubnetId: str

class AddIngressGatewayBridgeRequestTypeDef(BaseValidatorModel):
    MaxBitrate: int
    MaxOutputs: int

class AddMaintenanceTypeDef(BaseValidatorModel):
    MaintenanceDay: MaintenanceDayType
    MaintenanceStartHour: str

class EncryptionTypeDef(BaseValidatorModel):
    RoleArn: str
    Algorithm: Optional[AlgorithmType] = None
    ConstantInitializationVector: Optional[str] = None
    DeviceId: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Region: Optional[str] = None
    ResourceId: Optional[str] = None
    SecretArn: Optional[str] = None
    Url: Optional[str] = None

class BridgeFlowOutputTypeDef(BaseValidatorModel):
    FlowArn: str
    FlowSourceArn: str
    Name: str

class BridgeNetworkOutputTypeDef(BaseValidatorModel):
    IpAddress: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType
    Ttl: int

class BridgeNetworkSourceTypeDef(BaseValidatorModel):
    MulticastIp: str
    Name: str
    NetworkName: str
    Port: int
    Protocol: ProtocolType

class EgressGatewayBridgeTypeDef(BaseValidatorModel):
    MaxBitrate: int
    InstanceId: Optional[str] = None

class IngressGatewayBridgeTypeDef(BaseValidatorModel):
    MaxBitrate: int
    MaxOutputs: int
    InstanceId: Optional[str] = None

class MessageDetailTypeDef(BaseValidatorModel):
    Code: str
    Message: str
    ResourceName: Optional[str] = None

class GatewayNetworkTypeDef(BaseValidatorModel):
    CidrBlock: str
    Name: str

class DeleteBridgeRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str

class DeleteFlowRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str

class DeleteGatewayRequestRequestTypeDef(BaseValidatorModel):
    GatewayArn: str

class DeregisterGatewayInstanceRequestRequestTypeDef(BaseValidatorModel):
    GatewayInstanceArn: str
    Force: Optional[bool] = None

class DescribeBridgeRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeFlowRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str

class MessagesTypeDef(BaseValidatorModel):
    Errors: List[str]

class DescribeFlowSourceMetadataRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str

class DescribeGatewayInstanceRequestRequestTypeDef(BaseValidatorModel):
    GatewayInstanceArn: str

class DescribeGatewayRequestRequestTypeDef(BaseValidatorModel):
    GatewayArn: str

class DescribeOfferingRequestRequestTypeDef(BaseValidatorModel):
    OfferingArn: str

class DescribeReservationRequestRequestTypeDef(BaseValidatorModel):
    ReservationArn: str

class InterfaceRequestTypeDef(BaseValidatorModel):
    Name: str

class InterfaceTypeDef(BaseValidatorModel):
    Name: str

class EncodingParametersRequestTypeDef(BaseValidatorModel):
    CompressionFactor: float
    EncoderProfile: EncoderProfileType

class EncodingParametersTypeDef(BaseValidatorModel):
    CompressionFactor: float
    EncoderProfile: EncoderProfileType

class SourcePriorityTypeDef(BaseValidatorModel):
    PrimarySource: Optional[str] = None

class MaintenanceTypeDef(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceDeadline: Optional[str] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartHour: Optional[str] = None

class FmtpRequestTypeDef(BaseValidatorModel):
    ChannelOrder: Optional[str] = None
    Colorimetry: Optional[ColorimetryType] = None
    ExactFramerate: Optional[str] = None
    Par: Optional[str] = None
    Range: Optional[RangeType] = None
    ScanMode: Optional[ScanModeType] = None
    Tcs: Optional[TcsType] = None

class FmtpTypeDef(BaseValidatorModel):
    ChannelOrder: Optional[str] = None
    Colorimetry: Optional[ColorimetryType] = None
    ExactFramerate: Optional[str] = None
    Par: Optional[str] = None
    Range: Optional[RangeType] = None
    ScanMode: Optional[ScanModeType] = None
    Tcs: Optional[TcsType] = None

class FrameResolutionTypeDef(BaseValidatorModel):
    FrameHeight: int
    FrameWidth: int

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBridgesRequestRequestTypeDef(BaseValidatorModel):
    FilterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedBridgeTypeDef(BaseValidatorModel):
    BridgeArn: str
    BridgeState: BridgeStateType
    BridgeType: str
    Name: str
    PlacementArn: str

class ListEntitlementsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedEntitlementTypeDef(BaseValidatorModel):
    EntitlementArn: str
    EntitlementName: str
    DataTransferSubscriberFeePercent: Optional[int] = None

class ListFlowsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGatewayInstancesRequestRequestTypeDef(BaseValidatorModel):
    FilterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedGatewayInstanceTypeDef(BaseValidatorModel):
    GatewayArn: str
    GatewayInstanceArn: str
    InstanceId: str
    InstanceState: Optional[InstanceStateType] = None

class ListGatewaysRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedGatewayTypeDef(BaseValidatorModel):
    GatewayArn: str
    GatewayState: GatewayStateType
    Name: str

class ListOfferingsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListReservationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ResourceSpecificationTypeDef(BaseValidatorModel):
    ResourceType: Literal["Mbps_Outbound_Bandwidth"]
    ReservedBitrate: Optional[int] = None

class TransportTypeDef(BaseValidatorModel):
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

class PurchaseOfferingRequestRequestTypeDef(BaseValidatorModel):
    OfferingArn: str
    ReservationName: str
    Start: str

class RemoveBridgeOutputRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    OutputName: str

class RemoveBridgeSourceRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    SourceName: str

class RemoveFlowMediaStreamRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    MediaStreamName: str

class RemoveFlowOutputRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    OutputArn: str

class RemoveFlowSourceRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    SourceArn: str

class RemoveFlowVpcInterfaceRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    VpcInterfaceName: str

class RevokeFlowEntitlementRequestRequestTypeDef(BaseValidatorModel):
    EntitlementArn: str
    FlowArn: str

class StartFlowRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str

class StopFlowRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateBridgeNetworkOutputRequestTypeDef(BaseValidatorModel):
    IpAddress: Optional[str] = None
    NetworkName: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolType] = None
    Ttl: Optional[int] = None

class UpdateBridgeNetworkSourceRequestTypeDef(BaseValidatorModel):
    MulticastIp: Optional[str] = None
    NetworkName: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[ProtocolType] = None

class UpdateEgressGatewayBridgeRequestTypeDef(BaseValidatorModel):
    MaxBitrate: Optional[int] = None

class UpdateIngressGatewayBridgeRequestTypeDef(BaseValidatorModel):
    MaxBitrate: Optional[int] = None
    MaxOutputs: Optional[int] = None

class UpdateBridgeStateRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    DesiredState: DesiredStateType

class UpdateEncryptionTypeDef(BaseValidatorModel):
    Algorithm: Optional[AlgorithmType] = None
    ConstantInitializationVector: Optional[str] = None
    DeviceId: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Region: Optional[str] = None
    ResourceId: Optional[str] = None
    RoleArn: Optional[str] = None
    SecretArn: Optional[str] = None
    Url: Optional[str] = None

class UpdateMaintenanceTypeDef(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartHour: Optional[str] = None

class UpdateGatewayInstanceRequestRequestTypeDef(BaseValidatorModel):
    GatewayInstanceArn: str
    BridgePlacement: Optional[BridgePlacementType] = None

class AddBridgeFlowSourceRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    Name: str
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class BridgeFlowSourceTypeDef(BaseValidatorModel):
    FlowArn: str
    Name: str
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None
    OutputArn: Optional[str] = None

class GatewayBridgeSourceTypeDef(BaseValidatorModel):
    BridgeArn: str
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class SetGatewayBridgeSourceRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class UpdateBridgeFlowSourceRequestTypeDef(BaseValidatorModel):
    FlowArn: Optional[str] = None
    FlowVpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class UpdateGatewayBridgeSourceRequestTypeDef(BaseValidatorModel):
    BridgeArn: Optional[str] = None
    VpcInterfaceAttachment: Optional[VpcInterfaceAttachmentTypeDef] = None

class AddBridgeOutputRequestTypeDef(BaseValidatorModel):
    NetworkOutput: Optional[AddBridgeNetworkOutputRequestTypeDef] = None

class DeleteBridgeResponseTypeDef(BaseValidatorModel):
    BridgeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayResponseTypeDef(BaseValidatorModel):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterGatewayInstanceResponseTypeDef(BaseValidatorModel):
    GatewayInstanceArn: str
    InstanceState: InstanceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveBridgeOutputResponseTypeDef(BaseValidatorModel):
    BridgeArn: str
    OutputName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveBridgeSourceResponseTypeDef(BaseValidatorModel):
    BridgeArn: str
    SourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowMediaStreamResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    MediaStreamName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowOutputResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    OutputArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowSourceResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    SourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowVpcInterfaceResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    NonDeletedNetworkInterfaceIds: List[str]
    VpcInterfaceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeFlowEntitlementResponseTypeDef(BaseValidatorModel):
    EntitlementArn: str
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlowResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopFlowResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeStateResponseTypeDef(BaseValidatorModel):
    BridgeArn: str
    DesiredState: DesiredStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayInstanceResponseTypeDef(BaseValidatorModel):
    BridgePlacement: BridgePlacementType
    GatewayInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowVpcInterfacesRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    VpcInterfaces: Sequence[VpcInterfaceRequestTypeDef]

class AddFlowVpcInterfacesResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    VpcInterfaces: List[VpcInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EntitlementTypeDef(BaseValidatorModel):
    EntitlementArn: str
    Name: str
    Subscribers: List[str]
    DataTransferSubscriberFeePercent: Optional[int] = None
    Description: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None

class GrantEntitlementRequestTypeDef(BaseValidatorModel):
    Subscribers: Sequence[str]
    DataTransferSubscriberFeePercent: Optional[int] = None
    Description: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None
    Name: Optional[str] = None

class BridgeOutputTypeDef(BaseValidatorModel):
    FlowOutput: Optional[BridgeFlowOutputTypeDef] = None
    NetworkOutput: Optional[BridgeNetworkOutputTypeDef] = None

class GatewayInstanceTypeDef(BaseValidatorModel):
    BridgePlacement: BridgePlacementType
    ConnectionStatus: ConnectionStatusType
    GatewayArn: str
    GatewayInstanceArn: str
    InstanceId: str
    InstanceState: InstanceStateType
    RunningBridgeCount: int
    InstanceMessages: Optional[List[MessageDetailTypeDef]] = None

class CreateGatewayRequestRequestTypeDef(BaseValidatorModel):
    EgressCidrBlocks: Sequence[str]
    Name: str
    Networks: Sequence[GatewayNetworkTypeDef]

class GatewayTypeDef(BaseValidatorModel):
    EgressCidrBlocks: List[str]
    GatewayArn: str
    Name: str
    Networks: List[GatewayNetworkTypeDef]
    GatewayMessages: Optional[List[MessageDetailTypeDef]] = None
    GatewayState: Optional[GatewayStateType] = None

class DescribeFlowRequestFlowActiveWaitTypeDef(BaseValidatorModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFlowRequestFlowDeletedWaitTypeDef(BaseValidatorModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFlowRequestFlowStandbyWaitTypeDef(BaseValidatorModel):
    FlowArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DestinationConfigurationRequestTypeDef(BaseValidatorModel):
    DestinationIp: str
    DestinationPort: int
    Interface: InterfaceRequestTypeDef

class InputConfigurationRequestTypeDef(BaseValidatorModel):
    InputPort: int
    Interface: InterfaceRequestTypeDef

class DestinationConfigurationTypeDef(BaseValidatorModel):
    DestinationIp: str
    DestinationPort: int
    Interface: InterfaceTypeDef
    OutboundIp: str

class InputConfigurationTypeDef(BaseValidatorModel):
    InputIp: str
    InputPort: int
    Interface: InterfaceTypeDef

class FailoverConfigTypeDef(BaseValidatorModel):
    FailoverMode: Optional[FailoverModeType] = None
    RecoveryWindow: Optional[int] = None
    SourcePriority: Optional[SourcePriorityTypeDef] = None
    State: Optional[StateType] = None

class UpdateFailoverConfigTypeDef(BaseValidatorModel):
    FailoverMode: Optional[FailoverModeType] = None
    RecoveryWindow: Optional[int] = None
    SourcePriority: Optional[SourcePriorityTypeDef] = None
    State: Optional[StateType] = None

class ListedFlowTypeDef(BaseValidatorModel):
    AvailabilityZone: str
    Description: str
    FlowArn: str
    Name: str
    SourceType: SourceTypeType
    Status: StatusType
    Maintenance: Optional[MaintenanceTypeDef] = None

class MediaStreamAttributesRequestTypeDef(BaseValidatorModel):
    Fmtp: Optional[FmtpRequestTypeDef] = None
    Lang: Optional[str] = None

class MediaStreamAttributesTypeDef(BaseValidatorModel):
    Fmtp: FmtpTypeDef
    Lang: Optional[str] = None

class TransportStreamTypeDef(BaseValidatorModel):
    Pid: int
    StreamType: str
    Channels: Optional[int] = None
    Codec: Optional[str] = None
    FrameRate: Optional[str] = None
    FrameResolution: Optional[FrameResolutionTypeDef] = None
    SampleRate: Optional[int] = None
    SampleSize: Optional[int] = None

class ListBridgesRequestListBridgesPaginateTypeDef(BaseValidatorModel):
    FilterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntitlementsRequestListEntitlementsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowsRequestListFlowsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGatewayInstancesRequestListGatewayInstancesPaginateTypeDef(BaseValidatorModel):
    FilterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGatewaysRequestListGatewaysPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingsRequestListOfferingsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReservationsRequestListReservationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBridgesResponseTypeDef(BaseValidatorModel):
    Bridges: List[ListedBridgeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEntitlementsResponseTypeDef(BaseValidatorModel):
    Entitlements: List[ListedEntitlementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListGatewayInstancesResponseTypeDef(BaseValidatorModel):
    Instances: List[ListedGatewayInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListGatewaysResponseTypeDef(BaseValidatorModel):
    Gateways: List[ListedGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OfferingTypeDef(BaseValidatorModel):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal["HOURLY"]
    ResourceSpecification: ResourceSpecificationTypeDef

class ReservationTypeDef(BaseValidatorModel):
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

class UpdateBridgeOutputRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    OutputName: str
    NetworkOutput: Optional[UpdateBridgeNetworkOutputRequestTypeDef] = None

class UpdateFlowEntitlementRequestRequestTypeDef(BaseValidatorModel):
    EntitlementArn: str
    FlowArn: str
    Description: Optional[str] = None
    Encryption: Optional[UpdateEncryptionTypeDef] = None
    EntitlementStatus: Optional[EntitlementStatusType] = None
    Subscribers: Optional[Sequence[str]] = None

class AddBridgeSourceRequestTypeDef(BaseValidatorModel):
    FlowSource: Optional[AddBridgeFlowSourceRequestTypeDef] = None
    NetworkSource: Optional[AddBridgeNetworkSourceRequestTypeDef] = None

class BridgeSourceTypeDef(BaseValidatorModel):
    FlowSource: Optional[BridgeFlowSourceTypeDef] = None
    NetworkSource: Optional[BridgeNetworkSourceTypeDef] = None

class UpdateBridgeSourceRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    SourceName: str
    FlowSource: Optional[UpdateBridgeFlowSourceRequestTypeDef] = None
    NetworkSource: Optional[UpdateBridgeNetworkSourceRequestTypeDef] = None

class AddBridgeOutputsRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    Outputs: Sequence[AddBridgeOutputRequestTypeDef]

class GrantFlowEntitlementsResponseTypeDef(BaseValidatorModel):
    Entitlements: List[EntitlementTypeDef]
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowEntitlementResponseTypeDef(BaseValidatorModel):
    Entitlement: EntitlementTypeDef
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GrantFlowEntitlementsRequestRequestTypeDef(BaseValidatorModel):
    Entitlements: Sequence[GrantEntitlementRequestTypeDef]
    FlowArn: str

class AddBridgeOutputsResponseTypeDef(BaseValidatorModel):
    BridgeArn: str
    Outputs: List[BridgeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeOutputResponseTypeDef(BaseValidatorModel):
    BridgeArn: str
    Output: BridgeOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayInstanceResponseTypeDef(BaseValidatorModel):
    GatewayInstance: GatewayInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGatewayResponseTypeDef(BaseValidatorModel):
    Gateway: GatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayResponseTypeDef(BaseValidatorModel):
    Gateway: GatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaStreamOutputConfigurationRequestTypeDef(BaseValidatorModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    DestinationConfigurations: Optional[Sequence[DestinationConfigurationRequestTypeDef]] = None
    EncodingParameters: Optional[EncodingParametersRequestTypeDef] = None

class MediaStreamSourceConfigurationRequestTypeDef(BaseValidatorModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    InputConfigurations: Optional[Sequence[InputConfigurationRequestTypeDef]] = None

class MediaStreamOutputConfigurationTypeDef(BaseValidatorModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    DestinationConfigurations: Optional[List[DestinationConfigurationTypeDef]] = None
    EncodingParameters: Optional[EncodingParametersTypeDef] = None

class MediaStreamSourceConfigurationTypeDef(BaseValidatorModel):
    EncodingName: EncodingNameType
    MediaStreamName: str
    InputConfigurations: Optional[List[InputConfigurationTypeDef]] = None

class UpdateBridgeRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    EgressGatewayBridge: Optional[UpdateEgressGatewayBridgeRequestTypeDef] = None
    IngressGatewayBridge: Optional[UpdateIngressGatewayBridgeRequestTypeDef] = None
    SourceFailoverConfig: Optional[UpdateFailoverConfigTypeDef] = None

class UpdateFlowRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    SourceFailoverConfig: Optional[UpdateFailoverConfigTypeDef] = None
    Maintenance: Optional[UpdateMaintenanceTypeDef] = None

class ListFlowsResponseTypeDef(BaseValidatorModel):
    Flows: List[ListedFlowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AddMediaStreamRequestTypeDef(BaseValidatorModel):
    MediaStreamId: int
    MediaStreamName: str
    MediaStreamType: MediaStreamTypeType
    Attributes: Optional[MediaStreamAttributesRequestTypeDef] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    VideoFormat: Optional[str] = None

class UpdateFlowMediaStreamRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    MediaStreamName: str
    Attributes: Optional[MediaStreamAttributesRequestTypeDef] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    MediaStreamType: Optional[MediaStreamTypeType] = None
    VideoFormat: Optional[str] = None

class MediaStreamTypeDef(BaseValidatorModel):
    Fmt: int
    MediaStreamId: int
    MediaStreamName: str
    MediaStreamType: MediaStreamTypeType
    Attributes: Optional[MediaStreamAttributesTypeDef] = None
    ClockRate: Optional[int] = None
    Description: Optional[str] = None
    VideoFormat: Optional[str] = None

class TransportStreamProgramTypeDef(BaseValidatorModel):
    PcrPid: int
    ProgramNumber: int
    ProgramPid: int
    Streams: List[TransportStreamTypeDef]
    ProgramName: Optional[str] = None

class DescribeOfferingResponseTypeDef(BaseValidatorModel):
    Offering: OfferingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingsResponseTypeDef(BaseValidatorModel):
    Offerings: List[OfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservationResponseTypeDef(BaseValidatorModel):
    Reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReservationsResponseTypeDef(BaseValidatorModel):
    Reservations: List[ReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseOfferingResponseTypeDef(BaseValidatorModel):
    Reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddBridgeSourcesRequestRequestTypeDef(BaseValidatorModel):
    BridgeArn: str
    Sources: Sequence[AddBridgeSourceRequestTypeDef]

class CreateBridgeRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    PlacementArn: str
    Sources: Sequence[AddBridgeSourceRequestTypeDef]
    EgressGatewayBridge: Optional[AddEgressGatewayBridgeRequestTypeDef] = None
    IngressGatewayBridge: Optional[AddIngressGatewayBridgeRequestTypeDef] = None
    Outputs: Optional[Sequence[AddBridgeOutputRequestTypeDef]] = None
    SourceFailoverConfig: Optional[FailoverConfigTypeDef] = None

class AddBridgeSourcesResponseTypeDef(BaseValidatorModel):
    BridgeArn: str
    Sources: List[BridgeSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BridgeTypeDef(BaseValidatorModel):
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

class UpdateBridgeSourceResponseTypeDef(BaseValidatorModel):
    BridgeArn: str
    Source: BridgeSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddOutputRequestTypeDef(BaseValidatorModel):
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

class UpdateFlowOutputRequestRequestTypeDef(BaseValidatorModel):
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

class SetSourceRequestTypeDef(BaseValidatorModel):
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

class UpdateFlowSourceRequestRequestTypeDef(BaseValidatorModel):
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

class OutputTypeDef(BaseValidatorModel):
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

class SourceTypeDef(BaseValidatorModel):
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

class AddFlowMediaStreamsRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    MediaStreams: Sequence[AddMediaStreamRequestTypeDef]

class AddFlowMediaStreamsResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    MediaStreams: List[MediaStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowMediaStreamResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    MediaStream: MediaStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransportMediaInfoTypeDef(BaseValidatorModel):
    Programs: List[TransportStreamProgramTypeDef]

class CreateBridgeResponseTypeDef(BaseValidatorModel):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBridgeResponseTypeDef(BaseValidatorModel):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeResponseTypeDef(BaseValidatorModel):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowOutputsRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    Outputs: Sequence[AddOutputRequestTypeDef]

class AddFlowSourcesRequestRequestTypeDef(BaseValidatorModel):
    FlowArn: str
    Sources: Sequence[SetSourceRequestTypeDef]

class CreateFlowRequestRequestTypeDef(BaseValidatorModel):
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

class AddFlowOutputsResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    Outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowOutputResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    Output: OutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowSourcesResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    Sources: List[SourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FlowTypeDef(BaseValidatorModel):
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

class UpdateFlowSourceResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    Source: SourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlowSourceMetadataResponseTypeDef(BaseValidatorModel):
    FlowArn: str
    Messages: List[MessageDetailTypeDef]
    Timestamp: datetime
    TransportMediaInfo: TransportMediaInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowResponseTypeDef(BaseValidatorModel):
    Flow: FlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlowResponseTypeDef(BaseValidatorModel):
    Flow: FlowTypeDef
    Messages: MessagesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowResponseTypeDef(BaseValidatorModel):
    Flow: FlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


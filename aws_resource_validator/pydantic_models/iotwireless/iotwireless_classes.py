from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iotwireless.iotwireless_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class SessionKeysAbpV10X(BaseValidatorModel):
    NwkSKey: Optional[str] = None
    AppSKey: Optional[str] = None


class SessionKeysAbpV11(BaseValidatorModel):
    FNwkSIntKey: Optional[str] = None
    SNwkSIntKey: Optional[str] = None
    NwkSEncKey: Optional[str] = None
    AppSKey: Optional[str] = None


class Accuracy(BaseValidatorModel):
    HorizontalAccuracy: Optional[float] = None
    VerticalAccuracy: Optional[float] = None


class ApplicationConfig(BaseValidatorModel):
    FPort: Optional[int] = None
    Type: Optional[Literal['SemtechGeolocation']] = None
    DestinationName: Optional[str] = None


class SidewalkAccountInfo(BaseValidatorModel):
    AmazonId: Optional[str] = None
    AppServerPrivateKey: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateMulticastGroupWithFuotaTaskRequest(BaseValidatorModel):
    Id: str
    MulticastGroupId: str


class AssociateWirelessDeviceWithFuotaTaskRequest(BaseValidatorModel):
    Id: str
    WirelessDeviceId: str


class AssociateWirelessDeviceWithMulticastGroupRequest(BaseValidatorModel):
    Id: str
    WirelessDeviceId: str


class AssociateWirelessDeviceWithThingRequest(BaseValidatorModel):
    Id: str
    ThingArn: str


class AssociateWirelessGatewayWithCertificateRequest(BaseValidatorModel):
    Id: str
    IotCertificateId: str


class AssociateWirelessGatewayWithThingRequest(BaseValidatorModel):
    Id: str
    ThingArn: str


class BeaconingOutput(BaseValidatorModel):
    DataRate: Optional[int] = None
    Frequencies: Optional[List[int]] = None


class Beaconing(BaseValidatorModel):
    DataRate: Optional[int] = None
    Frequencies: Optional[List[int]] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelMulticastGroupSessionRequest(BaseValidatorModel):
    Id: str


class CdmaLocalId(BaseValidatorModel):
    PnOffset: int
    CdmaChannel: int


class CdmaNmrObj(BaseValidatorModel):
    PnOffset: int
    CdmaChannel: int
    PilotPower: Optional[int] = None
    BaseStationId: Optional[int] = None


class CertificateList(BaseValidatorModel):
    SigningAlg: SigningAlgType
    Value: str


class LoRaWANConnectionStatusEventNotificationConfigurations(BaseValidatorModel):
    GatewayEuiEventTopic: Optional[EventNotificationTopicStatusType] = None


class LoRaWANConnectionStatusResourceTypeEventConfiguration(BaseValidatorModel):
    WirelessGatewayEventTopic: Optional[EventNotificationTopicStatusType] = None


class LoRaWANFuotaTask(BaseValidatorModel):
    RfRegion: Optional[SupportedRfRegionType] = None


class TraceContent(BaseValidatorModel):
    WirelessDeviceFrameInfo: Optional[WirelessDeviceFrameInfoType] = None
    LogLevel: Optional[LogLevelType] = None
    MulticastFrameInfo: Optional[MulticastFrameInfoType] = None


class LoRaWANServiceProfile(BaseValidatorModel):
    AddGwMetadata: Optional[bool] = None
    DrMin: Optional[int] = None
    DrMax: Optional[int] = None
    PrAllowed: Optional[bool] = None
    RaAllowed: Optional[bool] = None


class SidewalkCreateWirelessDevice(BaseValidatorModel):
    DeviceProfileId: Optional[str] = None


class CreateWirelessGatewayTaskRequest(BaseValidatorModel):
    Id: str
    WirelessGatewayTaskDefinitionId: str


class DakCertificateMetadata(BaseValidatorModel):
    CertificateId: str
    MaxAllowedSignature: Optional[int] = None
    FactorySupport: Optional[bool] = None
    ApId: Optional[str] = None
    DeviceTypeId: Optional[str] = None


class DeleteDestinationRequest(BaseValidatorModel):
    Name: str


class DeleteDeviceProfileRequest(BaseValidatorModel):
    Id: str


class DeleteFuotaTaskRequest(BaseValidatorModel):
    Id: str


class DeleteMulticastGroupRequest(BaseValidatorModel):
    Id: str


class DeleteNetworkAnalyzerConfigurationRequest(BaseValidatorModel):
    ConfigurationName: str


class DeleteQueuedMessagesRequest(BaseValidatorModel):
    Id: str
    MessageId: str
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None


class DeleteServiceProfileRequest(BaseValidatorModel):
    Id: str


class DeleteWirelessDeviceImportTaskRequest(BaseValidatorModel):
    Id: str


class DeleteWirelessDeviceRequest(BaseValidatorModel):
    Id: str


class DeleteWirelessGatewayRequest(BaseValidatorModel):
    Id: str


class DeleteWirelessGatewayTaskDefinitionRequest(BaseValidatorModel):
    Id: str


class DeleteWirelessGatewayTaskRequest(BaseValidatorModel):
    Id: str


class DeregisterWirelessDeviceRequest(BaseValidatorModel):
    Identifier: str
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None


class Destinations(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ExpressionType: Optional[ExpressionTypeType] = None
    Expression: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None


class DeviceProfile(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Id: Optional[str] = None


class SidewalkEventNotificationConfigurations(BaseValidatorModel):
    AmazonIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class SidewalkResourceTypeEventConfiguration(BaseValidatorModel):
    WirelessDeviceEventTopic: Optional[EventNotificationTopicStatusType] = None


class Dimension(BaseValidatorModel):
    name: Optional[DimensionNameType] = None
    value: Optional[str] = None


class DisassociateAwsAccountFromPartnerAccountRequest(BaseValidatorModel):
    PartnerAccountId: str
    PartnerType: Literal['Sidewalk']


class DisassociateMulticastGroupFromFuotaTaskRequest(BaseValidatorModel):
    Id: str
    MulticastGroupId: str


class DisassociateWirelessDeviceFromFuotaTaskRequest(BaseValidatorModel):
    Id: str
    WirelessDeviceId: str


class DisassociateWirelessDeviceFromMulticastGroupRequest(BaseValidatorModel):
    Id: str
    WirelessDeviceId: str


class DisassociateWirelessDeviceFromThingRequest(BaseValidatorModel):
    Id: str


class DisassociateWirelessGatewayFromCertificateRequest(BaseValidatorModel):
    Id: str


class DisassociateWirelessGatewayFromThingRequest(BaseValidatorModel):
    Id: str


class Positioning(BaseValidatorModel):
    ClockSync: Optional[int] = None
    Stream: Optional[int] = None
    Gnss: Optional[int] = None


class FuotaTaskEventLogOption(BaseValidatorModel):
    Event: Literal['Fuota']
    LogLevel: LogLevelType


class FuotaTask(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None


class GatewayListItem(BaseValidatorModel):
    GatewayId: str
    DownlinkFrequency: int


class GetDestinationRequest(BaseValidatorModel):
    Name: str


class GetDeviceProfileRequest(BaseValidatorModel):
    Id: str


class LoRaWANDeviceProfileOutput(BaseValidatorModel):
    SupportsClassB: Optional[bool] = None
    ClassBTimeout: Optional[int] = None
    PingSlotPeriod: Optional[int] = None
    PingSlotDr: Optional[int] = None
    PingSlotFreq: Optional[int] = None
    SupportsClassC: Optional[bool] = None
    ClassCTimeout: Optional[int] = None
    MacVersion: Optional[str] = None
    RegParamsRevision: Optional[str] = None
    RxDelay1: Optional[int] = None
    RxDrOffset1: Optional[int] = None
    RxDataRate2: Optional[int] = None
    RxFreq2: Optional[int] = None
    FactoryPresetFreqsList: Optional[List[int]] = None
    MaxEirp: Optional[int] = None
    MaxDutyCycle: Optional[int] = None
    RfRegion: Optional[str] = None
    SupportsJoin: Optional[bool] = None
    Supports32BitFCnt: Optional[bool] = None


class GetFuotaTaskRequest(BaseValidatorModel):
    Id: str


class LoRaWANFuotaTaskGetInfo(BaseValidatorModel):
    RfRegion: Optional[str] = None
    StartTime: Optional[datetime] = None


class SummaryMetricConfiguration(BaseValidatorModel):
    Status: Optional[SummaryMetricConfigurationStatusType] = None


class GetMulticastGroupRequest(BaseValidatorModel):
    Id: str


class GetMulticastGroupSessionRequest(BaseValidatorModel):
    Id: str


class LoRaWANMulticastSessionOutput(BaseValidatorModel):
    DlDr: Optional[int] = None
    DlFreq: Optional[int] = None
    SessionStartTime: Optional[datetime] = None
    SessionTimeout: Optional[int] = None
    PingSlotPeriod: Optional[int] = None


class GetNetworkAnalyzerConfigurationRequest(BaseValidatorModel):
    ConfigurationName: str


class GetPartnerAccountRequest(BaseValidatorModel):
    PartnerAccountId: str
    PartnerType: Literal['Sidewalk']


class SidewalkAccountInfoWithFingerprint(BaseValidatorModel):
    AmazonId: Optional[str] = None
    Fingerprint: Optional[str] = None
    Arn: Optional[str] = None


class GetPositionConfigurationRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType


class Gnss(BaseValidatorModel):
    Payload: str
    CaptureTime: Optional[float] = None
    CaptureTimeAccuracy: Optional[float] = None
    AssistPosition: Optional[List[float]] = None
    AssistAltitude: Optional[float] = None
    Use2DSolver: Optional[bool] = None


class Ip(BaseValidatorModel):
    IpAddress: str

Timestamp = Union[datetime, str]


class WiFiAccessPoint(BaseValidatorModel):
    MacAddress: str
    Rss: int


class GetPositionRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType


class GetResourceEventConfigurationRequest(BaseValidatorModel):
    Identifier: str
    IdentifierType: IdentifierTypeType
    PartnerType: Optional[Literal['Sidewalk']] = None


class GetResourceLogLevelRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: str


class GetResourcePositionRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType


class GetServiceEndpointRequest(BaseValidatorModel):
    ServiceType: Optional[WirelessGatewayServiceTypeType] = None


class GetServiceProfileRequest(BaseValidatorModel):
    Id: str


class LoRaWANGetServiceProfileInfo(BaseValidatorModel):
    UlRate: Optional[int] = None
    UlBucketSize: Optional[int] = None
    UlRatePolicy: Optional[str] = None
    DlRate: Optional[int] = None
    DlBucketSize: Optional[int] = None
    DlRatePolicy: Optional[str] = None
    AddGwMetadata: Optional[bool] = None
    DevStatusReqFreq: Optional[int] = None
    ReportDevStatusBattery: Optional[bool] = None
    ReportDevStatusMargin: Optional[bool] = None
    DrMin: Optional[int] = None
    DrMax: Optional[int] = None
    ChannelMask: Optional[str] = None
    PrAllowed: Optional[bool] = None
    HrAllowed: Optional[bool] = None
    RaAllowed: Optional[bool] = None
    NwkGeoLoc: Optional[bool] = None
    TargetPer: Optional[int] = None
    MinGwDiversity: Optional[int] = None


class GetWirelessDeviceImportTaskRequest(BaseValidatorModel):
    Id: str


class SidewalkGetStartImportInfo(BaseValidatorModel):
    DeviceCreationFileList: Optional[List[str]] = None
    Role: Optional[str] = None


class GetWirelessDeviceRequest(BaseValidatorModel):
    Identifier: str
    IdentifierType: WirelessDeviceIdTypeType


class GetWirelessDeviceStatisticsRequest(BaseValidatorModel):
    WirelessDeviceId: str


class SidewalkDeviceMetadata(BaseValidatorModel):
    Rssi: Optional[int] = None
    BatteryLevel: Optional[BatteryLevelType] = None
    Event: Optional[EventType] = None
    DeviceState: Optional[DeviceStateType] = None


class GetWirelessGatewayCertificateRequest(BaseValidatorModel):
    Id: str


class GetWirelessGatewayFirmwareInformationRequest(BaseValidatorModel):
    Id: str


class GetWirelessGatewayRequest(BaseValidatorModel):
    Identifier: str
    IdentifierType: WirelessGatewayIdTypeType


class GetWirelessGatewayStatisticsRequest(BaseValidatorModel):
    WirelessGatewayId: str


class GetWirelessGatewayTaskDefinitionRequest(BaseValidatorModel):
    Id: str


class GetWirelessGatewayTaskRequest(BaseValidatorModel):
    Id: str


class GlobalIdentity(BaseValidatorModel):
    Lac: int
    GeranCid: int


class GsmLocalId(BaseValidatorModel):
    Bsic: int
    Bcch: int


class ImportedSidewalkDevice(BaseValidatorModel):
    SidewalkManufacturingSn: Optional[str] = None
    OnboardingStatus: Optional[OnboardStatusType] = None
    OnboardingStatusReason: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None


class LoRaWANJoinEventNotificationConfigurations(BaseValidatorModel):
    DevEuiEventTopic: Optional[EventNotificationTopicStatusType] = None


class LoRaWANJoinResourceTypeEventConfiguration(BaseValidatorModel):
    WirelessDeviceEventTopic: Optional[EventNotificationTopicStatusType] = None


class ListDestinationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDeviceProfilesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DeviceProfileType: Optional[DeviceProfileTypeType] = None


class ListDevicesForWirelessDeviceImportTaskRequest(BaseValidatorModel):
    Id: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[OnboardStatusType] = None


class ListEventConfigurationsRequest(BaseValidatorModel):
    ResourceType: EventNotificationResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFuotaTasksRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMulticastGroupsByFuotaTaskRequest(BaseValidatorModel):
    Id: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MulticastGroupByFuotaTask(BaseValidatorModel):
    Id: Optional[str] = None


class ListMulticastGroupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MulticastGroup(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None


class ListNetworkAnalyzerConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NetworkAnalyzerConfigurations(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class ListPartnerAccountsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPositionConfigurationsRequest(BaseValidatorModel):
    ResourceType: Optional[PositionResourceTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListQueuedMessagesRequest(BaseValidatorModel):
    Id: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None


class ListServiceProfilesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ServiceProfile(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Id: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListWirelessDeviceImportTasksRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListWirelessDevicesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DestinationName: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None
    FuotaTaskId: Optional[str] = None
    MulticastGroupId: Optional[str] = None


class ListWirelessGatewayTaskDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    TaskDefinitionType: Optional[Literal['UPDATE']] = None


class ListWirelessGatewaysRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class LoRaWANGatewayMetadata(BaseValidatorModel):
    GatewayEui: Optional[str] = None
    Snr: Optional[float] = None
    Rssi: Optional[float] = None


class LoRaWANPublicGatewayMetadata(BaseValidatorModel):
    ProviderNetId: Optional[str] = None
    Id: Optional[str] = None
    Rssi: Optional[float] = None
    Snr: Optional[float] = None
    RfRegion: Optional[str] = None
    DlAllowed: Optional[bool] = None


class OtaaV10X(BaseValidatorModel):
    AppKey: Optional[str] = None
    AppEui: Optional[str] = None
    JoinEui: Optional[str] = None
    GenAppKey: Optional[str] = None


class OtaaV11(BaseValidatorModel):
    AppKey: Optional[str] = None
    NwkKey: Optional[str] = None
    JoinEui: Optional[str] = None


class LoRaWANDeviceProfile(BaseValidatorModel):
    SupportsClassB: Optional[bool] = None
    ClassBTimeout: Optional[int] = None
    PingSlotPeriod: Optional[int] = None
    PingSlotDr: Optional[int] = None
    PingSlotFreq: Optional[int] = None
    SupportsClassC: Optional[bool] = None
    ClassCTimeout: Optional[int] = None
    MacVersion: Optional[str] = None
    RegParamsRevision: Optional[str] = None
    RxDelay1: Optional[int] = None
    RxDrOffset1: Optional[int] = None
    RxDataRate2: Optional[int] = None
    RxFreq2: Optional[int] = None
    FactoryPresetFreqsList: Optional[List[int]] = None
    MaxEirp: Optional[int] = None
    MaxDutyCycle: Optional[int] = None
    RfRegion: Optional[str] = None
    SupportsJoin: Optional[bool] = None
    Supports32BitFCnt: Optional[bool] = None


class LoRaWANGatewayVersion(BaseValidatorModel):
    PackageVersion: Optional[str] = None
    Model: Optional[str] = None
    Station: Optional[str] = None


class LoRaWANListDevice(BaseValidatorModel):
    DevEui: Optional[str] = None


class ParticipatingGatewaysMulticastOutput(BaseValidatorModel):
    GatewayList: Optional[List[str]] = None
    TransmissionInterval: Optional[int] = None


class LoRaWANMulticastMetadata(BaseValidatorModel):
    FPort: Optional[int] = None


class UpdateAbpV10X(BaseValidatorModel):
    FCntStart: Optional[int] = None


class UpdateAbpV11(BaseValidatorModel):
    FCntStart: Optional[int] = None


class LteLocalId(BaseValidatorModel):
    Pci: int
    Earfcn: int


class LteNmrObj(BaseValidatorModel):
    Pci: int
    Earfcn: int
    EutranCid: int
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None


class MetricQueryValue(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None
    Sum: Optional[float] = None
    Avg: Optional[float] = None
    Std: Optional[float] = None
    P90: Optional[float] = None


class ParticipatingGatewaysMulticast(BaseValidatorModel):
    GatewayList: Optional[List[str]] = None
    TransmissionInterval: Optional[int] = None


class SemtechGnssConfiguration(BaseValidatorModel):
    Status: PositionConfigurationStatusType
    Fec: PositionConfigurationFecType


class SemtechGnssDetail(BaseValidatorModel):
    Provider: Optional[Literal['Semtech']] = None
    Type: Optional[Literal['GNSS']] = None
    Status: Optional[PositionConfigurationStatusType] = None
    Fec: Optional[PositionConfigurationFecType] = None


class PutResourceLogLevelRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: str
    LogLevel: LogLevelType


class ResetResourceLogLevelRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: str


class SidewalkSendDataToDevice(BaseValidatorModel):
    Seq: Optional[int] = None
    MessageType: Optional[MessageTypeType] = None
    AckModeRetryDurationSecs: Optional[int] = None


class SidewalkSingleStartImportInfo(BaseValidatorModel):
    SidewalkManufacturingSn: Optional[str] = None


class SidewalkStartImportInfo(BaseValidatorModel):
    DeviceCreationFile: Optional[str] = None
    Role: Optional[str] = None


class SidewalkUpdateAccount(BaseValidatorModel):
    AppServerPrivateKey: Optional[str] = None


class SidewalkUpdateImportInfo(BaseValidatorModel):
    DeviceCreationFile: Optional[str] = None


class TdscdmaLocalId(BaseValidatorModel):
    Uarfcn: int
    CellParams: int


class TdscdmaNmrObj(BaseValidatorModel):
    Uarfcn: int
    CellParams: int
    UtranCid: Optional[int] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None


class TestWirelessDeviceRequest(BaseValidatorModel):
    Id: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateDestinationRequest(BaseValidatorModel):
    Name: str
    ExpressionType: Optional[ExpressionTypeType] = None
    Expression: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None


class UpdatePositionRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    Position: List[float]


class UpdateWirelessGatewayRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    JoinEuiFilters: Optional[List[List[str]]] = None
    NetIdFilters: Optional[List[str]] = None
    MaxEirp: Optional[float] = None


class WcdmaLocalId(BaseValidatorModel):
    Uarfcndl: int
    Psc: int


class WcdmaNmrObj(BaseValidatorModel):
    Uarfcndl: int
    Psc: int
    UtranCid: int
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None


class WirelessDeviceEventLogOption(BaseValidatorModel):
    Event: WirelessDeviceEventType
    LogLevel: LogLevelType


class WirelessGatewayEventLogOption(BaseValidatorModel):
    Event: WirelessGatewayEventType
    LogLevel: LogLevelType


class AbpV10X(BaseValidatorModel):
    DevAddr: Optional[str] = None
    SessionKeys: Optional[SessionKeysAbpV10X] = None
    FCntStart: Optional[int] = None


class AbpV11(BaseValidatorModel):
    DevAddr: Optional[str] = None
    SessionKeys: Optional[SessionKeysAbpV11] = None
    FCntStart: Optional[int] = None


class AssociateAwsAccountWithPartnerAccountRequest(BaseValidatorModel):
    Sidewalk: SidewalkAccountInfo
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateDestinationRequest(BaseValidatorModel):
    Name: str
    ExpressionType: ExpressionTypeType
    Expression: str
    RoleArn: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientRequestToken: Optional[str] = None


class StartBulkAssociateWirelessDeviceWithMulticastGroupRequest(BaseValidatorModel):
    Id: str
    QueryString: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest(BaseValidatorModel):
    Id: str
    QueryString: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class AssociateAwsAccountWithPartnerAccountResponse(BaseValidatorModel):
    Sidewalk: SidewalkAccountInfo
    Arn: str
    ResponseMetadata: ResponseMetadata


class AssociateWirelessGatewayWithCertificateResponse(BaseValidatorModel):
    IotCertificateId: str
    ResponseMetadata: ResponseMetadata


class CreateDestinationResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateDeviceProfileResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateFuotaTaskResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateMulticastGroupResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateNetworkAnalyzerConfigurationResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateServiceProfileResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateWirelessDeviceResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateWirelessGatewayResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateWirelessGatewayTaskDefinitionResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateWirelessGatewayTaskResponse(BaseValidatorModel):
    WirelessGatewayTaskDefinitionId: str
    Status: WirelessGatewayTaskStatusType
    ResponseMetadata: ResponseMetadata


class GetDestinationResponse(BaseValidatorModel):
    Arn: str
    Name: str
    Expression: str
    ExpressionType: ExpressionTypeType
    Description: str
    RoleArn: str
    ResponseMetadata: ResponseMetadata


class GetPositionEstimateResponse(BaseValidatorModel):
    GeoJsonPayload: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetPositionResponse(BaseValidatorModel):
    Position: List[float]
    Accuracy: Accuracy
    SolverType: Literal['GNSS']
    SolverProvider: Literal['Semtech']
    SolverVersion: str
    Timestamp: str
    ResponseMetadata: ResponseMetadata


class GetResourceLogLevelResponse(BaseValidatorModel):
    LogLevel: LogLevelType
    ResponseMetadata: ResponseMetadata


class GetResourcePositionResponse(BaseValidatorModel):
    GeoJsonPayload: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetServiceEndpointResponse(BaseValidatorModel):
    ServiceType: WirelessGatewayServiceTypeType
    ServiceEndpoint: str
    ServerTrust: str
    ResponseMetadata: ResponseMetadata


class GetWirelessGatewayCertificateResponse(BaseValidatorModel):
    IotCertificateId: str
    LoRaWANNetworkServerCertificateId: str
    ResponseMetadata: ResponseMetadata


class GetWirelessGatewayStatisticsResponse(BaseValidatorModel):
    WirelessGatewayId: str
    LastUplinkReceivedAt: str
    ConnectionStatus: ConnectionStatusType
    ResponseMetadata: ResponseMetadata


class GetWirelessGatewayTaskResponse(BaseValidatorModel):
    WirelessGatewayId: str
    WirelessGatewayTaskDefinitionId: str
    LastUplinkReceivedAt: str
    TaskCreatedAt: str
    Status: WirelessGatewayTaskStatusType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class SendDataToMulticastGroupResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendDataToWirelessDeviceResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class StartSingleWirelessDeviceImportTaskResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class StartWirelessDeviceImportTaskResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class TestWirelessDeviceResponse(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadata


class LoRaWANGatewayOutput(BaseValidatorModel):
    GatewayEui: Optional[str] = None
    RfRegion: Optional[str] = None
    JoinEuiFilters: Optional[List[List[str]]] = None
    NetIdFilters: Optional[List[str]] = None
    SubBands: Optional[List[int]] = None
    Beaconing: Optional[BeaconingOutput] = None
    MaxEirp: Optional[float] = None


class LoRaWANGateway(BaseValidatorModel):
    GatewayEui: Optional[str] = None
    RfRegion: Optional[str] = None
    JoinEuiFilters: Optional[List[List[str]]] = None
    NetIdFilters: Optional[List[str]] = None
    SubBands: Optional[List[int]] = None
    Beaconing: Optional[Beaconing] = None
    MaxEirp: Optional[float] = None


class UpdateResourcePositionRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    GeoJsonPayload: Optional[Blob] = None


class CdmaObj(BaseValidatorModel):
    SystemId: int
    NetworkId: int
    BaseStationId: int
    RegistrationZone: Optional[int] = None
    CdmaLocalId: Optional[CdmaLocalId] = None
    PilotPower: Optional[int] = None
    BaseLat: Optional[float] = None
    BaseLng: Optional[float] = None
    CdmaNmr: Optional[List[CdmaNmrObj]] = None


class SidewalkDevice(BaseValidatorModel):
    AmazonId: Optional[str] = None
    SidewalkId: Optional[str] = None
    SidewalkManufacturingSn: Optional[str] = None
    DeviceCertificates: Optional[List[CertificateList]] = None
    PrivateKeys: Optional[List[CertificateList]] = None
    DeviceProfileId: Optional[str] = None
    CertificateId: Optional[str] = None
    Status: Optional[WirelessDeviceSidewalkStatusType] = None


class SidewalkListDevice(BaseValidatorModel):
    AmazonId: Optional[str] = None
    SidewalkId: Optional[str] = None
    SidewalkManufacturingSn: Optional[str] = None
    DeviceCertificates: Optional[List[CertificateList]] = None
    DeviceProfileId: Optional[str] = None
    Status: Optional[WirelessDeviceSidewalkStatusType] = None


class ConnectionStatusEventConfiguration(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANConnectionStatusEventNotificationConfigurations] = None
    WirelessGatewayIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class ConnectionStatusResourceTypeEventConfiguration(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANConnectionStatusResourceTypeEventConfiguration] = None


class CreateFuotaTaskRequest(BaseValidatorModel):
    FirmwareUpdateImage: str
    FirmwareUpdateRole: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    LoRaWAN: Optional[LoRaWANFuotaTask] = None
    Tags: Optional[List[Tag]] = None
    RedundancyPercent: Optional[int] = None
    FragmentSizeBytes: Optional[int] = None
    FragmentIntervalMS: Optional[int] = None
    Descriptor: Optional[str] = None


class UpdateFuotaTaskRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANFuotaTask] = None
    FirmwareUpdateImage: Optional[str] = None
    FirmwareUpdateRole: Optional[str] = None
    RedundancyPercent: Optional[int] = None
    FragmentSizeBytes: Optional[int] = None
    FragmentIntervalMS: Optional[int] = None
    Descriptor: Optional[str] = None


class CreateNetworkAnalyzerConfigurationRequest(BaseValidatorModel):
    Name: str
    TraceContent: Optional[TraceContent] = None
    WirelessDevices: Optional[List[str]] = None
    WirelessGateways: Optional[List[str]] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientRequestToken: Optional[str] = None
    MulticastGroups: Optional[List[str]] = None


class GetNetworkAnalyzerConfigurationResponse(BaseValidatorModel):
    TraceContent: TraceContent
    WirelessDevices: List[str]
    WirelessGateways: List[str]
    Description: str
    Arn: str
    Name: str
    MulticastGroups: List[str]
    ResponseMetadata: ResponseMetadata


class UpdateNetworkAnalyzerConfigurationRequest(BaseValidatorModel):
    ConfigurationName: str
    TraceContent: Optional[TraceContent] = None
    WirelessDevicesToAdd: Optional[List[str]] = None
    WirelessDevicesToRemove: Optional[List[str]] = None
    WirelessGatewaysToAdd: Optional[List[str]] = None
    WirelessGatewaysToRemove: Optional[List[str]] = None
    Description: Optional[str] = None
    MulticastGroupsToAdd: Optional[List[str]] = None
    MulticastGroupsToRemove: Optional[List[str]] = None


class CreateServiceProfileRequest(BaseValidatorModel):
    Name: Optional[str] = None
    LoRaWAN: Optional[LoRaWANServiceProfile] = None
    Tags: Optional[List[Tag]] = None
    ClientRequestToken: Optional[str] = None


class SidewalkGetDeviceProfile(BaseValidatorModel):
    ApplicationServerPublicKey: Optional[str] = None
    QualificationStatus: Optional[bool] = None
    DakCertificateMetadata: Optional[List[DakCertificateMetadata]] = None


class ListDestinationsResponse(BaseValidatorModel):
    DestinationList: List[Destinations]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDeviceProfilesResponse(BaseValidatorModel):
    DeviceProfileList: List[DeviceProfile]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DeviceRegistrationStateEventConfiguration(BaseValidatorModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurations] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class MessageDeliveryStatusEventConfiguration(BaseValidatorModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurations] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class ProximityEventConfiguration(BaseValidatorModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurations] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class DeviceRegistrationStateResourceTypeEventConfiguration(BaseValidatorModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfiguration] = None


class MessageDeliveryStatusResourceTypeEventConfiguration(BaseValidatorModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfiguration] = None


class ProximityResourceTypeEventConfiguration(BaseValidatorModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfiguration] = None


class FPortsOutput(BaseValidatorModel):
    Fuota: Optional[int] = None
    Multicast: Optional[int] = None
    ClockSync: Optional[int] = None
    Positioning: Optional[Positioning] = None
    Applications: Optional[List[ApplicationConfig]] = None


class FPorts(BaseValidatorModel):
    Fuota: Optional[int] = None
    Multicast: Optional[int] = None
    ClockSync: Optional[int] = None
    Positioning: Optional[Positioning] = None
    Applications: Optional[List[ApplicationConfig]] = None


class UpdateFPorts(BaseValidatorModel):
    Positioning: Optional[Positioning] = None
    Applications: Optional[List[ApplicationConfig]] = None


class FuotaTaskLogOptionOutput(BaseValidatorModel):
    Type: Literal['LoRaWAN']
    LogLevel: LogLevelType
    Events: Optional[List[FuotaTaskEventLogOption]] = None


class FuotaTaskLogOption(BaseValidatorModel):
    Type: Literal['LoRaWAN']
    LogLevel: LogLevelType
    Events: Optional[List[FuotaTaskEventLogOption]] = None


class ListFuotaTasksResponse(BaseValidatorModel):
    FuotaTaskList: List[FuotaTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ParticipatingGatewaysOutput(BaseValidatorModel):
    DownlinkMode: DownlinkModeType
    GatewayList: List[GatewayListItem]
    TransmissionInterval: int


class ParticipatingGateways(BaseValidatorModel):
    DownlinkMode: DownlinkModeType
    GatewayList: List[GatewayListItem]
    TransmissionInterval: int


class GetFuotaTaskResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Status: FuotaTaskStatusType
    Name: str
    Description: str
    LoRaWAN: LoRaWANFuotaTaskGetInfo
    FirmwareUpdateImage: str
    FirmwareUpdateRole: str
    CreatedAt: datetime
    RedundancyPercent: int
    FragmentSizeBytes: int
    FragmentIntervalMS: int
    Descriptor: str
    ResponseMetadata: ResponseMetadata


class GetMetricConfigurationResponse(BaseValidatorModel):
    SummaryMetric: SummaryMetricConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateMetricConfigurationRequest(BaseValidatorModel):
    SummaryMetric: Optional[SummaryMetricConfiguration] = None


class GetMulticastGroupSessionResponse(BaseValidatorModel):
    LoRaWAN: LoRaWANMulticastSessionOutput
    ResponseMetadata: ResponseMetadata


class GetPartnerAccountResponse(BaseValidatorModel):
    Sidewalk: SidewalkAccountInfoWithFingerprint
    AccountLinked: bool
    ResponseMetadata: ResponseMetadata


class ListPartnerAccountsResponse(BaseValidatorModel):
    Sidewalk: List[SidewalkAccountInfoWithFingerprint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LoRaWANMulticastSession(BaseValidatorModel):
    DlDr: Optional[int] = None
    DlFreq: Optional[int] = None
    SessionStartTime: Optional[Timestamp] = None
    SessionTimeout: Optional[int] = None
    PingSlotPeriod: Optional[int] = None


class LoRaWANStartFuotaTask(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None


class SummaryMetricQuery(BaseValidatorModel):
    QueryId: Optional[str] = None
    MetricName: Optional[MetricNameType] = None
    Dimensions: Optional[List[Dimension]] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    StartTimestamp: Optional[Timestamp] = None
    EndTimestamp: Optional[Timestamp] = None


class GetServiceProfileResponse(BaseValidatorModel):
    Arn: str
    Name: str
    Id: str
    LoRaWAN: LoRaWANGetServiceProfileInfo
    ResponseMetadata: ResponseMetadata


class GetWirelessDeviceImportTaskResponse(BaseValidatorModel):
    Id: str
    Arn: str
    DestinationName: str
    Sidewalk: SidewalkGetStartImportInfo
    CreationTime: datetime
    Status: ImportTaskStatusType
    StatusReason: str
    InitializedImportedDeviceCount: int
    PendingImportedDeviceCount: int
    OnboardedImportedDeviceCount: int
    FailedImportedDeviceCount: int
    ResponseMetadata: ResponseMetadata


class WirelessDeviceImportTask(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    DestinationName: Optional[str] = None
    Sidewalk: Optional[SidewalkGetStartImportInfo] = None
    CreationTime: Optional[datetime] = None
    Status: Optional[ImportTaskStatusType] = None
    StatusReason: Optional[str] = None
    InitializedImportedDeviceCount: Optional[int] = None
    PendingImportedDeviceCount: Optional[int] = None
    OnboardedImportedDeviceCount: Optional[int] = None
    FailedImportedDeviceCount: Optional[int] = None


class GsmNmrObj(BaseValidatorModel):
    Bsic: int
    Bcch: int
    RxLevel: Optional[int] = None
    GlobalIdentity: Optional[GlobalIdentity] = None


class ImportedWirelessDevice(BaseValidatorModel):
    Sidewalk: Optional[ImportedSidewalkDevice] = None


class JoinEventConfiguration(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANJoinEventNotificationConfigurations] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class JoinResourceTypeEventConfiguration(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANJoinResourceTypeEventConfiguration] = None


class ListMulticastGroupsByFuotaTaskResponse(BaseValidatorModel):
    MulticastGroupList: List[MulticastGroupByFuotaTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMulticastGroupsResponse(BaseValidatorModel):
    MulticastGroupList: List[MulticastGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNetworkAnalyzerConfigurationsResponse(BaseValidatorModel):
    NetworkAnalyzerConfigurationList: List[NetworkAnalyzerConfigurations]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServiceProfilesResponse(BaseValidatorModel):
    ServiceProfileList: List[ServiceProfile]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LoRaWANDeviceMetadata(BaseValidatorModel):
    DevEui: Optional[str] = None
    FPort: Optional[int] = None
    DataRate: Optional[int] = None
    Frequency: Optional[int] = None
    Timestamp: Optional[str] = None
    Gateways: Optional[List[LoRaWANGatewayMetadata]] = None
    PublicGateways: Optional[List[LoRaWANPublicGatewayMetadata]] = None

LoRaWANDeviceProfileUnion = Union[LoRaWANDeviceProfile, LoRaWANDeviceProfileOutput]


class LoRaWANGatewayCurrentVersion(BaseValidatorModel):
    CurrentVersion: Optional[LoRaWANGatewayVersion] = None


class LoRaWANUpdateGatewayTaskCreate(BaseValidatorModel):
    UpdateSignature: Optional[str] = None
    SigKeyCrc: Optional[int] = None
    CurrentVersion: Optional[LoRaWANGatewayVersion] = None
    UpdateVersion: Optional[LoRaWANGatewayVersion] = None


class LoRaWANUpdateGatewayTaskEntry(BaseValidatorModel):
    CurrentVersion: Optional[LoRaWANGatewayVersion] = None
    UpdateVersion: Optional[LoRaWANGatewayVersion] = None


class LoRaWANMulticastGet(BaseValidatorModel):
    RfRegion: Optional[SupportedRfRegionType] = None
    DlClass: Optional[DlClassType] = None
    NumberOfDevicesRequested: Optional[int] = None
    NumberOfDevicesInGroup: Optional[int] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysMulticastOutput] = None


class MulticastWirelessMetadata(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANMulticastMetadata] = None


class LteObj(BaseValidatorModel):
    Mcc: int
    Mnc: int
    EutranCid: int
    Tac: Optional[int] = None
    LteLocalId: Optional[LteLocalId] = None
    LteTimingAdvance: Optional[int] = None
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None
    NrCapable: Optional[bool] = None
    LteNmr: Optional[List[LteNmrObj]] = None


class SummaryMetricQueryResult(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStatus: Optional[MetricQueryStatusType] = None
    Error: Optional[str] = None
    MetricName: Optional[MetricNameType] = None
    Dimensions: Optional[List[Dimension]] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    StartTimestamp: Optional[datetime] = None
    EndTimestamp: Optional[datetime] = None
    Timestamps: Optional[List[datetime]] = None
    Values: Optional[List[MetricQueryValue]] = None
    Unit: Optional[str] = None

ParticipatingGatewaysMulticastUnion = Union[ParticipatingGatewaysMulticast, ParticipatingGatewaysMulticastOutput]


class PositionSolverConfigurations(BaseValidatorModel):
    SemtechGnss: Optional[SemtechGnssConfiguration] = None


class PositionSolverDetails(BaseValidatorModel):
    SemtechGnss: Optional[SemtechGnssDetail] = None


class StartSingleWirelessDeviceImportTaskRequest(BaseValidatorModel):
    DestinationName: str
    Sidewalk: SidewalkSingleStartImportInfo
    ClientRequestToken: Optional[str] = None
    DeviceName: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class StartWirelessDeviceImportTaskRequest(BaseValidatorModel):
    DestinationName: str
    Sidewalk: SidewalkStartImportInfo
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdatePartnerAccountRequest(BaseValidatorModel):
    Sidewalk: SidewalkUpdateAccount
    PartnerAccountId: str
    PartnerType: Literal['Sidewalk']


class UpdateWirelessDeviceImportTaskRequest(BaseValidatorModel):
    Id: str
    Sidewalk: SidewalkUpdateImportInfo


class TdscdmaObj(BaseValidatorModel):
    Mcc: int
    Mnc: int
    UtranCid: int
    Lac: Optional[int] = None
    TdscdmaLocalId: Optional[TdscdmaLocalId] = None
    TdscdmaTimingAdvance: Optional[int] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None
    TdscdmaNmr: Optional[List[TdscdmaNmrObj]] = None


class WcdmaObj(BaseValidatorModel):
    Mcc: int
    Mnc: int
    UtranCid: int
    Lac: Optional[int] = None
    WcdmaLocalId: Optional[WcdmaLocalId] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None
    WcdmaNmr: Optional[List[WcdmaNmrObj]] = None


class WirelessDeviceLogOptionOutput(BaseValidatorModel):
    Type: WirelessDeviceTypeType
    LogLevel: LogLevelType
    Events: Optional[List[WirelessDeviceEventLogOption]] = None


class WirelessDeviceLogOption(BaseValidatorModel):
    Type: WirelessDeviceTypeType
    LogLevel: LogLevelType
    Events: Optional[List[WirelessDeviceEventLogOption]] = None


class WirelessGatewayLogOptionOutput(BaseValidatorModel):
    Type: Literal['LoRaWAN']
    LogLevel: LogLevelType
    Events: Optional[List[WirelessGatewayEventLogOption]] = None


class WirelessGatewayLogOption(BaseValidatorModel):
    Type: Literal['LoRaWAN']
    LogLevel: LogLevelType
    Events: Optional[List[WirelessGatewayEventLogOption]] = None


class GetWirelessGatewayResponse(BaseValidatorModel):
    Name: str
    Id: str
    Description: str
    LoRaWAN: LoRaWANGatewayOutput
    Arn: str
    ThingName: str
    ThingArn: str
    ResponseMetadata: ResponseMetadata


class WirelessGatewayStatistics(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANGatewayOutput] = None
    LastUplinkReceivedAt: Optional[str] = None

LoRaWANGatewayUnion = Union[LoRaWANGateway, LoRaWANGatewayOutput]


class WirelessDeviceStatistics(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[WirelessDeviceTypeType] = None
    Name: Optional[str] = None
    DestinationName: Optional[str] = None
    LastUplinkReceivedAt: Optional[str] = None
    LoRaWAN: Optional[LoRaWANListDevice] = None
    Sidewalk: Optional[SidewalkListDevice] = None
    FuotaDeviceStatus: Optional[FuotaDeviceStatusType] = None
    MulticastDeviceStatus: Optional[str] = None
    McGroupId: Optional[int] = None


class GetDeviceProfileResponse(BaseValidatorModel):
    Arn: str
    Name: str
    Id: str
    LoRaWAN: LoRaWANDeviceProfileOutput
    Sidewalk: SidewalkGetDeviceProfile
    ResponseMetadata: ResponseMetadata


class LoRaWANDeviceOutput(BaseValidatorModel):
    DevEui: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    OtaaV1_1: Optional[OtaaV11] = None
    OtaaV1_0_x: Optional[OtaaV10X] = None
    AbpV1_1: Optional[AbpV11] = None
    AbpV1_0_x: Optional[AbpV10X] = None
    FPorts: Optional[FPortsOutput] = None


class LoRaWANDevice(BaseValidatorModel):
    DevEui: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    OtaaV1_1: Optional[OtaaV11] = None
    OtaaV1_0_x: Optional[OtaaV10X] = None
    AbpV1_1: Optional[AbpV11] = None
    AbpV1_0_x: Optional[AbpV10X] = None
    FPorts: Optional[FPorts] = None


class LoRaWANUpdateDevice(BaseValidatorModel):
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    AbpV1_1: Optional[UpdateAbpV11] = None
    AbpV1_0_x: Optional[UpdateAbpV10X] = None
    FPorts: Optional[UpdateFPorts] = None

FuotaTaskLogOptionUnion = Union[FuotaTaskLogOption, FuotaTaskLogOptionOutput]


class LoRaWANSendDataToDeviceOutput(BaseValidatorModel):
    FPort: Optional[int] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysOutput] = None

ParticipatingGatewaysUnion = Union[ParticipatingGateways, ParticipatingGatewaysOutput]

LoRaWANMulticastSessionUnion = Union[LoRaWANMulticastSession, LoRaWANMulticastSessionOutput]


class StartFuotaTaskRequest(BaseValidatorModel):
    Id: str
    LoRaWAN: Optional[LoRaWANStartFuotaTask] = None


class GetMetricsRequest(BaseValidatorModel):
    SummaryMetricQueries: Optional[List[SummaryMetricQuery]] = None


class ListWirelessDeviceImportTasksResponse(BaseValidatorModel):
    WirelessDeviceImportTaskList: List[WirelessDeviceImportTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GsmObj(BaseValidatorModel):
    Mcc: int
    Mnc: int
    Lac: int
    GeranCid: int
    GsmLocalId: Optional[GsmLocalId] = None
    GsmTimingAdvance: Optional[int] = None
    RxLevel: Optional[int] = None
    GsmNmr: Optional[List[GsmNmrObj]] = None


class ListDevicesForWirelessDeviceImportTaskResponse(BaseValidatorModel):
    DestinationName: str
    ImportedWirelessDeviceList: List[ImportedWirelessDevice]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EventNotificationItemConfigurations(BaseValidatorModel):
    DeviceRegistrationState: Optional[DeviceRegistrationStateEventConfiguration] = None
    Proximity: Optional[ProximityEventConfiguration] = None
    Join: Optional[JoinEventConfiguration] = None
    ConnectionStatus: Optional[ConnectionStatusEventConfiguration] = None
    MessageDeliveryStatus: Optional[MessageDeliveryStatusEventConfiguration] = None


class GetResourceEventConfigurationResponse(BaseValidatorModel):
    DeviceRegistrationState: DeviceRegistrationStateEventConfiguration
    Proximity: ProximityEventConfiguration
    Join: JoinEventConfiguration
    ConnectionStatus: ConnectionStatusEventConfiguration
    MessageDeliveryStatus: MessageDeliveryStatusEventConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateResourceEventConfigurationRequest(BaseValidatorModel):
    Identifier: str
    IdentifierType: IdentifierTypeType
    PartnerType: Optional[Literal['Sidewalk']] = None
    DeviceRegistrationState: Optional[DeviceRegistrationStateEventConfiguration] = None
    Proximity: Optional[ProximityEventConfiguration] = None
    Join: Optional[JoinEventConfiguration] = None
    ConnectionStatus: Optional[ConnectionStatusEventConfiguration] = None
    MessageDeliveryStatus: Optional[MessageDeliveryStatusEventConfiguration] = None


class GetEventConfigurationByResourceTypesResponse(BaseValidatorModel):
    DeviceRegistrationState: DeviceRegistrationStateResourceTypeEventConfiguration
    Proximity: ProximityResourceTypeEventConfiguration
    Join: JoinResourceTypeEventConfiguration
    ConnectionStatus: ConnectionStatusResourceTypeEventConfiguration
    MessageDeliveryStatus: MessageDeliveryStatusResourceTypeEventConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateEventConfigurationByResourceTypesRequest(BaseValidatorModel):
    DeviceRegistrationState: Optional[DeviceRegistrationStateResourceTypeEventConfiguration] = None
    Proximity: Optional[ProximityResourceTypeEventConfiguration] = None
    Join: Optional[JoinResourceTypeEventConfiguration] = None
    ConnectionStatus: Optional[ConnectionStatusResourceTypeEventConfiguration] = None
    MessageDeliveryStatus: Optional[MessageDeliveryStatusResourceTypeEventConfiguration] = None


class GetWirelessDeviceStatisticsResponse(BaseValidatorModel):
    WirelessDeviceId: str
    LastUplinkReceivedAt: str
    LoRaWAN: LoRaWANDeviceMetadata
    Sidewalk: SidewalkDeviceMetadata
    ResponseMetadata: ResponseMetadata


class CreateDeviceProfileRequest(BaseValidatorModel):
    Name: Optional[str] = None
    LoRaWAN: Optional[LoRaWANDeviceProfileUnion] = None
    Tags: Optional[List[Tag]] = None
    ClientRequestToken: Optional[str] = None
    Sidewalk: Optional[Dict[str, Any]] = None


class GetWirelessGatewayFirmwareInformationResponse(BaseValidatorModel):
    LoRaWAN: LoRaWANGatewayCurrentVersion
    ResponseMetadata: ResponseMetadata


class UpdateWirelessGatewayTaskCreate(BaseValidatorModel):
    UpdateDataSource: Optional[str] = None
    UpdateDataRole: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateGatewayTaskCreate] = None


class UpdateWirelessGatewayTaskEntry(BaseValidatorModel):
    Id: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateGatewayTaskEntry] = None
    Arn: Optional[str] = None


class GetMulticastGroupResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    Status: str
    LoRaWAN: LoRaWANMulticastGet
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


class SendDataToMulticastGroupRequest(BaseValidatorModel):
    Id: str
    PayloadData: str
    WirelessMetadata: MulticastWirelessMetadata


class GetMetricsResponse(BaseValidatorModel):
    SummaryMetricQueryResults: List[SummaryMetricQueryResult]
    ResponseMetadata: ResponseMetadata


class LoRaWANMulticast(BaseValidatorModel):
    RfRegion: Optional[SupportedRfRegionType] = None
    DlClass: Optional[DlClassType] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysMulticastUnion] = None


class PutPositionConfigurationRequest(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    Solvers: Optional[PositionSolverConfigurations] = None
    Destination: Optional[str] = None


class GetPositionConfigurationResponse(BaseValidatorModel):
    Solvers: PositionSolverDetails
    Destination: str
    ResponseMetadata: ResponseMetadata


class PositionConfigurationItem(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[PositionResourceTypeType] = None
    Solvers: Optional[PositionSolverDetails] = None
    Destination: Optional[str] = None

WirelessDeviceLogOptionUnion = Union[WirelessDeviceLogOption, WirelessDeviceLogOptionOutput]


class GetLogLevelsByResourceTypesResponse(BaseValidatorModel):
    DefaultLogLevel: LogLevelType
    WirelessGatewayLogOptions: List[WirelessGatewayLogOptionOutput]
    WirelessDeviceLogOptions: List[WirelessDeviceLogOptionOutput]
    FuotaTaskLogOptions: List[FuotaTaskLogOptionOutput]
    ResponseMetadata: ResponseMetadata

WirelessGatewayLogOptionUnion = Union[WirelessGatewayLogOption, WirelessGatewayLogOptionOutput]


class ListWirelessGatewaysResponse(BaseValidatorModel):
    WirelessGatewayList: List[WirelessGatewayStatistics]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateWirelessGatewayRequest(BaseValidatorModel):
    LoRaWAN: LoRaWANGatewayUnion
    Name: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientRequestToken: Optional[str] = None


class ListWirelessDevicesResponse(BaseValidatorModel):
    WirelessDeviceList: List[WirelessDeviceStatistics]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetWirelessDeviceResponse(BaseValidatorModel):
    Type: WirelessDeviceTypeType
    Name: str
    Description: str
    DestinationName: str
    Id: str
    Arn: str
    ThingName: str
    ThingArn: str
    LoRaWAN: LoRaWANDeviceOutput
    Sidewalk: SidewalkDevice
    Positioning: PositioningConfigStatusType
    ResponseMetadata: ResponseMetadata

LoRaWANDeviceUnion = Union[LoRaWANDevice, LoRaWANDeviceOutput]


class UpdateWirelessDeviceRequest(BaseValidatorModel):
    Id: str
    DestinationName: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateDevice] = None
    Positioning: Optional[PositioningConfigStatusType] = None


class DownlinkQueueMessage(BaseValidatorModel):
    MessageId: Optional[str] = None
    TransmitMode: Optional[int] = None
    ReceivedAt: Optional[str] = None
    LoRaWAN: Optional[LoRaWANSendDataToDeviceOutput] = None


class LoRaWANSendDataToDevice(BaseValidatorModel):
    FPort: Optional[int] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysUnion] = None


class StartMulticastGroupSessionRequest(BaseValidatorModel):
    Id: str
    LoRaWAN: LoRaWANMulticastSessionUnion


class CellTowers(BaseValidatorModel):
    Gsm: Optional[List[GsmObj]] = None
    Wcdma: Optional[List[WcdmaObj]] = None
    Tdscdma: Optional[List[TdscdmaObj]] = None
    Lte: Optional[List[LteObj]] = None
    Cdma: Optional[List[CdmaObj]] = None


class EventConfigurationItem(BaseValidatorModel):
    Identifier: Optional[str] = None
    IdentifierType: Optional[IdentifierTypeType] = None
    PartnerType: Optional[Literal['Sidewalk']] = None
    Events: Optional[EventNotificationItemConfigurations] = None


class CreateWirelessGatewayTaskDefinitionRequest(BaseValidatorModel):
    AutoCreateTasks: bool
    Name: Optional[str] = None
    Update: Optional[UpdateWirelessGatewayTaskCreate] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class GetWirelessGatewayTaskDefinitionResponse(BaseValidatorModel):
    AutoCreateTasks: bool
    Name: str
    Update: UpdateWirelessGatewayTaskCreate
    Arn: str
    ResponseMetadata: ResponseMetadata


class ListWirelessGatewayTaskDefinitionsResponse(BaseValidatorModel):
    TaskDefinitions: List[UpdateWirelessGatewayTaskEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateMulticastGroupRequest(BaseValidatorModel):
    LoRaWAN: LoRaWANMulticast
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateMulticastGroupRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANMulticast] = None


class ListPositionConfigurationsResponse(BaseValidatorModel):
    PositionConfigurationList: List[PositionConfigurationItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateLogLevelsByResourceTypesRequest(BaseValidatorModel):
    DefaultLogLevel: Optional[LogLevelType] = None
    FuotaTaskLogOptions: Optional[List[FuotaTaskLogOptionUnion]] = None
    WirelessDeviceLogOptions: Optional[List[WirelessDeviceLogOptionUnion]] = None
    WirelessGatewayLogOptions: Optional[List[WirelessGatewayLogOptionUnion]] = None


class CreateWirelessDeviceRequest(BaseValidatorModel):
    Type: WirelessDeviceTypeType
    DestinationName: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    LoRaWAN: Optional[LoRaWANDeviceUnion] = None
    Tags: Optional[List[Tag]] = None
    Positioning: Optional[PositioningConfigStatusType] = None
    Sidewalk: Optional[SidewalkCreateWirelessDevice] = None


class ListQueuedMessagesResponse(BaseValidatorModel):
    DownlinkQueueMessagesList: List[DownlinkQueueMessage]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

LoRaWANSendDataToDeviceUnion = Union[LoRaWANSendDataToDevice, LoRaWANSendDataToDeviceOutput]


class GetPositionEstimateRequest(BaseValidatorModel):
    WiFiAccessPoints: Optional[List[WiFiAccessPoint]] = None
    CellTowers: Optional[CellTowers] = None
    Ip: Optional[Ip] = None
    Gnss: Optional[Gnss] = None
    Timestamp: Optional[Timestamp] = None


class ListEventConfigurationsResponse(BaseValidatorModel):
    EventConfigurationsList: List[EventConfigurationItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class WirelessMetadata(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANSendDataToDeviceUnion] = None
    Sidewalk: Optional[SidewalkSendDataToDevice] = None


class SendDataToWirelessDeviceRequest(BaseValidatorModel):
    Id: str
    TransmitMode: int
    PayloadData: str

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
from aws_resource_validator.pydantic_models.iotwireless_constants import *

class SessionKeysAbpV10XTypeDef(BaseModel):
    NwkSKey: Optional[str] = None
    AppSKey: Optional[str] = None

class SessionKeysAbpV11TypeDef(BaseModel):
    FNwkSIntKey: Optional[str] = None
    SNwkSIntKey: Optional[str] = None
    NwkSEncKey: Optional[str] = None
    AppSKey: Optional[str] = None

class AccuracyTypeDef(BaseModel):
    HorizontalAccuracy: Optional[float] = None
    VerticalAccuracy: Optional[float] = None

class ApplicationConfigTypeDef(BaseModel):
    FPort: Optional[int] = None
    Type: Optional[Literal["SemtechGeolocation"]] = None
    DestinationName: Optional[str] = None

class SidewalkAccountInfoTypeDef(BaseModel):
    AmazonId: Optional[str] = None
    AppServerPrivateKey: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str
    MulticastGroupId: str

class AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str
    WirelessDeviceId: str

class AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef(BaseModel):
    Id: str
    WirelessDeviceId: str

class AssociateWirelessDeviceWithThingRequestRequestTypeDef(BaseModel):
    Id: str
    ThingArn: str

class AssociateWirelessGatewayWithCertificateRequestRequestTypeDef(BaseModel):
    Id: str
    IotCertificateId: str

class AssociateWirelessGatewayWithThingRequestRequestTypeDef(BaseModel):
    Id: str
    ThingArn: str

class BeaconingOutputTypeDef(BaseModel):
    DataRate: Optional[int] = None
    Frequencies: Optional[List[int]] = None

class BeaconingTypeDef(BaseModel):
    DataRate: Optional[int] = None
    Frequencies: Optional[Sequence[int]] = None

class CancelMulticastGroupSessionRequestRequestTypeDef(BaseModel):
    Id: str

class CdmaLocalIdTypeDef(BaseModel):
    PnOffset: int
    CdmaChannel: int

class CdmaNmrObjTypeDef(BaseModel):
    PnOffset: int
    CdmaChannel: int
    PilotPower: Optional[int] = None
    BaseStationId: Optional[int] = None

class CertificateListTypeDef(BaseModel):
    SigningAlg: SigningAlgType
    Value: str

class LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef(BaseModel):
    GatewayEuiEventTopic: Optional[EventNotificationTopicStatusType] = None

class LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef(BaseModel):
    WirelessGatewayEventTopic: Optional[EventNotificationTopicStatusType] = None

class LoRaWANDeviceProfileTypeDef(BaseModel):
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
    FactoryPresetFreqsList: Optional[Sequence[int]] = None
    MaxEirp: Optional[int] = None
    MaxDutyCycle: Optional[int] = None
    RfRegion: Optional[str] = None
    SupportsJoin: Optional[bool] = None
    Supports32BitFCnt: Optional[bool] = None

class LoRaWANFuotaTaskTypeDef(BaseModel):
    RfRegion: Optional[SupportedRfRegionType] = None

class LoRaWANMulticastTypeDef(BaseModel):
    RfRegion: Optional[SupportedRfRegionType] = None
    DlClass: Optional[DlClassType] = None

class TraceContentTypeDef(BaseModel):
    WirelessDeviceFrameInfo: Optional[WirelessDeviceFrameInfoType] = None
    LogLevel: Optional[LogLevelType] = None
    MulticastFrameInfo: Optional[MulticastFrameInfoType] = None

class LoRaWANServiceProfileTypeDef(BaseModel):
    AddGwMetadata: Optional[bool] = None
    DrMin: Optional[int] = None
    DrMax: Optional[int] = None
    PrAllowed: Optional[bool] = None
    RaAllowed: Optional[bool] = None

class SidewalkCreateWirelessDeviceTypeDef(BaseModel):
    DeviceProfileId: Optional[str] = None

class CreateWirelessGatewayTaskRequestRequestTypeDef(BaseModel):
    Id: str
    WirelessGatewayTaskDefinitionId: str

class DakCertificateMetadataTypeDef(BaseModel):
    CertificateId: str
    MaxAllowedSignature: Optional[int] = None
    FactorySupport: Optional[bool] = None
    ApId: Optional[str] = None
    DeviceTypeId: Optional[str] = None

class DeleteDestinationRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteDeviceProfileRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteMulticastGroupRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteNetworkAnalyzerConfigurationRequestRequestTypeDef(BaseModel):
    ConfigurationName: str

class DeleteQueuedMessagesRequestRequestTypeDef(BaseModel):
    Id: str
    MessageId: str
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None

class DeleteServiceProfileRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteWirelessDeviceImportTaskRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteWirelessDeviceRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteWirelessGatewayRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteWirelessGatewayTaskRequestRequestTypeDef(BaseModel):
    Id: str

class DeregisterWirelessDeviceRequestRequestTypeDef(BaseModel):
    Identifier: str
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None

class DestinationsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ExpressionType: Optional[ExpressionTypeType] = None
    Expression: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None

class DeviceProfileTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Id: Optional[str] = None

class SidewalkEventNotificationConfigurationsTypeDef(BaseModel):
    AmazonIdEventTopic: Optional[EventNotificationTopicStatusType] = None

class SidewalkResourceTypeEventConfigurationTypeDef(BaseModel):
    WirelessDeviceEventTopic: Optional[EventNotificationTopicStatusType] = None

class DimensionTypeDef(BaseModel):
    name: Optional[DimensionNameType] = None
    value: Optional[str] = None

class DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef(BaseModel):
    PartnerAccountId: str
    PartnerType: Literal["Sidewalk"]

class DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str
    MulticastGroupId: str

class DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str
    WirelessDeviceId: str

class DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef(BaseModel):
    Id: str
    WirelessDeviceId: str

class DisassociateWirelessDeviceFromThingRequestRequestTypeDef(BaseModel):
    Id: str

class DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef(BaseModel):
    Id: str

class DisassociateWirelessGatewayFromThingRequestRequestTypeDef(BaseModel):
    Id: str

class PositioningTypeDef(BaseModel):
    ClockSync: Optional[int] = None
    Stream: Optional[int] = None
    Gnss: Optional[int] = None

class FuotaTaskTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None

class GatewayListItemTypeDef(BaseModel):
    GatewayId: str
    DownlinkFrequency: int

class GetDestinationRequestRequestTypeDef(BaseModel):
    Name: str

class GetDeviceProfileRequestRequestTypeDef(BaseModel):
    Id: str

class LoRaWANDeviceProfileOutputTypeDef(BaseModel):
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

class GetFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str

class LoRaWANFuotaTaskGetInfoTypeDef(BaseModel):
    RfRegion: Optional[str] = None
    StartTime: Optional[datetime] = None

class SummaryMetricConfigurationTypeDef(BaseModel):
    Status: Optional[SummaryMetricConfigurationStatusType] = None

class GetMulticastGroupRequestRequestTypeDef(BaseModel):
    Id: str

class LoRaWANMulticastGetTypeDef(BaseModel):
    RfRegion: Optional[SupportedRfRegionType] = None
    DlClass: Optional[DlClassType] = None
    NumberOfDevicesRequested: Optional[int] = None
    NumberOfDevicesInGroup: Optional[int] = None

class GetMulticastGroupSessionRequestRequestTypeDef(BaseModel):
    Id: str

class LoRaWANMulticastSessionOutputTypeDef(BaseModel):
    DlDr: Optional[int] = None
    DlFreq: Optional[int] = None
    SessionStartTime: Optional[datetime] = None
    SessionTimeout: Optional[int] = None
    PingSlotPeriod: Optional[int] = None

class GetNetworkAnalyzerConfigurationRequestRequestTypeDef(BaseModel):
    ConfigurationName: str

class GetPartnerAccountRequestRequestTypeDef(BaseModel):
    PartnerAccountId: str
    PartnerType: Literal["Sidewalk"]

class SidewalkAccountInfoWithFingerprintTypeDef(BaseModel):
    AmazonId: Optional[str] = None
    Fingerprint: Optional[str] = None
    Arn: Optional[str] = None

class GetPositionConfigurationRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType

class GnssTypeDef(BaseModel):
    Payload: str
    CaptureTime: Optional[float] = None
    CaptureTimeAccuracy: Optional[float] = None
    AssistPosition: Optional[Sequence[float]] = None
    AssistAltitude: Optional[float] = None
    Use2DSolver: Optional[bool] = None

class IpTypeDef(BaseModel):
    IpAddress: str

class WiFiAccessPointTypeDef(BaseModel):
    MacAddress: str
    Rss: int

class GetPositionRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType

class GetResourceEventConfigurationRequestRequestTypeDef(BaseModel):
    Identifier: str
    IdentifierType: IdentifierTypeType
    PartnerType: Optional[Literal["Sidewalk"]] = None

class GetResourceLogLevelRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: str

class GetResourcePositionRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType

class GetServiceEndpointRequestRequestTypeDef(BaseModel):
    ServiceType: Optional[WirelessGatewayServiceTypeType] = None

class GetServiceProfileRequestRequestTypeDef(BaseModel):
    Id: str

class LoRaWANGetServiceProfileInfoTypeDef(BaseModel):
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

class GetWirelessDeviceImportTaskRequestRequestTypeDef(BaseModel):
    Id: str

class SidewalkGetStartImportInfoTypeDef(BaseModel):
    DeviceCreationFileList: Optional[List[str]] = None
    Role: Optional[str] = None

class GetWirelessDeviceRequestRequestTypeDef(BaseModel):
    Identifier: str
    IdentifierType: WirelessDeviceIdTypeType

class GetWirelessDeviceStatisticsRequestRequestTypeDef(BaseModel):
    WirelessDeviceId: str

class SidewalkDeviceMetadataTypeDef(BaseModel):
    Rssi: Optional[int] = None
    BatteryLevel: Optional[BatteryLevelType] = None
    Event: Optional[EventType] = None
    DeviceState: Optional[DeviceStateType] = None

class GetWirelessGatewayCertificateRequestRequestTypeDef(BaseModel):
    Id: str

class GetWirelessGatewayFirmwareInformationRequestRequestTypeDef(BaseModel):
    Id: str

class GetWirelessGatewayRequestRequestTypeDef(BaseModel):
    Identifier: str
    IdentifierType: WirelessGatewayIdTypeType

class GetWirelessGatewayStatisticsRequestRequestTypeDef(BaseModel):
    WirelessGatewayId: str

class GetWirelessGatewayTaskDefinitionRequestRequestTypeDef(BaseModel):
    Id: str

class GetWirelessGatewayTaskRequestRequestTypeDef(BaseModel):
    Id: str

class GlobalIdentityTypeDef(BaseModel):
    Lac: int
    GeranCid: int

class GsmLocalIdTypeDef(BaseModel):
    Bsic: int
    Bcch: int

class ImportedSidewalkDeviceTypeDef(BaseModel):
    SidewalkManufacturingSn: Optional[str] = None
    OnboardingStatus: Optional[OnboardStatusType] = None
    OnboardingStatusReason: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class LoRaWANJoinEventNotificationConfigurationsTypeDef(BaseModel):
    DevEuiEventTopic: Optional[EventNotificationTopicStatusType] = None

class LoRaWANJoinResourceTypeEventConfigurationTypeDef(BaseModel):
    WirelessDeviceEventTopic: Optional[EventNotificationTopicStatusType] = None

class ListDestinationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDeviceProfilesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DeviceProfileType: Optional[DeviceProfileTypeType] = None

class ListDevicesForWirelessDeviceImportTaskRequestRequestTypeDef(BaseModel):
    Id: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[OnboardStatusType] = None

class ListEventConfigurationsRequestRequestTypeDef(BaseModel):
    ResourceType: EventNotificationResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFuotaTasksRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMulticastGroupsByFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MulticastGroupByFuotaTaskTypeDef(BaseModel):
    Id: Optional[str] = None

class ListMulticastGroupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MulticastGroupTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ListNetworkAnalyzerConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NetworkAnalyzerConfigurationsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ListPartnerAccountsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPositionConfigurationsRequestRequestTypeDef(BaseModel):
    ResourceType: Optional[PositionResourceTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListQueuedMessagesRequestRequestTypeDef(BaseModel):
    Id: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None

class ListServiceProfilesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ServiceProfileTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Id: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListWirelessDeviceImportTasksRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListWirelessDevicesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DestinationName: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None
    FuotaTaskId: Optional[str] = None
    MulticastGroupId: Optional[str] = None

class ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    TaskDefinitionType: Optional[Literal["UPDATE"]] = None

class ListWirelessGatewaysRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LoRaWANGatewayMetadataTypeDef(BaseModel):
    GatewayEui: Optional[str] = None
    Snr: Optional[float] = None
    Rssi: Optional[float] = None

class LoRaWANPublicGatewayMetadataTypeDef(BaseModel):
    ProviderNetId: Optional[str] = None
    Id: Optional[str] = None
    Rssi: Optional[float] = None
    Snr: Optional[float] = None
    RfRegion: Optional[str] = None
    DlAllowed: Optional[bool] = None

class OtaaV10XTypeDef(BaseModel):
    AppKey: Optional[str] = None
    AppEui: Optional[str] = None
    JoinEui: Optional[str] = None
    GenAppKey: Optional[str] = None

class OtaaV11TypeDef(BaseModel):
    AppKey: Optional[str] = None
    NwkKey: Optional[str] = None
    JoinEui: Optional[str] = None

class LoRaWANGatewayVersionTypeDef(BaseModel):
    PackageVersion: Optional[str] = None
    Model: Optional[str] = None
    Station: Optional[str] = None

class LoRaWANListDeviceTypeDef(BaseModel):
    DevEui: Optional[str] = None

class LoRaWANMulticastMetadataTypeDef(BaseModel):
    FPort: Optional[int] = None

class UpdateAbpV10XTypeDef(BaseModel):
    FCntStart: Optional[int] = None

class UpdateAbpV11TypeDef(BaseModel):
    FCntStart: Optional[int] = None

class LteLocalIdTypeDef(BaseModel):
    Pci: int
    Earfcn: int

class LteNmrObjTypeDef(BaseModel):
    Pci: int
    Earfcn: int
    EutranCid: int
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None

class MetricQueryValueTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None
    Sum: Optional[float] = None
    Avg: Optional[float] = None
    Std: Optional[float] = None
    P90: Optional[float] = None

class SemtechGnssConfigurationTypeDef(BaseModel):
    Status: PositionConfigurationStatusType
    Fec: PositionConfigurationFecType

class SemtechGnssDetailTypeDef(BaseModel):
    Provider: Optional[Literal["Semtech"]] = None
    Type: Optional[Literal["GNSS"]] = None
    Status: Optional[PositionConfigurationStatusType] = None
    Fec: Optional[PositionConfigurationFecType] = None

class PutResourceLogLevelRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: str
    LogLevel: LogLevelType

class ResetResourceLogLevelRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: str

class SidewalkSendDataToDeviceTypeDef(BaseModel):
    Seq: Optional[int] = None
    MessageType: Optional[MessageTypeType] = None
    AckModeRetryDurationSecs: Optional[int] = None

class SidewalkSingleStartImportInfoTypeDef(BaseModel):
    SidewalkManufacturingSn: Optional[str] = None

class SidewalkStartImportInfoTypeDef(BaseModel):
    DeviceCreationFile: Optional[str] = None
    Role: Optional[str] = None

class SidewalkUpdateAccountTypeDef(BaseModel):
    AppServerPrivateKey: Optional[str] = None

class SidewalkUpdateImportInfoTypeDef(BaseModel):
    DeviceCreationFile: Optional[str] = None

class TdscdmaLocalIdTypeDef(BaseModel):
    Uarfcn: int
    CellParams: int

class TdscdmaNmrObjTypeDef(BaseModel):
    Uarfcn: int
    CellParams: int
    UtranCid: Optional[int] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None

class TestWirelessDeviceRequestRequestTypeDef(BaseModel):
    Id: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDestinationRequestRequestTypeDef(BaseModel):
    Name: str
    ExpressionType: Optional[ExpressionTypeType] = None
    Expression: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None

class UpdatePositionRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    Position: Sequence[float]

class UpdateWirelessGatewayRequestRequestTypeDef(BaseModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    JoinEuiFilters: Optional[Sequence[Sequence[str]]] = None
    NetIdFilters: Optional[Sequence[str]] = None
    MaxEirp: Optional[float] = None

class WcdmaLocalIdTypeDef(BaseModel):
    Uarfcndl: int
    Psc: int

class WcdmaNmrObjTypeDef(BaseModel):
    Uarfcndl: int
    Psc: int
    UtranCid: int
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None

class WirelessDeviceEventLogOptionTypeDef(BaseModel):
    Event: WirelessDeviceEventType
    LogLevel: LogLevelType

class WirelessGatewayEventLogOptionTypeDef(BaseModel):
    Event: WirelessGatewayEventType
    LogLevel: LogLevelType

class AbpV10XTypeDef(BaseModel):
    DevAddr: Optional[str] = None
    SessionKeys: Optional[SessionKeysAbpV10XTypeDef] = None
    FCntStart: Optional[int] = None

class AbpV11TypeDef(BaseModel):
    DevAddr: Optional[str] = None
    SessionKeys: Optional[SessionKeysAbpV11TypeDef] = None
    FCntStart: Optional[int] = None

class AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef(BaseModel):
    Sidewalk: SidewalkAccountInfoTypeDef
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDestinationRequestRequestTypeDef(BaseModel):
    Name: str
    ExpressionType: ExpressionTypeType
    Expression: str
    RoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef(BaseModel):
    Id: str
    QueryString: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef(BaseModel):
    Id: str
    QueryString: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class AssociateAwsAccountWithPartnerAccountResponseTypeDef(BaseModel):
    Sidewalk: SidewalkAccountInfoTypeDef
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateWirelessGatewayWithCertificateResponseTypeDef(BaseModel):
    IotCertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDestinationResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceProfileResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFuotaTaskResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMulticastGroupResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkAnalyzerConfigurationResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceProfileResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWirelessDeviceResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWirelessGatewayResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWirelessGatewayTaskDefinitionResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWirelessGatewayTaskResponseTypeDef(BaseModel):
    WirelessGatewayTaskDefinitionId: str
    Status: WirelessGatewayTaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetDestinationResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    Expression: str
    ExpressionType: ExpressionTypeType
    Description: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPositionEstimateResponseTypeDef(BaseModel):
    GeoJsonPayload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetPositionResponseTypeDef(BaseModel):
    Position: List[float]
    Accuracy: AccuracyTypeDef
    SolverType: Literal["GNSS"]
    SolverProvider: Literal["Semtech"]
    SolverVersion: str
    Timestamp: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceLogLevelResponseTypeDef(BaseModel):
    LogLevel: LogLevelType
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePositionResponseTypeDef(BaseModel):
    GeoJsonPayload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceEndpointResponseTypeDef(BaseModel):
    ServiceType: WirelessGatewayServiceTypeType
    ServiceEndpoint: str
    ServerTrust: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWirelessGatewayCertificateResponseTypeDef(BaseModel):
    IotCertificateId: str
    LoRaWANNetworkServerCertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWirelessGatewayStatisticsResponseTypeDef(BaseModel):
    WirelessGatewayId: str
    LastUplinkReceivedAt: str
    ConnectionStatus: ConnectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetWirelessGatewayTaskResponseTypeDef(BaseModel):
    WirelessGatewayId: str
    WirelessGatewayTaskDefinitionId: str
    LastUplinkReceivedAt: str
    TaskCreatedAt: str
    Status: WirelessGatewayTaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendDataToMulticastGroupResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendDataToWirelessDeviceResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSingleWirelessDeviceImportTaskResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartWirelessDeviceImportTaskResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestWirelessDeviceResponseTypeDef(BaseModel):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef

class LoRaWANGatewayOutputTypeDef(BaseModel):
    GatewayEui: Optional[str] = None
    RfRegion: Optional[str] = None
    JoinEuiFilters: Optional[List[List[str]]] = None
    NetIdFilters: Optional[List[str]] = None
    SubBands: Optional[List[int]] = None
    Beaconing: Optional[BeaconingOutputTypeDef] = None
    MaxEirp: Optional[float] = None

class LoRaWANGatewayTypeDef(BaseModel):
    GatewayEui: Optional[str] = None
    RfRegion: Optional[str] = None
    JoinEuiFilters: Optional[Sequence[Sequence[str]]] = None
    NetIdFilters: Optional[Sequence[str]] = None
    SubBands: Optional[Sequence[int]] = None
    Beaconing: Optional[BeaconingTypeDef] = None
    MaxEirp: Optional[float] = None

class UpdateResourcePositionRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    GeoJsonPayload: Optional[BlobTypeDef] = None

class CdmaObjTypeDef(BaseModel):
    SystemId: int
    NetworkId: int
    BaseStationId: int
    RegistrationZone: Optional[int] = None
    CdmaLocalId: Optional[CdmaLocalIdTypeDef] = None
    PilotPower: Optional[int] = None
    BaseLat: Optional[float] = None
    BaseLng: Optional[float] = None
    CdmaNmr: Optional[Sequence[CdmaNmrObjTypeDef]] = None

class SidewalkDeviceTypeDef(BaseModel):
    AmazonId: Optional[str] = None
    SidewalkId: Optional[str] = None
    SidewalkManufacturingSn: Optional[str] = None
    DeviceCertificates: Optional[List[CertificateListTypeDef]] = None
    PrivateKeys: Optional[List[CertificateListTypeDef]] = None
    DeviceProfileId: Optional[str] = None
    CertificateId: Optional[str] = None
    Status: Optional[WirelessDeviceSidewalkStatusType] = None

class SidewalkListDeviceTypeDef(BaseModel):
    AmazonId: Optional[str] = None
    SidewalkId: Optional[str] = None
    SidewalkManufacturingSn: Optional[str] = None
    DeviceCertificates: Optional[List[CertificateListTypeDef]] = None
    DeviceProfileId: Optional[str] = None
    Status: Optional[WirelessDeviceSidewalkStatusType] = None

class ConnectionStatusEventConfigurationTypeDef(BaseModel):
    LoRaWAN: Optional[LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef] = None
    WirelessGatewayIdEventTopic: Optional[EventNotificationTopicStatusType] = None

class ConnectionStatusResourceTypeEventConfigurationTypeDef(BaseModel):
    LoRaWAN: Optional[LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef] = None

class CreateDeviceProfileRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    LoRaWAN: Optional[LoRaWANDeviceProfileTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None
    Sidewalk: Optional[Mapping[str, Any]] = None

class CreateFuotaTaskRequestRequestTypeDef(BaseModel):
    FirmwareUpdateImage: str
    FirmwareUpdateRole: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    LoRaWAN: Optional[LoRaWANFuotaTaskTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    RedundancyPercent: Optional[int] = None
    FragmentSizeBytes: Optional[int] = None
    FragmentIntervalMS: Optional[int] = None

class UpdateFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANFuotaTaskTypeDef] = None
    FirmwareUpdateImage: Optional[str] = None
    FirmwareUpdateRole: Optional[str] = None
    RedundancyPercent: Optional[int] = None
    FragmentSizeBytes: Optional[int] = None
    FragmentIntervalMS: Optional[int] = None

class CreateMulticastGroupRequestRequestTypeDef(BaseModel):
    LoRaWAN: LoRaWANMulticastTypeDef
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateMulticastGroupRequestRequestTypeDef(BaseModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANMulticastTypeDef] = None

class CreateNetworkAnalyzerConfigurationRequestRequestTypeDef(BaseModel):
    Name: str
    TraceContent: Optional[TraceContentTypeDef] = None
    WirelessDevices: Optional[Sequence[str]] = None
    WirelessGateways: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None
    MulticastGroups: Optional[Sequence[str]] = None

class GetNetworkAnalyzerConfigurationResponseTypeDef(BaseModel):
    TraceContent: TraceContentTypeDef
    WirelessDevices: List[str]
    WirelessGateways: List[str]
    Description: str
    Arn: str
    Name: str
    MulticastGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef(BaseModel):
    ConfigurationName: str
    TraceContent: Optional[TraceContentTypeDef] = None
    WirelessDevicesToAdd: Optional[Sequence[str]] = None
    WirelessDevicesToRemove: Optional[Sequence[str]] = None
    WirelessGatewaysToAdd: Optional[Sequence[str]] = None
    WirelessGatewaysToRemove: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    MulticastGroupsToAdd: Optional[Sequence[str]] = None
    MulticastGroupsToRemove: Optional[Sequence[str]] = None

class CreateServiceProfileRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    LoRaWAN: Optional[LoRaWANServiceProfileTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class SidewalkGetDeviceProfileTypeDef(BaseModel):
    ApplicationServerPublicKey: Optional[str] = None
    QualificationStatus: Optional[bool] = None
    DakCertificateMetadata: Optional[List[DakCertificateMetadataTypeDef]] = None

class ListDestinationsResponseTypeDef(BaseModel):
    DestinationList: List[DestinationsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDeviceProfilesResponseTypeDef(BaseModel):
    DeviceProfileList: List[DeviceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeviceRegistrationStateEventConfigurationTypeDef(BaseModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurationsTypeDef] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None

class MessageDeliveryStatusEventConfigurationTypeDef(BaseModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurationsTypeDef] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None

class ProximityEventConfigurationTypeDef(BaseModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurationsTypeDef] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None

class DeviceRegistrationStateResourceTypeEventConfigurationTypeDef(BaseModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfigurationTypeDef] = None

class MessageDeliveryStatusResourceTypeEventConfigurationTypeDef(BaseModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfigurationTypeDef] = None

class ProximityResourceTypeEventConfigurationTypeDef(BaseModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfigurationTypeDef] = None

class FPortsOutputTypeDef(BaseModel):
    Fuota: Optional[int] = None
    Multicast: Optional[int] = None
    ClockSync: Optional[int] = None
    Positioning: Optional[PositioningTypeDef] = None
    Applications: Optional[List[ApplicationConfigTypeDef]] = None

class FPortsTypeDef(BaseModel):
    Fuota: Optional[int] = None
    Multicast: Optional[int] = None
    ClockSync: Optional[int] = None
    Positioning: Optional[PositioningTypeDef] = None
    Applications: Optional[Sequence[ApplicationConfigTypeDef]] = None

class UpdateFPortsTypeDef(BaseModel):
    Positioning: Optional[PositioningTypeDef] = None
    Applications: Optional[Sequence[ApplicationConfigTypeDef]] = None

class ListFuotaTasksResponseTypeDef(BaseModel):
    FuotaTaskList: List[FuotaTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ParticipatingGatewaysOutputTypeDef(BaseModel):
    DownlinkMode: DownlinkModeType
    GatewayList: List[GatewayListItemTypeDef]
    TransmissionInterval: int

class ParticipatingGatewaysTypeDef(BaseModel):
    DownlinkMode: DownlinkModeType
    GatewayList: Sequence[GatewayListItemTypeDef]
    TransmissionInterval: int

class GetFuotaTaskResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Status: FuotaTaskStatusType
    Name: str
    Description: str
    LoRaWAN: LoRaWANFuotaTaskGetInfoTypeDef
    FirmwareUpdateImage: str
    FirmwareUpdateRole: str
    CreatedAt: datetime
    RedundancyPercent: int
    FragmentSizeBytes: int
    FragmentIntervalMS: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetMetricConfigurationResponseTypeDef(BaseModel):
    SummaryMetric: SummaryMetricConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMetricConfigurationRequestRequestTypeDef(BaseModel):
    SummaryMetric: Optional[SummaryMetricConfigurationTypeDef] = None

class GetMulticastGroupResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    Status: str
    LoRaWAN: LoRaWANMulticastGetTypeDef
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMulticastGroupSessionResponseTypeDef(BaseModel):
    LoRaWAN: LoRaWANMulticastSessionOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartnerAccountResponseTypeDef(BaseModel):
    Sidewalk: SidewalkAccountInfoWithFingerprintTypeDef
    AccountLinked: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListPartnerAccountsResponseTypeDef(BaseModel):
    Sidewalk: List[SidewalkAccountInfoWithFingerprintTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LoRaWANMulticastSessionTypeDef(BaseModel):
    DlDr: Optional[int] = None
    DlFreq: Optional[int] = None
    SessionStartTime: Optional[TimestampTypeDef] = None
    SessionTimeout: Optional[int] = None
    PingSlotPeriod: Optional[int] = None

class LoRaWANStartFuotaTaskTypeDef(BaseModel):
    StartTime: Optional[TimestampTypeDef] = None

class SummaryMetricQueryTypeDef(BaseModel):
    QueryId: Optional[str] = None
    MetricName: Optional[MetricNameType] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    StartTimestamp: Optional[TimestampTypeDef] = None
    EndTimestamp: Optional[TimestampTypeDef] = None

class GetServiceProfileResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    Id: str
    LoRaWAN: LoRaWANGetServiceProfileInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWirelessDeviceImportTaskResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    DestinationName: str
    Sidewalk: SidewalkGetStartImportInfoTypeDef
    CreationTime: datetime
    Status: ImportTaskStatusType
    StatusReason: str
    InitializedImportedDeviceCount: int
    PendingImportedDeviceCount: int
    OnboardedImportedDeviceCount: int
    FailedImportedDeviceCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class WirelessDeviceImportTaskTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    DestinationName: Optional[str] = None
    Sidewalk: Optional[SidewalkGetStartImportInfoTypeDef] = None
    CreationTime: Optional[datetime] = None
    Status: Optional[ImportTaskStatusType] = None
    StatusReason: Optional[str] = None
    InitializedImportedDeviceCount: Optional[int] = None
    PendingImportedDeviceCount: Optional[int] = None
    OnboardedImportedDeviceCount: Optional[int] = None
    FailedImportedDeviceCount: Optional[int] = None

class GsmNmrObjTypeDef(BaseModel):
    Bsic: int
    Bcch: int
    RxLevel: Optional[int] = None
    GlobalIdentity: Optional[GlobalIdentityTypeDef] = None

class ImportedWirelessDeviceTypeDef(BaseModel):
    Sidewalk: Optional[ImportedSidewalkDeviceTypeDef] = None

class JoinEventConfigurationTypeDef(BaseModel):
    LoRaWAN: Optional[LoRaWANJoinEventNotificationConfigurationsTypeDef] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None

class JoinResourceTypeEventConfigurationTypeDef(BaseModel):
    LoRaWAN: Optional[LoRaWANJoinResourceTypeEventConfigurationTypeDef] = None

class ListMulticastGroupsByFuotaTaskResponseTypeDef(BaseModel):
    MulticastGroupList: List[MulticastGroupByFuotaTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMulticastGroupsResponseTypeDef(BaseModel):
    MulticastGroupList: List[MulticastGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNetworkAnalyzerConfigurationsResponseTypeDef(BaseModel):
    NetworkAnalyzerConfigurationList: List[NetworkAnalyzerConfigurationsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListServiceProfilesResponseTypeDef(BaseModel):
    ServiceProfileList: List[ServiceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LoRaWANDeviceMetadataTypeDef(BaseModel):
    DevEui: Optional[str] = None
    FPort: Optional[int] = None
    DataRate: Optional[int] = None
    Frequency: Optional[int] = None
    Timestamp: Optional[str] = None
    Gateways: Optional[List[LoRaWANGatewayMetadataTypeDef]] = None
    PublicGateways: Optional[List[LoRaWANPublicGatewayMetadataTypeDef]] = None

class LoRaWANGatewayCurrentVersionTypeDef(BaseModel):
    CurrentVersion: Optional[LoRaWANGatewayVersionTypeDef] = None

class LoRaWANUpdateGatewayTaskCreateTypeDef(BaseModel):
    UpdateSignature: Optional[str] = None
    SigKeyCrc: Optional[int] = None
    CurrentVersion: Optional[LoRaWANGatewayVersionTypeDef] = None
    UpdateVersion: Optional[LoRaWANGatewayVersionTypeDef] = None

class LoRaWANUpdateGatewayTaskEntryTypeDef(BaseModel):
    CurrentVersion: Optional[LoRaWANGatewayVersionTypeDef] = None
    UpdateVersion: Optional[LoRaWANGatewayVersionTypeDef] = None

class MulticastWirelessMetadataTypeDef(BaseModel):
    LoRaWAN: Optional[LoRaWANMulticastMetadataTypeDef] = None

class LteObjTypeDef(BaseModel):
    Mcc: int
    Mnc: int
    EutranCid: int
    Tac: Optional[int] = None
    LteLocalId: Optional[LteLocalIdTypeDef] = None
    LteTimingAdvance: Optional[int] = None
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None
    NrCapable: Optional[bool] = None
    LteNmr: Optional[Sequence[LteNmrObjTypeDef]] = None

class SummaryMetricQueryResultTypeDef(BaseModel):
    QueryId: Optional[str] = None
    QueryStatus: Optional[MetricQueryStatusType] = None
    Error: Optional[str] = None
    MetricName: Optional[MetricNameType] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    StartTimestamp: Optional[datetime] = None
    EndTimestamp: Optional[datetime] = None
    Timestamps: Optional[List[datetime]] = None
    Values: Optional[List[MetricQueryValueTypeDef]] = None
    Unit: Optional[str] = None

class PositionSolverConfigurationsTypeDef(BaseModel):
    SemtechGnss: Optional[SemtechGnssConfigurationTypeDef] = None

class PositionSolverDetailsTypeDef(BaseModel):
    SemtechGnss: Optional[SemtechGnssDetailTypeDef] = None

class StartSingleWirelessDeviceImportTaskRequestRequestTypeDef(BaseModel):
    DestinationName: str
    Sidewalk: SidewalkSingleStartImportInfoTypeDef
    ClientRequestToken: Optional[str] = None
    DeviceName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartWirelessDeviceImportTaskRequestRequestTypeDef(BaseModel):
    DestinationName: str
    Sidewalk: SidewalkStartImportInfoTypeDef
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdatePartnerAccountRequestRequestTypeDef(BaseModel):
    Sidewalk: SidewalkUpdateAccountTypeDef
    PartnerAccountId: str
    PartnerType: Literal["Sidewalk"]

class UpdateWirelessDeviceImportTaskRequestRequestTypeDef(BaseModel):
    Id: str
    Sidewalk: SidewalkUpdateImportInfoTypeDef

class TdscdmaObjTypeDef(BaseModel):
    Mcc: int
    Mnc: int
    UtranCid: int
    Lac: Optional[int] = None
    TdscdmaLocalId: Optional[TdscdmaLocalIdTypeDef] = None
    TdscdmaTimingAdvance: Optional[int] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None
    TdscdmaNmr: Optional[Sequence[TdscdmaNmrObjTypeDef]] = None

class WcdmaObjTypeDef(BaseModel):
    Mcc: int
    Mnc: int
    UtranCid: int
    Lac: Optional[int] = None
    WcdmaLocalId: Optional[WcdmaLocalIdTypeDef] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None
    WcdmaNmr: Optional[Sequence[WcdmaNmrObjTypeDef]] = None

class WirelessDeviceLogOptionOutputTypeDef(BaseModel):
    Type: WirelessDeviceTypeType
    LogLevel: LogLevelType
    Events: Optional[List[WirelessDeviceEventLogOptionTypeDef]] = None

class WirelessDeviceLogOptionTypeDef(BaseModel):
    Type: WirelessDeviceTypeType
    LogLevel: LogLevelType
    Events: Optional[Sequence[WirelessDeviceEventLogOptionTypeDef]] = None

class WirelessGatewayLogOptionOutputTypeDef(BaseModel):
    Type: Literal["LoRaWAN"]
    LogLevel: LogLevelType
    Events: Optional[List[WirelessGatewayEventLogOptionTypeDef]] = None

class WirelessGatewayLogOptionTypeDef(BaseModel):
    Type: Literal["LoRaWAN"]
    LogLevel: LogLevelType
    Events: Optional[Sequence[WirelessGatewayEventLogOptionTypeDef]] = None

class GetWirelessGatewayResponseTypeDef(BaseModel):
    Name: str
    Id: str
    Description: str
    LoRaWAN: LoRaWANGatewayOutputTypeDef
    Arn: str
    ThingName: str
    ThingArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class WirelessGatewayStatisticsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANGatewayOutputTypeDef] = None
    LastUplinkReceivedAt: Optional[str] = None

class CreateWirelessGatewayRequestRequestTypeDef(BaseModel):
    LoRaWAN: LoRaWANGatewayTypeDef
    Name: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class WirelessDeviceStatisticsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[WirelessDeviceTypeType] = None
    Name: Optional[str] = None
    DestinationName: Optional[str] = None
    LastUplinkReceivedAt: Optional[str] = None
    LoRaWAN: Optional[LoRaWANListDeviceTypeDef] = None
    Sidewalk: Optional[SidewalkListDeviceTypeDef] = None
    FuotaDeviceStatus: Optional[FuotaDeviceStatusType] = None
    MulticastDeviceStatus: Optional[str] = None
    McGroupId: Optional[int] = None

class GetDeviceProfileResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    Id: str
    LoRaWAN: LoRaWANDeviceProfileOutputTypeDef
    Sidewalk: SidewalkGetDeviceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LoRaWANDeviceOutputTypeDef(BaseModel):
    DevEui: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    OtaaV1_1: Optional[OtaaV11TypeDef] = None
    OtaaV1_0_x: Optional[OtaaV10XTypeDef] = None
    AbpV1_1: Optional[AbpV11TypeDef] = None
    AbpV1_0_x: Optional[AbpV10XTypeDef] = None
    FPorts: Optional[FPortsOutputTypeDef] = None

class LoRaWANDeviceTypeDef(BaseModel):
    DevEui: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    OtaaV1_1: Optional[OtaaV11TypeDef] = None
    OtaaV1_0_x: Optional[OtaaV10XTypeDef] = None
    AbpV1_1: Optional[AbpV11TypeDef] = None
    AbpV1_0_x: Optional[AbpV10XTypeDef] = None
    FPorts: Optional[FPortsTypeDef] = None

class LoRaWANUpdateDeviceTypeDef(BaseModel):
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    AbpV1_1: Optional[UpdateAbpV11TypeDef] = None
    AbpV1_0_x: Optional[UpdateAbpV10XTypeDef] = None
    FPorts: Optional[UpdateFPortsTypeDef] = None

class LoRaWANSendDataToDeviceOutputTypeDef(BaseModel):
    FPort: Optional[int] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysOutputTypeDef] = None

class LoRaWANSendDataToDeviceTypeDef(BaseModel):
    FPort: Optional[int] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysTypeDef] = None

class StartMulticastGroupSessionRequestRequestTypeDef(BaseModel):
    Id: str
    LoRaWAN: LoRaWANMulticastSessionTypeDef

class StartFuotaTaskRequestRequestTypeDef(BaseModel):
    Id: str
    LoRaWAN: Optional[LoRaWANStartFuotaTaskTypeDef] = None

class GetMetricsRequestRequestTypeDef(BaseModel):
    SummaryMetricQueries: Optional[Sequence[SummaryMetricQueryTypeDef]] = None

class ListWirelessDeviceImportTasksResponseTypeDef(BaseModel):
    WirelessDeviceImportTaskList: List[WirelessDeviceImportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GsmObjTypeDef(BaseModel):
    Mcc: int
    Mnc: int
    Lac: int
    GeranCid: int
    GsmLocalId: Optional[GsmLocalIdTypeDef] = None
    GsmTimingAdvance: Optional[int] = None
    RxLevel: Optional[int] = None
    GsmNmr: Optional[Sequence[GsmNmrObjTypeDef]] = None

class ListDevicesForWirelessDeviceImportTaskResponseTypeDef(BaseModel):
    DestinationName: str
    ImportedWirelessDeviceList: List[ImportedWirelessDeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EventNotificationItemConfigurationsTypeDef(BaseModel):
    DeviceRegistrationState: Optional[DeviceRegistrationStateEventConfigurationTypeDef] = None
    Proximity: Optional[ProximityEventConfigurationTypeDef] = None
    Join: Optional[JoinEventConfigurationTypeDef] = None
    ConnectionStatus: Optional[ConnectionStatusEventConfigurationTypeDef] = None
    MessageDeliveryStatus: Optional[MessageDeliveryStatusEventConfigurationTypeDef] = None

class GetResourceEventConfigurationResponseTypeDef(BaseModel):
    DeviceRegistrationState: DeviceRegistrationStateEventConfigurationTypeDef
    Proximity: ProximityEventConfigurationTypeDef
    Join: JoinEventConfigurationTypeDef
    ConnectionStatus: ConnectionStatusEventConfigurationTypeDef
    MessageDeliveryStatus: MessageDeliveryStatusEventConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourceEventConfigurationRequestRequestTypeDef(BaseModel):
    Identifier: str
    IdentifierType: IdentifierTypeType
    PartnerType: Optional[Literal["Sidewalk"]] = None
    DeviceRegistrationState: Optional[DeviceRegistrationStateEventConfigurationTypeDef] = None
    Proximity: Optional[ProximityEventConfigurationTypeDef] = None
    Join: Optional[JoinEventConfigurationTypeDef] = None
    ConnectionStatus: Optional[ConnectionStatusEventConfigurationTypeDef] = None
    MessageDeliveryStatus: Optional[MessageDeliveryStatusEventConfigurationTypeDef] = None

class GetEventConfigurationByResourceTypesResponseTypeDef(BaseModel):
    DeviceRegistrationState: DeviceRegistrationStateResourceTypeEventConfigurationTypeDef
    Proximity: ProximityResourceTypeEventConfigurationTypeDef
    Join: JoinResourceTypeEventConfigurationTypeDef
    ConnectionStatus: ConnectionStatusResourceTypeEventConfigurationTypeDef
    MessageDeliveryStatus: MessageDeliveryStatusResourceTypeEventConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventConfigurationByResourceTypesRequestRequestTypeDef(BaseModel):
    DeviceRegistrationState: Optional[       DeviceRegistrationStateResourceTypeEventConfigurationTypeDef     ] = None
    Proximity: Optional[ProximityResourceTypeEventConfigurationTypeDef] = None
    Join: Optional[JoinResourceTypeEventConfigurationTypeDef] = None
    ConnectionStatus: Optional[ConnectionStatusResourceTypeEventConfigurationTypeDef] = None
    MessageDeliveryStatus: Optional[       MessageDeliveryStatusResourceTypeEventConfigurationTypeDef     ] = None

class GetWirelessDeviceStatisticsResponseTypeDef(BaseModel):
    WirelessDeviceId: str
    LastUplinkReceivedAt: str
    LoRaWAN: LoRaWANDeviceMetadataTypeDef
    Sidewalk: SidewalkDeviceMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWirelessGatewayFirmwareInformationResponseTypeDef(BaseModel):
    LoRaWAN: LoRaWANGatewayCurrentVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWirelessGatewayTaskCreateTypeDef(BaseModel):
    UpdateDataSource: Optional[str] = None
    UpdateDataRole: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateGatewayTaskCreateTypeDef] = None

class UpdateWirelessGatewayTaskEntryTypeDef(BaseModel):
    Id: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateGatewayTaskEntryTypeDef] = None
    Arn: Optional[str] = None

class SendDataToMulticastGroupRequestRequestTypeDef(BaseModel):
    Id: str
    PayloadData: str
    WirelessMetadata: MulticastWirelessMetadataTypeDef

class GetMetricsResponseTypeDef(BaseModel):
    SummaryMetricQueryResults: List[SummaryMetricQueryResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPositionConfigurationRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    Solvers: Optional[PositionSolverConfigurationsTypeDef] = None
    Destination: Optional[str] = None

class GetPositionConfigurationResponseTypeDef(BaseModel):
    Solvers: PositionSolverDetailsTypeDef
    Destination: str
    ResponseMetadata: ResponseMetadataTypeDef

class PositionConfigurationItemTypeDef(BaseModel):
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[PositionResourceTypeType] = None
    Solvers: Optional[PositionSolverDetailsTypeDef] = None
    Destination: Optional[str] = None

class GetLogLevelsByResourceTypesResponseTypeDef(BaseModel):
    DefaultLogLevel: LogLevelType
    WirelessGatewayLogOptions: List[WirelessGatewayLogOptionOutputTypeDef]
    WirelessDeviceLogOptions: List[WirelessDeviceLogOptionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWirelessGatewaysResponseTypeDef(BaseModel):
    WirelessGatewayList: List[WirelessGatewayStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListWirelessDevicesResponseTypeDef(BaseModel):
    WirelessDeviceList: List[WirelessDeviceStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetWirelessDeviceResponseTypeDef(BaseModel):
    Type: WirelessDeviceTypeType
    Name: str
    Description: str
    DestinationName: str
    Id: str
    Arn: str
    ThingName: str
    ThingArn: str
    LoRaWAN: LoRaWANDeviceOutputTypeDef
    Sidewalk: SidewalkDeviceTypeDef
    Positioning: PositioningConfigStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWirelessDeviceRequestRequestTypeDef(BaseModel):
    Type: WirelessDeviceTypeType
    DestinationName: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    LoRaWAN: Optional[LoRaWANDeviceTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Positioning: Optional[PositioningConfigStatusType] = None
    Sidewalk: Optional[SidewalkCreateWirelessDeviceTypeDef] = None

class UpdateWirelessDeviceRequestRequestTypeDef(BaseModel):
    Id: str
    DestinationName: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateDeviceTypeDef] = None
    Positioning: Optional[PositioningConfigStatusType] = None

class DownlinkQueueMessageTypeDef(BaseModel):
    MessageId: Optional[str] = None
    TransmitMode: Optional[int] = None
    ReceivedAt: Optional[str] = None
    LoRaWAN: Optional[LoRaWANSendDataToDeviceOutputTypeDef] = None

class WirelessMetadataTypeDef(BaseModel):
    LoRaWAN: Optional[LoRaWANSendDataToDeviceTypeDef] = None
    Sidewalk: Optional[SidewalkSendDataToDeviceTypeDef] = None

class CellTowersTypeDef(BaseModel):
    Gsm: Optional[Sequence[GsmObjTypeDef]] = None
    Wcdma: Optional[Sequence[WcdmaObjTypeDef]] = None
    Tdscdma: Optional[Sequence[TdscdmaObjTypeDef]] = None
    Lte: Optional[Sequence[LteObjTypeDef]] = None
    Cdma: Optional[Sequence[CdmaObjTypeDef]] = None

class EventConfigurationItemTypeDef(BaseModel):
    Identifier: Optional[str] = None
    IdentifierType: Optional[IdentifierTypeType] = None
    PartnerType: Optional[Literal["Sidewalk"]] = None
    Events: Optional[EventNotificationItemConfigurationsTypeDef] = None

class CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef(BaseModel):
    AutoCreateTasks: bool
    Name: Optional[str] = None
    Update: Optional[UpdateWirelessGatewayTaskCreateTypeDef] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetWirelessGatewayTaskDefinitionResponseTypeDef(BaseModel):
    AutoCreateTasks: bool
    Name: str
    Update: UpdateWirelessGatewayTaskCreateTypeDef
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWirelessGatewayTaskDefinitionsResponseTypeDef(BaseModel):
    TaskDefinitions: List[UpdateWirelessGatewayTaskEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPositionConfigurationsResponseTypeDef(BaseModel):
    PositionConfigurationList: List[PositionConfigurationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateLogLevelsByResourceTypesRequestRequestTypeDef(BaseModel):
    DefaultLogLevel: Optional[LogLevelType] = None
    WirelessDeviceLogOptions: Optional[Sequence[WirelessDeviceLogOptionUnionTypeDef]] = None
    WirelessGatewayLogOptions: Optional[Sequence[WirelessGatewayLogOptionUnionTypeDef]] = None

class ListQueuedMessagesResponseTypeDef(BaseModel):
    DownlinkQueueMessagesList: List[DownlinkQueueMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SendDataToWirelessDeviceRequestRequestTypeDef(BaseModel):
    Id: str
    TransmitMode: int
    PayloadData: str
    WirelessMetadata: Optional[WirelessMetadataTypeDef] = None

class GetPositionEstimateRequestRequestTypeDef(BaseModel):
    WiFiAccessPoints: Optional[Sequence[WiFiAccessPointTypeDef]] = None
    CellTowers: Optional[CellTowersTypeDef] = None
    Ip: Optional[IpTypeDef] = None
    Gnss: Optional[GnssTypeDef] = None
    Timestamp: Optional[TimestampTypeDef] = None

class ListEventConfigurationsResponseTypeDef(BaseModel):
    EventConfigurationsList: List[EventConfigurationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


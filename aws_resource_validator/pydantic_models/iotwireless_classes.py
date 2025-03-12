from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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

class SessionKeysAbpV10XTypeDef(BaseValidatorModel):
    NwkSKey: Optional[str] = None
    AppSKey: Optional[str] = None


class SessionKeysAbpV11TypeDef(BaseValidatorModel):
    FNwkSIntKey: Optional[str] = None
    SNwkSIntKey: Optional[str] = None
    NwkSEncKey: Optional[str] = None
    AppSKey: Optional[str] = None


class AccuracyTypeDef(BaseValidatorModel):
    HorizontalAccuracy: Optional[float] = None
    VerticalAccuracy: Optional[float] = None


class SidewalkAccountInfoTypeDef(BaseValidatorModel):
    AmazonId: Optional[str] = None
    AppServerPrivateKey: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateMulticastGroupWithFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    MulticastGroupId: str


class AssociateWirelessDeviceWithFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    WirelessDeviceId: str


class AssociateWirelessDeviceWithMulticastGroupRequestTypeDef(BaseValidatorModel):
    Id: str
    WirelessDeviceId: str


class AssociateWirelessDeviceWithThingRequestTypeDef(BaseValidatorModel):
    Id: str
    ThingArn: str


class AssociateWirelessGatewayWithCertificateRequestTypeDef(BaseValidatorModel):
    Id: str
    IotCertificateId: str


class AssociateWirelessGatewayWithThingRequestTypeDef(BaseValidatorModel):
    Id: str
    ThingArn: str


class BeaconingOutputTypeDef(BaseValidatorModel):
    DataRate: Optional[int] = None
    Frequencies: Optional[List[int]] = None


class BeaconingTypeDef(BaseValidatorModel):
    DataRate: Optional[int] = None
    Frequencies: Optional[Sequence[int]] = None


class CancelMulticastGroupSessionRequestTypeDef(BaseValidatorModel):
    Id: str


class CdmaLocalIdTypeDef(BaseValidatorModel):
    PnOffset: int
    CdmaChannel: int


class CdmaNmrObjTypeDef(BaseValidatorModel):
    PnOffset: int
    CdmaChannel: int
    PilotPower: Optional[int] = None
    BaseStationId: Optional[int] = None


class CertificateListTypeDef(BaseValidatorModel):
    SigningAlg: SigningAlgType
    Value: str


class LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef(BaseValidatorModel):
    GatewayEuiEventTopic: Optional[EventNotificationTopicStatusType] = None


class LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef(BaseValidatorModel):
    WirelessGatewayEventTopic: Optional[EventNotificationTopicStatusType] = None


class LoRaWANFuotaTaskTypeDef(BaseValidatorModel):
    RfRegion: Optional[SupportedRfRegionType] = None


class TraceContentTypeDef(BaseValidatorModel):
    WirelessDeviceFrameInfo: Optional[WirelessDeviceFrameInfoType] = None
    LogLevel: Optional[LogLevelType] = None
    MulticastFrameInfo: Optional[MulticastFrameInfoType] = None


class LoRaWANServiceProfileTypeDef(BaseValidatorModel):
    AddGwMetadata: Optional[bool] = None
    DrMin: Optional[int] = None
    DrMax: Optional[int] = None
    PrAllowed: Optional[bool] = None
    RaAllowed: Optional[bool] = None


class SidewalkCreateWirelessDeviceTypeDef(BaseValidatorModel):
    DeviceProfileId: Optional[str] = None


class CreateWirelessGatewayTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    WirelessGatewayTaskDefinitionId: str


class DakCertificateMetadataTypeDef(BaseValidatorModel):
    CertificateId: str
    MaxAllowedSignature: Optional[int] = None
    FactorySupport: Optional[bool] = None
    ApId: Optional[str] = None
    DeviceTypeId: Optional[str] = None


class DeleteDestinationRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteDeviceProfileRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteMulticastGroupRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteNetworkAnalyzerConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigurationName: str


class DeleteQueuedMessagesRequestTypeDef(BaseValidatorModel):
    Id: str
    MessageId: str
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None


class DeleteServiceProfileRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteWirelessDeviceImportTaskRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteWirelessDeviceRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteWirelessGatewayRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteWirelessGatewayTaskDefinitionRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteWirelessGatewayTaskRequestTypeDef(BaseValidatorModel):
    Id: str


class DeregisterWirelessDeviceRequestTypeDef(BaseValidatorModel):
    Identifier: str
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None


class DestinationsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ExpressionType: Optional[ExpressionTypeType] = None
    Expression: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None


class DeviceProfileTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Id: Optional[str] = None


class SidewalkEventNotificationConfigurationsTypeDef(BaseValidatorModel):
    AmazonIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class SidewalkResourceTypeEventConfigurationTypeDef(BaseValidatorModel):
    WirelessDeviceEventTopic: Optional[EventNotificationTopicStatusType] = None


class DimensionTypeDef(BaseValidatorModel):
    name: Optional[DimensionNameType] = None
    value: Optional[str] = None


class DisassociateAwsAccountFromPartnerAccountRequestTypeDef(BaseValidatorModel):
    PartnerAccountId: str
    PartnerType: Literal["Sidewalk"]


class DisassociateMulticastGroupFromFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    MulticastGroupId: str


class DisassociateWirelessDeviceFromFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    WirelessDeviceId: str


class DisassociateWirelessDeviceFromMulticastGroupRequestTypeDef(BaseValidatorModel):
    Id: str
    WirelessDeviceId: str


class DisassociateWirelessDeviceFromThingRequestTypeDef(BaseValidatorModel):
    Id: str


class DisassociateWirelessGatewayFromCertificateRequestTypeDef(BaseValidatorModel):
    Id: str


class DisassociateWirelessGatewayFromThingRequestTypeDef(BaseValidatorModel):
    Id: str


class PositioningTypeDef(BaseValidatorModel):
    ClockSync: Optional[int] = None
    Stream: Optional[int] = None
    Gnss: Optional[int] = None


class FuotaTaskEventLogOptionTypeDef(BaseValidatorModel):
    Event: Literal["Fuota"]
    LogLevel: LogLevelType


class FuotaTaskTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None


class GatewayListItemTypeDef(BaseValidatorModel):
    GatewayId: str
    DownlinkFrequency: int


class GetDestinationRequestTypeDef(BaseValidatorModel):
    Name: str


class GetDeviceProfileRequestTypeDef(BaseValidatorModel):
    Id: str


class LoRaWANDeviceProfileOutputTypeDef(BaseValidatorModel):
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


class GetFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str


class LoRaWANFuotaTaskGetInfoTypeDef(BaseValidatorModel):
    RfRegion: Optional[str] = None
    StartTime: Optional[datetime] = None


class SummaryMetricConfigurationTypeDef(BaseValidatorModel):
    Status: Optional[SummaryMetricConfigurationStatusType] = None


class GetMulticastGroupRequestTypeDef(BaseValidatorModel):
    Id: str


class GetMulticastGroupSessionRequestTypeDef(BaseValidatorModel):
    Id: str


class LoRaWANMulticastSessionOutputTypeDef(BaseValidatorModel):
    DlDr: Optional[int] = None
    DlFreq: Optional[int] = None
    SessionStartTime: Optional[datetime] = None
    SessionTimeout: Optional[int] = None
    PingSlotPeriod: Optional[int] = None


class GetNetworkAnalyzerConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigurationName: str


class GetPartnerAccountRequestTypeDef(BaseValidatorModel):
    PartnerAccountId: str
    PartnerType: Literal["Sidewalk"]


class SidewalkAccountInfoWithFingerprintTypeDef(BaseValidatorModel):
    AmazonId: Optional[str] = None
    Fingerprint: Optional[str] = None
    Arn: Optional[str] = None


class GetPositionConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType


class GnssTypeDef(BaseValidatorModel):
    Payload: str
    CaptureTime: Optional[float] = None
    CaptureTimeAccuracy: Optional[float] = None
    AssistPosition: Optional[Sequence[float]] = None
    AssistAltitude: Optional[float] = None
    Use2DSolver: Optional[bool] = None


class IpTypeDef(BaseValidatorModel):
    IpAddress: str


class WiFiAccessPointTypeDef(BaseValidatorModel):
    MacAddress: str
    Rss: int


class GetPositionRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType


class GetResourceEventConfigurationRequestTypeDef(BaseValidatorModel):
    Identifier: str
    IdentifierType: IdentifierTypeType
    PartnerType: Optional[Literal["Sidewalk"]] = None


class GetResourceLogLevelRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: str


class GetResourcePositionRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType


class GetServiceEndpointRequestTypeDef(BaseValidatorModel):
    ServiceType: Optional[WirelessGatewayServiceTypeType] = None


class GetServiceProfileRequestTypeDef(BaseValidatorModel):
    Id: str


class LoRaWANGetServiceProfileInfoTypeDef(BaseValidatorModel):
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


class GetWirelessDeviceImportTaskRequestTypeDef(BaseValidatorModel):
    Id: str


class SidewalkGetStartImportInfoTypeDef(BaseValidatorModel):
    DeviceCreationFileList: Optional[List[str]] = None
    Role: Optional[str] = None


class GetWirelessDeviceRequestTypeDef(BaseValidatorModel):
    Identifier: str
    IdentifierType: WirelessDeviceIdTypeType


class GetWirelessDeviceStatisticsRequestTypeDef(BaseValidatorModel):
    WirelessDeviceId: str


class SidewalkDeviceMetadataTypeDef(BaseValidatorModel):
    Rssi: Optional[int] = None
    BatteryLevel: Optional[BatteryLevelType] = None
    Event: Optional[EventType] = None
    DeviceState: Optional[DeviceStateType] = None


class GetWirelessGatewayCertificateRequestTypeDef(BaseValidatorModel):
    Id: str


class GetWirelessGatewayFirmwareInformationRequestTypeDef(BaseValidatorModel):
    Id: str


class GetWirelessGatewayRequestTypeDef(BaseValidatorModel):
    Identifier: str
    IdentifierType: WirelessGatewayIdTypeType


class GetWirelessGatewayStatisticsRequestTypeDef(BaseValidatorModel):
    WirelessGatewayId: str


class GetWirelessGatewayTaskDefinitionRequestTypeDef(BaseValidatorModel):
    Id: str


class GetWirelessGatewayTaskRequestTypeDef(BaseValidatorModel):
    Id: str


class GlobalIdentityTypeDef(BaseValidatorModel):
    Lac: int
    GeranCid: int


class GsmLocalIdTypeDef(BaseValidatorModel):
    Bsic: int
    Bcch: int


class ImportedSidewalkDeviceTypeDef(BaseValidatorModel):
    SidewalkManufacturingSn: Optional[str] = None
    OnboardingStatus: Optional[OnboardStatusType] = None
    OnboardingStatusReason: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None


class LoRaWANJoinEventNotificationConfigurationsTypeDef(BaseValidatorModel):
    DevEuiEventTopic: Optional[EventNotificationTopicStatusType] = None


class LoRaWANJoinResourceTypeEventConfigurationTypeDef(BaseValidatorModel):
    WirelessDeviceEventTopic: Optional[EventNotificationTopicStatusType] = None


class ListDestinationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDeviceProfilesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DeviceProfileType: Optional[DeviceProfileTypeType] = None


class ListDevicesForWirelessDeviceImportTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[OnboardStatusType] = None


class ListEventConfigurationsRequestTypeDef(BaseValidatorModel):
    ResourceType: EventNotificationResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFuotaTasksRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMulticastGroupsByFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MulticastGroupByFuotaTaskTypeDef(BaseValidatorModel):
    Id: Optional[str] = None


class ListMulticastGroupsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MulticastGroupTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None


class ListNetworkAnalyzerConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NetworkAnalyzerConfigurationsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class ListPartnerAccountsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPositionConfigurationsRequestTypeDef(BaseValidatorModel):
    ResourceType: Optional[PositionResourceTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListQueuedMessagesRequestTypeDef(BaseValidatorModel):
    Id: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None


class ListServiceProfilesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ServiceProfileTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Id: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListWirelessDeviceImportTasksRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListWirelessDevicesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DestinationName: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    WirelessDeviceType: Optional[WirelessDeviceTypeType] = None
    FuotaTaskId: Optional[str] = None
    MulticastGroupId: Optional[str] = None


class ListWirelessGatewayTaskDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    TaskDefinitionType: Optional[Literal["UPDATE"]] = None


class ListWirelessGatewaysRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class LoRaWANGatewayMetadataTypeDef(BaseValidatorModel):
    GatewayEui: Optional[str] = None
    Snr: Optional[float] = None
    Rssi: Optional[float] = None


class LoRaWANPublicGatewayMetadataTypeDef(BaseValidatorModel):
    ProviderNetId: Optional[str] = None
    Id: Optional[str] = None
    Rssi: Optional[float] = None
    Snr: Optional[float] = None
    RfRegion: Optional[str] = None
    DlAllowed: Optional[bool] = None


class OtaaV10XTypeDef(BaseValidatorModel):
    AppKey: Optional[str] = None
    AppEui: Optional[str] = None
    JoinEui: Optional[str] = None
    GenAppKey: Optional[str] = None


class OtaaV11TypeDef(BaseValidatorModel):
    AppKey: Optional[str] = None
    NwkKey: Optional[str] = None
    JoinEui: Optional[str] = None


class LoRaWANDeviceProfileTypeDef(BaseValidatorModel):
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


class LoRaWANGatewayVersionTypeDef(BaseValidatorModel):
    PackageVersion: Optional[str] = None
    Model: Optional[str] = None
    Station: Optional[str] = None


class LoRaWANListDeviceTypeDef(BaseValidatorModel):
    DevEui: Optional[str] = None


class ParticipatingGatewaysMulticastOutputTypeDef(BaseValidatorModel):
    GatewayList: Optional[List[str]] = None
    TransmissionInterval: Optional[int] = None


class LoRaWANMulticastMetadataTypeDef(BaseValidatorModel):
    FPort: Optional[int] = None


class UpdateAbpV10XTypeDef(BaseValidatorModel):
    FCntStart: Optional[int] = None


class UpdateAbpV11TypeDef(BaseValidatorModel):
    FCntStart: Optional[int] = None


class LteLocalIdTypeDef(BaseValidatorModel):
    Pci: int
    Earfcn: int


class LteNmrObjTypeDef(BaseValidatorModel):
    Pci: int
    Earfcn: int
    EutranCid: int
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None


class MetricQueryValueTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None
    Sum: Optional[float] = None
    Avg: Optional[float] = None
    Std: Optional[float] = None
    P90: Optional[float] = None


class ParticipatingGatewaysMulticastTypeDef(BaseValidatorModel):
    GatewayList: Optional[Sequence[str]] = None
    TransmissionInterval: Optional[int] = None


class SemtechGnssConfigurationTypeDef(BaseValidatorModel):
    Status: PositionConfigurationStatusType
    Fec: PositionConfigurationFecType


class PutResourceLogLevelRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: str
    LogLevel: LogLevelType


class ResetResourceLogLevelRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: str


class SidewalkSendDataToDeviceTypeDef(BaseValidatorModel):
    Seq: Optional[int] = None
    MessageType: Optional[MessageTypeType] = None
    AckModeRetryDurationSecs: Optional[int] = None


class SidewalkSingleStartImportInfoTypeDef(BaseValidatorModel):
    SidewalkManufacturingSn: Optional[str] = None


class SidewalkStartImportInfoTypeDef(BaseValidatorModel):
    DeviceCreationFile: Optional[str] = None
    Role: Optional[str] = None


class SidewalkUpdateAccountTypeDef(BaseValidatorModel):
    AppServerPrivateKey: Optional[str] = None


class SidewalkUpdateImportInfoTypeDef(BaseValidatorModel):
    DeviceCreationFile: Optional[str] = None


class TdscdmaLocalIdTypeDef(BaseValidatorModel):
    Uarfcn: int
    CellParams: int


class TdscdmaNmrObjTypeDef(BaseValidatorModel):
    Uarfcn: int
    CellParams: int
    UtranCid: Optional[int] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None


class TestWirelessDeviceRequestTypeDef(BaseValidatorModel):
    Id: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateDestinationRequestTypeDef(BaseValidatorModel):
    Name: str
    ExpressionType: Optional[ExpressionTypeType] = None
    Expression: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None


class UpdatePositionRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    Position: Sequence[float]


class UpdateWirelessGatewayRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    JoinEuiFilters: Optional[Sequence[Sequence[str]]] = None
    NetIdFilters: Optional[Sequence[str]] = None
    MaxEirp: Optional[float] = None


class WcdmaLocalIdTypeDef(BaseValidatorModel):
    Uarfcndl: int
    Psc: int


class WcdmaNmrObjTypeDef(BaseValidatorModel):
    Uarfcndl: int
    Psc: int
    UtranCid: int
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None


class WirelessDeviceEventLogOptionTypeDef(BaseValidatorModel):
    Event: WirelessDeviceEventType
    LogLevel: LogLevelType


class WirelessGatewayEventLogOptionTypeDef(BaseValidatorModel):
    Event: WirelessGatewayEventType
    LogLevel: LogLevelType


class AbpV10XTypeDef(BaseValidatorModel):
    DevAddr: Optional[str] = None
    SessionKeys: Optional[SessionKeysAbpV10XTypeDef] = None
    FCntStart: Optional[int] = None


class AbpV11TypeDef(BaseValidatorModel):
    DevAddr: Optional[str] = None
    SessionKeys: Optional[SessionKeysAbpV11TypeDef] = None
    FCntStart: Optional[int] = None


class AssociateAwsAccountWithPartnerAccountRequestTypeDef(BaseValidatorModel):
    Sidewalk: SidewalkAccountInfoTypeDef
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateDestinationRequestTypeDef(BaseValidatorModel):
    Name: str
    ExpressionType: ExpressionTypeType
    Expression: str
    RoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None


class StartBulkAssociateWirelessDeviceWithMulticastGroupRequestTypeDef(BaseValidatorModel):
    Id: str
    QueryString: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestTypeDef(BaseValidatorModel):
    Id: str
    QueryString: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class AssociateAwsAccountWithPartnerAccountResponseTypeDef(BaseValidatorModel):
    Sidewalk: SidewalkAccountInfoTypeDef
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateWirelessGatewayWithCertificateResponseTypeDef(BaseValidatorModel):
    IotCertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDestinationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDeviceProfileResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFuotaTaskResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMulticastGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateNetworkAnalyzerConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateServiceProfileResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWirelessDeviceResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWirelessGatewayResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWirelessGatewayTaskDefinitionResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWirelessGatewayTaskResponseTypeDef(BaseValidatorModel):
    WirelessGatewayTaskDefinitionId: str
    Status: WirelessGatewayTaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetDestinationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Expression: str
    ExpressionType: ExpressionTypeType
    Description: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPositionEstimateResponseTypeDef(BaseValidatorModel):
    GeoJsonPayload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetPositionResponseTypeDef(BaseValidatorModel):
    Position: List[float]
    Accuracy: AccuracyTypeDef
    SolverType: Literal["GNSS"]
    SolverProvider: Literal["Semtech"]
    SolverVersion: str
    Timestamp: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceLogLevelResponseTypeDef(BaseValidatorModel):
    LogLevel: LogLevelType
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePositionResponseTypeDef(BaseValidatorModel):
    GeoJsonPayload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetServiceEndpointResponseTypeDef(BaseValidatorModel):
    ServiceType: WirelessGatewayServiceTypeType
    ServiceEndpoint: str
    ServerTrust: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetWirelessGatewayCertificateResponseTypeDef(BaseValidatorModel):
    IotCertificateId: str
    LoRaWANNetworkServerCertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetWirelessGatewayStatisticsResponseTypeDef(BaseValidatorModel):
    WirelessGatewayId: str
    LastUplinkReceivedAt: str
    ConnectionStatus: ConnectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetWirelessGatewayTaskResponseTypeDef(BaseValidatorModel):
    WirelessGatewayId: str
    WirelessGatewayTaskDefinitionId: str
    LastUplinkReceivedAt: str
    TaskCreatedAt: str
    Status: WirelessGatewayTaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SendDataToMulticastGroupResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendDataToWirelessDeviceResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartSingleWirelessDeviceImportTaskResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartWirelessDeviceImportTaskResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class TestWirelessDeviceResponseTypeDef(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef


class LoRaWANGatewayOutputTypeDef(BaseValidatorModel):
    GatewayEui: Optional[str] = None
    RfRegion: Optional[str] = None
    JoinEuiFilters: Optional[List[List[str]]] = None
    NetIdFilters: Optional[List[str]] = None
    SubBands: Optional[List[int]] = None
    Beaconing: Optional[BeaconingOutputTypeDef] = None
    MaxEirp: Optional[float] = None


class LoRaWANGatewayTypeDef(BaseValidatorModel):
    GatewayEui: Optional[str] = None
    RfRegion: Optional[str] = None
    JoinEuiFilters: Optional[Sequence[Sequence[str]]] = None
    NetIdFilters: Optional[Sequence[str]] = None
    SubBands: Optional[Sequence[int]] = None
    Beaconing: Optional[BeaconingTypeDef] = None
    MaxEirp: Optional[float] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class UpdateResourcePositionRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    GeoJsonPayload: Optional[BlobTypeDef] = None


class CdmaObjTypeDef(BaseValidatorModel):
    SystemId: int
    NetworkId: int
    BaseStationId: int
    RegistrationZone: Optional[int] = None
    CdmaLocalId: Optional[CdmaLocalIdTypeDef] = None
    PilotPower: Optional[int] = None
    BaseLat: Optional[float] = None
    BaseLng: Optional[float] = None
    CdmaNmr: Optional[Sequence[CdmaNmrObjTypeDef]] = None


class SidewalkDeviceTypeDef(BaseValidatorModel):
    AmazonId: Optional[str] = None
    SidewalkId: Optional[str] = None
    SidewalkManufacturingSn: Optional[str] = None
    DeviceCertificates: Optional[List[CertificateListTypeDef]] = None
    PrivateKeys: Optional[List[CertificateListTypeDef]] = None
    DeviceProfileId: Optional[str] = None
    CertificateId: Optional[str] = None
    Status: Optional[WirelessDeviceSidewalkStatusType] = None


class SidewalkListDeviceTypeDef(BaseValidatorModel):
    AmazonId: Optional[str] = None
    SidewalkId: Optional[str] = None
    SidewalkManufacturingSn: Optional[str] = None
    DeviceCertificates: Optional[List[CertificateListTypeDef]] = None
    DeviceProfileId: Optional[str] = None
    Status: Optional[WirelessDeviceSidewalkStatusType] = None


class ConnectionStatusEventConfigurationTypeDef(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef] = None
    WirelessGatewayIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class ConnectionStatusResourceTypeEventConfigurationTypeDef(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef] = None


class CreateFuotaTaskRequestTypeDef(BaseValidatorModel):
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
    Descriptor: Optional[str] = None


class UpdateFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANFuotaTaskTypeDef] = None
    FirmwareUpdateImage: Optional[str] = None
    FirmwareUpdateRole: Optional[str] = None
    RedundancyPercent: Optional[int] = None
    FragmentSizeBytes: Optional[int] = None
    FragmentIntervalMS: Optional[int] = None
    Descriptor: Optional[str] = None


class CreateNetworkAnalyzerConfigurationRequestTypeDef(BaseValidatorModel):
    Name: str
    TraceContent: Optional[TraceContentTypeDef] = None
    WirelessDevices: Optional[Sequence[str]] = None
    WirelessGateways: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None
    MulticastGroups: Optional[Sequence[str]] = None


class GetNetworkAnalyzerConfigurationResponseTypeDef(BaseValidatorModel):
    TraceContent: TraceContentTypeDef
    WirelessDevices: List[str]
    WirelessGateways: List[str]
    Description: str
    Arn: str
    Name: str
    MulticastGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNetworkAnalyzerConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigurationName: str
    TraceContent: Optional[TraceContentTypeDef] = None
    WirelessDevicesToAdd: Optional[Sequence[str]] = None
    WirelessDevicesToRemove: Optional[Sequence[str]] = None
    WirelessGatewaysToAdd: Optional[Sequence[str]] = None
    WirelessGatewaysToRemove: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    MulticastGroupsToAdd: Optional[Sequence[str]] = None
    MulticastGroupsToRemove: Optional[Sequence[str]] = None


class CreateServiceProfileRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    LoRaWAN: Optional[LoRaWANServiceProfileTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None


class SidewalkGetDeviceProfileTypeDef(BaseValidatorModel):
    ApplicationServerPublicKey: Optional[str] = None
    QualificationStatus: Optional[bool] = None
    DakCertificateMetadata: Optional[List[DakCertificateMetadataTypeDef]] = None


class ListDestinationsResponseTypeDef(BaseValidatorModel):
    DestinationList: List[DestinationsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDeviceProfilesResponseTypeDef(BaseValidatorModel):
    DeviceProfileList: List[DeviceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DeviceRegistrationStateEventConfigurationTypeDef(BaseValidatorModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurationsTypeDef] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class MessageDeliveryStatusEventConfigurationTypeDef(BaseValidatorModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurationsTypeDef] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class ProximityEventConfigurationTypeDef(BaseValidatorModel):
    Sidewalk: Optional[SidewalkEventNotificationConfigurationsTypeDef] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class DeviceRegistrationStateResourceTypeEventConfigurationTypeDef(BaseValidatorModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfigurationTypeDef] = None


class MessageDeliveryStatusResourceTypeEventConfigurationTypeDef(BaseValidatorModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfigurationTypeDef] = None


class ProximityResourceTypeEventConfigurationTypeDef(BaseValidatorModel):
    Sidewalk: Optional[SidewalkResourceTypeEventConfigurationTypeDef] = None


class ApplicationConfigTypeDef(BaseValidatorModel):
    pass


class FPortsOutputTypeDef(BaseValidatorModel):
    Fuota: Optional[int] = None
    Multicast: Optional[int] = None
    ClockSync: Optional[int] = None
    Positioning: Optional[PositioningTypeDef] = None
    Applications: Optional[List[ApplicationConfigTypeDef]] = None


class FPortsTypeDef(BaseValidatorModel):
    Fuota: Optional[int] = None
    Multicast: Optional[int] = None
    ClockSync: Optional[int] = None
    Positioning: Optional[PositioningTypeDef] = None
    Applications: Optional[Sequence[ApplicationConfigTypeDef]] = None


class UpdateFPortsTypeDef(BaseValidatorModel):
    Positioning: Optional[PositioningTypeDef] = None
    Applications: Optional[Sequence[ApplicationConfigTypeDef]] = None


class ListFuotaTasksResponseTypeDef(BaseValidatorModel):
    FuotaTaskList: List[FuotaTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ParticipatingGatewaysOutputTypeDef(BaseValidatorModel):
    DownlinkMode: DownlinkModeType
    GatewayList: List[GatewayListItemTypeDef]
    TransmissionInterval: int


class ParticipatingGatewaysTypeDef(BaseValidatorModel):
    DownlinkMode: DownlinkModeType
    GatewayList: Sequence[GatewayListItemTypeDef]
    TransmissionInterval: int


class GetFuotaTaskResponseTypeDef(BaseValidatorModel):
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
    Descriptor: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMetricConfigurationResponseTypeDef(BaseValidatorModel):
    SummaryMetric: SummaryMetricConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMetricConfigurationRequestTypeDef(BaseValidatorModel):
    SummaryMetric: Optional[SummaryMetricConfigurationTypeDef] = None


class GetMulticastGroupSessionResponseTypeDef(BaseValidatorModel):
    LoRaWAN: LoRaWANMulticastSessionOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPartnerAccountResponseTypeDef(BaseValidatorModel):
    Sidewalk: SidewalkAccountInfoWithFingerprintTypeDef
    AccountLinked: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ListPartnerAccountsResponseTypeDef(BaseValidatorModel):
    Sidewalk: List[SidewalkAccountInfoWithFingerprintTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class LoRaWANMulticastSessionTypeDef(BaseValidatorModel):
    DlDr: Optional[int] = None
    DlFreq: Optional[int] = None
    SessionStartTime: Optional[TimestampTypeDef] = None
    SessionTimeout: Optional[int] = None
    PingSlotPeriod: Optional[int] = None


class LoRaWANStartFuotaTaskTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None


class SummaryMetricQueryTypeDef(BaseValidatorModel):
    QueryId: Optional[str] = None
    MetricName: Optional[MetricNameType] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    StartTimestamp: Optional[TimestampTypeDef] = None
    EndTimestamp: Optional[TimestampTypeDef] = None


class GetServiceProfileResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Id: str
    LoRaWAN: LoRaWANGetServiceProfileInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetWirelessDeviceImportTaskResponseTypeDef(BaseValidatorModel):
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


class WirelessDeviceImportTaskTypeDef(BaseValidatorModel):
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


class GsmNmrObjTypeDef(BaseValidatorModel):
    Bsic: int
    Bcch: int
    RxLevel: Optional[int] = None
    GlobalIdentity: Optional[GlobalIdentityTypeDef] = None


class ImportedWirelessDeviceTypeDef(BaseValidatorModel):
    Sidewalk: Optional[ImportedSidewalkDeviceTypeDef] = None


class JoinEventConfigurationTypeDef(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANJoinEventNotificationConfigurationsTypeDef] = None
    WirelessDeviceIdEventTopic: Optional[EventNotificationTopicStatusType] = None


class JoinResourceTypeEventConfigurationTypeDef(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANJoinResourceTypeEventConfigurationTypeDef] = None


class ListMulticastGroupsByFuotaTaskResponseTypeDef(BaseValidatorModel):
    MulticastGroupList: List[MulticastGroupByFuotaTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMulticastGroupsResponseTypeDef(BaseValidatorModel):
    MulticastGroupList: List[MulticastGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListNetworkAnalyzerConfigurationsResponseTypeDef(BaseValidatorModel):
    NetworkAnalyzerConfigurationList: List[NetworkAnalyzerConfigurationsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListServiceProfilesResponseTypeDef(BaseValidatorModel):
    ServiceProfileList: List[ServiceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LoRaWANDeviceMetadataTypeDef(BaseValidatorModel):
    DevEui: Optional[str] = None
    FPort: Optional[int] = None
    DataRate: Optional[int] = None
    Frequency: Optional[int] = None
    Timestamp: Optional[str] = None
    Gateways: Optional[List[LoRaWANGatewayMetadataTypeDef]] = None
    PublicGateways: Optional[List[LoRaWANPublicGatewayMetadataTypeDef]] = None


class LoRaWANGatewayCurrentVersionTypeDef(BaseValidatorModel):
    CurrentVersion: Optional[LoRaWANGatewayVersionTypeDef] = None


class LoRaWANUpdateGatewayTaskCreateTypeDef(BaseValidatorModel):
    UpdateSignature: Optional[str] = None
    SigKeyCrc: Optional[int] = None
    CurrentVersion: Optional[LoRaWANGatewayVersionTypeDef] = None
    UpdateVersion: Optional[LoRaWANGatewayVersionTypeDef] = None


class LoRaWANUpdateGatewayTaskEntryTypeDef(BaseValidatorModel):
    CurrentVersion: Optional[LoRaWANGatewayVersionTypeDef] = None
    UpdateVersion: Optional[LoRaWANGatewayVersionTypeDef] = None


class LoRaWANMulticastGetTypeDef(BaseValidatorModel):
    RfRegion: Optional[SupportedRfRegionType] = None
    DlClass: Optional[DlClassType] = None
    NumberOfDevicesRequested: Optional[int] = None
    NumberOfDevicesInGroup: Optional[int] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysMulticastOutputTypeDef] = None


class MulticastWirelessMetadataTypeDef(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANMulticastMetadataTypeDef] = None


class LteObjTypeDef(BaseValidatorModel):
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


class SummaryMetricQueryResultTypeDef(BaseValidatorModel):
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


class PositionSolverConfigurationsTypeDef(BaseValidatorModel):
    SemtechGnss: Optional[SemtechGnssConfigurationTypeDef] = None


class SemtechGnssDetailTypeDef(BaseValidatorModel):
    pass


class PositionSolverDetailsTypeDef(BaseValidatorModel):
    SemtechGnss: Optional[SemtechGnssDetailTypeDef] = None


class StartSingleWirelessDeviceImportTaskRequestTypeDef(BaseValidatorModel):
    DestinationName: str
    Sidewalk: SidewalkSingleStartImportInfoTypeDef
    ClientRequestToken: Optional[str] = None
    DeviceName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartWirelessDeviceImportTaskRequestTypeDef(BaseValidatorModel):
    DestinationName: str
    Sidewalk: SidewalkStartImportInfoTypeDef
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdatePartnerAccountRequestTypeDef(BaseValidatorModel):
    Sidewalk: SidewalkUpdateAccountTypeDef
    PartnerAccountId: str
    PartnerType: Literal["Sidewalk"]


class UpdateWirelessDeviceImportTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    Sidewalk: SidewalkUpdateImportInfoTypeDef


class TdscdmaObjTypeDef(BaseValidatorModel):
    Mcc: int
    Mnc: int
    UtranCid: int
    Lac: Optional[int] = None
    TdscdmaLocalId: Optional[TdscdmaLocalIdTypeDef] = None
    TdscdmaTimingAdvance: Optional[int] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None
    TdscdmaNmr: Optional[Sequence[TdscdmaNmrObjTypeDef]] = None


class WcdmaObjTypeDef(BaseValidatorModel):
    Mcc: int
    Mnc: int
    UtranCid: int
    Lac: Optional[int] = None
    WcdmaLocalId: Optional[WcdmaLocalIdTypeDef] = None
    Rscp: Optional[int] = None
    PathLoss: Optional[int] = None
    WcdmaNmr: Optional[Sequence[WcdmaNmrObjTypeDef]] = None


class GetWirelessGatewayResponseTypeDef(BaseValidatorModel):
    Name: str
    Id: str
    Description: str
    LoRaWAN: LoRaWANGatewayOutputTypeDef
    Arn: str
    ThingName: str
    ThingArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class WirelessGatewayStatisticsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANGatewayOutputTypeDef] = None
    LastUplinkReceivedAt: Optional[str] = None


class GetDeviceProfileResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Id: str
    LoRaWAN: LoRaWANDeviceProfileOutputTypeDef
    Sidewalk: SidewalkGetDeviceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoRaWANDeviceOutputTypeDef(BaseValidatorModel):
    DevEui: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    OtaaV1_1: Optional[OtaaV11TypeDef] = None
    OtaaV1_0_x: Optional[OtaaV10XTypeDef] = None
    AbpV1_1: Optional[AbpV11TypeDef] = None
    AbpV1_0_x: Optional[AbpV10XTypeDef] = None
    FPorts: Optional[FPortsOutputTypeDef] = None


class LoRaWANDeviceTypeDef(BaseValidatorModel):
    DevEui: Optional[str] = None
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    OtaaV1_1: Optional[OtaaV11TypeDef] = None
    OtaaV1_0_x: Optional[OtaaV10XTypeDef] = None
    AbpV1_1: Optional[AbpV11TypeDef] = None
    AbpV1_0_x: Optional[AbpV10XTypeDef] = None
    FPorts: Optional[FPortsTypeDef] = None


class LoRaWANUpdateDeviceTypeDef(BaseValidatorModel):
    DeviceProfileId: Optional[str] = None
    ServiceProfileId: Optional[str] = None
    AbpV1_1: Optional[UpdateAbpV11TypeDef] = None
    AbpV1_0_x: Optional[UpdateAbpV10XTypeDef] = None
    FPorts: Optional[UpdateFPortsTypeDef] = None


class LoRaWANSendDataToDeviceOutputTypeDef(BaseValidatorModel):
    FPort: Optional[int] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysOutputTypeDef] = None


class StartFuotaTaskRequestTypeDef(BaseValidatorModel):
    Id: str
    LoRaWAN: Optional[LoRaWANStartFuotaTaskTypeDef] = None


class GetMetricsRequestTypeDef(BaseValidatorModel):
    SummaryMetricQueries: Optional[Sequence[SummaryMetricQueryTypeDef]] = None


class ListWirelessDeviceImportTasksResponseTypeDef(BaseValidatorModel):
    WirelessDeviceImportTaskList: List[WirelessDeviceImportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GsmObjTypeDef(BaseValidatorModel):
    Mcc: int
    Mnc: int
    Lac: int
    GeranCid: int
    GsmLocalId: Optional[GsmLocalIdTypeDef] = None
    GsmTimingAdvance: Optional[int] = None
    RxLevel: Optional[int] = None
    GsmNmr: Optional[Sequence[GsmNmrObjTypeDef]] = None


class ListDevicesForWirelessDeviceImportTaskResponseTypeDef(BaseValidatorModel):
    DestinationName: str
    ImportedWirelessDeviceList: List[ImportedWirelessDeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EventNotificationItemConfigurationsTypeDef(BaseValidatorModel):
    DeviceRegistrationState: Optional[DeviceRegistrationStateEventConfigurationTypeDef] = None
    Proximity: Optional[ProximityEventConfigurationTypeDef] = None
    Join: Optional[JoinEventConfigurationTypeDef] = None
    ConnectionStatus: Optional[ConnectionStatusEventConfigurationTypeDef] = None
    MessageDeliveryStatus: Optional[MessageDeliveryStatusEventConfigurationTypeDef] = None


class GetResourceEventConfigurationResponseTypeDef(BaseValidatorModel):
    DeviceRegistrationState: DeviceRegistrationStateEventConfigurationTypeDef
    Proximity: ProximityEventConfigurationTypeDef
    Join: JoinEventConfigurationTypeDef
    ConnectionStatus: ConnectionStatusEventConfigurationTypeDef
    MessageDeliveryStatus: MessageDeliveryStatusEventConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateResourceEventConfigurationRequestTypeDef(BaseValidatorModel):
    Identifier: str
    IdentifierType: IdentifierTypeType
    PartnerType: Optional[Literal["Sidewalk"]] = None
    DeviceRegistrationState: Optional[DeviceRegistrationStateEventConfigurationTypeDef] = None
    Proximity: Optional[ProximityEventConfigurationTypeDef] = None
    Join: Optional[JoinEventConfigurationTypeDef] = None
    ConnectionStatus: Optional[ConnectionStatusEventConfigurationTypeDef] = None
    MessageDeliveryStatus: Optional[MessageDeliveryStatusEventConfigurationTypeDef] = None


class GetEventConfigurationByResourceTypesResponseTypeDef(BaseValidatorModel):
    DeviceRegistrationState: DeviceRegistrationStateResourceTypeEventConfigurationTypeDef
    Proximity: ProximityResourceTypeEventConfigurationTypeDef
    Join: JoinResourceTypeEventConfigurationTypeDef
    ConnectionStatus: ConnectionStatusResourceTypeEventConfigurationTypeDef
    MessageDeliveryStatus: MessageDeliveryStatusResourceTypeEventConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEventConfigurationByResourceTypesRequestTypeDef(BaseValidatorModel):
    DeviceRegistrationState: Optional[ DeviceRegistrationStateResourceTypeEventConfigurationTypeDef ] = None
    Proximity: Optional[ProximityResourceTypeEventConfigurationTypeDef] = None
    Join: Optional[JoinResourceTypeEventConfigurationTypeDef] = None
    ConnectionStatus: Optional[ConnectionStatusResourceTypeEventConfigurationTypeDef] = None
    MessageDeliveryStatus: Optional[MessageDeliveryStatusResourceTypeEventConfigurationTypeDef] = None


class GetWirelessDeviceStatisticsResponseTypeDef(BaseValidatorModel):
    WirelessDeviceId: str
    LastUplinkReceivedAt: str
    LoRaWAN: LoRaWANDeviceMetadataTypeDef
    Sidewalk: SidewalkDeviceMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoRaWANDeviceProfileUnionTypeDef(BaseValidatorModel):
    pass


class CreateDeviceProfileRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    LoRaWAN: Optional[LoRaWANDeviceProfileUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None
    Sidewalk: Optional[Mapping[str, Any]] = None


class GetWirelessGatewayFirmwareInformationResponseTypeDef(BaseValidatorModel):
    LoRaWAN: LoRaWANGatewayCurrentVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWirelessGatewayTaskCreateTypeDef(BaseValidatorModel):
    UpdateDataSource: Optional[str] = None
    UpdateDataRole: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateGatewayTaskCreateTypeDef] = None


class UpdateWirelessGatewayTaskEntryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateGatewayTaskEntryTypeDef] = None
    Arn: Optional[str] = None


class GetMulticastGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    Status: str
    LoRaWAN: LoRaWANMulticastGetTypeDef
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class SendDataToMulticastGroupRequestTypeDef(BaseValidatorModel):
    Id: str
    PayloadData: str
    WirelessMetadata: MulticastWirelessMetadataTypeDef


class GetMetricsResponseTypeDef(BaseValidatorModel):
    SummaryMetricQueryResults: List[SummaryMetricQueryResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ParticipatingGatewaysMulticastUnionTypeDef(BaseValidatorModel):
    pass


class LoRaWANMulticastTypeDef(BaseValidatorModel):
    RfRegion: Optional[SupportedRfRegionType] = None
    DlClass: Optional[DlClassType] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysMulticastUnionTypeDef] = None


class PutPositionConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ResourceType: PositionResourceTypeType
    Solvers: Optional[PositionSolverConfigurationsTypeDef] = None
    Destination: Optional[str] = None


class GetPositionConfigurationResponseTypeDef(BaseValidatorModel):
    Solvers: PositionSolverDetailsTypeDef
    Destination: str
    ResponseMetadata: ResponseMetadataTypeDef


class PositionConfigurationItemTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[PositionResourceTypeType] = None
    Solvers: Optional[PositionSolverDetailsTypeDef] = None
    Destination: Optional[str] = None


class WirelessGatewayLogOptionOutputTypeDef(BaseValidatorModel):
    pass


class WirelessDeviceLogOptionOutputTypeDef(BaseValidatorModel):
    pass


class FuotaTaskLogOptionOutputTypeDef(BaseValidatorModel):
    pass


class GetLogLevelsByResourceTypesResponseTypeDef(BaseValidatorModel):
    DefaultLogLevel: LogLevelType
    WirelessGatewayLogOptions: List[WirelessGatewayLogOptionOutputTypeDef]
    WirelessDeviceLogOptions: List[WirelessDeviceLogOptionOutputTypeDef]
    FuotaTaskLogOptions: List[FuotaTaskLogOptionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListWirelessGatewaysResponseTypeDef(BaseValidatorModel):
    WirelessGatewayList: List[WirelessGatewayStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LoRaWANGatewayUnionTypeDef(BaseValidatorModel):
    pass


class CreateWirelessGatewayRequestTypeDef(BaseValidatorModel):
    LoRaWAN: LoRaWANGatewayUnionTypeDef
    Name: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None


class WirelessDeviceStatisticsTypeDef(BaseValidatorModel):
    pass


class ListWirelessDevicesResponseTypeDef(BaseValidatorModel):
    WirelessDeviceList: List[WirelessDeviceStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateWirelessDeviceRequestTypeDef(BaseValidatorModel):
    Id: str
    DestinationName: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANUpdateDeviceTypeDef] = None
    Positioning: Optional[PositioningConfigStatusType] = None


class DownlinkQueueMessageTypeDef(BaseValidatorModel):
    MessageId: Optional[str] = None
    TransmitMode: Optional[int] = None
    ReceivedAt: Optional[str] = None
    LoRaWAN: Optional[LoRaWANSendDataToDeviceOutputTypeDef] = None


class ParticipatingGatewaysUnionTypeDef(BaseValidatorModel):
    pass


class LoRaWANSendDataToDeviceTypeDef(BaseValidatorModel):
    FPort: Optional[int] = None
    ParticipatingGateways: Optional[ParticipatingGatewaysUnionTypeDef] = None


class LoRaWANMulticastSessionUnionTypeDef(BaseValidatorModel):
    pass


class StartMulticastGroupSessionRequestTypeDef(BaseValidatorModel):
    Id: str
    LoRaWAN: LoRaWANMulticastSessionUnionTypeDef


class CellTowersTypeDef(BaseValidatorModel):
    Gsm: Optional[Sequence[GsmObjTypeDef]] = None
    Wcdma: Optional[Sequence[WcdmaObjTypeDef]] = None
    Tdscdma: Optional[Sequence[TdscdmaObjTypeDef]] = None
    Lte: Optional[Sequence[LteObjTypeDef]] = None
    Cdma: Optional[Sequence[CdmaObjTypeDef]] = None


class EventConfigurationItemTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    IdentifierType: Optional[IdentifierTypeType] = None
    PartnerType: Optional[Literal["Sidewalk"]] = None
    Events: Optional[EventNotificationItemConfigurationsTypeDef] = None


class CreateWirelessGatewayTaskDefinitionRequestTypeDef(BaseValidatorModel):
    AutoCreateTasks: bool
    Name: Optional[str] = None
    Update: Optional[UpdateWirelessGatewayTaskCreateTypeDef] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class GetWirelessGatewayTaskDefinitionResponseTypeDef(BaseValidatorModel):
    AutoCreateTasks: bool
    Name: str
    Update: UpdateWirelessGatewayTaskCreateTypeDef
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListWirelessGatewayTaskDefinitionsResponseTypeDef(BaseValidatorModel):
    TaskDefinitions: List[UpdateWirelessGatewayTaskEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateMulticastGroupRequestTypeDef(BaseValidatorModel):
    LoRaWAN: LoRaWANMulticastTypeDef
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateMulticastGroupRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoRaWAN: Optional[LoRaWANMulticastTypeDef] = None


class ListPositionConfigurationsResponseTypeDef(BaseValidatorModel):
    PositionConfigurationList: List[PositionConfigurationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FuotaTaskLogOptionUnionTypeDef(BaseValidatorModel):
    pass


class WirelessDeviceLogOptionUnionTypeDef(BaseValidatorModel):
    pass


class WirelessGatewayLogOptionUnionTypeDef(BaseValidatorModel):
    pass


class UpdateLogLevelsByResourceTypesRequestTypeDef(BaseValidatorModel):
    DefaultLogLevel: Optional[LogLevelType] = None
    FuotaTaskLogOptions: Optional[Sequence[FuotaTaskLogOptionUnionTypeDef]] = None
    WirelessDeviceLogOptions: Optional[Sequence[WirelessDeviceLogOptionUnionTypeDef]] = None
    WirelessGatewayLogOptions: Optional[Sequence[WirelessGatewayLogOptionUnionTypeDef]] = None


class ListQueuedMessagesResponseTypeDef(BaseValidatorModel):
    DownlinkQueueMessagesList: List[DownlinkQueueMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetPositionEstimateRequestTypeDef(BaseValidatorModel):
    WiFiAccessPoints: Optional[Sequence[WiFiAccessPointTypeDef]] = None
    CellTowers: Optional[CellTowersTypeDef] = None
    Ip: Optional[IpTypeDef] = None
    Gnss: Optional[GnssTypeDef] = None
    Timestamp: Optional[TimestampTypeDef] = None


class ListEventConfigurationsResponseTypeDef(BaseValidatorModel):
    EventConfigurationsList: List[EventConfigurationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LoRaWANSendDataToDeviceUnionTypeDef(BaseValidatorModel):
    pass


class WirelessMetadataTypeDef(BaseValidatorModel):
    LoRaWAN: Optional[LoRaWANSendDataToDeviceUnionTypeDef] = None
    Sidewalk: Optional[SidewalkSendDataToDeviceTypeDef] = None


class SendDataToWirelessDeviceRequestTypeDef(BaseValidatorModel):
    Id: str
    TransmitMode: int
    PayloadData: str
    WirelessMetadata: Optional[WirelessMetadataTypeDef] = None



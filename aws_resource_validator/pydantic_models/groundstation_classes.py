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
from aws_resource_validator.pydantic_models.groundstation_constants import *

class ComponentVersionTypeDef(BaseModel):
    componentType: str
    versions: Sequence[str]

class AggregateStatusTypeDef(BaseModel):
    status: AgentStatusType
    signatureMap: Optional[Mapping[str, bool]] = None

class AntennaDemodDecodeDetailsTypeDef(BaseModel):
    outputNode: Optional[str] = None

class DecodeConfigTypeDef(BaseModel):
    unvalidatedJSON: str

class DemodulationConfigTypeDef(BaseModel):
    unvalidatedJSON: str

class EirpTypeDef(BaseModel):
    units: Literal["dBW"]
    value: float

class CancelContactRequestRequestTypeDef(BaseModel):
    contactId: str

class ComponentStatusDataTypeDef(BaseModel):
    capabilityArn: str
    componentType: str
    dataflowId: str
    status: AgentStatusType
    bytesReceived: Optional[int] = None
    bytesSent: Optional[int] = None
    packetsDropped: Optional[int] = None

class S3RecordingDetailsTypeDef(BaseModel):
    bucketArn: Optional[str] = None
    keyTemplate: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConfigListItemTypeDef(BaseModel):
    configArn: Optional[str] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    name: Optional[str] = None

class DataflowEndpointConfigTypeDef(BaseModel):
    dataflowEndpointName: str
    dataflowEndpointRegion: Optional[str] = None

class S3RecordingConfigTypeDef(BaseModel):
    bucketArn: str
    roleArn: str
    prefix: Optional[str] = None

class TrackingConfigTypeDef(BaseModel):
    autotrack: CriticalityType

class UplinkEchoConfigTypeDef(BaseModel):
    antennaUplinkConfigArn: str
    enabled: bool

class SocketAddressTypeDef(BaseModel):
    name: str
    port: int

class ElevationTypeDef(BaseModel):
    unit: AngleUnitsType
    value: float

class KmsKeyTypeDef(BaseModel):
    kmsAliasArn: Optional[str] = None
    kmsAliasName: Optional[str] = None
    kmsKeyArn: Optional[str] = None

class DataflowEndpointListItemTypeDef(BaseModel):
    dataflowEndpointGroupArn: Optional[str] = None
    dataflowEndpointGroupId: Optional[str] = None

class DeleteConfigRequestRequestTypeDef(BaseModel):
    configId: str
    configType: ConfigCapabilityTypeType

class DeleteDataflowEndpointGroupRequestRequestTypeDef(BaseModel):
    dataflowEndpointGroupId: str

class DeleteEphemerisRequestRequestTypeDef(BaseModel):
    ephemerisId: str

class DeleteMissionProfileRequestRequestTypeDef(BaseModel):
    missionProfileId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeContactRequestRequestTypeDef(BaseModel):
    contactId: str

class DescribeEphemerisRequestRequestTypeDef(BaseModel):
    ephemerisId: str

class DiscoveryDataTypeDef(BaseModel):
    capabilityArns: Sequence[str]
    privateIpAddresses: Sequence[str]
    publicIpAddresses: Sequence[str]

class SecurityDetailsOutputTypeDef(BaseModel):
    roleArn: str
    securityGroupIds: List[str]
    subnetIds: List[str]

class SecurityDetailsTypeDef(BaseModel):
    roleArn: str
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]

class S3ObjectTypeDef(BaseModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    version: Optional[str] = None

class EphemerisMetaDataTypeDef(BaseModel):
    source: EphemerisSourceType
    ephemerisId: Optional[str] = None
    epoch: Optional[datetime] = None
    name: Optional[str] = None

class FrequencyBandwidthTypeDef(BaseModel):
    units: BandwidthUnitsType
    value: float

class FrequencyTypeDef(BaseModel):
    units: FrequencyUnitsType
    value: float

class GetAgentConfigurationRequestRequestTypeDef(BaseModel):
    agentId: str

class GetConfigRequestRequestTypeDef(BaseModel):
    configId: str
    configType: ConfigCapabilityTypeType

class GetDataflowEndpointGroupRequestRequestTypeDef(BaseModel):
    dataflowEndpointGroupId: str

class GetMinuteUsageRequestRequestTypeDef(BaseModel):
    month: int
    year: int

class GetMissionProfileRequestRequestTypeDef(BaseModel):
    missionProfileId: str

class GetSatelliteRequestRequestTypeDef(BaseModel):
    satelliteId: str

class GroundStationDataTypeDef(BaseModel):
    groundStationId: Optional[str] = None
    groundStationName: Optional[str] = None
    region: Optional[str] = None

class IntegerRangeTypeDef(BaseModel):
    maximum: int
    minimum: int

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListConfigsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataflowEndpointGroupsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListGroundStationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    satelliteId: Optional[str] = None

class ListMissionProfilesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MissionProfileListItemTypeDef(BaseModel):
    missionProfileArn: Optional[str] = None
    missionProfileId: Optional[str] = None
    name: Optional[str] = None
    region: Optional[str] = None

class ListSatellitesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateEphemerisRequestRequestTypeDef(BaseModel):
    enabled: bool
    ephemerisId: str
    name: Optional[str] = None
    priority: Optional[int] = None

class AgentDetailsTypeDef(BaseModel):
    agentVersion: str
    componentVersions: Sequence[ComponentVersionTypeDef]
    instanceId: str
    instanceType: str
    agentCpuCores: Optional[Sequence[int]] = None
    reservedCpuCores: Optional[Sequence[int]] = None

class UpdateAgentStatusRequestRequestTypeDef(BaseModel):
    agentId: str
    aggregateStatus: AggregateStatusTypeDef
    componentStatuses: Sequence[ComponentStatusDataTypeDef]
    taskId: str

class ConfigIdResponseTypeDef(BaseModel):
    configArn: str
    configId: str
    configType: ConfigCapabilityTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ContactIdResponseTypeDef(BaseModel):
    contactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataflowEndpointGroupIdResponseTypeDef(BaseModel):
    dataflowEndpointGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EphemerisIdResponseTypeDef(BaseModel):
    ephemerisId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentConfigurationResponseTypeDef(BaseModel):
    agentId: str
    taskingDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMinuteUsageResponseTypeDef(BaseModel):
    estimatedMinutesRemaining: int
    isReservedMinutesCustomer: bool
    totalReservedMinuteAllocation: int
    totalScheduledMinutes: int
    upcomingMinutesScheduled: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MissionProfileIdResponseTypeDef(BaseModel):
    missionProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterAgentResponseTypeDef(BaseModel):
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentStatusResponseTypeDef(BaseModel):
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigsResponseTypeDef(BaseModel):
    configList: List[ConfigListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionDetailsTypeDef(BaseModel):
    socketAddress: SocketAddressTypeDef
    mtu: Optional[int] = None

class DataflowEndpointTypeDef(BaseModel):
    address: Optional[SocketAddressTypeDef] = None
    mtu: Optional[int] = None
    name: Optional[str] = None
    status: Optional[EndpointStatusType] = None

class ContactDataTypeDef(BaseModel):
    contactId: Optional[str] = None
    contactStatus: Optional[ContactStatusType] = None
    endTime: Optional[datetime] = None
    errorMessage: Optional[str] = None
    groundStation: Optional[str] = None
    maximumElevation: Optional[ElevationTypeDef] = None
    missionProfileArn: Optional[str] = None
    postPassEndTime: Optional[datetime] = None
    prePassStartTime: Optional[datetime] = None
    region: Optional[str] = None
    satelliteArn: Optional[str] = None
    startTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    visibilityEndTime: Optional[datetime] = None
    visibilityStartTime: Optional[datetime] = None

class ListContactsRequestRequestTypeDef(BaseModel):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef
    statusList: Sequence[ContactStatusType]
    groundStation: Optional[str] = None
    maxResults: Optional[int] = None
    missionProfileArn: Optional[str] = None
    nextToken: Optional[str] = None
    satelliteArn: Optional[str] = None

class ListEphemeridesRequestRequestTypeDef(BaseModel):
    endTime: TimestampTypeDef
    satelliteId: str
    startTime: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    statusList: Optional[Sequence[EphemerisStatusType]] = None

class ReserveContactRequestRequestTypeDef(BaseModel):
    endTime: TimestampTypeDef
    groundStation: str
    missionProfileArn: str
    satelliteArn: str
    startTime: TimestampTypeDef
    tags: Optional[Mapping[str, str]] = None

class TimeRangeTypeDef(BaseModel):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef

class CreateMissionProfileRequestRequestTypeDef(BaseModel):
    dataflowEdges: Sequence[Sequence[str]]
    minimumViableContactDurationSeconds: int
    name: str
    trackingConfigArn: str
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    streamsKmsKey: Optional[KmsKeyTypeDef] = None
    streamsKmsRole: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetMissionProfileResponseTypeDef(BaseModel):
    contactPostPassDurationSeconds: int
    contactPrePassDurationSeconds: int
    dataflowEdges: List[List[str]]
    minimumViableContactDurationSeconds: int
    missionProfileArn: str
    missionProfileId: str
    name: str
    region: str
    streamsKmsKey: KmsKeyTypeDef
    streamsKmsRole: str
    tags: Dict[str, str]
    trackingConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMissionProfileRequestRequestTypeDef(BaseModel):
    missionProfileId: str
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    dataflowEdges: Optional[Sequence[Sequence[str]]] = None
    minimumViableContactDurationSeconds: Optional[int] = None
    name: Optional[str] = None
    streamsKmsKey: Optional[KmsKeyTypeDef] = None
    streamsKmsRole: Optional[str] = None
    trackingConfigArn: Optional[str] = None

class ListDataflowEndpointGroupsResponseTypeDef(BaseModel):
    dataflowEndpointGroupList: List[DataflowEndpointListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContactRequestContactScheduledWaitTypeDef(BaseModel):
    contactId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class EphemerisDescriptionTypeDef(BaseModel):
    ephemerisData: Optional[str] = None
    sourceS3Object: Optional[S3ObjectTypeDef] = None

class EphemerisItemTypeDef(BaseModel):
    creationTime: Optional[datetime] = None
    enabled: Optional[bool] = None
    ephemerisId: Optional[str] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    sourceS3Object: Optional[S3ObjectTypeDef] = None
    status: Optional[EphemerisStatusType] = None

class OEMEphemerisTypeDef(BaseModel):
    oemData: Optional[str] = None
    s3Object: Optional[S3ObjectTypeDef] = None

class GetSatelliteResponseTypeDef(BaseModel):
    currentEphemeris: EphemerisMetaDataTypeDef
    groundStations: List[str]
    noradSatelliteID: int
    satelliteArn: str
    satelliteId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SatelliteListItemTypeDef(BaseModel):
    currentEphemeris: Optional[EphemerisMetaDataTypeDef] = None
    groundStations: Optional[List[str]] = None
    noradSatelliteID: Optional[int] = None
    satelliteArn: Optional[str] = None
    satelliteId: Optional[str] = None

class SpectrumConfigTypeDef(BaseModel):
    bandwidth: FrequencyBandwidthTypeDef
    centerFrequency: FrequencyTypeDef
    polarization: Optional[PolarizationType] = None

class UplinkSpectrumConfigTypeDef(BaseModel):
    centerFrequency: FrequencyTypeDef
    polarization: Optional[PolarizationType] = None

class ListGroundStationsResponseTypeDef(BaseModel):
    groundStationList: List[GroundStationDataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RangedSocketAddressTypeDef(BaseModel):
    name: str
    portRange: IntegerRangeTypeDef

class ListConfigsRequestListConfigsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactsRequestListContactsPaginateTypeDef(BaseModel):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef
    statusList: Sequence[ContactStatusType]
    groundStation: Optional[str] = None
    missionProfileArn: Optional[str] = None
    satelliteArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEphemeridesRequestListEphemeridesPaginateTypeDef(BaseModel):
    endTime: TimestampTypeDef
    satelliteId: str
    startTime: TimestampTypeDef
    statusList: Optional[Sequence[EphemerisStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroundStationsRequestListGroundStationsPaginateTypeDef(BaseModel):
    satelliteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMissionProfilesRequestListMissionProfilesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSatellitesRequestListSatellitesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMissionProfilesResponseTypeDef(BaseModel):
    missionProfileList: List[MissionProfileListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterAgentRequestRequestTypeDef(BaseModel):
    agentDetails: AgentDetailsTypeDef
    discoveryData: DiscoveryDataTypeDef

class ListContactsResponseTypeDef(BaseModel):
    contactList: List[ContactDataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TLEDataTypeDef(BaseModel):
    tleLine1: str
    tleLine2: str
    validTimeRange: TimeRangeTypeDef

class EphemerisTypeDescriptionTypeDef(BaseModel):
    oem: Optional[EphemerisDescriptionTypeDef] = None
    tle: Optional[EphemerisDescriptionTypeDef] = None

class ListEphemeridesResponseTypeDef(BaseModel):
    ephemerides: List[EphemerisItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSatellitesResponseTypeDef(BaseModel):
    nextToken: str
    satellites: List[SatelliteListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AntennaDownlinkConfigTypeDef(BaseModel):
    spectrumConfig: SpectrumConfigTypeDef

class AntennaDownlinkDemodDecodeConfigTypeDef(BaseModel):
    decodeConfig: DecodeConfigTypeDef
    demodulationConfig: DemodulationConfigTypeDef
    spectrumConfig: SpectrumConfigTypeDef

class AntennaUplinkConfigTypeDef(BaseModel):
    spectrumConfig: UplinkSpectrumConfigTypeDef
    targetEirp: EirpTypeDef
    transmitDisabled: Optional[bool] = None

class RangedConnectionDetailsTypeDef(BaseModel):
    socketAddress: RangedSocketAddressTypeDef
    mtu: Optional[int] = None

class TLEEphemerisTypeDef(BaseModel):
    s3Object: Optional[S3ObjectTypeDef] = None
    tleData: Optional[Sequence[TLEDataTypeDef]] = None

class DescribeEphemerisResponseTypeDef(BaseModel):
    creationTime: datetime
    enabled: bool
    ephemerisId: str
    invalidReason: EphemerisInvalidReasonType
    name: str
    priority: int
    satelliteId: str
    status: EphemerisStatusType
    suppliedData: EphemerisTypeDescriptionTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigTypeDataTypeDef(BaseModel):
    antennaDownlinkConfig: Optional[AntennaDownlinkConfigTypeDef] = None
    antennaDownlinkDemodDecodeConfig: Optional[AntennaDownlinkDemodDecodeConfigTypeDef] = None
    antennaUplinkConfig: Optional[AntennaUplinkConfigTypeDef] = None
    dataflowEndpointConfig: Optional[DataflowEndpointConfigTypeDef] = None
    s3RecordingConfig: Optional[S3RecordingConfigTypeDef] = None
    trackingConfig: Optional[TrackingConfigTypeDef] = None
    uplinkEchoConfig: Optional[UplinkEchoConfigTypeDef] = None

class AwsGroundStationAgentEndpointTypeDef(BaseModel):
    egressAddress: ConnectionDetailsTypeDef
    ingressAddress: RangedConnectionDetailsTypeDef
    name: str
    agentStatus: Optional[AgentStatusType] = None
    auditResults: Optional[AuditResultsType] = None

class EphemerisDataTypeDef(BaseModel):
    oem: Optional[OEMEphemerisTypeDef] = None
    tle: Optional[TLEEphemerisTypeDef] = None

class CreateConfigRequestRequestTypeDef(BaseModel):
    configData: ConfigTypeDataTypeDef
    name: str
    tags: Optional[Mapping[str, str]] = None

class GetConfigResponseTypeDef(BaseModel):
    configArn: str
    configData: ConfigTypeDataTypeDef
    configId: str
    configType: ConfigCapabilityTypeType
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfigRequestRequestTypeDef(BaseModel):
    configData: ConfigTypeDataTypeDef
    configId: str
    configType: ConfigCapabilityTypeType
    name: str

class EndpointDetailsOutputTypeDef(BaseModel):
    awsGroundStationAgentEndpoint: Optional[AwsGroundStationAgentEndpointTypeDef] = None
    endpoint: Optional[DataflowEndpointTypeDef] = None
    healthReasons: Optional[List[CapabilityHealthReasonType]] = None
    healthStatus: Optional[CapabilityHealthType] = None
    securityDetails: Optional[SecurityDetailsOutputTypeDef] = None

class EndpointDetailsTypeDef(BaseModel):
    awsGroundStationAgentEndpoint: Optional[AwsGroundStationAgentEndpointTypeDef] = None
    endpoint: Optional[DataflowEndpointTypeDef] = None
    healthReasons: Optional[Sequence[CapabilityHealthReasonType]] = None
    healthStatus: Optional[CapabilityHealthType] = None
    securityDetails: Optional[SecurityDetailsTypeDef] = None

class CreateEphemerisRequestRequestTypeDef(BaseModel):
    name: str
    satelliteId: str
    enabled: Optional[bool] = None
    ephemeris: Optional[EphemerisDataTypeDef] = None
    expirationTime: Optional[TimestampTypeDef] = None
    kmsKeyArn: Optional[str] = None
    priority: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class ConfigDetailsTypeDef(BaseModel):
    antennaDemodDecodeDetails: Optional[AntennaDemodDecodeDetailsTypeDef] = None
    endpointDetails: Optional[EndpointDetailsOutputTypeDef] = None
    s3RecordingDetails: Optional[S3RecordingDetailsTypeDef] = None

class GetDataflowEndpointGroupResponseTypeDef(BaseModel):
    contactPostPassDurationSeconds: int
    contactPrePassDurationSeconds: int
    dataflowEndpointGroupArn: str
    dataflowEndpointGroupId: str
    endpointsDetails: List[EndpointDetailsOutputTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationTypeDef(BaseModel):
    configDetails: Optional[ConfigDetailsTypeDef] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    dataflowDestinationRegion: Optional[str] = None

class SourceTypeDef(BaseModel):
    configDetails: Optional[ConfigDetailsTypeDef] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    dataflowSourceRegion: Optional[str] = None

class CreateDataflowEndpointGroupRequestRequestTypeDef(BaseModel):
    endpointDetails: Sequence[EndpointDetailsUnionTypeDef]
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class DataflowDetailTypeDef(BaseModel):
    destination: Optional[DestinationTypeDef] = None
    errorMessage: Optional[str] = None
    source: Optional[SourceTypeDef] = None

class DescribeContactResponseTypeDef(BaseModel):
    contactId: str
    contactStatus: ContactStatusType
    dataflowList: List[DataflowDetailTypeDef]
    endTime: datetime
    errorMessage: str
    groundStation: str
    maximumElevation: ElevationTypeDef
    missionProfileArn: str
    postPassEndTime: datetime
    prePassStartTime: datetime
    region: str
    satelliteArn: str
    startTime: datetime
    tags: Dict[str, str]
    visibilityEndTime: datetime
    visibilityStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


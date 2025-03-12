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
from aws_resource_validator.pydantic_models.groundstation_constants import *

class ComponentVersionTypeDef(BaseValidatorModel):
    componentType: str
    versions: Sequence[str]


class AggregateStatusTypeDef(BaseValidatorModel):
    status: AgentStatusType
    signatureMap: Optional[Mapping[str, bool]] = None


class AntennaDemodDecodeDetailsTypeDef(BaseValidatorModel):
    outputNode: Optional[str] = None


class DecodeConfigTypeDef(BaseValidatorModel):
    unvalidatedJSON: str


class DemodulationConfigTypeDef(BaseValidatorModel):
    unvalidatedJSON: str


class EirpTypeDef(BaseValidatorModel):
    units: Literal["dBW"]
    value: float


class CancelContactRequestTypeDef(BaseValidatorModel):
    contactId: str


class ComponentStatusDataTypeDef(BaseValidatorModel):
    capabilityArn: str
    componentType: str
    dataflowId: str
    status: AgentStatusType
    bytesReceived: Optional[int] = None
    bytesSent: Optional[int] = None
    packetsDropped: Optional[int] = None


class S3RecordingDetailsTypeDef(BaseValidatorModel):
    bucketArn: Optional[str] = None
    keyTemplate: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ConfigListItemTypeDef(BaseValidatorModel):
    configArn: Optional[str] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    name: Optional[str] = None


class DataflowEndpointConfigTypeDef(BaseValidatorModel):
    dataflowEndpointName: str
    dataflowEndpointRegion: Optional[str] = None


class S3RecordingConfigTypeDef(BaseValidatorModel):
    bucketArn: str
    roleArn: str
    prefix: Optional[str] = None


class TrackingConfigTypeDef(BaseValidatorModel):
    autotrack: CriticalityType


class UplinkEchoConfigTypeDef(BaseValidatorModel):
    antennaUplinkConfigArn: str
    enabled: bool


class SocketAddressTypeDef(BaseValidatorModel):
    name: str
    port: int


class ElevationTypeDef(BaseValidatorModel):
    unit: AngleUnitsType
    value: float


class KmsKeyTypeDef(BaseValidatorModel):
    kmsAliasArn: Optional[str] = None
    kmsAliasName: Optional[str] = None
    kmsKeyArn: Optional[str] = None


class DataflowEndpointListItemTypeDef(BaseValidatorModel):
    dataflowEndpointGroupArn: Optional[str] = None
    dataflowEndpointGroupId: Optional[str] = None


class DeleteConfigRequestTypeDef(BaseValidatorModel):
    configId: str
    configType: ConfigCapabilityTypeType


class DeleteDataflowEndpointGroupRequestTypeDef(BaseValidatorModel):
    dataflowEndpointGroupId: str


class DeleteEphemerisRequestTypeDef(BaseValidatorModel):
    ephemerisId: str


class DeleteMissionProfileRequestTypeDef(BaseValidatorModel):
    missionProfileId: str


class DescribeContactRequestTypeDef(BaseValidatorModel):
    contactId: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeEphemerisRequestTypeDef(BaseValidatorModel):
    ephemerisId: str


class DiscoveryDataTypeDef(BaseValidatorModel):
    capabilityArns: Sequence[str]
    privateIpAddresses: Sequence[str]
    publicIpAddresses: Sequence[str]


class SecurityDetailsOutputTypeDef(BaseValidatorModel):
    roleArn: str
    securityGroupIds: List[str]
    subnetIds: List[str]


class S3ObjectTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    version: Optional[str] = None


class EphemerisMetaDataTypeDef(BaseValidatorModel):
    source: EphemerisSourceType
    ephemerisId: Optional[str] = None
    epoch: Optional[datetime] = None
    name: Optional[str] = None


class FrequencyBandwidthTypeDef(BaseValidatorModel):
    units: BandwidthUnitsType
    value: float


class FrequencyTypeDef(BaseValidatorModel):
    units: FrequencyUnitsType
    value: float


class GetAgentConfigurationRequestTypeDef(BaseValidatorModel):
    agentId: str


class GetConfigRequestTypeDef(BaseValidatorModel):
    configId: str
    configType: ConfigCapabilityTypeType


class GetDataflowEndpointGroupRequestTypeDef(BaseValidatorModel):
    dataflowEndpointGroupId: str


class GetMinuteUsageRequestTypeDef(BaseValidatorModel):
    month: int
    year: int


class GetMissionProfileRequestTypeDef(BaseValidatorModel):
    missionProfileId: str


class GetSatelliteRequestTypeDef(BaseValidatorModel):
    satelliteId: str


class GroundStationDataTypeDef(BaseValidatorModel):
    groundStationId: Optional[str] = None
    groundStationName: Optional[str] = None
    region: Optional[str] = None


class IntegerRangeTypeDef(BaseValidatorModel):
    maximum: int
    minimum: int


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListConfigsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataflowEndpointGroupsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListGroundStationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    satelliteId: Optional[str] = None


class ListMissionProfilesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MissionProfileListItemTypeDef(BaseValidatorModel):
    missionProfileArn: Optional[str] = None
    missionProfileId: Optional[str] = None
    name: Optional[str] = None
    region: Optional[str] = None


class ListSatellitesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class SecurityDetailsTypeDef(BaseValidatorModel):
    roleArn: str
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateEphemerisRequestTypeDef(BaseValidatorModel):
    enabled: bool
    ephemerisId: str
    name: Optional[str] = None
    priority: Optional[int] = None


class AgentDetailsTypeDef(BaseValidatorModel):
    agentVersion: str
    componentVersions: Sequence[ComponentVersionTypeDef]
    instanceId: str
    instanceType: str
    agentCpuCores: Optional[Sequence[int]] = None
    reservedCpuCores: Optional[Sequence[int]] = None


class UpdateAgentStatusRequestTypeDef(BaseValidatorModel):
    agentId: str
    aggregateStatus: AggregateStatusTypeDef
    componentStatuses: Sequence[ComponentStatusDataTypeDef]
    taskId: str


class ConfigIdResponseTypeDef(BaseValidatorModel):
    configArn: str
    configId: str
    configType: ConfigCapabilityTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class ContactIdResponseTypeDef(BaseValidatorModel):
    contactId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DataflowEndpointGroupIdResponseTypeDef(BaseValidatorModel):
    dataflowEndpointGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EphemerisIdResponseTypeDef(BaseValidatorModel):
    ephemerisId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAgentConfigurationResponseTypeDef(BaseValidatorModel):
    agentId: str
    taskingDocument: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMinuteUsageResponseTypeDef(BaseValidatorModel):
    estimatedMinutesRemaining: int
    isReservedMinutesCustomer: bool
    totalReservedMinuteAllocation: int
    totalScheduledMinutes: int
    upcomingMinutesScheduled: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class MissionProfileIdResponseTypeDef(BaseValidatorModel):
    missionProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterAgentResponseTypeDef(BaseValidatorModel):
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAgentStatusResponseTypeDef(BaseValidatorModel):
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigsResponseTypeDef(BaseValidatorModel):
    configList: List[ConfigListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConnectionDetailsTypeDef(BaseValidatorModel):
    socketAddress: SocketAddressTypeDef
    mtu: Optional[int] = None


class DataflowEndpointTypeDef(BaseValidatorModel):
    address: Optional[SocketAddressTypeDef] = None
    mtu: Optional[int] = None
    name: Optional[str] = None
    status: Optional[EndpointStatusType] = None


class ContactDataTypeDef(BaseValidatorModel):
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


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListContactsRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef
    statusList: Sequence[ContactStatusType]
    groundStation: Optional[str] = None
    maxResults: Optional[int] = None
    missionProfileArn: Optional[str] = None
    nextToken: Optional[str] = None
    satelliteArn: Optional[str] = None


class ListEphemeridesRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    satelliteId: str
    startTime: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    statusList: Optional[Sequence[EphemerisStatusType]] = None


class ReserveContactRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    groundStation: str
    missionProfileArn: str
    satelliteArn: str
    startTime: TimestampTypeDef
    tags: Optional[Mapping[str, str]] = None


class TimeRangeTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef


class CreateMissionProfileRequestTypeDef(BaseValidatorModel):
    dataflowEdges: Sequence[Sequence[str]]
    minimumViableContactDurationSeconds: int
    name: str
    trackingConfigArn: str
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    streamsKmsKey: Optional[KmsKeyTypeDef] = None
    streamsKmsRole: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class GetMissionProfileResponseTypeDef(BaseValidatorModel):
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


class UpdateMissionProfileRequestTypeDef(BaseValidatorModel):
    missionProfileId: str
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    dataflowEdges: Optional[Sequence[Sequence[str]]] = None
    minimumViableContactDurationSeconds: Optional[int] = None
    name: Optional[str] = None
    streamsKmsKey: Optional[KmsKeyTypeDef] = None
    streamsKmsRole: Optional[str] = None
    trackingConfigArn: Optional[str] = None


class ListDataflowEndpointGroupsResponseTypeDef(BaseValidatorModel):
    dataflowEndpointGroupList: List[DataflowEndpointListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeContactRequestWaitTypeDef(BaseValidatorModel):
    contactId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class EphemerisDescriptionTypeDef(BaseValidatorModel):
    ephemerisData: Optional[str] = None
    sourceS3Object: Optional[S3ObjectTypeDef] = None


class EphemerisItemTypeDef(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    enabled: Optional[bool] = None
    ephemerisId: Optional[str] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    sourceS3Object: Optional[S3ObjectTypeDef] = None
    status: Optional[EphemerisStatusType] = None


class OEMEphemerisTypeDef(BaseValidatorModel):
    oemData: Optional[str] = None
    s3Object: Optional[S3ObjectTypeDef] = None


class GetSatelliteResponseTypeDef(BaseValidatorModel):
    currentEphemeris: EphemerisMetaDataTypeDef
    groundStations: List[str]
    noradSatelliteID: int
    satelliteArn: str
    satelliteId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SatelliteListItemTypeDef(BaseValidatorModel):
    currentEphemeris: Optional[EphemerisMetaDataTypeDef] = None
    groundStations: Optional[List[str]] = None
    noradSatelliteID: Optional[int] = None
    satelliteArn: Optional[str] = None
    satelliteId: Optional[str] = None


class SpectrumConfigTypeDef(BaseValidatorModel):
    bandwidth: FrequencyBandwidthTypeDef
    centerFrequency: FrequencyTypeDef
    polarization: Optional[PolarizationType] = None


class UplinkSpectrumConfigTypeDef(BaseValidatorModel):
    centerFrequency: FrequencyTypeDef
    polarization: Optional[PolarizationType] = None


class ListGroundStationsResponseTypeDef(BaseValidatorModel):
    groundStationList: List[GroundStationDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RangedSocketAddressTypeDef(BaseValidatorModel):
    name: str
    portRange: IntegerRangeTypeDef


class ListConfigsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContactsRequestPaginateTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef
    statusList: Sequence[ContactStatusType]
    groundStation: Optional[str] = None
    missionProfileArn: Optional[str] = None
    satelliteArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataflowEndpointGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEphemeridesRequestPaginateTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    satelliteId: str
    startTime: TimestampTypeDef
    statusList: Optional[Sequence[EphemerisStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroundStationsRequestPaginateTypeDef(BaseValidatorModel):
    satelliteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMissionProfilesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSatellitesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMissionProfilesResponseTypeDef(BaseValidatorModel):
    missionProfileList: List[MissionProfileListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RegisterAgentRequestTypeDef(BaseValidatorModel):
    agentDetails: AgentDetailsTypeDef
    discoveryData: DiscoveryDataTypeDef


class ListContactsResponseTypeDef(BaseValidatorModel):
    contactList: List[ContactDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TLEDataTypeDef(BaseValidatorModel):
    tleLine1: str
    tleLine2: str
    validTimeRange: TimeRangeTypeDef


class EphemerisTypeDescriptionTypeDef(BaseValidatorModel):
    oem: Optional[EphemerisDescriptionTypeDef] = None
    tle: Optional[EphemerisDescriptionTypeDef] = None


class ListEphemeridesResponseTypeDef(BaseValidatorModel):
    ephemerides: List[EphemerisItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSatellitesResponseTypeDef(BaseValidatorModel):
    satellites: List[SatelliteListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AntennaDownlinkConfigTypeDef(BaseValidatorModel):
    spectrumConfig: SpectrumConfigTypeDef


class AntennaDownlinkDemodDecodeConfigTypeDef(BaseValidatorModel):
    decodeConfig: DecodeConfigTypeDef
    demodulationConfig: DemodulationConfigTypeDef
    spectrumConfig: SpectrumConfigTypeDef


class AntennaUplinkConfigTypeDef(BaseValidatorModel):
    spectrumConfig: UplinkSpectrumConfigTypeDef
    targetEirp: EirpTypeDef
    transmitDisabled: Optional[bool] = None


class RangedConnectionDetailsTypeDef(BaseValidatorModel):
    socketAddress: RangedSocketAddressTypeDef
    mtu: Optional[int] = None


class TLEEphemerisTypeDef(BaseValidatorModel):
    s3Object: Optional[S3ObjectTypeDef] = None
    tleData: Optional[Sequence[TLEDataTypeDef]] = None


class DescribeEphemerisResponseTypeDef(BaseValidatorModel):
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


class ConfigTypeDataTypeDef(BaseValidatorModel):
    antennaDownlinkConfig: Optional[AntennaDownlinkConfigTypeDef] = None
    antennaDownlinkDemodDecodeConfig: Optional[AntennaDownlinkDemodDecodeConfigTypeDef] = None
    antennaUplinkConfig: Optional[AntennaUplinkConfigTypeDef] = None
    dataflowEndpointConfig: Optional[DataflowEndpointConfigTypeDef] = None
    s3RecordingConfig: Optional[S3RecordingConfigTypeDef] = None
    trackingConfig: Optional[TrackingConfigTypeDef] = None
    uplinkEchoConfig: Optional[UplinkEchoConfigTypeDef] = None


class AwsGroundStationAgentEndpointTypeDef(BaseValidatorModel):
    egressAddress: ConnectionDetailsTypeDef
    ingressAddress: RangedConnectionDetailsTypeDef
    name: str
    agentStatus: Optional[AgentStatusType] = None
    auditResults: Optional[AuditResultsType] = None


class EphemerisDataTypeDef(BaseValidatorModel):
    oem: Optional[OEMEphemerisTypeDef] = None
    tle: Optional[TLEEphemerisTypeDef] = None


class CreateConfigRequestTypeDef(BaseValidatorModel):
    configData: ConfigTypeDataTypeDef
    name: str
    tags: Optional[Mapping[str, str]] = None


class GetConfigResponseTypeDef(BaseValidatorModel):
    configArn: str
    configData: ConfigTypeDataTypeDef
    configId: str
    configType: ConfigCapabilityTypeType
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConfigRequestTypeDef(BaseValidatorModel):
    configData: ConfigTypeDataTypeDef
    configId: str
    configType: ConfigCapabilityTypeType
    name: str


class EndpointDetailsOutputTypeDef(BaseValidatorModel):
    awsGroundStationAgentEndpoint: Optional[AwsGroundStationAgentEndpointTypeDef] = None
    endpoint: Optional[DataflowEndpointTypeDef] = None
    healthReasons: Optional[List[CapabilityHealthReasonType]] = None
    healthStatus: Optional[CapabilityHealthType] = None
    securityDetails: Optional[SecurityDetailsOutputTypeDef] = None


class SecurityDetailsUnionTypeDef(BaseValidatorModel):
    pass


class EndpointDetailsTypeDef(BaseValidatorModel):
    awsGroundStationAgentEndpoint: Optional[AwsGroundStationAgentEndpointTypeDef] = None
    endpoint: Optional[DataflowEndpointTypeDef] = None
    healthReasons: Optional[Sequence[CapabilityHealthReasonType]] = None
    healthStatus: Optional[CapabilityHealthType] = None
    securityDetails: Optional[SecurityDetailsUnionTypeDef] = None


class CreateEphemerisRequestTypeDef(BaseValidatorModel):
    name: str
    satelliteId: str
    enabled: Optional[bool] = None
    ephemeris: Optional[EphemerisDataTypeDef] = None
    expirationTime: Optional[TimestampTypeDef] = None
    kmsKeyArn: Optional[str] = None
    priority: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class ConfigDetailsTypeDef(BaseValidatorModel):
    antennaDemodDecodeDetails: Optional[AntennaDemodDecodeDetailsTypeDef] = None
    endpointDetails: Optional[EndpointDetailsOutputTypeDef] = None
    s3RecordingDetails: Optional[S3RecordingDetailsTypeDef] = None


class GetDataflowEndpointGroupResponseTypeDef(BaseValidatorModel):
    contactPostPassDurationSeconds: int
    contactPrePassDurationSeconds: int
    dataflowEndpointGroupArn: str
    dataflowEndpointGroupId: str
    endpointsDetails: List[EndpointDetailsOutputTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationTypeDef(BaseValidatorModel):
    configDetails: Optional[ConfigDetailsTypeDef] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    dataflowDestinationRegion: Optional[str] = None


class SourceTypeDef(BaseValidatorModel):
    configDetails: Optional[ConfigDetailsTypeDef] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    dataflowSourceRegion: Optional[str] = None


class EndpointDetailsUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataflowEndpointGroupRequestTypeDef(BaseValidatorModel):
    endpointDetails: Sequence[EndpointDetailsUnionTypeDef]
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class DataflowDetailTypeDef(BaseValidatorModel):
    destination: Optional[DestinationTypeDef] = None
    errorMessage: Optional[str] = None
    source: Optional[SourceTypeDef] = None


class DescribeContactResponseTypeDef(BaseValidatorModel):
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



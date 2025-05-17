from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.groundstation.groundstation_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ComponentVersion(BaseValidatorModel):
    componentType: str
    versions: List[str]


class AggregateStatus(BaseValidatorModel):
    status: AgentStatusType
    signatureMap: Optional[Dict[str, bool]] = None


class AntennaDemodDecodeDetails(BaseValidatorModel):
    outputNode: Optional[str] = None


class DecodeConfig(BaseValidatorModel):
    unvalidatedJSON: str


class DemodulationConfig(BaseValidatorModel):
    unvalidatedJSON: str


class Eirp(BaseValidatorModel):
    units: Literal['dBW']
    value: float


# This class is the input for the 'cancel_contact' function.
class CancelContactRequest(BaseValidatorModel):
    contactId: str


class ComponentStatusData(BaseValidatorModel):
    capabilityArn: str
    componentType: str
    dataflowId: str
    status: AgentStatusType
    bytesReceived: Optional[int] = None
    bytesSent: Optional[int] = None
    packetsDropped: Optional[int] = None


class S3RecordingDetails(BaseValidatorModel):
    bucketArn: Optional[str] = None
    keyTemplate: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ConfigListItem(BaseValidatorModel):
    configArn: Optional[str] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    name: Optional[str] = None


class DataflowEndpointConfig(BaseValidatorModel):
    dataflowEndpointName: str
    dataflowEndpointRegion: Optional[str] = None


class S3RecordingConfig(BaseValidatorModel):
    bucketArn: str
    roleArn: str
    prefix: Optional[str] = None


class TrackingConfig(BaseValidatorModel):
    autotrack: CriticalityType


class UplinkEchoConfig(BaseValidatorModel):
    antennaUplinkConfigArn: str
    enabled: bool


class SocketAddress(BaseValidatorModel):
    name: str
    port: int


class Elevation(BaseValidatorModel):
    unit: AngleUnitsType
    value: float

Timestamp = Union[datetime, str]


class KmsKey(BaseValidatorModel):
    kmsAliasArn: Optional[str] = None
    kmsAliasName: Optional[str] = None
    kmsKeyArn: Optional[str] = None


class DataflowEndpointListItem(BaseValidatorModel):
    dataflowEndpointGroupArn: Optional[str] = None
    dataflowEndpointGroupId: Optional[str] = None


# This class is the input for the 'delete_config' function.
class DeleteConfigRequest(BaseValidatorModel):
    configId: str
    configType: ConfigCapabilityTypeType


# This class is the input for the 'delete_dataflow_endpoint_group' function.
class DeleteDataflowEndpointGroupRequest(BaseValidatorModel):
    dataflowEndpointGroupId: str


# This class is the input for the 'delete_ephemeris' function.
class DeleteEphemerisRequest(BaseValidatorModel):
    ephemerisId: str


# This class is the input for the 'delete_mission_profile' function.
class DeleteMissionProfileRequest(BaseValidatorModel):
    missionProfileId: str


# This class is the input for the 'describe_contact' function.
class DescribeContactRequest(BaseValidatorModel):
    contactId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_ephemeris' function.
class DescribeEphemerisRequest(BaseValidatorModel):
    ephemerisId: str


class DiscoveryData(BaseValidatorModel):
    capabilityArns: List[str]
    privateIpAddresses: List[str]
    publicIpAddresses: List[str]


class SecurityDetailsOutput(BaseValidatorModel):
    roleArn: str
    securityGroupIds: List[str]
    subnetIds: List[str]


class S3Object(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    version: Optional[str] = None


class EphemerisMetaData(BaseValidatorModel):
    source: EphemerisSourceType
    ephemerisId: Optional[str] = None
    epoch: Optional[datetime] = None
    name: Optional[str] = None


class FrequencyBandwidth(BaseValidatorModel):
    units: BandwidthUnitsType
    value: float


class Frequency(BaseValidatorModel):
    units: FrequencyUnitsType
    value: float


# This class is the input for the 'get_agent_configuration' function.
class GetAgentConfigurationRequest(BaseValidatorModel):
    agentId: str


# This class is the input for the 'get_config' function.
class GetConfigRequest(BaseValidatorModel):
    configId: str
    configType: ConfigCapabilityTypeType


# This class is the input for the 'get_dataflow_endpoint_group' function.
class GetDataflowEndpointGroupRequest(BaseValidatorModel):
    dataflowEndpointGroupId: str


# This class is the input for the 'get_minute_usage' function.
class GetMinuteUsageRequest(BaseValidatorModel):
    month: int
    year: int


# This class is the input for the 'get_mission_profile' function.
class GetMissionProfileRequest(BaseValidatorModel):
    missionProfileId: str


# This class is the input for the 'get_satellite' function.
class GetSatelliteRequest(BaseValidatorModel):
    satelliteId: str


class GroundStationData(BaseValidatorModel):
    groundStationId: Optional[str] = None
    groundStationName: Optional[str] = None
    region: Optional[str] = None


class IntegerRange(BaseValidatorModel):
    maximum: int
    minimum: int


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_configs' function.
class ListConfigsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_dataflow_endpoint_groups' function.
class ListDataflowEndpointGroupsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_ground_stations' function.
class ListGroundStationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    satelliteId: Optional[str] = None


# This class is the input for the 'list_mission_profiles' function.
class ListMissionProfilesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MissionProfileListItem(BaseValidatorModel):
    missionProfileArn: Optional[str] = None
    missionProfileId: Optional[str] = None
    name: Optional[str] = None
    region: Optional[str] = None


# This class is the input for the 'list_satellites' function.
class ListSatellitesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class SecurityDetails(BaseValidatorModel):
    roleArn: str
    securityGroupIds: List[str]
    subnetIds: List[str]


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_ephemeris' function.
class UpdateEphemerisRequest(BaseValidatorModel):
    enabled: bool
    ephemerisId: str
    name: Optional[str] = None
    priority: Optional[int] = None


class AgentDetails(BaseValidatorModel):
    agentVersion: str
    componentVersions: List[ComponentVersion]
    instanceId: str
    instanceType: str
    agentCpuCores: Optional[List[int]] = None
    reservedCpuCores: Optional[List[int]] = None


# This class is the input for the 'update_agent_status' function.
class UpdateAgentStatusRequest(BaseValidatorModel):
    agentId: str
    aggregateStatus: AggregateStatus
    componentStatuses: List[ComponentStatusData]
    taskId: str


# This class is the output for the 'update_config' function.
class ConfigIdResponse(BaseValidatorModel):
    configArn: str
    configId: str
    configType: ConfigCapabilityTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reserve_contact' function.
class ContactIdResponse(BaseValidatorModel):
    contactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_dataflow_endpoint_group' function.
class DataflowEndpointGroupIdResponse(BaseValidatorModel):
    dataflowEndpointGroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ephemeris' function.
class EphemerisIdResponse(BaseValidatorModel):
    ephemerisId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_agent_configuration' function.
class GetAgentConfigurationResponse(BaseValidatorModel):
    agentId: str
    taskingDocument: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_minute_usage' function.
class GetMinuteUsageResponse(BaseValidatorModel):
    estimatedMinutesRemaining: int
    isReservedMinutesCustomer: bool
    totalReservedMinuteAllocation: int
    totalScheduledMinutes: int
    upcomingMinutesScheduled: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_mission_profile' function.
class MissionProfileIdResponse(BaseValidatorModel):
    missionProfileId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_agent' function.
class RegisterAgentResponse(BaseValidatorModel):
    agentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_agent_status' function.
class UpdateAgentStatusResponse(BaseValidatorModel):
    agentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_configs' function.
class ListConfigsResponse(BaseValidatorModel):
    configList: List[ConfigListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConnectionDetails(BaseValidatorModel):
    socketAddress: SocketAddress
    mtu: Optional[int] = None


class DataflowEndpoint(BaseValidatorModel):
    address: Optional[SocketAddress] = None
    mtu: Optional[int] = None
    name: Optional[str] = None
    status: Optional[EndpointStatusType] = None


class ContactData(BaseValidatorModel):
    contactId: Optional[str] = None
    contactStatus: Optional[ContactStatusType] = None
    endTime: Optional[datetime] = None
    errorMessage: Optional[str] = None
    groundStation: Optional[str] = None
    maximumElevation: Optional[Elevation] = None
    missionProfileArn: Optional[str] = None
    postPassEndTime: Optional[datetime] = None
    prePassStartTime: Optional[datetime] = None
    region: Optional[str] = None
    satelliteArn: Optional[str] = None
    startTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    visibilityEndTime: Optional[datetime] = None
    visibilityStartTime: Optional[datetime] = None


# This class is the input for the 'list_contacts' function.
class ListContactsRequest(BaseValidatorModel):
    endTime: Timestamp
    startTime: Timestamp
    statusList: List[ContactStatusType]
    groundStation: Optional[str] = None
    maxResults: Optional[int] = None
    missionProfileArn: Optional[str] = None
    nextToken: Optional[str] = None
    satelliteArn: Optional[str] = None


# This class is the input for the 'list_ephemerides' function.
class ListEphemeridesRequest(BaseValidatorModel):
    endTime: Timestamp
    satelliteId: str
    startTime: Timestamp
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    statusList: Optional[List[EphemerisStatusType]] = None


# This class is the input for the 'reserve_contact' function.
class ReserveContactRequest(BaseValidatorModel):
    endTime: Timestamp
    groundStation: str
    missionProfileArn: str
    satelliteArn: str
    startTime: Timestamp
    tags: Optional[Dict[str, str]] = None


class TimeRange(BaseValidatorModel):
    endTime: Timestamp
    startTime: Timestamp


# This class is the input for the 'create_mission_profile' function.
class CreateMissionProfileRequest(BaseValidatorModel):
    dataflowEdges: List[List[str]]
    minimumViableContactDurationSeconds: int
    name: str
    trackingConfigArn: str
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    streamsKmsKey: Optional[KmsKey] = None
    streamsKmsRole: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_mission_profile' function.
class GetMissionProfileResponse(BaseValidatorModel):
    contactPostPassDurationSeconds: int
    contactPrePassDurationSeconds: int
    dataflowEdges: List[List[str]]
    minimumViableContactDurationSeconds: int
    missionProfileArn: str
    missionProfileId: str
    name: str
    region: str
    streamsKmsKey: KmsKey
    streamsKmsRole: str
    tags: Dict[str, str]
    trackingConfigArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_mission_profile' function.
class UpdateMissionProfileRequest(BaseValidatorModel):
    missionProfileId: str
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    dataflowEdges: Optional[List[List[str]]] = None
    minimumViableContactDurationSeconds: Optional[int] = None
    name: Optional[str] = None
    streamsKmsKey: Optional[KmsKey] = None
    streamsKmsRole: Optional[str] = None
    trackingConfigArn: Optional[str] = None


# This class is the output for the 'list_dataflow_endpoint_groups' function.
class ListDataflowEndpointGroupsResponse(BaseValidatorModel):
    dataflowEndpointGroupList: List[DataflowEndpointListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeContactRequestWait(BaseValidatorModel):
    contactId: str
    WaiterConfig: Optional[WaiterConfig] = None


class EphemerisDescription(BaseValidatorModel):
    ephemerisData: Optional[str] = None
    sourceS3Object: Optional[S3Object] = None


class EphemerisItem(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    enabled: Optional[bool] = None
    ephemerisId: Optional[str] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    sourceS3Object: Optional[S3Object] = None
    status: Optional[EphemerisStatusType] = None


class OEMEphemeris(BaseValidatorModel):
    oemData: Optional[str] = None
    s3Object: Optional[S3Object] = None


# This class is the output for the 'get_satellite' function.
class GetSatelliteResponse(BaseValidatorModel):
    currentEphemeris: EphemerisMetaData
    groundStations: List[str]
    noradSatelliteID: int
    satelliteArn: str
    satelliteId: str
    ResponseMetadata: ResponseMetadata


class SatelliteListItem(BaseValidatorModel):
    currentEphemeris: Optional[EphemerisMetaData] = None
    groundStations: Optional[List[str]] = None
    noradSatelliteID: Optional[int] = None
    satelliteArn: Optional[str] = None
    satelliteId: Optional[str] = None


class SpectrumConfig(BaseValidatorModel):
    bandwidth: FrequencyBandwidth
    centerFrequency: Frequency
    polarization: Optional[PolarizationType] = None


class UplinkSpectrumConfig(BaseValidatorModel):
    centerFrequency: Frequency
    polarization: Optional[PolarizationType] = None


# This class is the output for the 'list_ground_stations' function.
class ListGroundStationsResponse(BaseValidatorModel):
    groundStationList: List[GroundStationData]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RangedSocketAddress(BaseValidatorModel):
    name: str
    portRange: IntegerRange


class ListConfigsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContactsRequestPaginate(BaseValidatorModel):
    endTime: Timestamp
    startTime: Timestamp
    statusList: List[ContactStatusType]
    groundStation: Optional[str] = None
    missionProfileArn: Optional[str] = None
    satelliteArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataflowEndpointGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEphemeridesRequestPaginate(BaseValidatorModel):
    endTime: Timestamp
    satelliteId: str
    startTime: Timestamp
    statusList: Optional[List[EphemerisStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroundStationsRequestPaginate(BaseValidatorModel):
    satelliteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMissionProfilesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSatellitesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_mission_profiles' function.
class ListMissionProfilesResponse(BaseValidatorModel):
    missionProfileList: List[MissionProfileListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

SecurityDetailsUnion = Union[SecurityDetails, SecurityDetailsOutput]


# This class is the input for the 'register_agent' function.
class RegisterAgentRequest(BaseValidatorModel):
    agentDetails: AgentDetails
    discoveryData: DiscoveryData


# This class is the output for the 'list_contacts' function.
class ListContactsResponse(BaseValidatorModel):
    contactList: List[ContactData]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TLEData(BaseValidatorModel):
    tleLine1: str
    tleLine2: str
    validTimeRange: TimeRange


class EphemerisTypeDescription(BaseValidatorModel):
    oem: Optional[EphemerisDescription] = None
    tle: Optional[EphemerisDescription] = None


# This class is the output for the 'list_ephemerides' function.
class ListEphemeridesResponse(BaseValidatorModel):
    ephemerides: List[EphemerisItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_satellites' function.
class ListSatellitesResponse(BaseValidatorModel):
    satellites: List[SatelliteListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AntennaDownlinkConfig(BaseValidatorModel):
    spectrumConfig: SpectrumConfig


class AntennaDownlinkDemodDecodeConfig(BaseValidatorModel):
    decodeConfig: DecodeConfig
    demodulationConfig: DemodulationConfig
    spectrumConfig: SpectrumConfig


class AntennaUplinkConfig(BaseValidatorModel):
    spectrumConfig: UplinkSpectrumConfig
    targetEirp: Eirp
    transmitDisabled: Optional[bool] = None


class RangedConnectionDetails(BaseValidatorModel):
    socketAddress: RangedSocketAddress
    mtu: Optional[int] = None


class TLEEphemeris(BaseValidatorModel):
    s3Object: Optional[S3Object] = None
    tleData: Optional[List[TLEData]] = None


# This class is the output for the 'describe_ephemeris' function.
class DescribeEphemerisResponse(BaseValidatorModel):
    creationTime: datetime
    enabled: bool
    ephemerisId: str
    invalidReason: EphemerisInvalidReasonType
    name: str
    priority: int
    satelliteId: str
    status: EphemerisStatusType
    suppliedData: EphemerisTypeDescription
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ConfigTypeData(BaseValidatorModel):
    antennaDownlinkConfig: Optional[AntennaDownlinkConfig] = None
    antennaDownlinkDemodDecodeConfig: Optional[AntennaDownlinkDemodDecodeConfig] = None
    antennaUplinkConfig: Optional[AntennaUplinkConfig] = None
    dataflowEndpointConfig: Optional[DataflowEndpointConfig] = None
    s3RecordingConfig: Optional[S3RecordingConfig] = None
    trackingConfig: Optional[TrackingConfig] = None
    uplinkEchoConfig: Optional[UplinkEchoConfig] = None


class AwsGroundStationAgentEndpoint(BaseValidatorModel):
    egressAddress: ConnectionDetails
    ingressAddress: RangedConnectionDetails
    name: str
    agentStatus: Optional[AgentStatusType] = None
    auditResults: Optional[AuditResultsType] = None


class EphemerisData(BaseValidatorModel):
    oem: Optional[OEMEphemeris] = None
    tle: Optional[TLEEphemeris] = None


# This class is the input for the 'create_config' function.
class CreateConfigRequest(BaseValidatorModel):
    configData: ConfigTypeData
    name: str
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_config' function.
class GetConfigResponse(BaseValidatorModel):
    configArn: str
    configData: ConfigTypeData
    configId: str
    configType: ConfigCapabilityTypeType
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_config' function.
class UpdateConfigRequest(BaseValidatorModel):
    configData: ConfigTypeData
    configId: str
    configType: ConfigCapabilityTypeType
    name: str


class EndpointDetailsOutput(BaseValidatorModel):
    awsGroundStationAgentEndpoint: Optional[AwsGroundStationAgentEndpoint] = None
    endpoint: Optional[DataflowEndpoint] = None
    healthReasons: Optional[List[CapabilityHealthReasonType]] = None
    healthStatus: Optional[CapabilityHealthType] = None
    securityDetails: Optional[SecurityDetailsOutput] = None


class EndpointDetails(BaseValidatorModel):
    awsGroundStationAgentEndpoint: Optional[AwsGroundStationAgentEndpoint] = None
    endpoint: Optional[DataflowEndpoint] = None
    healthReasons: Optional[List[CapabilityHealthReasonType]] = None
    healthStatus: Optional[CapabilityHealthType] = None
    securityDetails: Optional[SecurityDetailsUnion] = None


# This class is the input for the 'create_ephemeris' function.
class CreateEphemerisRequest(BaseValidatorModel):
    name: str
    satelliteId: str
    enabled: Optional[bool] = None
    ephemeris: Optional[EphemerisData] = None
    expirationTime: Optional[Timestamp] = None
    kmsKeyArn: Optional[str] = None
    priority: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class ConfigDetails(BaseValidatorModel):
    antennaDemodDecodeDetails: Optional[AntennaDemodDecodeDetails] = None
    endpointDetails: Optional[EndpointDetailsOutput] = None
    s3RecordingDetails: Optional[S3RecordingDetails] = None


# This class is the output for the 'get_dataflow_endpoint_group' function.
class GetDataflowEndpointGroupResponse(BaseValidatorModel):
    contactPostPassDurationSeconds: int
    contactPrePassDurationSeconds: int
    dataflowEndpointGroupArn: str
    dataflowEndpointGroupId: str
    endpointsDetails: List[EndpointDetailsOutput]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

EndpointDetailsUnion = Union[EndpointDetails, EndpointDetailsOutput]


class Destination(BaseValidatorModel):
    configDetails: Optional[ConfigDetails] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    dataflowDestinationRegion: Optional[str] = None


class Source(BaseValidatorModel):
    configDetails: Optional[ConfigDetails] = None
    configId: Optional[str] = None
    configType: Optional[ConfigCapabilityTypeType] = None
    dataflowSourceRegion: Optional[str] = None


# This class is the input for the 'create_dataflow_endpoint_group' function.
class CreateDataflowEndpointGroupRequest(BaseValidatorModel):
    endpointDetails: List[EndpointDetailsUnion]
    contactPostPassDurationSeconds: Optional[int] = None
    contactPrePassDurationSeconds: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class DataflowDetail(BaseValidatorModel):
    destination: Optional[Destination] = None
    errorMessage: Optional[str] = None
    source: Optional[Source] = None


# This class is the output for the 'describe_contact' function.
class DescribeContactResponse(BaseValidatorModel):
    contactId: str
    contactStatus: ContactStatusType
    dataflowList: List[DataflowDetail]
    endTime: datetime
    errorMessage: str
    groundStation: str
    maximumElevation: Elevation
    missionProfileArn: str
    postPassEndTime: datetime
    prePassStartTime: datetime
    region: str
    satelliteArn: str
    startTime: datetime
    tags: Dict[str, str]
    visibilityEndTime: datetime
    visibilityStartTime: datetime
    ResponseMetadata: ResponseMetadata
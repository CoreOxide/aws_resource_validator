# Groundstation Groundstation Classes

# AgentDetails

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### componentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ComponentVersion]
- **Required**: Yes

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### agentCpuCores
- **Type**: typing.Optional[typing.List[int]]

### reservedCpuCores
- **Type**: typing.Optional[typing.List[int]]


# AggregateStatus

### status
- **Type**: typing.Literal['ACTIVE', 'FAILED', 'INACTIVE', 'SUCCESS']
- **Required**: Yes

### signatureMap
- **Type**: typing.Optional[typing.Dict[str, bool]]


# AntennaDemodDecodeDetails

### outputNode
- **Type**: typing.Optional[str]


# AntennaDownlinkConfig

### spectrumConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.SpectrumConfig'>
- **Required**: Yes


# AntennaDownlinkDemodDecodeConfig

### decodeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.DecodeConfig'>
- **Required**: Yes

### demodulationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.DemodulationConfig'>
- **Required**: Yes

### spectrumConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.SpectrumConfig'>
- **Required**: Yes


# AntennaUplinkConfig

### spectrumConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.UplinkSpectrumConfig'>
- **Required**: Yes

### targetEirp
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.Eirp'>
- **Required**: Yes

### transmitDisabled
- **Type**: typing.Optional[bool]


# AwsGroundStationAgentEndpoint

### egressAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ConnectionDetails'>
- **Required**: Yes

### ingressAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.RangedConnectionDetails'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'INACTIVE', 'SUCCESS']]

### auditResults
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelContactRequest

### contactId
- **Type**: <class 'str'>
- **Required**: Yes


# ComponentStatusData

### capabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### dataflowId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'FAILED', 'INACTIVE', 'SUCCESS']
- **Required**: Yes

### bytesReceived
- **Type**: typing.Optional[int]

### bytesSent
- **Type**: typing.Optional[int]

### packetsDropped
- **Type**: typing.Optional[int]


# ComponentVersion

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.List[str]
- **Required**: Yes


# ConfigDetails

### antennaDemodDecodeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.AntennaDemodDecodeDetails]

### endpointDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EndpointDetailsOutput]

### s3RecordingDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.S3RecordingDetails]


# ConfigIdResponse

### configArn
- **Type**: <class 'str'>
- **Required**: Yes

### configId
- **Type**: <class 'str'>
- **Required**: Yes

### configType
- **Type**: typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigListItem

### configArn
- **Type**: typing.Optional[str]

### configId
- **Type**: typing.Optional[str]

### configType
- **Type**: typing.Optional[typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']]

### name
- **Type**: typing.Optional[str]


# ConfigTypeData

### antennaDownlinkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.AntennaDownlinkConfig]

### antennaDownlinkDemodDecodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.AntennaDownlinkDemodDecodeConfig]

### antennaUplinkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.AntennaUplinkConfig]

### dataflowEndpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.DataflowEndpointConfig]

### s3RecordingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.S3RecordingConfig]

### trackingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.TrackingConfig]

### uplinkEchoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.UplinkEchoConfig]


# ConnectionDetails

### socketAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.SocketAddress'>
- **Required**: Yes

### mtu
- **Type**: typing.Optional[int]


# ContactData

### contactId
- **Type**: typing.Optional[str]

### contactStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'AWS_CANCELLED', 'AWS_FAILED', 'CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'PASS', 'POSTPASS', 'PREPASS', 'SCHEDULED', 'SCHEDULING']]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### errorMessage
- **Type**: typing.Optional[str]

### groundStation
- **Type**: typing.Optional[str]

### maximumElevation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.Elevation]

### missionProfileArn
- **Type**: typing.Optional[str]

### postPassEndTime
- **Type**: typing.Optional[datetime.datetime]

### prePassStartTime
- **Type**: typing.Optional[datetime.datetime]

### region
- **Type**: typing.Optional[str]

### satelliteArn
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### visibilityEndTime
- **Type**: typing.Optional[datetime.datetime]

### visibilityStartTime
- **Type**: typing.Optional[datetime.datetime]


# ContactIdResponse

### contactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfigRequest

### configData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ConfigTypeData'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDataflowEndpointGroupRequest

### endpointDetails
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EndpointDetails, aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EndpointDetailsOutput]]
- **Required**: Yes

### contactPostPassDurationSeconds
- **Type**: typing.Optional[int]

### contactPrePassDurationSeconds
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateEphemerisRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### satelliteId
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### ephemeris
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EphemerisData]

### expirationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### kmsKeyArn
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMissionProfileRequest

### dataflowEdges
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### minimumViableContactDurationSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trackingConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### contactPostPassDurationSeconds
- **Type**: typing.Optional[int]

### contactPrePassDurationSeconds
- **Type**: typing.Optional[int]

### streamsKmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.KmsKey]

### streamsKmsRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataflowDetail

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.Destination]

### errorMessage
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.Source]


# DataflowEndpoint

### address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.SocketAddress]

### mtu
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['created', 'creating', 'deleted', 'deleting', 'failed']]


# DataflowEndpointConfig

### dataflowEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### dataflowEndpointRegion
- **Type**: typing.Optional[str]


# DataflowEndpointGroupIdResponse

### dataflowEndpointGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# DataflowEndpointListItem

### dataflowEndpointGroupArn
- **Type**: typing.Optional[str]

### dataflowEndpointGroupId
- **Type**: typing.Optional[str]


# DecodeConfig

### unvalidatedJSON
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigRequest

### configId
- **Type**: <class 'str'>
- **Required**: Yes

### configType
- **Type**: typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']
- **Required**: Yes


# DeleteDataflowEndpointGroupRequest

### dataflowEndpointGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEphemerisRequest

### ephemerisId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMissionProfileRequest

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DemodulationConfig

### unvalidatedJSON
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactRequest

### contactId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactRequestWait

### contactId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeContactResponse

### contactId
- **Type**: <class 'str'>
- **Required**: Yes

### contactStatus
- **Type**: typing.Literal['AVAILABLE', 'AWS_CANCELLED', 'AWS_FAILED', 'CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'PASS', 'POSTPASS', 'PREPASS', 'SCHEDULED', 'SCHEDULING']
- **Required**: Yes

### dataflowList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.DataflowDetail]
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### groundStation
- **Type**: <class 'str'>
- **Required**: Yes

### maximumElevation
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.Elevation'>
- **Required**: Yes

### missionProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### postPassEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### prePassStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### satelliteArn
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### visibilityEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### visibilityStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEphemerisRequest

### ephemerisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEphemerisResponse

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ephemerisId
- **Type**: <class 'str'>
- **Required**: Yes

### invalidReason
- **Type**: typing.Literal['KMS_KEY_INVALID', 'METADATA_INVALID', 'TIME_RANGE_INVALID', 'TRAJECTORY_INVALID', 'VALIDATION_ERROR']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### satelliteId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'ERROR', 'EXPIRED', 'INVALID', 'VALIDATING']
- **Required**: Yes

### suppliedData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EphemerisTypeDescription'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

### configDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ConfigDetails]

### configId
- **Type**: typing.Optional[str]

### configType
- **Type**: typing.Optional[typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']]

### dataflowDestinationRegion
- **Type**: typing.Optional[str]


# DiscoveryData

### capabilityArns
- **Type**: typing.List[str]
- **Required**: Yes

### privateIpAddresses
- **Type**: typing.List[str]
- **Required**: Yes

### publicIpAddresses
- **Type**: typing.List[str]
- **Required**: Yes


# Eirp

### units
- **Type**: typing.Literal['dBW']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# Elevation

### unit
- **Type**: typing.Literal['DEGREE_ANGLE', 'RADIAN']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# EndpointDetails

### awsGroundStationAgentEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.AwsGroundStationAgentEndpoint]

### endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.DataflowEndpoint]

### healthReasons
- **Type**: typing.Optional[typing.List[typing.Literal['DATAPLANE_FAILURE', 'HEALTHY', 'INITIALIZING_DATAPLANE', 'INVALID_IP_OWNERSHIP', 'NOT_AUTHORIZED_TO_CREATE_SLR', 'NO_REGISTERED_AGENT', 'UNVERIFIED_IP_OWNERSHIP']]]

### healthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### securityDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.SecurityDetails, aws_resource_validator.pydantic_models.groundstation.groundstation_classes.SecurityDetailsOutput, NoneType]


# EndpointDetailsOutput

### awsGroundStationAgentEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.AwsGroundStationAgentEndpoint]

### endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.DataflowEndpoint]

### healthReasons
- **Type**: typing.Optional[typing.List[typing.Literal['DATAPLANE_FAILURE', 'HEALTHY', 'INITIALIZING_DATAPLANE', 'INVALID_IP_OWNERSHIP', 'NOT_AUTHORIZED_TO_CREATE_SLR', 'NO_REGISTERED_AGENT', 'UNVERIFIED_IP_OWNERSHIP']]]

### healthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### securityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.SecurityDetailsOutput]


# EphemerisData

### oem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.OEMEphemeris]

### tle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.TLEEphemeris]


# EphemerisDescription

### ephemerisData
- **Type**: typing.Optional[str]

### sourceS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.S3Object]


# EphemerisIdResponse

### ephemerisId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# EphemerisItem

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### enabled
- **Type**: typing.Optional[bool]

### ephemerisId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### sourceS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.S3Object]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ERROR', 'EXPIRED', 'INVALID', 'VALIDATING']]


# EphemerisMetaData

### source
- **Type**: typing.Literal['CUSTOMER_PROVIDED', 'SPACE_TRACK']
- **Required**: Yes

### ephemerisId
- **Type**: typing.Optional[str]

### epoch
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]


# EphemerisTypeDescription

### oem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EphemerisDescription]

### tle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EphemerisDescription]


# Frequency

### units
- **Type**: typing.Literal['GHz', 'MHz', 'kHz']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# FrequencyBandwidth

### units
- **Type**: typing.Literal['GHz', 'MHz', 'kHz']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# GetAgentConfigurationRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentConfigurationResponse

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### taskingDocument
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigRequest

### configId
- **Type**: <class 'str'>
- **Required**: Yes

### configType
- **Type**: typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']
- **Required**: Yes


# GetConfigResponse

### configArn
- **Type**: <class 'str'>
- **Required**: Yes

### configData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ConfigTypeData'>
- **Required**: Yes

### configId
- **Type**: <class 'str'>
- **Required**: Yes

### configType
- **Type**: typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataflowEndpointGroupRequest

### dataflowEndpointGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataflowEndpointGroupResponse

### contactPostPassDurationSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### contactPrePassDurationSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### dataflowEndpointGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataflowEndpointGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### endpointsDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EndpointDetailsOutput]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# GetMinuteUsageRequest

### month
- **Type**: <class 'int'>
- **Required**: Yes

### year
- **Type**: <class 'int'>
- **Required**: Yes


# GetMinuteUsageResponse

### estimatedMinutesRemaining
- **Type**: <class 'int'>
- **Required**: Yes

### isReservedMinutesCustomer
- **Type**: <class 'bool'>
- **Required**: Yes

### totalReservedMinuteAllocation
- **Type**: <class 'int'>
- **Required**: Yes

### totalScheduledMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### upcomingMinutesScheduled
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# GetMissionProfileRequest

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMissionProfileResponse

### contactPostPassDurationSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### contactPrePassDurationSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### dataflowEdges
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### minimumViableContactDurationSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### missionProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### streamsKmsKey
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.KmsKey'>
- **Required**: Yes

### streamsKmsRole
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### trackingConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# GetSatelliteRequest

### satelliteId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSatelliteResponse

### currentEphemeris
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EphemerisMetaData'>
- **Required**: Yes

### groundStations
- **Type**: typing.List[str]
- **Required**: Yes

### noradSatelliteID
- **Type**: <class 'int'>
- **Required**: Yes

### satelliteArn
- **Type**: <class 'str'>
- **Required**: Yes

### satelliteId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# GroundStationData

### groundStationId
- **Type**: typing.Optional[str]

### groundStationName
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# IntegerRange

### maximum
- **Type**: <class 'int'>
- **Required**: Yes

### minimum
- **Type**: <class 'int'>
- **Required**: Yes


# KmsKey

### kmsAliasArn
- **Type**: typing.Optional[str]

### kmsAliasName
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]


# ListConfigsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConfigsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.PaginatorConfig]


# ListConfigsResponse

### configList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ConfigListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContactsRequest

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### statusList
- **Type**: typing.List[typing.Literal['AVAILABLE', 'AWS_CANCELLED', 'AWS_FAILED', 'CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'PASS', 'POSTPASS', 'PREPASS', 'SCHEDULED', 'SCHEDULING']]
- **Required**: Yes

### groundStation
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### missionProfileArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### satelliteArn
- **Type**: typing.Optional[str]


# ListContactsRequestPaginate

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### statusList
- **Type**: typing.List[typing.Literal['AVAILABLE', 'AWS_CANCELLED', 'AWS_FAILED', 'CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'PASS', 'POSTPASS', 'PREPASS', 'SCHEDULED', 'SCHEDULING']]
- **Required**: Yes

### groundStation
- **Type**: typing.Optional[str]

### missionProfileArn
- **Type**: typing.Optional[str]

### satelliteArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.PaginatorConfig]


# ListContactsResponse

### contactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ContactData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataflowEndpointGroupsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataflowEndpointGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.PaginatorConfig]


# ListDataflowEndpointGroupsResponse

### dataflowEndpointGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.DataflowEndpointListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEphemeridesRequest

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### satelliteId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### statusList
- **Type**: typing.Optional[typing.List[typing.Literal['DISABLED', 'ENABLED', 'ERROR', 'EXPIRED', 'INVALID', 'VALIDATING']]]


# ListEphemeridesRequestPaginate

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### satelliteId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### statusList
- **Type**: typing.Optional[typing.List[typing.Literal['DISABLED', 'ENABLED', 'ERROR', 'EXPIRED', 'INVALID', 'VALIDATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.PaginatorConfig]


# ListEphemeridesResponse

### ephemerides
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EphemerisItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGroundStationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### satelliteId
- **Type**: typing.Optional[str]


# ListGroundStationsRequestPaginate

### satelliteId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.PaginatorConfig]


# ListGroundStationsResponse

### groundStationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.GroundStationData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMissionProfilesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMissionProfilesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.PaginatorConfig]


# ListMissionProfilesResponse

### missionProfileList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.MissionProfileListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSatellitesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSatellitesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.PaginatorConfig]


# ListSatellitesResponse

### satellites
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.SatelliteListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# MissionProfileIdResponse

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# MissionProfileListItem

### missionProfileArn
- **Type**: typing.Optional[str]

### missionProfileId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# OEMEphemeris

### oemData
- **Type**: typing.Optional[str]

### s3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.S3Object]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RangedConnectionDetails

### socketAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.RangedSocketAddress'>
- **Required**: Yes

### mtu
- **Type**: typing.Optional[int]


# RangedSocketAddress

### name
- **Type**: <class 'str'>
- **Required**: Yes

### portRange
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.IntegerRange'>
- **Required**: Yes


# RegisterAgentRequest

### agentDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.AgentDetails'>
- **Required**: Yes

### discoveryData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.DiscoveryData'>
- **Required**: Yes


# RegisterAgentResponse

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# ReserveContactRequest

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### groundStation
- **Type**: <class 'str'>
- **Required**: Yes

### missionProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### satelliteArn
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# S3Object

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# S3RecordingConfig

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# S3RecordingDetails

### bucketArn
- **Type**: typing.Optional[str]

### keyTemplate
- **Type**: typing.Optional[str]


# SatelliteListItem

### currentEphemeris
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.EphemerisMetaData]

### groundStations
- **Type**: typing.Optional[typing.List[str]]

### noradSatelliteID
- **Type**: typing.Optional[int]

### satelliteArn
- **Type**: typing.Optional[str]

### satelliteId
- **Type**: typing.Optional[str]


# SecurityDetails

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# SecurityDetailsOutput

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# SocketAddress

### name
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes


# Source

### configDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ConfigDetails]

### configId
- **Type**: typing.Optional[str]

### configType
- **Type**: typing.Optional[typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']]

### dataflowSourceRegion
- **Type**: typing.Optional[str]


# SpectrumConfig

### bandwidth
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.FrequencyBandwidth'>
- **Required**: Yes

### centerFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.Frequency'>
- **Required**: Yes

### polarization
- **Type**: typing.Optional[typing.Literal['LEFT_HAND', 'NONE', 'RIGHT_HAND']]


# TLEData

### tleLine1
- **Type**: <class 'str'>
- **Required**: Yes

### tleLine2
- **Type**: <class 'str'>
- **Required**: Yes

### validTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.TimeRange'>
- **Required**: Yes


# TLEEphemeris

### s3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.S3Object]

### tleData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.TLEData]]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TimeRange

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# TrackingConfig

### autotrack
- **Type**: typing.Literal['PREFERRED', 'REMOVED', 'REQUIRED']
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAgentStatusRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregateStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.AggregateStatus'>
- **Required**: Yes

### componentStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ComponentStatusData]
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAgentStatusResponse

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfigRequest

### configData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.ConfigTypeData'>
- **Required**: Yes

### configId
- **Type**: <class 'str'>
- **Required**: Yes

### configType
- **Type**: typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateEphemerisRequest

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ephemerisId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]


# UpdateMissionProfileRequest

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### contactPostPassDurationSeconds
- **Type**: typing.Optional[int]

### contactPrePassDurationSeconds
- **Type**: typing.Optional[int]

### dataflowEdges
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### minimumViableContactDurationSeconds
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### streamsKmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation.groundstation_classes.KmsKey]

### streamsKmsRole
- **Type**: typing.Optional[str]

### trackingConfigArn
- **Type**: typing.Optional[str]


# UplinkEchoConfig

### antennaUplinkConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# UplinkSpectrumConfig

### centerFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation.groundstation_classes.Frequency'>
- **Required**: Yes

### polarization
- **Type**: typing.Optional[typing.Literal['LEFT_HAND', 'NONE', 'RIGHT_HAND']]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



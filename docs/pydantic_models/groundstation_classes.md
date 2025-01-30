# groundstation_classes

# AgentDetailsTypeDef

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### componentVersions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.groundstation_classes.ComponentVersionTypeDef]
- **Required**: Yes

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### agentCpuCores
- **Type**: typing.Optional[typing.Sequence[int]]

### reservedCpuCores
- **Type**: typing.Optional[typing.Sequence[int]]


# AggregateStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'FAILED', 'INACTIVE', 'SUCCESS']
- **Required**: Yes

### signatureMap
- **Type**: typing.Optional[typing.Mapping[str, bool]]


# AntennaDemodDecodeDetailsTypeDef

### outputNode
- **Type**: typing.Optional[str]


# AntennaDownlinkConfigTypeDef

### spectrumConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.SpectrumConfigTypeDef'>
- **Required**: Yes


# AntennaDownlinkDemodDecodeConfigTypeDef

### decodeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.DecodeConfigTypeDef'>
- **Required**: Yes

### demodulationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.DemodulationConfigTypeDef'>
- **Required**: Yes

### spectrumConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.SpectrumConfigTypeDef'>
- **Required**: Yes


# AntennaUplinkConfigTypeDef

### spectrumConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.UplinkSpectrumConfigTypeDef'>
- **Required**: Yes

### targetEirp
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.EirpTypeDef'>
- **Required**: Yes

### transmitDisabled
- **Type**: typing.Optional[bool]


# AwsGroundStationAgentEndpointTypeDef

### egressAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ConnectionDetailsTypeDef'>
- **Required**: Yes

### ingressAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.RangedConnectionDetailsTypeDef'>
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

# CancelContactRequestRequestTypeDef

### contactId
- **Type**: <class 'str'>
- **Required**: Yes


# ComponentStatusDataTypeDef

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


# ComponentVersionTypeDef

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ConfigDetailsTypeDef

### antennaDemodDecodeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.AntennaDemodDecodeDetailsTypeDef]

### endpointDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.EndpointDetailsOutputTypeDef]

### s3RecordingDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.S3RecordingDetailsTypeDef]


# ConfigIdResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigListItemTypeDef

### configArn
- **Type**: typing.Optional[str]

### configId
- **Type**: typing.Optional[str]

### configType
- **Type**: typing.Optional[typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']]

### name
- **Type**: typing.Optional[str]


# ConfigTypeDataTypeDef

### antennaDownlinkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.AntennaDownlinkConfigTypeDef]

### antennaDownlinkDemodDecodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.AntennaDownlinkDemodDecodeConfigTypeDef]

### antennaUplinkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.AntennaUplinkConfigTypeDef]

### dataflowEndpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.DataflowEndpointConfigTypeDef]

### s3RecordingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.S3RecordingConfigTypeDef]

### trackingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.TrackingConfigTypeDef]

### uplinkEchoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.UplinkEchoConfigTypeDef]


# ConnectionDetailsTypeDef

### socketAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.SocketAddressTypeDef'>
- **Required**: Yes

### mtu
- **Type**: typing.Optional[int]


# ContactDataTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.ElevationTypeDef]

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


# ContactIdResponseTypeDef

### contactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfigRequestRequestTypeDef

### configData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ConfigTypeDataTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDataflowEndpointGroupRequestRequestTypeDef

### endpointDetails
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.groundstation_classes.EndpointDetailsTypeDef, aws_resource_validator.pydantic_models.groundstation_classes.EndpointDetailsOutputTypeDef]]
- **Required**: Yes

### contactPostPassDurationSeconds
- **Type**: typing.Optional[int]

### contactPrePassDurationSeconds
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEphemerisRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### satelliteId
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### ephemeris
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.EphemerisDataTypeDef]

### expirationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### kmsKeyArn
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMissionProfileRequestRequestTypeDef

### dataflowEdges
- **Type**: typing.Sequence[typing.Sequence[str]]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.KmsKeyTypeDef]

### streamsKmsRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DataflowDetailTypeDef

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.DestinationTypeDef]

### errorMessage
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.SourceTypeDef]


# DataflowEndpointConfigTypeDef

### dataflowEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### dataflowEndpointRegion
- **Type**: typing.Optional[str]


# DataflowEndpointGroupIdResponseTypeDef

### dataflowEndpointGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataflowEndpointListItemTypeDef

### dataflowEndpointGroupArn
- **Type**: typing.Optional[str]

### dataflowEndpointGroupId
- **Type**: typing.Optional[str]


# DataflowEndpointTypeDef

### address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.SocketAddressTypeDef]

### mtu
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['created', 'creating', 'deleted', 'deleting', 'failed']]


# DecodeConfigTypeDef

### unvalidatedJSON
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigRequestRequestTypeDef

### configId
- **Type**: <class 'str'>
- **Required**: Yes

### configType
- **Type**: typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']
- **Required**: Yes


# DeleteDataflowEndpointGroupRequestRequestTypeDef

### dataflowEndpointGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEphemerisRequestRequestTypeDef

### ephemerisId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMissionProfileRequestRequestTypeDef

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DemodulationConfigTypeDef

### unvalidatedJSON
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactRequestContactScheduledWaitTypeDef

### contactId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.WaiterConfigTypeDef]


# DescribeContactRequestRequestTypeDef

### contactId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactResponseTypeDef

### contactId
- **Type**: <class 'str'>
- **Required**: Yes

### contactStatus
- **Type**: typing.Literal['AVAILABLE', 'AWS_CANCELLED', 'AWS_FAILED', 'CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'PASS', 'POSTPASS', 'PREPASS', 'SCHEDULED', 'SCHEDULING']
- **Required**: Yes

### dataflowList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.DataflowDetailTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ElevationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEphemerisRequestRequestTypeDef

### ephemerisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEphemerisResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.EphemerisTypeDescriptionTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

### configDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.ConfigDetailsTypeDef]

### configId
- **Type**: typing.Optional[str]

### configType
- **Type**: typing.Optional[typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']]

### dataflowDestinationRegion
- **Type**: typing.Optional[str]


# DiscoveryDataTypeDef

### capabilityArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### privateIpAddresses
- **Type**: typing.Sequence[str]
- **Required**: Yes

### publicIpAddresses
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EirpTypeDef

### units
- **Type**: typing.Literal['dBW']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# ElevationTypeDef

### unit
- **Type**: typing.Literal['DEGREE_ANGLE', 'RADIAN']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# EndpointDetailsOutputTypeDef

### awsGroundStationAgentEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.AwsGroundStationAgentEndpointTypeDef]

### endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.DataflowEndpointTypeDef]

### healthReasons
- **Type**: typing.Optional[typing.List[typing.Literal['DATAPLANE_FAILURE', 'HEALTHY', 'INITIALIZING_DATAPLANE', 'INVALID_IP_OWNERSHIP', 'NOT_AUTHORIZED_TO_CREATE_SLR', 'NO_REGISTERED_AGENT', 'UNVERIFIED_IP_OWNERSHIP']]]

### healthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### securityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.SecurityDetailsOutputTypeDef]


# EndpointDetailsTypeDef

### awsGroundStationAgentEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.AwsGroundStationAgentEndpointTypeDef]

### endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.DataflowEndpointTypeDef]

### healthReasons
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DATAPLANE_FAILURE', 'HEALTHY', 'INITIALIZING_DATAPLANE', 'INVALID_IP_OWNERSHIP', 'NOT_AUTHORIZED_TO_CREATE_SLR', 'NO_REGISTERED_AGENT', 'UNVERIFIED_IP_OWNERSHIP']]]

### healthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### securityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.SecurityDetailsTypeDef]


# EphemerisDataTypeDef

### oem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.OEMEphemerisTypeDef]

### tle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.TLEEphemerisTypeDef]


# EphemerisDescriptionTypeDef

### ephemerisData
- **Type**: typing.Optional[str]

### sourceS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.S3ObjectTypeDef]


# EphemerisIdResponseTypeDef

### ephemerisId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EphemerisItemTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.S3ObjectTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ERROR', 'EXPIRED', 'INVALID', 'VALIDATING']]


# EphemerisMetaDataTypeDef

### source
- **Type**: typing.Literal['CUSTOMER_PROVIDED', 'SPACE_TRACK']
- **Required**: Yes

### ephemerisId
- **Type**: typing.Optional[str]

### epoch
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]


# EphemerisTypeDescriptionTypeDef

### oem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.EphemerisDescriptionTypeDef]

### tle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.EphemerisDescriptionTypeDef]


# FrequencyBandwidthTypeDef

### units
- **Type**: typing.Literal['GHz', 'MHz', 'kHz']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# FrequencyTypeDef

### units
- **Type**: typing.Literal['GHz', 'MHz', 'kHz']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# GetAgentConfigurationRequestRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentConfigurationResponseTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### taskingDocument
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigRequestRequestTypeDef

### configId
- **Type**: <class 'str'>
- **Required**: Yes

### configType
- **Type**: typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']
- **Required**: Yes


# GetConfigResponseTypeDef

### configArn
- **Type**: <class 'str'>
- **Required**: Yes

### configData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ConfigTypeDataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataflowEndpointGroupRequestRequestTypeDef

### dataflowEndpointGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataflowEndpointGroupResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.EndpointDetailsOutputTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMinuteUsageRequestRequestTypeDef

### month
- **Type**: <class 'int'>
- **Required**: Yes

### year
- **Type**: <class 'int'>
- **Required**: Yes


# GetMinuteUsageResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMissionProfileRequestRequestTypeDef

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMissionProfileResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.KmsKeyTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSatelliteRequestRequestTypeDef

### satelliteId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSatelliteResponseTypeDef

### currentEphemeris
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.EphemerisMetaDataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroundStationDataTypeDef

### groundStationId
- **Type**: typing.Optional[str]

### groundStationName
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# IntegerRangeTypeDef

### maximum
- **Type**: <class 'int'>
- **Required**: Yes

### minimum
- **Type**: <class 'int'>
- **Required**: Yes


# KmsKeyTypeDef

### kmsAliasArn
- **Type**: typing.Optional[str]

### kmsAliasName
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]


# ListConfigsRequestListConfigsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.PaginatorConfigTypeDef]


# ListConfigsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConfigsResponseTypeDef

### configList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.ConfigListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContactsRequestListContactsPaginateTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### statusList
- **Type**: typing.Sequence[typing.Literal['AVAILABLE', 'AWS_CANCELLED', 'AWS_FAILED', 'CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'PASS', 'POSTPASS', 'PREPASS', 'SCHEDULED', 'SCHEDULING']]
- **Required**: Yes

### groundStation
- **Type**: typing.Optional[str]

### missionProfileArn
- **Type**: typing.Optional[str]

### satelliteArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.PaginatorConfigTypeDef]


# ListContactsRequestRequestTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### statusList
- **Type**: typing.Sequence[typing.Literal['AVAILABLE', 'AWS_CANCELLED', 'AWS_FAILED', 'CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'PASS', 'POSTPASS', 'PREPASS', 'SCHEDULED', 'SCHEDULING']]
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


# ListContactsResponseTypeDef

### contactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.ContactDataTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.PaginatorConfigTypeDef]


# ListDataflowEndpointGroupsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataflowEndpointGroupsResponseTypeDef

### dataflowEndpointGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.DataflowEndpointListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEphemeridesRequestListEphemeridesPaginateTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DISABLED', 'ENABLED', 'ERROR', 'EXPIRED', 'INVALID', 'VALIDATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.PaginatorConfigTypeDef]


# ListEphemeridesRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DISABLED', 'ENABLED', 'ERROR', 'EXPIRED', 'INVALID', 'VALIDATING']]]


# ListEphemeridesResponseTypeDef

### ephemerides
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.EphemerisItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroundStationsRequestListGroundStationsPaginateTypeDef

### satelliteId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.PaginatorConfigTypeDef]


# ListGroundStationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### satelliteId
- **Type**: typing.Optional[str]


# ListGroundStationsResponseTypeDef

### groundStationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.GroundStationDataTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMissionProfilesRequestListMissionProfilesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.PaginatorConfigTypeDef]


# ListMissionProfilesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMissionProfilesResponseTypeDef

### missionProfileList
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.MissionProfileListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSatellitesRequestListSatellitesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.PaginatorConfigTypeDef]


# ListSatellitesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSatellitesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### satellites
- **Type**: typing.List[aws_resource_validator.pydantic_models.groundstation_classes.SatelliteListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MissionProfileIdResponseTypeDef

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MissionProfileListItemTypeDef

### missionProfileArn
- **Type**: typing.Optional[str]

### missionProfileId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# OEMEphemerisTypeDef

### oemData
- **Type**: typing.Optional[str]

### s3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.S3ObjectTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RangedConnectionDetailsTypeDef

### socketAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.RangedSocketAddressTypeDef'>
- **Required**: Yes

### mtu
- **Type**: typing.Optional[int]


# RangedSocketAddressTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### portRange
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.IntegerRangeTypeDef'>
- **Required**: Yes


# RegisterAgentRequestRequestTypeDef

### agentDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.AgentDetailsTypeDef'>
- **Required**: Yes

### discoveryData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.DiscoveryDataTypeDef'>
- **Required**: Yes


# RegisterAgentResponseTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReserveContactRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ResponseMetadataTypeDef

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


# S3ObjectTypeDef

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# S3RecordingConfigTypeDef

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# S3RecordingDetailsTypeDef

### bucketArn
- **Type**: typing.Optional[str]

### keyTemplate
- **Type**: typing.Optional[str]


# SatelliteListItemTypeDef

### currentEphemeris
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.EphemerisMetaDataTypeDef]

### groundStations
- **Type**: typing.Optional[typing.List[str]]

### noradSatelliteID
- **Type**: typing.Optional[int]

### satelliteArn
- **Type**: typing.Optional[str]

### satelliteId
- **Type**: typing.Optional[str]


# SecurityDetailsOutputTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# SecurityDetailsTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SocketAddressTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes


# SourceTypeDef

### configDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.ConfigDetailsTypeDef]

### configId
- **Type**: typing.Optional[str]

### configType
- **Type**: typing.Optional[typing.Literal['antenna-downlink', 'antenna-downlink-demod-decode', 'antenna-uplink', 'dataflow-endpoint', 's3-recording', 'tracking', 'uplink-echo']]

### dataflowSourceRegion
- **Type**: typing.Optional[str]


# SpectrumConfigTypeDef

### bandwidth
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.FrequencyBandwidthTypeDef'>
- **Required**: Yes

### centerFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.FrequencyTypeDef'>
- **Required**: Yes

### polarization
- **Type**: typing.Optional[typing.Literal['LEFT_HAND', 'NONE', 'RIGHT_HAND']]


# TLEDataTypeDef

### tleLine1
- **Type**: <class 'str'>
- **Required**: Yes

### tleLine2
- **Type**: <class 'str'>
- **Required**: Yes

### validTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.TimeRangeTypeDef'>
- **Required**: Yes


# TLEEphemerisTypeDef

### s3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.S3ObjectTypeDef]

### tleData
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.groundstation_classes.TLEDataTypeDef]]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimeRangeTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# TrackingConfigTypeDef

### autotrack
- **Type**: typing.Literal['PREFERRED', 'REMOVED', 'REQUIRED']
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAgentStatusRequestRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregateStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.AggregateStatusTypeDef'>
- **Required**: Yes

### componentStatuses
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.groundstation_classes.ComponentStatusDataTypeDef]
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAgentStatusResponseTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfigRequestRequestTypeDef

### configData
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.ConfigTypeDataTypeDef'>
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


# UpdateEphemerisRequestRequestTypeDef

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


# UpdateMissionProfileRequestRequestTypeDef

### missionProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### contactPostPassDurationSeconds
- **Type**: typing.Optional[int]

### contactPrePassDurationSeconds
- **Type**: typing.Optional[int]

### dataflowEdges
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### minimumViableContactDurationSeconds
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### streamsKmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.groundstation_classes.KmsKeyTypeDef]

### streamsKmsRole
- **Type**: typing.Optional[str]

### trackingConfigArn
- **Type**: typing.Optional[str]


# UplinkEchoConfigTypeDef

### antennaUplinkConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# UplinkSpectrumConfigTypeDef

### centerFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.groundstation_classes.FrequencyTypeDef'>
- **Required**: Yes

### polarization
- **Type**: typing.Optional[typing.Literal['LEFT_HAND', 'NONE', 'RIGHT_HAND']]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



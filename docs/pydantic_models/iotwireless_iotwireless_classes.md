# Iotwireless Iotwireless Classes

# AbpV10X

### DevAddr
- **Type**: typing.Optional[str]

### SessionKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SessionKeysAbpV10X]

### FCntStart
- **Type**: typing.Optional[int]


# AbpV11

### DevAddr
- **Type**: typing.Optional[str]

### SessionKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SessionKeysAbpV11]

### FCntStart
- **Type**: typing.Optional[int]


# Accuracy

### HorizontalAccuracy
- **Type**: typing.Optional[float]

### VerticalAccuracy
- **Type**: typing.Optional[float]


# ApplicationConfig

### FPort
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[typing.Literal['SemtechGeolocation']]

### DestinationName
- **Type**: typing.Optional[str]


# AssociateAwsAccountWithPartnerAccountRequest

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkAccountInfo'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]


# AssociateAwsAccountWithPartnerAccountResponse

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkAccountInfo'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateMulticastGroupWithFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MulticastGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithMulticastGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithThingRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessGatewayWithCertificateRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IotCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessGatewayWithCertificateResponse

### IotCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateWirelessGatewayWithThingRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Beaconing

### DataRate
- **Type**: typing.Optional[int]

### Frequencies
- **Type**: typing.Optional[typing.List[int]]


# BeaconingOutput

### DataRate
- **Type**: typing.Optional[int]

### Frequencies
- **Type**: typing.Optional[typing.List[int]]


# CancelMulticastGroupSessionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CdmaLocalId

### PnOffset
- **Type**: <class 'int'>
- **Required**: Yes

### CdmaChannel
- **Type**: <class 'int'>
- **Required**: Yes


# CdmaNmrObj

### PnOffset
- **Type**: <class 'int'>
- **Required**: Yes

### CdmaChannel
- **Type**: <class 'int'>
- **Required**: Yes

### PilotPower
- **Type**: typing.Optional[int]

### BaseStationId
- **Type**: typing.Optional[int]


# CdmaObj

### SystemId
- **Type**: <class 'int'>
- **Required**: Yes

### NetworkId
- **Type**: <class 'int'>
- **Required**: Yes

### BaseStationId
- **Type**: <class 'int'>
- **Required**: Yes

### RegistrationZone
- **Type**: typing.Optional[int]

### CdmaLocalId
- **Type**: <class 'NoneType'>

### PilotPower
- **Type**: typing.Optional[int]

### BaseLat
- **Type**: typing.Optional[float]

### BaseLng
- **Type**: typing.Optional[float]

### CdmaNmr
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.CdmaNmrObj]]


# CellTowers

### Gsm
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.GsmObj]]

### Wcdma
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WcdmaObj]]

### Tdscdma
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.TdscdmaObj]]

### Lte
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LteObj]]

### Cdma
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.CdmaObj]]


# CertificateList

### SigningAlg
- **Type**: typing.Literal['Ed25519', 'P256r1']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ConnectionStatusEventConfiguration

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANConnectionStatusEventNotificationConfigurations]

### WirelessGatewayIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# ConnectionStatusResourceTypeEventConfiguration

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANConnectionStatusResourceTypeEventConfiguration]


# CreateDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionType
- **Type**: typing.Literal['MqttTopic', 'RuleName']
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateDestinationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeviceProfileRequest

### Name
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANDeviceProfile, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANDeviceProfileOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Sidewalk
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# CreateDeviceProfileResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFuotaTaskRequest

### FirmwareUpdateImage
- **Type**: <class 'str'>
- **Required**: Yes

### FirmwareUpdateRole
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANFuotaTask]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]

### RedundancyPercent
- **Type**: typing.Optional[int]

### FragmentSizeBytes
- **Type**: typing.Optional[int]

### FragmentIntervalMS
- **Type**: typing.Optional[int]

### Descriptor
- **Type**: typing.Optional[str]


# CreateFuotaTaskResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMulticastGroupRequest

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANMulticast'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]


# CreateMulticastGroupResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNetworkAnalyzerConfigurationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TraceContent
- **Type**: <class 'NoneType'>

### WirelessDevices
- **Type**: typing.Optional[typing.List[str]]

### WirelessGateways
- **Type**: typing.Optional[typing.List[str]]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### MulticastGroups
- **Type**: typing.Optional[typing.List[str]]


# CreateNetworkAnalyzerConfigurationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceProfileRequest

### Name
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANServiceProfile]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateServiceProfileResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWirelessDeviceRequest

### Type
- **Type**: typing.Literal['LoRaWAN', 'Sidewalk']
- **Required**: Yes

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANDevice, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANDeviceOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]

### Positioning
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkCreateWirelessDevice]


# CreateWirelessDeviceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWirelessGatewayRequest

### LoRaWAN
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGateway, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayOutput]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateWirelessGatewayResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWirelessGatewayTaskDefinitionRequest

### AutoCreateTasks
- **Type**: <class 'bool'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.UpdateWirelessGatewayTaskCreate]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]


# CreateWirelessGatewayTaskDefinitionResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWirelessGatewayTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessGatewayTaskDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWirelessGatewayTaskResponse

### WirelessGatewayTaskDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'FIRST_RETRY', 'IN_PROGRESS', 'PENDING', 'SECOND_RETRY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# DakCertificateMetadata

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxAllowedSignature
- **Type**: typing.Optional[int]

### FactorySupport
- **Type**: typing.Optional[bool]

### ApId
- **Type**: typing.Optional[str]

### DeviceTypeId
- **Type**: typing.Optional[str]


# DeleteDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceProfileRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMulticastGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkAnalyzerConfigurationRequest

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueuedMessagesRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# DeleteServiceProfileRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessDeviceImportTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessDeviceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayTaskDefinitionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterWirelessDeviceRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# Destinations

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ExpressionType
- **Type**: typing.Optional[typing.Literal['MqttTopic', 'RuleName']]

### Expression
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# DeviceProfile

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# DeviceRegistrationStateEventConfiguration

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkEventNotificationConfigurations]

### WirelessDeviceIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# DeviceRegistrationStateResourceTypeEventConfiguration

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkResourceTypeEventConfiguration]


# Dimension

### name
- **Type**: typing.Optional[typing.Literal['DeviceId', 'GatewayId']]

### value
- **Type**: typing.Optional[str]


# DisassociateAwsAccountFromPartnerAccountRequest

### PartnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerType
- **Type**: typing.Literal['Sidewalk']
- **Required**: Yes


# DisassociateMulticastGroupFromFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MulticastGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromMulticastGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromThingRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessGatewayFromCertificateRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessGatewayFromThingRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DownlinkQueueMessage

### MessageId
- **Type**: typing.Optional[str]

### TransmitMode
- **Type**: typing.Optional[int]

### ReceivedAt
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANSendDataToDeviceOutput]


# EventConfigurationItem

### Identifier
- **Type**: typing.Optional[str]

### IdentifierType
- **Type**: typing.Optional[typing.Literal['DevEui', 'FuotaTaskId', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']]

### PartnerType
- **Type**: typing.Optional[typing.Literal['Sidewalk']]

### Events
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.EventNotificationItemConfigurations]


# EventNotificationItemConfigurations

### DeviceRegistrationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.DeviceRegistrationStateEventConfiguration]

### Proximity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ProximityEventConfiguration]

### Join
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.JoinEventConfiguration]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ConnectionStatusEventConfiguration]

### MessageDeliveryStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MessageDeliveryStatusEventConfiguration]


# FPorts

### Fuota
- **Type**: typing.Optional[int]

### Multicast
- **Type**: typing.Optional[int]

### ClockSync
- **Type**: typing.Optional[int]

### Positioning
- **Type**: <class 'NoneType'>

### Applications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ApplicationConfig]]


# FPortsOutput

### Fuota
- **Type**: typing.Optional[int]

### Multicast
- **Type**: typing.Optional[int]

### ClockSync
- **Type**: typing.Optional[int]

### Positioning
- **Type**: <class 'NoneType'>

### Applications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ApplicationConfig]]


# FuotaTask

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# FuotaTaskEventLogOption

### Event
- **Type**: typing.Literal['Fuota']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# FuotaTaskLogOption

### Type
- **Type**: typing.Literal['LoRaWAN']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.FuotaTaskEventLogOption]]


# FuotaTaskLogOptionOutput

### Type
- **Type**: typing.Literal['LoRaWAN']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.FuotaTaskEventLogOption]]


# GatewayListItem

### GatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### DownlinkFrequency
- **Type**: <class 'int'>
- **Required**: Yes


# GetDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDestinationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionType
- **Type**: typing.Literal['MqttTopic', 'RuleName']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceProfileRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceProfileResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANDeviceProfileOutput'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkGetDeviceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventConfigurationByResourceTypesResponse

### DeviceRegistrationState
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.DeviceRegistrationStateResourceTypeEventConfiguration'>
- **Required**: Yes

### Proximity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ProximityResourceTypeEventConfiguration'>
- **Required**: Yes

### Join
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.JoinResourceTypeEventConfiguration'>
- **Required**: Yes

### ConnectionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ConnectionStatusResourceTypeEventConfiguration'>
- **Required**: Yes

### MessageDeliveryStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MessageDeliveryStatusResourceTypeEventConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFuotaTaskResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Delete_Waiting', 'FuotaDone', 'FuotaSession_Waiting', 'In_FuotaSession', 'Pending']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANFuotaTaskGetInfo'>
- **Required**: Yes

### FirmwareUpdateImage
- **Type**: <class 'str'>
- **Required**: Yes

### FirmwareUpdateRole
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RedundancyPercent
- **Type**: <class 'int'>
- **Required**: Yes

### FragmentSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### FragmentIntervalMS
- **Type**: <class 'int'>
- **Required**: Yes

### Descriptor
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetLogLevelsByResourceTypesResponse

### DefaultLogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### WirelessGatewayLogOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessGatewayLogOptionOutput]
- **Required**: Yes

### WirelessDeviceLogOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessDeviceLogOptionOutput]
- **Required**: Yes

### FuotaTaskLogOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.FuotaTaskLogOptionOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetricConfigurationResponse

### SummaryMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SummaryMetricConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetricsRequest

### SummaryMetricQueries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SummaryMetricQuery]]


# GetMetricsResponse

### SummaryMetricQueryResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SummaryMetricQueryResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetMulticastGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMulticastGroupResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANMulticastGet'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetMulticastGroupSessionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMulticastGroupSessionResponse

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANMulticastSessionOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkAnalyzerConfigurationRequest

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkAnalyzerConfigurationResponse

### TraceContent
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.TraceContent'>
- **Required**: Yes

### WirelessDevices
- **Type**: typing.List[str]
- **Required**: Yes

### WirelessGateways
- **Type**: typing.List[str]
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MulticastGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetPartnerAccountRequest

### PartnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerType
- **Type**: typing.Literal['Sidewalk']
- **Required**: Yes


# GetPartnerAccountResponse

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkAccountInfoWithFingerprint'>
- **Required**: Yes

### AccountLinked
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetPositionConfigurationRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes


# GetPositionConfigurationResponse

### Solvers
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.PositionSolverDetails'>
- **Required**: Yes

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetPositionEstimateRequest

### WiFiAccessPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WiFiAccessPoint]]

### CellTowers
- **Type**: <class 'NoneType'>

### Ip
- **Type**: <class 'NoneType'>

### Gnss
- **Type**: <class 'NoneType'>

### Timestamp
- **Type**: <class 'NoneType'>


# GetPositionEstimateResponse

### GeoJsonPayload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetPositionRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes


# GetPositionResponse

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Accuracy
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Accuracy'>
- **Required**: Yes

### SolverType
- **Type**: typing.Literal['GNSS']
- **Required**: Yes

### SolverProvider
- **Type**: typing.Literal['Semtech']
- **Required**: Yes

### SolverVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceEventConfigurationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'FuotaTaskId', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']
- **Required**: Yes

### PartnerType
- **Type**: typing.Optional[typing.Literal['Sidewalk']]


# GetResourceEventConfigurationResponse

### DeviceRegistrationState
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.DeviceRegistrationStateEventConfiguration'>
- **Required**: Yes

### Proximity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ProximityEventConfiguration'>
- **Required**: Yes

### Join
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.JoinEventConfiguration'>
- **Required**: Yes

### ConnectionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ConnectionStatusEventConfiguration'>
- **Required**: Yes

### MessageDeliveryStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MessageDeliveryStatusEventConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceLogLevelRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceLogLevelResponse

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePositionRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes


# GetResourcePositionResponse

### GeoJsonPayload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceEndpointRequest

### ServiceType
- **Type**: typing.Optional[typing.Literal['CUPS', 'LNS']]


# GetServiceEndpointResponse

### ServiceType
- **Type**: typing.Literal['CUPS', 'LNS']
- **Required**: Yes

### ServiceEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ServerTrust
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceProfileRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceProfileResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGetServiceProfileInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessDeviceImportTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessDeviceImportTaskResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkGetStartImportInfo'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'DELETING', 'FAILED', 'INITIALIZED', 'INITIALIZING', 'PENDING']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### InitializedImportedDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### PendingImportedDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### OnboardedImportedDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### FailedImportedDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessDeviceRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'SidewalkManufacturingSn', 'ThingName', 'WirelessDeviceId']
- **Required**: Yes


# GetWirelessDeviceResponse

### Type
- **Type**: typing.Literal['LoRaWAN', 'Sidewalk']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANDeviceOutput'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkDevice'>
- **Required**: Yes

### Positioning
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessDeviceStatisticsRequest

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessDeviceStatisticsResponse

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUplinkReceivedAt
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANDeviceMetadata'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkDeviceMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessGatewayCertificateRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayCertificateResponse

### IotCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWANNetworkServerCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessGatewayFirmwareInformationRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayFirmwareInformationResponse

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayCurrentVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessGatewayRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['GatewayEui', 'ThingName', 'WirelessGatewayId']
- **Required**: Yes


# GetWirelessGatewayResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayOutput'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ThingName
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessGatewayStatisticsRequest

### WirelessGatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayStatisticsResponse

### WirelessGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUplinkReceivedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionStatus
- **Type**: typing.Literal['Connected', 'Disconnected']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessGatewayTaskDefinitionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayTaskDefinitionResponse

### AutoCreateTasks
- **Type**: <class 'bool'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Update
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.UpdateWirelessGatewayTaskCreate'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWirelessGatewayTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayTaskResponse

### WirelessGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessGatewayTaskDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUplinkReceivedAt
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'FIRST_RETRY', 'IN_PROGRESS', 'PENDING', 'SECOND_RETRY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# GlobalIdentity

### Lac
- **Type**: <class 'int'>
- **Required**: Yes

### GeranCid
- **Type**: <class 'int'>
- **Required**: Yes


# Gnss

### Payload
- **Type**: <class 'str'>
- **Required**: Yes

### CaptureTime
- **Type**: typing.Optional[float]

### CaptureTimeAccuracy
- **Type**: typing.Optional[float]

### AssistPosition
- **Type**: typing.Optional[typing.List[float]]

### AssistAltitude
- **Type**: typing.Optional[float]

### Use2DSolver
- **Type**: typing.Optional[bool]


# GsmLocalId

### Bsic
- **Type**: <class 'int'>
- **Required**: Yes

### Bcch
- **Type**: <class 'int'>
- **Required**: Yes


# GsmNmrObj

### Bsic
- **Type**: <class 'int'>
- **Required**: Yes

### Bcch
- **Type**: <class 'int'>
- **Required**: Yes

### RxLevel
- **Type**: typing.Optional[int]

### GlobalIdentity
- **Type**: <class 'NoneType'>


# GsmObj

### Mcc
- **Type**: <class 'int'>
- **Required**: Yes

### Mnc
- **Type**: <class 'int'>
- **Required**: Yes

### Lac
- **Type**: <class 'int'>
- **Required**: Yes

### GeranCid
- **Type**: <class 'int'>
- **Required**: Yes

### GsmLocalId
- **Type**: <class 'NoneType'>

### GsmTimingAdvance
- **Type**: typing.Optional[int]

### RxLevel
- **Type**: typing.Optional[int]

### GsmNmr
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.GsmNmrObj]]


# ImportedSidewalkDevice

### SidewalkManufacturingSn
- **Type**: typing.Optional[str]

### OnboardingStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'ONBOARDED', 'PENDING']]

### OnboardingStatusReason
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# ImportedWirelessDevice

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ImportedSidewalkDevice]


# Ip

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes


# JoinEventConfiguration

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANJoinEventNotificationConfigurations]

### WirelessDeviceIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# JoinResourceTypeEventConfiguration

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANJoinResourceTypeEventConfiguration]


# ListDestinationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDestinationsResponse

### DestinationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Destinations]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceProfilesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### DeviceProfileType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# ListDeviceProfilesResponse

### DeviceProfileList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.DeviceProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesForWirelessDeviceImportTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'ONBOARDED', 'PENDING']]


# ListDevicesForWirelessDeviceImportTaskResponse

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### ImportedWirelessDeviceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ImportedWirelessDevice]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventConfigurationsRequest

### ResourceType
- **Type**: typing.Literal['FuotaTask', 'SidewalkAccount', 'WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEventConfigurationsResponse

### EventConfigurationsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.EventConfigurationItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFuotaTasksRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFuotaTasksResponse

### FuotaTaskList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.FuotaTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMulticastGroupsByFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMulticastGroupsByFuotaTaskResponse

### MulticastGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MulticastGroupByFuotaTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMulticastGroupsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMulticastGroupsResponse

### MulticastGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MulticastGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNetworkAnalyzerConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNetworkAnalyzerConfigurationsResponse

### NetworkAnalyzerConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.NetworkAnalyzerConfigurations]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerAccountsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPartnerAccountsResponse

### Sidewalk
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkAccountInfoWithFingerprint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPositionConfigurationsRequest

### ResourceType
- **Type**: typing.Optional[typing.Literal['WirelessDevice', 'WirelessGateway']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPositionConfigurationsResponse

### PositionConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.PositionConfigurationItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueuedMessagesRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WirelessDeviceType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# ListQueuedMessagesResponse

### DownlinkQueueMessagesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.DownlinkQueueMessage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceProfilesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServiceProfilesResponse

### ServiceProfileList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ServiceProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# ListWirelessDeviceImportTasksRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListWirelessDeviceImportTasksResponse

### WirelessDeviceImportTaskList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessDeviceImportTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWirelessDevicesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### DestinationName
- **Type**: typing.Optional[str]

### DeviceProfileId
- **Type**: typing.Optional[str]

### ServiceProfileId
- **Type**: typing.Optional[str]

### WirelessDeviceType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]

### FuotaTaskId
- **Type**: typing.Optional[str]

### MulticastGroupId
- **Type**: typing.Optional[str]


# ListWirelessDevicesResponse

### WirelessDeviceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessDeviceStatistics]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWirelessGatewayTaskDefinitionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### TaskDefinitionType
- **Type**: typing.Optional[typing.Literal['UPDATE']]


# ListWirelessGatewayTaskDefinitionsResponse

### TaskDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.UpdateWirelessGatewayTaskEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWirelessGatewaysRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWirelessGatewaysResponse

### WirelessGatewayList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessGatewayStatistics]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoRaWANConnectionStatusEventNotificationConfigurations

### GatewayEuiEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# LoRaWANConnectionStatusResourceTypeEventConfiguration

### WirelessGatewayEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# LoRaWANDevice

### DevEui
- **Type**: typing.Optional[str]

### DeviceProfileId
- **Type**: typing.Optional[str]

### ServiceProfileId
- **Type**: typing.Optional[str]

### OtaaV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.OtaaV11]

### OtaaV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.OtaaV10X]

### AbpV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.AbpV11]

### AbpV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.AbpV10X]

### FPorts
- **Type**: <class 'NoneType'>


# LoRaWANDeviceMetadata

### DevEui
- **Type**: typing.Optional[str]

### FPort
- **Type**: typing.Optional[int]

### DataRate
- **Type**: typing.Optional[int]

### Frequency
- **Type**: typing.Optional[int]

### Timestamp
- **Type**: typing.Optional[str]

### Gateways
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayMetadata]]

### PublicGateways
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANPublicGatewayMetadata]]


# LoRaWANDeviceOutput

### DevEui
- **Type**: typing.Optional[str]

### DeviceProfileId
- **Type**: typing.Optional[str]

### ServiceProfileId
- **Type**: typing.Optional[str]

### OtaaV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.OtaaV11]

### OtaaV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.OtaaV10X]

### AbpV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.AbpV11]

### AbpV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.AbpV10X]

### FPorts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.FPortsOutput]


# LoRaWANDeviceProfile

### SupportsClassB
- **Type**: typing.Optional[bool]

### ClassBTimeout
- **Type**: typing.Optional[int]

### PingSlotPeriod
- **Type**: typing.Optional[int]

### PingSlotDr
- **Type**: typing.Optional[int]

### PingSlotFreq
- **Type**: typing.Optional[int]

### SupportsClassC
- **Type**: typing.Optional[bool]

### ClassCTimeout
- **Type**: typing.Optional[int]

### MacVersion
- **Type**: typing.Optional[str]

### RegParamsRevision
- **Type**: typing.Optional[str]

### RxDelay1
- **Type**: typing.Optional[int]

### RxDrOffset1
- **Type**: typing.Optional[int]

### RxDataRate2
- **Type**: typing.Optional[int]

### RxFreq2
- **Type**: typing.Optional[int]

### FactoryPresetFreqsList
- **Type**: typing.Optional[typing.List[int]]

### MaxEirp
- **Type**: typing.Optional[int]

### MaxDutyCycle
- **Type**: typing.Optional[int]

### RfRegion
- **Type**: typing.Optional[str]

### SupportsJoin
- **Type**: typing.Optional[bool]

### Supports32BitFCnt
- **Type**: typing.Optional[bool]


# LoRaWANDeviceProfileOutput

### SupportsClassB
- **Type**: typing.Optional[bool]

### ClassBTimeout
- **Type**: typing.Optional[int]

### PingSlotPeriod
- **Type**: typing.Optional[int]

### PingSlotDr
- **Type**: typing.Optional[int]

### PingSlotFreq
- **Type**: typing.Optional[int]

### SupportsClassC
- **Type**: typing.Optional[bool]

### ClassCTimeout
- **Type**: typing.Optional[int]

### MacVersion
- **Type**: typing.Optional[str]

### RegParamsRevision
- **Type**: typing.Optional[str]

### RxDelay1
- **Type**: typing.Optional[int]

### RxDrOffset1
- **Type**: typing.Optional[int]

### RxDataRate2
- **Type**: typing.Optional[int]

### RxFreq2
- **Type**: typing.Optional[int]

### FactoryPresetFreqsList
- **Type**: typing.Optional[typing.List[int]]

### MaxEirp
- **Type**: typing.Optional[int]

### MaxDutyCycle
- **Type**: typing.Optional[int]

### RfRegion
- **Type**: typing.Optional[str]

### SupportsJoin
- **Type**: typing.Optional[bool]

### Supports32BitFCnt
- **Type**: typing.Optional[bool]


# LoRaWANFuotaTask

### RfRegion
- **Type**: typing.Optional[typing.Literal['AS923-1', 'AS923-2', 'AS923-3', 'AS923-4', 'AU915', 'CN470', 'CN779', 'EU433', 'EU868', 'IN865', 'KR920', 'RU864', 'US915']]


# LoRaWANFuotaTaskGetInfo

### RfRegion
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# LoRaWANGateway

### GatewayEui
- **Type**: typing.Optional[str]

### RfRegion
- **Type**: typing.Optional[str]

### JoinEuiFilters
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### NetIdFilters
- **Type**: typing.Optional[typing.List[str]]

### SubBands
- **Type**: typing.Optional[typing.List[int]]

### Beaconing
- **Type**: <class 'NoneType'>

### MaxEirp
- **Type**: typing.Optional[float]


# LoRaWANGatewayCurrentVersion

### CurrentVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayVersion]


# LoRaWANGatewayMetadata

### GatewayEui
- **Type**: typing.Optional[str]

### Snr
- **Type**: typing.Optional[float]

### Rssi
- **Type**: typing.Optional[float]


# LoRaWANGatewayOutput

### GatewayEui
- **Type**: typing.Optional[str]

### RfRegion
- **Type**: typing.Optional[str]

### JoinEuiFilters
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### NetIdFilters
- **Type**: typing.Optional[typing.List[str]]

### SubBands
- **Type**: typing.Optional[typing.List[int]]

### Beaconing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.BeaconingOutput]

### MaxEirp
- **Type**: typing.Optional[float]


# LoRaWANGatewayVersion

### PackageVersion
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### Station
- **Type**: typing.Optional[str]


# LoRaWANGetServiceProfileInfo

### UlRate
- **Type**: typing.Optional[int]

### UlBucketSize
- **Type**: typing.Optional[int]

### UlRatePolicy
- **Type**: typing.Optional[str]

### DlRate
- **Type**: typing.Optional[int]

### DlBucketSize
- **Type**: typing.Optional[int]

### DlRatePolicy
- **Type**: typing.Optional[str]

### AddGwMetadata
- **Type**: typing.Optional[bool]

### DevStatusReqFreq
- **Type**: typing.Optional[int]

### ReportDevStatusBattery
- **Type**: typing.Optional[bool]

### ReportDevStatusMargin
- **Type**: typing.Optional[bool]

### DrMin
- **Type**: typing.Optional[int]

### DrMax
- **Type**: typing.Optional[int]

### ChannelMask
- **Type**: typing.Optional[str]

### PrAllowed
- **Type**: typing.Optional[bool]

### HrAllowed
- **Type**: typing.Optional[bool]

### RaAllowed
- **Type**: typing.Optional[bool]

### NwkGeoLoc
- **Type**: typing.Optional[bool]

### TargetPer
- **Type**: typing.Optional[int]

### MinGwDiversity
- **Type**: typing.Optional[int]


# LoRaWANJoinEventNotificationConfigurations

### DevEuiEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# LoRaWANJoinResourceTypeEventConfiguration

### WirelessDeviceEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# LoRaWANListDevice

### DevEui
- **Type**: typing.Optional[str]


# LoRaWANMulticast

### RfRegion
- **Type**: typing.Optional[typing.Literal['AS923-1', 'AS923-2', 'AS923-3', 'AS923-4', 'AU915', 'CN470', 'CN779', 'EU433', 'EU868', 'IN865', 'KR920', 'RU864', 'US915']]

### DlClass
- **Type**: typing.Optional[typing.Literal['ClassB', 'ClassC']]

### ParticipatingGateways
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ParticipatingGatewaysMulticast, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ParticipatingGatewaysMulticastOutput, NoneType]


# LoRaWANMulticastGet

### RfRegion
- **Type**: typing.Optional[typing.Literal['AS923-1', 'AS923-2', 'AS923-3', 'AS923-4', 'AU915', 'CN470', 'CN779', 'EU433', 'EU868', 'IN865', 'KR920', 'RU864', 'US915']]

### DlClass
- **Type**: typing.Optional[typing.Literal['ClassB', 'ClassC']]

### NumberOfDevicesRequested
- **Type**: typing.Optional[int]

### NumberOfDevicesInGroup
- **Type**: typing.Optional[int]

### ParticipatingGateways
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ParticipatingGatewaysMulticastOutput]


# LoRaWANMulticastMetadata

### FPort
- **Type**: typing.Optional[int]


# LoRaWANMulticastSession

### DlDr
- **Type**: typing.Optional[int]

### DlFreq
- **Type**: typing.Optional[int]

### SessionStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SessionTimeout
- **Type**: typing.Optional[int]

### PingSlotPeriod
- **Type**: typing.Optional[int]


# LoRaWANMulticastSessionOutput

### DlDr
- **Type**: typing.Optional[int]

### DlFreq
- **Type**: typing.Optional[int]

### SessionStartTime
- **Type**: typing.Optional[datetime.datetime]

### SessionTimeout
- **Type**: typing.Optional[int]

### PingSlotPeriod
- **Type**: typing.Optional[int]


# LoRaWANPublicGatewayMetadata

### ProviderNetId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Rssi
- **Type**: typing.Optional[float]

### Snr
- **Type**: typing.Optional[float]

### RfRegion
- **Type**: typing.Optional[str]

### DlAllowed
- **Type**: typing.Optional[bool]


# LoRaWANSendDataToDevice

### FPort
- **Type**: typing.Optional[int]

### ParticipatingGateways
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ParticipatingGateways, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ParticipatingGatewaysOutput, NoneType]


# LoRaWANSendDataToDeviceOutput

### FPort
- **Type**: typing.Optional[int]

### ParticipatingGateways
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ParticipatingGatewaysOutput]


# LoRaWANServiceProfile

### AddGwMetadata
- **Type**: typing.Optional[bool]

### DrMin
- **Type**: typing.Optional[int]

### DrMax
- **Type**: typing.Optional[int]

### PrAllowed
- **Type**: typing.Optional[bool]

### RaAllowed
- **Type**: typing.Optional[bool]


# LoRaWANStartFuotaTask

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# LoRaWANUpdateDevice

### DeviceProfileId
- **Type**: typing.Optional[str]

### ServiceProfileId
- **Type**: typing.Optional[str]

### AbpV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.UpdateAbpV11]

### AbpV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.UpdateAbpV10X]

### FPorts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.UpdateFPorts]


# LoRaWANUpdateGatewayTaskCreate

### UpdateSignature
- **Type**: typing.Optional[str]

### SigKeyCrc
- **Type**: typing.Optional[int]

### CurrentVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayVersion]

### UpdateVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayVersion]


# LoRaWANUpdateGatewayTaskEntry

### CurrentVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayVersion]

### UpdateVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayVersion]


# LteLocalId

### Pci
- **Type**: <class 'int'>
- **Required**: Yes

### Earfcn
- **Type**: <class 'int'>
- **Required**: Yes


# LteNmrObj

### Pci
- **Type**: <class 'int'>
- **Required**: Yes

### Earfcn
- **Type**: <class 'int'>
- **Required**: Yes

### EutranCid
- **Type**: <class 'int'>
- **Required**: Yes

### Rsrp
- **Type**: typing.Optional[int]

### Rsrq
- **Type**: typing.Optional[float]


# LteObj

### Mcc
- **Type**: <class 'int'>
- **Required**: Yes

### Mnc
- **Type**: <class 'int'>
- **Required**: Yes

### EutranCid
- **Type**: <class 'int'>
- **Required**: Yes

### Tac
- **Type**: typing.Optional[int]

### LteLocalId
- **Type**: <class 'NoneType'>

### LteTimingAdvance
- **Type**: typing.Optional[int]

### Rsrp
- **Type**: typing.Optional[int]

### Rsrq
- **Type**: typing.Optional[float]

### NrCapable
- **Type**: typing.Optional[bool]

### LteNmr
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LteNmrObj]]


# MessageDeliveryStatusEventConfiguration

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkEventNotificationConfigurations]

### WirelessDeviceIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# MessageDeliveryStatusResourceTypeEventConfiguration

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkResourceTypeEventConfiguration]


# MetricQueryValue

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]

### Sum
- **Type**: typing.Optional[float]

### Avg
- **Type**: typing.Optional[float]

### Std
- **Type**: typing.Optional[float]

### P90
- **Type**: typing.Optional[float]


# MulticastGroup

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# MulticastGroupByFuotaTask

### Id
- **Type**: typing.Optional[str]


# MulticastWirelessMetadata

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANMulticastMetadata]


# NetworkAnalyzerConfigurations

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# OtaaV10X

### AppKey
- **Type**: typing.Optional[str]

### AppEui
- **Type**: typing.Optional[str]

### JoinEui
- **Type**: typing.Optional[str]

### GenAppKey
- **Type**: typing.Optional[str]


# OtaaV11

### AppKey
- **Type**: typing.Optional[str]

### NwkKey
- **Type**: typing.Optional[str]

### JoinEui
- **Type**: typing.Optional[str]


# ParticipatingGateways

### DownlinkMode
- **Type**: typing.Literal['CONCURRENT', 'SEQUENTIAL', 'USING_UPLINK_GATEWAY']
- **Required**: Yes

### GatewayList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.GatewayListItem]
- **Required**: Yes

### TransmissionInterval
- **Type**: <class 'int'>
- **Required**: Yes


# ParticipatingGatewaysMulticast

### GatewayList
- **Type**: typing.Optional[typing.List[str]]

### TransmissionInterval
- **Type**: typing.Optional[int]


# ParticipatingGatewaysMulticastOutput

### GatewayList
- **Type**: typing.Optional[typing.List[str]]

### TransmissionInterval
- **Type**: typing.Optional[int]


# ParticipatingGatewaysOutput

### DownlinkMode
- **Type**: typing.Literal['CONCURRENT', 'SEQUENTIAL', 'USING_UPLINK_GATEWAY']
- **Required**: Yes

### GatewayList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.GatewayListItem]
- **Required**: Yes

### TransmissionInterval
- **Type**: <class 'int'>
- **Required**: Yes


# PositionConfigurationItem

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['WirelessDevice', 'WirelessGateway']]

### Solvers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.PositionSolverDetails]

### Destination
- **Type**: typing.Optional[str]


# PositionSolverConfigurations

### SemtechGnss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SemtechGnssConfiguration]


# PositionSolverDetails

### SemtechGnss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SemtechGnssDetail]


# Positioning

### ClockSync
- **Type**: typing.Optional[int]

### Stream
- **Type**: typing.Optional[int]

### Gnss
- **Type**: typing.Optional[int]


# ProximityEventConfiguration

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkEventNotificationConfigurations]

### WirelessDeviceIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# ProximityResourceTypeEventConfiguration

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkResourceTypeEventConfiguration]


# PutPositionConfigurationRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### Solvers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.PositionSolverConfigurations]

### Destination
- **Type**: typing.Optional[str]


# PutResourceLogLevelRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# ResetResourceLogLevelRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes


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


# SemtechGnssConfiguration

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Fec
- **Type**: typing.Literal['NONE', 'ROSE']
- **Required**: Yes


# SemtechGnssDetail

### Provider
- **Type**: typing.Optional[typing.Literal['Semtech']]

### Type
- **Type**: typing.Optional[typing.Literal['GNSS']]

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Fec
- **Type**: typing.Optional[typing.Literal['NONE', 'ROSE']]


# SendDataToMulticastGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PayloadData
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MulticastWirelessMetadata'>
- **Required**: Yes


# SendDataToMulticastGroupResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# SendDataToWirelessDeviceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### TransmitMode
- **Type**: <class 'int'>
- **Required**: Yes

### PayloadData
- **Type**: <class 'str'>
- **Required**: Yes


# SendDataToWirelessDeviceResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# ServiceProfile

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# SessionKeysAbpV10X

### NwkSKey
- **Type**: typing.Optional[str]

### AppSKey
- **Type**: typing.Optional[str]


# SessionKeysAbpV11

### FNwkSIntKey
- **Type**: typing.Optional[str]

### SNwkSIntKey
- **Type**: typing.Optional[str]

### NwkSEncKey
- **Type**: typing.Optional[str]

### AppSKey
- **Type**: typing.Optional[str]


# SidewalkAccountInfo

### AmazonId
- **Type**: typing.Optional[str]

### AppServerPrivateKey
- **Type**: typing.Optional[str]


# SidewalkAccountInfoWithFingerprint

### AmazonId
- **Type**: typing.Optional[str]

### Fingerprint
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# SidewalkCreateWirelessDevice

### DeviceProfileId
- **Type**: typing.Optional[str]


# SidewalkDevice

### AmazonId
- **Type**: typing.Optional[str]

### SidewalkId
- **Type**: typing.Optional[str]

### SidewalkManufacturingSn
- **Type**: typing.Optional[str]

### DeviceCertificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.CertificateList]]

### PrivateKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.CertificateList]]

### DeviceProfileId
- **Type**: typing.Optional[str]

### CertificateId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'PROVISIONED', 'REGISTERED', 'UNKNOWN']]


# SidewalkDeviceMetadata

### Rssi
- **Type**: typing.Optional[int]

### BatteryLevel
- **Type**: typing.Optional[typing.Literal['critical', 'low', 'normal']]

### Event
- **Type**: typing.Optional[typing.Literal['ack', 'discovered', 'lost', 'nack', 'passthrough']]

### DeviceState
- **Type**: typing.Optional[typing.Literal['Provisioned', 'RegisteredNotSeen', 'RegisteredReachable', 'RegisteredUnreachable']]


# SidewalkEventNotificationConfigurations

### AmazonIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SidewalkGetDeviceProfile

### ApplicationServerPublicKey
- **Type**: typing.Optional[str]

### QualificationStatus
- **Type**: typing.Optional[bool]

### DakCertificateMetadata
- **Type**: typing.Optional[typing.List[NoneType]]


# SidewalkGetStartImportInfo

### DeviceCreationFileList
- **Type**: typing.Optional[typing.List[str]]

### Role
- **Type**: typing.Optional[str]


# SidewalkListDevice

### AmazonId
- **Type**: typing.Optional[str]

### SidewalkId
- **Type**: typing.Optional[str]

### SidewalkManufacturingSn
- **Type**: typing.Optional[str]

### DeviceCertificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.CertificateList]]

### DeviceProfileId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'PROVISIONED', 'REGISTERED', 'UNKNOWN']]


# SidewalkResourceTypeEventConfiguration

### WirelessDeviceEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SidewalkSendDataToDevice

### Seq
- **Type**: typing.Optional[int]

### MessageType
- **Type**: typing.Optional[typing.Literal['CUSTOM_COMMAND_ID_GET', 'CUSTOM_COMMAND_ID_NOTIFY', 'CUSTOM_COMMAND_ID_RESP', 'CUSTOM_COMMAND_ID_SET']]

### AckModeRetryDurationSecs
- **Type**: typing.Optional[int]


# SidewalkSingleStartImportInfo

### SidewalkManufacturingSn
- **Type**: typing.Optional[str]


# SidewalkStartImportInfo

### DeviceCreationFile
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]


# SidewalkUpdateAccount

### AppServerPrivateKey
- **Type**: typing.Optional[str]


# SidewalkUpdateImportInfo

### DeviceCreationFile
- **Type**: typing.Optional[str]


# StartBulkAssociateWirelessDeviceWithMulticastGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]


# StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]


# StartFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANStartFuotaTask]


# StartMulticastGroupSessionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANMulticastSession, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANMulticastSessionOutput]
- **Required**: Yes


# StartSingleWirelessDeviceImportTaskRequest

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkSingleStartImportInfo'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]


# StartSingleWirelessDeviceImportTaskResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# StartWirelessDeviceImportTaskRequest

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkStartImportInfo'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]]


# StartWirelessDeviceImportTaskResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# SummaryMetricConfiguration

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SummaryMetricQuery

### QueryId
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[typing.Literal['AwsAccountActiveDeviceCount', 'AwsAccountActiveGatewayCount', 'AwsAccountDeviceCount', 'AwsAccountDownlinkCount', 'AwsAccountGatewayCount', 'AwsAccountJoinAcceptCount', 'AwsAccountJoinRequestCount', 'AwsAccountRoamingDownlinkCount', 'AwsAccountRoamingUplinkCount', 'AwsAccountUplinkCount', 'AwsAccountUplinkLostCount', 'AwsAccountUplinkLostRate', 'DeviceDownlinkCount', 'DeviceJoinAcceptCount', 'DeviceJoinRequestCount', 'DeviceRSSI', 'DeviceRoamingDownlinkCount', 'DeviceRoamingRSSI', 'DeviceRoamingSNR', 'DeviceRoamingUplinkCount', 'DeviceSNR', 'DeviceUplinkCount', 'DeviceUplinkLostCount', 'DeviceUplinkLostRate', 'GatewayDownTime', 'GatewayDownlinkCount', 'GatewayJoinAcceptCount', 'GatewayJoinRequestCount', 'GatewayRSSI', 'GatewaySNR', 'GatewayUpTime', 'GatewayUplinkCount']]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Dimension]]

### AggregationPeriod
- **Type**: typing.Optional[typing.Literal['OneDay', 'OneHour', 'OneWeek']]

### StartTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# SummaryMetricQueryResult

### QueryId
- **Type**: typing.Optional[str]

### QueryStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Succeeded']]

### Error
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[typing.Literal['AwsAccountActiveDeviceCount', 'AwsAccountActiveGatewayCount', 'AwsAccountDeviceCount', 'AwsAccountDownlinkCount', 'AwsAccountGatewayCount', 'AwsAccountJoinAcceptCount', 'AwsAccountJoinRequestCount', 'AwsAccountRoamingDownlinkCount', 'AwsAccountRoamingUplinkCount', 'AwsAccountUplinkCount', 'AwsAccountUplinkLostCount', 'AwsAccountUplinkLostRate', 'DeviceDownlinkCount', 'DeviceJoinAcceptCount', 'DeviceJoinRequestCount', 'DeviceRSSI', 'DeviceRoamingDownlinkCount', 'DeviceRoamingRSSI', 'DeviceRoamingSNR', 'DeviceRoamingUplinkCount', 'DeviceSNR', 'DeviceUplinkCount', 'DeviceUplinkLostCount', 'DeviceUplinkLostRate', 'GatewayDownTime', 'GatewayDownlinkCount', 'GatewayJoinAcceptCount', 'GatewayJoinRequestCount', 'GatewayRSSI', 'GatewaySNR', 'GatewayUpTime', 'GatewayUplinkCount']]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Dimension]]

### AggregationPeriod
- **Type**: typing.Optional[typing.Literal['OneDay', 'OneHour', 'OneWeek']]

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### EndTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MetricQueryValue]]

### Unit
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.Tag]
- **Required**: Yes


# TdscdmaLocalId

### Uarfcn
- **Type**: <class 'int'>
- **Required**: Yes

### CellParams
- **Type**: <class 'int'>
- **Required**: Yes


# TdscdmaNmrObj

### Uarfcn
- **Type**: <class 'int'>
- **Required**: Yes

### CellParams
- **Type**: <class 'int'>
- **Required**: Yes

### UtranCid
- **Type**: typing.Optional[int]

### Rscp
- **Type**: typing.Optional[int]

### PathLoss
- **Type**: typing.Optional[int]


# TdscdmaObj

### Mcc
- **Type**: <class 'int'>
- **Required**: Yes

### Mnc
- **Type**: <class 'int'>
- **Required**: Yes

### UtranCid
- **Type**: <class 'int'>
- **Required**: Yes

### Lac
- **Type**: typing.Optional[int]

### TdscdmaLocalId
- **Type**: <class 'NoneType'>

### TdscdmaTimingAdvance
- **Type**: typing.Optional[int]

### Rscp
- **Type**: typing.Optional[int]

### PathLoss
- **Type**: typing.Optional[int]

### TdscdmaNmr
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.TdscdmaNmrObj]]


# TestWirelessDeviceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# TestWirelessDeviceResponse

### Result
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ResponseMetadata'>
- **Required**: Yes


# TraceContent

### WirelessDeviceFrameInfo
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ERROR', 'INFO']]

### MulticastFrameInfo
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAbpV10X

### FCntStart
- **Type**: typing.Optional[int]


# UpdateAbpV11

### FCntStart
- **Type**: typing.Optional[int]


# UpdateDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionType
- **Type**: typing.Optional[typing.Literal['MqttTopic', 'RuleName']]

### Expression
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateEventConfigurationByResourceTypesRequest

### DeviceRegistrationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.DeviceRegistrationStateResourceTypeEventConfiguration]

### Proximity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ProximityResourceTypeEventConfiguration]

### Join
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.JoinResourceTypeEventConfiguration]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ConnectionStatusResourceTypeEventConfiguration]

### MessageDeliveryStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MessageDeliveryStatusResourceTypeEventConfiguration]


# UpdateFPorts

### Positioning
- **Type**: <class 'NoneType'>

### Applications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ApplicationConfig]]


# UpdateFuotaTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANFuotaTask]

### FirmwareUpdateImage
- **Type**: typing.Optional[str]

### FirmwareUpdateRole
- **Type**: typing.Optional[str]

### RedundancyPercent
- **Type**: typing.Optional[int]

### FragmentSizeBytes
- **Type**: typing.Optional[int]

### FragmentIntervalMS
- **Type**: typing.Optional[int]

### Descriptor
- **Type**: typing.Optional[str]


# UpdateLogLevelsByResourceTypesRequest

### DefaultLogLevel
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ERROR', 'INFO']]

### FuotaTaskLogOptions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.FuotaTaskLogOption, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.FuotaTaskLogOptionOutput]]]

### WirelessDeviceLogOptions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessDeviceLogOption, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessDeviceLogOptionOutput]]]

### WirelessGatewayLogOptions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessGatewayLogOption, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessGatewayLogOptionOutput]]]


# UpdateMetricConfigurationRequest

### SummaryMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SummaryMetricConfiguration]


# UpdateMulticastGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANMulticast]


# UpdateNetworkAnalyzerConfigurationRequest

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### TraceContent
- **Type**: <class 'NoneType'>

### WirelessDevicesToAdd
- **Type**: typing.Optional[typing.List[str]]

### WirelessDevicesToRemove
- **Type**: typing.Optional[typing.List[str]]

### WirelessGatewaysToAdd
- **Type**: typing.Optional[typing.List[str]]

### WirelessGatewaysToRemove
- **Type**: typing.Optional[typing.List[str]]

### Description
- **Type**: typing.Optional[str]

### MulticastGroupsToAdd
- **Type**: typing.Optional[typing.List[str]]

### MulticastGroupsToRemove
- **Type**: typing.Optional[typing.List[str]]


# UpdatePartnerAccountRequest

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkUpdateAccount'>
- **Required**: Yes

### PartnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerType
- **Type**: typing.Literal['Sidewalk']
- **Required**: Yes


# UpdatePositionRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes


# UpdateResourceEventConfigurationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'FuotaTaskId', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']
- **Required**: Yes

### PartnerType
- **Type**: typing.Optional[typing.Literal['Sidewalk']]

### DeviceRegistrationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.DeviceRegistrationStateEventConfiguration]

### Proximity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ProximityEventConfiguration]

### Join
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.JoinEventConfiguration]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.ConnectionStatusEventConfiguration]

### MessageDeliveryStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.MessageDeliveryStatusEventConfiguration]


# UpdateResourcePositionRequest

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### GeoJsonPayload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# UpdateWirelessDeviceImportTaskRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkUpdateImportInfo'>
- **Required**: Yes


# UpdateWirelessDeviceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANUpdateDevice]

### Positioning
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UpdateWirelessGatewayRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### JoinEuiFilters
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### NetIdFilters
- **Type**: typing.Optional[typing.List[str]]

### MaxEirp
- **Type**: typing.Optional[float]


# UpdateWirelessGatewayTaskCreate

### UpdateDataSource
- **Type**: typing.Optional[str]

### UpdateDataRole
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANUpdateGatewayTaskCreate]


# UpdateWirelessGatewayTaskEntry

### Id
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANUpdateGatewayTaskEntry]

### Arn
- **Type**: typing.Optional[str]


# WcdmaLocalId

### Uarfcndl
- **Type**: <class 'int'>
- **Required**: Yes

### Psc
- **Type**: <class 'int'>
- **Required**: Yes


# WcdmaNmrObj

### Uarfcndl
- **Type**: <class 'int'>
- **Required**: Yes

### Psc
- **Type**: <class 'int'>
- **Required**: Yes

### UtranCid
- **Type**: <class 'int'>
- **Required**: Yes

### Rscp
- **Type**: typing.Optional[int]

### PathLoss
- **Type**: typing.Optional[int]


# WcdmaObj

### Mcc
- **Type**: <class 'int'>
- **Required**: Yes

### Mnc
- **Type**: <class 'int'>
- **Required**: Yes

### UtranCid
- **Type**: <class 'int'>
- **Required**: Yes

### Lac
- **Type**: typing.Optional[int]

### WcdmaLocalId
- **Type**: <class 'NoneType'>

### Rscp
- **Type**: typing.Optional[int]

### PathLoss
- **Type**: typing.Optional[int]

### WcdmaNmr
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WcdmaNmrObj]]


# WiFiAccessPoint

### MacAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Rss
- **Type**: <class 'int'>
- **Required**: Yes


# WirelessDeviceEventLogOption

### Event
- **Type**: typing.Literal['Downlink_Data', 'Join', 'Registration', 'Rejoin', 'Uplink_Data']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# WirelessDeviceImportTask

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### DestinationName
- **Type**: typing.Optional[str]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkGetStartImportInfo]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'DELETING', 'FAILED', 'INITIALIZED', 'INITIALIZING', 'PENDING']]

### StatusReason
- **Type**: typing.Optional[str]

### InitializedImportedDeviceCount
- **Type**: typing.Optional[int]

### PendingImportedDeviceCount
- **Type**: typing.Optional[int]

### OnboardedImportedDeviceCount
- **Type**: typing.Optional[int]

### FailedImportedDeviceCount
- **Type**: typing.Optional[int]


# WirelessDeviceLogOption

### Type
- **Type**: typing.Literal['LoRaWAN', 'Sidewalk']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessDeviceEventLogOption]]


# WirelessDeviceLogOptionOutput

### Type
- **Type**: typing.Literal['LoRaWAN', 'Sidewalk']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessDeviceEventLogOption]]


# WirelessDeviceStatistics

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]

### Name
- **Type**: typing.Optional[str]

### DestinationName
- **Type**: typing.Optional[str]

### LastUplinkReceivedAt
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANListDevice]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkListDevice]

### FuotaDeviceStatus
- **Type**: typing.Optional[typing.Literal['Device_exist_in_conflict_fuota_task', 'FragAlgo_unsupported', 'FragIndex_unsupported', 'Initial', 'MICError', 'MemoryError', 'MissingFrag', 'Not_enough_memory', 'Package_Not_Supported', 'SessionCnt_replay', 'Successful', 'Wrong_descriptor']]

### MulticastDeviceStatus
- **Type**: typing.Optional[str]

### McGroupId
- **Type**: typing.Optional[int]


# WirelessGatewayEventLogOption

### Event
- **Type**: typing.Literal['CUPS_Request', 'Certificate']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# WirelessGatewayLogOption

### Type
- **Type**: typing.Literal['LoRaWAN']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessGatewayEventLogOption]]


# WirelessGatewayLogOptionOutput

### Type
- **Type**: typing.Literal['LoRaWAN']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.WirelessGatewayEventLogOption]]


# WirelessGatewayStatistics

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANGatewayOutput]

### LastUplinkReceivedAt
- **Type**: typing.Optional[str]


# WirelessMetadata

### LoRaWAN
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANSendDataToDevice, aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.LoRaWANSendDataToDeviceOutput, NoneType]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless.iotwireless_classes.SidewalkSendDataToDevice]



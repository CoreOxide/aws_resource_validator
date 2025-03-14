# Iotwireless Classes

# AbpV10XTypeDef

### DevAddr
- **Type**: typing.Optional[str]

### SessionKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SessionKeysAbpV10XTypeDef]

### FCntStart
- **Type**: typing.Optional[int]


# AbpV11TypeDef

### DevAddr
- **Type**: typing.Optional[str]

### SessionKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SessionKeysAbpV11TypeDef]

### FCntStart
- **Type**: typing.Optional[int]


# AccuracyTypeDef

### HorizontalAccuracy
- **Type**: typing.Optional[float]

### VerticalAccuracy
- **Type**: typing.Optional[float]


# ApplicationConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateAwsAccountWithPartnerAccountRequestTypeDef

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkAccountInfoTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# AssociateAwsAccountWithPartnerAccountResponseTypeDef

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkAccountInfoTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateMulticastGroupWithFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MulticastGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithMulticastGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithThingRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessGatewayWithCertificateRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IotCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessGatewayWithCertificateResponseTypeDef

### IotCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateWirelessGatewayWithThingRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BeaconingOutputTypeDef

### DataRate
- **Type**: typing.Optional[int]

### Frequencies
- **Type**: typing.Optional[typing.List[int]]


# BeaconingTypeDef

### DataRate
- **Type**: typing.Optional[int]

### Frequencies
- **Type**: typing.Optional[typing.Sequence[int]]


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelMulticastGroupSessionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CdmaLocalIdTypeDef

### PnOffset
- **Type**: <class 'int'>
- **Required**: Yes

### CdmaChannel
- **Type**: <class 'int'>
- **Required**: Yes


# CdmaNmrObjTypeDef

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


# CdmaObjTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.CdmaLocalIdTypeDef]

### PilotPower
- **Type**: typing.Optional[int]

### BaseLat
- **Type**: typing.Optional[float]

### BaseLng
- **Type**: typing.Optional[float]

### CdmaNmr
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.CdmaNmrObjTypeDef]]


# CellTowersTypeDef

### Gsm
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.GsmObjTypeDef]]

### Wcdma
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.WcdmaObjTypeDef]]

### Tdscdma
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TdscdmaObjTypeDef]]

### Lte
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.LteObjTypeDef]]

### Cdma
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.CdmaObjTypeDef]]


# CertificateListTypeDef

### SigningAlg
- **Type**: typing.Literal['Ed25519', 'P256r1']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ConnectionStatusEventConfigurationTypeDef

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef]

### WirelessGatewayIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# ConnectionStatusResourceTypeEventConfigurationTypeDef

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef]


# CreateDestinationRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateDestinationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeviceProfileRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANDeviceProfileUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Sidewalk
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# CreateDeviceProfileResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFuotaTaskRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANFuotaTaskTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]

### RedundancyPercent
- **Type**: typing.Optional[int]

### FragmentSizeBytes
- **Type**: typing.Optional[int]

### FragmentIntervalMS
- **Type**: typing.Optional[int]

### Descriptor
- **Type**: typing.Optional[str]


# CreateFuotaTaskResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMulticastGroupRequestTypeDef

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANMulticastTypeDef'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# CreateMulticastGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNetworkAnalyzerConfigurationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TraceContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.TraceContentTypeDef]

### WirelessDevices
- **Type**: typing.Optional[typing.Sequence[str]]

### WirelessGateways
- **Type**: typing.Optional[typing.Sequence[str]]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### MulticastGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateNetworkAnalyzerConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceProfileRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANServiceProfileTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateServiceProfileResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWirelessDeviceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWirelessGatewayRequestTypeDef

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayUnionTypeDef'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateWirelessGatewayResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWirelessGatewayTaskDefinitionRequestTypeDef

### AutoCreateTasks
- **Type**: <class 'bool'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.UpdateWirelessGatewayTaskCreateTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# CreateWirelessGatewayTaskDefinitionResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWirelessGatewayTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessGatewayTaskDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWirelessGatewayTaskResponseTypeDef

### WirelessGatewayTaskDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'FIRST_RETRY', 'IN_PROGRESS', 'PENDING', 'SECOND_RETRY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DakCertificateMetadataTypeDef

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


# DeleteDestinationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceProfileRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMulticastGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkAnalyzerConfigurationRequestTypeDef

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueuedMessagesRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# DeleteServiceProfileRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessDeviceImportTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessDeviceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayTaskDefinitionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterWirelessDeviceRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# DestinationsTypeDef

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


# DeviceProfileTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# DeviceRegistrationStateEventConfigurationTypeDef

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkEventNotificationConfigurationsTypeDef]

### WirelessDeviceIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# DeviceRegistrationStateResourceTypeEventConfigurationTypeDef

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkResourceTypeEventConfigurationTypeDef]


# DimensionTypeDef

### name
- **Type**: typing.Optional[typing.Literal['DeviceId', 'GatewayId']]

### value
- **Type**: typing.Optional[str]


# DisassociateAwsAccountFromPartnerAccountRequestTypeDef

### PartnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerType
- **Type**: typing.Literal['Sidewalk']
- **Required**: Yes


# DisassociateMulticastGroupFromFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MulticastGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromMulticastGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromThingRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessGatewayFromCertificateRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessGatewayFromThingRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DownlinkQueueMessageTypeDef

### MessageId
- **Type**: typing.Optional[str]

### TransmitMode
- **Type**: typing.Optional[int]

### ReceivedAt
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANSendDataToDeviceOutputTypeDef]


# EventConfigurationItemTypeDef

### Identifier
- **Type**: typing.Optional[str]

### IdentifierType
- **Type**: typing.Optional[typing.Literal['DevEui', 'FuotaTaskId', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']]

### PartnerType
- **Type**: typing.Optional[typing.Literal['Sidewalk']]

### Events
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.EventNotificationItemConfigurationsTypeDef]


# EventNotificationItemConfigurationsTypeDef

### DeviceRegistrationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.DeviceRegistrationStateEventConfigurationTypeDef]

### Proximity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ProximityEventConfigurationTypeDef]

### Join
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.JoinEventConfigurationTypeDef]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ConnectionStatusEventConfigurationTypeDef]

### MessageDeliveryStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.MessageDeliveryStatusEventConfigurationTypeDef]


# FPortsOutputTypeDef

### Fuota
- **Type**: typing.Optional[int]

### Multicast
- **Type**: typing.Optional[int]

### ClockSync
- **Type**: typing.Optional[int]

### Positioning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.PositioningTypeDef]

### Applications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.ApplicationConfigTypeDef]]


# FPortsTypeDef

### Fuota
- **Type**: typing.Optional[int]

### Multicast
- **Type**: typing.Optional[int]

### ClockSync
- **Type**: typing.Optional[int]

### Positioning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.PositioningTypeDef]

### Applications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.ApplicationConfigTypeDef]]


# FuotaTaskEventLogOptionTypeDef

### Event
- **Type**: typing.Literal['Fuota']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# FuotaTaskLogOptionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FuotaTaskLogOptionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FuotaTaskTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# GatewayListItemTypeDef

### GatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### DownlinkFrequency
- **Type**: <class 'int'>
- **Required**: Yes


# GetDestinationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDestinationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeviceProfileRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceProfileResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANDeviceProfileOutputTypeDef'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkGetDeviceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventConfigurationByResourceTypesResponseTypeDef

### DeviceRegistrationState
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.DeviceRegistrationStateResourceTypeEventConfigurationTypeDef'>
- **Required**: Yes

### Proximity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ProximityResourceTypeEventConfigurationTypeDef'>
- **Required**: Yes

### Join
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.JoinResourceTypeEventConfigurationTypeDef'>
- **Required**: Yes

### ConnectionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ConnectionStatusResourceTypeEventConfigurationTypeDef'>
- **Required**: Yes

### MessageDeliveryStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.MessageDeliveryStatusResourceTypeEventConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFuotaTaskResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANFuotaTaskGetInfoTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLogLevelsByResourceTypesResponseTypeDef

### DefaultLogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### WirelessGatewayLogOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessGatewayLogOptionOutputTypeDef]
- **Required**: Yes

### WirelessDeviceLogOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessDeviceLogOptionOutputTypeDef]
- **Required**: Yes

### FuotaTaskLogOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.FuotaTaskLogOptionOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetricConfigurationResponseTypeDef

### SummaryMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SummaryMetricConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetricsRequestTypeDef

### SummaryMetricQueries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.SummaryMetricQueryTypeDef]]


# GetMetricsResponseTypeDef

### SummaryMetricQueryResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.SummaryMetricQueryResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMulticastGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMulticastGroupResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANMulticastGetTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMulticastGroupSessionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMulticastGroupSessionResponseTypeDef

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANMulticastSessionOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNetworkAnalyzerConfigurationRequestTypeDef

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkAnalyzerConfigurationResponseTypeDef

### TraceContent
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.TraceContentTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPartnerAccountRequestTypeDef

### PartnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerType
- **Type**: typing.Literal['Sidewalk']
- **Required**: Yes


# GetPartnerAccountResponseTypeDef

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkAccountInfoWithFingerprintTypeDef'>
- **Required**: Yes

### AccountLinked
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPositionConfigurationRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes


# GetPositionConfigurationResponseTypeDef

### Solvers
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.PositionSolverDetailsTypeDef'>
- **Required**: Yes

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPositionEstimateRequestTypeDef

### WiFiAccessPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.WiFiAccessPointTypeDef]]

### CellTowers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.CellTowersTypeDef]

### Ip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.IpTypeDef]

### Gnss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.GnssTypeDef]

### Timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.TimestampTypeDef]


# GetPositionEstimateResponseTypeDef

### GeoJsonPayload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPositionRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes


# GetPositionResponseTypeDef

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Accuracy
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.AccuracyTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceEventConfigurationRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'FuotaTaskId', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']
- **Required**: Yes

### PartnerType
- **Type**: typing.Optional[typing.Literal['Sidewalk']]


# GetResourceEventConfigurationResponseTypeDef

### DeviceRegistrationState
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.DeviceRegistrationStateEventConfigurationTypeDef'>
- **Required**: Yes

### Proximity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ProximityEventConfigurationTypeDef'>
- **Required**: Yes

### Join
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.JoinEventConfigurationTypeDef'>
- **Required**: Yes

### ConnectionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ConnectionStatusEventConfigurationTypeDef'>
- **Required**: Yes

### MessageDeliveryStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.MessageDeliveryStatusEventConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceLogLevelRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceLogLevelResponseTypeDef

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePositionRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes


# GetResourcePositionResponseTypeDef

### GeoJsonPayload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceEndpointRequestTypeDef

### ServiceType
- **Type**: typing.Optional[typing.Literal['CUPS', 'LNS']]


# GetServiceEndpointResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceProfileRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceProfileResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGetServiceProfileInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessDeviceImportTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessDeviceImportTaskResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkGetStartImportInfoTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessDeviceRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'SidewalkManufacturingSn', 'ThingName', 'WirelessDeviceId']
- **Required**: Yes


# GetWirelessDeviceStatisticsRequestTypeDef

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessDeviceStatisticsResponseTypeDef

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUplinkReceivedAt
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANDeviceMetadataTypeDef'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkDeviceMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessGatewayCertificateRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayCertificateResponseTypeDef

### IotCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWANNetworkServerCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessGatewayFirmwareInformationRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayFirmwareInformationResponseTypeDef

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayCurrentVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessGatewayRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['GatewayEui', 'ThingName', 'WirelessGatewayId']
- **Required**: Yes


# GetWirelessGatewayResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessGatewayStatisticsRequestTypeDef

### WirelessGatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayStatisticsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessGatewayTaskDefinitionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayTaskDefinitionResponseTypeDef

### AutoCreateTasks
- **Type**: <class 'bool'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Update
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.UpdateWirelessGatewayTaskCreateTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessGatewayTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWirelessGatewayTaskResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlobalIdentityTypeDef

### Lac
- **Type**: <class 'int'>
- **Required**: Yes

### GeranCid
- **Type**: <class 'int'>
- **Required**: Yes


# GnssTypeDef

### Payload
- **Type**: <class 'str'>
- **Required**: Yes

### CaptureTime
- **Type**: typing.Optional[float]

### CaptureTimeAccuracy
- **Type**: typing.Optional[float]

### AssistPosition
- **Type**: typing.Optional[typing.Sequence[float]]

### AssistAltitude
- **Type**: typing.Optional[float]

### Use2DSolver
- **Type**: typing.Optional[bool]


# GsmLocalIdTypeDef

### Bsic
- **Type**: <class 'int'>
- **Required**: Yes

### Bcch
- **Type**: <class 'int'>
- **Required**: Yes


# GsmNmrObjTypeDef

### Bsic
- **Type**: <class 'int'>
- **Required**: Yes

### Bcch
- **Type**: <class 'int'>
- **Required**: Yes

### RxLevel
- **Type**: typing.Optional[int]

### GlobalIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.GlobalIdentityTypeDef]


# GsmObjTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.GsmLocalIdTypeDef]

### GsmTimingAdvance
- **Type**: typing.Optional[int]

### RxLevel
- **Type**: typing.Optional[int]

### GsmNmr
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.GsmNmrObjTypeDef]]


# ImportedSidewalkDeviceTypeDef

### SidewalkManufacturingSn
- **Type**: typing.Optional[str]

### OnboardingStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'ONBOARDED', 'PENDING']]

### OnboardingStatusReason
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# ImportedWirelessDeviceTypeDef

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ImportedSidewalkDeviceTypeDef]


# IpTypeDef

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes


# JoinEventConfigurationTypeDef

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANJoinEventNotificationConfigurationsTypeDef]

### WirelessDeviceIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# JoinResourceTypeEventConfigurationTypeDef

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANJoinResourceTypeEventConfigurationTypeDef]


# ListDestinationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDestinationsResponseTypeDef

### DestinationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.DestinationsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceProfilesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### DeviceProfileType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# ListDeviceProfilesResponseTypeDef

### DeviceProfileList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.DeviceProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesForWirelessDeviceImportTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'ONBOARDED', 'PENDING']]


# ListDevicesForWirelessDeviceImportTaskResponseTypeDef

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### ImportedWirelessDeviceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.ImportedWirelessDeviceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventConfigurationsRequestTypeDef

### ResourceType
- **Type**: typing.Literal['FuotaTask', 'SidewalkAccount', 'WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEventConfigurationsResponseTypeDef

### EventConfigurationsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.EventConfigurationItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFuotaTasksRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFuotaTasksResponseTypeDef

### FuotaTaskList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.FuotaTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMulticastGroupsByFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMulticastGroupsByFuotaTaskResponseTypeDef

### MulticastGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.MulticastGroupByFuotaTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMulticastGroupsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMulticastGroupsResponseTypeDef

### MulticastGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.MulticastGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNetworkAnalyzerConfigurationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNetworkAnalyzerConfigurationsResponseTypeDef

### NetworkAnalyzerConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.NetworkAnalyzerConfigurationsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerAccountsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPartnerAccountsResponseTypeDef

### Sidewalk
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkAccountInfoWithFingerprintTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPositionConfigurationsRequestTypeDef

### ResourceType
- **Type**: typing.Optional[typing.Literal['WirelessDevice', 'WirelessGateway']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPositionConfigurationsResponseTypeDef

### PositionConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.PositionConfigurationItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueuedMessagesRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WirelessDeviceType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# ListQueuedMessagesResponseTypeDef

### DownlinkQueueMessagesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.DownlinkQueueMessageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceProfilesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServiceProfilesResponseTypeDef

### ServiceProfileList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.ServiceProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWirelessDeviceImportTasksRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListWirelessDeviceImportTasksResponseTypeDef

### WirelessDeviceImportTaskList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessDeviceImportTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWirelessDevicesRequestTypeDef

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


# ListWirelessDevicesResponseTypeDef

### WirelessDeviceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessDeviceStatisticsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWirelessGatewayTaskDefinitionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### TaskDefinitionType
- **Type**: typing.Optional[typing.Literal['UPDATE']]


# ListWirelessGatewayTaskDefinitionsResponseTypeDef

### TaskDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.UpdateWirelessGatewayTaskEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWirelessGatewaysRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWirelessGatewaysResponseTypeDef

### WirelessGatewayList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessGatewayStatisticsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef

### GatewayEuiEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef

### WirelessGatewayEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# LoRaWANDeviceMetadataTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayMetadataTypeDef]]

### PublicGateways
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANPublicGatewayMetadataTypeDef]]


# LoRaWANDeviceOutputTypeDef

### DevEui
- **Type**: typing.Optional[str]

### DeviceProfileId
- **Type**: typing.Optional[str]

### ServiceProfileId
- **Type**: typing.Optional[str]

### OtaaV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.OtaaV11TypeDef]

### OtaaV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.OtaaV10XTypeDef]

### AbpV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.AbpV11TypeDef]

### AbpV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.AbpV10XTypeDef]

### FPorts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.FPortsOutputTypeDef]


# LoRaWANDeviceProfileOutputTypeDef

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


# LoRaWANDeviceProfileTypeDef

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
- **Type**: typing.Optional[typing.Sequence[int]]

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


# LoRaWANDeviceProfileUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoRaWANDeviceTypeDef

### DevEui
- **Type**: typing.Optional[str]

### DeviceProfileId
- **Type**: typing.Optional[str]

### ServiceProfileId
- **Type**: typing.Optional[str]

### OtaaV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.OtaaV11TypeDef]

### OtaaV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.OtaaV10XTypeDef]

### AbpV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.AbpV11TypeDef]

### AbpV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.AbpV10XTypeDef]

### FPorts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.FPortsTypeDef]


# LoRaWANFuotaTaskGetInfoTypeDef

### RfRegion
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# LoRaWANFuotaTaskTypeDef

### RfRegion
- **Type**: typing.Optional[typing.Literal['AS923-1', 'AS923-2', 'AS923-3', 'AS923-4', 'AU915', 'CN470', 'CN779', 'EU433', 'EU868', 'IN865', 'KR920', 'RU864', 'US915']]


# LoRaWANGatewayCurrentVersionTypeDef

### CurrentVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayVersionTypeDef]


# LoRaWANGatewayMetadataTypeDef

### GatewayEui
- **Type**: typing.Optional[str]

### Snr
- **Type**: typing.Optional[float]

### Rssi
- **Type**: typing.Optional[float]


# LoRaWANGatewayOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.BeaconingOutputTypeDef]

### MaxEirp
- **Type**: typing.Optional[float]


# LoRaWANGatewayTypeDef

### GatewayEui
- **Type**: typing.Optional[str]

### RfRegion
- **Type**: typing.Optional[str]

### JoinEuiFilters
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### NetIdFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### SubBands
- **Type**: typing.Optional[typing.Sequence[int]]

### Beaconing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.BeaconingTypeDef]

### MaxEirp
- **Type**: typing.Optional[float]


# LoRaWANGatewayUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoRaWANGatewayVersionTypeDef

### PackageVersion
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### Station
- **Type**: typing.Optional[str]


# LoRaWANGetServiceProfileInfoTypeDef

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


# LoRaWANJoinEventNotificationConfigurationsTypeDef

### DevEuiEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# LoRaWANJoinResourceTypeEventConfigurationTypeDef

### WirelessDeviceEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# LoRaWANListDeviceTypeDef

### DevEui
- **Type**: typing.Optional[str]


# LoRaWANMulticastGetTypeDef

### RfRegion
- **Type**: typing.Optional[typing.Literal['AS923-1', 'AS923-2', 'AS923-3', 'AS923-4', 'AU915', 'CN470', 'CN779', 'EU433', 'EU868', 'IN865', 'KR920', 'RU864', 'US915']]

### DlClass
- **Type**: typing.Optional[typing.Literal['ClassB', 'ClassC']]

### NumberOfDevicesRequested
- **Type**: typing.Optional[int]

### NumberOfDevicesInGroup
- **Type**: typing.Optional[int]

### ParticipatingGateways
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ParticipatingGatewaysMulticastOutputTypeDef]


# LoRaWANMulticastMetadataTypeDef

### FPort
- **Type**: typing.Optional[int]


# LoRaWANMulticastSessionOutputTypeDef

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


# LoRaWANMulticastSessionTypeDef

### DlDr
- **Type**: typing.Optional[int]

### DlFreq
- **Type**: typing.Optional[int]

### SessionStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.TimestampTypeDef]

### SessionTimeout
- **Type**: typing.Optional[int]

### PingSlotPeriod
- **Type**: typing.Optional[int]


# LoRaWANMulticastSessionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoRaWANMulticastTypeDef

### RfRegion
- **Type**: typing.Optional[typing.Literal['AS923-1', 'AS923-2', 'AS923-3', 'AS923-4', 'AU915', 'CN470', 'CN779', 'EU433', 'EU868', 'IN865', 'KR920', 'RU864', 'US915']]

### DlClass
- **Type**: typing.Optional[typing.Literal['ClassB', 'ClassC']]

### ParticipatingGateways
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ParticipatingGatewaysMulticastUnionTypeDef]


# LoRaWANPublicGatewayMetadataTypeDef

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


# LoRaWANSendDataToDeviceOutputTypeDef

### FPort
- **Type**: typing.Optional[int]

### ParticipatingGateways
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ParticipatingGatewaysOutputTypeDef]


# LoRaWANSendDataToDeviceTypeDef

### FPort
- **Type**: typing.Optional[int]

### ParticipatingGateways
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ParticipatingGatewaysUnionTypeDef]


# LoRaWANSendDataToDeviceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoRaWANServiceProfileTypeDef

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


# LoRaWANStartFuotaTaskTypeDef

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.TimestampTypeDef]


# LoRaWANUpdateDeviceTypeDef

### DeviceProfileId
- **Type**: typing.Optional[str]

### ServiceProfileId
- **Type**: typing.Optional[str]

### AbpV1_1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.UpdateAbpV11TypeDef]

### AbpV1_0_x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.UpdateAbpV10XTypeDef]

### FPorts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.UpdateFPortsTypeDef]


# LoRaWANUpdateGatewayTaskCreateTypeDef

### UpdateSignature
- **Type**: typing.Optional[str]

### SigKeyCrc
- **Type**: typing.Optional[int]

### CurrentVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayVersionTypeDef]

### UpdateVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayVersionTypeDef]


# LoRaWANUpdateGatewayTaskEntryTypeDef

### CurrentVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayVersionTypeDef]

### UpdateVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayVersionTypeDef]


# LteLocalIdTypeDef

### Pci
- **Type**: <class 'int'>
- **Required**: Yes

### Earfcn
- **Type**: <class 'int'>
- **Required**: Yes


# LteNmrObjTypeDef

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


# LteObjTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LteLocalIdTypeDef]

### LteTimingAdvance
- **Type**: typing.Optional[int]

### Rsrp
- **Type**: typing.Optional[int]

### Rsrq
- **Type**: typing.Optional[float]

### NrCapable
- **Type**: typing.Optional[bool]

### LteNmr
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.LteNmrObjTypeDef]]


# MessageDeliveryStatusEventConfigurationTypeDef

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkEventNotificationConfigurationsTypeDef]

### WirelessDeviceIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# MessageDeliveryStatusResourceTypeEventConfigurationTypeDef

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkResourceTypeEventConfigurationTypeDef]


# MetricQueryValueTypeDef

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


# MulticastGroupByFuotaTaskTypeDef

### Id
- **Type**: typing.Optional[str]


# MulticastGroupTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# MulticastWirelessMetadataTypeDef

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANMulticastMetadataTypeDef]


# NetworkAnalyzerConfigurationsTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# OtaaV10XTypeDef

### AppKey
- **Type**: typing.Optional[str]

### AppEui
- **Type**: typing.Optional[str]

### JoinEui
- **Type**: typing.Optional[str]

### GenAppKey
- **Type**: typing.Optional[str]


# OtaaV11TypeDef

### AppKey
- **Type**: typing.Optional[str]

### NwkKey
- **Type**: typing.Optional[str]

### JoinEui
- **Type**: typing.Optional[str]


# ParticipatingGatewaysMulticastOutputTypeDef

### GatewayList
- **Type**: typing.Optional[typing.List[str]]

### TransmissionInterval
- **Type**: typing.Optional[int]


# ParticipatingGatewaysMulticastTypeDef

### GatewayList
- **Type**: typing.Optional[typing.Sequence[str]]

### TransmissionInterval
- **Type**: typing.Optional[int]


# ParticipatingGatewaysMulticastUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParticipatingGatewaysOutputTypeDef

### DownlinkMode
- **Type**: typing.Literal['CONCURRENT', 'SEQUENTIAL', 'USING_UPLINK_GATEWAY']
- **Required**: Yes

### GatewayList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.GatewayListItemTypeDef]
- **Required**: Yes

### TransmissionInterval
- **Type**: <class 'int'>
- **Required**: Yes


# ParticipatingGatewaysTypeDef

### DownlinkMode
- **Type**: typing.Literal['CONCURRENT', 'SEQUENTIAL', 'USING_UPLINK_GATEWAY']
- **Required**: Yes

### GatewayList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.GatewayListItemTypeDef]
- **Required**: Yes

### TransmissionInterval
- **Type**: <class 'int'>
- **Required**: Yes


# ParticipatingGatewaysUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PositionConfigurationItemTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['WirelessDevice', 'WirelessGateway']]

### Solvers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.PositionSolverDetailsTypeDef]

### Destination
- **Type**: typing.Optional[str]


# PositionSolverConfigurationsTypeDef

### SemtechGnss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SemtechGnssConfigurationTypeDef]


# PositionSolverDetailsTypeDef

### SemtechGnss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SemtechGnssDetailTypeDef]


# PositioningTypeDef

### ClockSync
- **Type**: typing.Optional[int]

### Stream
- **Type**: typing.Optional[int]

### Gnss
- **Type**: typing.Optional[int]


# ProximityEventConfigurationTypeDef

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkEventNotificationConfigurationsTypeDef]

### WirelessDeviceIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# ProximityResourceTypeEventConfigurationTypeDef

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkResourceTypeEventConfigurationTypeDef]


# PutPositionConfigurationRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### Solvers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.PositionSolverConfigurationsTypeDef]

### Destination
- **Type**: typing.Optional[str]


# PutResourceLogLevelRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# ResetResourceLogLevelRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes


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


# SemtechGnssConfigurationTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Fec
- **Type**: typing.Literal['NONE', 'ROSE']
- **Required**: Yes


# SemtechGnssDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SendDataToMulticastGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PayloadData
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.MulticastWirelessMetadataTypeDef'>
- **Required**: Yes


# SendDataToMulticastGroupResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendDataToWirelessDeviceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### TransmitMode
- **Type**: <class 'int'>
- **Required**: Yes

### PayloadData
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessMetadataTypeDef]


# SendDataToWirelessDeviceResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServiceProfileTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# SessionKeysAbpV10XTypeDef

### NwkSKey
- **Type**: typing.Optional[str]

### AppSKey
- **Type**: typing.Optional[str]


# SessionKeysAbpV11TypeDef

### FNwkSIntKey
- **Type**: typing.Optional[str]

### SNwkSIntKey
- **Type**: typing.Optional[str]

### NwkSEncKey
- **Type**: typing.Optional[str]

### AppSKey
- **Type**: typing.Optional[str]


# SidewalkAccountInfoTypeDef

### AmazonId
- **Type**: typing.Optional[str]

### AppServerPrivateKey
- **Type**: typing.Optional[str]


# SidewalkAccountInfoWithFingerprintTypeDef

### AmazonId
- **Type**: typing.Optional[str]

### Fingerprint
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# SidewalkCreateWirelessDeviceTypeDef

### DeviceProfileId
- **Type**: typing.Optional[str]


# SidewalkDeviceMetadataTypeDef

### Rssi
- **Type**: typing.Optional[int]

### BatteryLevel
- **Type**: typing.Optional[typing.Literal['critical', 'low', 'normal']]

### Event
- **Type**: typing.Optional[typing.Literal['ack', 'discovered', 'lost', 'nack', 'passthrough']]

### DeviceState
- **Type**: typing.Optional[typing.Literal['Provisioned', 'RegisteredNotSeen', 'RegisteredReachable', 'RegisteredUnreachable']]


# SidewalkDeviceTypeDef

### AmazonId
- **Type**: typing.Optional[str]

### SidewalkId
- **Type**: typing.Optional[str]

### SidewalkManufacturingSn
- **Type**: typing.Optional[str]

### DeviceCertificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.CertificateListTypeDef]]

### PrivateKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.CertificateListTypeDef]]

### DeviceProfileId
- **Type**: typing.Optional[str]

### CertificateId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'PROVISIONED', 'REGISTERED', 'UNKNOWN']]


# SidewalkEventNotificationConfigurationsTypeDef

### AmazonIdEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SidewalkGetDeviceProfileTypeDef

### ApplicationServerPublicKey
- **Type**: typing.Optional[str]

### QualificationStatus
- **Type**: typing.Optional[bool]

### DakCertificateMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.DakCertificateMetadataTypeDef]]


# SidewalkGetStartImportInfoTypeDef

### DeviceCreationFileList
- **Type**: typing.Optional[typing.List[str]]

### Role
- **Type**: typing.Optional[str]


# SidewalkListDeviceTypeDef

### AmazonId
- **Type**: typing.Optional[str]

### SidewalkId
- **Type**: typing.Optional[str]

### SidewalkManufacturingSn
- **Type**: typing.Optional[str]

### DeviceCertificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.CertificateListTypeDef]]

### DeviceProfileId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'PROVISIONED', 'REGISTERED', 'UNKNOWN']]


# SidewalkResourceTypeEventConfigurationTypeDef

### WirelessDeviceEventTopic
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SidewalkSendDataToDeviceTypeDef

### Seq
- **Type**: typing.Optional[int]

### MessageType
- **Type**: typing.Optional[typing.Literal['CUSTOM_COMMAND_ID_GET', 'CUSTOM_COMMAND_ID_NOTIFY', 'CUSTOM_COMMAND_ID_RESP', 'CUSTOM_COMMAND_ID_SET']]

### AckModeRetryDurationSecs
- **Type**: typing.Optional[int]


# SidewalkSingleStartImportInfoTypeDef

### SidewalkManufacturingSn
- **Type**: typing.Optional[str]


# SidewalkStartImportInfoTypeDef

### DeviceCreationFile
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]


# SidewalkUpdateAccountTypeDef

### AppServerPrivateKey
- **Type**: typing.Optional[str]


# SidewalkUpdateImportInfoTypeDef

### DeviceCreationFile
- **Type**: typing.Optional[str]


# StartBulkAssociateWirelessDeviceWithMulticastGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# StartFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANStartFuotaTaskTypeDef]


# StartMulticastGroupSessionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANMulticastSessionUnionTypeDef'>
- **Required**: Yes


# StartSingleWirelessDeviceImportTaskRequestTypeDef

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkSingleStartImportInfoTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# StartSingleWirelessDeviceImportTaskResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartWirelessDeviceImportTaskRequestTypeDef

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkStartImportInfoTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# StartWirelessDeviceImportTaskResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SummaryMetricConfigurationTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SummaryMetricQueryResultTypeDef

### QueryId
- **Type**: typing.Optional[str]

### QueryStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Succeeded']]

### Error
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[typing.Literal['AwsAccountActiveDeviceCount', 'AwsAccountActiveGatewayCount', 'AwsAccountDeviceCount', 'AwsAccountDownlinkCount', 'AwsAccountGatewayCount', 'AwsAccountJoinAcceptCount', 'AwsAccountJoinRequestCount', 'AwsAccountRoamingDownlinkCount', 'AwsAccountRoamingUplinkCount', 'AwsAccountUplinkCount', 'AwsAccountUplinkLostCount', 'AwsAccountUplinkLostRate', 'DeviceDownlinkCount', 'DeviceJoinAcceptCount', 'DeviceJoinRequestCount', 'DeviceRSSI', 'DeviceRoamingDownlinkCount', 'DeviceRoamingRSSI', 'DeviceRoamingSNR', 'DeviceRoamingUplinkCount', 'DeviceSNR', 'DeviceUplinkCount', 'DeviceUplinkLostCount', 'DeviceUplinkLostRate', 'GatewayDownTime', 'GatewayDownlinkCount', 'GatewayJoinAcceptCount', 'GatewayJoinRequestCount', 'GatewayRSSI', 'GatewaySNR', 'GatewayUpTime', 'GatewayUplinkCount']]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.DimensionTypeDef]]

### AggregationPeriod
- **Type**: typing.Optional[typing.Literal['OneDay', 'OneHour', 'OneWeek']]

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### EndTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.MetricQueryValueTypeDef]]

### Unit
- **Type**: typing.Optional[str]


# SummaryMetricQueryTypeDef

### QueryId
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[typing.Literal['AwsAccountActiveDeviceCount', 'AwsAccountActiveGatewayCount', 'AwsAccountDeviceCount', 'AwsAccountDownlinkCount', 'AwsAccountGatewayCount', 'AwsAccountJoinAcceptCount', 'AwsAccountJoinRequestCount', 'AwsAccountRoamingDownlinkCount', 'AwsAccountRoamingUplinkCount', 'AwsAccountUplinkCount', 'AwsAccountUplinkLostCount', 'AwsAccountUplinkLostRate', 'DeviceDownlinkCount', 'DeviceJoinAcceptCount', 'DeviceJoinRequestCount', 'DeviceRSSI', 'DeviceRoamingDownlinkCount', 'DeviceRoamingRSSI', 'DeviceRoamingSNR', 'DeviceRoamingUplinkCount', 'DeviceSNR', 'DeviceUplinkCount', 'DeviceUplinkLostCount', 'DeviceUplinkLostRate', 'GatewayDownTime', 'GatewayDownlinkCount', 'GatewayJoinAcceptCount', 'GatewayJoinRequestCount', 'GatewayRSSI', 'GatewaySNR', 'GatewayUpTime', 'GatewayUplinkCount']]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.DimensionTypeDef]]

### AggregationPeriod
- **Type**: typing.Optional[typing.Literal['OneDay', 'OneHour', 'OneWeek']]

### StartTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.TimestampTypeDef]

### EndTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.TimestampTypeDef]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TdscdmaLocalIdTypeDef

### Uarfcn
- **Type**: <class 'int'>
- **Required**: Yes

### CellParams
- **Type**: <class 'int'>
- **Required**: Yes


# TdscdmaNmrObjTypeDef

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


# TdscdmaObjTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.TdscdmaLocalIdTypeDef]

### TdscdmaTimingAdvance
- **Type**: typing.Optional[int]

### Rscp
- **Type**: typing.Optional[int]

### PathLoss
- **Type**: typing.Optional[int]

### TdscdmaNmr
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TdscdmaNmrObjTypeDef]]


# TestWirelessDeviceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# TestWirelessDeviceResponseTypeDef

### Result
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TraceContentTypeDef

### WirelessDeviceFrameInfo
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ERROR', 'INFO']]

### MulticastFrameInfo
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAbpV10XTypeDef

### FCntStart
- **Type**: typing.Optional[int]


# UpdateAbpV11TypeDef

### FCntStart
- **Type**: typing.Optional[int]


# UpdateDestinationRequestTypeDef

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


# UpdateEventConfigurationByResourceTypesRequestTypeDef

### DeviceRegistrationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.DeviceRegistrationStateResourceTypeEventConfigurationTypeDef]

### Proximity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ProximityResourceTypeEventConfigurationTypeDef]

### Join
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.JoinResourceTypeEventConfigurationTypeDef]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ConnectionStatusResourceTypeEventConfigurationTypeDef]

### MessageDeliveryStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.MessageDeliveryStatusResourceTypeEventConfigurationTypeDef]


# UpdateFPortsTypeDef

### Positioning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.PositioningTypeDef]

### Applications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.ApplicationConfigTypeDef]]


# UpdateFuotaTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANFuotaTaskTypeDef]

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


# UpdateLogLevelsByResourceTypesRequestTypeDef

### DefaultLogLevel
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ERROR', 'INFO']]

### FuotaTaskLogOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.FuotaTaskLogOptionUnionTypeDef]]

### WirelessDeviceLogOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessDeviceLogOptionUnionTypeDef]]

### WirelessGatewayLogOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessGatewayLogOptionUnionTypeDef]]


# UpdateMetricConfigurationRequestTypeDef

### SummaryMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SummaryMetricConfigurationTypeDef]


# UpdateMulticastGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANMulticastTypeDef]


# UpdateNetworkAnalyzerConfigurationRequestTypeDef

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### TraceContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.TraceContentTypeDef]

### WirelessDevicesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### WirelessDevicesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### WirelessGatewaysToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### WirelessGatewaysToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### Description
- **Type**: typing.Optional[str]

### MulticastGroupsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### MulticastGroupsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdatePartnerAccountRequestTypeDef

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkUpdateAccountTypeDef'>
- **Required**: Yes

### PartnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerType
- **Type**: typing.Literal['Sidewalk']
- **Required**: Yes


# UpdatePositionRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### Position
- **Type**: typing.Sequence[float]
- **Required**: Yes


# UpdateResourceEventConfigurationRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'FuotaTaskId', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']
- **Required**: Yes

### PartnerType
- **Type**: typing.Optional[typing.Literal['Sidewalk']]

### DeviceRegistrationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.DeviceRegistrationStateEventConfigurationTypeDef]

### Proximity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ProximityEventConfigurationTypeDef]

### Join
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.JoinEventConfigurationTypeDef]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ConnectionStatusEventConfigurationTypeDef]

### MessageDeliveryStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.MessageDeliveryStatusEventConfigurationTypeDef]


# UpdateResourcePositionRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### GeoJsonPayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.BlobTypeDef]


# UpdateWirelessDeviceImportTaskRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkUpdateImportInfoTypeDef'>
- **Required**: Yes


# UpdateWirelessDeviceRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANUpdateDeviceTypeDef]

### Positioning
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UpdateWirelessGatewayRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### JoinEuiFilters
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]

### NetIdFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxEirp
- **Type**: typing.Optional[float]


# UpdateWirelessGatewayTaskCreateTypeDef

### UpdateDataSource
- **Type**: typing.Optional[str]

### UpdateDataRole
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANUpdateGatewayTaskCreateTypeDef]


# UpdateWirelessGatewayTaskEntryTypeDef

### Id
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANUpdateGatewayTaskEntryTypeDef]

### Arn
- **Type**: typing.Optional[str]


# WcdmaLocalIdTypeDef

### Uarfcndl
- **Type**: <class 'int'>
- **Required**: Yes

### Psc
- **Type**: <class 'int'>
- **Required**: Yes


# WcdmaNmrObjTypeDef

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


# WcdmaObjTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.WcdmaLocalIdTypeDef]

### Rscp
- **Type**: typing.Optional[int]

### PathLoss
- **Type**: typing.Optional[int]

### WcdmaNmr
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.WcdmaNmrObjTypeDef]]


# WiFiAccessPointTypeDef

### MacAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Rss
- **Type**: <class 'int'>
- **Required**: Yes


# WirelessDeviceEventLogOptionTypeDef

### Event
- **Type**: typing.Literal['Downlink_Data', 'Join', 'Registration', 'Rejoin', 'Uplink_Data']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# WirelessDeviceImportTaskTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### DestinationName
- **Type**: typing.Optional[str]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkGetStartImportInfoTypeDef]

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


# WirelessDeviceLogOptionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WirelessDeviceLogOptionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WirelessDeviceStatisticsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WirelessGatewayEventLogOptionTypeDef

### Event
- **Type**: typing.Literal['CUPS_Request', 'Certificate']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# WirelessGatewayLogOptionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WirelessGatewayLogOptionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WirelessGatewayStatisticsTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayOutputTypeDef]

### LastUplinkReceivedAt
- **Type**: typing.Optional[str]


# WirelessMetadataTypeDef

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANSendDataToDeviceUnionTypeDef]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkSendDataToDeviceTypeDef]



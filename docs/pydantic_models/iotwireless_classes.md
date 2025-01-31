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

### FPort
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[typing.Literal['SemtechGeolocation']]

### DestinationName
- **Type**: typing.Optional[str]


# AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef

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


# AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MulticastGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessDeviceWithThingRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ThingArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWirelessGatewayWithCertificateRequestRequestTypeDef

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


# AssociateWirelessGatewayWithThingRequestRequestTypeDef

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


# CancelMulticastGroupSessionRequestRequestTypeDef

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


# CreateDestinationRequestRequestTypeDef

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


# CreateDeviceProfileRequestRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANDeviceProfileTypeDef]

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


# CreateFuotaTaskRequestRequestTypeDef

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


# CreateMulticastGroupRequestRequestTypeDef

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


# CreateNetworkAnalyzerConfigurationRequestRequestTypeDef

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


# CreateServiceProfileRequestRequestTypeDef

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


# CreateWirelessDeviceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANDeviceTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]

### Positioning
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkCreateWirelessDeviceTypeDef]


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


# CreateWirelessGatewayRequestRequestTypeDef

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANGatewayTypeDef'>
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


# CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef

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


# CreateWirelessGatewayTaskRequestRequestTypeDef

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


# DeleteDestinationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceProfileRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFuotaTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMulticastGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkAnalyzerConfigurationRequestRequestTypeDef

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueuedMessagesRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceType
- **Type**: typing.Optional[typing.Literal['LoRaWAN', 'Sidewalk']]


# DeleteServiceProfileRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessDeviceImportTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessDeviceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWirelessGatewayTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterWirelessDeviceRequestRequestTypeDef

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


# DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef

### PartnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerType
- **Type**: typing.Literal['Sidewalk']
- **Required**: Yes


# DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MulticastGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WirelessDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessDeviceFromThingRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWirelessGatewayFromThingRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['DevEui', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']]

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


# GetDestinationRequestRequestTypeDef

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


# GetDeviceProfileRequestRequestTypeDef

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


# GetFuotaTaskRequestRequestTypeDef

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


# GetMetricsRequestRequestTypeDef

### SummaryMetricQueries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.SummaryMetricQueryTypeDef]]


# GetMetricsResponseTypeDef

### SummaryMetricQueryResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.SummaryMetricQueryResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMulticastGroupRequestRequestTypeDef

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


# GetMulticastGroupSessionRequestRequestTypeDef

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


# GetNetworkAnalyzerConfigurationRequestRequestTypeDef

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


# GetPartnerAccountRequestRequestTypeDef

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


# GetPositionConfigurationRequestRequestTypeDef

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


# GetPositionEstimateRequestRequestTypeDef

### WiFiAccessPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.WiFiAccessPointTypeDef]]

### CellTowers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.CellTowersTypeDef]

### Ip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.IpTypeDef]

### Gnss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.GnssTypeDef]

### Timestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetPositionEstimateResponseTypeDef

### GeoJsonPayload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPositionRequestRequestTypeDef

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


# GetResourceEventConfigurationRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']
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


# GetResourceLogLevelRequestRequestTypeDef

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


# GetResourcePositionRequestRequestTypeDef

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


# GetServiceEndpointRequestRequestTypeDef

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


# GetServiceProfileRequestRequestTypeDef

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


# GetWirelessDeviceImportTaskRequestRequestTypeDef

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


# GetWirelessDeviceRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'SidewalkManufacturingSn', 'ThingName', 'WirelessDeviceId']
- **Required**: Yes


# GetWirelessDeviceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANDeviceOutputTypeDef'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkDeviceTypeDef'>
- **Required**: Yes

### Positioning
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWirelessDeviceStatisticsRequestRequestTypeDef

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


# GetWirelessGatewayCertificateRequestRequestTypeDef

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


# GetWirelessGatewayFirmwareInformationRequestRequestTypeDef

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


# GetWirelessGatewayRequestRequestTypeDef

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


# GetWirelessGatewayStatisticsRequestRequestTypeDef

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


# GetWirelessGatewayTaskDefinitionRequestRequestTypeDef

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


# GetWirelessGatewayTaskRequestRequestTypeDef

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


# ListDestinationsRequestRequestTypeDef

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


# ListDeviceProfilesRequestRequestTypeDef

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


# ListDevicesForWirelessDeviceImportTaskRequestRequestTypeDef

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


# ListEventConfigurationsRequestRequestTypeDef

### ResourceType
- **Type**: typing.Literal['SidewalkAccount', 'WirelessDevice', 'WirelessGateway']
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


# ListFuotaTasksRequestRequestTypeDef

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


# ListMulticastGroupsByFuotaTaskRequestRequestTypeDef

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


# ListMulticastGroupsRequestRequestTypeDef

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


# ListNetworkAnalyzerConfigurationsRequestRequestTypeDef

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


# ListPartnerAccountsRequestRequestTypeDef

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


# ListPositionConfigurationsRequestRequestTypeDef

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


# ListQueuedMessagesRequestRequestTypeDef

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


# ListServiceProfilesRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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


# ListWirelessDeviceImportTasksRequestRequestTypeDef

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


# ListWirelessDevicesRequestRequestTypeDef

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


# ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef

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


# ListWirelessGatewaysRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SessionTimeout
- **Type**: typing.Optional[int]

### PingSlotPeriod
- **Type**: typing.Optional[int]


# LoRaWANMulticastTypeDef

### RfRegion
- **Type**: typing.Optional[typing.Literal['AS923-1', 'AS923-2', 'AS923-3', 'AS923-4', 'AU915', 'CN470', 'CN779', 'EU433', 'EU868', 'IN865', 'KR920', 'RU864', 'US915']]

### DlClass
- **Type**: typing.Optional[typing.Literal['ClassB', 'ClassC']]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.ParticipatingGatewaysTypeDef]


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
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# PutPositionConfigurationRequestRequestTypeDef

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


# PutResourceLogLevelRequestRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# ResetResourceLogLevelRequestRequestTypeDef

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

### Provider
- **Type**: typing.Optional[typing.Literal['Semtech']]

### Type
- **Type**: typing.Optional[typing.Literal['GNSS']]

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Fec
- **Type**: typing.Optional[typing.Literal['NONE', 'ROSE']]


# SendDataToMulticastGroupRequestRequestTypeDef

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


# SendDataToWirelessDeviceRequestRequestTypeDef

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


# StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.TagTypeDef]]


# StartFuotaTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANStartFuotaTaskTypeDef]


# StartMulticastGroupSessionRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LoRaWAN
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANMulticastSessionTypeDef'>
- **Required**: Yes


# StartSingleWirelessDeviceImportTaskRequestRequestTypeDef

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


# StartWirelessDeviceImportTaskRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TagResourceRequestRequestTypeDef

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


# TestWirelessDeviceRequestRequestTypeDef

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


# TraceContentTypeDef

### WirelessDeviceFrameInfo
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ERROR', 'INFO']]

### MulticastFrameInfo
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UntagResourceRequestRequestTypeDef

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


# UpdateDestinationRequestRequestTypeDef

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


# UpdateEventConfigurationByResourceTypesRequestRequestTypeDef

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


# UpdateFuotaTaskRequestRequestTypeDef

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


# UpdateLogLevelsByResourceTypesRequestRequestTypeDef

### DefaultLogLevel
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ERROR', 'INFO']]

### WirelessDeviceLogOptions
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessDeviceLogOptionTypeDef, aws_resource_validator.pydantic_models.iotwireless_classes.WirelessDeviceLogOptionOutputTypeDef]]]

### WirelessGatewayLogOptions
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessGatewayLogOptionTypeDef, aws_resource_validator.pydantic_models.iotwireless_classes.WirelessGatewayLogOptionOutputTypeDef]]]


# UpdateMetricConfigurationRequestRequestTypeDef

### SummaryMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SummaryMetricConfigurationTypeDef]


# UpdateMulticastGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LoRaWAN
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANMulticastTypeDef]


# UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef

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


# UpdatePartnerAccountRequestRequestTypeDef

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkUpdateAccountTypeDef'>
- **Required**: Yes

### PartnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerType
- **Type**: typing.Literal['Sidewalk']
- **Required**: Yes


# UpdatePositionRequestRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### Position
- **Type**: typing.Sequence[float]
- **Required**: Yes


# UpdateResourceEventConfigurationRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### IdentifierType
- **Type**: typing.Literal['DevEui', 'GatewayEui', 'PartnerAccountId', 'WirelessDeviceId', 'WirelessGatewayId']
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


# UpdateResourcePositionRequestRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['WirelessDevice', 'WirelessGateway']
- **Required**: Yes

### GeoJsonPayload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# UpdateWirelessDeviceImportTaskRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Sidewalk
- **Type**: <class 'aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkUpdateImportInfoTypeDef'>
- **Required**: Yes


# UpdateWirelessDeviceRequestRequestTypeDef

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


# UpdateWirelessGatewayRequestRequestTypeDef

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

### Type
- **Type**: typing.Literal['LoRaWAN', 'Sidewalk']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessDeviceEventLogOptionTypeDef]]


# WirelessDeviceLogOptionTypeDef

### Type
- **Type**: typing.Literal['LoRaWAN', 'Sidewalk']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessDeviceEventLogOptionTypeDef]]


# WirelessDeviceStatisticsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANListDeviceTypeDef]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkListDeviceTypeDef]

### FuotaDeviceStatus
- **Type**: typing.Optional[typing.Literal['Device_exist_in_conflict_fuota_task', 'FragAlgo_unsupported', 'FragIndex_unsupported', 'Initial', 'MICError', 'MemoryError', 'MissingFrag', 'Not_enough_memory', 'Package_Not_Supported', 'SessionCnt_replay', 'Successful', 'Wrong_descriptor']]

### MulticastDeviceStatus
- **Type**: typing.Optional[str]

### McGroupId
- **Type**: typing.Optional[int]


# WirelessGatewayEventLogOptionTypeDef

### Event
- **Type**: typing.Literal['CUPS_Request', 'Certificate']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes


# WirelessGatewayLogOptionOutputTypeDef

### Type
- **Type**: typing.Literal['LoRaWAN']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessGatewayEventLogOptionTypeDef]]


# WirelessGatewayLogOptionTypeDef

### Type
- **Type**: typing.Literal['LoRaWAN']
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DISABLED', 'ERROR', 'INFO']
- **Required**: Yes

### Events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotwireless_classes.WirelessGatewayEventLogOptionTypeDef]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.LoRaWANSendDataToDeviceTypeDef]

### Sidewalk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotwireless_classes.SidewalkSendDataToDeviceTypeDef]



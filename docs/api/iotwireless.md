# Iotwireless Service

### AppEui
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{16}`

### AppKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{32}`

### AppSKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{32}`

### AppServerPrivateKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{64}`
- **Min Length**: 1
- **Max Length**: 4096

### ApplicationServerPublicKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{64}`
- **Min Length**: 1
- **Max Length**: 4096

### CertificatePEM
- **Type**: string
- **Pattern**: `[^-A-Za-z0-9+/=]|=[^=]|={3,}${1,4096}`
- **Min Length**: 1
- **Max Length**: 4096

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### DestinationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]+`
- **Max Length**: 128

### DevAddr
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}`

### DevEui
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{16}`

### FNwkSIntKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{32}`

### FileDescriptor
- **Type**: string
- **Pattern**: `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
- **Max Length**: 332

### Fingerprint
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{64}`
- **Min Length**: 64
- **Max Length**: 64

### GatewayEui
- **Type**: string
- **Pattern**: `^(([0-9A-Fa-f]{2}-){7}|([0-9A-Fa-f]{2}:){7}|([0-9A-Fa-f]{2}\s){7}|([0-9A-Fa-f]{2}){7})([0-9A-Fa-f]{2})$`

### GenAppKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{32}`

### ISODateTimeString
- **Type**: string
- **Pattern**: `^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$`

### JoinEui
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{16}`

### MacAddress
- **Type**: string
- **Pattern**: `^([0-9A-Fa-f]{2}[:-]?){5}([0-9A-Fa-f]{2})$`
- **Min Length**: 12
- **Max Length**: 17

### NetId
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{6}`

### NetworkAnalyzerConfigurationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]+`
- **Min Length**: 1
- **Max Length**: 1024

### NwkKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{32}`

### NwkSEncKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{32}`

### NwkSKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{32}`

### PayloadData
- **Type**: string
- **Pattern**: `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
- **Max Length**: 2048

### PositionResourceIdentifier
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`

### SNwkSIntKey
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{32}`

### WirelessGatewayTaskDefinitionId
- **Type**: string
- **Pattern**: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
- **Max Length**: 36


# Iotmanagedintegrations Service

### ActionName
- **Type**: string
- **Pattern**: `[/a-zA-Z0-9\._ ]+`
- **Min Length**: 1
- **Max Length**: 128

### ActionReference
- **Type**: string
- **Pattern**: `[a-zA-Z.]+`

### ActionTraceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+=(?:_[0-9]+)?`
- **Min Length**: 16
- **Max Length**: 20

### AdvertisedProductId
- **Type**: string
- **Pattern**: `([A-Za-z0-9!#$%&()*\+\-;<=>?@^_`{|}~])+`
- **Min Length**: 5
- **Max Length**: 5

### AttributeName
- **Type**: string
- **Pattern**: `.*[a-zA-Z0-9_.,@/:#-]+.*`
- **Min Length**: 0
- **Max Length**: 128

### AttributeValue
- **Type**: string
- **Pattern**: `.*[a-zA-Z0-9_.,@/:#-]*.*`
- **Min Length**: 0
- **Max Length**: 800

### AuthMaterialString
- **Type**: string
- **Pattern**: `[0-9A-Za-z!#$%&()*\+\-;<=>?@^_`{|}~\/: ]+`
- **Min Length**: 1
- **Max Length**: 512

### Brand
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_ ]+`
- **Min Length**: 1
- **Max Length**: 128

### CaCertificate
- **Type**: string
- **Pattern**: `-----BEGIN CERTIFICATE-----.*(.|\n)*-----END CERTIFICATE-----\n?`

### Capabilities
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\s\'\x{0022},.:\\\/{$}\[\]=_\-\+]+`
- **Min Length**: 1
- **Max Length**: 65535

### CapabilityActionName
- **Type**: string
- **Pattern**: `[/a-zA-Z]+`

### CapabilityId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9./]+(@\d+\.\d+)?`
- **Min Length**: 1
- **Max Length**: 128

### CapabilityName
- **Type**: string
- **Pattern**: `[/a-zA-Z0-9\._ ]+`
- **Min Length**: 1
- **Max Length**: 128

### CapabilityReportVersion
- **Type**: string
- **Pattern**: `1\.0\.0`
- **Min Length**: 1
- **Max Length**: 10

### CapabilityVersion
- **Type**: string
- **Pattern**: `(0|[1-9][0-9]*)`
- **Min Length**: 1
- **Max Length**: 64

### ClientToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=_-]+`
- **Min Length**: 1
- **Max Length**: 64

### ConfigurationErrorCode
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 256

### ConfigurationErrorMessage
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-._,]+`
- **Min Length**: 1
- **Max Length**: 65535

### ConnectorAssociationId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 64

### ConnectorDeviceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.,@-]+`
- **Min Length**: 1
- **Max Length**: 256

### ConnectorPolicyId
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_]+`
- **Min Length**: 1
- **Max Length**: 64

### CredentialLockerArn
- **Type**: string
- **Pattern**: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:credential-locker/[0-9a-zA-Z]+`
- **Min Length**: 32
- **Max Length**: 1011

### CredentialLockerId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 64

### CredentialLockerName
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_ ]+`
- **Min Length**: 1
- **Max Length**: 128

### DeliveryDestinationArn
- **Type**: string
- **Pattern**: `arn:aws:[0-9a-zA-Z]+:[0-9a-zA-Z-]+:[0-9]+:[0-9a-zA-Z]+/[0-9a-zA-Z._-]+`
- **Min Length**: 20
- **Max Length**: 2048

### DestinationDescription
- **Type**: string
- **Pattern**: `[0-9A-Za-z_\- ]+`
- **Min Length**: 1
- **Max Length**: 256

### DestinationName
- **Type**: string
- **Pattern**: `[\p{L}\p{N} ._-]+`
- **Min Length**: 1
- **Max Length**: 128

### DeviceDiscoveryArn
- **Type**: string
- **Pattern**: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:device-discovery/[0-9a-zA-Z]+`

### DeviceDiscoveryId
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 200

### DeviceSpecificKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=_.,@\+\-]+`
- **Min Length**: 1
- **Max Length**: 128

### DeviceType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=_. ,@\+\-/]+`
- **Min Length**: 0
- **Max Length**: 256

### DiscoveryAuthMaterialString
- **Type**: string
- **Pattern**: `[0-9A-Za-z_\-\+=\/:; ]+`
- **Min Length**: 1
- **Max Length**: 64

### EndpointAddress
- **Type**: string
- **Pattern**: `[A-Za-z0-9._@-]+`
- **Min Length**: 1
- **Max Length**: 256

### EndpointId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 64

### EventName
- **Type**: string
- **Pattern**: `[/a-zA-Z0-9\._ ]+`
- **Min Length**: 1
- **Max Length**: 128

### InternationalArticleNumber
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 8
- **Max Length**: 13

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws:kms:[0-9a-zA-Z-]+:[0-9]+:key/[0-9a-zA-Z-]+`
- **Min Length**: 1
- **Max Length**: 200

### LogConfigurationId
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 200

### ManagedThingArn
- **Type**: string
- **Pattern**: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:managed-thing/([0-9a-zA-Z:_-])+`
- **Min Length**: 32
- **Max Length**: 1011

### ManagedThingId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]*`
- **Min Length**: 1
- **Max Length**: 64

### Model
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_ ]+`
- **Min Length**: 1
- **Max Length**: 128

### Name
- **Type**: string
- **Pattern**: `[\p{L}\p{N} ._-]+`
- **Min Length**: 1
- **Max Length**: 128

### NextToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=_-]+`
- **Min Length**: 1
- **Max Length**: 65535

### NodeId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=_.,@\+\-/]+`
- **Min Length**: 1
- **Max Length**: 64

### OtaDescription
- **Type**: string
- **Pattern**: `[0-9A-Za-z_\- ]+`
- **Min Length**: 1
- **Max Length**: 256

### OtaNextToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9=_+/-]+`
- **Min Length**: 1
- **Max Length**: 65535

### OtaTaskArn
- **Type**: string
- **Pattern**: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:ota-task/[0-9a-zA-Z]+`
- **Min Length**: 0
- **Max Length**: 1011

### OtaTaskConfigurationId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 64

### OtaTaskConfigurationName
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_ ]+`
- **Min Length**: 1
- **Max Length**: 128

### OtaTaskId
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 200

### Owner
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.,@-]+`
- **Min Length**: 1
- **Max Length**: 64

### ParentControllerId
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 64

### PropertyName
- **Type**: string
- **Pattern**: `[/a-zA-Z0-9\._ ]+`
- **Min Length**: 1
- **Max Length**: 128

### ProvisioningProfileArn
- **Type**: string
- **Pattern**: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:provisioning-profile/[0-9a-zA-Z]+`
- **Min Length**: 32
- **Max Length**: 64

### ProvisioningProfileId
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_]+`
- **Min Length**: 1
- **Max Length**: 64

### ProvisioningProfileName
- **Type**: string
- **Pattern**: `[0-9A-Za-z_-]+`
- **Min Length**: 1
- **Max Length**: 36

### SchemaId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9./]+`
- **Min Length**: 1
- **Max Length**: 128

### SchemaVersionDescription
- **Type**: string
- **Pattern**: `[a-zA-Z0-9., ]+`
- **Min Length**: 1
- **Max Length**: 256

### SchemaVersionNamespaceName
- **Type**: string
- **Pattern**: `[a-z]+`
- **Min Length**: 1
- **Max Length**: 256

### SchemaVersionVersion
- **Type**: string
- **Pattern**: `(\d+\.\d+|\$latest)`
- **Min Length**: 1
- **Max Length**: 256

### SchemaVersionedId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9.\/]+(@(\d+\.\d+|\$latest))?`
- **Min Length**: 1
- **Max Length**: 128

### SerialNumber
- **Type**: string
- **Pattern**: `[A-Za-z0-9-_ ]+`
- **Min Length**: 1
- **Max Length**: 128

### SmartHomeResourceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9+*]*`
- **Min Length**: 1
- **Max Length**: 200

### SmartHomeResourceType
- **Type**: string
- **Pattern**: `[*]$|^(managed-thing|credential-locker|provisioning-profile|ota-task)`

### TraceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:=_-]+`
- **Min Length**: 1
- **Max Length**: 128

### UniversalProductCode
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 12
- **Max Length**: 12


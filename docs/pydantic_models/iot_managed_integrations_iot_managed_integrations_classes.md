# Iot Managed Integrations Iot Managed Integrations Classes

# AbortConfigCriteria

### Action
- **Type**: typing.Optional[typing.Literal['CANCEL']]

### FailureType
- **Type**: typing.Optional[typing.Literal['ALL', 'FAILED', 'REJECTED', 'TIMED_OUT']]

### MinNumberOfExecutedThings
- **Type**: typing.Optional[int]

### ThresholdPercentage
- **Type**: typing.Optional[float]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapabilityAction

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ref
- **Type**: typing.Optional[str]

### actionTraceId
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# CapabilityReport

### version
- **Type**: <class 'str'>
- **Required**: Yes

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReportEndpoint]
- **Required**: Yes

### nodeId
- **Type**: typing.Optional[str]


# CapabilityReportCapability

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.List[str]
- **Required**: Yes

### actions
- **Type**: typing.List[str]
- **Required**: Yes

### events
- **Type**: typing.List[str]
- **Required**: Yes


# CapabilityReportCapabilityOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.List[str]
- **Required**: Yes

### actions
- **Type**: typing.List[str]
- **Required**: Yes

### events
- **Type**: typing.List[str]
- **Required**: Yes


# CapabilityReportEndpoint

### id
- **Type**: <class 'str'>
- **Required**: Yes

### deviceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### capabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReportCapability]
- **Required**: Yes


# CapabilityReportEndpointOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### deviceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### capabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReportCapabilityOutput]
- **Required**: Yes


# CapabilityReportOutput

### version
- **Type**: <class 'str'>
- **Required**: Yes

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReportEndpointOutput]
- **Required**: Yes

### nodeId
- **Type**: typing.Optional[str]


# CommandCapability

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityAction]
- **Required**: Yes


# CommandEndpoint

### endpointId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CommandCapability]
- **Required**: Yes


# ConfigurationError

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# ConfigurationStatus

### state
- **Type**: typing.Literal['ENABLED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ConfigurationError]


# CreateCredentialLockerRequest

### Name
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCredentialLockerResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDestinationRequest

### DeliveryDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryDestinationType
- **Type**: typing.Literal['KINESIS']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDestinationResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventLogConfigurationRequest

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### EventLogLevel
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes

### ResourceId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# CreateEventLogConfigurationResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateManagedThingRequest

### Role
- **Type**: typing.Literal['CONTROLLER', 'DEVICE']
- **Required**: Yes

### AuthenticationMaterial
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMaterialType
- **Type**: typing.Literal['WIFI_SETUP_QR_BAR_CODE', 'ZIGBEE_QR_BAR_CODE', 'ZWAVE_QR_BAR_CODE']
- **Required**: Yes

### Owner
- **Type**: typing.Optional[str]

### CredentialLockerId
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### Brand
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CapabilityReport
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReport, aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReportOutput, NoneType]

### Capabilities
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Classification
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### MetaData
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateManagedThingResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNotificationConfigurationRequest

### EventType
- **Type**: typing.Literal['CONNECTOR_ASSOCIATION', 'CONNECTOR_ERROR_REPORT', 'DEVICE_COMMAND', 'DEVICE_COMMAND_REQUEST', 'DEVICE_EVENT', 'DEVICE_LIFE_CYCLE', 'DEVICE_OTA', 'DEVICE_STATE']
- **Required**: Yes

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNotificationConfigurationResponse

### EventType
- **Type**: typing.Literal['CONNECTOR_ASSOCIATION', 'CONNECTOR_ERROR_REPORT', 'DEVICE_COMMAND', 'DEVICE_COMMAND_REQUEST', 'DEVICE_EVENT', 'DEVICE_LIFE_CYCLE', 'DEVICE_OTA', 'DEVICE_STATE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOtaTaskConfigurationRequest

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PushConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PushConfig, aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PushConfigOutput, NoneType]

### ClientToken
- **Type**: typing.Optional[str]


# CreateOtaTaskConfigurationResponse

### TaskConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOtaTaskRequest

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes

### OtaType
- **Type**: typing.Literal['CONTINUOUS', 'ONE_TIME']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[typing.Literal['HTTP']]

### Target
- **Type**: typing.Optional[typing.List[str]]

### TaskConfigurationId
- **Type**: typing.Optional[str]

### OtaMechanism
- **Type**: typing.Optional[typing.Literal['PUSH']]

### OtaTargetQueryString
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### OtaSchedulingConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskSchedulingConfig, aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskSchedulingConfigOutput, NoneType]

### OtaTaskExecutionRetryConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskExecutionRetryConfig, aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskExecutionRetryConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateOtaTaskResponse

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProvisioningProfileRequest

### ProvisioningType
- **Type**: typing.Literal['FLEET_PROVISIONING', 'JITR']
- **Required**: Yes

### CaCertificate
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateProvisioningProfileResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningType
- **Type**: typing.Literal['FLEET_PROVISIONING', 'JITR']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ClaimCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### ClaimCertificatePrivateKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# CredentialLockerSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteCredentialLockerRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventLogConfigurationRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteManagedThingRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# DeleteNotificationConfigurationRequest

### EventType
- **Type**: typing.Literal['CONNECTOR_ASSOCIATION', 'CONNECTOR_ERROR_REPORT', 'DEVICE_COMMAND', 'DEVICE_COMMAND_REQUEST', 'DEVICE_EVENT', 'DEVICE_LIFE_CYCLE', 'DEVICE_OTA', 'DEVICE_STATE']
- **Required**: Yes


# DeleteOtaTaskConfigurationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOtaTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisioningProfileRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationSummary

### Description
- **Type**: typing.Optional[str]

### DeliveryDestinationArn
- **Type**: typing.Optional[str]

### DeliveryDestinationType
- **Type**: typing.Optional[typing.Literal['KINESIS']]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# EventLogConfigurationSummary

### Id
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### EventLogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]


# ExponentialRolloutRate

### BaseRatePerMinute
- **Type**: typing.Optional[int]

### IncrementFactor
- **Type**: typing.Optional[float]

### RateIncreaseCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.RolloutRateIncreaseCriteria]


# GetCredentialLockerRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCredentialLockerResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetCustomEndpointResponse

### EndpointAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetDefaultEncryptionConfigurationResponse

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ConfigurationStatus'>
- **Required**: Yes

### encryptionType
- **Type**: typing.Literal['CUSTOMER_KEY_ENCRYPTION', 'MANAGED_INTEGRATIONS_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDestinationResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryDestinationType
- **Type**: typing.Literal['KINESIS']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceDiscoveryRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceDiscoveryResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveryType
- **Type**: typing.Literal['CLOUD', 'ZIGBEE', 'ZWAVE']
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ControllerId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### FinishedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventLogConfigurationRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventLogConfigurationResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### EventLogLevel
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetHubConfigurationResponse

### HubTokenTimerExpirySettingInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedThingCapabilitiesRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedThingCapabilitiesResponse

### ManagedThingId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: <class 'str'>
- **Required**: Yes

### CapabilityReport
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReportOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedThingConnectivityDataRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedThingConnectivityDataResponse

### ManagedThingId
- **Type**: <class 'str'>
- **Required**: Yes

### Connected
- **Type**: <class 'bool'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DisconnectReason
- **Type**: typing.Literal['AUTH_ERROR', 'CLIENT_ERROR', 'CLIENT_INITIATED_DISCONNECT', 'CONNECTION_LOST', 'CUSTOMAUTH_TTL_EXPIRATION', 'DUPLICATE_CLIENTID', 'FORBIDDEN_ACCESS', 'MQTT_KEEP_ALIVE_TIMEOUT', 'NONE', 'SERVER_ERROR', 'SERVER_INITIATED_DISCONNECT', 'THROTTLED', 'UNKNOWN', 'WEBSOCKET_TTL_EXPIRATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedThingMetaDataRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedThingMetaDataResponse

### ManagedThingId
- **Type**: <class 'str'>
- **Required**: Yes

### MetaData
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedThingRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedThingResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Owner
- **Type**: <class 'str'>
- **Required**: Yes

### CredentialLockerId
- **Type**: <class 'str'>
- **Required**: Yes

### AdvertisedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Literal['CONTROLLER', 'DEVICE']
- **Required**: Yes

### ProvisioningStatus
- **Type**: typing.Literal['ACTIVATED', 'DELETED', 'DELETE_IN_PROGRESS', 'DELETION_FAILED', 'DISCOVERED', 'ISOLATED', 'PRE_ASSOCIATED', 'UNASSOCIATED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Model
- **Type**: <class 'str'>
- **Required**: Yes

### Brand
- **Type**: <class 'str'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### UniversalProductCode
- **Type**: <class 'str'>
- **Required**: Yes

### InternationalArticleNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceSpecificKey
- **Type**: <class 'str'>
- **Required**: Yes

### MacAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ParentControllerId
- **Type**: <class 'str'>
- **Required**: Yes

### Classification
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ActivatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HubNetworkMode
- **Type**: typing.Literal['NETWORK_WIDE_EXCLUSION', 'STANDARD']
- **Required**: Yes

### MetaData
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedThingStateRequest

### ManagedThingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedThingStateResponse

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.StateEndpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetNotificationConfigurationRequest

### EventType
- **Type**: typing.Literal['CONNECTOR_ASSOCIATION', 'CONNECTOR_ERROR_REPORT', 'DEVICE_COMMAND', 'DEVICE_COMMAND_REQUEST', 'DEVICE_EVENT', 'DEVICE_LIFE_CYCLE', 'DEVICE_OTA', 'DEVICE_STATE']
- **Required**: Yes


# GetNotificationConfigurationResponse

### EventType
- **Type**: typing.Literal['CONNECTOR_ASSOCIATION', 'CONNECTOR_ERROR_REPORT', 'DEVICE_COMMAND', 'DEVICE_COMMAND_REQUEST', 'DEVICE_EVENT', 'DEVICE_LIFE_CYCLE', 'DEVICE_OTA', 'DEVICE_STATE']
- **Required**: Yes

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetOtaTaskConfigurationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetOtaTaskConfigurationResponse

### TaskConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PushConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PushConfigOutput'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetOtaTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetOtaTaskResponse

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['HTTP']
- **Required**: Yes

### OtaType
- **Type**: typing.Literal['CONTINUOUS', 'ONE_TIME']
- **Required**: Yes

### OtaTargetQueryString
- **Type**: <class 'str'>
- **Required**: Yes

### OtaMechanism
- **Type**: typing.Literal['PUSH']
- **Required**: Yes

### Target
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TaskConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskProcessingDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.TaskProcessingDetails'>
- **Required**: Yes

### OtaSchedulingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskSchedulingConfigOutput'>
- **Required**: Yes

### OtaTaskExecutionRetryConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskExecutionRetryConfigOutput'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELED', 'COMPLETED', 'DELETION_IN_PROGRESS', 'IN_PROGRESS', 'SCHEDULED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetProvisioningProfileRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProvisioningProfileResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningType
- **Type**: typing.Literal['FLEET_PROVISIONING', 'JITR']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ClaimCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetRuntimeLogConfigurationRequest

### ManagedThingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuntimeLogConfigurationResponse

### ManagedThingId
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeLogConfigurations
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.RuntimeLogConfigurations'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaVersionRequest

### Type
- **Type**: typing.Literal['capability', 'definition']
- **Required**: Yes

### SchemaVersionedId
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['AWS', 'CONNECTOR', 'ZCL']]


# GetSchemaVersionResponse

### SchemaId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['capability', 'definition']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Visibility
- **Type**: typing.Literal['PRIVATE', 'PUBLIC']
- **Required**: Yes

### Schema
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# ListCredentialLockersRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCredentialLockersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListCredentialLockersResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CredentialLockerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDestinationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDestinationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListDestinationsResponse

### DestinationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.DestinationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventLogConfigurationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventLogConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListEventLogConfigurationsResponse

### EventLogConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.EventLogConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedThingSchemasRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointIdFilter
- **Type**: typing.Optional[str]

### CapabilityIdFilter
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListManagedThingSchemasRequestPaginate

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointIdFilter
- **Type**: typing.Optional[str]

### CapabilityIdFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListManagedThingSchemasResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ManagedThingSchemaListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedThingsRequest

### OwnerFilter
- **Type**: typing.Optional[str]

### CredentialLockerFilter
- **Type**: typing.Optional[str]

### RoleFilter
- **Type**: typing.Optional[typing.Literal['CONTROLLER', 'DEVICE']]

### ParentControllerIdentifierFilter
- **Type**: typing.Optional[str]

### ConnectorPolicyIdFilter
- **Type**: typing.Optional[str]

### SerialNumberFilter
- **Type**: typing.Optional[str]

### ProvisioningStatusFilter
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DELETED', 'DELETE_IN_PROGRESS', 'DELETION_FAILED', 'DISCOVERED', 'ISOLATED', 'PRE_ASSOCIATED', 'UNASSOCIATED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListManagedThingsRequestPaginate

### OwnerFilter
- **Type**: typing.Optional[str]

### CredentialLockerFilter
- **Type**: typing.Optional[str]

### RoleFilter
- **Type**: typing.Optional[typing.Literal['CONTROLLER', 'DEVICE']]

### ParentControllerIdentifierFilter
- **Type**: typing.Optional[str]

### ConnectorPolicyIdFilter
- **Type**: typing.Optional[str]

### SerialNumberFilter
- **Type**: typing.Optional[str]

### ProvisioningStatusFilter
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DELETED', 'DELETE_IN_PROGRESS', 'DELETION_FAILED', 'DISCOVERED', 'ISOLATED', 'PRE_ASSOCIATED', 'UNASSOCIATED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListManagedThingsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ManagedThingSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListNotificationConfigurationsResponse

### NotificationConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.NotificationConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOtaTaskConfigurationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOtaTaskConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListOtaTaskConfigurationsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOtaTaskExecutionsRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOtaTaskExecutionsRequestPaginate

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListOtaTaskExecutionsResponse

### ExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskExecutionSummaries]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOtaTasksRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOtaTasksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListOtaTasksResponse

### Tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProvisioningProfilesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProvisioningProfilesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListProvisioningProfilesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ProvisioningProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaVersionsRequest

### Type
- **Type**: typing.Literal['capability', 'definition']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SchemaId
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### SemanticVersion
- **Type**: typing.Optional[str]


# ListSchemaVersionsRequestPaginate

### Type
- **Type**: typing.Literal['capability', 'definition']
- **Required**: Yes

### SchemaId
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### SemanticVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.PaginatorConfig]


# ListSchemaVersionsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.SchemaVersionListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ManagedThingSchemaListItem

### EndpointId
- **Type**: typing.Optional[str]

### CapabilityId
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ManagedThingSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### AdvertisedProductId
- **Type**: typing.Optional[str]

### Brand
- **Type**: typing.Optional[str]

### Classification
- **Type**: typing.Optional[str]

### ConnectorDeviceId
- **Type**: typing.Optional[str]

### ConnectorPolicyId
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### CredentialLockerId
- **Type**: typing.Optional[str]

### ParentControllerId
- **Type**: typing.Optional[str]

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DELETED', 'DELETE_IN_PROGRESS', 'DELETION_FAILED', 'DISCOVERED', 'ISOLATED', 'PRE_ASSOCIATED', 'UNASSOCIATED']]

### Role
- **Type**: typing.Optional[typing.Literal['CONTROLLER', 'DEVICE']]

### SerialNumber
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ActivatedAt
- **Type**: typing.Optional[datetime.datetime]


# NotificationConfigurationSummary

### EventType
- **Type**: typing.Optional[typing.Literal['CONNECTOR_ASSOCIATION', 'CONNECTOR_ERROR_REPORT', 'DEVICE_COMMAND', 'DEVICE_COMMAND_REQUEST', 'DEVICE_EVENT', 'DEVICE_LIFE_CYCLE', 'DEVICE_OTA', 'DEVICE_STATE']]

### DestinationName
- **Type**: typing.Optional[str]


# OtaTaskAbortConfig

### AbortConfigCriteriaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.AbortConfigCriteria]]


# OtaTaskAbortConfigOutput

### AbortConfigCriteriaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.AbortConfigCriteria]]


# OtaTaskConfigurationSummary

### TaskConfigurationId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# OtaTaskExecutionRetryConfig

### RetryConfigCriteria
- **Type**: typing.Optional[typing.List[NoneType]]


# OtaTaskExecutionRetryConfigOutput

### RetryConfigCriteria
- **Type**: typing.Optional[typing.List[NoneType]]


# OtaTaskExecutionRolloutConfig

### ExponentialRolloutRate
- **Type**: <class 'NoneType'>

### MaximumPerMinute
- **Type**: typing.Optional[int]


# OtaTaskExecutionSummaries

### TaskExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskExecutionSummary]

### ManagedThingId
- **Type**: typing.Optional[str]


# OtaTaskExecutionSummary

### ExecutionNumber
- **Type**: typing.Optional[int]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### QueuedAt
- **Type**: typing.Optional[datetime.datetime]

### RetryAttempt
- **Type**: typing.Optional[int]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]


# OtaTaskSchedulingConfig

### EndBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL', 'FORCE_CANCEL', 'STOP_ROLLOUT']]

### EndTime
- **Type**: typing.Optional[str]

### MaintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ScheduleMaintenanceWindow]]

### StartTime
- **Type**: typing.Optional[str]


# OtaTaskSchedulingConfigOutput

### EndBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL', 'FORCE_CANCEL', 'STOP_ROLLOUT']]

### EndTime
- **Type**: typing.Optional[str]

### MaintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ScheduleMaintenanceWindow]]

### StartTime
- **Type**: typing.Optional[str]


# OtaTaskSummary

### TaskId
- **Type**: typing.Optional[str]

### TaskArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### TaskConfigurationId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'DELETION_IN_PROGRESS', 'IN_PROGRESS', 'SCHEDULED']]


# OtaTaskTimeoutConfig

### InProgressTimeoutInMinutes
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProvisioningProfileSummary

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ProvisioningType
- **Type**: typing.Optional[typing.Literal['FLEET_PROVISIONING', 'JITR']]


# PushConfig

### AbortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskAbortConfig]

### RolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskExecutionRolloutConfig]

### TimeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskTimeoutConfig]


# PushConfigOutput

### AbortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskAbortConfigOutput]

### RolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskExecutionRolloutConfig]

### TimeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.OtaTaskTimeoutConfig]


# PutDefaultEncryptionConfigurationRequest

### encryptionType
- **Type**: typing.Literal['CUSTOMER_KEY_ENCRYPTION', 'MANAGED_INTEGRATIONS_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# PutDefaultEncryptionConfigurationResponse

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ConfigurationStatus'>
- **Required**: Yes

### encryptionType
- **Type**: typing.Literal['CUSTOMER_KEY_ENCRYPTION', 'MANAGED_INTEGRATIONS_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# PutHubConfigurationRequest

### HubTokenTimerExpirySettingInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# PutHubConfigurationResponse

### HubTokenTimerExpirySettingInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# PutRuntimeLogConfigurationRequest

### ManagedThingId
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeLogConfigurations
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.RuntimeLogConfigurations'>
- **Required**: Yes


# RegisterCustomEndpointResponse

### EndpointAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# ResetRuntimeLogConfigurationRequest

### ManagedThingId
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


# RetryConfigCriteria

### FailureType
- **Type**: typing.Optional[typing.Literal['ALL', 'FAILED', 'TIMED_OUT']]

### MinNumberOfRetries
- **Type**: typing.Optional[int]


# RolloutRateIncreaseCriteria

### numberOfNotifiedThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]


# RuntimeLogConfigurations

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]

### LogFlushLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']]

### LocalStoreLocation
- **Type**: typing.Optional[str]

### LocalStoreFileRotationMaxFiles
- **Type**: typing.Optional[int]

### LocalStoreFileRotationMaxBytes
- **Type**: typing.Optional[int]

### UploadLog
- **Type**: typing.Optional[bool]

### UploadPeriodMinutes
- **Type**: typing.Optional[int]

### DeleteLocalStoreAfterUpload
- **Type**: typing.Optional[bool]


# ScheduleMaintenanceWindow

### DurationInMinutes
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[str]


# SchemaVersionListItem

### SchemaId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['capability', 'definition']]

### Description
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### SemanticVersion
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]


# SendManagedThingCommandRequest

### ManagedThingId
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CommandEndpoint]
- **Required**: Yes

### ConnectorAssociationId
- **Type**: typing.Optional[str]


# SendManagedThingCommandResponse

### TraceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# StartDeviceDiscoveryRequest

### DiscoveryType
- **Type**: typing.Literal['CLOUD', 'ZIGBEE', 'ZWAVE']
- **Required**: Yes

### ControllerIdentifier
- **Type**: typing.Optional[str]

### ConnectorAssociationIdentifier
- **Type**: typing.Optional[str]

### AuthenticationMaterial
- **Type**: typing.Optional[str]

### AuthenticationMaterialType
- **Type**: typing.Optional[typing.Literal['ZWAVE_INSTALL_CODE']]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartDeviceDiscoveryResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.ResponseMetadata'>
- **Required**: Yes


# StateCapability

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# StateEndpoint

### endpointId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.StateCapability]
- **Required**: Yes


# TaskProcessingDetails

### NumberOfCanceledThings
- **Type**: typing.Optional[int]

### NumberOfFailedThings
- **Type**: typing.Optional[int]

### NumberOfInProgressThings
- **Type**: typing.Optional[int]

### numberOfQueuedThings
- **Type**: typing.Optional[int]

### numberOfRejectedThings
- **Type**: typing.Optional[int]

### numberOfRemovedThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]

### numberOfTimedOutThings
- **Type**: typing.Optional[int]

### processingTargets
- **Type**: typing.Optional[typing.List[str]]


# UpdateDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryDestinationArn
- **Type**: typing.Optional[str]

### DeliveryDestinationType
- **Type**: typing.Optional[typing.Literal['KINESIS']]

### RoleArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateEventLogConfigurationRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### EventLogLevel
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO', 'WARN']
- **Required**: Yes


# UpdateManagedThingRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Owner
- **Type**: typing.Optional[str]

### CredentialLockerId
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### Brand
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CapabilityReport
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReport, aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_classes.CapabilityReportOutput, NoneType]

### Capabilities
- **Type**: typing.Optional[str]

### Classification
- **Type**: typing.Optional[str]

### HubNetworkMode
- **Type**: typing.Optional[typing.Literal['NETWORK_WIDE_EXCLUSION', 'STANDARD']]

### MetaData
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateNotificationConfigurationRequest

### EventType
- **Type**: typing.Literal['CONNECTOR_ASSOCIATION', 'CONNECTOR_ERROR_REPORT', 'DEVICE_COMMAND', 'DEVICE_COMMAND_REQUEST', 'DEVICE_EVENT', 'DEVICE_LIFE_CYCLE', 'DEVICE_OTA', 'DEVICE_STATE']
- **Required**: Yes

### DestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateOtaTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### TaskConfigurationId
- **Type**: typing.Optional[str]



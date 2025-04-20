# Chime Sdk Voice Chime Sdk Voice Classes

# Address

### streetName
- **Type**: typing.Optional[str]

### streetSuffix
- **Type**: typing.Optional[str]

### postDirectional
- **Type**: typing.Optional[str]

### preDirectional
- **Type**: typing.Optional[str]

### streetNumber
- **Type**: typing.Optional[str]

### city
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]

### postalCode
- **Type**: typing.Optional[str]

### postalCodePlus4
- **Type**: typing.Optional[str]

### country
- **Type**: typing.Optional[str]


# AssociatePhoneNumbersWithVoiceConnectorGroupRequest

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### ForceAssociate
- **Type**: typing.Optional[bool]


# AssociatePhoneNumbersWithVoiceConnectorGroupResponse

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatePhoneNumbersWithVoiceConnectorRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### ForceAssociate
- **Type**: typing.Optional[bool]


# AssociatePhoneNumbersWithVoiceConnectorResponse

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeletePhoneNumberRequest

### PhoneNumberIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeletePhoneNumberResponse

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdatePhoneNumberRequest

### UpdatePhoneNumberRequestItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.UpdatePhoneNumberRequestItem]
- **Required**: Yes


# BatchUpdatePhoneNumberResponse

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CallDetails

### VoiceConnectorId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]

### IsCaller
- **Type**: typing.Optional[bool]


# CandidateAddress

### streetInfo
- **Type**: typing.Optional[str]

### streetNumber
- **Type**: typing.Optional[str]

### city
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]

### postalCode
- **Type**: typing.Optional[str]

### postalCodePlus4
- **Type**: typing.Optional[str]

### country
- **Type**: typing.Optional[str]


# CreatePhoneNumberOrderRequest

### ProductType
- **Type**: typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# CreatePhoneNumberOrderResponse

### PhoneNumberOrder
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberOrder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProxySessionRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantPhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### Capabilities
- **Type**: typing.List[typing.Literal['SMS', 'Voice']]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### ExpiryMinutes
- **Type**: typing.Optional[int]

### NumberSelectionBehavior
- **Type**: typing.Optional[typing.Literal['AvoidSticky', 'PreferSticky']]

### GeoMatchLevel
- **Type**: typing.Optional[typing.Literal['AreaCode', 'Country']]

### GeoMatchParams
- **Type**: <class 'NoneType'>


# CreateProxySessionResponse

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ProxySession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSipMediaApplicationCallRequest

### FromPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ToPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SipHeaders
- **Type**: typing.Optional[typing.Dict[str, str]]

### ArgumentsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSipMediaApplicationCallResponse

### SipMediaApplicationCall
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationCall'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSipMediaApplicationRequest

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationEndpoint]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Tag]]


# CreateSipMediaApplicationResponse

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplication'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSipRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TriggerType
- **Type**: typing.Literal['RequestUriHostname', 'ToPhoneNumber']
- **Required**: Yes

### TriggerValue
- **Type**: <class 'str'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]

### TargetApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipRuleTargetApplication]]


# CreateSipRuleResponse

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVoiceConnectorGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceConnectorItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorItem]]


# CreateVoiceConnectorGroupResponse

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVoiceConnectorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequireEncryption
- **Type**: <class 'bool'>
- **Required**: Yes

### AwsRegion
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'us-east-1', 'us-west-2']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Tag]]

### IntegrationType
- **Type**: typing.Optional[typing.Literal['CONNECT_ANALYTICS_CONNECTOR', 'CONNECT_CALL_TRANSFER_CONNECTOR']]


# CreateVoiceConnectorResponse

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVoiceProfileDomainRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideEncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ServerSideEncryptionConfiguration'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Tag]]


# CreateVoiceProfileDomainResponse

### VoiceProfileDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceProfileDomain'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVoiceProfileRequest

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateVoiceProfileResponse

### VoiceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# Credential

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# DNISEmergencyCallingConfiguration

### EmergencyPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### CallingCountry
- **Type**: <class 'str'>
- **Required**: Yes

### TestPhoneNumber
- **Type**: typing.Optional[str]


# DeletePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProxySessionRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSipMediaApplicationRequest

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSipRuleRequest

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorEmergencyCallingConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorExternalSystemsConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorGroupRequest

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorOriginationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorProxyRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorStreamingConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorTerminationCredentialsRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Usernames
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteVoiceConnectorTerminationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceProfileDomainRequest

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceProfileRequest

### VoiceProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorGroupRequest

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorGroupResponse

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorResponse

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# EmergencyCallingConfiguration

### DNIS
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.DNISEmergencyCallingConfiguration]]


# EmergencyCallingConfigurationOutput

### DNIS
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.DNISEmergencyCallingConfiguration]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# ExternalSystemsConfiguration

### SessionBorderControllerTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIOCODES_MEDIANT_SBC', 'AVAYA_SBCE', 'CISCO_UNIFIED_BORDER_ELEMENT', 'ORACLE_ACME_PACKET_SBC', 'RIBBON_SBC']]]

### ContactCenterSystemTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AVAYA_AURA_CALL_CENTER_ELITE', 'AVAYA_AURA_CONTACT_CENTER', 'CISCO_UNIFIED_CONTACT_CENTER_ENTERPRISE', 'GENESYS_ENGAGE_ON_PREMISES']]]


# GeoMatchParams

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### AreaCode
- **Type**: <class 'str'>
- **Required**: Yes


# GetGlobalSettingsResponse

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetPhoneNumberOrderRequest

### PhoneNumberOrderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPhoneNumberOrderResponse

### PhoneNumberOrder
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberOrder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetPhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPhoneNumberResponse

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumber'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetPhoneNumberSettingsResponse

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes

### CallingNameUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetProxySessionRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProxySessionResponse

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ProxySession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetSipMediaApplicationAlexaSkillConfigurationRequest

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipMediaApplicationAlexaSkillConfigurationResponse

### SipMediaApplicationAlexaSkillConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetSipMediaApplicationLoggingConfigurationRequest

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipMediaApplicationLoggingConfigurationResponse

### SipMediaApplicationLoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationLoggingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetSipMediaApplicationRequest

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipMediaApplicationResponse

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplication'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetSipRuleRequest

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipRuleResponse

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetSpeakerSearchTaskRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpeakerSearchTaskResponse

### SpeakerSearchTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SpeakerSearchTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorEmergencyCallingConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorEmergencyCallingConfigurationResponse

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.EmergencyCallingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorExternalSystemsConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorExternalSystemsConfigurationResponse

### ExternalSystemsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ExternalSystemsConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorGroupRequest

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorGroupResponse

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorLoggingConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorLoggingConfigurationResponse

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.LoggingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorOriginationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorOriginationResponse

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.OriginationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorProxyRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorProxyResponse

### Proxy
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Proxy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorResponse

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorStreamingConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorStreamingConfigurationResponse

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.StreamingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorTerminationHealthRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorTerminationHealthResponse

### TerminationHealth
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.TerminationHealth'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceConnectorTerminationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorTerminationResponse

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.TerminationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceProfileDomainRequest

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceProfileDomainResponse

### VoiceProfileDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceProfileDomain'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceProfileRequest

### VoiceProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceProfileResponse

### VoiceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceToneAnalysisTaskRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceToneAnalysisTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### IsCaller
- **Type**: <class 'bool'>
- **Required**: Yes


# GetVoiceToneAnalysisTaskResponse

### VoiceToneAnalysisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceToneAnalysisTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# ListAvailableVoiceConnectorRegionsResponse

### VoiceConnectorRegions
- **Type**: typing.List[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'us-east-1', 'us-west-2']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# ListPhoneNumberOrdersRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPhoneNumberOrdersResponse

### PhoneNumberOrders
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberOrder]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersRequest

### Status
- **Type**: typing.Optional[str]

### ProductType
- **Type**: typing.Optional[typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']]

### FilterName
- **Type**: typing.Optional[typing.Literal['SipRuleId', 'VoiceConnectorGroupId', 'VoiceConnectorId']]

### FilterValue
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersResponse

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumber]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProxySessionsRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Closed', 'InProgress', 'Open']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProxySessionsResponse

### ProxySessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ProxySession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSipMediaApplicationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSipMediaApplicationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PaginatorConfig]


# ListSipMediaApplicationsResponse

### SipMediaApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplication]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSipRulesRequest

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSipRulesRequestPaginate

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PaginatorConfig]


# ListSipRulesResponse

### SipRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedPhoneNumberCountriesRequest

### ProductType
- **Type**: typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']
- **Required**: Yes


# ListSupportedPhoneNumberCountriesResponse

### PhoneNumberCountries
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberCountry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# ListVoiceConnectorGroupsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceConnectorGroupsResponse

### VoiceConnectorGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVoiceConnectorTerminationCredentialsRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# ListVoiceConnectorTerminationCredentialsResponse

### Usernames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# ListVoiceConnectorsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceConnectorsResponse

### VoiceConnectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVoiceProfileDomainsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceProfileDomainsResponse

### VoiceProfileDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceProfileDomainSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVoiceProfilesRequest

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceProfilesResponse

### VoiceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoggingConfiguration

### EnableSIPLogs
- **Type**: typing.Optional[bool]

### EnableMediaMetricLogs
- **Type**: typing.Optional[bool]


# MediaInsightsConfiguration

### Disabled
- **Type**: typing.Optional[bool]

### ConfigurationArn
- **Type**: typing.Optional[str]


# OrderedPhoneNumber

### E164PhoneNumber
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Acquired', 'Failed', 'Processing']]


# Origination

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.OriginationRoute]]

### Disabled
- **Type**: typing.Optional[bool]


# OriginationOutput

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.OriginationRoute]]

### Disabled
- **Type**: typing.Optional[bool]


# OriginationRoute

### Host
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### Priority
- **Type**: typing.Optional[int]

### Weight
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Participant

### PhoneNumber
- **Type**: typing.Optional[str]

### ProxyPhoneNumber
- **Type**: typing.Optional[str]


# PhoneNumber

### PhoneNumberId
- **Type**: typing.Optional[str]

### E164PhoneNumber
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['Local', 'TollFree']]

### ProductType
- **Type**: typing.Optional[typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']]

### Status
- **Type**: typing.Optional[typing.Literal['AcquireFailed', 'AcquireInProgress', 'Assigned', 'Cancelled', 'DeleteFailed', 'DeleteInProgress', 'PortinCancelRequested', 'PortinInProgress', 'ReleaseFailed', 'ReleaseInProgress', 'Unassigned']]

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberCapabilities]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumberAssociation]]

### CallingName
- **Type**: typing.Optional[str]

### CallingNameStatus
- **Type**: typing.Optional[typing.Literal['Unassigned', 'UpdateFailed', 'UpdateInProgress', 'UpdateSucceeded']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DeletionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### OrderId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# PhoneNumberAssociation

### Value
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[typing.Literal['SipRuleId', 'VoiceConnectorGroupId', 'VoiceConnectorId']]

### AssociatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PhoneNumberCapabilities

### InboundCall
- **Type**: typing.Optional[bool]

### OutboundCall
- **Type**: typing.Optional[bool]

### InboundSMS
- **Type**: typing.Optional[bool]

### OutboundSMS
- **Type**: typing.Optional[bool]

### InboundMMS
- **Type**: typing.Optional[bool]

### OutboundMMS
- **Type**: typing.Optional[bool]


# PhoneNumberCountry

### CountryCode
- **Type**: typing.Optional[str]

### SupportedPhoneNumberTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Local', 'TollFree']]]


# PhoneNumberError

### PhoneNumberId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'Gone', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# PhoneNumberOrder

### PhoneNumberOrderId
- **Type**: typing.Optional[str]

### ProductType
- **Type**: typing.Optional[typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']]

### Status
- **Type**: typing.Optional[typing.Literal['CancelRequested', 'Cancelled', 'ChangeRequested', 'Exception', 'FOC', 'Failed', 'Partial', 'PendingDocuments', 'Processing', 'Submitted', 'Successful']]

### OrderType
- **Type**: typing.Optional[typing.Literal['New', 'Porting']]

### OrderedPhoneNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.OrderedPhoneNumber]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# Proxy

### DefaultSessionExpiryMinutes
- **Type**: typing.Optional[int]

### Disabled
- **Type**: typing.Optional[bool]

### FallBackPhoneNumber
- **Type**: typing.Optional[str]

### PhoneNumberCountries
- **Type**: typing.Optional[typing.List[str]]


# ProxySession

### VoiceConnectorId
- **Type**: typing.Optional[str]

### ProxySessionId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Closed', 'InProgress', 'Open']]

### ExpiryMinutes
- **Type**: typing.Optional[int]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['SMS', 'Voice']]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### EndedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Participants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Participant]]

### NumberSelectionBehavior
- **Type**: typing.Optional[typing.Literal['AvoidSticky', 'PreferSticky']]

### GeoMatchLevel
- **Type**: typing.Optional[typing.Literal['AreaCode', 'Country']]

### GeoMatchParams
- **Type**: <class 'NoneType'>


# PutSipMediaApplicationAlexaSkillConfigurationRequest

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SipMediaApplicationAlexaSkillConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfiguration, aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfigurationOutput, NoneType]


# PutSipMediaApplicationAlexaSkillConfigurationResponse

### SipMediaApplicationAlexaSkillConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# PutSipMediaApplicationLoggingConfigurationRequest

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SipMediaApplicationLoggingConfiguration
- **Type**: <class 'NoneType'>


# PutSipMediaApplicationLoggingConfigurationResponse

### SipMediaApplicationLoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationLoggingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# PutVoiceConnectorEmergencyCallingConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### EmergencyCallingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.EmergencyCallingConfiguration, aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.EmergencyCallingConfigurationOutput]
- **Required**: Yes


# PutVoiceConnectorEmergencyCallingConfigurationResponse

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.EmergencyCallingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# PutVoiceConnectorExternalSystemsConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionBorderControllerTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIOCODES_MEDIANT_SBC', 'AVAYA_SBCE', 'CISCO_UNIFIED_BORDER_ELEMENT', 'ORACLE_ACME_PACKET_SBC', 'RIBBON_SBC']]]

### ContactCenterSystemTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AVAYA_AURA_CALL_CENTER_ELITE', 'AVAYA_AURA_CONTACT_CENTER', 'CISCO_UNIFIED_CONTACT_CENTER_ENTERPRISE', 'GENESYS_ENGAGE_ON_PREMISES']]]


# PutVoiceConnectorExternalSystemsConfigurationResponse

### ExternalSystemsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ExternalSystemsConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# PutVoiceConnectorLoggingConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.LoggingConfiguration'>
- **Required**: Yes


# PutVoiceConnectorLoggingConfigurationResponse

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.LoggingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# PutVoiceConnectorOriginationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Origination
- **Type**: typing.Union[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Origination, aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.OriginationOutput]
- **Required**: Yes


# PutVoiceConnectorOriginationResponse

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.OriginationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# PutVoiceConnectorProxyRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultSessionExpiryMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### PhoneNumberPoolCountries
- **Type**: typing.List[str]
- **Required**: Yes

### FallBackPhoneNumber
- **Type**: typing.Optional[str]

### Disabled
- **Type**: typing.Optional[bool]


# PutVoiceConnectorProxyResponse

### Proxy
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Proxy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# PutVoiceConnectorStreamingConfigurationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.StreamingConfiguration, aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.StreamingConfigurationOutput]
- **Required**: Yes


# PutVoiceConnectorStreamingConfigurationResponse

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.StreamingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# PutVoiceConnectorTerminationCredentialsRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Credentials
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Credential]]


# PutVoiceConnectorTerminationRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Termination
- **Type**: typing.Union[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Termination, aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.TerminationOutput]
- **Required**: Yes


# PutVoiceConnectorTerminationResponse

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.TerminationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
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


# RestorePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# RestorePhoneNumberResponse

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumber'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# SearchAvailablePhoneNumbersRequest

### AreaCode
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### TollFreePrefix
- **Type**: typing.Optional[str]

### PhoneNumberType
- **Type**: typing.Optional[typing.Literal['Local', 'TollFree']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchAvailablePhoneNumbersResponse

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ServerSideEncryptionConfiguration

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# SipMediaApplication

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationEndpoint]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SipMediaApplicationArn
- **Type**: typing.Optional[str]


# SipMediaApplicationAlexaSkillConfiguration

### AlexaSkillStatus
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### AlexaSkillIds
- **Type**: typing.List[str]
- **Required**: Yes


# SipMediaApplicationAlexaSkillConfigurationOutput

### AlexaSkillStatus
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### AlexaSkillIds
- **Type**: typing.List[str]
- **Required**: Yes


# SipMediaApplicationCall

### TransactionId
- **Type**: typing.Optional[str]


# SipMediaApplicationEndpoint

### LambdaArn
- **Type**: typing.Optional[str]


# SipMediaApplicationLoggingConfiguration

### EnableSipMediaApplicationMessageLogs
- **Type**: typing.Optional[bool]


# SipRule

### SipRuleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Disabled
- **Type**: typing.Optional[bool]

### TriggerType
- **Type**: typing.Optional[typing.Literal['RequestUriHostname', 'ToPhoneNumber']]

### TriggerValue
- **Type**: typing.Optional[str]

### TargetApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipRuleTargetApplication]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SipRuleTargetApplication

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### AwsRegion
- **Type**: typing.Optional[str]


# SpeakerSearchDetails

### Results
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SpeakerSearchResult]]

### VoiceprintGenerationStatus
- **Type**: typing.Optional[str]


# SpeakerSearchResult

### ConfidenceScore
- **Type**: typing.Optional[float]

### VoiceProfileId
- **Type**: typing.Optional[str]


# SpeakerSearchTask

### SpeakerSearchTaskId
- **Type**: typing.Optional[str]

### SpeakerSearchTaskStatus
- **Type**: typing.Optional[str]

### CallDetails
- **Type**: <class 'NoneType'>

### SpeakerSearchDetails
- **Type**: <class 'NoneType'>

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StartedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]


# StartSpeakerSearchTaskRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### CallLeg
- **Type**: typing.Optional[typing.Literal['Callee', 'Caller']]


# StartSpeakerSearchTaskResponse

### SpeakerSearchTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SpeakerSearchTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# StartVoiceToneAnalysisTaskRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['en-US']
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartVoiceToneAnalysisTaskResponse

### VoiceToneAnalysisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceToneAnalysisTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# StopSpeakerSearchTaskRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StopVoiceToneAnalysisTaskRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceToneAnalysisTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StreamingConfiguration

### DataRetentionInHours
- **Type**: <class 'int'>
- **Required**: Yes

### Disabled
- **Type**: <class 'bool'>
- **Required**: Yes

### StreamingNotificationTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.StreamingNotificationTarget]]

### MediaInsightsConfiguration
- **Type**: <class 'NoneType'>


# StreamingConfigurationOutput

### DataRetentionInHours
- **Type**: <class 'int'>
- **Required**: Yes

### Disabled
- **Type**: <class 'bool'>
- **Required**: Yes

### StreamingNotificationTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.StreamingNotificationTarget]]

### MediaInsightsConfiguration
- **Type**: <class 'NoneType'>


# StreamingNotificationTarget

### NotificationTarget
- **Type**: typing.Optional[typing.Literal['EventBridge', 'SNS', 'SQS']]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Tag]
- **Required**: Yes


# Termination

### CpsLimit
- **Type**: typing.Optional[int]

### DefaultPhoneNumber
- **Type**: typing.Optional[str]

### CallingRegions
- **Type**: typing.Optional[typing.List[str]]

### CidrAllowedList
- **Type**: typing.Optional[typing.List[str]]

### Disabled
- **Type**: typing.Optional[bool]


# TerminationHealth

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Source
- **Type**: typing.Optional[str]


# TerminationOutput

### CpsLimit
- **Type**: typing.Optional[int]

### DefaultPhoneNumber
- **Type**: typing.Optional[str]

### CallingRegions
- **Type**: typing.Optional[typing.List[str]]

### CidrAllowedList
- **Type**: typing.Optional[typing.List[str]]

### Disabled
- **Type**: typing.Optional[bool]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateGlobalSettingsRequest

### VoiceConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorSettings]


# UpdatePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']]

### CallingName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdatePhoneNumberRequestItem

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']]

### CallingName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdatePhoneNumberResponse

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.PhoneNumber'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePhoneNumberSettingsRequest

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateProxySessionRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.List[typing.Literal['SMS', 'Voice']]
- **Required**: Yes

### ExpiryMinutes
- **Type**: typing.Optional[int]


# UpdateProxySessionResponse

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ProxySession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSipMediaApplicationCallRequest

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### Arguments
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UpdateSipMediaApplicationCallResponse

### SipMediaApplicationCall
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationCall'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSipMediaApplicationRequest

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplicationEndpoint]]


# UpdateSipMediaApplicationResponse

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipMediaApplication'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSipRuleRequest

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]

### TargetApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipRuleTargetApplication]]


# UpdateSipRuleResponse

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.SipRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVoiceConnectorGroupRequest

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceConnectorItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorItem]
- **Required**: Yes


# UpdateVoiceConnectorGroupResponse

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVoiceConnectorRequest

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequireEncryption
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateVoiceConnectorResponse

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVoiceProfileDomainRequest

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateVoiceProfileDomainResponse

### VoiceProfileDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceProfileDomain'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVoiceProfileRequest

### VoiceProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateVoiceProfileResponse

### VoiceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# ValidateE911AddressRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### StreetNumber
- **Type**: <class 'str'>
- **Required**: Yes

### StreetInfo
- **Type**: <class 'str'>
- **Required**: Yes

### City
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### PostalCode
- **Type**: <class 'str'>
- **Required**: Yes


# ValidateE911AddressResponse

### ValidationResult
- **Type**: <class 'int'>
- **Required**: Yes

### AddressExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.Address'>
- **Required**: Yes

### CandidateAddressList
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.CandidateAddress]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.ResponseMetadata'>
- **Required**: Yes


# VoiceConnector

### VoiceConnectorId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'us-east-1', 'us-west-2']]

### Name
- **Type**: typing.Optional[str]

### OutboundHostName
- **Type**: typing.Optional[str]

### RequireEncryption
- **Type**: typing.Optional[bool]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### VoiceConnectorArn
- **Type**: typing.Optional[str]

### IntegrationType
- **Type**: typing.Optional[typing.Literal['CONNECT_ANALYTICS_CONNECTOR', 'CONNECT_CALL_TRANSFER_CONNECTOR']]


# VoiceConnectorGroup

### VoiceConnectorGroupId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VoiceConnectorItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_classes.VoiceConnectorItem]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### VoiceConnectorGroupArn
- **Type**: typing.Optional[str]


# VoiceConnectorItem

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# VoiceConnectorSettings

### CdrBucket
- **Type**: typing.Optional[str]


# VoiceProfile

### VoiceProfileId
- **Type**: typing.Optional[str]

### VoiceProfileArn
- **Type**: typing.Optional[str]

### VoiceProfileDomainId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# VoiceProfileDomain

### VoiceProfileDomainId
- **Type**: typing.Optional[str]

### VoiceProfileDomainArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: <class 'NoneType'>

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# VoiceProfileDomainSummary

### VoiceProfileDomainId
- **Type**: typing.Optional[str]

### VoiceProfileDomainArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# VoiceProfileSummary

### VoiceProfileId
- **Type**: typing.Optional[str]

### VoiceProfileArn
- **Type**: typing.Optional[str]

### VoiceProfileDomainId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# VoiceToneAnalysisTask

### VoiceToneAnalysisTaskId
- **Type**: typing.Optional[str]

### VoiceToneAnalysisTaskStatus
- **Type**: typing.Optional[str]

### CallDetails
- **Type**: <class 'NoneType'>

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StartedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]



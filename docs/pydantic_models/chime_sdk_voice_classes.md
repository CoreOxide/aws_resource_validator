# Chime Sdk Voice Classes

# AddressTypeDef

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


# AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ForceAssociate
- **Type**: typing.Optional[bool]


# AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ForceAssociate
- **Type**: typing.Optional[bool]


# AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeletePhoneNumberRequestTypeDef

### PhoneNumberIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeletePhoneNumberResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdatePhoneNumberRequestTypeDef

### UpdatePhoneNumberRequestItems
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.UpdatePhoneNumberRequestItemTypeDef]
- **Required**: Yes


# BatchUpdatePhoneNumberResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CallDetailsTypeDef

### VoiceConnectorId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]

### IsCaller
- **Type**: typing.Optional[bool]


# CandidateAddressTypeDef

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


# CreatePhoneNumberOrderRequestTypeDef

### ProductType
- **Type**: typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# CreatePhoneNumberOrderResponseTypeDef

### PhoneNumberOrder
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberOrderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProxySessionRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantPhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Capabilities
- **Type**: typing.Sequence[typing.Literal['SMS', 'Voice']]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.GeoMatchParamsTypeDef]


# CreateProxySessionResponseTypeDef

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ProxySessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSipMediaApplicationCallRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ArgumentsMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSipMediaApplicationCallResponseTypeDef

### SipMediaApplicationCall
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationCallTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSipMediaApplicationRequestTypeDef

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationEndpointTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TagTypeDef]]


# CreateSipMediaApplicationResponseTypeDef

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSipRuleRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipRuleTargetApplicationTypeDef]]


# CreateSipRuleResponseTypeDef

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVoiceConnectorGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceConnectorItems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorItemTypeDef]]


# CreateVoiceConnectorGroupResponseTypeDef

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVoiceConnectorRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequireEncryption
- **Type**: <class 'bool'>
- **Required**: Yes

### AwsRegion
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'us-east-1', 'us-west-2']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TagTypeDef]]

### IntegrationType
- **Type**: typing.Optional[typing.Literal['CONNECT_ANALYTICS_CONNECTOR', 'CONNECT_CALL_TRANSFER_CONNECTOR']]


# CreateVoiceConnectorResponseTypeDef

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVoiceProfileDomainRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideEncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ServerSideEncryptionConfigurationTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TagTypeDef]]


# CreateVoiceProfileDomainResponseTypeDef

### VoiceProfileDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceProfileDomainTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVoiceProfileRequestTypeDef

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateVoiceProfileResponseTypeDef

### VoiceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CredentialTypeDef

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# DNISEmergencyCallingConfigurationTypeDef

### EmergencyPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### CallingCountry
- **Type**: <class 'str'>
- **Required**: Yes

### TestPhoneNumber
- **Type**: typing.Optional[str]


# DeletePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProxySessionRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSipMediaApplicationRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSipRuleRequestTypeDef

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorExternalSystemsConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorGroupRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorOriginationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorProxyRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorStreamingConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorTerminationCredentialsRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Usernames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteVoiceConnectorTerminationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceProfileDomainRequestTypeDef

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceProfileRequestTypeDef

### VoiceProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmergencyCallingConfigurationOutputTypeDef

### DNIS
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.DNISEmergencyCallingConfigurationTypeDef]]


# EmergencyCallingConfigurationTypeDef

### DNIS
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.DNISEmergencyCallingConfigurationTypeDef]]


# EmergencyCallingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExternalSystemsConfigurationTypeDef

### SessionBorderControllerTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIOCODES_MEDIANT_SBC', 'AVAYA_SBCE', 'CISCO_UNIFIED_BORDER_ELEMENT', 'ORACLE_ACME_PACKET_SBC', 'RIBBON_SBC']]]

### ContactCenterSystemTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AVAYA_AURA_CALL_CENTER_ELITE', 'AVAYA_AURA_CONTACT_CENTER', 'CISCO_UNIFIED_CONTACT_CENTER_ENTERPRISE', 'GENESYS_ENGAGE_ON_PREMISES']]]


# GeoMatchParamsTypeDef

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### AreaCode
- **Type**: <class 'str'>
- **Required**: Yes


# GetGlobalSettingsResponseTypeDef

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPhoneNumberOrderRequestTypeDef

### PhoneNumberOrderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPhoneNumberOrderResponseTypeDef

### PhoneNumberOrder
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberOrderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPhoneNumberResponseTypeDef

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPhoneNumberSettingsResponseTypeDef

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes

### CallingNameUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProxySessionRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProxySessionResponseTypeDef

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ProxySessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSipMediaApplicationAlexaSkillConfigurationRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef

### SipMediaApplicationAlexaSkillConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSipMediaApplicationLoggingConfigurationRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipMediaApplicationLoggingConfigurationResponseTypeDef

### SipMediaApplicationLoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationLoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSipMediaApplicationRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipMediaApplicationResponseTypeDef

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSipRuleRequestTypeDef

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipRuleResponseTypeDef

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSpeakerSearchTaskRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpeakerSearchTaskResponseTypeDef

### SpeakerSearchTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SpeakerSearchTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.EmergencyCallingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorExternalSystemsConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef

### ExternalSystemsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ExternalSystemsConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorGroupRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorGroupResponseTypeDef

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorLoggingConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorOriginationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorOriginationResponseTypeDef

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OriginationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorProxyRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorProxyResponseTypeDef

### Proxy
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ProxyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorResponseTypeDef

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorStreamingConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorStreamingConfigurationResponseTypeDef

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.StreamingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorTerminationHealthRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorTerminationHealthResponseTypeDef

### TerminationHealth
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TerminationHealthTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorTerminationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorTerminationResponseTypeDef

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TerminationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceProfileDomainRequestTypeDef

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceProfileDomainResponseTypeDef

### VoiceProfileDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceProfileDomainTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceProfileRequestTypeDef

### VoiceProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceProfileResponseTypeDef

### VoiceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceToneAnalysisTaskRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceToneAnalysisTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### IsCaller
- **Type**: <class 'bool'>
- **Required**: Yes


# GetVoiceToneAnalysisTaskResponseTypeDef

### VoiceToneAnalysisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceToneAnalysisTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAvailableVoiceConnectorRegionsResponseTypeDef

### VoiceConnectorRegions
- **Type**: typing.List[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'us-east-1', 'us-west-2']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPhoneNumberOrdersRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPhoneNumberOrdersResponseTypeDef

### PhoneNumberOrders
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberOrderTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersRequestTypeDef

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


# ListPhoneNumbersResponseTypeDef

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProxySessionsRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Closed', 'InProgress', 'Open']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProxySessionsResponseTypeDef

### ProxySessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ProxySessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSipMediaApplicationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PaginatorConfigTypeDef]


# ListSipMediaApplicationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSipMediaApplicationsResponseTypeDef

### SipMediaApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSipRulesRequestPaginateTypeDef

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PaginatorConfigTypeDef]


# ListSipRulesRequestTypeDef

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSipRulesResponseTypeDef

### SipRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedPhoneNumberCountriesRequestTypeDef

### ProductType
- **Type**: typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']
- **Required**: Yes


# ListSupportedPhoneNumberCountriesResponseTypeDef

### PhoneNumberCountries
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberCountryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVoiceConnectorGroupsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceConnectorGroupsResponseTypeDef

### VoiceConnectorGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVoiceConnectorTerminationCredentialsRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# ListVoiceConnectorTerminationCredentialsResponseTypeDef

### Usernames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVoiceConnectorsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceConnectorsResponseTypeDef

### VoiceConnectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVoiceProfileDomainsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceProfileDomainsResponseTypeDef

### VoiceProfileDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceProfileDomainSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVoiceProfilesRequestTypeDef

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceProfilesResponseTypeDef

### VoiceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoggingConfigurationTypeDef

### EnableSIPLogs
- **Type**: typing.Optional[bool]

### EnableMediaMetricLogs
- **Type**: typing.Optional[bool]


# MediaInsightsConfigurationTypeDef

### Disabled
- **Type**: typing.Optional[bool]

### ConfigurationArn
- **Type**: typing.Optional[str]


# OrderedPhoneNumberTypeDef

### E164PhoneNumber
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Acquired', 'Failed', 'Processing']]


# OriginationOutputTypeDef

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OriginationRouteTypeDef]]

### Disabled
- **Type**: typing.Optional[bool]


# OriginationRouteTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginationTypeDef

### Routes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OriginationRouteTypeDef]]

### Disabled
- **Type**: typing.Optional[bool]


# OriginationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipantTypeDef

### PhoneNumber
- **Type**: typing.Optional[str]

### ProxyPhoneNumber
- **Type**: typing.Optional[str]


# PhoneNumberAssociationTypeDef

### Value
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[typing.Literal['SipRuleId', 'VoiceConnectorGroupId', 'VoiceConnectorId']]

### AssociatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PhoneNumberCapabilitiesTypeDef

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


# PhoneNumberCountryTypeDef

### CountryCode
- **Type**: typing.Optional[str]

### SupportedPhoneNumberTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Local', 'TollFree']]]


# PhoneNumberErrorTypeDef

### PhoneNumberId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'Gone', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# PhoneNumberOrderTypeDef

### PhoneNumberOrderId
- **Type**: typing.Optional[str]

### ProductType
- **Type**: typing.Optional[typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']]

### Status
- **Type**: typing.Optional[typing.Literal['CancelRequested', 'Cancelled', 'ChangeRequested', 'Exception', 'FOC', 'Failed', 'Partial', 'PendingDocuments', 'Processing', 'Submitted', 'Successful']]

### OrderType
- **Type**: typing.Optional[typing.Literal['New', 'Porting']]

### OrderedPhoneNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OrderedPhoneNumberTypeDef]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PhoneNumberTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProxySessionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ParticipantTypeDef]]

### NumberSelectionBehavior
- **Type**: typing.Optional[typing.Literal['AvoidSticky', 'PreferSticky']]

### GeoMatchLevel
- **Type**: typing.Optional[typing.Literal['AreaCode', 'Country']]

### GeoMatchParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.GeoMatchParamsTypeDef]


# ProxyTypeDef

### DefaultSessionExpiryMinutes
- **Type**: typing.Optional[int]

### Disabled
- **Type**: typing.Optional[bool]

### FallBackPhoneNumber
- **Type**: typing.Optional[str]

### PhoneNumberCountries
- **Type**: typing.Optional[typing.List[str]]


# PutSipMediaApplicationAlexaSkillConfigurationRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SipMediaApplicationAlexaSkillConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfigurationUnionTypeDef]


# PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef

### SipMediaApplicationAlexaSkillConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutSipMediaApplicationLoggingConfigurationRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SipMediaApplicationLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationLoggingConfigurationTypeDef]


# PutSipMediaApplicationLoggingConfigurationResponseTypeDef

### SipMediaApplicationLoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationLoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.EmergencyCallingConfigurationUnionTypeDef'>
- **Required**: Yes


# PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.EmergencyCallingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorExternalSystemsConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionBorderControllerTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AUDIOCODES_MEDIANT_SBC', 'AVAYA_SBCE', 'CISCO_UNIFIED_BORDER_ELEMENT', 'ORACLE_ACME_PACKET_SBC', 'RIBBON_SBC']]]

### ContactCenterSystemTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AVAYA_AURA_CALL_CENTER_ELITE', 'AVAYA_AURA_CONTACT_CENTER', 'CISCO_UNIFIED_CONTACT_CENTER_ENTERPRISE', 'GENESYS_ENGAGE_ON_PREMISES']]]


# PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef

### ExternalSystemsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ExternalSystemsConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorLoggingConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorOriginationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OriginationUnionTypeDef'>
- **Required**: Yes


# PutVoiceConnectorOriginationResponseTypeDef

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OriginationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorProxyRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultSessionExpiryMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### PhoneNumberPoolCountries
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FallBackPhoneNumber
- **Type**: typing.Optional[str]

### Disabled
- **Type**: typing.Optional[bool]


# PutVoiceConnectorProxyResponseTypeDef

### Proxy
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ProxyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorStreamingConfigurationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.StreamingConfigurationUnionTypeDef'>
- **Required**: Yes


# PutVoiceConnectorStreamingConfigurationResponseTypeDef

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.StreamingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorTerminationCredentialsRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Credentials
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.CredentialTypeDef]]


# PutVoiceConnectorTerminationRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TerminationUnionTypeDef'>
- **Required**: Yes


# PutVoiceConnectorTerminationResponseTypeDef

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TerminationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
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


# RestorePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# RestorePhoneNumberResponseTypeDef

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchAvailablePhoneNumbersRequestTypeDef

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


# SearchAvailablePhoneNumbersResponseTypeDef

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ServerSideEncryptionConfigurationTypeDef

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# SipMediaApplicationAlexaSkillConfigurationOutputTypeDef

### AlexaSkillStatus
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### AlexaSkillIds
- **Type**: typing.List[str]
- **Required**: Yes


# SipMediaApplicationAlexaSkillConfigurationTypeDef

### AlexaSkillStatus
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### AlexaSkillIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SipMediaApplicationAlexaSkillConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SipMediaApplicationCallTypeDef

### TransactionId
- **Type**: typing.Optional[str]


# SipMediaApplicationEndpointTypeDef

### LambdaArn
- **Type**: typing.Optional[str]


# SipMediaApplicationLoggingConfigurationTypeDef

### EnableSipMediaApplicationMessageLogs
- **Type**: typing.Optional[bool]


# SipMediaApplicationTypeDef

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationEndpointTypeDef]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SipMediaApplicationArn
- **Type**: typing.Optional[str]


# SipRuleTargetApplicationTypeDef

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### AwsRegion
- **Type**: typing.Optional[str]


# SipRuleTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipRuleTargetApplicationTypeDef]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SpeakerSearchDetailsTypeDef

### Results
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SpeakerSearchResultTypeDef]]

### VoiceprintGenerationStatus
- **Type**: typing.Optional[str]


# SpeakerSearchResultTypeDef

### ConfidenceScore
- **Type**: typing.Optional[float]

### VoiceProfileId
- **Type**: typing.Optional[str]


# SpeakerSearchTaskTypeDef

### SpeakerSearchTaskId
- **Type**: typing.Optional[str]

### SpeakerSearchTaskStatus
- **Type**: typing.Optional[str]

### CallDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.CallDetailsTypeDef]

### SpeakerSearchDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SpeakerSearchDetailsTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StartedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]


# StartSpeakerSearchTaskRequestTypeDef

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


# StartSpeakerSearchTaskResponseTypeDef

### SpeakerSearchTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SpeakerSearchTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartVoiceToneAnalysisTaskRequestTypeDef

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


# StartVoiceToneAnalysisTaskResponseTypeDef

### VoiceToneAnalysisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceToneAnalysisTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopSpeakerSearchTaskRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StopVoiceToneAnalysisTaskRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceToneAnalysisTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StreamingConfigurationOutputTypeDef

### DataRetentionInHours
- **Type**: <class 'int'>
- **Required**: Yes

### Disabled
- **Type**: <class 'bool'>
- **Required**: Yes

### StreamingNotificationTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.StreamingNotificationTargetTypeDef]]

### MediaInsightsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.MediaInsightsConfigurationTypeDef]


# StreamingConfigurationTypeDef

### DataRetentionInHours
- **Type**: <class 'int'>
- **Required**: Yes

### Disabled
- **Type**: <class 'bool'>
- **Required**: Yes

### StreamingNotificationTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.StreamingNotificationTargetTypeDef]]

### MediaInsightsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.MediaInsightsConfigurationTypeDef]


# StreamingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StreamingNotificationTargetTypeDef

### NotificationTarget
- **Type**: typing.Optional[typing.Literal['EventBridge', 'SNS', 'SQS']]


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TerminationHealthTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Source
- **Type**: typing.Optional[str]


# TerminationOutputTypeDef

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


# TerminationTypeDef

### CpsLimit
- **Type**: typing.Optional[int]

### DefaultPhoneNumber
- **Type**: typing.Optional[str]

### CallingRegions
- **Type**: typing.Optional[typing.Sequence[str]]

### CidrAllowedList
- **Type**: typing.Optional[typing.Sequence[str]]

### Disabled
- **Type**: typing.Optional[bool]


# TerminationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGlobalSettingsRequestTypeDef

### VoiceConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorSettingsTypeDef]


# UpdatePhoneNumberRequestItemTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']]

### CallingName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdatePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['SipMediaApplicationDialIn', 'VoiceConnector']]

### CallingName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdatePhoneNumberResponseTypeDef

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePhoneNumberSettingsRequestTypeDef

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateProxySessionRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Sequence[typing.Literal['SMS', 'Voice']]
- **Required**: Yes

### ExpiryMinutes
- **Type**: typing.Optional[int]


# UpdateProxySessionResponseTypeDef

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ProxySessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSipMediaApplicationCallRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### Arguments
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UpdateSipMediaApplicationCallResponseTypeDef

### SipMediaApplicationCall
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationCallTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSipMediaApplicationRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationEndpointTypeDef]]


# UpdateSipMediaApplicationResponseTypeDef

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSipRuleRequestTypeDef

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]

### TargetApplications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipRuleTargetApplicationTypeDef]]


# UpdateSipRuleResponseTypeDef

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVoiceConnectorGroupRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceConnectorItems
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorItemTypeDef]
- **Required**: Yes


# UpdateVoiceConnectorGroupResponseTypeDef

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVoiceConnectorRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequireEncryption
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateVoiceConnectorResponseTypeDef

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVoiceProfileDomainRequestTypeDef

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateVoiceProfileDomainResponseTypeDef

### VoiceProfileDomain
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceProfileDomainTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVoiceProfileRequestTypeDef

### VoiceProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateVoiceProfileResponseTypeDef

### VoiceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateE911AddressRequestTypeDef

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


# ValidateE911AddressResponseTypeDef

### ValidationResult
- **Type**: <class 'int'>
- **Required**: Yes

### AddressExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.AddressTypeDef'>
- **Required**: Yes

### CandidateAddressList
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.CandidateAddressTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VoiceConnectorGroupTypeDef

### VoiceConnectorGroupId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VoiceConnectorItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorItemTypeDef]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### VoiceConnectorGroupArn
- **Type**: typing.Optional[str]


# VoiceConnectorItemTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# VoiceConnectorSettingsTypeDef

### CdrBucket
- **Type**: typing.Optional[str]


# VoiceConnectorTypeDef

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


# VoiceProfileDomainSummaryTypeDef

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


# VoiceProfileDomainTypeDef

### VoiceProfileDomainId
- **Type**: typing.Optional[str]

### VoiceProfileDomainArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ServerSideEncryptionConfigurationTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# VoiceProfileSummaryTypeDef

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


# VoiceProfileTypeDef

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


# VoiceToneAnalysisTaskTypeDef

### VoiceToneAnalysisTaskId
- **Type**: typing.Optional[str]

### VoiceToneAnalysisTaskStatus
- **Type**: typing.Optional[str]

### CallDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.CallDetailsTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StartedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]



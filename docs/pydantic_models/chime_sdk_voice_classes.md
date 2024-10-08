# Pydantic Models in chime_sdk_voice_classes

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


# AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef

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


# AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef

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

# BatchDeletePhoneNumberRequestRequestTypeDef

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


# BatchUpdatePhoneNumberRequestRequestTypeDef

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


# CreatePhoneNumberOrderRequestRequestTypeDef

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


# CreateProxySessionRequestRequestTypeDef

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


# CreateSipMediaApplicationCallRequestRequestTypeDef

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


# CreateSipMediaApplicationRequestRequestTypeDef

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


# CreateSipRuleRequestRequestTypeDef

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


# CreateVoiceConnectorGroupRequestRequestTypeDef

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


# CreateVoiceConnectorRequestRequestTypeDef

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


# CreateVoiceConnectorResponseTypeDef

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.VoiceConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVoiceProfileDomainRequestRequestTypeDef

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


# CreateVoiceProfileRequestRequestTypeDef

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


# DeletePhoneNumberRequestRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProxySessionRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSipMediaApplicationRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSipRuleRequestRequestTypeDef

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorGroupRequestRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorOriginationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorProxyRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Usernames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteVoiceConnectorTerminationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceProfileDomainRequestRequestTypeDef

### VoiceProfileDomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceProfileRequestRequestTypeDef

### VoiceProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef

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


# DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef

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


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# GetPhoneNumberOrderRequestRequestTypeDef

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


# GetPhoneNumberRequestRequestTypeDef

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


# GetProxySessionRequestRequestTypeDef

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


# GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef

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


# GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef

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


# GetSipMediaApplicationRequestRequestTypeDef

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


# GetSipRuleRequestRequestTypeDef

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


# GetSpeakerSearchTaskRequestRequestTypeDef

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


# GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef

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


# GetVoiceConnectorGroupRequestRequestTypeDef

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


# GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef

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


# GetVoiceConnectorOriginationRequestRequestTypeDef

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


# GetVoiceConnectorProxyRequestRequestTypeDef

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


# GetVoiceConnectorRequestRequestTypeDef

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


# GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef

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


# GetVoiceConnectorTerminationHealthRequestRequestTypeDef

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


# GetVoiceConnectorTerminationRequestRequestTypeDef

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


# GetVoiceProfileDomainRequestRequestTypeDef

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


# GetVoiceProfileRequestRequestTypeDef

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


# GetVoiceToneAnalysisTaskRequestRequestTypeDef

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


# ListPhoneNumberOrdersRequestRequestTypeDef

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


# ListPhoneNumbersRequestRequestTypeDef

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


# ListProxySessionsRequestRequestTypeDef

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


# ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PaginatorConfigTypeDef]


# ListSipMediaApplicationsRequestRequestTypeDef

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


# ListSipRulesRequestListSipRulesPaginateTypeDef

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PaginatorConfigTypeDef]


# ListSipRulesRequestRequestTypeDef

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


# ListSupportedPhoneNumberCountriesRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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


# ListVoiceConnectorGroupsRequestRequestTypeDef

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


# ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef

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


# ListVoiceConnectorsRequestRequestTypeDef

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


# ListVoiceProfileDomainsRequestRequestTypeDef

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


# ListVoiceProfilesRequestRequestTypeDef

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


# OriginationTypeDef

### Routes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OriginationRouteTypeDef]]

### Disabled
- **Type**: typing.Optional[bool]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberCapabilitiesTypeDef]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.PhoneNumberAssociationTypeDef]]

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


# PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SipMediaApplicationAlexaSkillConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfigurationTypeDef]


# PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef

### SipMediaApplicationAlexaSkillConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.SipMediaApplicationAlexaSkillConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef

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


# PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.EmergencyCallingConfigurationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.EmergencyCallingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef

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


# PutVoiceConnectorOriginationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OriginationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorOriginationResponseTypeDef

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.OriginationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorProxyRequestRequestTypeDef

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


# PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.StreamingConfigurationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorStreamingConfigurationResponseTypeDef

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.StreamingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Credentials
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_voice_classes.CredentialTypeDef]]


# PutVoiceConnectorTerminationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_voice_classes.TerminationTypeDef'>
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


# RestorePhoneNumberRequestRequestTypeDef

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


# SearchAvailablePhoneNumbersRequestRequestTypeDef

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


# StartSpeakerSearchTaskRequestRequestTypeDef

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


# StartVoiceToneAnalysisTaskRequestRequestTypeDef

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


# StopSpeakerSearchTaskRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StopVoiceToneAnalysisTaskRequestRequestTypeDef

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


# StreamingNotificationTargetTypeDef

### NotificationTarget
- **Type**: typing.Optional[typing.Literal['EventBridge', 'SNS', 'SQS']]


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGlobalSettingsRequestRequestTypeDef

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


# UpdatePhoneNumberRequestRequestTypeDef

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


# UpdatePhoneNumberSettingsRequestRequestTypeDef

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateProxySessionRequestRequestTypeDef

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


# UpdateSipMediaApplicationCallRequestRequestTypeDef

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


# UpdateSipMediaApplicationRequestRequestTypeDef

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


# UpdateSipRuleRequestRequestTypeDef

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


# UpdateVoiceConnectorGroupRequestRequestTypeDef

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


# UpdateVoiceConnectorRequestRequestTypeDef

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


# UpdateVoiceProfileDomainRequestRequestTypeDef

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


# UpdateVoiceProfileRequestRequestTypeDef

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


# ValidateE911AddressRequestRequestTypeDef

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



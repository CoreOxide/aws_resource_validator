# sms_voice_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CallInstructionsMessageTypeTypeDef

### Text
- **Type**: typing.Optional[str]


# CloudWatchLogsDestinationTypeDef

### IamRoleArn
- **Type**: typing.Optional[str]

### LogGroupArn
- **Type**: typing.Optional[str]


# CreateConfigurationSetEventDestinationRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.EventDestinationDefinitionTypeDef]

### EventDestinationName
- **Type**: typing.Optional[str]


# CreateConfigurationSetRequestRequestTypeDef

### ConfigurationSetName
- **Type**: typing.Optional[str]


# DeleteConfigurationSetEventDestinationRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationSetRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# EventDestinationDefinitionTypeDef

### CloudWatchLogsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.CloudWatchLogsDestinationTypeDef]

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.KinesisFirehoseDestinationTypeDef]

### MatchingEventTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ANSWERED', 'BUSY', 'COMPLETED_CALL', 'FAILED', 'INITIATED_CALL', 'NO_ANSWER', 'RINGING']]]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.SnsDestinationTypeDef]


# EventDestinationTypeDef

### CloudWatchLogsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.CloudWatchLogsDestinationTypeDef]

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.KinesisFirehoseDestinationTypeDef]

### MatchingEventTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ANSWERED', 'BUSY', 'COMPLETED_CALL', 'FAILED', 'INITIATED_CALL', 'NO_ANSWER', 'RINGING']]]

### Name
- **Type**: typing.Optional[str]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.SnsDestinationTypeDef]


# GetConfigurationSetEventDestinationsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsResponseTypeDef

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_voice_classes.EventDestinationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KinesisFirehoseDestinationTypeDef

### DeliveryStreamArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# ListConfigurationSetsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]


# ListConfigurationSetsResponseTypeDef

### ConfigurationSets
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PlainTextMessageTypeTypeDef

### LanguageCode
- **Type**: typing.Optional[str]

### Text
- **Type**: typing.Optional[str]

### VoiceId
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# SSMLMessageTypeTypeDef

### LanguageCode
- **Type**: typing.Optional[str]

### Text
- **Type**: typing.Optional[str]

### VoiceId
- **Type**: typing.Optional[str]


# SendVoiceMessageRequestRequestTypeDef

### CallerId
- **Type**: typing.Optional[str]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.VoiceMessageContentTypeDef]

### DestinationPhoneNumber
- **Type**: typing.Optional[str]

### OriginationPhoneNumber
- **Type**: typing.Optional[str]


# SendVoiceMessageResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SnsDestinationTypeDef

### TopicArn
- **Type**: typing.Optional[str]


# UpdateConfigurationSetEventDestinationRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.EventDestinationDefinitionTypeDef]


# VoiceMessageContentTypeDef

### CallInstructionsMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.CallInstructionsMessageTypeTypeDef]

### PlainTextMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.PlainTextMessageTypeTypeDef]

### SSMLMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice_classes.SSMLMessageTypeTypeDef]



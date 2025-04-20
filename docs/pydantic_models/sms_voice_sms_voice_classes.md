# Sms Voice Sms Voice Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CallInstructionsMessageType

### Text
- **Type**: typing.Optional[str]


# CloudWatchLogsDestination

### IamRoleArn
- **Type**: typing.Optional[str]

### LogGroupArn
- **Type**: typing.Optional[str]


# CreateConfigurationSetEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.EventDestinationDefinition]

### EventDestinationName
- **Type**: typing.Optional[str]


# CreateConfigurationSetRequest

### ConfigurationSetName
- **Type**: typing.Optional[str]


# DeleteConfigurationSetEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationSetRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# EventDestination

### CloudWatchLogsDestination
- **Type**: <class 'NoneType'>

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### MatchingEventTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ANSWERED', 'BUSY', 'COMPLETED_CALL', 'FAILED', 'INITIATED_CALL', 'NO_ANSWER', 'RINGING']]]

### Name
- **Type**: typing.Optional[str]

### SnsDestination
- **Type**: <class 'NoneType'>


# EventDestinationDefinition

### CloudWatchLogsDestination
- **Type**: <class 'NoneType'>

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### MatchingEventTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ANSWERED', 'BUSY', 'COMPLETED_CALL', 'FAILED', 'INITIATED_CALL', 'NO_ANSWER', 'RINGING']]]

### SnsDestination
- **Type**: <class 'NoneType'>


# GetConfigurationSetEventDestinationsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsResponse

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.EventDestination]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.ResponseMetadata'>
- **Required**: Yes


# KinesisFirehoseDestination

### DeliveryStreamArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# ListConfigurationSetsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]


# ListConfigurationSetsResponse

### ConfigurationSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PlainTextMessageType

### LanguageCode
- **Type**: typing.Optional[str]

### Text
- **Type**: typing.Optional[str]

### VoiceId
- **Type**: typing.Optional[str]


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


# SSMLMessageType

### LanguageCode
- **Type**: typing.Optional[str]

### Text
- **Type**: typing.Optional[str]

### VoiceId
- **Type**: typing.Optional[str]


# SendVoiceMessageRequest

### CallerId
- **Type**: typing.Optional[str]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.VoiceMessageContent]

### DestinationPhoneNumber
- **Type**: typing.Optional[str]

### OriginationPhoneNumber
- **Type**: typing.Optional[str]


# SendVoiceMessageResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.ResponseMetadata'>
- **Required**: Yes


# SnsDestination

### TopicArn
- **Type**: typing.Optional[str]


# UpdateConfigurationSetEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.EventDestinationDefinition]


# VoiceMessageContent

### CallInstructionsMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.CallInstructionsMessageType]

### PlainTextMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.PlainTextMessageType]

### SSMLMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_voice.sms_voice_classes.SSMLMessageType]



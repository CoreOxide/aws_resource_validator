# Pinpoint Sms Voice Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CallInstructionsMessageTypeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsDestinationTypeDef

### IamRoleArn
- **Type**: typing.Optional[str]

### LogGroupArn
- **Type**: typing.Optional[str]


# CreateConfigurationSetEventDestinationRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.EventDestinationDefinitionTypeDef]

### EventDestinationName
- **Type**: typing.Optional[str]


# CreateConfigurationSetRequestTypeDef

### ConfigurationSetName
- **Type**: typing.Optional[str]


# DeleteConfigurationSetEventDestinationRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationSetRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# EventDestinationDefinitionTypeDef

### CloudWatchLogsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.CloudWatchLogsDestinationTypeDef]

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.KinesisFirehoseDestinationTypeDef]

### MatchingEventTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ANSWERED', 'BUSY', 'COMPLETED_CALL', 'FAILED', 'INITIATED_CALL', 'NO_ANSWER', 'RINGING']]]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.SnsDestinationTypeDef]


# EventDestinationTypeDef

### CloudWatchLogsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.CloudWatchLogsDestinationTypeDef]

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.KinesisFirehoseDestinationTypeDef]

### MatchingEventTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ANSWERED', 'BUSY', 'COMPLETED_CALL', 'FAILED', 'INITIATED_CALL', 'NO_ANSWER', 'RINGING']]]

### Name
- **Type**: typing.Optional[str]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.SnsDestinationTypeDef]


# GetConfigurationSetEventDestinationsRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsResponseTypeDef

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.EventDestinationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KinesisFirehoseDestinationTypeDef

### DeliveryStreamArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# PlainTextMessageTypeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SSMLMessageTypeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SendVoiceMessageRequestTypeDef

### CallerId
- **Type**: typing.Optional[str]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.VoiceMessageContentTypeDef]

### DestinationPhoneNumber
- **Type**: typing.Optional[str]

### OriginationPhoneNumber
- **Type**: typing.Optional[str]


# SendVoiceMessageResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SnsDestinationTypeDef

### TopicArn
- **Type**: typing.Optional[str]


# UpdateConfigurationSetEventDestinationRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.EventDestinationDefinitionTypeDef]


# VoiceMessageContentTypeDef

### CallInstructionsMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.CallInstructionsMessageTypeTypeDef]

### PlainTextMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.PlainTextMessageTypeTypeDef]

### SSMLMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_classes.SSMLMessageTypeTypeDef]



# Lexv2 Runtime Classes

# AccessDeniedExceptionTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# ActiveContextOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextTimeToLiveTypeDef'>
- **Required**: Yes

### contextAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# ActiveContextTimeToLiveTypeDef

### timeToLiveInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### turnsToLive
- **Type**: <class 'int'>
- **Required**: Yes


# ActiveContextTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextTimeToLiveTypeDef'>
- **Required**: Yes

### contextAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ActiveContextUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudioInputEventTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### audioChunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.BlobTypeDef]

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# AudioResponseEventTypeDef

### audioChunk
- **Type**: typing.Optional[bytes]

### contentType
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]


# BadGatewayExceptionTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ButtonTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ConfidenceScoreTypeDef

### score
- **Type**: typing.Optional[float]


# ConfigurationEventTypeDef

### responseContentType
- **Type**: <class 'str'>
- **Required**: Yes

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateUnionTypeDef]

### welcomeMessages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageUnionTypeDef]]

### disablePlayback
- **Type**: typing.Optional[bool]

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# ConflictExceptionTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# DTMFInputEventTypeDef

### inputCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# DeleteSessionRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSessionResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DependencyFailedExceptionTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# DialogActionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DialogActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisconnectionEventTypeDef

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# ElicitSubSlotOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subSlotToElicit
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ElicitSubSlotTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subSlotToElicit
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# GetSessionRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponseTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageOutputTypeDef]
- **Required**: Yes

### interpretations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.InterpretationTypeDef]
- **Required**: Yes

### sessionState
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HeartbeatEventTypeDef

### eventId
- **Type**: typing.Optional[str]


# ImageResponseCardOutputTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ButtonTypeDef]]


# ImageResponseCardTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ButtonTypeDef]]


# ImageResponseCardUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntentOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.SlotOutputTypeDef]]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'FulfillmentInProgress', 'InProgress', 'ReadyForFulfillment', 'Waiting']]

### confirmationState
- **Type**: typing.Optional[typing.Literal['Confirmed', 'Denied', 'None']]


# IntentResultEventTypeDef

### inputMode
- **Type**: typing.Optional[typing.Literal['DTMF', 'Speech', 'Text']]

### interpretations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.InterpretationTypeDef]]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateOutputTypeDef]

### requestAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### sessionId
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]

### recognizedBotMember
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RecognizedBotMemberTypeDef]


# IntentTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.SlotUnionTypeDef]]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'FulfillmentInProgress', 'InProgress', 'ReadyForFulfillment', 'Waiting']]

### confirmationState
- **Type**: typing.Optional[typing.Literal['Confirmed', 'Denied', 'None']]


# IntentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InternalServerExceptionTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# InterpretationTypeDef

### nluConfidence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ConfidenceScoreTypeDef]

### sentimentResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SentimentResponseTypeDef]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentOutputTypeDef]

### interpretationSource
- **Type**: typing.Optional[typing.Literal['Bedrock', 'Lex']]


# MessageOutputTypeDef

### contentType
- **Type**: typing.Literal['CustomPayload', 'ImageResponseCard', 'PlainText', 'SSML']
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ImageResponseCardOutputTypeDef]


# MessageTypeDef

### contentType
- **Type**: typing.Literal['CustomPayload', 'ImageResponseCard', 'PlainText', 'SSML']
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ImageResponseCardUnionTypeDef]


# MessageUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PlaybackCompletionEventTypeDef

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# PlaybackInterruptionEventTypeDef

### eventReason
- **Type**: typing.Optional[typing.Literal['DTMF_START_DETECTED', 'TEXT_DETECTED', 'VOICE_START_DETECTED']]

### causedByEventId
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]


# PutSessionRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateUnionTypeDef'>
- **Required**: Yes

### messages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageUnionTypeDef]]

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### responseContentType
- **Type**: typing.Optional[str]


# PutSessionResponseTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: <class 'str'>
- **Required**: Yes

### requestAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### audioStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecognizeTextRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### text
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateUnionTypeDef]

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RecognizeTextResponseTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageOutputTypeDef]
- **Required**: Yes

### sessionState
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateOutputTypeDef'>
- **Required**: Yes

### interpretations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.InterpretationTypeDef]
- **Required**: Yes

### requestAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### recognizedBotMember
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.RecognizedBotMemberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecognizeUtteranceRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### requestContentType
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: typing.Optional[str]

### requestAttributes
- **Type**: typing.Optional[str]

### responseContentType
- **Type**: typing.Optional[str]

### inputStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.BlobTypeDef]


# RecognizeUtteranceResponseTypeDef

### inputMode
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: <class 'str'>
- **Required**: Yes

### interpretations
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: <class 'str'>
- **Required**: Yes

### requestAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### inputTranscript
- **Type**: <class 'str'>
- **Required**: Yes

### audioStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### recognizedBotMember
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecognizedBotMemberTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: typing.Optional[str]


# ResourceNotFoundExceptionTypeDef

### message
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


# RuntimeHintDetailsOutputTypeDef

### runtimeHintValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintValueTypeDef]]

### subSlotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# RuntimeHintDetailsTypeDef

### runtimeHintValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintValueTypeDef]]

### subSlotHints
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


# RuntimeHintDetailsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuntimeHintValueTypeDef

### phrase
- **Type**: <class 'str'>
- **Required**: Yes


# RuntimeHintsOutputTypeDef

### slotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintDetailsOutputTypeDef]]]


# RuntimeHintsTypeDef

### slotHints
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintDetailsUnionTypeDef]]]


# RuntimeHintsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SentimentResponseTypeDef

### sentiment
- **Type**: typing.Optional[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]

### sentimentScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SentimentScoreTypeDef]


# SentimentScoreTypeDef

### positive
- **Type**: typing.Optional[float]

### negative
- **Type**: typing.Optional[float]

### neutral
- **Type**: typing.Optional[float]

### mixed
- **Type**: typing.Optional[float]


# SessionStateOutputTypeDef

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.DialogActionOutputTypeDef]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentOutputTypeDef]

### activeContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextOutputTypeDef]]

### sessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### originatingRequestId
- **Type**: typing.Optional[str]

### runtimeHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintsOutputTypeDef]


# SessionStateTypeDef

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.DialogActionUnionTypeDef]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentUnionTypeDef]

### activeContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextUnionTypeDef]]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### originatingRequestId
- **Type**: typing.Optional[str]

### runtimeHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintsUnionTypeDef]


# SessionStateUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SlotOutputTypeDef

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ValueOutputTypeDef]

### shape
- **Type**: typing.Optional[typing.Literal['Composite', 'List', 'Scalar']]

### values
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### subSlots
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# SlotTypeDef

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ValueUnionTypeDef]

### shape
- **Type**: typing.Optional[typing.Literal['Composite', 'List', 'Scalar']]

### values
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### subSlots
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


# SlotUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartConversationRequestEventStreamTypeDef

### ConfigurationEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ConfigurationEventTypeDef]

### AudioInputEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.AudioInputEventTypeDef]

### DTMFInputEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.DTMFInputEventTypeDef]

### TextInputEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.TextInputEventTypeDef]

### PlaybackCompletionEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.PlaybackCompletionEventTypeDef]

### DisconnectionEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.DisconnectionEventTypeDef]


# StartConversationRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### requestEventStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.lexv2_runtime_classes.StartConversationRequestEventStreamTypeDef]
- **Required**: Yes

### conversationMode
- **Type**: typing.Optional[typing.Literal['AUDIO', 'TEXT']]


# StartConversationResponseEventStreamTypeDef

### PlaybackInterruptionEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.PlaybackInterruptionEventTypeDef]

### TranscriptEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.TranscriptEventTypeDef]

### IntentResultEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentResultEventTypeDef]

### TextResponseEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.TextResponseEventTypeDef]

### AudioResponseEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.AudioResponseEventTypeDef]

### HeartbeatEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.HeartbeatEventTypeDef]

### AccessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.AccessDeniedExceptionTypeDef]

### ResourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResourceNotFoundExceptionTypeDef]

### ValidationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ValidationExceptionTypeDef]

### ThrottlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ThrottlingExceptionTypeDef]

### InternalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.InternalServerExceptionTypeDef]

### ConflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ConflictExceptionTypeDef]

### DependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.DependencyFailedExceptionTypeDef]

### BadGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.BadGatewayExceptionTypeDef]


# StartConversationResponseTypeDef

### responseEventStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.lexv2_runtime_classes.StartConversationResponseEventStreamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TextInputEventTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# TextResponseEventTypeDef

### messages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageOutputTypeDef]]

### eventId
- **Type**: typing.Optional[str]


# ThrottlingExceptionTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# TranscriptEventTypeDef

### transcript
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]


# ValidationExceptionTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes


# ValueOutputTypeDef

### interpretedValue
- **Type**: <class 'str'>
- **Required**: Yes

### originalValue
- **Type**: typing.Optional[str]

### resolvedValues
- **Type**: typing.Optional[typing.List[str]]


# ValueTypeDef

### interpretedValue
- **Type**: <class 'str'>
- **Required**: Yes

### originalValue
- **Type**: typing.Optional[str]

### resolvedValues
- **Type**: typing.Optional[typing.Sequence[str]]


# ValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


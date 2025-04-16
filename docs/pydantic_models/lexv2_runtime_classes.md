# Lexv2 Runtime Classes

# AccessDeniedException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# ActiveContext

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextTimeToLive'>
- **Required**: Yes

### contextAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ActiveContextOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextTimeToLive'>
- **Required**: Yes

### contextAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# ActiveContextTimeToLive

### timeToLiveInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### turnsToLive
- **Type**: <class 'int'>
- **Required**: Yes


# ActiveContextUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudioInputEvent

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### audioChunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.Blob]

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# AudioResponseEvent

### audioChunk
- **Type**: typing.Optional[bytes]

### contentType
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]


# BadGatewayException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Button

### text
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ConfidenceScore

### score
- **Type**: typing.Optional[float]


# ConfigurationEvent

### responseContentType
- **Type**: <class 'str'>
- **Required**: Yes

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateUnion]

### welcomeMessages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageUnion]]

### disablePlayback
- **Type**: typing.Optional[bool]

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# ConflictException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# DTMFInputEvent

### inputCharacter
- **Type**: <class 'str'>
- **Required**: Yes

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# DeleteSessionRequest

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


# DeleteSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# DependencyFailedException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# DialogActionOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DialogActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisconnectionEvent

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# ElicitSubSlot

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subSlotToElicit
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ElicitSubSlotOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subSlotToElicit
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# GetSessionRequest

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


# GetSessionResponse

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageOutput]
- **Required**: Yes

### interpretations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.Interpretation]
- **Required**: Yes

### sessionState
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# HeartbeatEvent

### eventId
- **Type**: typing.Optional[str]


# ImageResponseCard

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.Button]]


# ImageResponseCardOutput

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.Button]]


# ImageResponseCardUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Intent

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.SlotUnion]]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'FulfillmentInProgress', 'InProgress', 'ReadyForFulfillment', 'Waiting']]

### confirmationState
- **Type**: typing.Optional[typing.Literal['Confirmed', 'Denied', 'None']]


# IntentOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.SlotOutput]]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'FulfillmentInProgress', 'InProgress', 'ReadyForFulfillment', 'Waiting']]

### confirmationState
- **Type**: typing.Optional[typing.Literal['Confirmed', 'Denied', 'None']]


# IntentResultEvent

### inputMode
- **Type**: typing.Optional[typing.Literal['DTMF', 'Speech', 'Text']]

### interpretations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.Interpretation]]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateOutput]

### requestAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### sessionId
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]

### recognizedBotMember
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RecognizedBotMember]


# IntentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InternalServerException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# Interpretation

### nluConfidence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ConfidenceScore]

### sentimentResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SentimentResponse]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentOutput]

### interpretationSource
- **Type**: typing.Optional[typing.Literal['Bedrock', 'Lex']]


# Message

### contentType
- **Type**: typing.Literal['CustomPayload', 'ImageResponseCard', 'PlainText', 'SSML']
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ImageResponseCardUnion]


# MessageOutput

### contentType
- **Type**: typing.Literal['CustomPayload', 'ImageResponseCard', 'PlainText', 'SSML']
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ImageResponseCardOutput]


# MessageUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PlaybackCompletionEvent

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# PlaybackInterruptionEvent

### eventReason
- **Type**: typing.Optional[typing.Literal['DTMF_START_DETECTED', 'TEXT_DETECTED', 'VOICE_START_DETECTED']]

### causedByEventId
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]


# PutSessionRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateUnion'>
- **Required**: Yes

### messages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageUnion]]

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### responseContentType
- **Type**: typing.Optional[str]


# PutSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# RecognizeTextRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateUnion]

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RecognizeTextResponse

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageOutput]
- **Required**: Yes

### sessionState
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateOutput'>
- **Required**: Yes

### interpretations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.Interpretation]
- **Required**: Yes

### requestAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### recognizedBotMember
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.RecognizedBotMember'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# RecognizeUtteranceRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.Blob]


# RecognizeUtteranceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# RecognizedBotMember

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: typing.Optional[str]


# ResourceNotFoundException

### message
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


# RuntimeHintDetails

### runtimeHintValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintValue]]

### subSlotHints
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


# RuntimeHintDetailsOutput

### runtimeHintValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintValue]]

### subSlotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# RuntimeHintDetailsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuntimeHintValue

### phrase
- **Type**: <class 'str'>
- **Required**: Yes


# RuntimeHints

### slotHints
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintDetailsUnion]]]


# RuntimeHintsOutput

### slotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintDetailsOutput]]]


# RuntimeHintsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SentimentResponse

### sentiment
- **Type**: typing.Optional[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]

### sentimentScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SentimentScore]


# SentimentScore

### positive
- **Type**: typing.Optional[float]

### negative
- **Type**: typing.Optional[float]

### neutral
- **Type**: typing.Optional[float]

### mixed
- **Type**: typing.Optional[float]


# SessionState

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.DialogActionUnion]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentUnion]

### activeContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextUnion]]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### originatingRequestId
- **Type**: typing.Optional[str]

### runtimeHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintsUnion]


# SessionStateOutput

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.DialogActionOutput]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentOutput]

### activeContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextOutput]]

### sessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### originatingRequestId
- **Type**: typing.Optional[str]

### runtimeHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintsOutput]


# SessionStateUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Slot

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ValueUnion]

### shape
- **Type**: typing.Optional[typing.Literal['Composite', 'List', 'Scalar']]

### values
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### subSlots
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


# SlotOutput

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ValueOutput]

### shape
- **Type**: typing.Optional[typing.Literal['Composite', 'List', 'Scalar']]

### values
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### subSlots
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# SlotUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartConversationRequest

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
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.lexv2_runtime_classes.StartConversationRequestEventStream]
- **Required**: Yes

### conversationMode
- **Type**: typing.Optional[typing.Literal['AUDIO', 'TEXT']]


# StartConversationRequestEventStream

### ConfigurationEvent
- **Type**: <class 'NoneType'>

### AudioInputEvent
- **Type**: <class 'NoneType'>

### DTMFInputEvent
- **Type**: <class 'NoneType'>

### TextInputEvent
- **Type**: <class 'NoneType'>

### PlaybackCompletionEvent
- **Type**: <class 'NoneType'>

### DisconnectionEvent
- **Type**: <class 'NoneType'>


# StartConversationResponse

### responseEventStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.lexv2_runtime_classes.StartConversationResponseEventStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# StartConversationResponseEventStream

### PlaybackInterruptionEvent
- **Type**: <class 'NoneType'>

### TranscriptEvent
- **Type**: <class 'NoneType'>

### IntentResultEvent
- **Type**: <class 'NoneType'>

### TextResponseEvent
- **Type**: <class 'NoneType'>

### AudioResponseEvent
- **Type**: <class 'NoneType'>

### HeartbeatEvent
- **Type**: <class 'NoneType'>

### AccessDeniedException
- **Type**: <class 'NoneType'>

### ResourceNotFoundException
- **Type**: <class 'NoneType'>

### ValidationException
- **Type**: <class 'NoneType'>

### ThrottlingException
- **Type**: <class 'NoneType'>

### InternalServerException
- **Type**: <class 'NoneType'>

### ConflictException
- **Type**: <class 'NoneType'>

### DependencyFailedException
- **Type**: <class 'NoneType'>

### BadGatewayException
- **Type**: <class 'NoneType'>


# TextInputEvent

### text
- **Type**: <class 'str'>
- **Required**: Yes

### eventId
- **Type**: typing.Optional[str]

### clientTimestampMillis
- **Type**: typing.Optional[int]


# TextResponseEvent

### messages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageOutput]]

### eventId
- **Type**: typing.Optional[str]


# ThrottlingException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# TranscriptEvent

### transcript
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]


# ValidationException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# Value

### interpretedValue
- **Type**: <class 'str'>
- **Required**: Yes

### originalValue
- **Type**: typing.Optional[str]

### resolvedValues
- **Type**: typing.Optional[typing.Sequence[str]]


# ValueOutput

### interpretedValue
- **Type**: <class 'str'>
- **Required**: Yes

### originalValue
- **Type**: typing.Optional[str]

### resolvedValues
- **Type**: typing.Optional[typing.List[str]]


# ValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

